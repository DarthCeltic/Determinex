"""rosetta/latent_memory.py — Layer 2C: latent memory / hidden-state RAG.

This is the *honest* name for the system that earlier docs called "KV broadcast"
or "KV-cache RAG". It is NOT a transformer K/V cache. It is a store of
COMPRESSED POOLED HIDDEN STATES (one float vector per context, int8-quantized)
indexed in sqlite, retrieved by either context hash or cosine similarity.

The filename `kv_store.py` is kept (renaming would break callers) but the
public surface here uses the accurate term.

Terminology lock — write this exactly when describing this layer in docs:

    Latent memory stores compressed pooled hidden states, not literal
    transformer K/V cache tensors. Layer 2C complements Layer 2B (soft-prefix
    injection): 2C is the retrieval surface, 2B is the delivery mechanism.
    True Layer 3 KV-cache broadcast remains future work — see kv_broadcast.py.

Public API:
    LatentMemory.store(context, hidden_state, metadata=None) -> int
    LatentMemory.retrieve(query_hidden, k=5) -> list[LatentHit]
    LatentMemory.retrieve_by_text(query_text, k=5) -> list[LatentHit]
    LatentMemory.recent(k=5, family=None) -> list[LatentHit]
    LatentMemory.close()

Wraps:
    rosetta.kv_store.KVStore           — sqlite persistence
    rosetta.kv_compress.KVCompressor    — int8 quantization
    rosetta.kv_compress.CompressedState — blob format
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# rosetta/ modules import each other; tolerate both module-path and direct execution
try:
    from rosetta.kv_compress import CompressedState, KVCompressor
    from rosetta.kv_store import KVStore
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from kv_compress import CompressedState, KVCompressor  # type: ignore[no-redef]
    from kv_store import KVStore  # type: ignore[no-redef]


# ---------------------------------------------------------------------------
# Hit record returned by retrieve()
# ---------------------------------------------------------------------------


@dataclass
class LatentHit:
    """A single retrieved latent state with similarity score and metadata."""

    similarity: float  # cosine similarity vs query in [-1, 1]
    family: str  # source model family
    layer_idx: int  # transformer layer the state was drawn from
    hidden_dim: int  # vector length
    context_hash: str  # sha256 of the originating context text
    context_preview: str  # first 200 chars of the context
    created_at: float  # epoch seconds
    pooled_state: np.ndarray  # dequantized [hidden_dim] float32 vector
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "similarity": self.similarity,
            "family": self.family,
            "layer_idx": self.layer_idx,
            "hidden_dim": self.hidden_dim,
            "context_hash": self.context_hash,
            "context_preview": self.context_preview,
            "created_at": self.created_at,
            "metadata": self.metadata,
        }


# ---------------------------------------------------------------------------
# LatentMemory
# ---------------------------------------------------------------------------


class LatentMemory:
    """Layer 2C: latent memory / hidden-state RAG.

    NOT a transformer K/V cache. Stores COMPRESSED POOLED HIDDEN STATES per
    context, retrieves by cosine similarity over the dequantized vectors.

    For larger corpora (>50k entries) the brute-force cosine scan in retrieve()
    becomes the cost bottleneck and a proper vector index (FAISS / hnswlib /
    sqlite-vec) should replace it. For Determinex's local-only use today, brute
    force is honest and avoids a heavy dependency.
    """

    def __init__(self, db_path: str | Path = "determinex_latent.db"):
        self._store = KVStore(db_path=db_path)
        self._compressor = KVCompressor()

    # ── Lifecycle ────────────────────────────────────────────────────────────

    def close(self) -> None:
        self._store.close()

    def __enter__(self) -> LatentMemory:
        return self

    def __exit__(self, *_) -> None:
        self.close()

    # ── Write ────────────────────────────────────────────────────────────────

    def store(
        self,
        context: str,
        hidden_state: Any,
        metadata: dict | None = None,
    ) -> int:
        """Store a pooled hidden state keyed by its originating context.

        Args:
            context       : the text the source model processed (used as the key)
            hidden_state  : a 1-D pooled hidden state — torch.Tensor or np.ndarray of
                            shape [hidden_dim]. If a 2-D [seq_len, hidden_dim] tensor
                            is passed, it is mean-pooled along axis 0.
            metadata      : caller-supplied dict; family / layer_idx / seq_len are
                            pulled out if present, the rest is dropped on the floor
                            for now (no schema extension yet — keeps storage honest).

        Returns:
            sqlite row id.
        """
        meta = dict(metadata or {})
        family = meta.pop("family", "unknown")
        layer_idx = int(meta.pop("layer_idx", -1))
        seq_len = int(meta.pop("seq_len", 1))

        pooled = self._to_pooled(hidden_state)

        # Defer torch import to call site so import time stays low for non-torch users
        try:
            import torch

            state_t = torch.from_numpy(pooled).float()
        except ImportError as e:
            raise RuntimeError(
                "rosetta.latent_memory.LatentMemory.store requires torch for compression."
            ) from e

        cs = self._compressor.compress(
            state=state_t,
            family=family,
            layer_idx=layer_idx,
            context_text=context,
            seq_len=seq_len,
        )
        return self._store.store(
            context_text=context,
            source_family=family,
            cs=cs,
            overwrite=True,
        )

    # ── Read: vector similarity ──────────────────────────────────────────────

    def retrieve(self, query_hidden: Any, k: int = 5) -> list[LatentHit]:
        """Retrieve the top-k most similar stored states by cosine similarity.

        Args:
            query_hidden : 1-D pooled hidden state to compare against. Same shape
                           contract as store(): torch tensor / np.ndarray / list,
                           or 2-D for auto-mean-pooling.
            k            : number of hits to return (default 5)

        Returns:
            List of LatentHit, sorted by similarity descending.
        """
        query_vec = self._to_pooled(query_hidden)
        q_norm = float(np.linalg.norm(query_vec))
        if q_norm == 0.0:
            return []

        # Pull every stored row. For Determinex's small N this is fine; the
        # brute-force scan is documented as honest-but-not-scalable.
        rows = self._store._conn.execute(
            """SELECT id, context_hash, source_family, layer_idx, hidden_dim,
                      created_at, context_preview, compressed_blob
               FROM kv_states ORDER BY created_at DESC""",
        ).fetchall()

        hits: list[LatentHit] = []
        for row in rows:
            cs = CompressedState.from_blob(row[7])
            if cs.hidden_dim != len(query_vec):
                continue  # dim mismatch — skip silently here; bridge validates separately
            pooled = self._dequantize(cs)
            denom = (q_norm * float(np.linalg.norm(pooled))) or 1e-12
            sim = float(np.dot(query_vec, pooled) / denom)
            hits.append(
                LatentHit(
                    similarity=sim,
                    family=row[2],
                    layer_idx=row[3],
                    hidden_dim=row[4],
                    context_hash=row[1],
                    context_preview=row[6] or "",
                    created_at=row[5],
                    pooled_state=pooled,
                )
            )

        hits.sort(key=lambda h: h.similarity, reverse=True)
        return hits[:k]

    # ── Read: text-keyed convenience ─────────────────────────────────────────

    def retrieve_by_text(self, query_text: str, k: int = 5) -> list[LatentHit]:
        """Convenience: hash the query text and return exact-match hits.

        For *semantic* text-keyed retrieval, use rosetta.latent_rag.LatentRetriever
        which uses sentence-transformer embeddings as the index key (different
        semantic surface from hidden-state similarity).
        """
        cs = self._store.retrieve_by_text(query_text)
        if cs is None:
            return []
        pooled = self._dequantize(cs)
        return [
            LatentHit(
                similarity=1.0,
                family=cs.family,
                layer_idx=cs.layer_idx,
                hidden_dim=cs.hidden_dim,
                context_hash=cs.context_hash,
                context_preview=query_text[:200],
                created_at=0.0,
                pooled_state=pooled,
            )
        ][:k]

    def recent(self, k: int = 5, family: str | None = None) -> list[LatentHit]:
        """Return the k most-recent stored states (optional family filter)."""
        rows = self._store.retrieve_recent(n=k, family=family)
        hits = []
        for r in rows:
            cs = r.get("compressed_state")
            if cs is None:
                # retrieve_recent may not include the state in some shapes; skip
                continue
            pooled = self._dequantize(cs)
            hits.append(
                LatentHit(
                    similarity=1.0,
                    family=r.get("source_family", ""),
                    layer_idx=r.get("layer_idx", -1),
                    hidden_dim=r.get("hidden_dim", 0),
                    context_hash=r.get("context_hash", ""),
                    context_preview=r.get("context_preview", ""),
                    created_at=r.get("created_at", 0.0),
                    pooled_state=pooled,
                )
            )
        return hits

    # ── Diagnostics ──────────────────────────────────────────────────────────

    def count(self) -> int:
        row = self._store._conn.execute("SELECT COUNT(*) FROM kv_states").fetchone()
        return int(row[0]) if row else 0

    def status(self) -> dict:
        """JSON-serializable status — used by the healthcheck."""
        try:
            return {
                "layer": "Layer 2C (latent memory / hidden-state RAG)",
                "status": "ACTIVE",
                "db_path": str(self._store.db_path),
                "entries": self.count(),
                "note": "stores compressed pooled hidden states, NOT literal transformer K/V cache",
            }
        except Exception as e:
            return {
                "layer": "Layer 2C (latent memory / hidden-state RAG)",
                "status": "UNAVAILABLE WITH REASON",
                "reason": f"{type(e).__name__}: {e}",
            }

    # ── Internals ────────────────────────────────────────────────────────────

    @staticmethod
    def _to_pooled(hidden: Any) -> np.ndarray:
        """Normalize input to a 1-D float32 np.ndarray."""
        arr = np.asarray(hidden, dtype=np.float32)
        if arr.ndim == 2:
            arr = arr.mean(axis=0)
        if arr.ndim != 1:
            raise ValueError(
                f"hidden_state must be 1-D pooled or 2-D [seq, dim]; got shape {arr.shape}"
            )
        return arr

    @staticmethod
    def _dequantize(cs: CompressedState) -> np.ndarray:
        """Reconstruct the float32 pooled state from a CompressedState."""
        d = cs.hidden_dim
        q = np.frombuffer(cs.int8_data, dtype=np.int8)
        scales = np.frombuffer(cs.scales, dtype=np.float32)
        zero_points = np.frombuffer(cs.zero_points, dtype=np.float32)
        if q.shape != (d,) or scales.shape != (d,) or zero_points.shape != (d,):
            raise ValueError(
                f"CompressedState shape mismatch: dim={d} "
                f"q={q.shape} scales={scales.shape} zp={zero_points.shape}"
            )
        return ((q.astype(np.float32) - zero_points) * scales).astype(np.float32)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _cli():
    import argparse
    import json

    ap = argparse.ArgumentParser(description="Determinex Layer 2C — latent memory")
    ap.add_argument("--db", default="determinex_latent.db", help="sqlite path")
    ap.add_argument("--status", action="store_true", help="print status JSON")
    args = ap.parse_args()

    lm = LatentMemory(db_path=args.db)
    try:
        if args.status or True:
            print(json.dumps(lm.status(), indent=2))
    finally:
        lm.close()


if __name__ == "__main__":
    _cli()
