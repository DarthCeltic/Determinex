# Determinex React Universal 100 Sector Gulp Batch 005 Binding

Lock: `DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_005_BINDING_LOCK_001`

Loader decision: `REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_005_BINDING_PASSED`

## Sectors gulped

- `cli_file_data_sector`
- `node_typescript_cli_sector`

## Codex counts

- Tagged / classified / routed: **12 / 12 / 12**
- Promoted: **12**
- Blocked: **0**
- release_supported: **0**
- Claim-state counts: `{'IMPLEMENTED_WITH_CAVEATS': 3, 'PARTIAL': 9}`
- Support-state counts: `{'smoke_supported': 12}`
- Lifecycle-state counts: `{'SMOKE_SUPPORTED': 12}`

## Promoted cells

- `python_cli_multi_command` (`cli_file_data_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `python_file_transform_pipeline` (`cli_file_data_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `python_json_csv_transform` (`cli_file_data_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `python_csv_to_sqlite_importer` (`cli_file_data_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `sqlite_seed_query_verifier` (`cli_file_data_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `sqlite_crud_migration_query` (`cli_file_data_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `typescript_node_multi_command_cli` (`node_typescript_cli_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `typescript_node_file_data_tool` (`node_typescript_cli_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `typescript_node_json_validation_cli` (`node_typescript_cli_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `javascript_node_file_pipeline` (`node_typescript_cli_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `javascript_node_test_supported_variant` (`node_typescript_cli_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `powershell_file_pipeline` (`cli_file_data_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`

## Captions

- This panel displays evidence; it does not grant authority.
- Fixture-local proof is not production readiness.
- Smoke-supported is not release-supported.
- Fully supported with caveats is not release-supported.
- No source mutation without authority.
- No working-app claim without build/test/smoke evidence.
- Universal 100 means universal intake/routing, not magic execution.
- Blocked cells are visible by exact missing rung.

## Hard rules enforced

- status mismatch -> BLOCKED_MALFORMED
- sectors_gulped missing or empty -> BLOCKED_MALFORMED
- summary.cells_probed missing -> BLOCKED_MALFORMED
- authority flag true (top or under authority bag) -> BLOCKED_AUTHORITY_CONFUSION
- broad_claims_granted true -> BLOCKED_BROAD_CLAIM
- summary.release_supported > 0 without release-proof source path -> BLOCKED_RELEASE_OVERCLAIM
- blocked_cells key absent -> BLOCKED_BLOCKED_CELLS_HIDDEN
- required fixture-local caveat missing -> BLOCKED_FIXTURE_CAVEAT_MISSING
- forbidden broad-claim phrase as current claim outside refusal context -> BLOCKED_BROAD_CLAIM
- promoted IMPLEMENTED claim with support_state < demo_proven -> BLOCKED_MALFORMED
- promoted cell with FULLY_SUPPORTED_WITH_CAVEATS lifecycle without release-proof path -> BLOCKED_RELEASE_OVERCLAIM
- evidence absent/corrupt -> AWAITING_EVIDENCE
