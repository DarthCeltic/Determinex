# Real Temp Patch Verify

> Locked under `locks/sentinel/REAL_TEMP_PATCH_VERIFY_LOCK_001.json`.

`scripts/repair/real_temp_patch_verify.py` stages a copy of the
original workspace into a temp root, applies a previously-quarantined
patch plan there, and runs the verifier callable. The **original
source is never written**; pre/post sha256 of the original tree is
captured and compared.

Decisions:

| Decision | Meaning |
|---|---|
| `REAL_TEMP_PATCH_VERIFIER_PASSED` | verifier passed on temp; `human_approval_required=True` |
| `REAL_TEMP_PATCH_VERIFIER_FAILED` | verifier failed on temp; no further action |
| `REAL_TEMP_PATCH_BLOCKED_NOT_QUARANTINED` | upstream plan missing or not quarantined |
| `REAL_TEMP_PATCH_BLOCKED_APPLY_REJECTED` | safe-patch apply blocked or no resolvable bodies |

The verifier callable is pluggable. Default = `stub_verifier_pass`
from the locked SafePatchWorkspace surface. Callers should pass a
real BuildAdapter-backed verifier for production.

Every record carries `source_mutation_authorized=False`,
`training_eligible=False`, and `original_unchanged=True`.
