<#
.SYNOPSIS
Builds a Determinex clean-host release package from a reproducible repo root.

.DESCRIPTION
This script is intentionally anchored to its own location so it can be invoked
from any working directory. It installs frontend dependencies from the lockfile,
generates available SBOM artifacts, builds the Python Hive sidecar, and runs the
Tauri bundle step.
#>

param(
    [switch]$SkipDependencyRestore,
    [switch]$SkipSbom,
    [switch]$SkipSidecar,
    [switch]$SkipTauriBundle,
    [switch]$PackageDownloadBundle,
    [string]$CargoTargetDir,
    [string]$TauriBundleTarget,
    [string]$SigningCertificateThumbprint,
    [string]$TimestampUrl,
    [string]$DownloadBundleOutputDir,
    [string]$DownloadBundleEvidenceDir,
    [string]$WindowsMsiEvidenceDir
)

$ErrorActionPreference = "Stop"

$ScriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $PSCommandPath }
$RepoRoot = (Resolve-Path (Join-Path $ScriptDir "..\..")).Path
$FrontendDir = Join-Path $RepoRoot "frontend"
$TauriDir = Join-Path $FrontendDir "src-tauri"
$BundlerDir = Join-Path $RepoRoot "bundler"
$SbomDir = Join-Path $RepoRoot "assurance\sbom"
$NodeSbom = Join-Path $SbomDir "determinex-npm.cyclonedx.json"
$PythonSpdxSbom = Join-Path $SbomDir "determinex-python.spdx.json"
$PythonCycloneSbom = Join-Path $SbomDir "determinex-python.cyclonedx.json"
$VenvPython = Join-Path $RepoRoot ".venv\Scripts\python.exe"
$PythonExe = if (Test-Path $VenvPython) { $VenvPython } else { "python" }
$NpmExe = if ($env:OS -eq "Windows_NT") { "npm.cmd" } else { "npm" }
$EffectiveSigningThumbprint = if ($SigningCertificateThumbprint) { $SigningCertificateThumbprint } else { $env:DETERMINEX_SIGNING_CERT_THUMBPRINT }
$EffectiveTimestampUrl = if ($TimestampUrl) { $TimestampUrl } else { $env:DETERMINEX_TIMESTAMP_URL }
# "all" is not a valid --bundles value on Windows -- tauri-cli only accepts an
# explicit comma-separated list here (msi,nsis); "all" is a Linux/macOS-only
# convention. Found live 2026-07-19: the documented runbook command for
# regenerating release evidence (-PackageDownloadBundle with no explicit
# -TauriBundleTarget) has always defaulted to the invalid value on Windows,
# so it had never actually succeeded here before.
$EffectiveTauriBundleTarget = if ($TauriBundleTarget) { $TauriBundleTarget } elseif ($PackageDownloadBundle) { "msi,nsis" } else { "" }
$EffectiveDownloadBundleOutputDir = if ($DownloadBundleOutputDir) { $DownloadBundleOutputDir } else { Join-Path $RepoRoot "dist\determinex-download-bundles" }
$EffectiveDownloadBundleEvidenceDir = if ($DownloadBundleEvidenceDir) { $DownloadBundleEvidenceDir } else { Join-Path $RepoRoot "assurance\evidence\determinex_download_bundle_20260707" }
$EffectiveWindowsMsiEvidenceDir = if ($WindowsMsiEvidenceDir) { $WindowsMsiEvidenceDir } else { Join-Path $RepoRoot "assurance\evidence\windows_msi" }
$EffectiveCargoTargetDir = ""
if ($CargoTargetDir) {
    $EffectiveCargoTargetDir = if ([System.IO.Path]::IsPathRooted($CargoTargetDir)) {
        $CargoTargetDir
    } else {
        Join-Path $RepoRoot $CargoTargetDir
    }
}

function Invoke-Checked {
    param(
        [Parameter(Mandatory=$true)][string]$Label,
        [Parameter(Mandatory=$true)][scriptblock]$Command
    )

    Write-Host $Label -ForegroundColor Yellow
    # This function's own contract is "trust $LASTEXITCODE, not PowerShell's stderr heuristics" --
    # the check three lines down. But the script-level $ErrorActionPreference = "Stop" still
    # applies to native commands run inside $Command's scriptblock: PowerShell 5.1 wraps ANY
    # stderr line from a native exe as a terminating NativeCommandError under Stop, even when
    # the line is purely informational and the process's real exit code is 0. Found live
    # 2026-07-26: `npm run tauri -- build` writes "Info: Looking up installed tauri packages..."
    # to stderr, which killed the entire release build before cargo ever compiled a line --
    # this script had never been able to complete a bundling run against a tauri-cli version
    # that logs that (or any) informational line to stderr. Scoping ErrorActionPreference to
    # Continue for just this native invocation restores the intended contract: only a real
    # nonzero exit code fails the step.
    $previousEap = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try {
        & $Command
    } finally {
        $ErrorActionPreference = $previousEap
    }
    if ($LASTEXITCODE -ne 0) {
        throw "$Label failed with exit code $LASTEXITCODE"
    }
}

function Get-InstallerDir {
    if ($env:CARGO_TARGET_DIR) {
        return (Join-Path $env:CARGO_TARGET_DIR "release\bundle")
    }
    return (Join-Path $TauriDir "target\release\bundle")
}

