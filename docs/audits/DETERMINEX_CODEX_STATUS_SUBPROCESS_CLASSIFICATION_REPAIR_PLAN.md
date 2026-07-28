# Determinex Codex Status Subprocess Classification Repair Plan

Lock: `DETERMINEX_CODEX_STATUS_SUBPROCESS_CLASSIFICATION_REPAIR_PLAN_LOCK_001`

Purpose: resolve Claude's deferred Codex-lane finding for two `subprocess.run` sites under `scripts/status/*` without loosening helper execution policy.

Classifications:

- `scripts/status/idea_lab_python_cli_verified_splash_demo.py`: allowed safe helper, recorded in the audit as `LEGACY_EXEMPT_TEST_FIXTURE`. It runs fixed Python argv for fixture/demo-local acceptance and smoke verification inside the allowed demo workspace, with no shell and no authority grant.
- `scripts/status/splash_path_reconciliation_and_prep.py`: legacy exempt read-only, recorded in the audit as `LEGACY_EXEMPT_READ_ONLY`. It runs fixed `git status --porcelain=v1` argv for reconciliation only, with no shell and no payload execution.

Repair status: `CODEX_STATUS_SUBPROCESS_CLASSIFICATION_REPAIRED`.

Policy state:

- Helper execution policy was not loosened.
- No unsafe site was marked safe without a narrow path-specific rationale.
- No Claude implementation file was changed.
- No source mutation, approval, proof, or training authority was granted.

Evidence record: `assurance/evidence/codex_status_subprocess_classification_repair_plan/run_20260529.CODEX_STATUS_SUBPROCESS_CLASSIFICATION_REPAIRED.json`
