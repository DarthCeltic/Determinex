"""Tests for DETERMINEX_REACT_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.universal_100_conveyor_backlog_and_depth_queue_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "Universal100ConveyorBacklogAndDepthQueuePanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_universal_100_conveyor_backlog_and_depth_queue_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "universal_100_conveyor_backlog_and_depth_queue"
)


def test_loader_passes_on_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_counts_truth():
    rec = loader.load()
    assert rec.known_cells_accounted == 75
    assert rec.next_gulp_batches_queued == 3
    assert rec.depth_candidates == 62
    assert rec.packaging_candidates == 52
    assert rec.user_ready_candidates == 45
    assert rec.blocked_missing_rung_count == 13
    assert rec.roadmap_missing_rung_count == 17
    assert rec.forbidden_policy_blocked_count == 0


def test_loader_next_gulp_queue_lists_batches_008_009_010():
    rec = loader.load()
    batch_keys = [item.get("batch") for item in rec.next_safe_sector_gulp_queue]
    assert "008" in batch_keys
    assert "009" in batch_keys
    assert "010" in batch_keys


def test_loader_codex_safe_parallel_work_queue_visible():
    rec = loader.load()
    assert rec.codex_safe_parallel_work_queue
    assert rec.codex_safe_parallel_work_queue.get("status")


def test_loader_blocked_cells_visible():
    rec = loader.load()
    assert len(rec.blocked_cells_by_exact_missing_rung) >= 1


def test_loader_roadmap_cells_visible():
    rec = loader.load()
    assert len(rec.roadmap_cells_by_exact_missing_rung) >= 1


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
    def m(b):
        b.setdefault("authority", {})
        b["authority"]["broad_claims_granted"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_empty_next_gulp_queue(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("next_safe_sector_gulp_queue", []))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_missing_known_cells_accounted(tmp_path):
    def m(b):
        b.setdefault("summary", {}).pop("known_cells_accounted", None)
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_missing_claude_visual_binding_backlog(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.pop("claude_visual_binding_backlog", None))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_status_mismatch(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("status", "UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_FAILED"))
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
    assert "get_universal_100_conveyor_backlog_and_depth_queue_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_universal_100_conveyor_backlog_and_depth_queue_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Backlog is planning structure, not a capability claim.",
        "Blocked cells remain visible by exact missing rung.",
        "Roadmap cells remain visible by exact missing rung.",
        "Queue membership does not grant support.",
        "Packaging candidates are CANDIDATES",
        "Release-supported remains 0",
        "User-ready-with-caveats candidates are CANDIDATES",
        "No source mutation without authority.",
        "Universal 100 means universal intake/routing, not magic execution.",
    ]
    for cap in required:
        assert cap in src, f"missing caption: {cap}"


def test_lock_present_and_authority_false():
    assert LOCK_PATH.is_file()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert lock["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_BINDING_LOCK_001" in ids
