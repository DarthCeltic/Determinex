# Real Local Model Provider Config

> Locked under `locks/sentinel/REAL_LOCAL_MODEL_PROVIDER_CONFIG_LOCK_001.json`.

`scripts/models/real_local_model_provider_config.py` is the production
save path for local-model configs. It wraps the already-locked
`LocalModelConfigWizard` and adds the rung's exact status tokens plus
a deterministic on-disk root at
`assurance/runtime/local_model_configs/`.

Supported providers: `no_model`, `ollama`, `local_hf`,
`executable_adapter`. Defaults: `enabled=False`, `dry_run_default=True`.

Hard refusals:

- network providers (`anthropic`, `openai`, `google`, `deepseek`,
  `gemini`, `openrouter`, …) →
  `REAL_LOCAL_MODEL_CONFIG_BLOCKED_NETWORK_PROVIDER`
- unknown providers → `BLOCKED_UNKNOWN_PROVIDER`
- stale ids (`determinex-engineer-v10-dsl`, etc.) → `BLOCKED_STALE_MODEL_ID`
- unpinned ids (not in `CURRENT_MODEL_IDS`) → `BLOCKED_UNPINNED_MODEL`
- config root unwritable → `BLOCKED_INVALID_LOCATION`

Save never calls a live model. `RealLocalModelProviderConfigRecord`
serializes with `live_model_called_on_save=false` and
`network_provider_admitted=false` for every code path.
