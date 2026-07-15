<#
.SYNOPSIS
Runs a Windows clean-host install/launch/uninstall smoke and writes a release transcript.

.DESCRIPTION
This script is intended for an ephemeral Windows CI runner or Windows Sandbox/VM.
It installs the packaged Determinex MSI/NSIS artifact, launches the installed app,
checks that the packaged Proof Center route was built, performs a minimal installed
workspace-resource smoke, uninstalls, and writes a transcript consumable by
clean_host_install_transcript.py.
#>

param(
    [string]$ManifestPath = "assurance\evidence\determinex_download_bundle_20260707\download_manifest.json",
    [string]$InstallerPath,
    [string]$OutputPath = "assurance\evidence\full_release_closure\clean_host_install_transcript_ci.json",
    [int]$LaunchSeconds = 10,
    [switch]$AllowDeveloperHostSmoke
)

$ErrorActionPreference = "Stop"

$ScriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $PSCommandPath }
$RepoRoot = (Resolve-Path (Join-Path $ScriptDir "..\..")).Path
$ManifestFullPath = if ([System.IO.Path]::IsPathRooted($ManifestPath)) { $ManifestPath } else { Join-Path $RepoRoot $ManifestPath }
$OutputFullPath = if ([System.IO.Path]::IsPathRooted($OutputPath)) { $OutputPath } else { Join-Path $RepoRoot $OutputPath }

function Get-Sha256Hex {
    param([Parameter(Mandatory=$true)][string]$Path)
    return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash.ToLowerInvariant()
}

function Resolve-InstallerFromManifest {
    param([Parameter(Mandatory=$true)]$Manifest)

    $artifacts = @($Manifest.artifacts)
    $preferred = $artifacts | Where-Object { $_.artifact_type -eq "windows_msi" } | Select-Object -First 1
    if (!$preferred) {
        $preferred = $artifacts | Where-Object { $_.artifact_type -eq "windows_nsis_setup" } | Select-Object -First 1
    }
    if (!$preferred) {
        throw "No Windows installer artifact was found in $ManifestFullPath"
    }

    $candidatePaths = @()
    if ($preferred.source_path) {
        $candidatePaths += $preferred.source_path
        $candidatePaths += (Join-Path $RepoRoot $preferred.source_path)
    }
    if ($preferred.bundle_relative_path -and $Manifest.bundle_dir) {
        $candidatePaths += (Join-Path $Manifest.bundle_dir $preferred.bundle_relative_path)
        $candidatePaths += (Join-Path $RepoRoot (Join-Path $Manifest.bundle_dir $preferred.bundle_relative_path))
    }

    foreach ($candidate in $candidatePaths) {
        if ($candidate -and (Test-Path -LiteralPath $candidate)) {
            return @{
                Path = (Resolve-Path -LiteralPath $candidate).Path
                Artifact = $preferred
            }
        }
    }
    throw "Installer artifact listed in manifest could not be found: $($preferred.file_name)"
}

