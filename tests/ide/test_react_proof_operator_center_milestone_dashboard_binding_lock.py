"""Tests for DETERMINEX_REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_LOCK_001."""
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

loader = importlib.import_module(
    "ide.proof_operator_center_milestone_dashboard_status"
)
loader_rec = importlib.import_module(
    "ide.proof_operator_center_milestone_dashboard_status_record"
)
bcs = importlib.import_module("ide.backend_command_surface")
td = importlib.import_module("ide._tauri_driver")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "ProofOperatorCenterMilestoneDashboard.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_proof_operator_center_milestone_dashboard_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"

CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "proof_operator_center_milestone_dashboard"
)


# ---------------------------------------------------------------------------
# Loader against the live Codex evidence
# ---------------------------------------------------------------------------
def test_loader_reads_live_codex_evidence_and_passes():
    rec = loader.load()
    assert rec.is_passed, rec.notes
    assert rec.target_surface == "Proof / Operator Center"
    assert "milestone" in rec.target_workflow.lower()
    # Authority bag — all False.
    assert rec.source_mutation_authorized is False
    assert rec.approval_authority_granted is False
    assert rec.proof_execution_authority_granted is False
    assert rec.training_eligible is False
    assert rec.training_rows_written is False
    assert rec.release_ready is False
    assert rec.broad_claims_granted is False
    assert rec.artifact_import_authorized is False
    assert rec.benchmark_execution_authorized is False
    assert rec.programbench_execution_authorized is False
    assert rec.release_deploy_workflow_created is False
    # Five rooms present.
    assert len(rec.surfaces) == 5
    surface_names = {s.surface for s in rec.surfaces}
    assert "Idea Lab" in surface_names
    assert "Repo Clinic" in surface_names
    assert "Maintenance Bay" in surface_names
    assert "Learning Studio" in surface_names
    assert "Proof / Operator Center" in surface_names
    # Release gate status.
    assert rec.cathedral_index_status == "pending"
    assert rec.columbia_house_tracker_status == "pending_not_built"
    assert rec.public_claims_ledger_status
    assert rec.release_repo_scrub_status
    assert rec.fresh_install_demo_workflow_status
    assert rec.windows_first_support_matrix_status
    assert rec.release_ready_label == "release_ready: false (remains false)"
    # Scale-to-100.
    assert rec.scale_to_100_normalized_as_current_ct_lock is False
    assert rec.scale_to_100_claim_truth_status
    # Evidence health.
    assert rec.evidence_index_count == 310
    assert rec.count_drift_status == "EVIDENCE_COUNT_DRIFT_GUARD_PASSED"
    assert rec.count_drift_expected == 310
    assert rec.count_drift_actual == 310
    assert rec.append_only_ledger_chain_valid is True
    assert rec.evidence_index_valid is True
    # Roadmap lists.
    assert "Cathedral Index" in rec.roadmap_items
    assert "Columbia House Tracker" in rec.roadmap_items
    assert "Windows-first support matrix" in rec.roadmap_items


def test_loader_returns_awaiting_when_evidence_missing(tmp_path):
    rec = loader.load(tmp_path / "no-such-dir")
    assert rec.is_awaiting
    assert rec.release_ready is False
    assert rec.training_eligible is False
    assert rec.source_mutation_authorized is False
    assert rec.proof_execution_authority_granted is False
    assert len(rec.surfaces) == 0


