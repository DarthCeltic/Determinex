# Determinex React Universal 100 Sector State Ladder Binding

Lock: `DETERMINEX_REACT_UNIVERSAL_100_SECTOR_STATE_LADDER_BINDING_LOCK_001`

Loader decision: `REACT_UNIVERSAL_100_SECTOR_STATE_LADDER_BINDING_PASSED`

Read-only Claude visual-lane binding of Codex sector state ladder evidence.

## Counts

- Sectors: **11**
- Lifecycle states: **24**
- Blocker missing-rung states: **14**
- Promotion rules: **16** transitions

## Lifecycle ladder

1. `DISCOVERED`
2. `TAGGED`
3. `CLASSIFIED`
4. `ROUTED`
5. `INGESTION_REQUIRED`
6. `INGESTED`
7. `ADAPTER_REQUIRED`
8. `ADAPTER_READY`
9. `FIXTURE_REQUIRED`
10. `FIXTURE_READY`
11. `SCAFFOLD_SUPPORTED`
12. `BUILD_SUPPORTED`
13. `TEST_SUPPORTED`
14. `SMOKE_SUPPORTED`
15. `REPAIR_SUPPORTED`
16. `MAINTAIN_SUPPORTED`
17. `TEACH_SUPPORTED`
18. `USER_READY_WITH_CAVEATS`
19. `PACKAGING_REQUIRED`
20. `PACKAGING_SUPPORTED`
21. `FRESH_INSTALL_VERIFIED`
22. `RELEASE_GATE_READY`
23. `RELEASE_SUPPORTED`
24. `FULLY_SUPPORTED_WITH_CAVEATS`

## Blocker missing-rung states

- `TOOLCHAIN_MISSING`
- `DEPENDENCY_MISSING`
- `LOCAL_DEPENDENCY_MISSING`
- `VERIFIER_MISSING`
- `SMOKE_MISSING`
- `FIXTURE_MISSING`
- `ADAPTER_MISSING`
- `PLATFORM_MISSING`
- `AUTHORITY_MISSING`
- `SAFETY_BLOCKED`
- `NETWORK_REQUIRED_BUT_NOT_ALLOWED`
- `UNSUPPORTED_BY_POLICY`
- `ROADMAP`
- `FORBIDDEN`

## Sector registry

- **CLI and File/Data Sector** (`cli_file_data_sector`) — targets: SMOKE_SUPPORTED, USER_READY_WITH_CAVEATS
- **SQLite Data App Sector** (`sqlite_data_app_sector`) — targets: SMOKE_SUPPORTED
- **Python FastAPI Local API Sector** (`python_fastapi_local_api_sector`) — targets: SMOKE_SUPPORTED
- **Node and TypeScript CLI Sector** (`node_typescript_cli_sector`) — targets: SMOKE_SUPPORTED, USER_READY_WITH_CAVEATS
- **React/Vite Static App Sector** (`react_vite_static_app_sector`) — targets: SMOKE_SUPPORTED
- **Static Web Sector** (`static_web_sector`) — targets: SMOKE_SUPPORTED
- **Rust Utility Sector** (`rust_utility_sector`) — targets: SMOKE_SUPPORTED
- **Go Utility Sector** (`go_utility_sector`) — targets: SMOKE_SUPPORTED
- **Maintenance and Repair Sector** (`maintenance_repair_sector`) — targets: REPAIR_SUPPORTED, MAINTAIN_SUPPORTED
- **Learning and Teaching Sector** (`learning_teaching_sector`) — targets: TEACH_SUPPORTED
- **Packaging and Fresh Install Sector** (`packaging_fresh_install_sector`) — targets: PACKAGING_SUPPORTED, FRESH_INSTALL_VERIFIED, RELEASE_SUPPORTED

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
- authority flag true -> BLOCKED_AUTHORITY_CONFUSION
- broad_claims_granted true -> BLOCKED_BROAD_CLAIM
- sector_registry missing or empty -> BLOCKED_MALFORMED
- lifecycle missing DISCOVERED start or FULLY_SUPPORTED_WITH_CAVEATS terminus -> BLOCKED_MALFORMED
- sector targets RELEASE_SUPPORTED without naming packaging/fresh-install/release-gate rung -> BLOCKED_RELEASE_OVERCLAIM
- forbidden broad-claim phrase as current claim outside refusal context -> BLOCKED_BROAD_CLAIM
- evidence absent/corrupt -> AWAITING_EVIDENCE
