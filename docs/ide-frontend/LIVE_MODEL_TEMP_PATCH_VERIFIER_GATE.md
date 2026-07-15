# Live Model Temp Patch Verifier Gate

> Locked under `locks/sentinel/LIVE_MODEL_TEMP_PATCH_VERIFIER_GATE_LOCK_001.json`.

Consumes a `QuarantinedPatchPlan` and applies it ONLY to a temp
workspace via `SafePatchWorkspace`. The original repo remains
immutable. The verifier runs on the temp workspace via an injected
callable. Verifier failure rolls back the temp tree. Verifier pass
still yields `LIVE_PATCH_VERIFIER_PASSED_TEMP_ONLY` — human approval is
still required for any subsequent original-repo write.

## Hard invariants

* Original repo sha256 tree before == after on every code path
* `human_approval_required=True` on every result
* `training_eligible=False` on every result
