# Determinex React Universal 100 Support Map Delta Batch 005 Binding

Lock: `DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_005_VISUAL_BINDING_LOCK_001`

Loader decision: `REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_005_BINDING_PASSED`

## Delta sources

- `assurance/evidence/universal_100_sector_gulp_batch_005/sector_gulp_results_20260529.json`

## Counts

- Promoted: 12
- Blocked: 0
- release_supported: 0
- Claim-state counts: `{'IMPLEMENTED_WITH_CAVEATS': 3, 'PARTIAL': 9}`
- Support-state counts: `{'smoke_supported': 12}`

## Promoted cells

- `python_cli_multi_command` — `PARTIAL` / `smoke_supported`
- `python_file_transform_pipeline` — `PARTIAL` / `smoke_supported`
- `python_json_csv_transform` — `PARTIAL` / `smoke_supported`
- `python_csv_to_sqlite_importer` — `PARTIAL` / `smoke_supported`
- `sqlite_seed_query_verifier` — `PARTIAL` / `smoke_supported`
- `sqlite_crud_migration_query` — `PARTIAL` / `smoke_supported`
- `typescript_node_multi_command_cli` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `typescript_node_file_data_tool` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `typescript_node_json_validation_cli` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `javascript_node_file_pipeline` — `PARTIAL` / `smoke_supported`
- `javascript_node_test_supported_variant` — `PARTIAL` / `smoke_supported`
- `powershell_file_pipeline` — `PARTIAL` / `smoke_supported`

## Captions

- This panel displays evidence; it does not grant authority.
- Support map delta is layered on top of the base map.
- Fixture-local probe-driven promotion is not production readiness.
- Universal 100 means universal intake/routing, not magic execution.
- No source mutation without authority.
- No release claim without release proof.
- Unsupported and blocked cells are routed by exact missing rung.

## Hard rules enforced

- status mismatch -> BLOCKED_MALFORMED
- authority flag true -> BLOCKED_AUTHORITY_CONFUSION
- broad_claims_granted true -> BLOCKED_BROAD_CLAIM
- support_state_counts.release_supported > 0 without release-proof source path -> BLOCKED_RELEASE_OVERCLAIM
- blocked_cells key absent -> BLOCKED_BLOCKED_CELLS_HIDDEN
- forbidden broad-claim phrase as current claim outside refusal context -> BLOCKED_BROAD_CLAIM
- promoted IMPLEMENTED claim with support_state < demo_proven -> BLOCKED_MALFORMED
- evidence absent/corrupt -> AWAITING_EVIDENCE
