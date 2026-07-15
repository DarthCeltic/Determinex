# Live Model Compatibility Harness

> Locked under `locks/sentinel/LIVE_MODEL_MOCK_COMPATIBILITY_HARNESS_LOCK_001.json`.

Fixture-provider harness that exercises the live-model interface
shape without ever invoking a real model. Six fixture providers cover
the safety surface: deterministic, unavailable, timeout, malformed,
oversized, empty.

## Safety checks (in order)

1. provider availability (`provider.available`)
2. provider invocation exceptions (timeout, unavailable, generic)
3. response is a `dict`
4. response is JSON-encodable
5. response size <= 64 kB
6. response is non-empty
7. response has the schema's required keys

## Invariant

Every `LiveModelResponse` is `trusted=False` — including the PASSED
ones. Downstream rungs apply the trust gates.
