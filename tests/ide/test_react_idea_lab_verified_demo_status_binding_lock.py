"""Tests for DETERMINEX_REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_LOCK_001."""
from __future__ import annotations

import importlib
import json
import sys
import tempfile
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

loader = importlib.import_module("ide.idea_lab_verified_demo_status")
loader_rec = importlib.import_module("ide.idea_lab_verified_demo_status_record")
bcs = importlib.import_module("ide.backend_command_surface")
td = importlib.import_module("ide._tauri_driver")

PANEL_PATH = _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell" / "IdeaLabVerifiedDemoStatus.tsx"
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = _REPO_ROOT / "locks" / "sentinel" / "DETERMINEX_REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json"
EVIDENCE_DIR = _REPO_ROOT / "assurance" / "evidence" / "determinex_react_idea_lab_verified_demo_status_binding"
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"


# ---------------------------------------------------------------------------
# Loader against the live Codex evidence
# ---------------------------------------------------------------------------
def test_loader_reads_live_codex_evidence_and_passes():
    rec = loader.load()
    assert rec.is_passed, rec.notes
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False
    assert rec.target_app_class == "CLI/file-data tool"
    assert rec.target_language == "Python"
    assert rec.tests_passed is True
    assert rec.smoke_passed is True
    assert rec.verified_working_local_app is True


def test_loader_returns_awaiting_when_evidence_missing(tmp_path):
    rec = loader.load(tmp_path / "no-such-dir")
    assert rec.is_awaiting
    assert "awaiting" in rec.demo_title.lower()
    assert rec.tests_passed is False
    assert rec.smoke_passed is False
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False


# ---------------------------------------------------------------------------
# Loader refuses authority leaks / broad claims
# ---------------------------------------------------------------------------
def _write_tampered(tmp: Path, mutate) -> Path:
    """Write a copy of the live evidence file with mutate(blob) applied."""
    src_dir = (
        _REPO_ROOT / "assurance" / "evidence"
        / "idea_lab_python_cli_verified_splash_demo"
    )
    src = sorted(src_dir.glob("run_*.json"))[-1]
    blob = json.loads(src.read_text(encoding="utf-8"))
    mutate(blob)
    out = tmp / "run_99999999.tampered.json"
    out.write_text(json.dumps(blob), encoding="utf-8")
    return tmp


