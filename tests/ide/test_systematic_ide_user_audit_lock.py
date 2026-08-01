"""Tests for the systematic user-facing IDE audit."""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

audit_mod = importlib.import_module("ide.systematic_ide_user_audit")


def test_systematic_audit_sections_pass_for_current_checkout():
    report = audit_mod.collect(_REPO_ROOT)
    payload = report.to_dict()

    assert payload["schema_version"] == "determinex-systematic-ide-user-audit-v1"
    assert payload["release_ready"] is False
    assert payload["authority_granted"] is False
    # `release_gates` reads assurance/evidence/determinex_release_gate_status/, and
    # assurance/ is on publish_mirror.NEVER -- so in the public checkout that section is
    # blocked for a structural reason, not a regression. Everything else must still be
    # unblocked, which is what this assertion is actually protecting.
    _evidence = _REPO_ROOT / "assurance" / "evidence"
    expected_blocked = [] if _evidence.is_dir() else ["release_gates"]
    assert payload["blocked_section_ids"] == expected_blocked
    section_ids = {section["section_id"] for section in payload["sections"]}
    assert section_ids == {
        "mission_control",
        "tools_and_providers",
        "backend_commands",
        "release_gates",
        "repair_panels",
        "llm_program_advisor",
    }


def test_audit_report_written_with_non_authorizing_notes(tmp_path: Path):
    output = tmp_path / "audit.json"
    report = audit_mod.write_report(output, _REPO_ROOT)
    text = output.read_text(encoding="utf-8")

    assert report.blocked_section_ids == ()
    assert "does not prove public release readiness" in text
    assert "universal verified support" in text
    assert '"authority_granted": false' in text
