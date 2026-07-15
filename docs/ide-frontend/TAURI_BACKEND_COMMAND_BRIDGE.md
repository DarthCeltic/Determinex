# Tauri Backend Command Bridge

> Locked under `locks/sentinel/TAURI_BACKEND_COMMAND_BRIDGE_LOCK_001.json`.

Stable Python backend bridge API a Tauri (or web/CLI) frontend can
consume via FFI/IPC/HTTP. 10 Tauri-style commands wrapping the existing
`IDEBackendCommandSurface`.

**This rung does not modify any Tauri/Rust files.** It pins the Python
side so the Tauri/Rust side can wire in when ready.

## Commands

* `open_workspace`
* `get_workspace_status`
* `get_model_route_status`
* `diagnose_dry_run`
* `diagnose_live_opt_in`
* `generate_patch_plan`
* `verify_temp_patch`
* `get_human_approval_packet`
* `source_apply_dry_run`
* `get_repair_flow_state`

source_mutation_authorized and training_eligible are False on every
response.
