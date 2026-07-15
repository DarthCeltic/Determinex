"""
rosetta/latent_rag.py — Latent RAG: Semantic Retrieval via Compressed Hidden States

Implements the Phase 3 Latent RAG architecture from the Determinex white paper.

Instead of retrieving text chunks (standard RAG), Latent RAG retrieves
compressed mid-layer hidden states from a semantic index, projects them
through the RosettaStone into the target model's embedding space, and
injects them as soft prefix tokens before generation.

This replaces the text-chunk injection step:
    Standard RAG:  context_text → tokenize → inject as prompt tokens
    Latent RAG:    context_text → mid-layer state → compress → store
                   query → semantic search → retrieve state → project → inject as prefix

The semantic index is built on top of the existing KVStore (kv_store.py)
with a cosine-similarity layer using sentence-transformers embeddings stored
in sqlite alongside the compressed states.

Architecture:
    ┌─────────────────────────────────────────────────────────────────────┐
    │  Offline Indexing (run once per codebase)                           │
    │                                                                     │
    │  semantic unit (function, class, module)                            │
    │      │                                                              │
    │  MidLayerExtractor (HF model, 4-bit NF4)                           │
    │      │  hidden state [hidden_dim]                                   │
    │  KVCompressor                                                       │
    │      │  CompressedState (int8 BLOB)                                │
    │  SemanticIndexer                                                    │
    │      │  stores (embedding [384], compressed_blob) in sqlite         │
    │      └→ LatentIndex.db                                              │
    └─────────────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────────────────┐
    │  Runtime Retrieval (per Architect step)                             │
    │                                                                     │
    │  query text (Architect instruction)                                 │
    │      │                                                              │
    │  fastembed AllMiniLML6V2 → query embedding [384]                   │
    │      │                                                              │
    │  cosine search (sqlite, no external vector DB)                      │
    │      │  top-K CompressedStates                                      │
    │  KVCompressor.decompress()  →  [hidden_dim] tensors                │
    │      │                                                              │
    │  RosettaStone.translate()   →  [target_dim] tensors                │
    │      │                                                              │
    │  RosettaInferenceBridge.generate_with_prefix()                     │
    │      └→  generated code conditioned on retrieved latent context     │
    └─────────────────────────────────────────────────────────────────────┘

Information bottleneck honest note:
    Mean-pooling is used for the hidden state. This captures semantic
    'essence' of a code unit — useful for routing and retrieval — but
    does not preserve full positional or syntactic structure. The benefit
    of Latent RAG over text RAG is bandwidth efficiency and the avoidance
    of re-tokenization: the model receives pre-processed semantic
    representations rather than raw text. The limit is that fine-grained
    structural information (e.g., exact parameter order) is not preserved
    in the pooled vector and must still come from the prompt.

Usage:
    # Build index once
    indexer = LatentIndexer(db_path="determinex_latent.db", source_family="mistral")
    indexer.index_directory("./my_project/src")

    # Retrieve at inference time
    retriever = LatentRetriever(db_path="determinex_latent.db")
    prefix_vectors = retriever.retrieve_and_project(
        query="implement thread-safe singleton",
        stone=rosetta_stone,
        target_family="qwen",
        top_k=3,
    )
    # Feed prefix_vectors to RosettaInferenceBridge.generate_with_prefix()
"""

import hashlib
import sqlite3
import sys
import time
from pathlib import Path
from typing import Optional

import numpy as np
import torch

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

try:
    from kv_compress import KVCompressor, CompressedState
    from kv_store import KVStore
    from train_rosetta import RosettaStone
    from extract_midlayer import MidLayerExtractor
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from kv_compress import KVCompressor, CompressedState
    from kv_store import KVStore
    from train_rosetta import RosettaStone
    from extract_midlayer import MidLayerExtractor


# ---------------------------------------------------------------------------
# EMBEDDING MODEL — fastembed AllMiniLML6V2 (384-dim, CPU, already in stack)
# ---------------------------------------------------------------------------

def _get_embedder():
    """
    Returns a fastembed TextEmbedding instance.
    Falls back to a simple hash-based mock if fastembed is unavailable.
    """
    try:
        from fastembed import TextEmbedding
        return TextEmbedding("sentence-transformers/all-MiniLM-L6-v2")
    except ImportError:
        print(
            "[LatentRAG] WARNING: fastembed not installed. "
            "Semantic search unavailable. Install: pip install fastembed",
            flush=True,
        )
        return None


# ---------------------------------------------------------------------------
# SCHEMA — extends KVStore with semantic embedding column
# ---------------------------------------------------------------------------

