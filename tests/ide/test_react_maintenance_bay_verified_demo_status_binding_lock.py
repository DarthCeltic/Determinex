"""Tests for DETERMINEX_REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_LOCK_001."""
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

loader = importlib.import_module("ide.maintenance_bay_verified_demo_status")
loader_rec = importlib.import_module("ide.maintenance_bay_verified_demo_status_record")
bcs = importlib.import_module("ide.backend_command_surface")
td = importlib.import_module("ide._tauri_driver")

PANEL_PATH = _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell" / "MaintenanceBayVerifiedDemoStatus.tsx"
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = _REPO_ROOT / "locks" / "sentinel" / "DETERMINEX_REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json"
EVIDENCE_DIR = _REPO_ROOT / "assurance" / "evidence" / "determinex_react_maintenance_bay_verified_demo_status_binding"
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"

CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "maintenance_bay_dry_run_update_splash_demo"
)


# ---------------------------------------------------------------------------
# Loader against the live Codex evidence
# ---------------------------------------------------------------------------
def test_loader_reads_live_codex_evidence_and_passes():
    rec = loader.load()
    assert rec.is_passed, rec.notes
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False
    assert rec.training_rows_written is False
    assert rec.target_surface == "Maintenance Bay"
    assert rec.target_language == "Python"
    assert "dry-run test configuration" in rec.target_workflow
    assert rec.baseline_failed is True
    assert rec.compatibility_verified is True
    assert rec.post_change_tests_passed is True
    assert rec.false_updated_claim_blocked is True
    assert rec.false_maintained_claim_blocked is True
    assert rec.unsafe_real_repo_mutation_blocked is True
    assert rec.unsupported_all_projects_claim_blocked is True
    assert rec.training_eligibility_without_positive_gate_blocked is True
    assert rec.release_deploy_readiness_claim_blocked is True
    assert rec.fixture_mutation_only is True
    assert rec.real_user_source_mutation_authorized is False
    assert rec.affected_files == ("pyproject.toml", "README.md")
    assert rec.change_body_hash.startswith("de900433e6")


def test_loader_returns_awaiting_when_evidence_missing(tmp_path):
    rec = loader.load(tmp_path / "no-such-dir")
    assert rec.is_awaiting
    assert "awaiting" in rec.demo_title.lower()
    assert rec.baseline_failed is False
    assert rec.compatibility_verified is False
    assert rec.post_change_tests_passed is False
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False


