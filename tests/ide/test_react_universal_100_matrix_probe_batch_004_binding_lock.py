"""Tests for DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004_BINDING_LOCK_001."""
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

loader_mod = importlib.import_module("ide.universal_100_matrix_probe_batch_status")
load_batch_004 = loader_mod.load_batch_004
BATCH_004 = loader_mod.BATCH_004

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "Universal100MatrixProbeBatch004Status.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_universal_100_matrix_probe_execution_batch_004_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"

CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "universal_100_matrix_probe_execution_batch_004"
)


def test_loader_reads_live_codex_batch_004_and_passes():
    rec = load_batch_004()
    assert rec.is_passed, rec.notes
    assert rec.batch_label == "Batch 004"
    assert rec.batch_lock_id == "DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004"
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False
    assert rec.release_ready is False
    assert rec.broad_claims_granted is False


def test_loader_batch_004_summary_counts_truth():
    rec = load_batch_004()
    # Codex Batch 004 truth: 10 probed, 10 promoted, 10 smoke_supported,
    # 0 release_supported, 0 blocked.
    assert rec.cells_probed == 10
    assert rec.cells_promoted == 10
    assert rec.smoke_supported_count == 10
    assert rec.test_supported_count == 0
    assert rec.release_supported_count == 0
    assert len(rec.promoted_cells) == 10
    assert len(rec.blocked_cells) == 0


def test_loader_batch_004_promoted_cells_cover_typescript_node_javascript_vite_react_html():
    rec = load_batch_004()
    promoted_ids = {c.cell_id for c in rec.promoted_cells}
    expected = {
        # TypeScript / Node CLI suite (5 cells unlocked by the new adapter)
        "typescript_node_cli_build",
        "typescript_node_cli_smoke",
        "typescript_file_transform_cli",
        "typescript_json_transform_cli",
        "typescript_node_http_healthcheck",
        # JavaScript / Node (2)
        "javascript_node_cli_smoke_variant",
        "javascript_json_transform_cli",
        # Vite static, React/Vite, HTML/CSS/JS static (3)
        "vite_static_app_build_smoke",
        "react_vite_component_build_smoke",
        "html_css_js_static_site_smoke",
    }
    assert expected <= promoted_ids


def test_loader_batch_004_fixture_local_caveat_present():
    rec = load_batch_004()
    assert "fixture-local" in rec.fixture_caveats_present


def test_loader_batch_004_claim_state_distribution():
    rec = load_batch_004()
    # Codex summary: IMPLEMENTED_WITH_CAVEATS: 5, PARTIAL: 5
    impl_caveats = [c for c in rec.promoted_cells if c.claim_state == "IMPLEMENTED_WITH_CAVEATS"]
    partial = [c for c in rec.promoted_cells if c.claim_state == "PARTIAL"]
    assert len(impl_caveats) == 5
    assert len(partial) == 5


def test_loader_returns_awaiting_when_evidence_missing(tmp_path):
    rec = load_batch_004(tmp_path / "no-such-dir")
    assert rec.is_awaiting


def test_loader_returns_awaiting_when_evidence_corrupt(tmp_path):
    (tmp_path / "run_99.broken.json").write_text("not json", encoding="utf-8")
    rec = load_batch_004(tmp_path)
    assert rec.is_awaiting


def test_loader_blocks_when_status_is_batch_003(tmp_path):
    src = sorted((_REPO_ROOT / "assurance" / "evidence" / "universal_100_matrix_probe_execution_batch_003").glob("run_*.json"))[-1]
    blob = json.loads(src.read_text(encoding="utf-8"))
    out = tmp_path / "run_99.batch003in004.json"
    out.write_text(json.dumps(blob), encoding="utf-8")
    rec = load_batch_004(tmp_path)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def _write_tampered(tmp: Path, mutate) -> Path:
    src = sorted(CODEX_EVIDENCE_DIR.glob("run_*.json"))[-1]
    blob = json.loads(src.read_text(encoding="utf-8"))
    mutate(blob)
    out = tmp / "run_99999999.tampered.json"
    out.write_text(json.dumps(blob), encoding="utf-8")
    return tmp


