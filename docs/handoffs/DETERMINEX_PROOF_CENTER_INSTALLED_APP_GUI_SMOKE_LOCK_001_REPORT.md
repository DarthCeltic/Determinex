# DETERMINEX_PROOF_CENTER_INSTALLED_APP_GUI_SMOKE_LOCK_001_REPORT

## Status

- Lock: `DETERMINEX_PROOF_CENTER_INSTALLED_APP_GUI_SMOKE_LOCK_001`.
- Status: `INSTALLED_PROOF_CENTER_GUI_SMOKE_VERIFIED_BATCH_003_ADVANCED`.
- Installed-app smoke attempted: `True`.
- Installed-app smoke verified: `True`.
- Observed href: `http://tauri.localhost/proof-center`.
- Screenshot: `assurance/evidence/proof_center_installed_app_gui_smoke_001/proof_center_installed_app_corrected_20260602.png`.
- Screenshot SHA256: `611C09072B7192D9E6C2B1FFD9E4099C06AA1275C722B31DD634DE276DD5F0CB`.
- Transcript: `assurance/evidence/proof_center_installed_app_gui_smoke_001/proof_center_installed_app_corrected_transcript_20260602.json`.

## Runtime Targets

- `proof_center_page_visible`: `True`.
- `batch_003_truth_block_visible`: `True`.
- `release_cell_status_visible`: `True`.
- `release_family_status_visible`: `True`.
- `queue_or_spend_status_visible`: `True`.
- `claim_scanner_status_visible`: `True`.
- `known_world_all_gap_status_visible`: `True`.
- `installer_proof_status_visible`: `True`.
- `sbom_clean_runner_status_visible`: `True`.
- `public_no_go_visible`: `True`.
- `patent_filed_false_visible`: `True`.

## Boundary

- The stale May installer attempt is retained as a failed pre-rebuild attempt.
- The corrected staged NSIS install proves local unsigned installer execution only.
- This does not prove signed/trusted installer, public release, beta readiness, full status-suite pass, all gaps closed, or family support.
