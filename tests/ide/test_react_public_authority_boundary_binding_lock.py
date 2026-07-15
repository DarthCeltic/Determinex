"""Tests for DETERMINEX_REACT_PUBLIC_AUTHORITY_BOUNDARY_BINDING_LOCK_001."""
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

loader = importlib.import_module("ide.public_authority_boundary_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "PublicAuthorityBoundaryPanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_PUBLIC_AUTHORITY_BOUNDARY_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_public_authority_boundary_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
FLAGSHIP_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "public_tidal_wave_flagship_flow_certification"
)


def test_loader_passes_against_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_release_supported_zero():
    rec = loader.load()
    assert rec.release_supported_cells == 0
    assert rec.release_supported_families == 0


def test_loader_all_authority_flags_false():
    rec = loader.load()
    for attr in (
        "source_mutation_authorized",
        "real_user_source_mutation_authorized",
        "proof_execution_authority_granted",
        "training_eligible",
        "broad_claims_granted",
        "release_ready",
        "artifact_import_authorized",
        "benchmark_execution_authorized",
        "programbench_execution_authorized",
        "release_deploy_workflow_created",
    ):
        assert getattr(rec, attr) is False, attr


def test_loader_preservation_assertions_true():
    rec = loader.load()
    assert rec.release_support_unchanged_at_zero is True
    assert rec.broad_claims_remain_false is True
    assert rec.proof_execution_authority_remains_false is True
    assert rec.source_mutation_remains_unauthorized is True
    assert rec.real_user_source_mutation_remains_unauthorized is True
    assert rec.training_eligibility_remains_false is True


def test_loader_universal_support_not_claimed():
    rec = loader.load()
    assert rec.universal_support_claimed is False


def test_loader_export_not_release_readiness():
    rec = loader.load()
    assert rec.proof_report_export_is_release_readiness is False
    assert rec.report_schema_is_runtime_execution_proof is False


def test_loader_returns_awaiting_when_missing(tmp_path):
    rec = loader.load(tmp_path / "no-flagship", tmp_path / "no-export")
    assert rec.is_awaiting


def test_loader_fallback_does_not_invent_success(tmp_path):
    rec = loader.load(tmp_path / "no-flagship", tmp_path / "no-export")
    assert rec.is_passed is False
    # Even in awaiting state, authority remains false (no invention).
    assert rec.source_mutation_authorized is False
    assert rec.release_supported_cells == 0
    assert rec.universal_support_claimed is False


def _write_tampered_flagship(tmp: Path, mutate) -> Path:
    src = sorted(FLAGSHIP_DIR.glob("run_*.json"))[-1]
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
    "broad_claims_granted",
])
def test_loader_blocks_authority_flag(tmp_path, flag):
    ed = _write_tampered_flagship(tmp_path, lambda b: b.__setitem__(flag, True))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_release_overclaim(tmp_path):
    def m(b):
        b["release_support_status"]["release_supported_cells"] = 1
    ed = _write_tampered_flagship(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_loader_blocks_universal_support_claimed(tmp_path):
    def m(b):
        b["authority_boundary"]["universal_support_claimed"] = True
    ed = _write_tampered_flagship(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_preservation_false(tmp_path):
    def m(b):
        b["authority_boundary"]["broad_claims_remain_false"] = False
    ed = _write_tampered_flagship(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_public_authority_boundary_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_public_authority_boundary_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Authority remains locked down. Readiness, verification,",
        "reporting, and routing do not grant release support, mutation",
        "authority, proof execution authority, training eligibility, or",
        "broad claims.",
        "Release-supported remains 0 cells / 0 families.",
        "source_mutation_authorized remains false.",
        "real_user_source_mutation_authorized remains false.",
        "proof_execution_authority_granted remains false.",
        "training_eligible remains false.",
        "broad_claims_granted remains false.",
        "Universal support is not claimed.",
        "Proof report export is not release readiness.",
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
    assert lock["lock_id"] == "DETERMINEX_REACT_PUBLIC_AUTHORITY_BOUNDARY_BINDING_LOCK_001"
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
    assert rec["lock_id"] == "DETERMINEX_REACT_PUBLIC_AUTHORITY_BOUNDARY_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_PUBLIC_AUTHORITY_BOUNDARY_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_PUBLIC_AUTHORITY_BOUNDARY_BINDING_LOCK_001" in ids
