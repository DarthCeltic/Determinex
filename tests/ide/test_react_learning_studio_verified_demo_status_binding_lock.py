"""Tests for DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001."""
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

loader = importlib.import_module("ide.learning_studio_verified_demo_status")
loader_rec = importlib.import_module(
    "ide.learning_studio_verified_demo_status_record"
)
bcs = importlib.import_module("ide.backend_command_surface")
td = importlib.import_module("ide._tauri_driver")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "LearningStudioVerifiedDemoStatus.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_learning_studio_verified_demo_status_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"

CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "learning_studio_teaching_splash_demo"
)


# ---------------------------------------------------------------------------
# Loader against the live Codex evidence
# ---------------------------------------------------------------------------
def test_loader_reads_live_codex_evidence_and_passes():
    rec = loader.load()
    assert rec.is_passed, rec.notes
    assert rec.target_surface == "Learning Studio"
    assert "non-authorizing" in rec.target_workflow.lower()
    assert rec.teaching_subject
    assert rec.beginner_explanation_written is True
    assert rec.pro_explanation_written is True
    assert rec.failure_explanation_written is True
    assert rec.safe_next_steps_written is True
    assert rec.what_this_does_not_prove_written is True
    assert rec.verifier_grounding_present is True
    assert rec.non_authorizing_teaching_only is True
    assert rec.source_mutation_authorized is False
    assert rec.approval_authority_granted is False
    assert rec.training_eligible is False
    assert rec.training_rows_written is False
    assert rec.release_ready is False
    assert rec.broad_claims_granted is False
    assert rec.real_user_source_mutation_authorized is False
    # Source evidence + report references.
    assert len(rec.source_evidence_paths) == 2
    assert any(
        "repo_clinic_fixture_repair_splash_demo" in p
        for p in rec.source_evidence_paths
    )
    assert any(
        "maintenance_bay_dry_run_update_splash_demo" in p
        for p in rec.source_evidence_paths
    )
    assert rec.final_report_path.endswith("FINAL_TEACHING_REPORT.md")
    assert rec.evidence_manifest_path.endswith("manifest.json")
    assert "Repo Clinic" in rec.repo_clinic_source_summary.get("surface", "")
    assert (
        "Maintenance Bay"
        in rec.maintenance_bay_source_summary.get("surface", "")
    )


def test_loader_returns_awaiting_when_evidence_missing(tmp_path):
    rec = loader.load(tmp_path / "no-such-dir")
    assert rec.is_awaiting
    assert rec.non_authorizing_teaching_only is True
    assert rec.beginner_explanation_written is False
    assert rec.pro_explanation_written is False
    assert rec.failure_explanation_written is False
    assert rec.verifier_grounding_present is False
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False


def test_loader_status_tokens_exact():
    assert set(loader.LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_STATUS_TOKENS) == {
        "REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_PASSED",
        "REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_AWAITING_EVIDENCE",
        "REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_BROAD_CLAIM",
        "REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_AUTHORITY_CONFUSION",
        "REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_MALFORMED",
    }


