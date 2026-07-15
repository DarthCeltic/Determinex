# Determinex Download And Setup

This document describes the current downloadable setup path. It is for local/operator testing and release-candidate packaging, not public release approval.

## Build The Installers

```powershell
powershell -ExecutionPolicy Bypass -File scripts\release\build_release_package.ps1 -SkipDependencyRestore -SkipSbom -SkipSidecar -CargoTargetDir .tmp\determinex-cargo-target -PackageDownloadBundle -TauriBundleTarget all -DownloadBundleOutputDir .tmp\determinex-download-bundles
```

The script builds the Tauri installer artifacts available on the current host and, when `-PackageDownloadBundle` is set, wraps them into a downloadable ZIP with:

- `SETUP.md`
- `CHECKSUMS.sha256`
- `download_manifest.json`
- Windows NSIS/MSI artifacts under `installers/` when built on Windows with WiX available
- Linux package artifacts under `installers/` when built on Linux

`-PackageDownloadBundle` defaults the Tauri bundle target to `all`. On Windows that covers the Windows bundle targets available to the host; Linux packages must be built in a Linux runner or clean Linux host.

Linux package pass:

```bash
cd frontend
npm run tauri -- build --bundles appimage,deb,rpm
python ../scripts/release/package_download_bundle.py --installer-dir src-tauri/target/release/bundle --output-dir ../.tmp/determinex-download-bundles --evidence-dir ../assurance/evidence/determinex_download_bundle_20260707
```

The package matrix workflow builds the Windows and Linux artifacts on native
runners, then merges them into one combined public-download bundle. A complete
public bundle must include all of these artifact families:

- Windows NSIS setup
- Windows MSI
- Linux AppImage
- Linux deb
- Linux rpm

## Evidence

The small evidence files are written to:

```text
assurance/evidence/determinex_download_bundle_20260707/
```

The large installer binaries and ZIP stay outside git by default.

## Windows Trust And Clean-Host Proof

After building the Windows bundle, record Authenticode/SmartScreen evidence from
the generated manifest:

```powershell
python scripts\release\windows_trust_packet.py --manifest assurance\evidence\determinex_download_bundle_20260707\download_manifest.json
```

Unsigned artifacts are recorded as unsigned evidence and do not pass the
`windows_trust` gate. Passing trust evidence requires a valid Authenticode
signature, timestamp evidence, and an explicit SmartScreen pass result.

The clean-host proof must run on an ephemeral Windows runner, VM, or sandbox; a
developer checkout cannot satisfy it. The package matrix workflow runs:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\release\run_windows_clean_host_install_smoke.ps1 -ManifestPath assurance\evidence\determinex_download_bundle_20260707\download_manifest.json -OutputPath assurance\evidence\full_release_closure\clean_host_install_transcript_ci.json
python scripts\release\clean_host_install_transcript.py --validate assurance\evidence\full_release_closure\clean_host_install_transcript_ci.json
```

## Current Boundary

The Windows NSIS/MSI bundle can be downloaded and used for local/operator setup
testing. The public distribution legal/IP packet and Windows MSI evidence are
now tracked as release evidence, but the local bundle is still not a public
release because these gates remain separate:

- code signing and timestamped Authenticode verification
- SmartScreen/trust reputation
- Linux AppImage, deb, and rpm package artifacts from a Linux runner
- combined all-platform download bundle evidence
- clean-host install, launch, and uninstall proof
