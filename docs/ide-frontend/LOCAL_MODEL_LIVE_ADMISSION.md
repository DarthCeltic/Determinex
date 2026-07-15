# Local Model Live Admission

> Locked under `locks/sentinel/LOCAL_MODEL_LIVE_ADMISSION_LOCK_001.json`.

The opt-in, bounded, evidence-recorded gate that admits live local
model usage. Dry-run is the default; live admission requires both
`mode=OPT_IN_LIVE` and `opt_in_live=True`.

## Decision matrix (closed set)

| Status                                                       | When                                              |
|--------------------------------------------------------------|---------------------------------------------------|
| `LOCAL_MODEL_LIVE_ADMISSION_READY`                           | All checks passed; `live_call_authorized=True`    |
| `LOCAL_MODEL_LIVE_ADMISSION_METADATA_ONLY`                   | Base policy refused (e.g. missing capabilities)   |
| `LOCAL_MODEL_LIVE_ADMISSION_BLOCKED_DRY_RUN_DEFAULT`         | Default mode is dry_run                           |
| `LOCAL_MODEL_LIVE_ADMISSION_BLOCKED_NO_CONFIG`               | `opt_in_live=False`                               |
| `LOCAL_MODEL_LIVE_ADMISSION_BLOCKED_MISSING_INVENTORY`       | No inventory or empty inventory                   |
| `LOCAL_MODEL_LIVE_ADMISSION_BLOCKED_NETWORK_PROVIDER`        | Network provider under conservative policy        |
| `LOCAL_MODEL_LIVE_ADMISSION_BLOCKED_UNKNOWN_PROVIDER`        | Provider not in known local set                   |
| `LOCAL_MODEL_LIVE_ADMISSION_BLOCKED_STALE_MODEL_ID`          | model_id in STALE_MODEL_IDS                       |
| `LOCAL_MODEL_LIVE_ADMISSION_BLOCKED_UNPINNED_MODEL`          | model_id not in CURRENT_MODEL_IDS                 |
| `LOCAL_MODEL_LIVE_ADMISSION_BLOCKED_UNSUPPORTED_TASK_CLASS`  | task_class not in allowed set                     |
| `LOCAL_MODEL_LIVE_ADMISSION_BLOCKED_MODEL_UNAVAILABLE`       | Inventory non-empty but lacks the model           |

## Hard invariant

**Every** decision keeps `source_mutation_authorized=False`,
`corpus_write_authorized=False`, `training_eligible=False`. These
remain independent gates. Live admission only opens the
`live_call_authorized` flag.
