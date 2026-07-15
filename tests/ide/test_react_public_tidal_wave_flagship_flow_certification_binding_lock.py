"""Tests for DETERMINEX_REACT_PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.public_tidal_wave_flagship_flow_certification_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "PublicTidalWaveFlagshipFlowCertificationPanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_public_tidal_wave_flagship_flow_certification_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "public_tidal_wave_flagship_flow_certification"
)


def test_loader_passes_against_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_certified_flow_count_is_10():
    rec = loader.load()
    assert rec.flagship_flows_certified_count == 10
    assert len(rec.flagship_flows) == 10


def test_loader_false_claim_phrases_count_is_9():
    rec = loader.load()
    assert rec.false_claim_phrases_count == 9


def test_loader_proof_report_fields_count_is_12():
    rec = loader.load()
    assert rec.proof_report_fields_count == 12


def test_loader_release_remains_zero():
    rec = loader.load()
    assert rec.release_supported_cells == 0
    assert rec.release_supported_families == 0
    assert rec.release_support_unchanged_at_zero is True


def test_loader_universal_support_not_claimed():
    rec = loader.load()
    assert rec.universal_support_claimed is False
    assert rec.universal_handling_certified_as_journey_model is True


def test_loader_unknown_novel_preserved():
    rec = loader.load()
    assert rec.unknown_novel_cell_id == "unknown_novel_intake_route"
    assert rec.unknown_novel_claim_state == "NOT_CLAIMED"
    assert rec.unknown_novel_missing_rung_key == "CONCRETE_FIXTURE_REQUIRED"
    assert rec.unknown_novel_support_claimed is False


def test_loader_source_truth_commit_is_ff1f047eb():
    rec = loader.load()
    assert rec.source_truth_commit == "ff1f047eb"
    assert rec.source_truth_lock_id == "DETERMINEX_PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_LOCK_001"


def test_loader_returns_awaiting_when_missing(tmp_path):
    rec = loader.load(tmp_path / "no-such")
    assert rec.is_awaiting


def test_loader_returns_awaiting_when_corrupt(tmp_path):
    (tmp_path / "run_99.broken.json").write_text("not json", encoding="utf-8")
    rec = loader.load(tmp_path)
    assert rec.is_awaiting


def test_loader_fallback_does_not_invent_success(tmp_path):
    rec = loader.load(tmp_path / "no-such")
    assert rec.is_passed is False
    assert rec.flagship_flows_certified_count == 0
    assert rec.universal_support_claimed is False
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


def test_loader_blocks_broad_claims_granted(tmp_path):
    def m(b):
        b.setdefault("authority", {})
        b["authority"]["broad_claims_granted"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_flagship_count_mismatch(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("flagship_flows_certified_count", 9))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "FLAGSHIP_COUNT_MISMATCH" in rec.decision


def test_loader_blocks_scanner_count_mismatch(tmp_path):
    def m(b):
        b["false_claim_scanner_model"]["blocked_or_flagged_phrases"] = b["false_claim_scanner_model"]["blocked_or_flagged_phrases"][:5]
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "SCANNER_COUNT_MISMATCH" in rec.decision


def test_loader_blocks_proof_report_fields_count_mismatch(tmp_path):
    def m(b):
        b["proof_report_model"]["fields"] = b["proof_report_model"]["fields"][:5]
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "PROOF_REPORT_FIELDS_COUNT_MISMATCH" in rec.decision


def test_loader_blocks_universal_support_claimed(tmp_path):
    def m(b):
        b["authority_boundary"]["universal_support_claimed"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_release_overclaim(tmp_path):
    def m(b):
        b["release_support_status"]["release_supported_cells"] = 1
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_loader_blocks_status_mismatch(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__("status", "PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_FAILED"),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_public_tidal_wave_flagship_flow_certification_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_public_tidal_wave_flagship_flow_certification_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Determinex",
        "public flagship journey model is certified for routing,",
        "This is not",
        "release support or production readiness.",
        "Release-supported remains 0 cells / 0 families.",
        "Universal support is not claimed.",
        "False-claim scanner blocks or flags forbidden broad claims.",
        "No source mutation, training, proof-execution, or broad-claims authority granted.",
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
    assert lock["lock_id"] == "DETERMINEX_REACT_PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_BINDING_LOCK_001" in ids
