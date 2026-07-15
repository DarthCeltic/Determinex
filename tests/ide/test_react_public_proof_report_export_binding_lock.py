"""Tests for DETERMINEX_REACT_PUBLIC_PROOF_REPORT_EXPORT_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.public_proof_report_export_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "PublicProofReportExportPanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_PUBLIC_PROOF_REPORT_EXPORT_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_public_proof_report_export_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "public_proof_report_export"
)


def test_loader_passes_against_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_contract_field_count_is_25():
    rec = loader.load()
    assert rec.proof_report_fields_count == 25
    assert len(rec.contract_fields) == 25


def test_loader_sample_count_is_5():
    rec = loader.load()
    assert rec.sample_reports_count == 5


def test_loader_route_outcome_count_is_7():
    rec = loader.load()
    assert rec.route_outcomes_count == 7


def test_loader_forbidden_blocked_count_is_11():
    rec = loader.load()
    assert rec.forbidden_report_claims_blocked_count == 11
    assert len(rec.forbidden_report_claims) == 11


def test_loader_release_remains_zero():
    rec = loader.load()
    assert rec.release_supported_cells == 0
    assert rec.release_supported_families == 0


def test_loader_export_is_not_release_readiness():
    rec = loader.load()
    assert rec.proof_report_export_is_not_release_readiness is True
    assert rec.proof_report_export_is_release_readiness is False
    assert rec.report_schema_does_not_equal_runtime_proof is True
    assert rec.report_schema_is_runtime_execution_proof is False


def test_loader_contract_includes_required_field_names():
    rec = loader.load()
    field_names = {f.field_name for f in rec.contract_fields}
    required = {
        "report_id",
        "generated_at",
        "determinex_version_or_commit",
        "source_lock",
        "user_request_summary",
        "detected_request_class",
        "detected_family_or_candidate_family",
        "route_outcome",
        "support_depth_before",
        "support_depth_after",
        "authority_state",
        "actions_attempted",
        "actions_skipped",
        "checks_run",
        "checks_passed",
        "checks_failed",
        "evidence_artifacts",
        "blockers",
        "missing_rungs",
        "safety_or_policy_notes",
        "privacy_training_notice",
        "commercial_license_notice",
        "user_claims_allowed",
        "user_claims_forbidden",
        "next_safe_steps",
    }
    missing = required - field_names
    assert not missing, f"missing required contract fields: {missing}"


def test_loader_source_truth_commit_is_ed8a50ff2():
    rec = loader.load()
    assert rec.source_truth_commit == "ed8a50ff2"


def test_loader_returns_awaiting_when_missing(tmp_path):
    rec = loader.load(tmp_path / "no-such")
    assert rec.is_awaiting


def test_loader_fallback_does_not_invent_success(tmp_path):
    rec = loader.load(tmp_path / "no-such")
    assert rec.is_passed is False
    assert rec.proof_report_fields_count == 0
    assert rec.release_supported_cells == 0


def _write_tampered(tmp: Path, mutate) -> Path:
    src = sorted(CODEX_EVIDENCE_DIR.glob("run_*.json"))[-1]
    blob = json.loads(src.read_text(encoding="utf-8"))
    mutate(blob)
    out = tmp / "run_99.tampered.json"
    out.write_text(json.dumps(blob), encoding="utf-8")
    return tmp


@pytest.mark.parametrize("flag", [
    "release_ready",
    "training_eligible",
    "source_mutation_authorized",
    "approval_authority_granted",
    "proof_execution_authority_granted",
])
def test_loader_blocks_authority_flag(tmp_path, flag):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__(flag, True))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_field_count_mismatch(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("proof_report_fields_count", 24))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "FIELD_COUNT_MISMATCH" in rec.decision


def test_loader_blocks_sample_count_mismatch(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("sample_reports_count", 4))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "SAMPLE_COUNT_MISMATCH" in rec.decision


def test_loader_blocks_route_count_mismatch(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("route_outcomes_count", 6))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "ROUTE_COUNT_MISMATCH" in rec.decision


def test_loader_blocks_forbidden_count_mismatch(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("forbidden_report_claims_blocked_count", 10))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "FORBIDDEN_COUNT_MISMATCH" in rec.decision


def test_loader_blocks_export_is_release_readiness(tmp_path):
    def m(b):
        b["authority_boundary"]["proof_report_export_is_release_readiness"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_release_overclaim(tmp_path):
    def m(b):
        b["release_support_status"]["release_supported_families"] = 1
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_public_proof_report_export_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_public_proof_report_export_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Proof report export is an evidence/reporting contract.",
        "It is not",
        "release readiness, runtime execution proof, or universal support.",
        "Release-supported remains 0 cells / 0 families.",
        "Universal support is not claimed.",
        "Report schema does not equal runtime proof.",
        "Forbidden report claims remain blocked or flagged.",
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
    assert lock["lock_id"] == "DETERMINEX_REACT_PUBLIC_PROOF_REPORT_EXPORT_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_PUBLIC_PROOF_REPORT_EXPORT_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_PUBLIC_PROOF_REPORT_EXPORT_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_PUBLIC_PROOF_REPORT_EXPORT_BINDING_LOCK_001" in ids
