# Local Model Settings Panel

> Locked under `locks/sentinel/LOCAL_MODEL_SETTINGS_PANEL_LOCK_001.json`.

UI for configuring a local model. Provider (no_model / ollama / local_hf /
executable_adapter), model id, digest, capabilities, allowed task classes,
`dry_run_default` toggle (default true), and a live opt-in warning checkbox.

Network/cloud providers (anthropic, openai, google, deepseek, gemini,
openrouter, vllm-remote, cloud, network) are blocked outright. Known stale
model ids show a warning and disable Save. Save posts metadata only — no
live model call is performed.
