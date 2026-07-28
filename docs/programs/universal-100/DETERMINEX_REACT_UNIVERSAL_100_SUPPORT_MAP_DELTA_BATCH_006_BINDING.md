# Determinex React Universal 100 Support Map Delta Batch 006 Binding

Lock: `DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_006_VISUAL_BINDING_LOCK_001`

Loader decision: `REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_006_BINDING_PASSED`

## Delta sources

- `assurance/evidence/universal_100_sector_gulp_batch_006/sector_gulp_results_20260529.json`

## Counts

- Promoted: 18
- Blocked: 0
- release_supported: 0
- Claim-state counts: `{'IMPLEMENTED_WITH_CAVEATS': 12, 'PARTIAL': 6}`
- Support-state counts: `{'smoke_supported': 18}`

## Promoted cells

- `react_vite_two_component_smoke` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `react_vite_form_state_smoke` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `react_vite_static_data_render_smoke` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `react_vite_route_like_state_smoke` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `react_vite_build_output_manifest_smoke` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `vite_multi_page_static_smoke` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `html_css_js_form_validation_smoke` — `PARTIAL` / `smoke_supported`
- `html_css_js_fetch_local_json_smoke` — `PARTIAL` / `smoke_supported`
- `html_css_js_multi_page_navigation_smoke` — `PARTIAL` / `smoke_supported`
- `static_site_asset_manifest_smoke` — `PARTIAL` / `smoke_supported`
- `static_site_accessibility_basic_check` — `PARTIAL` / `smoke_supported`
- `static_site_link_integrity_check` — `PARTIAL` / `smoke_supported`
- `python_fastapi_two_route_healthcheck` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `python_fastapi_static_json_api` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `python_fastapi_query_param_smoke` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `python_fastapi_error_response_smoke` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `python_fastapi_local_client_smoke` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`
- `python_fastapi_pytest_api_smoke` — `IMPLEMENTED_WITH_CAVEATS` / `smoke_supported`

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
