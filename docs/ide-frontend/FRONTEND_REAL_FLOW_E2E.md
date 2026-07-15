# Frontend Real Flow E2E

> Locked under `locks/sentinel/FRONTEND_REAL_FLOW_E2E_LOCK_001.json`.

Drives the 9-stage repair flow through the production
`_tauri_driver._dispatch` (the same function the Rust bridge invokes
in production). Each stage attaches an evidence_ref pointing at the
existing locked run_*.json for the panel it represents.

| # | Stage | Tauri command | Expected status |
|---|---|---|---|
| 1 | open workspace | `open_workspace` | `OK` |
| 2 | inspect status | `get_workspace_status` | `OK` |
| 3 | route model | `get_model_route_status` | `OK` |
| 4 | diagnose dry-run | `diagnose_dry_run` | `TEMP_ONLY` |
| 5 | patch plan quarantine | `generate_patch_plan` (opt_in=false) | `BLOCKED_NOT_OPTED_IN` |
| 6 | temp verify | `verify_temp_patch` | `TEMP_ONLY` |
| 7 | approval packet | `get_human_approval_packet` | `SOURCE_MUTATION_BLOCKED` |
| 8 | source apply dry-run | `source_apply_dry_run` | `OK` |
| 9 | evidence viewer | `get_repair_flow_state` | `OK` |

Trace invariants verified by the runner:

- `source_unchanged: true`
- `approval_required: true`
- `training_eligible: false`
- `network_called: false`
- `docker_used: false`
- `frontend_backend_states_agree: true`

No subprocess. No socket. No Docker. No live model call. No training row.
