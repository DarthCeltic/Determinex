# Determinex Extension Compatibility Contract

Status: contract defined, runtime evidence pending.

This contract defines the minimum bar for claiming VS Code/Open VSX compatibility. It does not claim that extension runtime compatibility is complete.

## Supported Package Intake

- Accept `.vsix` packages from local disk after checksum recording.
- Accept Open VSX metadata only after source URL, publisher, version, and license fields are captured.
- Reject packages that request unsupported host APIs unless an explicit compatibility shim exists.
- Store installed extension state under the Determinex user profile, not inside a project checkout.

## Trust Boundary

- Extension install is a user-authorized action.
- Activation runs inside the Determinex extension sandbox.
- Extension code must not receive raw API keys, model secrets, payment identifiers, or unrestricted filesystem access.
- Workspace access must be scoped to the active project root and surfaced in the UI before activation.

## Runtime Compatibility Bar

The `extension_compat` release gate may pass only after a packet with schema `determinex-extension-compat-runtime-evidence-v1` records:

- `extension_api_contract_defined: true`
- `vsix_import_smoke_passed: true`
- `open_vsx_metadata_parsed: true`
- `sandbox_permissions_enforced: true`
- `activation_event_smoke_passed: true`
- `authority_granted: false`

## Non-Claims

- This contract does not claim complete VS Code API parity.
- This contract does not claim marketplace publication.
- This contract does not bypass installer, trust, clean-host, or benchmark release gates.
