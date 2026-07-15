# Rollback Symlink Semantics

> Locked under `locks/sentinel/ROLLBACK_SYMLINK_SEMANTICS_LOCK_001.json`.

Remediates **CLAUDE-AUTH-009**: the snapshot/restore path was
silently dereferencing symlinks.

Three execution layers now refuse to operate on a workspace that
contains any symlink:

| Layer | Module | Token |
|---|---|---|
| Snapshot writer | `scripts/repair/source_mutation_rollback_snapshot.py` | `ROLLBACK_SNAPSHOT_BLOCKED_SYMLINKS_UNSUPPORTED` |
| Source apply | `scripts/repair/source_mutation_apply_after_approval.py` | `SOURCE_MUTATION_BLOCKED_SYMLINKS_UNSUPPORTED` |
| Rollback executor | `scripts/repair/source_mutation_rollback_execution.py` | `SOURCE_ROLLBACK_BLOCKED_SYMLINKS_UNSUPPORTED` |

The detection helper lives at
`scripts/repair/symlink_policy.py`. It calls `Path.is_symlink()`
on every path under the workspace; `is_symlink()` does **not**
follow links, so a hostile symlink cannot redirect the check.

## Why refuse rather than preserve

A symlink-preservation implementation would have to:

- Record link targets as snapshot metadata
- Reconstruct links at restore time
- Validate that target paths do not escape the snapshot root
- Resolve cross-platform link-semantics differences
- Handle link-of-link chains and missing targets

A clean refusal is auditable: the operator can resolve the
workspace to a symlink-free state (e.g. replace links with their
target contents, or move them outside the workspace) before
retrying.

If symlink-preservation becomes a hard requirement, a future
`SYMLINK_SEMANTICS_PRESERVED_LOCK_002` can add it.

## Defense-in-depth

Each layer checks its own invariants — it does not trust upstream
callers. Even if the snapshot writer blocked, a direct call to
`apply_after_approval()` or `execute_rollback()` with a hand-built
record would still hit the per-layer symlink refusal.
