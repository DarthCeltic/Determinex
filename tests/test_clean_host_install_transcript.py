from __future__ import annotations

import json
from pathlib import Path

from scripts.release import clean_host_install_transcript as transcript


def test_template_is_not_release_ready_and_names_required_steps():
    payload = transcript.build_template("2026-07-08T00:00:00Z")

    assert payload["schema_version"] == "determinex-clean-host-install-transcript-v1"
    assert payload["product_name"] == "Determinex"
    assert payload["clean_host_fresh_install"] is False
    assert payload["release_ready"] is False
    assert payload["authority_granted"] is False
    assert "install Determinex setup artifact" in " ".join(payload["required_steps"])
    assert "uninstall Determinex" in " ".join(payload["required_steps"])


def test_validate_file_accepts_complete_transcript(tmp_path: Path):
    path = tmp_path / "clean_host_install_transcript_20260708.json"
    path.write_text(
        json.dumps(
            {
                "schema_version": "determinex-clean-host-install-transcript-v1",
                "product_name": "Determinex",
                "clean_host_fresh_install": True,
                "runner": {
                    "is_clean_host": True,
                    "host_reused_from_developer_machine": False,
                    "os": "Windows 11",
                    "runner_id": "clean-host-runner-20260708",
                },
                "bundle": {
                    "source_commit": "final-release-commit",
                    "installer_sha256_verified": True,
                    "installer_sha256": "a" * 64,
                },
                "dry_run": False,
                "installer_execution_performed": True,
                "launch_performed": True,
                "proof_center_smoke_performed": True,
                "workspace_command_smoke_performed": True,
                "uninstall_performed": True,
                "release_ready": False,
                "authority_granted": False,
            }
        ),
        encoding="utf-8",
    )

    result = transcript.validate_file(path)

    assert result["status"] == "passed"
    assert result["errors"] == []


def test_validate_file_rejects_partial_or_dry_run_transcript(tmp_path: Path):
    path = tmp_path / "clean_host_install_transcript_20260708.json"
    path.write_text(
        json.dumps(
            {
                "schema_version": "determinex-clean-host-install-transcript-v1",
                "product_name": "Determinex",
                "clean_host_fresh_install": True,
                "runner": {
                    "is_clean_host": True,
                    "host_reused_from_developer_machine": False,
                    "os": "Windows 11",
                },
                "bundle": {
                    "source_commit": "final-release-commit",
                    "installer_sha256_verified": True,
                },
                "dry_run": True,
                "installer_execution_performed": True,
                "launch_performed": False,
                "proof_center_smoke_performed": True,
                "workspace_command_smoke_performed": True,
                "uninstall_performed": True,
                "release_ready": False,
                "authority_granted": False,
            }
        ),
        encoding="utf-8",
    )

    result = transcript.validate_file(path)

    assert result["status"] == "blocked"
    assert "dry_run must be false" in result["errors"]
    assert "launch_performed must be true" in result["errors"]


def test_windows_clean_host_smoke_script_installs_launches_and_validates_transcript():
    root = Path(__file__).resolve().parents[1]
    script = root / "scripts" / "release" / "run_windows_clean_host_install_smoke.ps1"
    text = script.read_text(encoding="utf-8")

    assert "msiexec.exe" in text
    assert "Start-Process" in text
    assert "Get-AuthenticodeSignature" in text
    assert "Test-BinaryContainsAscii" in text
    assert "frontend\\out" not in text
    assert "clean_host_install_transcript.py" in text
    assert "installer_execution_performed = $InstallPassed" in text
    assert "launch_performed = $LaunchPassed" in text
    assert "proof_center_smoke_performed = $ProofCenterSmokePassed" in text
    assert "workspace_command_smoke_performed = $WorkspaceSmokePassed" in text
    assert "uninstall_performed = $UninstallPassed" in text
    assert "[switch]$AllowDeveloperHostSmoke" in text
    assert '$IsGitHubWindowsRunner = $true' not in text
    assert '$env:GITHUB_ACTIONS -eq "true"' in text
    assert "Use -AllowDeveloperHostSmoke only for non-release local smoke output" in text
    assert "Developer-host smoke transcript written" in text
    assert "host_reused_from_developer_machine = -not $IsGitHubWindowsRunner" in text