def test_loader_blocks_when_source_mutation_authorized_true(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("source_mutation_authorized", True),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert rec.decision == (
        "REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_AUTHORITY_CONFUSION"
    )


def test_loader_blocks_when_training_eligible_true(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("training_eligible", True),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert rec.decision == (
        "REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_AUTHORITY_CONFUSION"
    )


def test_loader_blocks_when_approval_authority_granted_true(tmp_path):
    def m(b):
        b.setdefault("authority", {})
        b["authority"]["approval_authority_granted"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_claim_boundary_missing_required(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__(
            "claim_boundary",
            ["Python CLI/file-data demo only"],  # drops other required statements
        ),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert rec.decision == (
        "REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_BROAD_CLAIM"
    )


def test_loader_blocks_when_evidence_carries_affirmative_broad_claim(tmp_path):
    """If evidence body contains an affirmative 'all apps' claim
    OUTSIDE the blocked_path_demo subsection, the loader refuses."""
    def m(b):
        b["loose_marketing_string"] = "Determinex supports all apps in any language."
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_verified_label_without_tests_or_smoke(tmp_path):
    def m(b):
        v = b.setdefault("verification", {})
        v["verified_working_local_app"] = True
        v["tests_passed"] = False
        v["smoke_passed"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


# ---------------------------------------------------------------------------
# Backend command surface routing
# ---------------------------------------------------------------------------
def test_command_registered_in_unified_set():
    assert "get_idea_lab_verified_demo_status" in bcs.commands()
    assert "get_idea_lab_verified_demo_status" in (
        bcs.UNIFIED_PRODUCT_READ_ONLY_COMMANDS
    )


def test_command_returns_ok_with_no_authority_leak():
    surface = bcs.IDEBackendCommandSurface()
    r = surface.call("get_idea_lab_verified_demo_status")
    assert r.status == "IDE_COMMAND_OK"
    assert r.source_mutation_authorized is False
    assert r.training_eligible is False
    assert r.payload.get("decision", "").startswith(
        "REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_"
    )


def test_tauri_driver_routes_command():
    res = td._dispatch("get_idea_lab_verified_demo_status", {})
    assert res["status"] == "TAURI_COMMAND_OK"
    assert res["source_mutation_authorized"] is False
    assert res["training_eligible"] is False


# ---------------------------------------------------------------------------
# React component static-content
# ---------------------------------------------------------------------------
def _src() -> str:
    return PANEL_PATH.read_text(encoding="utf-8")


def test_react_component_file_exists():
    assert PANEL_PATH.is_file()


def test_react_component_invokes_only_the_read_only_command():
    src = _src()
    assert "invokeUnifiedProductCommand(" in src
    assert '"get_idea_lab_verified_demo_status"' in src
    for forbidden in (
        "apply_source", "approve_packet", "write_training_row",
        "release_workflow", "run_programbench",
    ):
        assert forbidden not in src


def test_react_component_renders_required_sections():
    src = _src()
    for tid in (
        "idea-lab-verified-demo-status",
        "idea-lab-verified-demo-status-demo-title",
        "idea-lab-verified-demo-status-app-class",
        "idea-lab-verified-demo-status-target-language",
        "idea-lab-verified-demo-status-tests-passed",
        "idea-lab-verified-demo-status-smoke-passed",
        "idea-lab-verified-demo-status-verified-label",
        "idea-lab-verified-demo-status-evidence-ref",
        "idea-lab-verified-demo-status-training-eligibility",
        "idea-lab-verified-demo-status-claim-boundary",
        "idea-lab-verified-demo-status-scoped-only-caption",
    ):
        assert f'data-testid="{tid}"' in src, tid


def test_react_component_surfaces_awaiting_banner():
    src = _src()
    assert 'data-testid="idea-lab-verified-demo-status-awaiting-banner"' in src
    assert "Awaiting Codex reconciliation" in src


def test_react_component_surfaces_blocked_banner():
    src = _src()
    assert 'data-testid="idea-lab-verified-demo-status-blocked-banner"' in src


def test_react_component_training_badge_is_false():
    src = _src()
    assert 'data-training-eligible="false"' in src
    assert "training_eligible: false" in src


def test_react_component_verified_label_says_fixture_only():
    src = _src()
    assert "verified ONLY for this fixture demo path" in src


def test_react_component_scoped_caption_present():
    src = _src()
    assert "not all apps" in src
    assert "not all languages" in src
    assert "not production-ready arbitrary app creation" in src


def test_react_component_does_not_carry_forbidden_phrases():
    src = _src().lower()
    forbidden = (
        "production-ready in any repo",
        "training enabled by default",
        "release ready: true",
        "no follow-up required",
        "all codebases supported",
    )
    for f in forbidden:
        assert f not in src, f


def test_api_lib_lists_new_command():
    src = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_idea_lab_verified_demo_status"' in src


# ---------------------------------------------------------------------------
# Lock / evidence / index
# ---------------------------------------------------------------------------
def test_lock_manifest_exists_and_validates():
    assert LOCK_PATH.is_file()
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert blob["lock_id"] == "DETERMINEX_REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_LOCK_001"
    sd = blob["scope_discipline"]
    assert sd["source_mutation_authorized"] is False
    assert sd["training_eligible"] is False


def test_evidence_artifact_present():
    candidates = sorted(EVIDENCE_DIR.glob("run_*.json"))
    assert candidates


def test_evidence_index_entry_present():
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    assert "DETERMINEX_REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_LOCK_001" in ids


def test_status_tokens_exact():
    assert set(loader.IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_STATUS_TOKENS) == {
        "REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_PASSED",
        "REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_AWAITING_EVIDENCE",
        "REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_BROAD_CLAIM",
        "REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_AUTHORITY_CONFUSION",
    }
