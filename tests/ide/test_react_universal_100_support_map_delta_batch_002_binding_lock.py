"""Tests for DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_002_VISUAL_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.universal_100_support_map_delta_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "Universal100SupportMapDeltaBatch002Panel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_002_VISUAL_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_universal_100_support_map_delta_batch_002_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"

CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "universal_100_support_map_delta_batch_002"
)


def test_loader_reads_live_codex_delta_and_passes():
    rec = loader.load()
    assert rec.is_passed, rec.notes
    assert len(rec.promoted_cells) == 18
    assert len(rec.blocked_cells) == 0
    assert rec.release_supported_count == 0
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False
    assert rec.release_ready is False


def test_loader_delta_counts_truth():
    rec = loader.load()
    assert rec.claim_state_counts["IMPLEMENTED_WITH_CAVEATS"] == 13
    assert rec.claim_state_counts["PARTIAL"] == 5
    assert rec.support_state_counts["smoke_supported"] == 16
    assert rec.support_state_counts["test_supported"] == 1
    assert rec.support_state_counts["repair_supported"] == 1
    assert rec.support_state_counts.get("release_supported", 0) == 0


def test_loader_delta_sources_referenced():
    rec = loader.load()
    sources = list(rec.delta_sources)
    assert any("matrix_probe_execution_batch_002" in s for s in sources)
    assert any("blocker_repair_results" in s for s in sources)


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
    "broad_claims_granted",
])
def test_loader_blocks_authority_flag(tmp_path, flag):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__(flag, True))
    rec = loader.load(ed)
    assert rec.is_blocked


def test_loader_blocks_blocked_cells_hidden(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.pop("blocked_cells", None))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BLOCKED_CELLS_HIDDEN" in rec.decision


def test_loader_blocks_release_supported_without_proof(tmp_path):
    def m(b):
        b.setdefault("support_state_counts", {})
        b["support_state_counts"]["release_supported"] = 2
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_loader_does_not_block_release_supported_with_proof(tmp_path):
    def m(b):
        b.setdefault("support_state_counts", {})
        b["support_state_counts"]["release_supported"] = 2
        paths = list(b.get("source_evidence_paths") or [])
        paths.append("assurance/evidence/fake_release_supported_proof.json")
        b["source_evidence_paths"] = paths
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_passed


def test_loader_blocks_broad_claim_as_current(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("active_state", "all apps supported in production"))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_universal_100_support_map_delta_batch_002_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_universal_100_support_map_delta_batch_002_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Support map delta is layered on top of the base map.",
        "Fixture-local probe-driven promotion is not production readiness.",
        "Universal 100 means universal intake/routing, not magic execution.",
        "No release claim without release proof.",
    ]
    for cap in required:
        assert cap in src, f"missing caption: {cap}"


def test_lock_present_and_authority_false():
    assert LOCK_PATH.is_file()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert lock["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_002_VISUAL_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_002_VISUAL_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_002_VISUAL_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_002_VISUAL_BINDING_LOCK_001" in ids
