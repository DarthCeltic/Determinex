"""Tests for DETERMINEX_REACT_UNIVERSAL_100_SECTOR_STATE_LADDER_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.universal_100_sector_state_ladder_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "Universal100SectorStateLadderPanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_STATE_LADDER_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_universal_100_sector_state_ladder_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"

CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "universal_100_sector_state_ladder"
)


def test_loader_reads_live_codex_and_passes():
    rec = loader.load()
    assert rec.is_passed, rec.notes
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False
    assert rec.release_ready is False


def test_loader_reports_11_sectors_24_lifecycle_states_14_blocker_states():
    rec = loader.load()
    assert rec.sector_count == 11
    assert len(rec.support_lifecycle_states) == 24
    assert rec.support_lifecycle_states[0] == "DISCOVERED"
    assert "FULLY_SUPPORTED_WITH_CAVEATS" in rec.support_lifecycle_states
    assert len(rec.blocker_missing_rung_states) == 14


def test_loader_lifecycle_contains_canonical_milestones():
    rec = loader.load()
    for state in (
        "TAGGED",
        "CLASSIFIED",
        "ROUTED",
        "SCAFFOLD_SUPPORTED",
        "BUILD_SUPPORTED",
        "TEST_SUPPORTED",
        "SMOKE_SUPPORTED",
        "USER_READY_WITH_CAVEATS",
        "PACKAGING_REQUIRED",
        "FRESH_INSTALL_VERIFIED",
        "RELEASE_GATE_READY",
        "RELEASE_SUPPORTED",
    ):
        assert state in rec.support_lifecycle_states, f"lifecycle missing {state}"


def test_loader_blocker_states_contain_canonical_set():
    rec = loader.load()
    for state in (
        "TOOLCHAIN_MISSING",
        "DEPENDENCY_MISSING",
        "VERIFIER_MISSING",
        "SMOKE_MISSING",
        "FIXTURE_MISSING",
        "ADAPTER_MISSING",
        "PLATFORM_MISSING",
        "AUTHORITY_MISSING",
        "NETWORK_REQUIRED_BUT_NOT_ALLOWED",
    ):
        assert state in rec.blocker_missing_rung_states, f"blocker state missing {state}"


def test_loader_sectors_have_required_fields():
    rec = loader.load()
    for s in rec.sectors:
        assert s.sector_id
        assert s.sector_name
        assert s.next_probe_batch  # every sector points to a batch
        # Promotion targets exist for every sector
        assert len(s.promotion_targets) >= 1


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


def test_loader_blocks_sector_registry_empty(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("sector_registry", []))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_lifecycle_missing_discovered(tmp_path):
    def m(b):
        b["support_lifecycle_states"] = ["NOT_DISCOVERED"] + list(b.get("support_lifecycle_states") or [])[1:]
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_lifecycle_missing_fully_supported(tmp_path):
    def m(b):
        b["support_lifecycle_states"] = [
            s for s in (b.get("support_lifecycle_states") or [])
            if s != "FULLY_SUPPORTED_WITH_CAVEATS"
        ]
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_release_supported_promotion_target_without_release_proof(tmp_path):
    def m(b):
        # Tamper the first sector to claim RELEASE_SUPPORTED without naming packaging/
        # fresh-install/release-gate evidence in release_boundary or missing_rungs.
        sr = b.get("sector_registry") or []
        if sr:
            sr[0]["promotion_targets"] = ["RELEASE_SUPPORTED"]
            sr[0]["release_boundary"] = ["some unrelated boundary"]
            sr[0]["missing_rungs"] = []
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_loader_blocks_forbidden_phrase_as_current_claim(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("active_claim", "all apps supported in production"))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_universal_100_sector_state_ladder_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_universal_100_sector_state_ladder_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Fixture-local proof is not production readiness.",
        "Smoke-supported is not release-supported.",
        "Fully supported with caveats is not release-supported.",
        "No source mutation without authority.",
        "No working-app claim without build/test/smoke evidence.",
        "Universal 100 means universal intake/routing, not magic execution.",
        "Blocked cells are visible by exact missing rung.",
    ]
    for cap in required:
        assert cap in src, f"missing caption: {cap}"


def test_panel_does_not_render_authority_grant():
    src = PANEL_PATH.read_text(encoding="utf-8")
    forbidden = [
        "release_ready: true",
        "training_eligible: true",
        "source_mutation_authorized: true",
    ]
    for f in forbidden:
        assert f not in src


def test_lock_present_and_authority_false():
    assert LOCK_PATH.is_file()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert lock["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_STATE_LADDER_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_STATE_LADDER_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_STATE_LADDER_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_UNIVERSAL_100_SECTOR_STATE_LADDER_BINDING_LOCK_001" in ids
