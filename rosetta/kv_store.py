"""
rosetta/kv_store.py — KV State Persistence for Flow AI

Stores and retrieves compressed mid-layer hidden states in sqlite.
No sqlite-vec dependency — pure sqlite BLOB storage with hash-based lookup.

Schema:
    kv_states table stores one row per context processed by the large model.
    Retrieval is by context_hash (exact match) or recency.

Usage:
    store = KVStore("determinex_kv.db")
    row_id = store.store(context_text, "mistral", compressed_state)
    cs = store.retrieve_by_hash(context_hash)
    recent = store.retrieve_recent(n=5)
"""

import hashlib
import sqlite3
import sys
import time
from pathlib import Path
from typing import Optional

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# kv_compress must be importable — add rosetta/ to path if run standalone
try:
    from kv_compress import CompressedState
except ImportError:
    import sys, os
    sys.path.insert(0, str(Path(__file__).parent))
    from kv_compress import CompressedState


# ---------------------------------------------------------------------------
# SCHEMA
# ---------------------------------------------------------------------------

_SCHEMA = """
CREATE TABLE IF NOT EXISTS kv_states (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    context_hash     TEXT    NOT NULL,
    source_family    TEXT    NOT NULL,
    layer_idx        INTEGER NOT NULL,
    hidden_dim       INTEGER NOT NULL,
    compressed_blob  BLOB    NOT NULL,
    created_at       REAL    NOT NULL,
    context_preview  TEXT    DEFAULT '',
    seq_len          INTEGER DEFAULT 1
);

CREATE INDEX IF NOT EXISTS idx_kv_context_hash ON kv_states(context_hash);
CREATE INDEX IF NOT EXISTS idx_kv_created_at   ON kv_states(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_kv_family       ON kv_states(source_family);
"""


# ---------------------------------------------------------------------------
# STORE
# ---------------------------------------------------------------------------