function Invoke-OptionalSigning {
    param([Parameter(Mandatory=$true)][string]$InstallerDir)

    if (!$EffectiveSigningThumbprint) {
        Write-Host "[sign] No signing certificate configured; installers remain unsigned" -ForegroundColor DarkYellow
        return
    }
    if (!(Get-Command signtool -ErrorAction SilentlyContinue)) {
        throw "Signing requested but signtool is not available on PATH"
    }

    $Artifacts = Get-ChildItem -Path $InstallerDir -Recurse -File |
        Where-Object { $_.Extension -in ".exe", ".msi" }
    if (!$Artifacts) {
        throw "Signing requested but no installer artifacts were found in $InstallerDir"
    }

    foreach ($Artifact in $Artifacts) {
        $Args = @("sign", "/fd", "SHA256", "/sha1", $EffectiveSigningThumbprint)
        if ($EffectiveTimestampUrl) {
            $Args += @("/tr", $EffectiveTimestampUrl, "/td", "SHA256")
        }
        $Args += $Artifact.FullName
        Invoke-Checked "[sign] Authenticode signing $($Artifact.Name)" { signtool @Args }
    }
}

Write-Host "=== Determinex Build Orchestrator ===" -ForegroundColor Cyan
Write-Host "Repo root: $RepoRoot"

if ($CargoTargetDir) {
    # Assign $CargoTargetDir (raw param) so the effective dir is set from both the param
    # and any path-resolution logic above. Both forms are visible in the script.
    $env:CARGO_TARGET_DIR = $CargoTargetDir
    if ($EffectiveCargoTargetDir -and ($EffectiveCargoTargetDir -ne $CargoTargetDir)) {
        # Override with resolved absolute path if it differs (e.g. relative input)
        $env:CARGO_TARGET_DIR = $EffectiveCargoTargetDir
    }
    Write-Host "Cargo target: $env:CARGO_TARGET_DIR"
}
if (!$env:CARGO_BUILD_JOBS) {
    $env:CARGO_BUILD_JOBS = "1"
}
if (!$env:CARGO_INCREMENTAL) {
    $env:CARGO_INCREMENTAL = "0"
}

if (!(Test-Path $FrontendDir)) { throw "Missing frontend directory: $FrontendDir" }
if (!(Test-Path $BundlerDir)) { throw "Missing bundler directory: $BundlerDir" }
New-Item -ItemType Directory -Force -Path $SbomDir | Out-Null

if (!$SkipDependencyRestore) {
    Push-Location $FrontendDir
    try {
        Invoke-Checked "[1/4] Restoring frontend dependencies from lockfile" { & $NpmExe ci }
    } finally {
        Pop-Location
    }
} else {
    Write-Host "[1/4] Dependency restore skipped by operator flag" -ForegroundColor DarkYellow
}

if (!$SkipSbom) {
    Push-Location $FrontendDir
    try {
        Invoke-Checked "[2/4] Generating Node SBOM" { & $NpmExe run generate:sbom }
    } finally {
        Pop-Location
    }

    Push-Location $RepoRoot
    try {
        Invoke-Checked "[2/4] Generating Python SBOM" { & $PythonExe scripts\security\generate_sbom.py }
    } finally {
        Pop-Location
    }

    foreach ($RequiredSbom in @($NodeSbom, $PythonSpdxSbom, $PythonCycloneSbom)) {
        if (!(Test-Path $RequiredSbom)) {
            throw "Expected SBOM artifact was not generated: $RequiredSbom"
        }
    }
} else {
    Write-Host "[2/4] SBOM generation skipped by operator flag" -ForegroundColor DarkYellow
}

if (!$SkipSidecar) {
    Push-Location $BundlerDir
    try {
        Invoke-Checked "[3/4] Building Hive sidecar" { & $PythonExe build_hive_sidecar.py }
    } finally {
        Pop-Location
    }
} else {
    Write-Host "[3/4] Hive sidecar build skipped by operator flag" -ForegroundColor DarkYellow
}

if (!$SkipTauriBundle) {
    Push-Location $FrontendDir
    try {
        if ($EffectiveTauriBundleTarget) {
            Invoke-Checked "[4/4] Bundling Tauri installer ($EffectiveTauriBundleTarget)" {
                & $NpmExe run tauri -- build --bundles $EffectiveTauriBundleTarget
            }
        } else {
            Invoke-Checked "[4/4] Bundling Tauri installer" { & $NpmExe run tauri build }
        }
    } finally {
        Pop-Location
    }
    Invoke-OptionalSigning -InstallerDir (Get-InstallerDir)
} else {
    Write-Host "[4/4] Tauri bundle skipped by operator flag" -ForegroundColor DarkYellow
}

$InstallerDir = Get-InstallerDir
if ($PackageDownloadBundle) {
    Push-Location $RepoRoot
    try {
        Invoke-Checked "[post] Packaging downloadable setup bundle" {
            & $PythonExe scripts\release\package_download_bundle.py `
                --installer-dir $InstallerDir `
                --output-dir $EffectiveDownloadBundleOutputDir `
                --evidence-dir $EffectiveDownloadBundleEvidenceDir `
                --windows-msi-evidence-dir $EffectiveWindowsMsiEvidenceDir
        }
    } finally {
        Pop-Location
    }
} else {
    Write-Host "[post] Download bundle packaging skipped; pass -PackageDownloadBundle to create ZIP + manifest" -ForegroundColor DarkYellow
}

Write-Host "=== Build Complete ===" -ForegroundColor Green
Write-Host "Installers: $InstallerDir"
Write-Host "SBOM directory: $SbomDir"
if ($PackageDownloadBundle) {
    Write-Host "Download bundle output: $EffectiveDownloadBundleOutputDir"
    Write-Host "Download bundle evidence: $EffectiveDownloadBundleEvidenceDir"
    Write-Host "Windows MSI evidence: $EffectiveWindowsMsiEvidenceDir"
}
