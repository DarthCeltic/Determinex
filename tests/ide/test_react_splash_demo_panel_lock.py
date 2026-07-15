"""Tests for DETERMINEX_REACT_SPLASH_DEMO_PANEL_LOCK_001."""
from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

PANEL_PATH = _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell" / "SplashDemoPanel.tsx"
LOCK_PATH = _REPO_ROOT / "locks" / "sentinel" / "DETERMINEX_REACT_SPLASH_DEMO_PANEL_LOCK_001.json"
EVIDENCE_DIR = _REPO_ROOT / "assurance" / "evidence" / "determinex_react_splash_demo_panel"
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"


def _src() -> str:
    return PANEL_PATH.read_text(encoding="utf-8")


def test_panel_file_exists():
    assert PANEL_PATH.is_file()


def test_status_tokens_declared():
    src = _src()
    for t in (
        "REACT_SPLASH_DEMO_PANEL_PASSED",
        "REACT_SPLASH_DEMO_PANEL_BLOCKED_FALSE_UNIVERSALITY",
        "REACT_SPLASH_DEMO_PANEL_BLOCKED_AUTHORITY_CONFUSION",
        "REACT_SPLASH_DEMO_PANEL_BLOCKED_MISSING_PROOF_VIEW",
    ):
        assert t in src


def test_five_steps_one_per_surface_in_order():
    src = _src()
    # The DEMO_STEPS array must contain idea_lab, repo_clinic,
    # maintenance_bay, learning_studio, proof_operator_center in order.
    idx_idea = src.index("idea_lab")
    idx_repo = src.index("repo_clinic")
    idx_main = src.index("maintenance_bay")
    idx_learn = src.index("learning_studio")
    idx_proof = src.index("proof_operator_center")
    assert idx_idea < idx_repo < idx_main < idx_learn < idx_proof


def test_required_markers_present():
    src = _src()
    assert 'marker: "happy"' in src
    assert 'marker: "blocked"' in src
    assert 'marker: "teaching"' in src
    assert 'marker: "proof"' in src


def test_proof_view_marker_visible():
    src = _src()
    # The marker test-id is rendered as a template literal:
    #   `splash-demo-marker-${step.marker}`
    # so we assert the template segment + the "proof" marker value
    # are both present.
    assert "splash-demo-marker-" in src
    assert "${step.marker}" in src
    # And the proof marker value is one of the canonical step markers.
    assert 'marker: "proof"' in src


def test_required_tagline_visible():
    src = _src()
    assert 'data-testid="splash-demo-tagline"' in src
    # Appears as tagline node AND as data attr.
    assert 'data-tagline="Proof Before Mutation"' in src
    assert "Proof Before Mutation" in src


def test_required_phrases_visible():
    src = _src()
    assert 'data-testid="splash-demo-phrase-generated-not-verified"' in src
    assert "Generated is not verified." in src
    assert 'data-testid="splash-demo-phrase-working-means"' in src
    assert "Working means build/test/smoke passed." in src


def test_does_not_prove_caveats_visible():
    src = _src()
    for tid, text in (
        ("splash-demo-caveat-not-all-apps", "not all apps"),
        ("splash-demo-caveat-not-all-languages", "not all languages"),
        ("splash-demo-caveat-not-production-ready", "not production-ready arbitrary apps"),
        ("splash-demo-caveat-not-training-enabled", "not training enabled"),
    ):
        assert f'data-testid="{tid}"' in src, tid
        assert text in src, text


def test_infrastructure_caveats_visible():
    src = _src()
    for tid, text in (
        ("splash-demo-no-network", "No network model call required."),
        ("splash-demo-no-docker", "No Docker required."),
        ("splash-demo-no-programbench", "No ProgramBench required."),
        ("splash-demo-no-real-user-repo", "No real user repo touched"),
    ):
        assert f'data-testid="{tid}"' in src, tid
        assert text in src, text


def test_no_forbidden_universality_claim():
    src = _src().lower()
    for f in (
        "all apps supported", "every language supported",
        "production-ready in any repo", "training enabled by default",
    ):
        assert f not in src, f


def test_no_mutating_command_invoked():
    src = _src()
    assert "invokeUnifiedProductCommand(" in src
    assert '"get_unified_splash_demo_spec"' in src
    for forbidden in ("apply_source", "approve_packet", "write_training", "release_workflow"):
        assert forbidden not in src


def test_no_real_user_repo_mention():
    src = _src()
    for forbidden in (
        "mutate the user's real repo", "real user source repo",
        "live production codebase",
    ):
        assert forbidden not in src


def test_lock_manifest_exists_and_validates():
    assert LOCK_PATH.is_file()
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert blob["lock_id"] == "DETERMINEX_REACT_SPLASH_DEMO_PANEL_LOCK_001"
    sd = blob["scope_discipline"]
    assert sd["source_mutation_authorized"] is False
    assert sd["training_eligible"] is False


def test_evidence_artifact_present():
    assert sorted(EVIDENCE_DIR.glob("run_*.json"))


def test_evidence_index_entry_present():
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    assert "DETERMINEX_REACT_SPLASH_DEMO_PANEL_LOCK_001" in ids
