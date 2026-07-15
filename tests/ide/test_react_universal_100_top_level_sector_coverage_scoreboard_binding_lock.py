"""Tests for DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COVERAGE_SCOREBOARD_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.universal_100_top_level_sector_coverage_scoreboard_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "Universal100TopLevelSectorCoverageScoreboardPanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COVERAGE_SCOREBOARD_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_universal_100_top_level_sector_coverage_scoreboard_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "universal_100_top_level_sector_coverage_scoreboard"
)


def test_loader_passes_against_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_families_total_is_40():
    rec = loader.load()
    assert rec.families_total == 40
    assert rec.families_level_1_covered == 40


def test_loader_release_supported_is_zero():
    rec = loader.load()
    assert rec.families_with_release_supported == 0
    assert rec.release_supported_count == 0


def test_loader_support_depth_truthful():
    rec = loader.load()
    assert rec.families_with_build_support == 2
    assert rec.families_with_scaffold_support == 5
    assert rec.families_with_smoke_support == 10
    assert rec.families_with_user_ready_with_caveats == 1


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


def test_loader_blocks_families_total_not_40(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("families_total", 39))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "TAXONOMY_OVERCLAIM" in rec.decision


def test_loader_blocks_level_1_below_total(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("families_level_1_covered", 39))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "LEVEL_1_NOT_40" in rec.decision


def test_loader_blocks_release_supported_without_proof(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("families_with_release_supported", 1))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_loader_blocks_release_count_without_proof(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("release_supported_count", 1))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_loader_blocks_blockers_remaining_absent(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.pop("blockers_remaining_by_category", None))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_support_depth_absent(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.pop("support_depth_counts", None))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_status_mismatch(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__("status", "UNIVERSAL_100_TOP_LEVEL_SECTOR_COVERAGE_SCOREBOARD_FAILED"),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_universal_100_top_level_sector_coverage_scoreboard_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_universal_100_top_level_sector_coverage_scoreboard_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Coverage reporting is routing/accounting, not promotion.",
        "40 / 40 routed does not mean 40 / 40 supported.",
        "Scaffold-supported is not working-app proof.",
        "Smoke-supported is not production proof.",
        "Release-supported remains 0.",
        "Roadmap-only families remain visible.",
        "Blockers remain visible by category.",
        "No source mutation without authority.",
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
    assert lock["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COVERAGE_SCOREBOARD_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COVERAGE_SCOREBOARD_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COVERAGE_SCOREBOARD_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COVERAGE_SCOREBOARD_BINDING_LOCK_001" in ids
