# IDE Repair State Model

> Locked under `locks/sentinel/IDE_REPAIR_STATE_MODEL_LOCK_001.json`.
> Evidence: `assurance/evidence/ide_repair_state_model/run_20260527.json`.

The IDE repair state model is the apparatus's first frontend-facing
surface. It takes a `VerifiedRepairTrace` (and optionally an
`ApprovalGateDecision`) and produces a flat `IDERepairState` dataclass
that any consumer — Tauri, web, CLI, dashboard — can render directly.

## Why a flat record

Front-ends should not need to know that:

* `intake` actually comes from `trace.final_status != UNSUPPORTED_REPO`
* `verifier` is derived from `trace.safe_patch_result.verifier_status`
* `source_approval` requires looking at *both* the trace and the gate
  decision
* "Approval required" is not the same shape as "approval blocked"

The state model encapsulates all of that. The consumer reads one JSON
record and renders.

## Dimensions

| Dimension          | Possible values                                                        |
|--------------------|------------------------------------------------------------------------|
| `intake`           | `INTAKE_READY`, `INTAKE_UNSUPPORTED`                                   |
| `verifier`         | `VERIFIER_AVAILABLE`, `VERIFIER_MISSING`                               |
| `model_route`      | `MODEL_ROUTE_SELECTED`, `MODEL_ROUTE_BLOCKED`, `MODEL_ROUTE_NO_MODEL`  |
| `patch_plan`       | `PATCH_PLAN_AVAILABLE`, `PATCH_PLAN_UNAVAILABLE`                       |
| `patch_temp`       | `PATCH_TEMP_APPLIED`, `PATCH_TEMP_FAILED`                              |
| `patch_verifier`   | `PATCH_VERIFIED_TEMP_ONLY`, `PATCH_VERIFIER_FAILED`, `VERIFIER_MISSING`|
| `source_approval`  | `SOURCE_APPROVAL_REQUIRED`, `SOURCE_APPROVAL_ACCEPTED_FIXTURE`, `SOURCE_MUTATION_BLOCKED` |
| `corpus_eligibility` | `CORPUS_ELIGIBILITY_FALSE` (always — for now)                        |

Plus two scalars:

* `source_mutation_authorized: bool` — True only when approval was
  accepted; False otherwise.
* `training_eligible: bool` — always False at this rung.

## Evidence pointers

The state record carries `evidence.locks` and `evidence.evidence_files`
arrays. Pass them at construction time:

```python
state = build_ide_state(
    trace,
    approval=approval_decision,
    lock_paths=("locks/sentinel/MODEL_ROUTER_LOCK_001.json",),
    evidence_paths=("assurance/evidence/model_router/run_20260527.json",),
)
```

A consumer can deep-link these — open the lock file, render the
evidence — without re-running anything.

## Required vs blocked

A subtle but important distinction:

* `SOURCE_APPROVAL_REQUIRED` — no packet was submitted yet. The IDE
  should render an "approve?" surface.
* `SOURCE_MUTATION_BLOCKED` — a packet *was* submitted and refused
  (mismatch, missing field, etc.). The IDE should render the failure
  reason from the `ApprovalGateDecision`.

The state model distinguishes these — `required` does not collapse to
`blocked`.

## What this lock does *not* do

* No UI implementation. Tauri/web rendering is downstream.
* No I/O. The state model is a pure function of its inputs.
* No live operator admission — approval is still FIXTURE-only.
* No corpus row write.

## Reproducing the evidence

```
.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_repair_state_model_lock.py -q --tb=short
```
