"""Tests for DETERMINEX_REACT_RELEASE_READINESS_BLOCKER_PANEL_LOCK_001."""
from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

PANEL_PATH = _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell" / "ReleaseReadinessBlockerPanel.tsx"
LOCK_PATH = _REPO_ROOT / "locks" / "sentinel" / "DETERMINEX_REACT_RELEASE_READINESS_BLOCKER_PANEL_LOCK_001.json"
EVIDENCE_DIR = _REPO_ROOT / "assurance" / "evidence" / "determinex_react_release_readiness_blocker_panel"
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"


def _src() -> str:
    return PANEL_PATH.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Inventory
# ---------------------------------------------------------------------------
def test_panel_file_exists():
    assert PANEL_PATH.is_file()


def test_status_tokens_declared():
    src = _src()
    for t in (
        "REACT_RELEASE_READINESS_BLOCKER_PANEL_PASSED",
        "REACT_RELEASE_READINESS_BLOCKER_PANEL_BLOCKED_HIDES_RELEASE_FALSE",
        "REACT_RELEASE_READINESS_BLOCKER_PANEL_BLOCKED_HIDES_CLAIM_LIMITS",
    ):
        assert t in src


# ---------------------------------------------------------------------------
# Required sections visible
# ---------------------------------------------------------------------------
def test_required_sections_present():
    src = _src()
    for tid in (
        "release-readiness-blocker-panel",
        "release-readiness-blocker-panel-release-ready-badge",
        "release-readiness-blocker-panel-public-release-scrub-required",
        "release-readiness-blocker-panel-install-demo-workflow-pending",
        "release-readiness-blocker-panel-repo-scrub-pending",
        "release-readiness-blocker-panel-claim-ledger-active",
        "release-readiness-blocker-panel-evidence-reconciliation-status",
        "release-readiness-blocker-panel-broad-public-claims-granted",
        "release-readiness-blocker-panel-training-eligible",
        "release-readiness-blocker-panel-programbench-status",
        "release-readiness-blocker-panel-source-mutation-authorized",
    ):
        assert f'data-testid="{tid}"' in src, tid


def test_release_ready_false_badge_visible():
    src = _src()
    assert 'data-testid="release-readiness-blocker-panel-release-ready-badge"' in src
    assert 'data-value="false"' in src
    assert "release_ready: false" in src


def test_data_release_ready_attribute_false():
    src = _src()
    assert "data-release-ready={releaseReady}" in src
    assert "const releaseReady = false;" in src


def test_public_release_scrub_required_visible():
    src = _src()
    assert "public_release_scrub_required" in src
    assert "const publicReleaseScrubRequired = true;" in src
    assert "scrub blocker active" in src


def test_install_demo_workflow_pending_visible():
    src = _src()
    assert "const installDemoWorkflowPending = true;" in src
    assert "install/demo workflow not yet shipped" in src


def test_repo_scrub_pending_visible():
    src = _src()
    assert "const repoScrubPending = true;" in src
    assert "repository scrub workflow has not yet run" in src


def test_claim_ledger_active_visible():
    src = _src()
    assert "const claimLedgerActive = true;" in src
    assert "CLAUDE_PUBLIC_CLAIMS_LEDGER_LOCK_001" in src


def test_evidence_reconciliation_status_visible():
    src = _src()
    # Default reconciliation status mentions WORKSPACE_EVIDENCE_RECONCILIATION.
    assert "WORKSPACE_EVIDENCE_RECONCILIATION_PASSED" in src


# ---------------------------------------------------------------------------
# Hard invariants visible
# ---------------------------------------------------------------------------
def test_broad_public_claims_granted_false():
    src = _src()
    assert "const broadPublicClaimsGranted = false;" in src
    assert "data-broad-public-claims-granted={broadPublicClaimsGranted}" in src
    assert "no broad public claim granted" in src


def test_training_eligible_false():
    src = _src()
    assert "const trainingEligible = false;" in src
    assert "data-training-eligible={trainingEligible}" in src or 'data-training-eligible="false"' in src
    assert "training_eligible: false (remains false)" in src


def test_programbench_not_executed_imported_or_scanned():
    src = _src()
    assert "const programbenchExecutedFromClaudeLane = false;" in src
    assert "const programbenchImportedFromClaudeLane = false;" in src
    assert "const programbenchScannedFromClaudeLane = false;" in src
    assert "NOT executed, NOT imported, NOT scanned (unless separately gated)" in src


def test_source_mutation_authorized_false():
    src = _src()
    assert "const sourceMutationAuthorized = false;" in src
    assert "data-source-mutation-authorized={sourceMutationAuthorized}" in src
    assert (
        "no source mutation authorized unless a separate proper approval gate supplies it"
        in src
    )


# ---------------------------------------------------------------------------
# Non-authorizing captions
# ---------------------------------------------------------------------------
def test_non_authorizing_caption_visible():
    src = _src()
    assert 'data-testid="release-readiness-blocker-panel-non-authorizing-caption"' in src
    assert "REPORTS status" in src
    assert "does NOT authorize" in src


def test_ready_does_not_mean_authorized_present():
    src = _src()
    assert "READY_DOES_NOT_MEAN_AUTHORIZED" in src


def test_training_stays_false_caption_visible():
    src = _src()
    assert "Training stays false (training_eligible: false)." in src


# ---------------------------------------------------------------------------
# No mutating command / no per-prop flag override
# ---------------------------------------------------------------------------
def test_no_mutating_command_invoked():
    src = _src()
    for forbidden in (
        "invokeUnifiedProductCommand",
        "apply_source", "approve_packet", "write_training_row",
        "release_workflow", "run_programbench",
    ):
        assert forbidden not in src, forbidden


def test_no_prop_overrides_release_ready():
    """Hard rule: releaseReady is a compile-time const, not derived
    from props. Tests forbid any pattern that ties release-ready
    state to a prop."""
    src = _src()
    forbidden = (
        "releaseReadyProp", "props.releaseReady",
        "if (props.releaseReady", "props.training",
    )
    for f in forbidden:
        assert f not in src, f


# ---------------------------------------------------------------------------
# Lock / evidence / index
# ---------------------------------------------------------------------------
def test_lock_manifest_exists_and_validates():
    assert LOCK_PATH.is_file()
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert blob["lock_id"] == "DETERMINEX_REACT_RELEASE_READINESS_BLOCKER_PANEL_LOCK_001"
    sd = blob["scope_discipline"]
    assert sd["source_mutation_authorized"] is False
    assert sd["training_eligible"] is False


def test_evidence_artifact_present():
    assert sorted(EVIDENCE_DIR.glob("run_*.json"))


def test_evidence_index_entry_present():
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    assert "DETERMINEX_REACT_RELEASE_READINESS_BLOCKER_PANEL_LOCK_001" in ids
