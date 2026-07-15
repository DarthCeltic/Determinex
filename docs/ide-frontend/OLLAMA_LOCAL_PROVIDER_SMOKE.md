# Ollama Local Provider Smoke

> Locked under `locks/sentinel/OLLAMA_LOCAL_PROVIDER_SMOKE_LOCK_001.json`.

`scripts/models/ollama_local_provider_smoke.py` performs a bounded
localhost availability probe of a local Ollama daemon.

Rules:

- Default = `BLOCKED_NOT_CONFIGURED`. Callers must explicitly pass a
  localhost `endpoint` to opt in.
- Only `127.0.0.1`, `localhost`, `::1` accepted; anything else returns
  `BLOCKED_NOT_CONFIGURED`.
- Strict timeout (default 1.5s).
- Stdlib `urllib` only — no `requests`, no `httpx`.
- Output is always recorded as untrusted (`OLLAMA_PROVIDER_OUTPUT_UNTRUSTED`).
- No repo/source input. No patch generation. No corpus write. No
  training-eligibility change.

The probe is transport-pluggable so tests verify the gate logic
without opening a real socket.
