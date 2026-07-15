import json
import subprocess
from pathlib import Path

from scripts.release import public_distribution_packet


def _write_release_files(root: Path) -> None:
    (root / "LICENSE").write_text("GNU AFFERO GENERAL PUBLIC LICENSE\nVersion 3\n", encoding="utf-8")
    (root / "pyproject.toml").write_text('license = { text = "AGPL-3.0-or-later" }\n', encoding="utf-8")
    (root / "frontend/package.json").parent.mkdir(parents=True)
    (root / "frontend/package.json").write_text('{"license":"AGPL-3.0-or-later"}\n', encoding="utf-8")
    (root / "frontend/src-tauri/Cargo.toml").parent.mkdir(parents=True)
    (root / "frontend/src-tauri/Cargo.toml").write_text('license = "AGPL-3.0-or-later"\n', encoding="utf-8")
    (root / "frontend/vscode-extension/package.json").parent.mkdir(parents=True)
    (root / "frontend/vscode-extension/package.json").write_text('{"license":"AGPL-3.0-or-later"}\n', encoding="utf-8")
    (root / "docs/release").mkdir(parents=True)
    (root / "docs/release/MODEL_NOTICES.md").write_text("# Model Notices\n\nNo bundled model weights.\n", encoding="utf-8")
    (root / "docs/release/THIRD_PARTY_NOTICES.md").write_text("# Third Party Notices\n\nSee SBOMs.\n", encoding="utf-8")


def test_public_distribution_packet_requires_operator_review_for_legal_and_scrub(tmp_path: Path, monkeypatch):
    _write_release_files(tmp_path)
    monkeypatch.setattr(public_distribution_packet, "_secret_scan_clean", lambda pushed: (True, "clean"))

    packet = public_distribution_packet.build_packet(tmp_path, operator_reviewed=False)

    assert packet["schema_version"] == "determinex-legal-public-distribution-evidence-v1"
    assert packet["license_inventory_reviewed"] is True
    assert packet["model_notice_reviewed"] is True
    assert packet["third_party_notices_present"] is True
    assert packet["public_repo_secret_scan_passed"] is True
    assert packet["legal_review_completed"] is False
    assert packet["public_repo_scrub_completed"] is False
    assert packet["authority_granted"] is False


def test_public_distribution_packet_can_record_operator_reviewed_release_packet(tmp_path: Path, monkeypatch):
    _write_release_files(tmp_path)
    monkeypatch.setattr(public_distribution_packet, "_secret_scan_clean", lambda pushed: (True, "clean"))

    packet = public_distribution_packet.build_packet(tmp_path, operator_reviewed=True)

    assert packet["legal_review_completed"] is True
    assert packet["public_repo_scrub_completed"] is True
    assert packet["authority_granted"] is False


def test_public_distribution_packet_writes_json(tmp_path: Path, monkeypatch):
    _write_release_files(tmp_path)
    monkeypatch.setattr(public_distribution_packet, "_secret_scan_clean", lambda pushed: (True, "clean"))
    output = tmp_path / "assurance/evidence/public_distribution/legal_public_distribution_test.json"

    public_distribution_packet.write_packet(tmp_path, output, operator_reviewed=True)

    data = json.loads(output.read_text(encoding="utf-8"))
    assert data["schema_version"] == "determinex-legal-public-distribution-evidence-v1"
    assert data["legal_review_completed"] is True


def test_public_distribution_packet_records_secret_scan_timeout_as_blocker(monkeypatch):
    def timeout(*args, **kwargs):
        raise subprocess.TimeoutExpired(["python", "scripts/security/secret_scan.py", "--pushed"], 240)

    monkeypatch.setattr(public_distribution_packet.subprocess, "run", timeout)

    clean, transcript = public_distribution_packet._secret_scan_clean(pushed=True)

    assert clean is False
    assert "timed out" in transcript
