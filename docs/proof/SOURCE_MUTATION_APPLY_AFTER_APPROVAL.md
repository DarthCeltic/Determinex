# Source Mutation Apply After Approval

> Locked under `locks/sentinel/SOURCE_MUTATION_APPLY_AFTER_APPROVAL_LOCK_001.json`.

`scripts/repair/source_mutation_apply_after_approval.py` is the
**first place that actually writes the user's original workspace**.

Before any write, every upstream gate is re-checked:

- approval `ACCEPTED` (real, not fixture)
- temp verify `PASSED`
- rollback snapshot `WRITTEN`
- pre-apply workspace sha256 matches the snapshot's `pre_apply_source_hash`
- observed diff hash matches `approval.diff_hash`
- each path normalizes to a relative POSIX path under the workspace
- each accepted plan path has a body in `plan_entries`

Refusals: `BLOCKED_NO_APPROVAL`, `BLOCKED_NO_ROLLBACK`,
`BLOCKED_SOURCE_HASH_MISMATCH`, `BLOCKED_DIFF_MISMATCH`,
`BLOCKED_VERIFIER_NOT_PASSED`, `BLOCKED_PLAN_BODY_MISSING`,
`BLOCKED_PATH_ESCAPE`.

On `SOURCE_MUTATION_APPLIED_AFTER_APPROVAL`:

- `source_mutation_applied=True`
- `post_apply_verifier_required=True` (rung 9 runs it)
- `training_eligible=False` (no training row)
- `pre_apply_source_hash` and `post_apply_source_hash` recorded

Block paths preserve the workspace; including the deliberate drift
test case where the source has diverged from the snapshot.
