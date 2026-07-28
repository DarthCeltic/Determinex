# Determinex React Universal 100 Sector Gulp Batch 006 Binding

Lock: `DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_006_BINDING_LOCK_001`

Loader decision: `REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_006_BINDING_PASSED`

## Sectors gulped

- `react_vite_static_app_sector`
- `static_web_sector`
- `python_fastapi_local_api_sector`

## Codex counts

- Tagged / classified / routed: **18 / 18 / 18**
- Promoted: **18**
- Blocked: **0**
- release_supported: **0**
- Claim-state counts: `{'IMPLEMENTED_WITH_CAVEATS': 12, 'PARTIAL': 6}`
- Support-state counts: `{'smoke_supported': 18}`
- Lifecycle-state counts: `{'SMOKE_SUPPORTED': 18}`

## Promoted cells

- `react_vite_two_component_smoke` (`react_vite_static_app_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `react_vite_form_state_smoke` (`react_vite_static_app_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `react_vite_static_data_render_smoke` (`react_vite_static_app_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `react_vite_route_like_state_smoke` (`react_vite_static_app_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `react_vite_build_output_manifest_smoke` (`react_vite_static_app_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `vite_multi_page_static_smoke` (`react_vite_static_app_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `html_css_js_form_validation_smoke` (`static_web_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `html_css_js_fetch_local_json_smoke` (`static_web_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `html_css_js_multi_page_navigation_smoke` (`static_web_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `static_site_asset_manifest_smoke` (`static_web_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `static_site_accessibility_basic_check` (`static_web_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `static_site_link_integrity_check` (`static_web_sector`) — `PARTIAL` / `smoke_supported` · `SMOKE_SUPPORTED`
- `python_fastapi_two_route_healthcheck` (`python_fastapi_local_api_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `python_fastapi_static_json_api` (`python_fastapi_local_api_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `python_fastapi_query_param_smoke` (`python_fastapi_local_api_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `python_fastapi_error_response_smoke` (`python_fastapi_local_api_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `python_fastapi_local_client_smoke` (`python_fastapi_local_api_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`
- `python_fastapi_pytest_api_smoke` (`python_fastapi_local_api_sector`) — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported` · `SMOKE_SUPPORTED`

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
