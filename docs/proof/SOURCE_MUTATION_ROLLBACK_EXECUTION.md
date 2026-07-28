# Source Mutation Rollback Execution

> Locked under `locks/sentinel/SOURCE_MUTATION_ROLLBACK_EXECUTION_LOCK_001.json`.

`scripts/repair/source_mutation_rollback_execution.py` restores the
workspace from the rollback snapshot when the post-apply verifier
fails.

Decisions:

- `SOURCE_ROLLBACK_NOT_REQUIRED` — verifier passed; no restore
- `SOURCE_ROLLBACK_EXECUTED` — verifier failed; snapshot intact; restored
- `SOURCE_ROLLBACK_BLOCKED_MISSING_SNAPSHOT` — snapshot dir missing
- `SOURCE_ROLLBACK_BLOCKED_SNAPSHOT_HASH_MISMATCH` — snapshot mutated
  since it was written; refusing to restore from it

The executor verifies the snapshot tree hash matches
`snapshot.snapshot_tree_hash` before restoring. Files in the workspace
that aren't in the snapshot are removed; files in the snapshot are
copied over the workspace counterparts. `pre_rollback_source_hash` and
`post_rollback_source_hash` are captured for evidence.

`training_eligible=False` on every record.
