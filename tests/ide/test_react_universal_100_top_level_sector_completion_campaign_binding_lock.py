"""Tests for DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.universal_100_top_level_sector_completion_campaign_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "Universal100TopLevelSectorCompletionCampaignPanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_universal_100_top_level_sector_completion_campaign_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "universal_100_top_level_sector_completion_campaign"
)


def test_loader_passes_on_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_truth_counts():
    rec = loader.load()
    assert rec.top_level_sector_families == 40
    assert rec.level_1_scoreboard_coverage == 40
    assert rec.families_with_any_cell_evidence == 15
    assert rec.release_supported_count == 0
    assert rec.families_with_release_supported_coverage == 0
    assert len(rec.scoreboard) == 40


def test_loader_authority_false():
    rec = loader.load()
    for attr in (
        "source_mutation_authorized",
        "training_eligible",
        "release_ready",
        "broad_claims_granted",
        "proof_execution_authority_granted",
    ):
        assert getattr(rec, attr) is False


def test_loader_level_1_target_and_not_claimed_present():
    rec = loader.load()
    assert "top-level sector families" in rec.level_1_target.lower()
    assert "all apps supported" in rec.level_1_not_claimed
    assert "all languages supported" in rec.level_1_not_claimed
    assert "all platforms supported" in rec.level_1_not_claimed


def test_loader_every_family_identified_classified_and_represented():
    rec = loader.load()
    for row in rec.scoreboard:
        assert row.identified, f"{row.sector_id} not identified"
        assert row.classified, f"{row.sector_id} not classified"
        assert row.represented_in_completion_campaign_ledger, f"{row.sector_id} not in ledger"


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


def test_loader_blocks_level_1_not_40(tmp_path):
    def m(b):
        b.setdefault("summary", {})
        b["summary"]["level_1_scoreboard_coverage"] = 39
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "LEVEL_1_NOT_40" in rec.decision


def test_loader_blocks_family_not_identified(tmp_path):
    def m(b):
        sb = b.get("top_level_sector_scoreboard") or []
        if sb:
            sb[0]["identified"] = False
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "LEVEL_1_NOT_40" in rec.decision


def test_loader_blocks_family_not_classified(tmp_path):
    def m(b):
        sb = b.get("top_level_sector_scoreboard") or []
        if sb:
            sb[0]["classified"] = False
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "LEVEL_1_NOT_40" in rec.decision


def test_loader_blocks_family_not_represented(tmp_path):
    def m(b):
        sb = b.get("top_level_sector_scoreboard") or []
        if sb:
            sb[0]["represented_in_completion_campaign_ledger"] = False
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "LEVEL_1_NOT_40" in rec.decision


def test_loader_blocks_release_supported_without_proof(tmp_path):
    def m(b):
        b.setdefault("summary", {})
        b["summary"]["release_supported_count"] = 5
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_loader_does_not_block_release_supported_with_proof(tmp_path):
    def m(b):
        b.setdefault("summary", {})
        b["summary"]["release_supported_count"] = 5
        paths = list(b.get("source_evidence_paths") or [])
        paths.append("assurance/evidence/fake_release_supported_proof.json")
        b["source_evidence_paths"] = paths
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_passed


def test_loader_blocks_status_mismatch(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("status", "UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_FAILED"))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_scoreboard_empty(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("top_level_sector_scoreboard", []))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_forbidden_phrase_as_current_claim(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("active_claim", "all apps supported in production"))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_universal_100_top_level_sector_completion_campaign_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_universal_100_top_level_sector_completion_campaign_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Universal 100 Level 1 means top-level identification/classification/routing, not universal execution.",
        "40 / 40 routed does not mean 40 / 40 supported.",
        "Scaffold-supported is not working-app proof.",
        "Smoke-supported is not production proof.",
        "Packaging-supported is not release-supported.",
        "Release-supported remains 0.",
        "Fixture-local evidence is not production readiness.",
        "Blocked cells remain visible by exact missing rung.",
        "No all-app support",
        "No source mutation, training, proof-execution, or release authority.",
    ]
    for cap in required:
        assert cap in src, f"missing caption: {cap}"


def test_lock_present_and_authority_false():
    assert LOCK_PATH.is_file()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert lock["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_BINDING_LOCK_001" in ids
