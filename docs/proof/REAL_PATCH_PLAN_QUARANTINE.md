# Real Patch Plan Quarantine

> Locked under `locks/sentinel/REAL_PATCH_PLAN_QUARANTINE_LOCK_001.json`.

`scripts/repair/real_patch_plan_quarantine.py` validates a real-model
patch plan and records it as quarantined / untrusted. No filesystem
write happens at this rung.

Per-entry validation:

- schema: dict with `operation`, `path`, `new_content` (all strings,
  no NUL bytes)
- `operation ∈ {"replace_file"}`
- `path` normalized to a relative POSIX path; rejects absolute,
  drive-anchored, `..` segments
- `new_content` size bounded; total plan size bounded

Overall decisions: `QUARANTINED` (≥1 entry survived), or one of
`BLOCKED_SCHEMA_INVALID`, `BLOCKED_PATH_ESCAPE`,
`BLOCKED_UNSUPPORTED_OPERATION` (when no entry survives), or
`BLOCKED_NO_MODEL` / `BLOCKED_NOT_OPTED_IN` upstream gates.

Every record carries `patch_applied=False`,
`source_mutation_authorized=False`, `training_eligible=False`,
`output_trusted=False`.
