# Determinex Splash Path Reconciliation And Prep

Locked under:

- `DETERMINEX_WORKSPACE_EVIDENCE_RECONCILIATION_LOCK_001`
- `DETERMINEX_SPLASH_TARGET_REQUIREMENTS_PACKET_LOCK_001`
- `DETERMINEX_PYTHON_CLI_FILE_DATA_SCAFFOLD_SPEC_LOCK_001`
- `DETERMINEX_PYTHON_CLI_ACCEPTANCE_AND_SMOKE_PLAN_LOCK_001`
- `DETERMINEX_IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_READINESS_LOCK_001`

## Reconciliation

The prior evidence drift was caused by Claude unified-product UX evidence
landing after the append-only ledger snapshot. The affected lock IDs were the
Claude product navigation/workflow/user-level/splash/final-state locks plus
Claude claim/demo hygiene locks. The reconciliation updated the generated
evidence index to the current lock set and refreshed the append-only ledger
snapshot. The count drift guard is now expected to pass.

Remaining dirty workspace entries are classified in the reconciliation record.
They do not grant source mutation, artifact import, ProgramBench execution,
proof execution, approval authority, or training eligibility.

## Prepared Splash Target

Target:

- surface: Idea Lab
- workflow: new project creation
- app class: CLI/file-data tool
- language: Python

This rung does not implement the app. It defines the exact packet required for
the next implementation lock.

## Scaffold Spec

Planned files:

- `README.md`
- `pyproject.toml`
- `src/splash_tool/__init__.py`
- `src/splash_tool/cli.py`
- `src/splash_tool/transform.py`
- `tests/test_cli.py`
- `tests/fixtures/sample_input.csv`
- `tests/fixtures/expected_output.csv`
- `evidence/manifest.json`
- `FINAL_REPORT.md`

Default dependency policy is stdlib-only. No Docker, no network dependency, no
external service, no writes outside the project root, and no hidden source
mutation are allowed.

## Acceptance And Smoke Plan

Acceptance tests:

1. CLI help or usage behavior.
2. Sample input produces expected output.
3. Invalid input produces a safe error.

Smoke test:

1. Local command runs successfully and produces expected observable output.

No success claim is allowed if acceptance tests are absent. No working-app
claim is allowed if smoke evidence is absent.

## Readiness

The next implementation lock is ready to run only as:

`DETERMINEX_IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_LOCK_001`

Implementation is still not executed by this prep rung. Training eligibility
remains false.
