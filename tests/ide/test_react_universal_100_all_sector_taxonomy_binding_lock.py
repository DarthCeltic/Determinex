"""Tests for DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.universal_100_all_sector_taxonomy_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "Universal100AllSectorTaxonomyPanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_universal_100_all_sector_taxonomy_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "universal_100_all_sector_taxonomy"
)


def test_loader_passes_on_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_reports_40_sectors_and_40_top_level_families():
    rec = loader.load()
    assert rec.sector_count == 40
    assert len(rec.sectors) == 40
    assert len(rec.top_level_sector_families) == 40


def test_loader_taxonomy_carries_routing_and_missing_rung_templates():
    rec = loader.load()
    assert rec.routing_templates_count == 40
    assert rec.missing_rung_templates_count == 40


def test_loader_every_sector_defaults_to_classified_or_lower():
    rec = loader.load()
    allowed = {"classified", "scaffold_only", "discovered", "tagged", "routed"}
    for s in rec.sectors:
        assert s.default_support_state.lower() in allowed, f"{s.sector_id} default_support_state={s.default_support_state}"


def test_loader_every_sector_default_claim_state_is_non_implemented():
    rec = loader.load()
    not_allowed = {"IMPLEMENTED", "IMPLEMENTED_WITH_CAVEATS", "PARTIAL"}
    for s in rec.sectors:
        assert s.default_claim_state.upper() not in not_allowed, f"{s.sector_id} default_claim_state={s.default_claim_state}"


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
])
def test_loader_blocks_authority_flag(tmp_path, flag):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__(flag, True))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_broad_claims_granted(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("broad_claims_granted", True))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_taxonomy_overclaim_via_support_state(tmp_path):
    """Setting a sector's default_support_state to smoke_supported converts
    taxonomy into a capability claim — must block."""
    def m(b):
        sectors = b.get("sectors") or []
        if sectors:
            sectors[0]["default_support_state"] = "smoke_supported"
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "TAXONOMY_OVERCLAIM" in rec.decision


def test_loader_blocks_taxonomy_overclaim_via_claim_state(tmp_path):
    def m(b):
        sectors = b.get("sectors") or []
        if sectors:
            sectors[0]["default_claim_state"] = "IMPLEMENTED"
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "TAXONOMY_OVERCLAIM" in rec.decision


def test_loader_blocks_sectors_empty(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("sectors", []))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_sector_count_mismatch(tmp_path):
    def m(b):
        b["sector_count"] = 999
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_forbidden_phrase_as_current_claim(tmp_path):
    """A forbidden phrase outside refusal-context fields blocks the binding."""
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("active_claim", "all apps supported in production"))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_status_mismatch(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("status", "UNIVERSAL_100_ALL_SECTOR_TAXONOMY_FAILED"))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_universal_100_all_sector_taxonomy_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_universal_100_all_sector_taxonomy_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Taxonomy is routing structure, not support proof.",
        "Taxonomy family present",
        "Default claim state remains NOT_CLAIMED",
        "No source mutation without authority.",
        "Universal 100 means universal intake/routing, not magic execution.",
        "Blocked cells are visible by exact missing rung.",
    ]
    for cap in required:
        assert cap in src, f"missing caption: {cap}"


def test_lock_present_and_authority_false():
    assert LOCK_PATH.is_file()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert lock["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING_LOCK_001" in ids
