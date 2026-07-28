# Real Local Model Healthcheck

> Locked under `locks/sentinel/REAL_LOCAL_MODEL_HEALTHCHECK_LOCK_001.json`.

`scripts/models/real_local_model_healthcheck.py` POSTs a trivial
fixed prompt (`Reply with the single word 'OK'.`) to the local
`/api/generate` endpoint and records whether the daemon responded
within a strict timeout.

Rules:

- Selection record must be `CANONICAL_LOCAL_MODEL_SELECTED`
- Default endpoint is `http://127.0.0.1:11434`; non-local hosts
  are refused as `BLOCKED_PROVIDER_UNAVAILABLE`
- Bounded timeout (default 5 s; this-host run allowed up to 60 s
  for first-time model warm-up)
- Output is always recorded as untrusted; response is capped at
  256 chars
- Stdlib `urllib` only; no `requests`/`httpx`
- **NO source/repo content** is included in the prompt; the
  prompt is a fixed string at module scope

Decisions: `PASSED`, `BLOCKED_NOT_SELECTED`, `BLOCKED_MODEL_NOT_PULLED`,
`BLOCKED_PROVIDER_UNAVAILABLE`, `BLOCKED_TIMEOUT`,
`BLOCKED_PROVIDER_ERROR`. `OUTPUT_UNTRUSTED` is always present in
`statuses_seen`.
