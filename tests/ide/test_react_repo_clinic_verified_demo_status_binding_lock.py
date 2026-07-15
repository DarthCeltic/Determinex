"""Tests for DETERMINEX_REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_LOCK_001."""
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

loader = importlib.import_module("ide.repo_clinic_verified_demo_status")
loader_rec = importlib.import_module("ide.repo_clinic_verified_demo_status_record")
bcs = importlib.import_module("ide.backend_command_surface")
td = importlib.import_module("ide._tauri_driver")

PANEL_PATH = _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell" / "RepoClinicVerifiedDemoStatus.tsx"
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = _REPO_ROOT / "locks" / "sentinel" / "DETERMINEX_REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json"
EVIDENCE_DIR = _REPO_ROOT / "assurance" / "evidence" / "determinex_react_repo_clinic_verified_demo_status_binding"
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"

CODEX_EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "repo_clinic_fixture_repair_splash_demo"
)


# ---------------------------------------------------------------------------
# Loader against the live Codex evidence
# ---------------------------------------------------------------------------
def test_loader_reads_live_codex_evidence_and_passes():
    rec = loader.load()
    assert rec.is_passed, rec.notes
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False
    assert rec.target_surface == "Repo Clinic"
    assert rec.target_language == "Python"
    assert "fixture repo to verifier-backed repair evidence" in rec.target_workflow
    assert rec.baseline_failed is True
    assert rec.repair_tests_passed is True
    assert rec.repair_verified is True
    assert rec.false_fixed_claim_blocked is True
    assert rec.fixture_mutation_only is True
    assert rec.real_user_source_mutation_authorized is False
    assert rec.affected_files == ("src/task_reporter/report.py",)
    assert rec.patch_body_hash.startswith("08c463e8a0")


def test_loader_returns_awaiting_when_evidence_missing(tmp_path):
    rec = loader.load(tmp_path / "no-such-dir")
    assert rec.is_awaiting
    assert "awaiting" in rec.demo_title.lower()
    assert rec.baseline_failed is False
    assert rec.repair_tests_passed is False
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False


