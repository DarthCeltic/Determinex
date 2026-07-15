# Model Admission — No Bypass

> Locked under `locks/sentinel/MODEL_ADMISSION_NO_BYPASS_LOCK_001.json`.

Remediates **CLAUDE-AUTH-004**: previously
`real_model_patch_plan_with_verifier_context` synthesized a
`RealLocalModelAdmissionRecord(decision=ADMITTED, ...)` inline,
bypassing the locked admission gate.

The fix:

- The function now accepts an `admission:
  RealLocalModelAdmissionRecord` parameter and requires it
- If `admission is None` or `not admission.is_admitted`:
  `REAL_PATCH_PLAN_CONTEXT_BLOCKED_MODEL_ADMISSION_REQUIRED`
- The admission's `model_id` / `provider` must match the
  healthcheck's `model_id` / `provider` — otherwise blocked with the
  same code

Callers must invoke
`real_local_model_admission.admit()` explicitly. The synthesized
shortcut is gone.
