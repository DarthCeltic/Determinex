# Real Ollama Provider Detection

> Locked under `locks/sentinel/REAL_OLLAMA_PROVIDER_DETECTION_LOCK_001.json`.

`scripts/models/real_ollama_provider_detection.py` is a read-only
two-step probe of a real local Ollama provider:

1. `shutil.which("ollama")` — locate the CLI binary
2. GET `<endpoint>/api/tags` — confirm the daemon is running and
   capture the model name list

Rules:

- localhost-only (`127.0.0.1`, `localhost`, `::1`); non-local hosts
  return `REAL_OLLAMA_PROVIDER_BLOCKED_NETWORK_PROVIDER`
- strict timeout (default 1.5s)
- stdlib `urllib` only — no `requests`/`httpx`
- no live inference, no model pull, no ollama subcommand spawned
- decisions: `DETECTED` / `BLOCKED_NOT_INSTALLED` / `BLOCKED_NOT_RUNNING`
  / `BLOCKED_TIMEOUT` / `BLOCKED_NETWORK_PROVIDER`

The probe is transport- and binary-locator-pluggable so tests can
exercise every gate without opening a socket.
