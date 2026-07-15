# Model Router

> Locked under `locks/sentinel/MODEL_ROUTER_LOCK_001.json`.
> Evidence: `assurance/evidence/model_router/run_20260527.json`.

The model router is the gatekeeper that decides **when and how a model is
allowed to participate** in any Determinex task. It is intentionally narrow:
it produces a structured `RouteRecord` and nothing else. It never invokes
a model. It never calls a subprocess. It never touches the network. It
never reads from the fast-drive. It never writes to the corpus.

## Core principle

> The model is replaceable. The apparatus decides when and how a model is
> allowed to participate.

The router is the apparatus's "yes/no/maybe-with-this-fallback" surface.
The caller is responsible for honoring the record's `execution_authorized`
boolean before doing anything live.

## Public surface

```python
from models.model_router import (
    ModelRouter, TaskClass, ModelRole, RouteDecision, RouterMode,
    RouterConfig, DEFAULT_ROUTES, CURRENT_MODEL_IDS, STALE_MODEL_IDS,
)
from models.model_router_record import RouteRecord
from models.model_inventory import LocalModelInventory
```

## Task classes

| Task class                  | Preferred role          | Fallback chain                                    |
|-----------------------------|-------------------------|---------------------------------------------------|
| `REPO_TRIAGE`               | `FAST_LOCAL`            | `STRONG_LOCAL → NO_MODEL`                         |
| `BUILD_DIAGNOSIS`           | `CODE_SPECIALIST`       | `STRONG_LOCAL → FAST_LOCAL → NO_MODEL`            |
| `TEST_FAILURE_LOCALIZATION` | `CODE_SPECIALIST`       | `STRONG_LOCAL → NO_MODEL`                         |
| `PATCH_PLANNING`            | `REASONING_SPECIALIST`  | `CODE_SPECIALIST → NO_MODEL`                      |
| `PATCH_GENERATION`          | `CODE_SPECIALIST`       | `NO_MODEL`                                        |
| `PATCH_REVIEW`              | `REASONING_SPECIALIST`  | `CODE_SPECIALIST → NO_MODEL`                      |
| `VERIFIER_SUMMARY`          | `FAST_LOCAL`            | `NO_MODEL`                                        |
| `CORPUS_ELIGIBILITY_REVIEW` | `REASONING_SPECIALIST`  | `CODE_SPECIALIST → NO_MODEL`                      |
| `GENERAL_EXPLANATION`       | `FAST_LOCAL`            | `NO_MODEL`                                        |
| `UNKNOWN`                   | _intentionally absent_  | _fails closed: `ROUTE_BLOCKED_UNSUPPORTED_TASK_CLASS`_ |

## Model roles

* `FAST_LOCAL` — cheap, fast, locally hosted (default mapping:
  `determinex-observer-v6-dsl`)
* `STRONG_LOCAL` — heavier reasoner running locally
  (`determinex-sentinel-v5-dsl`)
* `CODE_SPECIALIST` — code-tuned model (`determinex-engineer-v11-dsl`)
* `REASONING_SPECIALIST` — high-quality reasoner
  (`determinex-sentinel-v5-dsl` by default; can be remapped to a cloud
  reasoning model with `allow_unverified_model_ids=True`)
* `NO_MODEL` — sentinel terminus; no inference needed

## Route decisions

* `ROUTE_SELECTED` — preferred role available, live mode, ready to invoke
* `ROUTE_DRY_RUN_SELECTED` — preferred role available, dry-run, no
  invocation authorized
* `ROUTE_FALLBACK_SELECTED` — preferred role unavailable, fallback
  selected, live
* `ROUTE_NO_MODEL_REQUIRED` — chain ended at `NO_MODEL` (intentional)
* `ROUTE_BLOCKED_NO_AVAILABLE_MODEL` — chain exhausted without a
  `NO_MODEL` terminus (config bug)
* `ROUTE_BLOCKED_STALE_MODEL_ID` — a configured role mapped to a
  superseded id in `STALE_MODEL_IDS`
* `ROUTE_BLOCKED_UNSUPPORTED_TASK_CLASS` — task class not in
  `DEFAULT_ROUTES` (including `UNKNOWN`)

## Router modes

* `dry_run` (default) — produce a record; `execution_authorized` stays
  `False`. The caller may inspect the record, log it, or feed it to a
  mocked-call fixture (see `LLM_MOCKED_INTAKE_REPAIR_LOCK_001`).
* `live` — produce a record with `execution_authorized=True` if and only
  if the chosen role's model id is in `CURRENT_MODEL_IDS` (or
  `allow_unverified_model_ids=True`) and is present in the inventory.

`live` mode **alone** never opens corpus writes or training eligibility.
Those gates are owned by separate locks.

## Stale model id detection

Configured ids are checked against `STALE_MODEL_IDS` *before* the
inventory probe. Hitting a stale id short-circuits the entire route call
with `ROUTE_BLOCKED_STALE_MODEL_ID` — independent of mode, independent of
whether the id happens to still be on the host.

`STALE_MODEL_IDS` currently contains the v10/v5 defaults that were
discovered as hard-coded defaults in `scripts/codebase_explorer.py`
during the gap-to-100 audit, plus the rest of the documented superseded
generations (v9/v8/v4/v3/v2 across the engineer/observer/sentinel
families).

## Configuration

Configuration is via constructor injection plus the existing env-var
spine. A YAML wrapper was suggested in the directive — deferred so that
`DEFAULT_ROUTES` remains the single source of truth and the lock's
reproducibility invariant stays straightforward.

```python
cfg = RouterConfig(
    default_mode=RouterMode.DRY_RUN,
    allow_network_models=False,
    allow_unverified_model_ids=False,
)
inv = LocalModelInventory.from_env()  # reads DETERMINEX_*_MODEL + DETERMINEX_ROUTER_AVAILABLE_MODELS
router = ModelRouter(config=cfg, inventory=inv)

rec = router.route(TaskClass.BUILD_DIAGNOSIS, mode=RouterMode.DRY_RUN)
if rec.execution_authorized:
    # The router NEVER sets this in dry-run.
    ...
```

For tests, inject an inventory directly:

```python
inv = LocalModelInventory.of(["determinex-engineer-v11-dsl"])
router = ModelRouter(inventory=inv)
```

## What this lock does *not* do

* No live availability probe of Ollama (`ollama list`). The inventory is
  a passive view; live probing is deferred to
  `MODEL_ROUTER_LIVE_LOCAL_MODEL_ADMISSION_LOCK_001`.
* No network model gating beyond the `allow_network_models` config flag.
  The caller in `LLM_MOCKED_INTAKE_REPAIR_LOCK_001` will compose against
  it.
* No deletion of `scripts/model_advisor.py`. Its recommendations may be
  wrapped as a router signal in a later rung.
* No automatic flipping of corpus or training eligibility. Those gates
  are independent.

## Reproducing the evidence

```
.\.venv\Scripts\python.exe -m pytest tests/models/test_model_router_lock.py -q --tb=short
.\.venv\Scripts\python.exe -m scripts.dev.architecture_regression_gauntlet
.\.venv\Scripts\python.exe -m scripts.determinex_cli evidence validate
```
