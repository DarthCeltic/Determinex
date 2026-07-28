# Determinex React Universal 100 Sector Gulp Batch 007 Binding

Lock: `DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_007_BINDING_LOCK_001`

Loader decision: `REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_007_BINDING_PASSED`

## Sectors gulped

- `go_utility_sector`
- `maintenance_repair_sector`
- `rust_utility_sector`

## Codex counts

- Tagged / classified / routed: **16 / 16 / 16**
- Promoted: **16**
- Blocked: **0**
- release_supported: **0**
- Claim-state counts: `{'IMPLEMENTED_WITH_CAVEATS': 13, 'PARTIAL': 3}`
- Support-state counts: `{'maintain_supported': 3, 'repair_supported': 3, 'smoke_supported': 10}`
- Lifecycle-state counts: `{'MAINTAIN_SUPPORTED': 3, 'REPAIR_SUPPORTED': 3, 'SMOKE_SUPPORTED': 10}`

## Promoted cells

- `rust_cli_file_transform` (`rust_utility_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `rust_library_unit_test_variant` (`rust_utility_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `rust_cli_config_file_smoke` (`rust_utility_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `rust_json_like_text_transform` (`rust_utility_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `rust_error_path_test` (`rust_utility_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `go_cli_create_variant` (`go_utility_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `go_http_healthcheck_variant` (`go_utility_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `go_file_transform_variant` (`go_utility_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `go_unit_test_variant` (`go_utility_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `go_error_path_test` (`go_utility_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `python_repair_regression_variant` (`maintenance_repair_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `repair_supported` · `REPAIR_SUPPORTED`
- `node_repair_regression_variant` (`maintenance_repair_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `repair_supported` · `REPAIR_SUPPORTED`
- `rust_repair_regression_variant` (`maintenance_repair_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `repair_supported` · `REPAIR_SUPPORTED`
- `config_maintenance_dry_run_variant` (`maintenance_repair_sector`) — `PARTIAL` / `maintain_supported` · `MAINTAIN_SUPPORTED`
- `static_site_maintenance_link_update_dry_run` (`maintenance_repair_sector`) — `PARTIAL` / `maintain_supported` · `MAINTAIN_SUPPORTED`
- `dependency_manifest_readonly_audit` (`maintenance_repair_sector`) — `PARTIAL` / `maintain_supported` · `MAINTAIN_SUPPORTED`

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
