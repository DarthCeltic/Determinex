from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "release" / "build_release_package.ps1"


def test_release_build_script_anchors_paths_to_script_location():
    text = SCRIPT.read_text(encoding="utf-8")

    assert "$PSScriptRoot" in text
    assert "$RepoRoot" in text
    assert "Push-Location $FrontendDir" in text
    assert "Push-Location \"..\\..\\frontend\"" not in text


def test_release_build_script_uses_deterministic_dependency_install():
    text = SCRIPT.read_text(encoding="utf-8")

    assert "$NpmExe" in text
    assert '"npm.cmd"' in text
    assert "& $NpmExe ci" in text
    assert "npm install" not in text


def test_release_build_script_generates_required_sbom_artifacts():
    text = SCRIPT.read_text(encoding="utf-8")

    assert "$VenvPython" in text
    assert "$PythonExe" in text
    assert "determinex-npm.cyclonedx.json" in text
    assert "determinex-python.spdx.json" in text
    assert "determinex-python.cyclonedx.json" in text
    assert "scripts\\security\\generate_sbom.py" in text
    assert "Expected SBOM artifact was not generated" in text
    assert "cargo-cyclonedx is not installed" not in text


def test_release_build_script_has_cargo_lock_workarounds():
    text = SCRIPT.read_text(encoding="utf-8")

    assert "[string]$CargoTargetDir" in text
    assert "$env:CARGO_TARGET_DIR = $CargoTargetDir" in text
    assert "$env:CARGO_BUILD_JOBS = \"1\"" in text
    assert "$env:CARGO_INCREMENTAL = \"0\"" in text
    assert "function Get-InstallerDir" in text
    assert "Join-Path $env:CARGO_TARGET_DIR \"release\\bundle\"" in text


def test_release_build_script_has_optional_authenticode_signing_route():
    text = SCRIPT.read_text(encoding="utf-8")

    assert "[string]$SigningCertificateThumbprint" in text
    assert "DETERMINEX_SIGNING_CERT_THUMBPRINT" in text
    assert "DETERMINEX_TIMESTAMP_URL" in text
    assert "signtool" in text
    assert "Authenticode signing" in text
    assert "installers remain unsigned" in text


def test_release_build_script_can_package_download_bundle():
    text = SCRIPT.read_text(encoding="utf-8")

    assert "[switch]$PackageDownloadBundle" in text
    assert "[string]$TauriBundleTarget" in text
    assert '$EffectiveTauriBundleTarget = if ($TauriBundleTarget)' in text
    assert 'elseif ($PackageDownloadBundle) { "all" }' in text
    assert "& $NpmExe run tauri -- build --bundles $EffectiveTauriBundleTarget" in text
    assert "[string]$DownloadBundleOutputDir" in text
    assert "[string]$DownloadBundleEvidenceDir" in text
    assert "[string]$WindowsMsiEvidenceDir" in text
    assert "scripts\\release\\package_download_bundle.py" in text
    assert "--installer-dir $InstallerDir" in text
    assert "--output-dir $EffectiveDownloadBundleOutputDir" in text
    assert "--evidence-dir $EffectiveDownloadBundleEvidenceDir" in text
    assert "--windows-msi-evidence-dir $EffectiveWindowsMsiEvidenceDir" in text
