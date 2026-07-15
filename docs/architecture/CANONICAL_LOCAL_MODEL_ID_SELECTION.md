# Canonical Local Model ID Selection

> Locked under `locks/sentinel/CANONICAL_LOCAL_MODEL_ID_SELECTION_LOCK_001.json`.

`scripts/models/canonical_local_model_id_selection.py` picks a single
canonical local model id from `CURRENT_MODEL_IDS` and classifies the
current host into one of:

| host_state | decision |
|---|---|
| `MODEL_AVAILABLE` | `CANONICAL_LOCAL_MODEL_SELECTED` |
| `MODEL_NOT_PULLED` | `BLOCKED_NOT_PULLED` |
| `PROVIDER_NOT_RUNNING` | `BLOCKED_PROVIDER_UNAVAILABLE` |
| `PROVIDER_NOT_RECOGNIZED` | `BLOCKED_PROVIDER_UNAVAILABLE` |
| `PREFERRED_STALE` | `BLOCKED_STALE_ID` |
| `PREFERRED_UNPINNED` | `BLOCKED_UNPINNED` |
| `NETWORK_PROVIDER` | `BLOCKED_NETWORK_PROVIDER` |

When the canonical id is missing, the record's `operator_action`
field carries the exact command (e.g. `ollama pull <id>`). No model
invocation, no pull, no network call.
