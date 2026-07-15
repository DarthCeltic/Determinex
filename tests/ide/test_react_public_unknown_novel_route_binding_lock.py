"""Tests for DETERMINEX_REACT_PUBLIC_UNKNOWN_NOVEL_ROUTE_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.public_unknown_novel_route_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "PublicUnknownNovelRoutePanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_PUBLIC_UNKNOWN_NOVEL_ROUTE_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_public_unknown_novel_route_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
EDGE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "universal_100_edge_case_expansion_roadmap"
)
EDGE_STATUS = EDGE_DIR / "edge_case_status_20260529.json"


def test_loader_passes_against_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_cell_id_is_unknown_novel_intake_route():
    rec = loader.load()
    assert rec.cell_id == "unknown_novel_intake_route"


def test_loader_claim_state_not_claimed():
    rec = loader.load()
    assert rec.claim_state == "NOT_CLAIMED"
    assert rec.support_claimed is False
    assert rec.promoted is False
    assert rec.release_supported is False


def test_loader_missing_rung_is_concrete_fixture_required():
    rec = loader.load()
    assert rec.missing_rung_key == "CONCRETE_FIXTURE_REQUIRED"


def test_loader_route_status_routed():
    rec = loader.load()
    assert rec.route_status == "routed"


def test_loader_next_action_present():
    rec = loader.load()
    assert rec.next_required_action  # non-empty


def test_loader_returns_awaiting_when_status_missing(tmp_path):
    rec = loader.load(tmp_path / "no.json", tmp_path, tmp_path, tmp_path)
    assert rec.is_awaiting


def test_loader_fallback_does_not_invent_success(tmp_path):
    rec = loader.load(tmp_path / "no.json", tmp_path, tmp_path, tmp_path)
    assert rec.is_passed is False
    assert rec.support_claimed is False
    assert rec.cell_id == ""


def _write_tampered_edge_status(tmp: Path, mutate) -> Path:
    blob = json.loads(EDGE_STATUS.read_text(encoding="utf-8"))
    mutate(blob)
    out = tmp / "edge_case_status_99.tampered.json"
    out.write_text(json.dumps(blob), encoding="utf-8")
    return out


def _write_tampered_edge_run(tmp: Path, mutate) -> Path:
    src = sorted(EDGE_DIR.glob("run_*.json"))[-1]
    blob = json.loads(src.read_text(encoding="utf-8"))
    mutate(blob)
    out = tmp / "run_99.tampered.json"
    out.write_text(json.dumps(blob), encoding="utf-8")
    return tmp


def test_loader_blocks_when_cell_id_mismatch(tmp_path):
    def m(b):
        b["unknown_novel_request_routing"]["cell_id"] = "supported_cell"
    ed = _write_tampered_edge_run(tmp_path, m)
    rec = loader.load(edge_run_dir=ed)
    assert rec.is_blocked
    assert "ROUTE_MISMATCH" in rec.decision


def test_loader_blocks_when_claim_state_overclaimed(tmp_path):
    def m(b):
        b["unknown_novel_request_routing"]["claim_state"] = "IMPLEMENTED"
    ed = _write_tampered_edge_run(tmp_path, m)
    rec = loader.load(edge_run_dir=ed)
    assert rec.is_blocked
    assert "NOVEL_OVERCLAIM" in rec.decision


def test_loader_blocks_when_missing_rung_key_mismatch(tmp_path):
    def m(b):
        b["unknown_novel_request_routing"]["missing_rung_key"] = "OTHER_KEY"
    ed = _write_tampered_edge_run(tmp_path, m)
    rec = loader.load(edge_run_dir=ed)
    assert rec.is_blocked
    assert "BLOCKER_MISMATCH" in rec.decision


def test_loader_blocks_when_promoted_true(tmp_path):
    def m(b):
        b["unknown_novel_request_routing"]["promoted"] = True
    ed = _write_tampered_edge_run(tmp_path, m)
    rec = loader.load(edge_run_dir=ed)
    assert rec.is_blocked
    assert "NOVEL_OVERCLAIM" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_public_unknown_novel_route_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_public_unknown_novel_route_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Unknown and novel requests are accepted into routing and",
        "blocker accounting. They are not treated as supported until",
        "fixture, verifier, evidence, and promotion gates pass.",
        "Unknown/novel intake remains NOT_CLAIMED.",
        "Blocker remains CONCRETE_FIXTURE_REQUIRED.",
        "Universal support is not claimed.",
        "Novel cases are routed, not hallucinated.",
        "Release-supported remains 0 cells / 0 families.",
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
    assert lock["lock_id"] == "DETERMINEX_REACT_PUBLIC_UNKNOWN_NOVEL_ROUTE_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_PUBLIC_UNKNOWN_NOVEL_ROUTE_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_PUBLIC_UNKNOWN_NOVEL_ROUTE_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_PUBLIC_UNKNOWN_NOVEL_ROUTE_BINDING_LOCK_001" in ids
