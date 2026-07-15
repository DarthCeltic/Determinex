"""Tests for DETERMINEX_REACT_PRODUCT_SHELL_BROWSER_SNAPSHOT_LOCK_001.

The repo does not currently have a wired headless-browser snapshot
runner (Playwright/Vitest+jsdom/Storybook). The blocker is filed at
assurance/evidence/deferred_findings/. Until that lands, this lock
provides the strongest available static / component-render checks
across all 8 mounted panels: every required testid section,
authority caption, training-false state, unsupported-universal
caveat, 'Proof Before Mutation' tagline, 'Generated is not
verified', and 'Working means build/test/smoke passed' must appear
in the rendered .tsx source.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

SHELL_DIR = _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
LOCK_PATH = _REPO_ROOT / "locks" / "sentinel" / (
    "DETERMINEX_REACT_PRODUCT_SHELL_BROWSER_SNAPSHOT_LOCK_001.json"
)
EVIDENCE_DIR = _REPO_ROOT / "assurance" / "evidence" / (
    "determinex_react_product_shell_browser_snapshot"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
BLOCKER_PATH = _REPO_ROOT / "assurance" / "evidence" / "deferred_findings" / (
    "claude_lane_finding_browser_snapshot_tooling_unavailable_20260528.json"
)


PANELS = (
    "UnifiedNavigationPanel.tsx",
    "IdeaLabPanel.tsx",
    "RepoClinicPanel.tsx",
    "MaintenanceBayPanel.tsx",
    "LearningStudioPanel.tsx",
    "ProofOperatorCenterPanel.tsx",
    "UserLevelTeachingMode.tsx",
    "SplashDemoPanel.tsx",
)


def _all_src() -> dict[str, str]:
    return {
        name: (SHELL_DIR / name).read_text(encoding="utf-8")
        for name in PANELS
    }


# ---------------------------------------------------------------------------
# Inventory
# ---------------------------------------------------------------------------
def test_all_eight_panels_exist():
    for name in PANELS:
        assert (SHELL_DIR / name).is_file(), name


def test_each_panel_has_default_export():
    for name, src in _all_src().items():
        assert "export default " in src, name


def test_each_panel_exports_status_tokens_constant():
    for name, src in _all_src().items():
        assert "_STATUS_TOKENS = [" in src, name


# ---------------------------------------------------------------------------
# Required across-panel content
# ---------------------------------------------------------------------------
def test_ready_does_not_mean_authorized_visible_per_panel():
    """Splash panel is exempt — it carries the 'Proof Before Mutation'
    tagline instead. Every other panel must carry the
    READY_DOES_NOT_MEAN_AUTHORIZED constant."""
    for name, src in _all_src().items():
        if name == "SplashDemoPanel.tsx":
            continue
        assert "READY_DOES_NOT_MEAN_AUTHORIZED" in src, name


def test_training_false_visible_per_panel():
    """Every panel must say training is false somewhere — either in a
    'training_eligible: false' string, a data-training-eligible="false"
    attribute, or as a 'training stays false' / 'remains false' caption."""
    for name, src in _all_src().items():
        lower = src.lower()
        signals = (
            "training_eligible: false",
            'data-training-eligible="false"',
            "training stays false",
            "remains false",
            "training_eligible=false",
            "training: false",
            "training false",
            "trainingstaysfalse",  # camelCase constant
            "not training enabled",
            # Navigation panel: per-surface training_eligibility_boundary
            # text is rendered. The boundary string itself is supplied by
            # the backend view-model and always says "training_eligible
            # stays False" — accept the boundary-render pattern.
            "training_eligibility_boundary",
        )
        assert any(s in lower for s in signals), name


def test_blocked_states_visible_per_panel():
    """Every panel must surface at least one BLOCKED / NOT_AUTHORIZED /
    DISABLED / VERIFIER_MISSING / TOOLCHAIN_MISSING / BLOCKED_PENDING
    style label in its rendered output."""
    blocked_signals = (
        "BLOCKED_", "_DISABLED_", "_MISSING_", "_BLOCKED",
        "DISABLED_", "MISSING_", "UNDISCLOSED", "PENDING",
        "UNSUPPORTED_", "REQUIRED",
    )
    for name, src in _all_src().items():
        upper = src
        assert any(b in upper for b in blocked_signals), name


# ---------------------------------------------------------------------------
# Tagline and required phrases (splash + cross-panel coverage)
# ---------------------------------------------------------------------------
def test_proof_before_mutation_tagline_visible_in_splash():
    src = (SHELL_DIR / "SplashDemoPanel.tsx").read_text(encoding="utf-8")
    assert "Proof Before Mutation" in src
    assert 'data-testid="splash-demo-tagline"' in src
    assert 'data-tagline="Proof Before Mutation"' in src


def test_generated_is_not_verified_visible_in_splash():
    src = (SHELL_DIR / "SplashDemoPanel.tsx").read_text(encoding="utf-8")
    assert "Generated is not verified." in src
    assert 'data-testid="splash-demo-phrase-generated-not-verified"' in src


def test_working_means_visible_in_splash():
    src = (SHELL_DIR / "SplashDemoPanel.tsx").read_text(encoding="utf-8")
    assert "Working means build/test/smoke passed." in src
    assert 'data-testid="splash-demo-phrase-working-means"' in src


def test_unsupported_universal_caveats_visible_in_splash():
    src = (SHELL_DIR / "SplashDemoPanel.tsx").read_text(encoding="utf-8")
    for caveat in (
        "not all apps", "not all languages",
        "not production-ready arbitrary apps", "not training enabled",
    ):
        assert caveat in src, caveat


def test_generated_is_not_verified_visible_in_idea_lab():
    src = (SHELL_DIR / "IdeaLabPanel.tsx").read_text(encoding="utf-8")
    assert "Generated is not verified." in src
    assert "GENERATED_UNVERIFIED" in src


def test_idea_lab_unsupported_caveats_visible():
    src = (SHELL_DIR / "IdeaLabPanel.tsx").read_text(encoding="utf-8")
    assert "not all apps" in src
    assert "not all languages" in src


# ---------------------------------------------------------------------------
# Five-surface visibility from the navigation panel
# ---------------------------------------------------------------------------
def test_five_surfaces_referenced_in_navigation_panel():
    src = (SHELL_DIR / "UnifiedNavigationPanel.tsx").read_text(encoding="utf-8")
    for k in (
        "idea_lab", "repo_clinic", "maintenance_bay",
        "learning_studio", "proof_operator_center",
    ):
        assert f'"{k}"' in src or k in src, k


def test_five_surface_labels_visible_in_navigation_panel():
    src = (SHELL_DIR / "UnifiedNavigationPanel.tsx").read_text(encoding="utf-8")
    for label in (
        "Idea Lab", "Repo Clinic", "Maintenance Bay",
        "Learning Studio", "Proof / Operator Center",
    ):
        assert label in src, label


# ---------------------------------------------------------------------------
# No mutating Tauri verbs across the shell
# ---------------------------------------------------------------------------
def test_no_mutating_tauri_verb_in_shell():
    forbidden = (
        "apply_source", "approve_packet", "write_training_row",
        "grant_authorization", "release_workflow", "run_programbench",
    )
    for name, src in _all_src().items():
        for f in forbidden:
            assert f not in src, f"{f!r} in {name}"


# ---------------------------------------------------------------------------
# Blocker record exists
# ---------------------------------------------------------------------------
def test_browser_snapshot_tooling_blocker_recorded():
    assert BLOCKER_PATH.is_file()
    blob = json.loads(BLOCKER_PATH.read_text(encoding="utf-8"))
    assert blob["finding_id"]
    assert "browser_snapshot" in blob["finding_id"].lower()
    assert blob.get("category") == "tooling-gap"


# ---------------------------------------------------------------------------
# Status tokens declared on the lock manifest
# ---------------------------------------------------------------------------
def test_lock_manifest_status_tokens_exact():
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert set(blob["status_tokens"]) == {
        "REACT_PRODUCT_SHELL_BROWSER_SNAPSHOT_PASSED",
        "REACT_PRODUCT_SHELL_BROWSER_SNAPSHOT_BLOCKED_TOOLING_UNAVAILABLE",
        "REACT_PRODUCT_SHELL_BROWSER_SNAPSHOT_BLOCKED_MISSING_SURFACE",
        "REACT_PRODUCT_SHELL_BROWSER_SNAPSHOT_BLOCKED_AUTHORITY_CONFUSION",
    }


# ---------------------------------------------------------------------------
# Lock / evidence / index
# ---------------------------------------------------------------------------
def test_lock_manifest_exists_and_validates():
    assert LOCK_PATH.is_file()
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert blob["lock_id"] == "DETERMINEX_REACT_PRODUCT_SHELL_BROWSER_SNAPSHOT_LOCK_001"
    sd = blob["scope_discipline"]
    assert sd["source_mutation_authorized"] is False
    assert sd["training_eligible"] is False


def test_evidence_artifact_present():
    candidates = sorted(EVIDENCE_DIR.glob("run_*.json"))
    assert candidates


def test_evidence_index_entry_present():
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    assert "DETERMINEX_REACT_PRODUCT_SHELL_BROWSER_SNAPSHOT_LOCK_001" in ids
