# Local Model Admission Policy

> Locked under `locks/sentinel/LOCAL_MODEL_ADMISSION_POLICY_LOCK_001.json`.
> Evidence: `assurance/evidence/local_model_admission_policy/run_20260527.json`.

This is the policy that decides whether a local model *could*
eventually be admitted to participate in the apparatus. It admits
**metadata only** — no model is called, no subprocess runs, no network
is consulted. Even `LOCAL_MODEL_METADATA_ADMITTED` keeps
`execution_authorized=False`; live admission is a separate, later rung.

## Candidate metadata

```python
@dataclass(frozen=True)
class LocalModelCandidate:
    model_id: str
    provider: str            # "ollama" | "local_hf" | "executable_adapter" | "no_model"
    capability_tags: tuple[str, ...]
    supported_task_classes: tuple[str, ...]
    requires_network: bool = False
    declared_local: bool = True
```

## Admission checks (in order)

1. Provider must be a known `ModelProvider` enum value.
2. `model_id` must NOT be in `STALE_MODEL_IDS` (from
   `MODEL_ROUTER_LOCK_001`).
3. `requires_network=True` is rejected unless
   `config.allow_network_models=True`.
4. `model_id` must be in `CURRENT_MODEL_IDS` unless
   `config.allow_unverified_ids=True`. The `no_model` provider bypasses
   this.
5. At least one `capability_tag` must be declared (except for
   `no_model`).
6. `supported_task_classes` must overlap with
   `config.allowed_task_classes` (except for `no_model`).

## Decisions (closed set)

| Status                                       | Meaning                                                |
|----------------------------------------------|--------------------------------------------------------|
| `LOCAL_MODEL_ADMISSION_REQUIRED`             | UI-default; awaiting candidate                         |
| `LOCAL_MODEL_METADATA_ADMITTED`              | All checks passed; live admission still required       |
| `LOCAL_MODEL_BLOCKED_UNKNOWN_PROVIDER`       | Provider not in enum                                   |
| `LOCAL_MODEL_BLOCKED_STALE_ID`               | model_id in STALE_MODEL_IDS                            |
| `LOCAL_MODEL_BLOCKED_NETWORK_MODEL`          | requires_network=True under conservative policy        |
| `LOCAL_MODEL_BLOCKED_UNVERIFIED_ID`          | model_id not in CURRENT_MODEL_IDS                      |
| `LOCAL_MODEL_BLOCKED_MISSING_CAPABILITIES`   | No capability tags declared                            |
| `LOCAL_MODEL_BLOCKED_UNSUPPORTED_TASK_CLASS` | No overlap with allowed task classes                   |

## Why metadata-only

A live admission probe would need to call `ollama list` (or equivalent)
through the hardened runner. That introduces a subprocess seam. This
rung admits metadata so that:

* The IDE can render an "approve this model" surface.
* The policy logic is testable without invoking any model.
* A future `LOCAL_MODEL_LIVE_ADMISSION_LOCK_001` can consume admitted
  metadata + opt-in probe + matching capability assertion to actually
  open `execution_authorized`.

## What this lock does *not* do

* No live model probe. No `ollama list`. No subprocess.
* No network. No T:/ dependency.
* No flipping of `execution_authorized` or `training_eligible` under
  any decision.
* No corpus row write.

## Reproducing the evidence

```
.\.venv\Scripts\python.exe -m pytest tests/models/test_local_model_admission_policy_lock.py -q --tb=short
```
