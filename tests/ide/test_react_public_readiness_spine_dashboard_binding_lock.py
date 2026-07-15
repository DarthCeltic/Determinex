"""Tests for DETERMINEX_REACT_PUBLIC_READINESS_SPINE_DASHBOARD_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.public_readiness_spine_dashboard_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "PublicReadinessSpineDashboardPanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_PUBLIC_READINESS_SPINE_DASHBOARD_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_public_readiness_spine_dashboard_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
RECON_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "tandem_post_claude_binding_reconciliation_010"
)


def test_loader_passes_against_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_evidence_index_count_present():
    rec = loader.load()
    assert rec.evidence_index_count >= 439
    assert rec.ledger_entry_count == rec.evidence_index_count
    assert rec.count_drift_actual == rec.evidence_index_count
    assert rec.count_drift_expected == rec.evidence_index_count
    assert rec.count_drift_stored_index == rec.evidence_index_count


def test_loader_chain_valid_and_no_mutation():
    rec = loader.load()
    assert rec.ledger_chain_valid is True
    assert rec.mutation_detected is False


def test_loader_validation_errors_empty():
    rec = loader.load()
    assert rec.evidence_index_validation_errors == ()
    assert rec.evidence_index_valid is True


def test_loader_release_supported_zero():
    rec = loader.load()
    assert rec.release_supported_cells == 0
    assert rec.release_supported_families == 0


def test_loader_universal_support_not_claimed():
    rec = loader.load()
    assert rec.universal_support_claimed is False


def test_loader_authority_flags_all_false():
    rec = loader.load()
    for attr in (
        "source_mutation_authorized",
        "real_user_source_mutation_authorized",
        "proof_execution_authority_granted",
        "training_eligible",
        "broad_claims_granted",
    ):
        assert getattr(rec, attr) is False, attr


def test_loader_combined_focused_run_passed_default_67():
    rec = loader.load()
    assert rec.combined_focused_run_passed == 67


def test_loader_returns_awaiting_when_index_missing(tmp_path):
    rec = loader.load(tmp_path / "no.json")
    assert rec.is_awaiting


def test_loader_fallback_does_not_invent_success(tmp_path):
    rec = loader.load(tmp_path / "no.json")
    assert rec.is_passed is False
    assert rec.evidence_index_count == 0
    assert rec.ledger_chain_valid is False
    assert rec.release_supported_cells == 0


def test_loader_blocks_when_validation_errors_present(tmp_path):
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    idx["validation_errors"] = ["fabricated_error"]
    p = tmp_path / "evidence_index.json"
    p.write_text(json.dumps(idx), encoding="utf-8")
    rec = loader.load(p)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_when_reconciliation_authority_true(tmp_path):
    src = sorted(RECON_DIR.glob("run_*.json"))[-1]
    rec_blob = json.loads(src.read_text(encoding="utf-8"))
    rec_blob.setdefault("authority", {})["source_mutation_authorized"] = True
    rdir = tmp_path / "recon"
    rdir.mkdir()
    (rdir / "run_99.tampered.json").write_text(json.dumps(rec_blob), encoding="utf-8")
    rec = loader.load(None, rdir)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_public_readiness_spine_dashboard_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_public_readiness_spine_dashboard_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Determinex",
        "public-facing proof spine is clean for these",
        "certified reporting and routing surfaces. This does not mean",
        "public release support, production readiness, arbitrary app",
        "support, or training eligibility.",
        "Release-supported remains 0 cells / 0 families.",
        "Universal support is not claimed.",
        "Proof report export is not release readiness.",
        "Unknown/novel routing is not arbitrary app support.",
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
    assert lock["lock_id"] == "DETERMINEX_REACT_PUBLIC_READINESS_SPINE_DASHBOARD_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_PUBLIC_READINESS_SPINE_DASHBOARD_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_PUBLIC_READINESS_SPINE_DASHBOARD_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_PUBLIC_READINESS_SPINE_DASHBOARD_BINDING_LOCK_001" in ids