def test_loader_status_tokens_exact():
    assert set(loader.REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_STATUS_TOKENS) == {
        "REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_PASSED",
        "REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_AWAITING_EVIDENCE",
        "REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_BROAD_CLAIM",
        "REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_AUTHORITY_CONFUSION",
        "REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_BLOCKED_MALFORMED",
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


def test_loader_blocks_when_real_user_source_mutation_authorized_true(tmp_path):
    def m(b):
        b.setdefault("authority", {})
        b["authority"]["real_user_source_mutation_authorized"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_top_level_real_user_source_mutation_authorized_true(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__("real_user_source_mutation_authorized", True),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_when_approval_authority_granted_true(tmp_path):
    def m(b):
        b.setdefault("authority", {})
        b["authority"]["approval_authority_granted"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked


def test_loader_blocks_when_broad_claims_granted_true(tmp_path):
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


def test_loader_blocks_when_claim_boundary_missing_required(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__(
            "claim_boundary",
            ["Repo Clinic Python fixture repair demo only"],
        ),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_when_evidence_carries_affirmative_broad_claim(tmp_path):
    def m(b):
        b["loose_marketing_string"] = "Determinex can repair all codebases."
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


def test_loader_blocks_repair_verified_without_baseline_or_repair_tests(tmp_path):
    def m(b):
        v = b.setdefault("verification", {})
        v["repair_verified"] = True
        v["baseline_failed"] = False
        v["repair_tests_passed"] = True
        v["false_fixed_claim_blocked"] = True
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


def test_loader_blocks_repair_verified_without_false_fixed_claim_block(tmp_path):
    def m(b):
        v = b.setdefault("verification", {})
        v["repair_verified"] = True
        v["baseline_failed"] = True
        v["repair_tests_passed"] = True
        v["false_fixed_claim_blocked"] = False
    ed = _write_tampered(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "AUTHORITY_CONFUSION" in rec.decision


# ---------------------------------------------------------------------------
# Malformed / non-passing evidence
# ---------------------------------------------------------------------------
def test_loader_blocks_when_status_not_passed(tmp_path):
    ed = _write_tampered(
        tmp_path,
        lambda b: b.__setitem__("status", "REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_BLOCKED_VERIFIER_MISSING"),
    )
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "MALFORMED" in rec.decision


def test_loader_returns_awaiting_when_evidence_is_corrupt(tmp_path):
    p = tmp_path / "run_99999999.corrupt.json"
    p.write_text("{not valid json}", encoding="utf-8")
    rec = loader.load(tmp_path)
    assert rec.is_awaiting


# ---------------------------------------------------------------------------
# Backend command surface routing
# ---------------------------------------------------------------------------
def test_command_registered_in_unified_set():
    assert "get_repo_clinic_verified_demo_status" in bcs.commands()
    assert "get_repo_clinic_verified_demo_status" in (
        bcs.UNIFIED_PRODUCT_READ_ONLY_COMMANDS
    )


def test_command_returns_ok_with_no_authority_leak():
    surface = bcs.IDEBackendCommandSurface()
    r = surface.call("get_repo_clinic_verified_demo_status")
    assert r.status == "IDE_COMMAND_OK"
    assert r.source_mutation_authorized is False
    assert r.training_eligible is False
    assert r.payload.get("decision", "").startswith(
        "REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_"
    )


def test_tauri_driver_routes_command():
    res = td._dispatch("get_repo_clinic_verified_demo_status", {})
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
    assert '"get_repo_clinic_verified_demo_status"' in src
    for forbidden in (
        "apply_source", "approve_packet", "write_training_row",
        "release_workflow", "run_programbench",
    ):
        assert forbidden not in src


def test_react_component_renders_required_sections():
    src = _src()
    for tid in (
        "repo-clinic-verified-demo-status",
        "repo-clinic-verified-demo-status-demo-title",
        "repo-clinic-verified-demo-status-target-workflow",
        "repo-clinic-verified-demo-status-target-language",
        "repo-clinic-verified-demo-status-issue-summary",
        "repo-clinic-verified-demo-status-baseline-failed",
        "repo-clinic-verified-demo-status-repair-tests-passed",
        "repo-clinic-verified-demo-status-repair-verified",
        "repo-clinic-verified-demo-status-false-fixed-claim-blocked",
        "repo-clinic-verified-demo-status-fixture-mutation-only",
        "repo-clinic-verified-demo-status-affected-files",
        "repo-clinic-verified-demo-status-evidence-ref",
        "repo-clinic-verified-demo-status-patch-body-hash",
        "repo-clinic-verified-demo-status-fixture-workspace",
        "repo-clinic-verified-demo-status-training-eligibility",
        "repo-clinic-verified-demo-status-source-mutation",
        "repo-clinic-verified-demo-status-claim-boundary",
        "repo-clinic-verified-demo-status-blocked-path-summary",
        "repo-clinic-verified-demo-status-scoped-only-caption",
        "repo-clinic-verified-demo-status-no-real-user-repo-caption",
    ):
        assert f'data-testid="{tid}"' in src, tid


def test_react_component_surfaces_awaiting_banner():
    src = _src()
    assert 'data-testid="repo-clinic-verified-demo-status-awaiting-banner"' in src
    assert "Awaiting Codex reconciliation" in src


def test_react_component_surfaces_blocked_banner():
    src = _src()
    assert 'data-testid="repo-clinic-verified-demo-status-blocked-banner"' in src


def test_react_component_training_badge_is_false():
    src = _src()
    assert 'data-training-eligible="false"' in src
    assert "training_eligible: false" in src


def test_react_component_real_user_source_mutation_marked_false():
    src = _src()
    assert (
        "real_user_source_mutation_authorized: false (remains false)" in src
    )
    assert 'data-testid="repo-clinic-verified-demo-status-no-real-user-repo-caption"' in src
    assert "Real user repo mutation NOT authorized." in src


def test_react_component_repair_verified_label_says_fixture_only():
    src = _src()
    assert "verified ONLY for this fixture demo path" in src


def test_react_component_scoped_caption_present():
    src = _src()
    assert "not all codebases" in src
    assert "not all languages" in src
    assert "not arbitrary repair" in src
    assert "not production-ready arbitrary repair" in src


def test_react_component_does_not_carry_forbidden_phrases():
    src = _src().lower()
    forbidden = (
        "production-ready in any repo",
        "training enabled by default",
        "release ready: true",
        "no follow-up required",
        "all codebases supported",
        "real user repo mutation authorized",
        "arbitrary production repair",
    )
    for f in forbidden:
        assert f not in src, f


def test_api_lib_lists_new_command():
    src = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_repo_clinic_verified_demo_status"' in src


# ---------------------------------------------------------------------------
# Authority / training stay false
# ---------------------------------------------------------------------------
def test_authority_training_stay_false_throughout():
    """Loader, command surface, and Tauri response ALL declare
    source_mutation_authorized=False and training_eligible=False on
    every code path tested above."""
    # Live evidence.
    rec = loader.load()
    assert rec.source_mutation_authorized is False
    assert rec.training_eligible is False

    surface = bcs.IDEBackendCommandSurface()
    r = surface.call("get_repo_clinic_verified_demo_status")
    assert r.source_mutation_authorized is False
    assert r.training_eligible is False
    assert r.payload.get("source_mutation_authorized") is False
    assert r.payload.get("training_eligible") is False

    res = td._dispatch("get_repo_clinic_verified_demo_status", {})
    assert res["source_mutation_authorized"] is False
    assert res["training_eligible"] is False


# ---------------------------------------------------------------------------
# Existing Idea Lab binding remains green
# ---------------------------------------------------------------------------
def test_idea_lab_binding_still_passes():
    """Regression guard — adding the Repo Clinic verb must not have
    broken the Idea Lab binding."""
    idea_loader = importlib.import_module("ide.idea_lab_verified_demo_status")
    rec = idea_loader.load()
    assert rec.is_passed, rec.notes


def test_idea_lab_tauri_dispatch_still_passes():
    res = td._dispatch("get_idea_lab_verified_demo_status", {})
    assert res["status"] == "TAURI_COMMAND_OK"


# ---------------------------------------------------------------------------
# Lock / evidence / index
# ---------------------------------------------------------------------------
def test_lock_manifest_exists_and_validates():
    assert LOCK_PATH.is_file()
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert blob["lock_id"] == "DETERMINEX_REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_LOCK_001"
    sd = blob["scope_discipline"]
    assert sd["source_mutation_authorized"] is False
    assert sd["training_eligible"] is False


def test_evidence_artifact_present():
    candidates = sorted(EVIDENCE_DIR.glob("run_*.json"))
    assert candidates


def test_evidence_index_entry_present():
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    assert "DETERMINEX_REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_LOCK_001" in ids