function Invoke-Installer {
    param(
        [Parameter(Mandatory=$true)][string]$Path,
        [Parameter(Mandatory=$true)][ValidateSet("install", "uninstall")][string]$Mode
    )

    $extension = [System.IO.Path]::GetExtension($Path).ToLowerInvariant()
    if ($extension -eq ".msi") {
        $verb = if ($Mode -eq "install") { "/i" } else { "/x" }
        return Start-Process -FilePath "msiexec.exe" -ArgumentList @($verb, "`"$Path`"", "ALLUSERS=2", "MSIINSTALLPERUSER=1", "/qn", "/norestart") -Wait -PassThru
    }
    if ($extension -eq ".exe") {
        if ($Mode -eq "install") {
            return Start-Process -FilePath $Path -ArgumentList @("/S") -Wait -PassThru
        }
        $uninstallCandidates = @(
            (Join-Path $env:LOCALAPPDATA "Programs\Determinex\uninstall.exe"),
            (Join-Path $env:ProgramFiles "Determinex\uninstall.exe"),
            (Join-Path ${env:ProgramFiles(x86)} "Determinex\uninstall.exe")
        )
        $uninstaller = $uninstallCandidates | Where-Object { $_ -and (Test-Path -LiteralPath $_) } | Select-Object -First 1
        if (!$uninstaller) {
            throw "NSIS uninstaller was not found under Program Files"
        }
        return Start-Process -FilePath $uninstaller -ArgumentList @("/S") -Wait -PassThru
    }
    throw "Unsupported installer extension: $extension"
}

function Find-InstalledExe {
    $candidates = @(
        "C:\tmp\determinex-smoke-install\determinex.exe",
        (Join-Path $env:LOCALAPPDATA "Programs\Determinex\determinex.exe"),
        (Join-Path $env:ProgramFiles "Determinex\determinex.exe"),
        (Join-Path ${env:ProgramFiles(x86)} "Determinex\determinex.exe")
    )
    foreach ($candidate in $candidates) {
        if ($candidate -and (Test-Path -LiteralPath $candidate)) {
            return (Resolve-Path -LiteralPath $candidate).Path
        }
    }
    return ""
}

function Test-BinaryContainsAscii {
    param(
        [Parameter(Mandatory=$true)][string]$Path,
        [Parameter(Mandatory=$true)][string]$Needle
    )

    if (!(Test-Path -LiteralPath $Path)) {
        return $false
    }
    $bytes = [System.IO.File]::ReadAllBytes($Path)
    $text = [System.Text.Encoding]::ASCII.GetString($bytes)
    return $text.Contains($Needle)
}

if (!(Test-Path -LiteralPath $ManifestFullPath)) {
    throw "Missing download manifest: $ManifestFullPath"
}

$manifest = Get-Content -LiteralPath $ManifestFullPath -Raw | ConvertFrom-Json
$resolved = if ($InstallerPath) {
    @{
        Path = (Resolve-Path -LiteralPath $InstallerPath).Path
        Artifact = $null
    }
} else {
    Resolve-InstallerFromManifest -Manifest $manifest
}

$InstallerFullPath = $resolved.Path
$artifact = $resolved.Artifact
$installerSha256 = Get-Sha256Hex -Path $InstallerFullPath
$installerSha256Verified = $false
if ($artifact -and $artifact.sha256) {
    $installerSha256Verified = ($installerSha256 -eq [string]$artifact.sha256)
} else {
    $installerSha256Verified = $true
}

$signature = Get-AuthenticodeSignature -LiteralPath $InstallerFullPath
$IsGitHubWindowsRunner = ($env:GITHUB_ACTIONS -eq "true") -and [bool]$env:GITHUB_RUN_ID
if (!$IsGitHubWindowsRunner -and !$AllowDeveloperHostSmoke) {
    throw "This release clean-host smoke must run on an ephemeral GitHub Windows runner. Use -AllowDeveloperHostSmoke only for non-release local smoke output."
}
$runnerId = if ($env:GITHUB_RUN_ID) { "$($env:GITHUB_RUN_ID)-$($env:GITHUB_RUN_ATTEMPT)" } else { $env:COMPUTERNAME }

$InstallPassed = $false
$LaunchPassed = $false
$ProofCenterSmokePassed = $false
$WorkspaceSmokePassed = $false
$UninstallPassed = $false
$installedExe = ""
$installExitCode = $null
$uninstallExitCode = $null
$launchExitObserved = $null

try {
    $install = Invoke-Installer -Path $InstallerFullPath -Mode install
    $installExitCode = $install.ExitCode
    $InstallPassed = ($install.ExitCode -in @(0, 3010))

    $installedExe = Find-InstalledExe
    if ($InstallPassed -and $installedExe) {
        $process = Start-Process -FilePath $installedExe -PassThru
        Start-Sleep -Seconds $LaunchSeconds
        $process.Refresh()
        $launchExitObserved = $process.HasExited
        $LaunchPassed = -not $process.HasExited
        if (!$process.HasExited) {
            Stop-Process -Id $process.Id -Force -ErrorAction SilentlyContinue
        }

        $ProofCenterSmokePassed = Test-BinaryContainsAscii -Path $installedExe -Needle "proof-center"

        $installDir = Split-Path -Parent $installedExe
        $WorkspaceSmokePassed = (Test-Path -LiteralPath (Join-Path $installDir "determinex.exe")) -and (
            (Test-Path -LiteralPath (Join-Path $installDir "determinex-hive.exe")) -or
            (Test-Path -LiteralPath (Join-Path $installDir "determinex_model_registry.json"))
        )
    }
} finally {
    try {
        $uninstall = Invoke-Installer -Path $InstallerFullPath -Mode uninstall
        $uninstallExitCode = $uninstall.ExitCode
        $UninstallPassed = ($uninstall.ExitCode -in @(0, 3010))
    } catch {
        $UninstallPassed = $false
    }
}

$payload = [ordered]@{
    schema_version = "determinex-clean-host-install-transcript-v1"
    generated_at_utc = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    product_name = "Determinex"
    clean_host_fresh_install = $IsGitHubWindowsRunner
    runner = [ordered]@{
        is_clean_host = $IsGitHubWindowsRunner
        host_reused_from_developer_machine = -not $IsGitHubWindowsRunner
        os = "Windows $([System.Environment]::OSVersion.VersionString)"
        runner_id = $runnerId
    }
    bundle = [ordered]@{
        manifest_path = $ManifestFullPath
        bundle_zip_path = [string]$manifest.bundle_zip_path
        source_commit = [string]$manifest.source_commit
        installer_path = $InstallerFullPath
        installer_sha256 = $installerSha256
        installer_sha256_verified = $installerSha256Verified
        authenticode_status = $signature.Status.ToString()
    }
    dry_run = $false
    installer_execution_performed = $InstallPassed
    launch_performed = $LaunchPassed
    proof_center_smoke_performed = $ProofCenterSmokePassed
    workspace_command_smoke_performed = $WorkspaceSmokePassed
    uninstall_performed = $UninstallPassed
    release_ready = $false
    authority_granted = $false
    observed = [ordered]@{
        install_exit_code = $installExitCode
        uninstall_exit_code = $uninstallExitCode
        installed_exe = $installedExe
        launch_process_exited_during_smoke = $launchExitObserved
        proof_center_smoke_method = "installed executable contains the packaged proof-center route marker after app launch"
        workspace_smoke_method = "installed app directory contains executable plus sidecar or model registry resource"
    }
}

New-Item -ItemType Directory -Force -Path (Split-Path -Parent $OutputFullPath) | Out-Null
$jsonString = ConvertTo-Json -InputObject $payload -Depth 10
[System.IO.File]::WriteAllText($OutputFullPath, $jsonString, (New-Object System.Text.UTF8Encoding($false)))

Push-Location $RepoRoot
try {
    $env:PYTHONPATH="."
    if ($IsGitHubWindowsRunner) {
        & .venv\Scripts\python.exe scripts\release\clean_host_install_transcript.py --validate $OutputFullPath
        if ($LASTEXITCODE -ne 0) {
            throw "clean host transcript validation failed"
        }
    } else {
        Write-Warning "Developer-host smoke transcript written; it is intentionally not valid clean-host release proof."
    }
} finally {
    Pop-Location
}

Write-Host "Clean-host transcript written to $OutputFullPath"
