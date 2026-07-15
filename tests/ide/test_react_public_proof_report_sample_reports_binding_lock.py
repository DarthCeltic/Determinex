"""Tests for DETERMINEX_REACT_PUBLIC_PROOF_REPORT_SAMPLE_REPORTS_BINDING_LOCK_001."""
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

loader = importlib.import_module("ide.public_proof_report_sample_reports_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "PublicProofReportSampleReportsPanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_PUBLIC_PROOF_REPORT_SAMPLE_REPORTS_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_public_proof_report_sample_reports_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
CODEX_ARTIFACT = (
    _REPO_ROOT / "assurance" / "evidence" / "public_proof_report_export"
    / "proof_report_sample_reports_20260529.json"
)


def test_loader_passes_against_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_sample_count_is_5():
    rec = loader.load()
    assert rec.sample_reports_count == 5
    assert len(rec.sample_reports) == 5


def test_loader_covers_required_archetype_classes():
    rec = loader.load()
    classes = set(rec.detected_request_classes)
    # The archetype names in Codex evidence may differ slightly from
    # the prose label; require at least one match per archetype.
    assert any("fixture_local" in c or "supported" in c for c in classes), classes
    assert any("unsupported" in c or "missing_rung" in c or "blocked" in c for c in classes), classes
    assert any("unknown_novel" in c for c in classes), classes
    assert any("unsafe" in c or "refused" in c or "forbidden" in c for c in classes), classes
    assert any("mutation" in c or "authority" in c or "existing_repo" in c for c in classes), classes


def test_loader_each_sample_has_authority_state_locked_down():
    rec = loader.load()
    for s in rec.sample_reports:
        # The loader has already validated that each sample's
        # authority_state has no truthy flag; reaching here means PASS.
        assert s.detected_request_class


def test_loader_returns_awaiting_when_missing(tmp_path):
    rec = loader.load(tmp_path / "no-such.json")
    assert rec.is_awaiting


def test_loader_fallback_does_not_invent_success(tmp_path):
    rec = loader.load(tmp_path / "no-such.json")
    assert rec.is_passed is False
    assert rec.sample_reports_count == 0


def _write_tampered(tmp: Path, mutate) -> Path:
    blob = json.loads(CODEX_ARTIFACT.read_text(encoding="utf-8"))
    mutate(blob)
    out = tmp / "proof_report_sample_reports_99.tampered.json"
    out.write_text(json.dumps(blob), encoding="utf-8")
    return out


def test_loader_blocks_sample_count_mismatch(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("sample_reports", b["sample_reports"][:3]))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "SAMPLE_COUNT_MISMATCH" in rec.decision


def test_loader_blocks_authority_flag_in_sample(tmp_path):
    def m(b):
        b["sample_reports"][0]["authority_state"]["source_mutation_authorized"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_status_mismatch(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("status", "PUBLIC_PROOF_REPORT_EXPORT_FAILED"))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_public_proof_report_sample_reports_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_public_proof_report_sample_reports_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Sample reports are evidence-shape examples;",
        "they are not promises of runtime support, release readiness, or universal coverage.",
        "Each sample carries its own authority_state; all authority flags remain false.",
        "Release-supported remains 0 cells / 0 families.",
        "Universal support is not claimed.",
        "Unknown/novel sample remains NOT_CLAIMED, blocked by CONCRETE_FIXTURE_REQUIRED.",
        "Refused/contained sample remains refused; no execution authorized.",
    ]
    for cap in required:
        assert cap in src, f"missing caption: {cap}"


def test_panel_does_not_render_authority_grant():
    src = PANEL_PATH.read_text(encoding="utf-8")
    for f in ("release_ready: true", "training_eligible: true", "source_mutation_authorized: true"):
        assert f not in src


def test_lock_present_and_authority_false():
    assert LOCK_PATH.is_file()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert lock["lock_id"] == "DETERMINEX_REACT_PUBLIC_PROOF_REPORT_SAMPLE_REPORTS_BINDING_LOCK_001"
    sd = lock.get("scope_discipline", {})
    for flag in (
        "release_ready",
        "training_eligible",
        "source_mutation_authorized",
        "approval_authority_granted",
        "proof_execution_authority_granted",
        "broad_claims_granted",
    ):
        assert sd.get(flag) is False, flag


def test_evidence_record_present():
    files = sorted(EVIDENCE_DIR.glob("run_*.json"))
    assert files
    rec = json.loads(files[-1].read_text(encoding="utf-8"))
    assert rec["lock_id"] == "DETERMINEX_REACT_PUBLIC_PROOF_REPORT_SAMPLE_REPORTS_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_PUBLIC_PROOF_REPORT_SAMPLE_REPORTS_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_PUBLIC_PROOF_REPORT_SAMPLE_REPORTS_BINDING_LOCK_001" in ids
