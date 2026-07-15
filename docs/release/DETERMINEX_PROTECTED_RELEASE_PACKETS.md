# Determinex Protected Release Packets

Status: schemas defined for operator-supplied evidence.

These packet shapes let Determinex record external release proof without granting release authority in code. Every packet must keep `authority_granted: false`; the release collector reports evidence status only.

## Windows Trust

Path: `assurance/evidence/windows_trust/windows_trust_YYYYMMDD.json`

Collector:

```powershell
python scripts\release\windows_trust_packet.py --manifest assurance\evidence\determinex_download_bundle_20260707\download_manifest.json
```

Required fields:

- `schema_version: "determinex-windows-trust-evidence-v1"`
- `artifact_authenticode_status: "Valid"`
- `code_signing_verified: true`
- `timestamp_verified: true`
- `smartscreen_verification_performed: true`
- `smartscreen_result: "pass"`
- `certificate_subject: "<publisher certificate subject>"`
- `authority_granted: false`

## Legal Public Distribution

Path: `assurance/evidence/public_distribution/legal_public_distribution_YYYYMMDD.json`

Required fields:

- `schema_version: "determinex-legal-public-distribution-evidence-v1"`
- `legal_review_completed: true`
- `license_inventory_reviewed: true`
- `model_notice_reviewed: true`
- `public_repo_secret_scan_passed: true`
- `public_repo_scrub_completed: true`
- `third_party_notices_present: true`
- `authority_granted: false`

## Windows MSI

Path: `assurance/evidence/windows_msi/windows_msi_YYYYMMDD.json`

Required fields:

- `schema_version: "determinex-windows-msi-evidence-v1"`
- `wix_toolset_used: true`
- `msi_built: true`
- `msi_sha256_verified: true`
- `msi_installer_smoke_performed: true`
- `authority_granted: false`

## Extension Compatibility

Path: `assurance/evidence/extension_compat/extension_compat_YYYYMMDD.json`

Required fields:

- `schema_version: "determinex-extension-compat-runtime-evidence-v1"`
- `extension_api_contract_defined: true`
- `vsix_import_smoke_passed: true`
- `open_vsx_metadata_parsed: true`
- `sandbox_permissions_enforced: true`
- `activation_event_smoke_passed: true`
- `authority_granted: false`