def test_loader_status_tokens_exact():
    assert set(
        loader.REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_STATUS_TOKENS
    ) == {
        "REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_PASSED",
        "REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_AWAITING_EVIDENCE",
        "REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_BLOCKED_BROAD_CLAIM",
        "REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_BLOCKED_AUTHORITY_CONFUSION",
        "REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_BLOCKED_MALFORMED",
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


def test_loader_blocks_when_release_ready_true(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("release_ready", True))
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_training_eligible_true(tmp_path):
    ed = _write_tampered(tmp_path, lambda b: b.__setitem__("training_eligible", True))
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


def test_loader_blocks_when_source_mutation_authorized_true(tmp_path):
    ed = _write_tampered(
        tmp_path, lambda b: b.__setitem__("source_mutation_authorized", True),
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


def test_loader_blocks_when_proof_execution_authority_granted_true(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__("proof_execution_authority_granted", True),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_broad_claims_granted_true(tmp_path):
    def m(b):
        b.setdefault("authority_status", {})
        b["authority_status"]["broad_claims_granted"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_when_authority_status_release_ready_true(tmp_path):
    def m(b):
        b.setdefault("authority_status", {})
        b["authority_status"]["release_ready"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_release_gate_status_release_ready_true(tmp_path):
    def m(b):
        b.setdefault("release_gate_status", {})
        b["release_gate_status"]["release_ready"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_columbia_house_marked_built(tmp_path):
    def m(b):
        b.setdefault("release_gate_status", {})
        b["release_gate_status"]["columbia_house_tracker"] = "built"
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_when_columbia_house_marked_verified(tmp_path):
    def m(b):
        b.setdefault("release_gate_status", {})
        b["release_gate_status"]["columbia_house_tracker"] = "verified"
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_when_scale_to_100_normalized_as_current_ct_lock(tmp_path):
    def m(b):
        b.setdefault("scale_to_100_status", {})
        b["scale_to_100_status"]["normalized_as_current_ct_lock"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_when_proof_center_surface_pre_declared_react_bound(tmp_path):
    def m(b):
        for s in b.get("surface_statuses") or []:
            if isinstance(s, dict) and s.get("surface") == "Proof / Operator Center":
                s["react_bound"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_when_surface_missing(tmp_path):
    def m(b):
        b["surface_statuses"] = [
            s for s in (b.get("surface_statuses") or [])
            if not (isinstance(s, dict) and s.get("surface") == "Learning Studio")
        ]
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_when_count_drift_status_not_passed(tmp_path):
    def m(b):
        b.setdefault("evidence_health", {})
        b["evidence_health"]["count_drift_status"] = "EVIDENCE_COUNT_DRIFT_GUARD_BLOCKED_UNEXPLAINED_ADDITION"
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_when_append_only_ledger_chain_invalid(tmp_path):
    def m(b):
        b.setdefault("evidence_health", {})
        b["evidence_health"]["append_only_ledger_chain_valid"] = False
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_when_evidence_index_invalid(tmp_path):
    def m(b):
        b.setdefault("evidence_health", {})
        b["evidence_health"]["evidence_index_valid"] = False
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_blocks_when_claim_boundary_missing_required(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__(
            "claim_boundary",
            ["Proof / Operator Center milestone dashboard only"],
        ),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_when_evidence_carries_affirmative_broad_claim(tmp_path):
    def m(b):
        b["loose_marketing_string"] = (
            "Determinex supports all apps in any language across all platforms."
        )
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_production_ready_arbitrary_claim_inserted(tmp_path):
    def m(b):
        b["overclaim_string"] = (
            "Determinex is production-ready for arbitrary apps."
        )
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_autonomous_repair_phrase(tmp_path):
    def m(b):
        b["overclaim_string"] = "Determinex performs fully autonomous maintenance."
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_when_full_cathedral_marked_validated(tmp_path):
    def m(b):
        b["full_cathedral_status"] = "Full cathedral roadmap validated"
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
            "status", "PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BLOCKED_MALFORMED",
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
    assert "get_proof_operator_center_milestone_dashboard_status" in bcs.commands()
    assert "get_proof_operator_center_milestone_dashboard_status" in (
        bcs.UNIFIED_PRODUCT_READ_ONLY_COMMANDS
    )


def test_command_returns_ok_with_no_authority_leak():
    surface = bcs.IDEBackendCommandSurface()
    r = surface.call("get_proof_operator_center_milestone_dashboard_status")
    assert r.status == "IDE_COMMAND_OK"
    assert r.source_mutation_authorized is False
    assert r.training_eligible is False
    assert r.payload.get("decision", "").startswith(
        "REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_"
    )
    assert r.payload.get("release_ready") is False
    assert r.payload.get("proof_execution_authority_granted") is False
    assert r.payload.get("approval_authority_granted") is False
    assert r.payload.get("broad_claims_granted") is False
    assert r.payload.get("training_rows_written") is False


def test_tauri_driver_routes_command():
    res = td._dispatch(
        "get_proof_operator_center_milestone_dashboard_status", {},
    )
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
    assert '"get_proof_operator_center_milestone_dashboard_status"' in src
    for forbidden in (
        "apply_source", "approve_packet", "write_training_row",
        "release_workflow", "run_programbench", "import_artifact",
        "scan_artifact", "grant_proof_execution_authority",
    ):
        assert forbidden not in src


def test_react_component_renders_required_sections():
    src = _src()
    for tid in (
        "proof-operator-center-milestone-dashboard",
        "proof-operator-center-milestone-dashboard-five-rooms",
        "proof-operator-center-milestone-dashboard-authority-status",
        "proof-operator-center-milestone-dashboard-source-mutation",
        "proof-operator-center-milestone-dashboard-approval-authority",
        "proof-operator-center-milestone-dashboard-proof-execution-authority",
        "proof-operator-center-milestone-dashboard-training-eligibility",
        "proof-operator-center-milestone-dashboard-release-ready",
        "proof-operator-center-milestone-dashboard-broad-claims",
        "proof-operator-center-milestone-dashboard-release-gate-status",
        "proof-operator-center-milestone-dashboard-cathedral-index",
        "proof-operator-center-milestone-dashboard-columbia-house",
        "proof-operator-center-milestone-dashboard-public-claims-ledger",
        "proof-operator-center-milestone-dashboard-release-repo-scrub",
        "proof-operator-center-milestone-dashboard-fresh-install-demo",
        "proof-operator-center-milestone-dashboard-windows-first-support-matrix",
        "proof-operator-center-milestone-dashboard-scale-to-100",
        "proof-operator-center-milestone-dashboard-scale-to-100-claim-truth",
        "proof-operator-center-milestone-dashboard-scale-to-100-ct-lock",
        "proof-operator-center-milestone-dashboard-scale-to-100-windows-matrix",
        "proof-operator-center-milestone-dashboard-scale-to-100-corpus-training",
        "proof-operator-center-milestone-dashboard-scale-to-100-expansion-queue",
        "proof-operator-center-milestone-dashboard-scale-to-100-legacy-enterprise",
        "proof-operator-center-milestone-dashboard-scale-to-100-audit-path",
        "proof-operator-center-milestone-dashboard-evidence-health",
        "proof-operator-center-milestone-dashboard-evidence-index-count",
        "proof-operator-center-milestone-dashboard-append-only-ledger",
        "proof-operator-center-milestone-dashboard-count-drift",
        "proof-operator-center-milestone-dashboard-json-parse",
        "proof-operator-center-milestone-dashboard-evidence-ref",
        "proof-operator-center-milestone-dashboard-report-path",
        "proof-operator-center-milestone-dashboard-machine-readable",
        "proof-operator-center-milestone-dashboard-claim-boundary",
        "proof-operator-center-milestone-dashboard-forbidden-claims",
        "proof-operator-center-milestone-dashboard-blocked-path-summary",
        "proof-operator-center-milestone-dashboard-roadmap-items",
        "proof-operator-center-milestone-dashboard-next-rung",
        "proof-operator-center-milestone-dashboard-caveats-footer",
        # Captions.
        "proof-operator-center-milestone-dashboard-ready-does-not-mean-authorized",
        "proof-operator-center-milestone-dashboard-verified-rooms-not-universal-caption",
        "proof-operator-center-milestone-dashboard-displays-not-grants-caption",
        "proof-operator-center-milestone-dashboard-release-ready-false-caption",
        "proof-operator-center-milestone-dashboard-training-false-caption",
        "proof-operator-center-milestone-dashboard-source-mutation-false-caption",
        "proof-operator-center-milestone-dashboard-scale-to-100-not-ct-caption",
        "proof-operator-center-milestone-dashboard-columbia-house-pending-caption",
        "proof-operator-center-milestone-dashboard-full-cathedral-not-validated-caption",
    ):
        assert f'data-testid="{tid}"' in src, tid


def test_react_component_surfaces_awaiting_banner():
    src = _src()
    assert (
        'data-testid="proof-operator-center-milestone-dashboard-awaiting-banner"'
        in src
    )
    assert "Awaiting Codex reconciliation" in src


def test_react_component_surfaces_blocked_banner():
    src = _src()
    assert (
        'data-testid="proof-operator-center-milestone-dashboard-blocked-banner"'
        in src
    )


def test_react_component_root_has_negative_authority_data_attrs():
    src = _src()
    assert 'data-release-ready="false"' in src
    assert 'data-training-eligible="false"' in src
    assert 'data-proof-execution-authority-granted="false"' in src
    assert 'data-source-mutation-authorized="false"' in src
    assert 'data-approval-authority-granted="false"' in src
    assert 'data-broad-claims-granted="false"' in src


def test_react_component_five_room_status_renders():
    """Render once with an empty payload but check the slug template
    is present for each required slug."""
    src = _src()
    # Compose the slug suffix the component emits.
    for slug in ("idea-lab", "repo-clinic", "maintenance-bay",
                 "learning-studio", "proof-operator-center"):
        assert f"proof-operator-center-milestone-dashboard-surface-${{slug}}" in src
    # Container also present.
    assert 'data-testid="proof-operator-center-milestone-dashboard-five-rooms"' in src


def test_react_component_release_ready_marked_false():
    src = _src()
    assert "release_ready: false (remains false)" in src
    assert "Release ready remains false." in src


def test_react_component_training_marked_false():
    src = _src()
    assert "training_eligible: false (remains false)" in src
    assert "training_rows_written: 0 / false" in src
    assert "Training remains false." in src


def test_react_component_source_mutation_marked_false():
    src = _src()
    assert "source_mutation_authorized: false (remains false)" in src
    assert "Source mutation remains false." in src


def test_react_component_approval_authority_marked_false():
    src = _src()
    assert "approval_authority_granted: false (remains false)" in src


def test_react_component_proof_execution_authority_marked_false():
    src = _src()
    assert "proof_execution_authority_granted: false (remains false)" in src


def test_react_component_broad_claims_marked_false():
    src = _src()
    assert "broad_claims_granted: false (remains false)" in src


def test_react_component_columbia_house_marked_pending_not_built():
    src = _src()
    assert "not built" in src
    assert "Columbia House is pending, not built." in src


def test_react_component_scale_to_100_not_ct_lock_message():
    src = _src()
    assert "not current C&amp;T lock" in src
    assert "Scale-to-100 is roadmap/audit input, not current C&amp;T lock." in src
    assert "false (remains false — roadmap draft only)" in src


def test_react_component_full_cathedral_not_validated_caption():
    src = _src()
    assert "Full Cathedral roadmap is not validated by this binding." in src


def test_react_component_required_captions_present():
    """All 9 required captions appear verbatim."""
    src = _src()
    assert "Ready does NOT mean authorized" in src or "READY_DOES_NOT_MEAN_AUTHORIZED" in src
    assert "Verified rooms do NOT mean universal support." in src
    assert "Proof Center displays authority; it does not grant authority." in src
    assert "Release ready remains false." in src
    assert "Training remains false." in src
    assert "Source mutation remains false." in src
    assert "Scale-to-100 is roadmap/audit input, not current C&amp;T lock." in src
    assert "Columbia House is pending, not built." in src
    assert "Full Cathedral roadmap is not validated by this binding." in src
    assert "READY_DOES_NOT_MEAN_AUTHORIZED" in src


def test_react_component_does_not_carry_forbidden_phrases():
    """The component MUST NOT carry affirmative forbidden phrases
    outside of the captions explicitly negating them."""
    src = _src().lower()
    forbidden_affirmative = (
        "all apps supported",
        "any language supported",
        "all platforms supported",
        "all codebases supported",
        "production-ready arbitrary",
        "arbitrary app generation",
        "fully autonomous maintenance",
        "release ready: true",
        "release_ready: true",
        "training enabled",
        "training_eligible: true",
        "approval_authority_granted: true",
        "proof_execution_authority_granted: true",
        "broad_claims_granted: true",
        "columbia house tracker: built",
        "columbia house tracker: verified",
        "scale-to-100 lock active",
        "scale-to-100 is the current c&t lock",
        "full cathedral roadmap validated",
        "verified room means universal support",
    )
    for f in forbidden_affirmative:
        assert f not in src, f


def test_api_lib_lists_new_command():
    src = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_proof_operator_center_milestone_dashboard_status"' in src


# ---------------------------------------------------------------------------
# Authority invariants observed across loader / command surface / Tauri
# ---------------------------------------------------------------------------
def test_authority_training_release_stay_false_throughout():
    rec = loader.load()
    assert rec.source_mutation_authorized is False
    assert rec.approval_authority_granted is False
    assert rec.proof_execution_authority_granted is False
    assert rec.training_eligible is False
    assert rec.training_rows_written is False
    assert rec.release_ready is False
    assert rec.broad_claims_granted is False

    surface = bcs.IDEBackendCommandSurface()
    r = surface.call("get_proof_operator_center_milestone_dashboard_status")
    assert r.source_mutation_authorized is False
    assert r.training_eligible is False
    assert r.payload.get("release_ready") is False
    assert r.payload.get("proof_execution_authority_granted") is False
    assert r.payload.get("training_rows_written") is False
    assert r.payload.get("approval_authority_granted") is False
    assert r.payload.get("broad_claims_granted") is False

    res = td._dispatch("get_proof_operator_center_milestone_dashboard_status", {})
    assert res["source_mutation_authorized"] is False
    assert res["training_eligible"] is False


def test_dashboard_visibility_does_not_imply_authority():
    """Even at PASSED, no field implies mutation, approval,
    proof-execution authority, training, or release."""
    rec = loader.load()
    assert rec.is_passed
    assert rec.release_ready is False
    assert rec.proof_execution_authority_granted is False
    assert rec.approval_authority_granted is False
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False


# ---------------------------------------------------------------------------
# Existing four bindings remain green
# ---------------------------------------------------------------------------
def test_idea_lab_binding_still_passes():
    m = importlib.import_module("ide.idea_lab_verified_demo_status")
    assert m.load().is_passed


def test_idea_lab_tauri_dispatch_still_passes():
    res = td._dispatch("get_idea_lab_verified_demo_status", {})
    assert res["status"] == "TAURI_COMMAND_OK"


def test_repo_clinic_binding_still_passes():
    m = importlib.import_module("ide.repo_clinic_verified_demo_status")
    assert m.load().is_passed


def test_repo_clinic_tauri_dispatch_still_passes():
    res = td._dispatch("get_repo_clinic_verified_demo_status", {})
    assert res["status"] == "TAURI_COMMAND_OK"


def test_maintenance_bay_binding_still_passes():
    m = importlib.import_module("ide.maintenance_bay_verified_demo_status")
    assert m.load().is_passed


def test_maintenance_bay_tauri_dispatch_still_passes():
    res = td._dispatch("get_maintenance_bay_verified_demo_status", {})
    assert res["status"] == "TAURI_COMMAND_OK"


def test_learning_studio_binding_still_passes():
    m = importlib.import_module("ide.learning_studio_verified_demo_status")
    assert m.load().is_passed


def test_learning_studio_tauri_dispatch_still_passes():
    res = td._dispatch("get_learning_studio_verified_demo_status", {})
    assert res["status"] == "TAURI_COMMAND_OK"


# ---------------------------------------------------------------------------
# Lock / evidence / index
# ---------------------------------------------------------------------------
def test_lock_manifest_exists_and_validates():
    assert LOCK_PATH.is_file()
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert blob["lock_id"] == (
        "DETERMINEX_REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_LOCK_001"
    )
    sd = blob["scope_discipline"]
    assert sd["source_mutation_authorized"] is False
    assert sd["training_eligible"] is False
    assert sd["release_ready"] is False
    assert sd["approval_authority_granted"] is False
    assert sd["proof_execution_authority_granted"] is False
    assert sd["broad_claims_granted"] is False
    assert sd["scale_to_100_validated_as_ct_lock"] is False
    assert sd["full_cathedral_roadmap_validated"] is False
    assert sd["columbia_house_built"] is False


def test_evidence_artifact_present():
    candidates = sorted(EVIDENCE_DIR.glob("run_*.json"))
    assert candidates


def test_evidence_index_entry_present():
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    assert (
        "DETERMINEX_REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_LOCK_001"
        in ids
    )
