"""Tests for DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_WAVE_001_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.universal_100_depth_promotion_wave_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "Universal100DepthPromotionWave001Panel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_WAVE_001_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_universal_100_depth_promotion_wave_001_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "universal_100_depth_promotion_wave_001"
)


def test_loader_passes_against_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_wave_totals():
    rec = loader.load()
    assert rec.cells_probed == 9
    assert rec.cells_promoted == 8
    assert rec.cells_blocked == 1
    assert rec.families_with_any_evidence_before == 18
    assert rec.release_supported == 0
    assert rec.user_ready_with_caveats == 0


def test_loader_families_improved_count():
    rec = loader.load()
    assert len(rec.families_improved) == 8


def test_loader_includes_all_three_batches():
    rec = loader.load()
    batch_ids = {b.batch_id for b in rec.batches}
    assert batch_ids == {"017", "018", "019"}


def test_loader_includes_all_three_deltas():
    rec = loader.load()
    delta_ids = {d.batch_id for d in rec.deltas}
    assert delta_ids == {"017", "018", "019"}


def test_loader_blocked_cell_is_unknown_novel():
    rec = loader.load()
    assert len(rec.blocked_cells) == 1
    assert rec.blocked_cells[0].cell_id == "unknown_novel_intake_route"
    assert "CONCRETE_FIXTURE_REQUIRED" in rec.blocked_cells[0].missing_rung


def test_loader_returns_awaiting_when_missing(tmp_path):
    rec = loader.load(tmp_path / "no-such")
    assert rec.is_awaiting


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


def test_loader_blocks_release_supported_without_proof(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("release_supported", 1))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_loader_blocks_user_ready_overclaim(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("user_ready_with_caveats", 1))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "USER_READY_OVERCLAIM" in rec.decision


def test_loader_blocks_blocked_cells_hidden(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.pop("blocked_cells", None))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BLOCKED_CELLS_HIDDEN" in rec.decision


def test_loader_blocks_batches_dict_missing(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.pop("batches", None))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_deltas_dict_missing(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.pop("deltas", None))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_status_mismatch(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__("status", "UNIVERSAL_100_DEPTH_PROMOTION_WAVE_001_FAILED"),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_universal_100_depth_promotion_wave_001_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_universal_100_depth_promotion_wave_001_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Depth promotion raises proof depth; it does not create universal support.",
        "Wave aggregates batches; it does not promote cells.",
        "roadmap is universal by intake, routing, blocker accounting, and proof discipline.",
        "Universal roadmap does not mean every edge case is supported today.",
        "Every edge case must be supported, blocked by exact missing rung, forbidden, or roadmap.",
        "Family evidence is not full family support.",
        "Unknown/novel routing is not arbitrary app support.",
        "Release-supported remains 0.",
        "Blocked cells remain visible by exact missing rung.",
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
    assert lock["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_WAVE_001_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_WAVE_001_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_WAVE_001_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_WAVE_001_BINDING_LOCK_001" in ids
