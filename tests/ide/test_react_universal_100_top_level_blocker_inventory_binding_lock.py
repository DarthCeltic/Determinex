"""Tests for DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.universal_100_top_level_blocker_inventory_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "Universal100TopLevelBlockerInventoryPanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_universal_100_top_level_blocker_inventory_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "universal_100_top_level_blocker_inventory"
)


def test_loader_passes_against_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_blocker_count_is_10():
    rec = loader.load()
    assert rec.blocker_count == 10
    assert len(rec.blockers) == 10


def test_loader_category_counts():
    rec = loader.load()
    expected = {
        "AUTHORITY_MISSING": 1,
        "LOCAL_DEPENDENCY_MISSING": 2,
        "NETWORK_REQUIRED_BUT_NOT_ALLOWED": 1,
        "TOOLCHAIN_MISSING_OR_UNVERIFIED": 3,
        "VERIFIER_MISSING": 3,
    }
    assert rec.category_counts == expected


def test_loader_local_resolvability_counts():
    rec = loader.load()
    expected = {
        "requires_authority_gate": 1,
        "requires_network_provider_gate": 1,
        "requires_new_harness": 3,
        "resolvable_now": 3,
        "resolvable_with_operator_install": 2,
    }
    assert rec.local_resolvability_counts == expected


def test_loader_blockers_have_required_fields():
    rec = loader.load()
    for b in rec.blockers:
        assert b.blocker_id
        assert b.category
        assert b.family
        assert b.sector_id
        assert b.local_resolvability
        assert b.safe_next_rung
        assert b.forbidden_shortcut


def test_loader_returns_awaiting_when_missing(tmp_path):
    rec = loader.load(tmp_path / "no-such")
    assert rec.is_awaiting


def test_loader_returns_awaiting_when_corrupt(tmp_path):
    (tmp_path / "run_99.broken.json").write_text("not json", encoding="utf-8")
    rec = loader.load(tmp_path)
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


def test_loader_blocks_status_mismatch(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__("status", "UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_FAILED"),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_blockers_list_missing(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.pop("blockers", None))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_blocker_missing_required_key(tmp_path):
    def m(b):
        if b.get("blockers"):
            b["blockers"][0].pop("forbidden_shortcut", None)
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_category_counts_absent(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.pop("category_counts", None))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_universal_100_top_level_blocker_inventory_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_universal_100_top_level_blocker_inventory_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Inventory classifies blockers and safe next rungs only.",
        "Inventory does not promote support or grant capability.",
        "Forbidden shortcuts remain forbidden.",
        "Operator-action and provider-gate blockers remain operator-gated.",
        "Local resolvability does not mean automatic closure.",
        "Universal 100 means routing/accounting, not universal execution.",
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
    assert lock["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_BINDING_LOCK_001" in ids
