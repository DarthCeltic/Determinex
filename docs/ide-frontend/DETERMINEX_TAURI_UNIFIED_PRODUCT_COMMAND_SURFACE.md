# Tauri Unified Product Command Surface

> Locked under
> `locks/sentinel/DETERMINEX_TAURI_UNIFIED_PRODUCT_COMMAND_SURFACE_LOCK_001.json`.

Rung 1 of `DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_SERIES`.

## 8 read-only commands

| Tauri verb | Returns |
|---|---|
| `get_unified_product_navigation_model` | locked 5-surface model + shared authority vocabulary |
| `get_idea_lab_workflow_state` | 14 flow steps + 11 UI states + capability flags |
| `get_repo_clinic_workflow_state` | 17 flow steps + 13 UI states |
| `get_maintenance_bay_workflow_state` | 8 maintenance types + 8 UI states |
| `get_learning_studio_workflow_state` | 9 modes + non-authorizing flag |
| `get_proof_operator_center_state` | 10 required sections + read-only flags |
| `get_user_level_teaching_windows` | 8 user levels + invariants |
| `get_unified_splash_demo_spec` | 5-step demo + required tagline / phrases / caveats |

Each handler returns a deterministic JSON-serializable snapshot of
its lock module's view-model. Every payload declares
`source_mutation_authorized: false` and `training_eligible: false`.

## Hard rules

- **Command name matches behavior.** Tests forbid any verb
  containing `apply_source`, `write_training`, `train_`,
  `approve_packet`, `run_programbench`, `import_artifact`,
  `scan_artifact`, `grant`, `release`, or `deploy`.
- **No mutating command added.** The 8 commands are read-only.
- **No authorization leak.** Every CommandResult emits
  `source_mutation_authorized=False` and `training_eligible=False`.
- **No new approval-granting verb.** Existing approval/apply gates
  remain authoritative.
- **No ProgramBench write surface.** ProgramBench / provenance stays
  read-only from the Claude lane.
