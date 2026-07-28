# Determinex React Universal 100 Sector Gulp Batch 010 Binding

Lock: `DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_010_BINDING_LOCK_001`

Loader decision: `REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_010_BINDING_PASSED`

## Sectors gulped

- `browser_extension_sector`
- `documentation_static_docs_sector`
- `tauri_electron_desktop_sector`

## Codex counts

- Tagged / classified / routed: **9 / 9 / 9**
- Promoted: **7**
- Blocked: **2**
- release_supported: **0**
- Claim-state counts: `{'IMPLEMENTED_WITH_CAVEATS': 3, 'PARTIAL': 4, 'ROADMAP': 2}`
- Support-state counts: `{'scaffold_supported': 4, 'smoke_supported': 3}`
- Lifecycle-state counts: `{}`

## Promoted cells

- `tauri_minimal_manifest_scaffold` (`tauri_electron_desktop_sector`) — `PARTIAL` / `scaffold_supported` · ``
- `electron_minimal_manifest_scaffold` (`tauri_electron_desktop_sector`) — `PARTIAL` / `scaffold_supported` · ``
- `browser_extension_manifest_scaffold` (`browser_extension_sector`) — `PARTIAL` / `scaffold_supported` · ``
- `browser_extension_static_asset_manifest` (`browser_extension_sector`) — `PARTIAL` / `scaffold_supported` · ``
- `documentation_static_site_link_check` (`documentation_static_docs_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · ``
- `documentation_static_docs_build_manifest` (`documentation_static_docs_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · ``
- `documentation_markdown_anchor_check` (`documentation_static_docs_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · ``

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