class KVStore:
    """
    sqlite-backed store for compressed mid-layer hidden states.

    Thread safety: uses check_same_thread=False with WAL mode, safe for
    multiple readers and one writer (standard Determinex single-process use).
    """

    def __init__(self, db_path: str | Path = "determinex_kv.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(
            str(self.db_path),
            check_same_thread=False,
            isolation_level=None,   # autocommit
        )
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute("PRAGMA synchronous=NORMAL")
        self._conn.executescript(_SCHEMA)
        print(f"[KVStore] DB: {self.db_path}", flush=True)

    def close(self):
        if self._conn:
            self._conn.close()
            self._conn = None

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()

    # ── Write ────────────────────────────────────────────────────────────────

    def store(
        self,
        context_text: str,
        source_family: str,
        cs: CompressedState,
        overwrite: bool = True,
    ) -> int:
        """
        Store a compressed state for a given context.

        Args:
            context_text  : the full context text the large model processed
            source_family : family name of the large model ("mistral", etc.)
            cs            : CompressedState from KVCompressor.compress()
            overwrite     : if True, replace existing row with same context_hash

        Returns:
            sqlite row id
        """
        context_hash = hashlib.sha256(context_text.encode("utf-8")).hexdigest()
        preview      = context_text[:200].replace("\n", " ")
        blob         = cs.to_blob()
        now          = time.time()

        if overwrite:
            self._conn.execute(
                "DELETE FROM kv_states WHERE context_hash = ?",
                (context_hash,)
            )

        cur = self._conn.execute(
            """INSERT INTO kv_states
               (context_hash, source_family, layer_idx, hidden_dim,
                compressed_blob, created_at, context_preview, seq_len)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (context_hash, source_family, cs.layer_idx, cs.hidden_dim,
             blob, now, preview, cs.seq_len)
        )
        row_id = cur.lastrowid
        print(
            f"[KVStore] Stored: hash={context_hash[:12]}…  "
            f"family={source_family}  dim={cs.hidden_dim}  "
            f"layer={cs.layer_idx}  blob={len(blob):,}B  id={row_id}",
            flush=True
        )
        return row_id

    # ── Read ─────────────────────────────────────────────────────────────────

    def retrieve_by_hash(self, context_hash: str) -> Optional[CompressedState]:
        """
        Retrieve the compressed state for an exact context hash.

        Returns None if not found.
        """
        row = self._conn.execute(
            "SELECT compressed_blob FROM kv_states WHERE context_hash = ? ORDER BY created_at DESC LIMIT 1",
            (context_hash,)
        ).fetchone()
        if row is None:
            return None
        return CompressedState.from_blob(row[0])

    def retrieve_by_text(self, context_text: str) -> Optional[CompressedState]:
        """Convenience wrapper: hash the text and retrieve."""
        return self.retrieve_by_hash(
            hashlib.sha256(context_text.encode("utf-8")).hexdigest()
        )

    def retrieve_recent(self, n: int = 5, family: Optional[str] = None) -> list[dict]:
        """
        Retrieve the n most recently stored states as dicts with metadata.

        Returns list of:
            {id, context_hash, source_family, layer_idx, hidden_dim,
             created_at, context_preview, compressed_state}
        """
        if family:
            rows = self._conn.execute(
                """SELECT id, context_hash, source_family, layer_idx, hidden_dim,
                          created_at, context_preview, compressed_blob
                   FROM kv_states WHERE source_family = ?
                   ORDER BY created_at DESC LIMIT ?""",
                (family, n)
            ).fetchall()
        else:
            rows = self._conn.execute(
                """SELECT id, context_hash, source_family, layer_idx, hidden_dim,
                          created_at, context_preview, compressed_blob
                   FROM kv_states ORDER BY created_at DESC LIMIT ?""",
                (n,)
            ).fetchall()

        results = []
        for row in rows:
            results.append({
                "id":               row[0],
                "context_hash":     row[1],
                "source_family":    row[2],
                "layer_idx":        row[3],
                "hidden_dim":       row[4],
                "created_at":       row[5],
                "context_preview":  row[6],
                "compressed_state": CompressedState.from_blob(row[7]),
            })
        return results

    # ── Maintenance ───────────────────────────────────────────────────────────

    def count(self, family: Optional[str] = None) -> int:
        """Return number of stored states."""
        if family:
            return self._conn.execute(
                "SELECT COUNT(*) FROM kv_states WHERE source_family = ?", (family,)
            ).fetchone()[0]
        return self._conn.execute("SELECT COUNT(*) FROM kv_states").fetchone()[0]

    def purge_older_than(self, seconds: float) -> int:
        """Delete states older than `seconds`. Returns number of rows deleted."""
        cutoff = time.time() - seconds
        cur = self._conn.execute(
            "DELETE FROM kv_states WHERE created_at < ?", (cutoff,)
        )
        deleted = cur.rowcount
        if deleted:
            print(f"[KVStore] Purged {deleted} old states.", flush=True)
        return deleted

    def stats(self) -> dict:
        """Return summary statistics."""
        row = self._conn.execute(
            """SELECT COUNT(*), SUM(LENGTH(compressed_blob)),
                      MIN(hidden_dim), MAX(hidden_dim)
               FROM kv_states"""
        ).fetchone()
        families = [
            r[0] for r in self._conn.execute(
                "SELECT DISTINCT source_family FROM kv_states"
            ).fetchall()
        ]
        return {
            "total_states":   row[0] or 0,
            "total_bytes":    row[1] or 0,
            "min_hidden_dim": row[2],
            "max_hidden_dim": row[3],
            "families":       families,
            "db_path":        str(self.db_path),
        }


# ---------------------------------------------------------------------------
# SELF-TEST
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import tempfile
    import torch
    sys.path.insert(0, str(Path(__file__).parent))
    from kv_compress import KVCompressor

    print("[KVStore] Running self-test...", flush=True)
    compressor = KVCompressor()

    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        db_path = f.name

    with KVStore(db_path) as store:
        contexts = [
            "The Rust borrow checker enforces ownership at compile time.",
            "Flow AI is inference-time bidirectional latent-state transfer.",
            "A DAG is a directed acyclic graph used for dependency resolution.",
        ]
        hashes = []
        for ctx in contexts:
            state = torch.randn(3072)  # mistral hidden dim
            cs    = compressor.compress(state, family="mistral", layer_idx=16, context_text=ctx)
            h     = hashlib.sha256(ctx.encode()).hexdigest()
            store.store(ctx, "mistral", cs)
            hashes.append(h)

        # Retrieve by hash
        cs_back = store.retrieve_by_hash(hashes[0])
        assert cs_back is not None, "retrieve_by_hash failed"
        recovered = compressor.decompress(cs_back)
        print(f"  retrieve_by_hash: ok, dim={recovered.shape[0]}")

        # Retrieve by text
        cs_back2 = store.retrieve_by_text(contexts[1])
        assert cs_back2 is not None, "retrieve_by_text failed"
        print(f"  retrieve_by_text: ok")

        # Recent
        recent = store.retrieve_recent(2)
        assert len(recent) == 2, f"Expected 2, got {len(recent)}"
        print(f"  retrieve_recent(2): ok, previews: {[r['context_preview'][:30] for r in recent]}")

        # Stats
        s = store.stats()
        print(f"  stats: {s}")
        assert s["total_states"] == 3

    import os
    os.unlink(db_path)
    print("[KVStore] All tests passed.", flush=True)
