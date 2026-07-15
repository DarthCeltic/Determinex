# Frontend Panel Command Wiring

> Locked under `locks/sentinel/FRONTEND_PANEL_COMMAND_WIRING_LOCK_001.json`.

`frontend/src/lib/ide-panel-bindings.ts` is the single source of truth
mapping each visible repair panel to the Tauri command(s) it must call,
the default mode it must operate in, and the always-blocked
source-mutation rule. Python audit pins each binding against the
panel's TSX source so wiring cannot drift silently.

| Panel | Commands | Default mode |
|---|---|---|
| `DiagnoseAndPatchPlanPanel` | `diagnose_dry_run`, `diagnose_live_opt_in`, `generate_patch_plan` | DRY_RUN |
| `EvidenceViewerPanel` | `get_repair_flow_state` | READ_ONLY |
| `HumanApprovalPanel` | `get_human_approval_packet` | FIXTURE_ONLY |
| `ModelRoutePanel` | `get_model_route_status` | READ_ONLY |
| `SourceApplyDryRunPanel` | `source_apply_dry_run` | DRY_RUN |
| `TempVerifyPanel` | `verify_temp_patch` | FIXTURE_ONLY |
| `WorkspaceStatusPanel` | `get_workspace_status` | READ_ONLY |
