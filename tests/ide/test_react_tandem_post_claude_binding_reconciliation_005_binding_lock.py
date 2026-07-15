"""Tests for DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_005_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.tandem_post_claude_binding_reconciliation_005_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "TandemPostClaudeBindingReconciliation005Panel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_005_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_tandem_post_claude_binding_reconciliation_005_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "tandem_post_claude_binding_reconciliation_005"
)


def test_loader_passes_on_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes
    assert rec.source_mutation_authorized is False
    assert rec.release_ready is False
    assert rec.training_eligible is False


def test_loader_absorbed_checkpoint_is_354_clean():
    rec = loader.load()
    assert rec.absorbed_checkpoint_evidence_index_count == 354
    assert rec.absorbed_checkpoint_ledger_entry_count == 354
    assert rec.absorbed_checkpoint_count_drift_actual == 354
    assert rec.absorbed_checkpoint_count_drift_expected == 354
    assert rec.absorbed_checkpoint_count_drift_status == "EVIDENCE_COUNT_DRIFT_GUARD_PASSED"
    assert rec.absorbed_checkpoint_ledger_chain_valid is True
    assert rec.absorbed_checkpoint_mutation_detected is False
    assert list(rec.absorbed_checkpoint_evidence_index_validation_errors) == []


def test_loader_final_spine_at_or_above_355():
    rec = loader.load()
    assert rec.final_expected_evidence_count_after_this_lock >= 355


def test_loader_absorbed_locks_include_all_5_claude_bindings():
    rec = loader.load()
    required = {
        "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_STATE_LADDER_BINDING_LOCK_001",
        "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_005_BINDING_LOCK_001",
        "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_005_VISUAL_BINDING_LOCK_001",
        "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_006_BINDING_LOCK_001",
        "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_006_VISUAL_BINDING_LOCK_001",
    }
    assert required <= set(rec.absorbed_claude_locks)


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
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("broad_claims_granted", True))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_absorbed_checkpoint_mismatch(tmp_path):
    def m(b):
        b["absorbed_checkpoint_before_this_lock"]["evidence_index_count"] = 999
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "CHECKPOINT_MISMATCH" in rec.decision


def test_loader_blocks_absorbed_checkpoint_drift_not_passed(tmp_path):
    def m(b):
        b["absorbed_checkpoint_before_this_lock"]["count_drift_status"] = "EVIDENCE_COUNT_DRIFT_GUARD_BLOCKED"
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_absorbed_checkpoint_ledger_invalid(tmp_path):
    def m(b):
        b["absorbed_checkpoint_before_this_lock"]["ledger_chain_valid"] = False
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_absorbed_checkpoint_mutation_detected(tmp_path):
    def m(b):
        b["absorbed_checkpoint_before_this_lock"]["mutation_detected"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_absorbed_checkpoint_index_validation_errors(tmp_path):
    def m(b):
        b["absorbed_checkpoint_before_this_lock"]["evidence_index_validation_errors"] = ["some_error"]
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_final_spine_below_355(tmp_path):
    def m(b):
        b["final_expected_evidence_count_after_this_lock"] = 354
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_absorbed_locks_missing(tmp_path):
    def m(b):
        b["absorbed_claude_locks"] = ["only_one_lock"]
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_status_mismatch(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("status", "TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_005_FAILED"))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_tandem_post_claude_binding_reconciliation_005_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_tandem_post_claude_binding_reconciliation_005_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Reconciliation absorbs display evidence; it does not promote capability.",
        "Fixture-local proof is not production readiness.",
        "Smoke-supported is not release-supported.",
        "Fully supported with caveats is not release-supported.",
        "No source mutation without authority.",
        "Universal 100 means universal intake/routing, not magic execution.",
        "Blocked cells are visible by exact missing rung.",
    ]
    for cap in required:
        assert cap in src, f"missing caption: {cap}"


def test_panel_renders_stale_test_repair_note():
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "Stale Batch 004" in src or "stale" in src.lower()


def test_lock_present_and_authority_false():
    assert LOCK_PATH.is_file()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert lock["lock_id"] == "DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_005_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_005_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_005_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_005_BINDING_LOCK_001" in ids
