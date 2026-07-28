# Real Model Diagnose With Build Verifier

> Locked under `locks/sentinel/REAL_MODEL_DIAGNOSE_WITH_BUILD_VERIFIER_LOCK_001.json`.

`scripts/models/real_model_diagnose_with_build_verifier.py` composes
the healthcheck and verifier-selection records and asks the real
local model for an advisory diagnostic class.

The prompt carries:

- opaque `workspace_identity`
- `build_system_id` (e.g. `pip`)
- verifier argv (e.g. `pytest`)

The prompt does **NOT** carry any source content. The system message
reinforces that output is untrusted and the verifier is the source of
truth.

Decisions: `WRITTEN`, `BLOCKED_HEALTHCHECK_FAILED`,
`BLOCKED_NO_VERIFIER`, `BLOCKED_NOT_OPTED_IN`, `BLOCKED_TIMEOUT`,
`BLOCKED_PROVIDER_ERROR`. `ADVISORY_ONLY` always present in
`statuses_seen`. Advisory text is bounded to 2048 chars.

`advisory_only=True`, `output_trusted=False`, `patch_generated=False`,
`source_mutation_authorized=False`, `training_eligible=False`,
`verifier_remains_source_of_truth=True` on every record.
