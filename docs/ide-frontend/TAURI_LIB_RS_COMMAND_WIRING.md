# Tauri lib.rs Command Wiring

> Locked under `locks/sentinel/TAURI_LIB_RS_COMMAND_WIRING_LOCK_001.json`.

Registers the standalone `ide_repair_bridge` module's 10 commands inside
`frontend/src-tauri/src/lib.rs` so the Tauri runtime exposes them to the
frontend invoke client. `cargo check` passes.

The wiring:

- `mod ide_repair_bridge;` added near the other `mod` declarations
- 10 commands appended to the `tauri::generate_handler!` macro:
  `open_workspace`, `get_workspace_status`, `get_model_route_status`,
  `diagnose_dry_run`, `diagnose_live_opt_in`, `generate_patch_plan`,
  `verify_temp_patch`, `get_human_approval_packet`,
  `source_apply_dry_run`, `get_repair_flow_state`

All commands route through `scripts/ide/_tauri_driver.py`, which only
calls the locked `IDEBackendCommandSurface`. No source mutation. No
live model call. No training-eligibility change. No network provider
admission.
