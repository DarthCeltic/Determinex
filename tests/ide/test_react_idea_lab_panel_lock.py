"""Tests for DETERMINEX_REACT_IDEA_LAB_PANEL_LOCK_001."""
from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

PANEL_PATH = _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell" / "IdeaLabPanel.tsx"
LOCK_PATH = _REPO_ROOT / "locks" / "sentinel" / "DETERMINEX_REACT_IDEA_LAB_PANEL_LOCK_001.json"
EVIDENCE_DIR = _REPO_ROOT / "assurance" / "evidence" / "determinex_react_idea_lab_panel"
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"


def _src() -> str:
    return PANEL_PATH.read_text(encoding="utf-8")


def test_panel_file_exists():
    assert PANEL_PATH.is_file()


def test_status_tokens_declared():
    src = _src()
    for t in (
        "REACT_IDEA_LAB_PANEL_PASSED",
        "REACT_IDEA_LAB_PANEL_BLOCKED_FALSE_WORKING_LABEL",
        "REACT_IDEA_LAB_PANEL_BLOCKED_MISSING_SUPPORT_CHECK",
        "REACT_IDEA_LAB_PANEL_BLOCKED_HIDDEN_CAVEATS",
    ):
        assert t in src


def test_required_sections_present():
    src = _src()
    for tid in (
        "idea-lab-idea-intake-status",
        "idea-lab-support-check-status",
        "idea-lab-blueprint-status",
        "idea-lab-scaffold-status",
        "idea-lab-tests-status",
        "idea-lab-build-test-verifier-status",
        "idea-lab-smoke-status",
        "idea-lab-evidence-status",
        "idea-lab-training-eligibility-status",
        "idea-lab-unsupported-caveat-status",
    ):
        assert f'data-testid="{tid}"' in src, tid


def test_build_it_button_present_and_gated():
    src = _src()
    assert 'data-testid="idea-lab-build-it-button"' in src
    # The button is disabled when supportCheckPassed is False.
    assert "disabled={!buildItEnabled}" in src
    assert 'data-testid="idea-lab-build-it-disabled-reason"' in src


def test_working_label_only_with_evidence():
    src = _src()
    # workingLabelEnabled depends on all three verifier flags.
    assert "buildVerifierPassed && testsPassed && smokePassed" in src
    assert "WORKING_DISABLED_NO_VERIFIER_EVIDENCE" in src
    assert "VERIFIED_WORKING_LOCAL_APP" in src
    assert 'data-testid="idea-lab-working-meaning"' in src
    assert "Working means build/test/smoke passed." in src


def test_generated_unverified_state_visible():
    src = _src()
    assert "GENERATED_UNVERIFIED" in src
    assert 'data-testid="idea-lab-generated-unverified"' in src
    assert "Generated is not verified." in src


def test_cost_setup_caveats_visible():
    src = _src()
    assert 'data-testid="idea-lab-cost-setup-caveat"' in src
    assert "External cost / setup" in src
    assert "not all apps" in src
    assert "not all languages" in src


def test_training_eligibility_always_false():
    src = _src()
    assert "training_eligible: false" in src
    assert "remains false" in src


def test_no_forbidden_success_text():
    src = _src().lower()
    for f in (
        "your app is working", "fixed!", "deployment ready",
        "production-ready", "all apps supported",
    ):
        assert f not in src, f


def test_panel_only_invokes_read_only_command():
    src = _src()
    assert 'invokeUnifiedProductCommand("get_idea_lab_workflow_state")' in src
    for forbidden in ("apply_source", "approve_packet", "write_training", "release_workflow"):
        assert forbidden not in src


def test_ready_does_not_mean_authorized_present():
    src = _src()
    assert "READY_DOES_NOT_MEAN_AUTHORIZED" in src


def test_lock_manifest_exists_and_validates():
    assert LOCK_PATH.is_file()
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert blob["lock_id"] == "DETERMINEX_REACT_IDEA_LAB_PANEL_LOCK_001"
    sd = blob["scope_discipline"]
    assert sd["source_mutation_authorized"] is False
    assert sd["training_eligible"] is False


def test_evidence_artifact_present():
    assert sorted(EVIDENCE_DIR.glob("run_*.json"))


def test_evidence_index_entry_present():
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    assert "DETERMINEX_REACT_IDEA_LAB_PANEL_LOCK_001" in ids