def test_loader_status_tokens_exact():
    assert set(loader.MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_STATUS_TOKENS) == {
        "REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_PASSED",
        "REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_AWAITING_EVIDENCE",
        "REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_BROAD_CLAIM",
        "REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_AUTHORITY_CONFUSION",
        "REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_MALFORMED",
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


def test_loader_blocks_when_real_user_source_mutation_authorized_in_authority(tmp_path):
    def m(b):
        b.setdefault("authority", {})
        b["authority"]["real_user_source_mutation_authorized"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_top_level_real_user_source_mutation_authorized(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__("real_user_source_mutation_authorized", True),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_approval_authority_granted(tmp_path):
    def m(b):
        b.setdefault("authority", {})
        b["authority"]["approval_authority_granted"] = True
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


def test_loader_blocks_when_fixture_mutation_only_false(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("fixture_mutation_only", False),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_compatibility_verified_false(tmp_path):
    """Critical: without compatibility verifier evidence, the
    binding MUST NOT pass — that's the 'updated/maintained' label
    invariant."""
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("compatibility_verified", False),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_post_change_tests_passed_false(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("post_change_tests_passed", False),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_claim_boundary_missing_required(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__(
            "claim_boundary",
            ["Maintenance Bay Python fixture dry-run demo only"],
        ),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_when_evidence_carries_affirmative_broad_claim(tmp_path):
    def m(b):
        b["loose_marketing_string"] = "Determinex maintains all projects in any language."
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_arbitrary_maintenance_claim_inserted(tmp_path):
    def m(b):
        b["overclaim_string"] = "We do arbitrary maintenance on the fly."
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
            "status",
            "MAINTENANCE_BAY_DRY_RUN_UPDATE_SPLASH_DEMO_BLOCKED_COMPATIBILITY_FAILED",
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
    assert "get_maintenance_bay_verified_demo_status" in bcs.commands()
    assert "get_maintenance_bay_verified_demo_status" in (
        bcs.UNIFIED_PRODUCT_READ_ONLY_COMMANDS
    )


def test_command_returns_ok_with_no_authority_leak():
    surface = bcs.IDEBackendCommandSurface()
    r = surface.call("get_maintenance_bay_verified_demo_status")
    assert r.status == "IDE_COMMAND_OK"
    assert r.source_mutation_authorized is False
    assert r.training_eligible is False
    assert r.payload.get("decision", "").startswith(
        "REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_"
    )


def test_tauri_driver_routes_command():
    res = td._dispatch("get_maintenance_bay_verified_demo_status", {})
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
    assert '"get_maintenance_bay_verified_demo_status"' in src
    for forbidden in (
        "apply_source", "approve_packet", "write_training_row",
        "release_workflow", "run_programbench",
    ):
        assert forbidden not in src


def test_react_component_renders_required_sections():
    src = _src()
    for tid in (
        "maintenance-bay-verified-demo-status",
        "maintenance-bay-verified-demo-status-decision",
        "maintenance-bay-verified-demo-status-target-surface",
        "maintenance-bay-verified-demo-status-target-workflow",
        "maintenance-bay-verified-demo-status-target-language",
        "maintenance-bay-verified-demo-status-fixture-workspace",
        "maintenance-bay-verified-demo-status-issue-summary",
        "maintenance-bay-verified-demo-status-change-type",
        "maintenance-bay-verified-demo-status-baseline-verifier",
        "maintenance-bay-verified-demo-status-baseline-failed",
        "maintenance-bay-verified-demo-status-compatibility-verifier",
        "maintenance-bay-verified-demo-status-compatibility-verified",
        "maintenance-bay-verified-demo-status-post-change-tests-passed",
        "maintenance-bay-verified-demo-status-fixture-mutation-only",
        "maintenance-bay-verified-demo-status-real-user-source-mutation",
        "maintenance-bay-verified-demo-status-approval-authority",
        "maintenance-bay-verified-demo-status-training-eligibility",
        "maintenance-bay-verified-demo-status-affected-files",
        "maintenance-bay-verified-demo-status-evidence-ref",
        "maintenance-bay-verified-demo-status-change-body-hash",
        "maintenance-bay-verified-demo-status-compatibility-workspace",
        "maintenance-bay-verified-demo-status-source-repo-workspace",
        "maintenance-bay-verified-demo-status-updated-label",
        "maintenance-bay-verified-demo-status-updated-meaning",
        "maintenance-bay-verified-demo-status-blocked-claims",
        "maintenance-bay-verified-demo-status-claim-boundary",
        "maintenance-bay-verified-demo-status-blocked-path-summary",
        "maintenance-bay-verified-demo-status-scoped-only-caption",
        "maintenance-bay-verified-demo-status-no-real-user-repo-caption",
        "maintenance-bay-verified-demo-status-training-stays-false-caption",
        "maintenance-bay-verified-demo-status-no-broad-claim-caption",
    ):
        assert f'data-testid="{tid}"' in src, tid


def test_react_component_surfaces_awaiting_banner():
    src = _src()
    assert 'data-testid="maintenance-bay-verified-demo-status-awaiting-banner"' in src
    assert "Awaiting Codex reconciliation" in src


def test_react_component_surfaces_blocked_banner():
    src = _src()
    assert 'data-testid="maintenance-bay-verified-demo-status-blocked-banner"' in src


def test_react_component_training_badge_is_false():
    src = _src()
    assert 'data-training-eligible="false"' in src
    assert "training_eligible: false" in src
    assert "training_rows_written: false" in src


def test_react_component_real_user_source_mutation_marked_false():
    src = _src()
    assert "real_user_source_mutation_authorized: false (remains false)" in src
    assert 'data-testid="maintenance-bay-verified-demo-status-no-real-user-repo-caption"' in src
    assert "Real user repo mutation NOT authorized." in src


def test_react_component_updated_label_gated_on_compatibility_and_post_change():
    """Hard rule: the UPDATE_VERIFIED label only renders when passed
    AND compatibility_verified AND post_change_tests_passed."""
    src = _src()
    # Computed gate.
    compact = " ".join(src.split())
    assert "passed && compatibilityVerified && postChangeTestsPassed" in compact
    # Both the enabled and disabled labels are present.
    assert "UPDATE_VERIFIED" in src
    assert "UPDATED_LABEL_DISABLED_NO_VERIFIER_EVIDENCE" in src
    # Caption mentions the requirement.
    assert "compatibility verifier AND" in src
    assert "post-change verifier evidence" in src


def test_react_component_blocked_claims_section_lists_all_refusals():
    src = _src()
    for tid in (
        "maintenance-bay-verified-demo-status-false-updated-blocked",
        "maintenance-bay-verified-demo-status-false-maintained-blocked",
        "maintenance-bay-verified-demo-status-unsafe-mutation-blocked",
        "maintenance-bay-verified-demo-status-all-projects-claim-blocked",
        "maintenance-bay-verified-demo-status-training-without-gate-blocked",
        "maintenance-bay-verified-demo-status-release-deploy-blocked",
    ):
        assert f'data-testid="{tid}"' in src, tid


def test_react_component_required_captions_present():
    src = _src()
    assert "Verified only for this Maintenance Bay fixture dry-run/update path." in src
    assert "Real user repo mutation NOT authorized." in src
    assert "Training stays false." in src
    assert "No all-projects, all-languages, arbitrary-maintenance, production-ready maintenance, or release/deploy claim is granted." in src
    assert "READY_DOES_NOT_MEAN_AUTHORIZED" in src


def test_react_component_does_not_carry_forbidden_phrases():
    """The component MUST NOT carry affirmative forbidden phrases
    outside of the captions explicitly negating them."""
    src = _src().lower()
    # Affirmative claims must not appear outside negation captions.
    forbidden_affirmative = (
        "all projects supported",
        "any language supported",
        "all codebases supported",
        "production-ready in any repo",
        "training enabled by default",
        "release ready: true",
        "real user repo mutation authorized",
        "arbitrary production repair",
        "no follow-up required",
        "deploy now",
    )
    for f in forbidden_affirmative:
        assert f not in src, f


def test_api_lib_lists_new_command():
    src = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_maintenance_bay_verified_demo_status"' in src


# ---------------------------------------------------------------------------
# Authority / training stay false
# ---------------------------------------------------------------------------
def test_authority_training_stay_false_throughout():
    """Loader, command surface, and Tauri response ALL declare
    source_mutation_authorized=False, training_eligible=False, and
    training_rows_written=False on every code path tested above."""
    rec = loader.load()
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False
    assert rec.training_rows_written is False

    surface = bcs.IDEBackendCommandSurface()
    r = surface.call("get_maintenance_bay_verified_demo_status")
    assert r.source_mutation_authorized is False
    assert r.training_eligible is False
    assert r.payload.get("source_mutation_authorized") is False
    assert r.payload.get("training_eligible") is False
    assert r.payload.get("training_rows_written") is False

    res = td._dispatch("get_maintenance_bay_verified_demo_status", {})
    assert res["source_mutation_authorized"] is False
    assert res["training_eligible"] is False


# ---------------------------------------------------------------------------
# Existing Idea Lab and Repo Clinic bindings remain green
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


# ---------------------------------------------------------------------------
# Lock / evidence / index
# ---------------------------------------------------------------------------
def test_lock_manifest_exists_and_validates():
    assert LOCK_PATH.is_file()
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert blob["lock_id"] == "DETERMINEX_REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_LOCK_001"
    sd = blob["scope_discipline"]
    assert sd["source_mutation_authorized"] is False
    assert sd["training_eligible"] is False


def test_evidence_artifact_present():
    candidates = sorted(EVIDENCE_DIR.glob("run_*.json"))
    assert candidates


def test_evidence_index_entry_present():
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    assert "DETERMINEX_REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_LOCK_001" in ids
