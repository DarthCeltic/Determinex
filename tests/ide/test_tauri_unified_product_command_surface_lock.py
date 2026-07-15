"""Tests for DETERMINEX_TAURI_UNIFIED_PRODUCT_COMMAND_SURFACE_LOCK_001."""
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

bcs = importlib.import_module("ide.backend_command_surface")
td = importlib.import_module("ide._tauri_driver")

LOCK_PATH = _REPO_ROOT / "locks" / "sentinel" / (
    "DETERMINEX_TAURI_UNIFIED_PRODUCT_COMMAND_SURFACE_LOCK_001.json"
)
EVIDENCE_DIR = _REPO_ROOT / "assurance" / "evidence" / (
    "determinex_tauri_unified_product_command_surface"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"


REQUIRED_COMMANDS = (
    "get_unified_product_navigation_model",
    "get_idea_lab_workflow_state",
    "get_repo_clinic_workflow_state",
    "get_maintenance_bay_workflow_state",
    "get_learning_studio_workflow_state",
    "get_proof_operator_center_state",
    "get_user_level_teaching_windows",
    "get_unified_splash_demo_spec",
    # DETERMINEX_REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_LOCK_001 (rung 2
    # of DETERMINEX_LIVE_REACT_PRODUCT_SHELL_DEMO_READINESS_SERIES) added the
    # 9th read-only command. Each handler still emits IDE_COMMAND_OK with
    # source_mutation_authorized=False and training_eligible=False.
    "get_idea_lab_verified_demo_status",
    # DETERMINEX_REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_LOCK_001 added
    # the 10th read-only command. Same invariants.
    "get_repo_clinic_verified_demo_status",
    # DETERMINEX_REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_LOCK_001
    # added the 11th read-only command. Same invariants.
    "get_maintenance_bay_verified_demo_status",
    # DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001
    # added the 12th read-only command. Teaching outputs are
    # non-authorizing by construction; same all-False invariants.
    "get_learning_studio_verified_demo_status",
    # DETERMINEX_REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_LOCK_001
    # added the 13th read-only command. The dashboard DISPLAYS
    # authority; it does not grant authority. Same all-False
    # invariants, plus release_ready / proof_execution_authority /
    # broad_claims all remain False.
    "get_proof_operator_center_milestone_dashboard_status",
)


# ---------------------------------------------------------------------------
# Surface inventory
# ---------------------------------------------------------------------------
def test_required_commands_registered():
    cs = bcs.commands()
    for cmd in REQUIRED_COMMANDS:
        assert cmd in cs, f"missing command {cmd!r}"


def test_read_only_set_matches_required():
    assert bcs.UNIFIED_PRODUCT_READ_ONLY_COMMANDS == frozenset(REQUIRED_COMMANDS)


def test_no_new_mutating_commands():
    """The new commands surface MUST NOT include any verb whose
    name implies mutation (apply, write, train, approve, run)."""
    forbidden_substrings = (
        "apply_source", "write_training", "train_", "approve_packet",
        "run_programbench", "import_artifact", "scan_artifact",
        "grant", "release", "deploy",
    )
    for cmd in REQUIRED_COMMANDS:
        for sub in forbidden_substrings:
            assert sub not in cmd, f"forbidden substring {sub!r} in {cmd!r}"


def test_no_new_command_authorizes_anything():
    surface = bcs.IDEBackendCommandSurface()
    for cmd in REQUIRED_COMMANDS:
        r = surface.call(cmd)
        assert r.source_mutation_authorized is False, cmd
        assert r.training_eligible is False, cmd
        assert r.status == "IDE_COMMAND_OK", f"{cmd}: status={r.status!r}"


def test_command_name_matches_returned_payload_subject():
    """Each command must return a payload whose contents are about
    the named subject — i.e., command name matches behavior."""
    surface = bcs.IDEBackendCommandSurface()

    nav = surface.call("get_unified_product_navigation_model")
    assert "surfaces" in nav.payload or "shared_authority_vocabulary" in nav.payload

    idea = surface.call("get_idea_lab_workflow_state")
    assert "flow_steps" in idea.payload
    assert "ui_states" in idea.payload

    rc = surface.call("get_repo_clinic_workflow_state")
    assert "flow_steps" in rc.payload
    assert rc.payload.get("verifier_required") is True
    assert rc.payload.get("diagnosis_is_not_authorization") is True

    mb = surface.call("get_maintenance_bay_workflow_state")
    assert "maintenance_types" in mb.payload
    assert mb.payload.get("compatibility_verifier_required") is True

    ls = surface.call("get_learning_studio_workflow_state")
    assert "modes" in ls.payload
    assert ls.payload.get("non_authorizing") is True

    poc = surface.call("get_proof_operator_center_state")
    assert "required_sections" in poc.payload
    assert poc.payload.get("read_only_surface") is True

    ul = surface.call("get_user_level_teaching_windows")
    assert "user_levels" in ul.payload
    assert ul.payload.get("power_user_does_not_loosen_gates") is True

    sd = surface.call("get_unified_splash_demo_spec")
    assert sd.payload.get("required_tagline") == "Proof Before Mutation"
    assert "required_phrases" in sd.payload
    assert "required_negative_caveats" in sd.payload


def test_payloads_carry_negative_authority_flags():
    surface = bcs.IDEBackendCommandSurface()
    for cmd in REQUIRED_COMMANDS:
        r = surface.call(cmd)
        # The payload should explicitly declare source_mutation_authorized
        # False and training_eligible False (either directly or via a
        # nested view-model dict).
        blob = json.dumps(r.payload)
        assert '"source_mutation_authorized": false' in blob or (
            '"source_mutation_authorized": False' in blob
        ), cmd
        assert '"training_eligible": false' in blob or (
            '"training_eligible": False' in blob
        ), cmd


# ---------------------------------------------------------------------------
# Tauri driver routing
# ---------------------------------------------------------------------------
def test_tauri_driver_routes_each_new_command():
    for cmd in REQUIRED_COMMANDS:
        res = td._dispatch(cmd, {})
        assert res["command"] == cmd
        assert res["status"] == "TAURI_COMMAND_OK"
        assert res["source_mutation_authorized"] is False
        assert res["training_eligible"] is False


def test_tauri_driver_refuses_unknown_unified_command():
    res = td._dispatch("get_pretend_admin_command", {})
    assert res["status"] == "TAURI_COMMAND_BLOCKED_UNKNOWN"


def test_tauri_driver_did_not_remove_existing_commands():
    """Sanity: prior Tauri commands still route."""
    for prior in (
        "open_workspace", "get_workspace_status",
        "get_model_route_status", "diagnose_dry_run",
        "verify_temp_patch", "get_human_approval_packet",
        "source_apply_dry_run", "get_repair_flow_state",
    ):
        res = td._dispatch(prior, {})
        assert res["status"] != "TAURI_COMMAND_BLOCKED_UNKNOWN", (
            f"existing command {prior!r} accidentally removed"
        )


# ---------------------------------------------------------------------------
# Lock / evidence / index
# ---------------------------------------------------------------------------
def test_lock_manifest_exists_and_validates():
    assert LOCK_PATH.is_file()
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert blob["lock_id"] == "DETERMINEX_TAURI_UNIFIED_PRODUCT_COMMAND_SURFACE_LOCK_001"
    sd = blob["scope_discipline"]
    assert sd["source_mutation_authorized"] is False
    assert sd["training_eligible"] is False


def test_evidence_artifact_present():
    candidates = sorted(EVIDENCE_DIR.glob("run_*.json"))
    assert candidates


def test_evidence_index_entry_present():
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    assert "DETERMINEX_TAURI_UNIFIED_PRODUCT_COMMAND_SURFACE_LOCK_001" in ids
