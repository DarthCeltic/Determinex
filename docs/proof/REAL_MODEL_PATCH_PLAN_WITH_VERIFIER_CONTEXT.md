# Real Model Patch Plan With Verifier Context

> Locked under `locks/sentinel/REAL_MODEL_PATCH_PLAN_WITH_VERIFIER_CONTEXT_LOCK_001.json`.

`scripts/repair/real_model_patch_plan_with_verifier_context.py`
consumes a model-supplied structured patch plan and runs it
through the locked `REAL_PATCH_PLAN_QUARANTINE_LOCK_001` validator,
attaching the verifier context (build_system_id, verifier argv) to
the resulting record.

Gates:

- healthcheck `PASSED`
- verifier selection `SELECTED`
- explicit `opt_in=True`

Schema / path / op rejections from the locked quarantine validator
map to namespaced decisions:

| Inner decision | This rung's decision |
|---|---|
| `REAL_PATCH_PLAN_QUARANTINED` | `QUARANTINED` |
| `BLOCKED_SCHEMA_INVALID` | `BLOCKED_SCHEMA_INVALID` |
| `BLOCKED_PATH_ESCAPE` | `BLOCKED_PATH_ESCAPE` |
| `BLOCKED_UNSUPPORTED_OPERATION` | `BLOCKED_UNSUPPORTED_OPERATION` |

`patch_applied=False`, `source_mutation_authorized=False`,
`training_eligible=False`, `output_trusted=False`,
`OUTPUT_UNTRUSTED` always in `statuses_seen`.
