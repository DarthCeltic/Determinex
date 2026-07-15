# Ollama Model Pull Operator Guide

> Locked under `locks/sentinel/OLLAMA_MODEL_PULL_OPERATOR_GUIDE_LOCK_001.json`.

`scripts/models/ollama_model_pull_operator_guide.py` consumes a
`CanonicalLocalModelIdSelectionRecord` and produces an operator guide
ONLY when the canonical model is missing.

| Selection decision | Guide decision |
|---|---|
| `CANONICAL_LOCAL_MODEL_SELECTED` | `OPERATOR_GUIDE_NOT_NEEDED_MODEL_AVAILABLE` |
| `BLOCKED_NOT_PULLED` | `OPERATOR_GUIDE_WRITTEN` |
| `BLOCKED_NETWORK_PROVIDER` | `OPERATOR_GUIDE_BLOCKED_NETWORK_PROVIDER` |
| `BLOCKED_PROVIDER_UNAVAILABLE` | `OPERATOR_GUIDE_BLOCKED_PROVIDER_UNAVAILABLE` |
| `BLOCKED_STALE_ID` | `OPERATOR_GUIDE_BLOCKED_STALE_ID` |
| `BLOCKED_UNPINNED` | `OPERATOR_GUIDE_BLOCKED_UNPINNED` |

When written, the record carries:

- `expected_command` (e.g. `ollama pull determinex-engineer-v11-dsl`)
- `safety_warning` (a long-form note describing trust boundaries)
- `next_validation_command` (the pytest invocation that re-checks
  selection + healthcheck)

This lock NEVER auto-pulls. Autopull is intentionally deferred to a
separately-locked future rung that requires an explicit policy gate.
