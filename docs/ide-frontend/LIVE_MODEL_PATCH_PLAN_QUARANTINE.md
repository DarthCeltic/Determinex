# Live Model Patch-Plan Quarantine

> Locked under `locks/sentinel/LIVE_MODEL_PATCH_PLAN_QUARANTINE_LOCK_001.json`.

Allows an admitted live/local model to produce a patch *plan*. The
plan is validated, quarantined, and stored as evidence — never
trusted, never applied. The next rung (temp-patch verifier gate)
consumes quarantined plans and applies them to a temp workspace only.

## Plan entry shape

```json
{"operation": "replace_file", "path": "src/x.py", "new_content": "..."}
```

Only `replace_file` is supported. Each entry is validated for:

* operation (must be `replace_file`)
* path (no `..`, no absolute, no drive-anchored)
* content (UTF-8 text; no NUL bytes)
* size (≤ 2 MB per entry, ≤ 16 MB cumulative)

## Decisions (closed set)

| Status                                         | When                                  |
|------------------------------------------------|---------------------------------------|
| `PATCH_PLAN_QUARANTINED`                       | All entries validated                 |
| `PATCH_PLAN_BLOCKED_MODEL_NOT_ADMITTED`        | Admission record not READY            |
| `PATCH_PLAN_BLOCKED_SCHEMA_INVALID`            | Empty plan or non-dict entry          |
| `PATCH_PLAN_BLOCKED_UNSUPPORTED_OPERATION`     | Operation other than replace_file     |
| `PATCH_PLAN_BLOCKED_PATH_ESCAPE`               | Path traversal / absolute / drive     |
| `PATCH_PLAN_BLOCKED_BINARY_CONTENT`            | NUL byte in content                   |
| `PATCH_PLAN_BLOCKED_OVERSIZED`                 | Per-entry > 2 MB or total > 16 MB     |

## Hard invariants

* `trusted=False` on every plan
* `applied_to_source=False` on every plan
* `applied_to_temp_workspace=False` on every plan (this is rung 5's job)
* `source_mutation_authorized=False`
* `corpus_write_authorized=False`
* `training_eligible=False`
