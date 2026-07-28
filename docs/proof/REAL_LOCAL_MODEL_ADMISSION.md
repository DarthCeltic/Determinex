# Real Local Model Admission

> Locked under `locks/sentinel/REAL_LOCAL_MODEL_ADMISSION_LOCK_001.json`.

`scripts/models/real_local_model_admission.py` is the gate that admits
one real local model for one or more task classes. It is a pure
decision surface — no model invocation, no network, no subprocess.

Admits only when ALL of:

- provider is in the local set (`ollama`, `local_hf`,
  `executable_adapter`) and is not `no_model`
- when provider is `ollama`, a `RealOllamaProviderDetectionRecord` with
  `decision == REAL_OLLAMA_PROVIDER_DETECTED` is supplied
- `model_id ∈ CURRENT_MODEL_IDS`
- `model_id ∉ STALE_MODEL_IDS`
- every requested task class is in the supported set
- caller passed `opt_in=True`

Refusal codes: `BLOCKED_NETWORK_PROVIDER`, `BLOCKED_NO_PROVIDER`,
`BLOCKED_STALE`, `BLOCKED_UNPINNED`, `BLOCKED_UNSUPPORTED_TASK_CLASS`,
`BLOCKED_NOT_OPTED_IN`.

Every record carries `source_mutation_authorized=False`,
`training_eligible=False`, `network_provider_admitted=False`,
`dry_run_default=True`.
