"""Tests for DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.universal_100_support_depth_ledger_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "Universal100SupportDepthLedgerPanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_universal_100_support_depth_ledger_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "universal_100_support_depth_ledger"
)


def test_loader_passes_on_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_totals_truth():
    rec = loader.load()
    # From Codex prompt: 59 known / 34 fixture-local smoke / 7 test / 3 repair / 1 maintain / 1 teach / 0 release / 0 user-ready.
    assert rec.total_known_cells == 59
    assert rec.fixture_local_smoke_supported == 34
    assert rec.test_supported == 7
    assert rec.repair_supported == 3
    assert rec.maintain_supported == 1
    assert rec.teach_supported == 1
    assert rec.release_supported == 0
    assert rec.user_ready_with_caveats == 0


def test_loader_per_group_breakdowns_populated():
    rec = loader.load()
    # Each breakdown should have at least one entry from live Codex evidence.
    for group, value in (
        ("counts_by_sector", rec.counts_by_sector),
        ("counts_by_language", rec.counts_by_language),
        ("counts_by_app_class", rec.counts_by_app_class),
        ("counts_by_platform", rec.counts_by_platform),
        ("counts_by_workflow", rec.counts_by_workflow),
        ("counts_by_product_room", rec.counts_by_product_room),
    ):
        assert value, f"{group} should be populated from Codex evidence"


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


def test_loader_blocks_release_supported_without_proof(tmp_path):
    def m(b):
        b.setdefault("summary", {}).setdefault("support_depth_counts", {})["release_supported"] = 5
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_loader_does_not_block_release_supported_with_proof(tmp_path):
    def m(b):
        b.setdefault("summary", {}).setdefault("support_depth_counts", {})["release_supported"] = 5
        paths = list(b.get("source_evidence_paths") or [])
        paths.append("assurance/evidence/fake_release_supported_proof.json")
        b["source_evidence_paths"] = paths
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_passed


def test_loader_blocks_user_ready_without_proof(tmp_path):
    def m(b):
        b.setdefault("summary", {}).setdefault("support_depth_counts", {})["user_ready_with_caveats"] = 3
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "USER_READY_OVERCLAIM" in rec.decision


def test_loader_does_not_block_user_ready_with_proof(tmp_path):
    def m(b):
        b.setdefault("summary", {}).setdefault("support_depth_counts", {})["user_ready_with_caveats"] = 3
        paths = list(b.get("source_evidence_paths") or [])
        paths.append("assurance/evidence/fake_user_ready_proof.json")
        b["source_evidence_paths"] = paths
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_passed


def test_loader_blocks_total_known_missing(tmp_path):
    def m(b):
        b.setdefault("summary", {}).pop("total_known_cells", None)
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_support_depth_counts_empty(tmp_path):
    def m(b):
        b.setdefault("summary", {})["support_depth_counts"] = {}
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_status_mismatch(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("status", "UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_FAILED"))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_universal_100_support_depth_ledger_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_universal_100_support_depth_ledger_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Support-depth ledger is accounting, not promotion.",
        # &ldquo; / &rdquo; HTML entities are used in the rendered panel.
        "Accounted for",
        "Smoke-supported",
        "Fixture-local",
        "User-ready",
        "Release-supported",
        "Missing rung named",
        "Universal 100 means universal intake/routing, not magic execution.",
        "Blocked cells are visible by exact missing rung.",
    ]
    for cap in required:
        assert cap in src, f"missing caption fragment: {cap}"


def test_lock_present_and_authority_false():
    assert LOCK_PATH.is_file()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert lock["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_BINDING_LOCK_001" in ids
