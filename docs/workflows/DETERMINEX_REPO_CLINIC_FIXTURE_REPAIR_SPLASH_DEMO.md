# Determinex Repo Clinic Fixture Repair Splash Demo

Lock: `DETERMINEX_REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_LOCK_001`

Purpose: prove one narrow Repo Clinic path: a broken Python fixture repo can be analyzed, verified failing, patched only inside the fixture workspace, and re-verified with the same local test command.

Scope:

- Target surface: Repo Clinic
- Target workflow: existing broken fixture repo to verifier-backed repair evidence
- Target language: Python
- Fixture workspace: `assurance/demo_workspaces/repo_clinic_fixture_repair_splash_demo/run_20260529`
- Verifier: `python -m pytest tests -q`

Boundaries:

- This does not prove all codebases.
- This does not prove all languages.
- This does not prove arbitrary repair.
- This does not prove production-ready arbitrary repair.
- This does not grant real user source mutation authority.
- Training remains false.

Evidence record: `assurance/evidence/repo_clinic_fixture_repair_splash_demo/run_20260529.REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_PASSED.json`
