# Mocked Intake → Diagnose → Repair Loop

> Locked under `locks/sentinel/LLM_MOCKED_INTAKE_REPAIR_LOCK_001.json`.
> Evidence: `assurance/evidence/llm_mocked_intake_repair/run_20260527.json`.

The mocked intake/diagnose/repair loop is the first end-to-end shape
proof of the Claude lane's verified-repair apparatus. It runs the
canonical task-class pipeline against a fixture workspace and produces a
deterministic trace — without ever invoking a real model, calling the
network, spawning a subprocess, or mutating the fixture.

## Pipeline

```
workspace
  → BuildAdapterRegistry.select()
  → ModelRouter.route(BUILD_DIAGNOSIS, LIVE)
  → MockModelClient.invoke(BUILD_DIAGNOSIS)
  → ModelRouter.route(PATCH_PLANNING, LIVE)
  → MockModelClient.invoke(PATCH_PLANNING)
  → ModelRouter.route(PATCH_GENERATION, LIVE)
  → MockModelClient.invoke(PATCH_GENERATION)
  → ModelRouter.route(VERIFIER_SUMMARY, LIVE)
  → MockModelClient.invoke(VERIFIER_SUMMARY)
  → MockedIntakeRepairTrace
```

## Fixtures

| Fixture                                       | Build system | Expected terminus     |
|-----------------------------------------------|--------------|-----------------------|
| `tests/fixtures/intake/python_broken/`        | `pip`        | `MOCK_LOOP_COMPLETE`  |
| `tests/fixtures/intake/rust_broken/`          | `cargo`      | `MOCK_LOOP_COMPLETE`  |
| `tests/fixtures/intake/go_broken/`            | `go`         | `MOCK_LOOP_COMPLETE`  |
| `tests/fixtures/intake/ts_broken/`            | `npm`        | `MOCK_LOOP_COMPLETE`  |
| `tests/fixtures/intake/unsupported_repo/`     | `unknown`    | `UNSUPPORTED_REPO`    |

Every fixture's sha256 tree is hashed before and after `loop.run()`; any
divergence raises `_SourceMutationError`.

## Termini and statuses

* `MOCK_LOOP_COMPLETE` — all four pipeline steps invoked the mock
* `UNSUPPORTED_REPO` — `UnknownAdapter` selected; no mock invocations
* `ROUTER_BLOCKED` — router refused BUILD_DIAGNOSIS and PATCH_PLANNING
  (e.g. empty inventory triggered NO_MODEL terminus)

Lock-level status tokens:

```
DIAGNOSE_MOCK_ROUTE_SELECTED
PATCH_PLAN_MOCK_GENERATED
PATCH_NOT_APPLIED_TO_SOURCE
VERIFIER_RESULT_CAPTURED
TRAINING_ELIGIBLE_FALSE
EVIDENCE_WRITTEN
UNSUPPORTED_REPO_BLOCKED
NO_NETWORK_CALL_MADE
NO_SUBPROCESS_CALL_MADE
NO_SOURCE_MUTATION
```

## Mock client contract

`MockModelClient` takes a `{TaskClass: dict}` mapping at construction
time. `invoke()` enforces two invariants:

* If the route record is not `execution_authorized`, raise
  `RouteNotAuthorizedError`. The mock refuses to fabricate output for a
  blocked route.
* If the task class is not in the canned mapping, raise `KeyError`. The
  fixture must enumerate every class it intends to exercise.

The client records every call in `calls: tuple[MockedCall, ...]`, which
the trace consumes.

## What this lock does *not* do

* No real toolchain invocation (`cargo check`, `pytest`, `tsc`, etc.).
  Toolchain runs in temp workspaces are deferred to
  `SAFE_PATCH_DIFF_ROLLBACK_LOCK_001`.
* No real LLM provider integration. Live providers are deferred to
  `LOCAL_MODEL_ADMISSION_POLICY_LOCK_001`.
* No patch application. The mocked patch diff is returned as data only;
  the loop carries `patch_not_applied_to_source=True`.
* No corpus row write. `training_eligible` is `False` on every path.

## Reproducing the evidence

```
.\.venv\Scripts\python.exe -m pytest tests/intake/test_llm_mocked_intake_repair_lock.py -q --tb=short
```