# ---------------------------------------------------------------------------
# Authority leak / broad-claim refusals
# ---------------------------------------------------------------------------
def _write_tampered(tmp: Path, mutate) -> Path:
    src = sorted(CODEX_EVIDENCE_DIR.glob("run_*.json"))[-1]
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
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_training_eligible_true(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("training_eligible", True),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_training_rows_written_true(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("training_rows_written", True),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_approval_authority_granted_true(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("approval_authority_granted", True),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_release_ready_true(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("release_ready", True),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_real_user_source_mutation_authorized_in_authority(tmp_path):
    def m(b):
        b.setdefault("authority", {})
        b["authority"]["real_user_source_mutation_authorized"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_authority_source_mutation_authorized(tmp_path):
    def m(b):
        b.setdefault("authority", {})
        b["authority"]["source_mutation_authorized"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_broad_claims_granted(tmp_path):
    def m(b):
        b.setdefault("authority", {})
        b["authority"]["broad_claims_granted"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_when_non_authorizing_teaching_only_false(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("non_authorizing_teaching_only", False),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_learning_success_label_allowed_true(tmp_path):
    def m(b):
        b.setdefault("verification", {}).setdefault("learning_success_label", {})
        b["verification"]["learning_success_label"]["success_label_allowed"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_when_beginner_explanation_missing(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("beginner_explanation_written", False),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_when_pro_explanation_missing(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("pro_explanation_written", False),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_when_failure_explanation_missing(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("failure_explanation_written", False),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_when_safe_next_steps_missing(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("safe_next_steps_written", False),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_when_what_this_does_not_prove_missing(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("what_this_does_not_prove_written", False),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_when_verifier_grounding_missing(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("verifier_grounding_present", False),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_when_claim_boundary_missing_required(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__(
            "claim_boundary",
            ["Learning Studio explanation only"],
        ),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_when_evidence_carries_affirmative_broad_claim(tmp_path):
    def m(b):
        b["loose_marketing_string"] = (
            "Learning Studio teaches all projects in any language for all users."
        )
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_arbitrary_teaching_claim_inserted(tmp_path):
    def m(b):
        b["overclaim_string"] = "Learning Studio supports arbitrary teaching."
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_autonomous_repair_phrase(tmp_path):
    def m(b):
        b["overclaim_string"] = "Learning Studio enables autonomous repair."
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


# ---------------------------------------------------------------------------
# Malformed / non-passing evidence
# ---------------------------------------------------------------------------
def test_loader_blocks_when_status_not_passed(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__(
            "status", "LEARNING_STUDIO_TEACHING_SPLASH_DEMO_BLOCKED_BROAD_CLAIM",
        ),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_returns_awaiting_when_evidence_corrupt(tmp_path):
    p = tmp_path / "run_99999999.corrupt.json"
    p.write_text("{not valid json}", encoding="utf-8")
    rec = loader.load(tmp_path)
    assert rec.is_awaiting


# ---------------------------------------------------------------------------
# Backend command surface routing
# ---------------------------------------------------------------------------
def test_command_registered_in_unified_set():
    assert "get_learning_studio_verified_demo_status" in bcs.commands()
    assert "get_learning_studio_verified_demo_status" in (
        bcs.UNIFIED_PRODUCT_READ_ONLY_COMMANDS
    )


def test_command_returns_ok_with_no_authority_leak():
    surface = bcs.IDEBackendCommandSurface()
    r = surface.call("get_learning_studio_verified_demo_status")
    assert r.status == "IDE_COMMAND_OK"
    assert r.source_mutation_authorized is False
    assert r.training_eligible is False
    assert r.payload.get("decision", "").startswith(
        "REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_"
    )
    assert r.payload.get("non_authorizing_teaching_only") is True
    assert r.payload.get("approval_authority_granted") is False
    assert r.payload.get("release_ready") is False
    assert r.payload.get("training_rows_written") is False


def test_tauri_driver_routes_command():
    res = td._dispatch("get_learning_studio_verified_demo_status", {})
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
    assert '"get_learning_studio_verified_demo_status"' in src
    for forbidden in (
        "apply_source", "approve_packet", "write_training_row",
        "release_workflow", "run_programbench", "import_artifact",
        "scan_artifact",
    ):
        assert forbidden not in src


def test_react_component_renders_required_sections():
    src = _src()
    for tid in (
        "learning-studio-verified-demo-status",
        "learning-studio-verified-demo-status-decision",
        "learning-studio-verified-demo-status-target-surface",
        "learning-studio-verified-demo-status-target-workflow",
        "learning-studio-verified-demo-status-teaching-subject",
        "learning-studio-verified-demo-status-beginner-written",
        "learning-studio-verified-demo-status-pro-written",
        "learning-studio-verified-demo-status-failure-written",
        "learning-studio-verified-demo-status-verifier-grounding",
        "learning-studio-verified-demo-status-safe-next-steps-written",
        "learning-studio-verified-demo-status-does-not-prove-written",
        "learning-studio-verified-demo-status-non-authorizing",
        "learning-studio-verified-demo-status-source-mutation",
        "learning-studio-verified-demo-status-approval-authority",
        "learning-studio-verified-demo-status-training-eligibility",
        "learning-studio-verified-demo-status-release-ready",
        "learning-studio-verified-demo-status-broad-claims",
        "learning-studio-verified-demo-status-evidence-ref",
        "learning-studio-verified-demo-status-final-report",
        "learning-studio-verified-demo-status-manifest",
        "learning-studio-verified-demo-status-source-evidence",
        "learning-studio-verified-demo-status-explanations",
        "learning-studio-verified-demo-status-beginner-text",
        "learning-studio-verified-demo-status-pro-text",
        "learning-studio-verified-demo-status-what-failed-text",
        "learning-studio-verified-demo-status-why-worked-text",
        "learning-studio-verified-demo-status-safe-next-steps-text",
        "learning-studio-verified-demo-status-does-not-prove-text",
        "learning-studio-verified-demo-status-claim-boundary",
        "learning-studio-verified-demo-status-blocked-path-summary",
        "learning-studio-verified-demo-status-scoped-only-caption",
        "learning-studio-verified-demo-status-learning-explains-only-caption",
        "learning-studio-verified-demo-status-source-mutation-false-caption",
        "learning-studio-verified-demo-status-approval-false-caption",
        "learning-studio-verified-demo-status-training-false-caption",
        "learning-studio-verified-demo-status-release-false-caption",
        "learning-studio-verified-demo-status-no-broad-claim-caption",
        "learning-studio-verified-demo-status-grounded-caption",
    ):
        assert f'data-testid="{tid}"' in src, tid


def test_react_component_surfaces_awaiting_banner():
    src = _src()
    assert 'data-testid="learning-studio-verified-demo-status-awaiting-banner"' in src
    assert "Awaiting Codex reconciliation" in src


def test_react_component_surfaces_blocked_banner():
    src = _src()
    assert 'data-testid="learning-studio-verified-demo-status-blocked-banner"' in src


def test_react_component_training_badge_is_false():
    src = _src()
    assert 'data-training-eligible="false"' in src
    assert "training_eligible: false" in src
    assert "training_rows_written: false" in src


def test_react_component_release_ready_marked_false():
    src = _src()
    assert 'data-release-ready="false"' in src
    assert "release_ready: false (remains false)" in src


def test_react_component_non_authorizing_marker_present():
    src = _src()
    assert 'data-non-authorizing={nonAuthorizing}' in src
    assert "Non-authorizing teaching only" in src


def test_react_component_source_mutation_marked_false():
    src = _src()
    assert "source_mutation_authorized: false (remains false)" in src
    assert "Source mutation remains false." in src


def test_react_component_approval_marked_false():
    src = _src()
    assert "approval_authority_granted: false (remains false)" in src
    assert "Approval authority remains false." in src


def test_react_component_required_captions_present():
    """All 9 required captions appear verbatim."""
    src = _src()
    assert "Learning can explain; it cannot mutate code." in src
    assert "Verified only for this Learning Studio teaching splash path." in src
    assert "Source mutation remains false." in src
    assert "Approval authority remains false." in src
    assert "Training stays false." in src
    assert "Release readiness remains false." in src
    assert (
        "No all-projects, all-languages, all-users, arbitrary-teaching, "
        "production-ready, or autonomous-repair claim is granted."
    ) in src
    assert (
        "Teaching explanations are grounded in existing verifier evidence, "
        "not new authorization."
    ) in src
    assert "READY_DOES_NOT_MEAN_AUTHORIZED" in src


def test_react_component_does_not_carry_forbidden_phrases():
    """The component MUST NOT carry affirmative forbidden phrases
    outside of the captions explicitly negating them."""
    src = _src().lower()
    forbidden_affirmative = (
        "all projects supported",
        "any language supported",
        "all codebases supported",
        "all users supported",
        "production-ready in any repo",
        "training enabled by default",
        "release ready: true",
        "real user repo mutation authorized",
        "arbitrary production repair",
        "no follow-up required",
        "deploy now",
        "source_mutation_authorized: true",
        "training_eligible: true",
        "approval_authority_granted: true",
    )
    for f in forbidden_affirmative:
        assert f not in src, f


def test_api_lib_lists_new_command():
    src = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_learning_studio_verified_demo_status"' in src


# ---------------------------------------------------------------------------
# Authority / training stay false invariants
# ---------------------------------------------------------------------------
def test_authority_training_release_stay_false_throughout():
    """Loader, command surface, and Tauri response ALL declare
    source_mutation, training, approval, release, broad_claims are
    False at every observed code path."""
    rec = loader.load()
    assert rec.source_mutation_authorized is False
    assert rec.approval_authority_granted is False
    assert rec.training_eligible is False
    assert rec.training_rows_written is False
    assert rec.release_ready is False
    assert rec.broad_claims_granted is False
    assert rec.real_user_source_mutation_authorized is False

    surface = bcs.IDEBackendCommandSurface()
    r = surface.call("get_learning_studio_verified_demo_status")
    assert r.source_mutation_authorized is False
    assert r.training_eligible is False
    assert r.payload.get("source_mutation_authorized") is False
    assert r.payload.get("approval_authority_granted") is False
    assert r.payload.get("training_eligible") is False
    assert r.payload.get("training_rows_written") is False
    assert r.payload.get("release_ready") is False
    assert r.payload.get("broad_claims_granted") is False

    res = td._dispatch("get_learning_studio_verified_demo_status", {})
    assert res["source_mutation_authorized"] is False
    assert res["training_eligible"] is False


def test_teaching_does_not_imply_mutation_or_authorization():
    """The PASSED record must NEVER imply authorization. Even at
    PASSED the authority bag stays all-False, and the
    non_authorizing_teaching_only flag stays True."""
    rec = loader.load()
    assert rec.is_passed
    assert rec.non_authorizing_teaching_only is True
    assert rec.source_mutation_authorized is False
    assert rec.approval_authority_granted is False
    assert rec.training_eligible is False
    assert rec.release_ready is False


# ---------------------------------------------------------------------------
# Existing Idea Lab, Repo Clinic, and Maintenance Bay bindings remain green
# ---------------------------------------------------------------------------
def test_idea_lab_binding_still_passes():
    idea_loader = importlib.import_module("ide.idea_lab_verified_demo_status")
    rec = idea_loader.load()
    assert rec.is_passed, rec.notes


def test_idea_lab_tauri_dispatch_still_passes():
    res = td._dispatch("get_idea_lab_verified_demo_status", {})
    assert res["status"] == "TAURI_COMMAND_OK"


def test_repo_clinic_binding_still_passes():
    repo_loader = importlib.import_module("ide.repo_clinic_verified_demo_status")
    rec = repo_loader.load()
    assert rec.is_passed, rec.notes


def test_repo_clinic_tauri_dispatch_still_passes():
    res = td._dispatch("get_repo_clinic_verified_demo_status", {})
    assert res["status"] == "TAURI_COMMAND_OK"


def test_maintenance_bay_binding_still_passes():
    mb_loader = importlib.import_module(
        "ide.maintenance_bay_verified_demo_status"
    )
    rec = mb_loader.load()
    assert rec.is_passed, rec.notes


def test_maintenance_bay_tauri_dispatch_still_passes():
    res = td._dispatch("get_maintenance_bay_verified_demo_status", {})
    assert res["status"] == "TAURI_COMMAND_OK"


# ---------------------------------------------------------------------------
# Lock / evidence / index
# ---------------------------------------------------------------------------
def test_lock_manifest_exists_and_validates():
    assert LOCK_PATH.is_file()
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert blob["lock_id"] == (
        "DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001"
    )
    sd = blob["scope_discipline"]
    assert sd["source_mutation_authorized"] is False
    assert sd["training_eligible"] is False
    assert sd["release_ready"] is False
    assert sd["approval_authority_granted"] is False
    assert sd["broad_claims_granted"] is False
    assert sd["non_authorizing_teaching_only"] is True


def test_evidence_artifact_present():
    candidates = sorted(EVIDENCE_DIR.glob("run_*.json"))
    assert candidates


def test_evidence_index_entry_present():
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    assert (
        "DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001"
        in ids
    )
