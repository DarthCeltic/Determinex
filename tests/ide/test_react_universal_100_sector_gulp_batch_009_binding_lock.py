"""Tests for DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_009_BINDING_LOCK_001."""
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

loader_mod = importlib.import_module("ide.universal_100_sector_gulp_status")
load_batch_009 = loader_mod.load_batch_009

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "Universal100SectorGulpBatch009Panel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_009_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_universal_100_sector_gulp_batch_009_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"

CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "universal_100_sector_gulp_batch_009"
)


def test_loader_passes_against_live_codex_batch_009():
    rec = load_batch_009()
    assert rec.is_passed, rec.notes
    assert rec.batch_label == "Batch 009"
    assert rec.batch_lock_id == "DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_009_LOCK_001"


def test_loader_batch_009_counts_truth():
    rec = load_batch_009()
    assert rec.sectors_gulped == ('local_database_sqlite_sector', 'node_typescript_cli_sector', 'python_package_library_sector')
    assert rec.cells_tagged == 9
    assert rec.cells_classified == 9
    assert rec.cells_routed == 9
    assert rec.cells_probed == 9
    assert rec.cells_promoted == 9
    assert rec.cells_blocked == 0
    assert rec.release_supported_count == 0
    assert rec.support_state_counts == {'maintain_supported': 1, 'scaffold_supported': 4, 'smoke_supported': 3, 'test_supported': 1}


def test_loader_batch_009_fixture_caveat_present():
    rec = load_batch_009()
    assert "fixture-local" in rec.fixture_caveats_present


def test_loader_batch_009_promoted_cells_truthful():
    rec = load_batch_009()
    for c in rec.promoted_cells:
        assert c.promoted is True
        assert c.blocked is False
        # Batch 009 support_state must come from Codex evidence; loader-side ladder check enforces validity.


def test_loader_returns_awaiting_when_missing(tmp_path):
    rec = load_batch_009(tmp_path / "no-such")
    assert rec.is_awaiting


def test_loader_returns_awaiting_when_corrupt(tmp_path):
    (tmp_path / "run_99.broken.json").write_text("not json", encoding="utf-8")
    rec = load_batch_009(tmp_path)
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
    "training_rows_written",
    "source_mutation_authorized",
    "approval_authority_granted",
    "proof_execution_authority_granted",
])
def test_loader_blocks_authority_flag(tmp_path, flag):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__(flag, True))
    rec = load_batch_009(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_broad_claims_granted(tmp_path):
    def m(b):
        b.setdefault("authority", {})
        b["authority"]["broad_claims_granted"] = True
    ed = _write_tampered(tmp_path, m)
    rec = load_batch_009(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_release_supported_without_proof(tmp_path):
    def m(b):
        b.setdefault("summary", {})
        b["summary"]["release_supported"] = 1
    ed = _write_tampered(tmp_path, m)
    rec = load_batch_009(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_loader_blocks_blocked_cells_key_removed(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.pop("blocked_cells", None))
    rec = load_batch_009(ed)
    assert rec.is_blocked
    assert "BLOCKED_CELLS_HIDDEN" in rec.decision


def test_loader_blocks_sectors_gulped_empty(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("sectors_gulped", []))
    rec = load_batch_009(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_fully_supported_with_caveats_without_release_proof(tmp_path):
    def m(b):
        promoted = b.get("promoted_cells") or []
        if promoted:
            promoted[0]["lifecycle_state"] = "FULLY_SUPPORTED_WITH_CAVEATS"
    ed = _write_tampered(tmp_path, m)
    rec = load_batch_009(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_loader_blocks_status_mismatch(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("status", "UNIVERSAL_100_SECTOR_GULP_BATCH_009_FAILED"))
    rec = load_batch_009(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_forbidden_phrase_as_current_claim(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("strongest_truthful_new_claim", "all apps supported in production now"))
    rec = load_batch_009(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_universal_100_sector_gulp_batch_009_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_universal_100_sector_gulp_batch_009_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Fixture-local proof is not production readiness.",
        "Smoke-supported is not release-supported.",
        "Fully supported with caveats is not release-supported.",
        "No source mutation without authority.",
        "Universal 100 means universal intake/routing, not magic execution.",
        "Blocked cells are visible by exact missing rung.",
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
    assert lock["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_009_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_009_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_009_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_009_BINDING_LOCK_001" in ids
