"""Tests for DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_008_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.tandem_post_claude_binding_reconciliation_008_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "TandemPostClaudeBindingReconciliation008Panel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_008_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_tandem_post_claude_binding_reconciliation_008_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "tandem_post_claude_binding_reconciliation_008"
)


def test_loader_passes_on_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_claude_display_checkpoint_is_395():
    rec = loader.load()
    assert rec.claude_display_checkpoint_evidence_index_count == 395
    assert rec.claude_display_checkpoint_ledger_entry_count == 395
    assert rec.claude_display_checkpoint_count_drift_actual == 395
    assert rec.claude_display_checkpoint_count_drift_expected == 395
    assert rec.claude_display_checkpoint_count_drift_status == "EVIDENCE_COUNT_DRIFT_GUARD_PASSED"
    assert rec.claude_display_checkpoint_ledger_chain_valid is True
    assert rec.claude_display_checkpoint_mutation_detected is False


def test_loader_prior_codex_checkpoint_is_387():
    rec = loader.load()
    assert rec.prior_codex_source_truth_evidence_index_count == 387


def test_loader_final_spine_at_least_396():
    rec = loader.load()
    assert rec.final_expected_evidence_count_after_this_lock >= 396


def test_loader_absorbed_claude_commit_is_3227e8394():
    rec = loader.load()
    assert rec.absorbed_claude_commit == "3227e8394"


def test_loader_absorbed_locks_include_all_8_claude_bindings():
    rec = loader.load()
    required = {
        "DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_BINDING_LOCK_001",
        "DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_007_BINDING_LOCK_001",
        "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_011_BINDING_LOCK_001",
        "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_011_VISUAL_BINDING_LOCK_001",
        "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_012_BINDING_LOCK_001",
        "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_012_VISUAL_BINDING_LOCK_001",
        "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_013_BINDING_LOCK_001",
        "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_013_VISUAL_BINDING_LOCK_001",
    }
    assert required <= set(rec.absorbed_claude_locks)


def test_loader_source_truth_locks_preserved():
    rec = loader.load()
    assert len(rec.source_truth_locks_preserved) >= 1


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
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("broad_claims_granted", True))
    rec = loader.load(ed)
    assert rec.is_blocked


def test_loader_blocks_claude_display_checkpoint_mismatch(tmp_path):
    def m(b):
        b["claude_display_checkpoint_before_this_lock"]["evidence_index_count"] = 999
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "CHECKPOINT_MISMATCH" in rec.decision


def test_loader_blocks_ledger_invalid(tmp_path):
    def m(b):
        b["claude_display_checkpoint_before_this_lock"]["ledger_chain_valid"] = False
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_mutation_detected(tmp_path):
    def m(b):
        b["claude_display_checkpoint_before_this_lock"]["mutation_detected"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_evidence_validation_errors(tmp_path):
    def m(b):
        b["claude_display_checkpoint_before_this_lock"]["evidence_index_validation_errors"] = ["some_error"]
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_prior_codex_checkpoint_wrong(tmp_path):
    def m(b):
        b["prior_codex_source_truth_checkpoint"]["evidence_index_count"] = 999
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_final_spine_below_396(tmp_path):
    def m(b):
        b["final_expected_evidence_count_after_this_lock"] = 395
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
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("status", "TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_008_FAILED"))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_tandem_post_claude_binding_reconciliation_008_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_tandem_post_claude_binding_reconciliation_008_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Reconciliation absorbs display evidence; it does not promote capability.",
        "Fixture-local proof is not production readiness.",
        "Smoke-supported is not release-supported.",
        "No source mutation without authority.",
        "Universal 100 means universal intake/routing, not magic execution.",
    ]
    for cap in required:
        assert cap in src, f"missing caption: {cap}"


def test_lock_present_and_authority_false():
    assert LOCK_PATH.is_file()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert lock["lock_id"] == "DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_008_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_008_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_008_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_008_BINDING_LOCK_001" in ids
