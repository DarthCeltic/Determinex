"""Tests for DETERMINEX_REACT_DEMO_NAVIGATION_HAPPY_BLOCKED_PATH_LOCK_001.

Cross-panel coverage: the live shell must show BOTH the happy path
(verified Idea Lab Python CLI demo when evidence is available; or
explicit awaiting state if not) AND the blocked path (broad-claim
refusal, pre-smoke working-claim refusal, missing-verifier refusal).
Learning Studio must offer a teaching note for why blocked paths
are blocked, and the Proof / Operator Center must surface the
evidence/training-false/non-authorizing operator state.
"""
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

loader = importlib.import_module("ide.idea_lab_verified_demo_status")

SHELL_DIR = _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
LOCK_PATH = _REPO_ROOT / "locks" / "sentinel" / (
    "DETERMINEX_REACT_DEMO_NAVIGATION_HAPPY_BLOCKED_PATH_LOCK_001.json"
)
EVIDENCE_DIR = _REPO_ROOT / "assurance" / "evidence" / (
    "determinex_react_demo_navigation_happy_blocked_path"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"


def _read(name: str) -> str:
    return (SHELL_DIR / name).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------
def test_idea_lab_happy_path_status_resolvable():
    """When evidence is available, the loader returns PASSED with a
    verified-for-fixture status; the Idea Lab verified-demo-status
    component renders that."""
    rec = loader.load()
    # Either PASSED (live evidence present) or AWAITING_EVIDENCE
    # (evidence cleaned up between runs) — both are valid happy/awaiting
    # transitions. BLOCKED would indicate a regression.
    assert rec.is_passed or rec.is_awaiting, (
        f"unexpected demo loader decision: {rec.decision!r}"
    )


def test_idea_lab_verified_demo_status_component_renders_happy_path():
    src = _read("IdeaLabVerifiedDemoStatus.tsx")
    # The PASSED state must be representable. data-passed binding + verified
    # marker render the happy-path tag.
    assert "data-passed={passed}" in src
    assert 'data-testid="idea-lab-verified-demo-status-verified-value"' in src
    assert "verified ONLY for this fixture demo path" in src


def test_idea_lab_verified_demo_status_component_renders_awaiting_path():
    src = _read("IdeaLabVerifiedDemoStatus.tsx")
    assert "data-awaiting={awaiting}" in src
    assert 'data-testid="idea-lab-verified-demo-status-awaiting-banner"' in src
    assert "Awaiting Codex reconciliation" in src


def test_idea_lab_panel_shows_verified_working_status_token():
    """The Idea Lab workflow panel must still surface the
    VERIFIED_WORKING_LOCAL_APP token as part of the happy-path."""
    src = _read("IdeaLabPanel.tsx")
    assert "VERIFIED_WORKING_LOCAL_APP" in src


def test_splash_demo_marker_set_present():
    """The unified splash demo panel must mark happy / blocked /
    teaching / proof steps so the navigation shell exposes both
    paths visually."""
    src = _read("SplashDemoPanel.tsx")
    assert 'marker: "happy"' in src
    assert 'marker: "blocked"' in src
    assert 'marker: "teaching"' in src
    assert 'marker: "proof"' in src


# ---------------------------------------------------------------------------
# Blocked path — broad-claim, pre-smoke, missing-verifier
# ---------------------------------------------------------------------------
def test_splash_demo_lists_broad_claim_caveats():
    """The splash demo panel must enumerate the four broad-claim
    caveats so the blocked-path messaging is visible."""
    src = _read("SplashDemoPanel.tsx")
    for c in (
        "not all apps", "not all languages",
        "not production-ready arbitrary apps", "not training enabled",
    ):
        assert c in src, c


def test_idea_lab_panel_shows_pre_smoke_working_block():
    """Idea Lab panel must show a 'WORKING_DISABLED_NO_VERIFIER_EVIDENCE'
    badge when verifier evidence is missing — that's the blocked
    path for the pre-smoke working claim."""
    src = _read("IdeaLabPanel.tsx")
    assert "WORKING_DISABLED_NO_VERIFIER_EVIDENCE" in src
    assert "Working means build/test/smoke passed." in src


def test_repo_clinic_panel_shows_missing_verifier_block():
    """Repo Clinic must surface VERIFIER_MISSING (blocked path for
    missing-verifier scenarios)."""
    src = _read("RepoClinicPanel.tsx")
    assert "VERIFIER_MISSING" in src
    assert 'data-testid="repo-clinic-verifier-missing-badge"' in src


def test_maintenance_bay_shows_compatibility_verifier_block():
    src = _read("MaintenanceBayPanel.tsx")
    assert "UPDATED_LABEL_DISABLED_NO_VERIFIER" in src


def test_loader_blocks_pre_smoke_verified_claim(tmp_path):
    """Driver test: a tampered evidence file that claims verified
    without smoke pass MUST be blocked by the loader."""
    src_dir = (
        _REPO_ROOT / "assurance" / "evidence"
        / "idea_lab_python_cli_verified_splash_demo"
    )
    src = sorted(src_dir.glob("run_*.json"))[-1]
    blob = json.loads(src.read_text(encoding="utf-8"))
    blob.setdefault("verification", {})
    blob["verification"]["smoke_passed"] = False
    blob["verification"]["verified_working_local_app"] = True
    out = tmp_path / "run_99999999.tampered.json"
    out.write_text(json.dumps(blob), encoding="utf-8")
    rec = loader.load(tmp_path)
    assert rec.is_blocked


def test_loader_blocks_broad_claim_anywhere(tmp_path):
    src_dir = (
        _REPO_ROOT / "assurance" / "evidence"
        / "idea_lab_python_cli_verified_splash_demo"
    )
    src = sorted(src_dir.glob("run_*.json"))[-1]
    blob = json.loads(src.read_text(encoding="utf-8"))
    blob["marketing_blurb"] = (
        "Determinex builds production-ready arbitrary apps for any language."
    )
    out = tmp_path / "run_99999999.tampered.json"
    out.write_text(json.dumps(blob), encoding="utf-8")
    rec = loader.load(tmp_path)
    assert rec.is_blocked
    assert "BROAD_CLAIM" in rec.decision


# ---------------------------------------------------------------------------
# Teaching note — Learning Studio explains blocked reasons
# ---------------------------------------------------------------------------
def test_learning_studio_teaching_window_explains_blocked_reason():
    src = _read("LearningStudioPanel.tsx")
    assert 'data-testid="learning-studio-teaching-window-blocked-reason"' in src
    # The window's caption must name what gets blocked and why.
    assert "blocked" in src.lower()
    assert "gate" in src.lower()


def test_learning_studio_cannot_authorize_captions_visible():
    src = _read("LearningStudioPanel.tsx")
    assert "Learning cannot approve a patch." in src
    assert "Learning cannot mark repair success." in src
    assert "Learning cannot mutate source." in src


# ---------------------------------------------------------------------------
# Proof view — evidence, training-false, non-authorizing operator
# ---------------------------------------------------------------------------
def test_proof_operator_center_surfaces_evidence_ledger():
    src = _read("ProofOperatorCenterPanel.tsx")
    assert 'data-testid="proof-operator-center-evidence-ledger-status"' in src
    assert "records on disk (read-only)" in src


def test_proof_operator_center_surfaces_training_false():
    src = _read("ProofOperatorCenterPanel.tsx")
    assert 'data-testid="proof-operator-center-training-badge"' in src
    assert 'data-training-eligible="false"' in src
    assert "training_eligible: false (remains false)" in src


def test_proof_operator_center_operator_actions_are_requests():
    src = _read("ProofOperatorCenterPanel.tsx")
    assert 'data-kind="request"' in src
    assert 'data-kind="grant"' not in src
    assert "Operator queue request is a REQUEST, not a grant." in src


# ---------------------------------------------------------------------------
# Aggregated cross-panel presence
# ---------------------------------------------------------------------------
def test_happy_path_visible_across_shell():
    """At minimum: Idea Lab workflow panel surfaces the VERIFIED
    label AND the splash demo panel marks 2 happy steps."""
    idea = _read("IdeaLabPanel.tsx")
    splash = _read("SplashDemoPanel.tsx")
    assert "VERIFIED_WORKING_LOCAL_APP" in idea
    # SplashDemoPanel.tsx has at least 2 happy steps (idea_lab, repo_clinic).
    assert splash.count('marker: "happy"') >= 2


def test_blocked_path_visible_across_shell():
    """At minimum: Repo Clinic surfaces VERIFIER_MISSING, Idea Lab
    surfaces WORKING_DISABLED_NO_VERIFIER_EVIDENCE, Splash marks
    a blocked step."""
    assert "VERIFIER_MISSING" in _read("RepoClinicPanel.tsx")
    assert "WORKING_DISABLED_NO_VERIFIER_EVIDENCE" in _read("IdeaLabPanel.tsx")
    assert 'marker: "blocked"' in _read("SplashDemoPanel.tsx")


def test_teaching_note_visible():
    src = _read("LearningStudioPanel.tsx")
    assert 'data-testid="learning-studio-teaching-window-blocked-reason"' in src


def test_proof_view_visible():
    src = _read("ProofOperatorCenterPanel.tsx")
    # The "proof view" requires both evidence ledger AND a
    # blocked-actions list be visible.
    assert 'data-testid="proof-operator-center-evidence-ledger-status"' in src
    assert 'data-testid="proof-operator-center-blocked-actions"' in src


# ---------------------------------------------------------------------------
# Lock / evidence / index
# ---------------------------------------------------------------------------
def test_lock_manifest_exists_and_validates():
    assert LOCK_PATH.is_file()
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert blob["lock_id"] == "DETERMINEX_REACT_DEMO_NAVIGATION_HAPPY_BLOCKED_PATH_LOCK_001"
    sd = blob["scope_discipline"]
    assert sd["source_mutation_authorized"] is False
    assert sd["training_eligible"] is False


def test_evidence_artifact_present():
    assert sorted(EVIDENCE_DIR.glob("run_*.json"))


def test_evidence_index_entry_present():
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    assert "DETERMINEX_REACT_DEMO_NAVIGATION_HAPPY_BLOCKED_PATH_LOCK_001" in ids


def test_status_tokens_exact_on_lock_manifest():
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert set(blob["status_tokens"]) == {
        "REACT_DEMO_NAVIGATION_HAPPY_BLOCKED_PATH_PASSED",
        "REACT_DEMO_NAVIGATION_HAPPY_BLOCKED_PATH_BLOCKED_MISSING_HAPPY_PATH",
        "REACT_DEMO_NAVIGATION_HAPPY_BLOCKED_PATH_BLOCKED_MISSING_BLOCKED_PATH",
        "REACT_DEMO_NAVIGATION_HAPPY_BLOCKED_PATH_BLOCKED_MISSING_PROOF_VIEW",
    }