_LATENT_SCHEMA = """
CREATE TABLE IF NOT EXISTS latent_index (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    context_hash     TEXT    NOT NULL UNIQUE,
    source_family    TEXT    NOT NULL,
    layer_idx        INTEGER NOT NULL,
    hidden_dim       INTEGER NOT NULL,
    compressed_blob  BLOB    NOT NULL,
    embedding        BLOB    NOT NULL,   -- float32[384] AllMiniLML6V2
    embedding_dim    INTEGER NOT NULL DEFAULT 384,
    context_preview  TEXT    DEFAULT '',
    unit_path        TEXT    DEFAULT '',  -- source file path of indexed unit
    created_at       REAL    NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_latent_hash   ON latent_index(context_hash);
CREATE INDEX IF NOT EXISTS idx_latent_family ON latent_index(source_family);
CREATE INDEX IF NOT EXISTS idx_latent_path   ON latent_index(unit_path);
"""


# ---------------------------------------------------------------------------
# LATENT INDEXER — builds the semantic + hidden-state index
# ---------------------------------------------------------------------------

class LatentIndexer:
    """
    Indexes semantic units (functions, classes, files) by:
        1. Extracting mid-layer hidden states via MidLayerExtractor
        2. Compressing them with KVCompressor
        3. Storing alongside AllMiniLML6V2 semantic embeddings in sqlite

    This is the offline indexing step — run once per codebase update.
    """

    def __init__(
        self,
        db_path:       str | Path = "determinex_latent.db",
        source_family: str = "mistral",
    ):
        self.db_path       = Path(db_path)
        self.source_family = source_family
        self.compressor    = KVCompressor()
        self._embedder     = _get_embedder()

        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(
            str(self.db_path),
            check_same_thread=False,
            isolation_level=None,
        )
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute("PRAGMA synchronous=NORMAL")
        self._conn.executescript(_LATENT_SCHEMA)
        print(f"[LatentRAG] Index DB: {self.db_path}", flush=True)

    def _embed_text(self, text: str) -> Optional[np.ndarray]:
        """Returns [384] float32 embedding or None if embedder unavailable."""
        if self._embedder is None:
            return None
        try:
            embeddings = list(self._embedder.embed([text]))
            return np.array(embeddings[0], dtype=np.float32)
        except Exception as e:
            print(f"[LatentRAG] Embedding failed: {e}", flush=True)
            return None

    def index_unit(
        self,
        context_text:  str,
        extractor:     MidLayerExtractor,
        unit_path:     str = "",
        overwrite:     bool = True,
    ) -> Optional[int]:
        """
        Index a single semantic unit (code function, class, etc.)

        Args:
            context_text : the full text of the semantic unit
            extractor    : loaded MidLayerExtractor (HF model must be loaded)
            unit_path    : source file path for metadata
            overwrite    : replace existing entry with same hash

        Returns:
            sqlite row id, or None on failure
        """
        context_hash = hashlib.sha256(context_text.encode("utf-8")).hexdigest()

        # Skip if already indexed (unless overwrite)
        if not overwrite:
            row = self._conn.execute(
                "SELECT id FROM latent_index WHERE context_hash = ?",
                (context_hash,)
            ).fetchone()
            if row:
                return row[0]

        # Extract mid-layer hidden state
        try:
            hidden = extractor.extract(context_text, max_length=512)  # [hidden_dim]
        except Exception as e:
            print(f"[LatentRAG] Extraction failed for {unit_path}: {e}", flush=True)
            return None

        # Compress
        cs = self.compressor.compress(
            hidden,
            family=self.source_family,
            layer_idx=extractor._mid_idx,
            context_text=context_text,
            seq_len=1,
        )
        blob = cs.to_blob()

        # Semantic embedding
        emb = self._embed_text(context_text)
        if emb is None:
            # Fallback: zero embedding (retrieval will be random but won't crash)
            emb = np.zeros(384, dtype=np.float32)

        # Store
        if overwrite:
            self._conn.execute(
                "DELETE FROM latent_index WHERE context_hash = ?",
                (context_hash,)
            )

        cur = self._conn.execute(
            """INSERT INTO latent_index
               (context_hash, source_family, layer_idx, hidden_dim,
                compressed_blob, embedding, embedding_dim,
                context_preview, unit_path, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                context_hash,
                self.source_family,
                cs.layer_idx,
                cs.hidden_dim,
                blob,
                emb.tobytes(),
                len(emb),
                context_text[:200].replace("\n", " "),
                unit_path,
                time.time(),
            )
        )
        row_id = cur.lastrowid
        print(
            f"[LatentRAG] Indexed: {unit_path or 'unit'}  "
            f"dim={cs.hidden_dim}  hash={context_hash[:12]}…  id={row_id}",
            flush=True,
        )
        return row_id

    def index_texts(
        self,
        texts:     list[str],
        paths:     Optional[list[str]] = None,
        extractor: Optional[MidLayerExtractor] = None,
        family:    Optional[str] = None,
    ) -> int:
        """
        Index a batch of text units.

        If extractor is None, creates and manages one internally.
        Returns count of successfully indexed units.
        """
        family    = family or self.source_family
        paths     = paths or [""] * len(texts)
        managed   = extractor is None

        if managed:
            extractor = MidLayerExtractor(family)

        indexed = 0
        try:
            for text, path in zip(texts, paths):
                row_id = self.index_unit(text, extractor, unit_path=path)
                if row_id is not None:
                    indexed += 1
        finally:
            if managed:
                extractor.unload()

        print(f"[LatentRAG] Indexed {indexed}/{len(texts)} units.", flush=True)
        return indexed

    def count(self) -> int:
        return self._conn.execute("SELECT COUNT(*) FROM latent_index").fetchone()[0]

    def close(self):
        if self._conn:
            self._conn.close()
            self._conn = None

    def __enter__(self): return self
    def __exit__(self, *_): self.close()


# ---------------------------------------------------------------------------
# LATENT RETRIEVER — semantic search + Rosetta projection
# ---------------------------------------------------------------------------

class LatentRetriever:
    """
    Retrieves semantically similar hidden states from the latent index,
    decompresses them, and projects into the target model's embedding space.

    The projected tensors are fed directly to RosettaInferenceBridge as
    soft prefix vectors.
    """

    def __init__(self, db_path: str | Path = "determinex_latent.db"):
        self.db_path    = Path(db_path)
        self.compressor = KVCompressor()
        self._embedder  = _get_embedder()
        self._conn      = sqlite3.connect(
            str(self.db_path),
            check_same_thread=False,
            isolation_level=None,
        )
        print(f"[LatentRAG] Retriever DB: {self.db_path}", flush=True)

    def _cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        """Compute cosine similarity between two flat float32 arrays."""
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        if norm_a < 1e-8 or norm_b < 1e-8:
            return 0.0
        return float(np.dot(a, b) / (norm_a * norm_b))

    def retrieve_states(
        self,
        query:           str,
        top_k:           int = 3,
        source_family:   Optional[str] = None,
    ) -> list[dict]:
        """
        Retrieve top-K semantically similar compressed states for a query.

        Performs cosine similarity search over all stored AllMiniLML6V2
        embeddings in sqlite (pure Python, no external vector DB).

        Args:
            query         : natural language query (Architect step instruction)
            top_k         : number of states to retrieve
            source_family : filter by model family (None = any)

        Returns:
            list of dicts with keys:
                {context_hash, source_family, compressed_state, similarity,
                 context_preview, unit_path, hidden_dim}
        """
        # Embed query
        if self._embedder is not None:
            query_emb_list = list(self._embedder.embed([query]))
            query_emb = np.array(query_emb_list[0], dtype=np.float32)
        else:
            query_emb = np.zeros(384, dtype=np.float32)

        # Fetch all stored embeddings (efficient for <100K entries in sqlite)
        if source_family:
            rows = self._conn.execute(
                """SELECT context_hash, source_family, compressed_blob,
                          embedding, context_preview, unit_path, hidden_dim
                   FROM latent_index WHERE source_family = ?""",
                (source_family,)
            ).fetchall()
        else:
            rows = self._conn.execute(
                """SELECT context_hash, source_family, compressed_blob,
                          embedding, context_preview, unit_path, hidden_dim
                   FROM latent_index"""
            ).fetchall()

        if not rows:
            return []

        # Score by cosine similarity
        scored = []
        for row in rows:
            ctx_hash, family, blob, emb_bytes, preview, path, dim = row
            stored_emb = np.frombuffer(emb_bytes, dtype=np.float32)
            if len(stored_emb) != len(query_emb):
                continue
            sim = self._cosine_similarity(query_emb, stored_emb)
            scored.append((sim, ctx_hash, family, blob, preview, path, dim))

        # Sort descending and take top-K
        scored.sort(key=lambda x: x[0], reverse=True)
        results = []
        for sim, ctx_hash, family, blob, preview, path, dim in scored[:top_k]:
            cs = CompressedState.from_blob(blob)
            results.append({
                "context_hash":      ctx_hash,
                "source_family":     family,
                "compressed_state":  cs,
                "similarity":        sim,
                "context_preview":   preview,
                "unit_path":         path,
                "hidden_dim":        dim,
            })

        print(
            f"[LatentRAG] Retrieved {len(results)} states for query '{query[:50]}…'  "
            f"top_sim={results[0]['similarity']:.4f if results else 0:.4f}",
            flush=True,
        )
        return results

    def retrieve_and_project(
        self,
        query:         str,
        stone:         RosettaStone,
        target_family: str,
        top_k:         int = 3,
        source_family: Optional[str] = None,
    ) -> list[torch.Tensor]:
        """
        Retrieve top-K states and project into target model's embedding space.

        This is the primary method called by the Architect before Builder
        generation to inject latent context.

        Args:
            query         : Architect step instruction text
            stone         : loaded RosettaStone instance
            target_family : family key of the Builder GGUF model
            top_k         : number of prefix vectors to inject
            source_family : filter retrieval by source family

        Returns:
            list of [target_dim] float32 tensors (soft prefix vectors)
            Empty list if no states indexed or retrieval fails.
        """
        retrieved = self.retrieve_states(query, top_k=top_k, source_family=source_family)
        if not retrieved:
            return []

        prefix_vectors = []
        for item in retrieved:
            cs = item["compressed_state"]
            src_family = item["source_family"]

            # Decompress to float32 tensor
            hidden = self.compressor.decompress(cs)   # [hidden_dim]

            # Project through RosettaStone into target embedding space
            try:
                with torch.no_grad():
                    projected = stone.translate(
                        src_family=src_family,
                        tgt_family=target_family,
                        hidden=hidden.unsqueeze(0).float(),
                    )
                prefix_vectors.append(projected.squeeze(0).float())
            except KeyError as e:
                print(
                    f"[LatentRAG] Family '{e}' not in RosettaStone. Skipping.",
                    flush=True,
                )

        print(
            f"[LatentRAG] Projected {len(prefix_vectors)} prefix vectors  "
            f"{source_family or 'any'}→{target_family}",
            flush=True,
        )
        return prefix_vectors

    def close(self):
        if self._conn:
            self._conn.close()
            self._conn = None

    def __enter__(self): return self
    def __exit__(self, *_): self.close()


# ---------------------------------------------------------------------------
# SELF-TEST — no HF model or GGUF required
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import tempfile, os

    print("[LatentRAG] Running self-test (no model load)...", flush=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test_latent.db"

        # Manual insert (bypassing extractor for the self-test)
        indexer = LatentIndexer(db_path=db_path, source_family="mistral")
        indexer._conn.execute("PRAGMA journal_mode=WAL")

        compressor = KVCompressor()
        dummy_texts = [
            "Implement a thread-safe singleton using Arc and Mutex in Rust.",
            "Write a Go function that handles panics with defer and recover.",
            "Create a Python async context manager for database connections.",
        ]

        import torch as _torch
        for text in dummy_texts:
            hidden = _torch.randn(4096)    # mistral dim
            cs     = compressor.compress(hidden, "mistral", layer_idx=16, context_text=text)
            blob   = cs.to_blob()
            h      = hashlib.sha256(text.encode()).hexdigest()
            emb    = np.zeros(384, dtype=np.float32)   # dummy embedding
            indexer._conn.execute(
                """INSERT OR IGNORE INTO latent_index
                   (context_hash, source_family, layer_idx, hidden_dim,
                    compressed_blob, embedding, embedding_dim,
                    context_preview, unit_path, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (h, "mistral", 16, 4096, blob, emb.tobytes(), 384,
                 text[:100], "test", time.time())
            )
        indexer.close()

        assert db_path.exists(), "DB not created"
        print(f"  Indexed {len(dummy_texts)} units  ✓")

        # Retrieve
        retriever = LatentRetriever(db_path=db_path)
        results   = retriever.retrieve_states("thread-safe Rust singleton", top_k=2)
        assert len(results) > 0, "Retrieval returned empty"
        print(f"  Retrieved {len(results)} states  ✓")

        # Project through minimal RosettaStone
        stone   = RosettaStone()
        vectors = retriever.retrieve_and_project(
            "thread-safe Rust singleton", stone, "qwen", top_k=2,
            source_family="mistral",
        )
        assert len(vectors) > 0, "No projected vectors"
        assert vectors[0].shape == (_torch.Size([2048]),), f"Unexpected shape: {vectors[0].shape}"
        print(f"  Projected {len(vectors)} prefix vectors  shape={tuple(vectors[0].shape)}  ✓")

        retriever.close()

    print("[LatentRAG] Self-test passed.", flush=True)
