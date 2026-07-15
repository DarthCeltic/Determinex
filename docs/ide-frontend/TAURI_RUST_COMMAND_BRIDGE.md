# Tauri Rust Command Bridge

> Locked under `locks/sentinel/TAURI_RUST_COMMAND_BRIDGE_LOCK_001.json`.

A standalone Tauri Rust module (`frontend/src-tauri/src/ide_repair_bridge.rs`)
that fronts the locked Python backend command surface. The Rust file
declares 10 `#[tauri::command]` functions, each of which shells out via
argv-list (no shell strings) to `scripts/ide/_tauri_driver.py`, which
in turn calls `IDEBackendCommandSurface`.

**This rung deliberately does NOT modify `src-tauri/src/lib.rs`** so the
frontend team can wire the module in on their own audited path. The
recipe below is the change they would apply.

## Integration recipe

In `frontend/src-tauri/src/lib.rs`:

1. Add a mod declaration next to the other `mod` lines:

   ```rust
   mod ide_repair_bridge;
   ```

2. Append the 10 commands to the existing `tauri::generate_handler!`
   invocation (alphabetical order matches the module's
   `IDE_REPAIR_COMMANDS` constant):

   ```rust
   .invoke_handler(tauri::generate_handler![
       // ...existing commands...
       ide_repair_bridge::open_workspace,
       ide_repair_bridge::get_workspace_status,
       ide_repair_bridge::get_model_route_status,
       ide_repair_bridge::diagnose_dry_run,
       ide_repair_bridge::diagnose_live_opt_in,
       ide_repair_bridge::generate_patch_plan,
       ide_repair_bridge::verify_temp_patch,
       ide_repair_bridge::get_human_approval_packet,
       ide_repair_bridge::source_apply_dry_run,
       ide_repair_bridge::get_repair_flow_state,
   ])
   ```

That is the entire change. The bridge's response type is JSON-safe and
the Python driver is the only seam between Rust and the Determinex
backend.

## Status tokens

* `TAURI_RUST_COMMAND_BRIDGE_READY` — bridge file is present and the
  Python driver is reachable.
* `TAURI_RUST_COMMAND_BRIDGE_BLOCKED_NO_TAURI_APP` — used by the
  frontend probe when `src-tauri/` is missing.
* `TAURI_RUST_COMMAND_BRIDGE_BLOCKED_BACKEND_MISSING` — Rust side
  emits this when the Python driver script is missing or unreadable.
* `TAURI_COMMAND_SOURCE_MUTATION_BLOCKED` — invariant token; the
  response struct hardcodes `source_mutation_authorized: false`.
* `TAURI_COMMAND_TEMP_ONLY` — patch-touching commands flag temp-only.

## Hard invariants

* The bridge file contains no `reqwest::`, `ureq::`, `isahc::`,
  `hyper::Client`, or `TcpStream::connect` — no network seams.
* The bridge file contains no shell-string invocation
  (`sh -c`, `cmd.exe /c`, `.arg("-c")`).
* `source_mutation_authorized: false` and `training_eligible: false`
  appear in every response constructor.
* The Python driver is exercised in CI via a focused test that spawns
  it as a subprocess and validates the JSON shape.

## What this rung does *not* do

* Does not modify `lib.rs`.
* Does not call any model (live or fake).
* Does not write to any user source file.
