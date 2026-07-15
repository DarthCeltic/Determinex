# Determinex IDE Backend — Final State

> Locked under `locks/sentinel/DETERMINEX_IDE_BACKEND_FINAL_STATE_LOCK_001.json`.
> Evidence: `assurance/evidence/determinex_ide_backend_final_state/run_20260527.json`.

This is the campaign-end roll-up. The Claude lane's verified-repair
apparatus reaches its documented equilibrium: every foundation
hardening rung landed, every verified-repair rung landed, and the
apparatus is ready for its next campaign.

## Final dimensions

```
execution_surface:    CLEAN
model_routing:        READY_DRY_RUN
repo_intake:          READY_FIXTURES
verifier_matrix:      PARTIAL_BACKED
mocked_repair_loop:   READY
safe_patch_workspace: READY_TEMP_ONLY
source_mutation:      BLOCKED_PENDING_HUMAN_APPROVAL
ide_backend_state:    READY
live_model_calls:     NOT_ADMITTED
training_eligibility: BLOCKED_BY_DEFAULT
release_readiness:    NOT_RELEASED
next_unblocker:       LOCAL_MODEL_LIVE_ADMISSION_AND_IDE_UI_FLOW
```

## What this state means

* **CLEAN execution surface** — every script under `scripts/` is
  classified; `BLOCKED_UNSAFE=0`, `MUST_MIGRATE=0`,
  `UNKNOWN_REQUIRES_REVIEW=0`, `PROGRAMBENCH_OUT_OF_SCOPE=56`.
* **READY_DRY_RUN model routing** — `ModelRouter` produces structured
  decisions; `execution_authorized` opens only in `LIVE` mode and only
  for current, available ids.
* **READY_FIXTURES repo intake** — `BuildAdapterRegistry.select` works
  across the canonical fixture set (python/rust/go/ts/unknown).
* **PARTIAL_BACKED verifier matrix** — adapter coverage is real;
  verifier coverage is partial per the existing
  `VERIFIER_COVERAGE_MATRIX_LOCK_001`.
* **READY mocked repair loop** — `MockedIntakeRepairLoop` composes
  router + adapters + mock client over five fixtures.
* **READY_TEMP_ONLY safe patch workspace** — `SafePatchWorkspace`
  writes only to temp; original repo is immutable.
* **BLOCKED_PENDING_HUMAN_APPROVAL source mutation** — original-repo
  writes require an accepted `ApprovalGateDecision`; today only the
  `_FIXTURE` accepted path is admitted.
* **READY IDE backend state** — `IDERepairState` exposes a flat
  JSON-serializable record any frontend can render.
* **NOT_ADMITTED live model calls** — admission policy exists
  (metadata-only); live admission is a separate, later rung.
* **BLOCKED_BY_DEFAULT training eligibility** — the corpus eligibility
  guard refuses every trace produced by the current campaign.
* **NOT_RELEASED release readiness** — the apparatus is at equilibrium,
  not at a public release.

## Next unblocker

`LOCAL_MODEL_LIVE_ADMISSION_AND_IDE_UI_FLOW` — the campaign that takes
the apparatus from "dry-run + mocked + temp-only + fixture-approval"
to "live local models + real verified traces + operator-approved
source mutation."

## What this lock does *not* do

* No release workflow. No demo packaging.
* No live model admission.
* No frontend UI implementation.
* No flipping of any safety default.

## Reproducing the evidence

```
.\.venv\Scripts\python.exe -m pytest tests/dev/test_determinex_ide_backend_final_state_lock.py -q --tb=short
```
