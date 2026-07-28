# Source Mutation Rollback Snapshot

> Locked under `locks/sentinel/SOURCE_MUTATION_ROLLBACK_SNAPSHOT_LOCK_001.json`.

`scripts/repair/source_mutation_rollback_snapshot.py` writes a copy of
the original workspace under a caller-supplied snapshot root **before
any source mutation is attempted**.

The record binds:

- pre-apply sha256 of the original tree
- snapshot path and snapshot tree sha256
- diff hash from the approval packet
- approval reference (decision token)
- verifier reference (verifier status)

Refusals:

- `BLOCKED_NO_APPROVAL` — upstream approval missing or not accepted
- `BLOCKED_NO_VERIFY` — temp-verify missing or did not pass
- `BLOCKED_SOURCE_HASH_MISMATCH` — workspace state drifted from the
  hash captured at packet time
- `BLOCKED_INVALID_LOCATION` — snapshot root unwritable or path escapes,
  or destination already exists (no overwrite)

Source mutation is NOT applied by this lock. It only produces the
restore target for the next rung's failure path.
