# Real Live Diagnose Only

> Locked under `locks/sentinel/REAL_LIVE_DIAGNOSE_ONLY_LOCK_001.json`.

`scripts/models/real_live_diagnose_only.py` POSTs to a localhost
`/api/generate` endpoint to produce an advisory diagnostic summary.
Output is always recorded as untrusted; the verifier remains the
source of truth.

Gate ladder:

1. `admission` must be `REAL_LOCAL_MODEL_ADMITTED`
2. `opt_in=True` required
3. `task_class` must be in `admission.task_classes_admitted`
4. With the default transport, endpoint must be localhost
5. Bounded timeout (default 5 s)
6. Empty / oversize text is bounded; non-2xx → `BLOCKED_PROVIDER_ERROR`

Decisions: `WRITTEN`, `BLOCKED_NO_MODEL`, `BLOCKED_NOT_OPTED_IN`,
`BLOCKED_TIMEOUT`, `BLOCKED_PROVIDER_ERROR`. `ADVISORY_ONLY` is
always present in `statuses_seen`. Pluggable transport for tests.

Stdlib `urllib` only; no `requests`/`httpx`. No patch generation, no
source mutation, no training row, no network provider.
