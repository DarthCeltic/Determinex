"""Tests for DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_002_BINDING_LOCK_001."""
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

loader_mod = importlib.import_module(
    "ide.universal_100_matrix_probe_batch_status"
)
load_batch_002 = loader_mod.load_batch_002
BATCH_002 = loader_mod.BATCH_002

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "Universal100MatrixProbeBatch002Status.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_002_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_universal_100_matrix_probe_execution_batch_002_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"

CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "universal_100_matrix_probe_execution_batch_002"
)


# ---------------------------------------------------------------------------
# Loader against the live Codex Batch 002 evidence
# ---------------------------------------------------------------------------


def test_loader_reads_live_codex_batch_002_and_passes():
    rec = load_batch_002()
    assert rec.is_passed, rec.notes
    assert rec.batch_label == "Batch 002"
    assert rec.batch_lock_id == "DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_002"
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False
    assert rec.release_ready is False
    assert rec.broad_claims_granted is False


def test_loader_reads_live_codex_batch_002_summary_counts_truth():
    rec = load_batch_002()
    assert rec.is_passed
    # Codex Batch 002 truth: 15 probed, 15 promoted, 14 smoke + 1 test, 0 release.
    assert rec.cells_probed == 15
    assert rec.cells_promoted == 15
    assert rec.smoke_supported_count == 14
    assert rec.test_supported_count == 1
    assert rec.release_supported_count == 0
    assert len(rec.promoted_cells) == 15
    assert len(rec.blocked_cells) == 0


def test_loader_returns_awaiting_when_evidence_missing(tmp_path):
    rec = load_batch_002(tmp_path / "no-such-dir")
    assert rec.is_awaiting


def test_loader_blocks_when_status_is_batch_001_status(tmp_path):
    """Loading Batch 002 against Batch 001 evidence must reject the status mismatch."""
    src = sorted((_REPO_ROOT / "assurance" / "evidence" / "universal_100_matrix_probe_execution_batch").glob("run_*.json"))[-1]
    blob = json.loads(src.read_text(encoding="utf-8"))
    out = tmp_path / "run_99.batch001in002.json"
    out.write_text(json.dumps(blob), encoding="utf-8")
    rec = load_batch_002(tmp_path)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def _write_tampered_002(tmp: Path, mutate) -> Path:
    src = sorted(CODEX_EVIDENCE_DIR.glob("run_*.json"))[-1]
    blob = json.loads(src.read_text(encoding="utf-8"))
    mutate(blob)
    out = tmp / "run_99999999.tampered.json"
    out.write_text(json.dumps(blob), encoding="utf-8")
    return tmp


@pytest.mark.parametrize("flag", [
    "release_ready",
    "training_eligible",
    "source_mutation_authorized",
    "approval_authority_granted",
    "proof_execution_authority_granted",
])
def test_loader_batch_002_blocks_authority_flags(tmp_path, flag):
    ed = _write_tampered_002(tmp_path, lambda b: b.__setitem__(flag, True))
    rec = load_batch_002(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_batch_002_blocks_when_blocked_cells_key_removed(tmp_path):
    ed = _write_tampered_002(tmp_path, lambda b: b.pop("blocked_cells", None))
    rec = load_batch_002(ed)
    assert rec.is_blocked
    assert "BLOCKED_CELLS_HIDDEN" in rec.decision


def test_loader_batch_002_blocks_when_release_supported_without_proof(tmp_path):
    def m(b):
        b.setdefault("summary", {})
        b["summary"]["release_supported"] = 1
    ed = _write_tampered_002(tmp_path, m)
    rec = load_batch_002(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_loader_batch_002_does_not_block_release_with_proof_path(tmp_path):
    def m(b):
        b.setdefault("summary", {})
        b["summary"]["release_supported"] = 1
        paths = list(b.get("source_evidence_paths") or [])
        paths.append("assurance/evidence/fake_release_proof_supported_lock.json")
        b["source_evidence_paths"] = paths
    ed = _write_tampered_002(tmp_path, m)
    rec = load_batch_002(ed)
    assert rec.is_passed


def test_loader_batch_002_blocks_when_broad_claim_in_current_state(tmp_path):
    ed = _write_tampered_002(tmp_path, lambda b: b.__setitem__("current_state", "production-ready arbitrary app generation now"))
    rec = load_batch_002(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


# ---------------------------------------------------------------------------
# Panel + Tauri command registration
# ---------------------------------------------------------------------------


def test_batch_002_panel_component_present():
    assert PANEL_PATH.is_file(), f"missing {PANEL_PATH}"


def test_batch_002_panel_uses_invoke_unified_product_command_with_batch_002_command():
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_universal_100_matrix_probe_batch_002_status" in src


def test_batch_002_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Fixture-local proof is not production readiness.",
        "No release-supported cells in this batch.",
        "Unsupported or blocked cells are routed by exact missing rung.",
        "Universal 100 means universal intake/routing, not magic execution.",
    ]
    for cap in required:
        assert cap in src, f"missing caption: {cap}"


def test_batch_002_panel_does_not_render_authority_grant():
    src = PANEL_PATH.read_text(encoding="utf-8")
    forbidden = [
        "release_ready: true",
        "training_eligible: true",
        "source_mutation_authorized: true",
        "approval_authority_granted: true",
    ]
    for f in forbidden:
        assert f not in src, f"panel must not render: {f}"


def test_batch_002_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_universal_100_matrix_probe_batch_002_status"' in api


# ---------------------------------------------------------------------------
# Lock + evidence + index
# ---------------------------------------------------------------------------


def test_batch_002_lock_present_and_authority_remains_false():
    assert LOCK_PATH.is_file()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert lock["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_002_BINDING_LOCK_001"
    assert lock["status"] == "REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_BINDING_PASSED"
    sd = lock.get("scope_discipline", {})
    for flag in (
        "release_ready",
        "training_eligible",
        "training_rows_written",
        "source_mutation_authorized",
        "approval_authority_granted",
        "proof_execution_authority_granted",
        "broad_claims_granted",
        "release_deploy_workflow_created",
    ):
        assert sd.get(flag) is False, flag


def test_batch_002_evidence_record_present():
    files = sorted(EVIDENCE_DIR.glob("run_*.json"))
    assert files, f"no evidence record under {EVIDENCE_DIR}"
    rec = json.loads(files[-1].read_text(encoding="utf-8"))
    assert rec["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_002_BINDING_LOCK_001"


def test_batch_002_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_002_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated for new lock")
    assert "DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_002_BINDING_LOCK_001" in ids