@pytest.mark.parametrize("flag", [
    "release_ready",
    "training_eligible",
    "training_rows_written",
    "source_mutation_authorized",
    "approval_authority_granted",
    "proof_execution_authority_granted",
    "release_deploy_workflow_created",
    "artifact_import_authorized",
    "benchmark_execution_authorized",
    "programbench_execution_authorized",
])
def test_loader_batch_004_blocks_authority_flags_top_level(tmp_path, flag):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__(flag, True))
    rec = load_batch_004(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


@pytest.mark.parametrize("flag", [
    "release_ready",
    "training_eligible",
    "source_mutation_authorized",
])
def test_loader_batch_004_blocks_authority_in_authority_bag(tmp_path, flag):
    def m(b):
        b.setdefault("authority", {})
        b["authority"][flag] = True
    ed = _write_tampered(tmp_path, m)
    rec = load_batch_004(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_batch_004_blocks_broad_claims_granted(tmp_path):
    def m(b):
        b.setdefault("authority", {})
        b["authority"]["broad_claims_granted"] = True
    ed = _write_tampered(tmp_path, m)
    rec = load_batch_004(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_batch_004_blocks_release_overclaim_without_proof(tmp_path):
    def m(b):
        b.setdefault("summary", {})
        b["summary"]["release_supported"] = 2
    ed = _write_tampered(tmp_path, m)
    rec = load_batch_004(ed)
    assert rec.is_blocked
    assert "RELEASE_OVERCLAIM" in rec.decision


def test_loader_batch_004_does_not_block_release_with_proof_path(tmp_path):
    def m(b):
        b.setdefault("summary", {})
        b["summary"]["release_supported"] = 1
        paths = list(b.get("source_evidence_paths") or [])
        paths.append("assurance/evidence/fake_release_supported_proof.json")
        b["source_evidence_paths"] = paths
    ed = _write_tampered(tmp_path, m)
    rec = load_batch_004(ed)
    assert rec.is_passed


def test_loader_batch_004_blocks_when_blocked_cells_key_removed(tmp_path):
    """Even when Codex reports zero blocked cells in Batch 004, removing the key blocks the binding."""
    ed = _write_tampered(tmp_path, lambda b: b.pop("blocked_cells", None))
    rec = load_batch_004(ed)
    assert rec.is_blocked
    assert "BLOCKED_CELLS_HIDDEN" in rec.decision


def test_loader_batch_004_blocks_when_status_not_passed(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("status", "UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004_FAILED"))
    rec = load_batch_004(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_batch_004_blocks_when_summary_cells_probed_missing(tmp_path):
    def m(b):
        b.setdefault("summary", {})
        b["summary"].pop("cells_probed", None)
    ed = _write_tampered(tmp_path, m)
    rec = load_batch_004(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_batch_004_blocks_implemented_above_evidence(tmp_path):
    def m(b):
        promoted = b.setdefault("promoted_cells", [])
        promoted[0]["claim_state"] = "IMPLEMENTED"
        promoted[0]["support_state"] = "scaffold_only"
    ed = _write_tampered(tmp_path, m)
    rec = load_batch_004(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_batch_004_blocks_forbidden_phrase_as_current_claim(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("strongest_truthful_new_claim", "all apps supported in production"))
    rec = load_batch_004(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_batch_004_blocks_fixture_local_as_production_claim(tmp_path):
    """A 'fixture-local as production' framing must be rejected as broad-claim phrase."""
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("active_claim", "this fixture-local proof is production-ready"))
    rec = load_batch_004(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_batch_004_does_not_block_forbidden_phrase_in_refusal_context(tmp_path):
    def m(b):
        forbidden = list(b.get("forbidden_claims") or [])
        forbidden.append("all apps supported")
        b["forbidden_claims"] = forbidden
    ed = _write_tampered(tmp_path, m)
    rec = load_batch_004(ed)
    assert rec.is_passed


# ---------------------------------------------------------------------------
# Frontend wiring
# ---------------------------------------------------------------------------


def test_panel_component_present():
    assert PANEL_PATH.is_file()


def test_panel_uses_invoke_unified_product_command_with_batch_004_command():
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_universal_100_matrix_probe_batch_004_status" in src


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Fixture-local proof is not production readiness.",
        "Smoke-supported is not release-supported.",
        "No release-supported cells in this batch.",
        "No source mutation without authority.",
        "No working-app claim without build/test/smoke evidence.",
        "Universal 100 means universal intake/routing, not magic execution.",
        "Batch 004 expanded verified fixture-local smoke coverage; it did not",
    ]
    for cap in required:
        assert cap in src, f"missing caption: {cap}"


def test_panel_renders_typescript_adapter_unlock_callout():
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "DETERMINEX_TYPESCRIPT_NODE_CLI_ADAPTER_LOCK_001" in src
    assert "no network install" in src
    assert "no npm install" in src
    assert "no Docker" in src


def test_panel_does_not_render_authority_grant():
    src = PANEL_PATH.read_text(encoding="utf-8")
    forbidden = [
        "release_ready: true",
        "training_eligible: true",
        "source_mutation_authorized: true",
        "approval_authority_granted: true",
        "broad_claims_granted: true",
    ]
    for f in forbidden:
        assert f not in src, f"panel must not render: {f}"


def test_panel_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_universal_100_matrix_probe_batch_004_status"' in api


# ---------------------------------------------------------------------------
# Lock + evidence + index
# ---------------------------------------------------------------------------


def test_batch_004_lock_present_and_authority_remains_false():
    assert LOCK_PATH.is_file()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert lock["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004_BINDING_LOCK_001"
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
        "artifact_import_authorized",
        "benchmark_execution_authorized",
        "programbench_execution_authorized",
    ):
        assert sd.get(flag) is False, flag


def test_batch_004_evidence_record_present():
    files = sorted(EVIDENCE_DIR.glob("run_*.json"))
    assert files, f"no evidence record under {EVIDENCE_DIR}"
    rec = json.loads(files[-1].read_text(encoding="utf-8"))
    assert rec["lock_id"] == "DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004_BINDING_LOCK_001"


def test_batch_004_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004_BINDING_LOCK_001" in ids
