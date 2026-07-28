# DETERMINEX_PROOF_CENTER_INSTALLED_APP_ROUTE_MOUNT_001_REPORT

## Status

- Lock: `DETERMINEX_PROOF_CENTER_INSTALLED_APP_ROUTE_MOUNT_LOCK_001`.
- Status: `PROOF_CENTER_ROUTE_SOURCE_MOUNT_VERIFIED_GUI_SMOKE_PENDING`.
- Source route mounted: `True`.
- Route path: `/proof-center`.
- Root navigation bound: `True`.

## Evidence

- Route page: `frontend/src/app/proof-center/page.tsx`.
- Root navigation link: `frontend/src/app/page.tsx`.
- Mounted panel: `frontend/src/components/ide-product-shell/ProofOperatorCenterPanel.tsx`.
- Machine-readable evidence: `assurance/evidence/proof_center_installed_app_route_mount_001/run_20260602.PROOF_CENTER_INSTALLED_APP_ROUTE_MOUNT_001.json`.

## Boundary

- Installed-app GUI smoke attempted: `False`.
- Installed-app GUI smoke verified: `False`.
- Reason: This lock proves the Next/Tauri source route is mounted and linked. It does not launch the packaged Tauri installed app or capture GUI automation.
- No release readiness, public launch, family support, or universal support claim is made.
