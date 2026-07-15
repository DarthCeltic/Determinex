"""Tests for DETERMINEX_REACT_PROOF_OPERATOR_CENTER_PANEL_LOCK_001."""
from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

PANEL_PATH = _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell" / "ProofOperatorCenterPanel.tsx"
LOCK_PATH = _REPO_ROOT / "locks" / "sentinel" / "DETERMINEX_REACT_PROOF_OPERATOR_CENTER_PANEL_LOCK_001.json"
EVIDENCE_DIR = _REPO_ROOT / "assurance" / "evidence" / "determinex_react_proof_operator_center_panel"
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"


def _src() -> str:
    return PANEL_PATH.read_text(encoding="utf-8")


def test_panel_file_exists():
    assert PANEL_PATH.is_file()


def test_status_tokens_declared():
    src = _src()
    for t in (
        "REACT_PROOF_OPERATOR_CENTER_PANEL_PASSED",
        "REACT_PROOF_OPERATOR_CENTER_PANEL_BLOCKED_ACTION_HIDDEN",
        "REACT_PROOF_OPERATOR_CENTER_PANEL_BLOCKED_TRAINING_CONFUSION",
        "REACT_PROOF_OPERATOR_CENTER_PANEL_BLOCKED_OPERATOR_QUEUE_GRANT_CONFUSION",
    ):
        assert t in src


def test_required_sections_present():
    src = _src()
    for tid in (
        "proof-operator-center-evidence-ledger-status",
        "proof-operator-center-workspace-status",
        "proof-operator-center-source-mutation-gates",
        "proof-operator-center-verifier-status",
        "proof-operator-center-rollback-status",
        "proof-operator-center-operator-actions",
        "proof-operator-center-programbench-status",
        "proof-operator-center-training-status",
        "proof-operator-center-claim-safety-status",
        "proof-operator-center-blocked-actions",
    ):
        assert f'data-testid="{tid}"' in src, tid


def test_training_status_always_false():
    src = _src()
    assert 'data-testid="proof-operator-center-training-badge"' in src
    assert 'data-training-eligible="false"' in src
    assert "training_eligible: false (remains false)" in src


def test_blocked_actions_visible():
    src = _src()
    assert 'data-testid="proof-operator-center-blocked-actions-text"' in src
    # blockedActionsText default must mention several blocked things.
    assert "Source apply blocked" in src
    assert "Training blocked" in src
    assert "ProgramBench writes blocked" in src


def test_operator_queue_is_request_not_grant():
    src = _src()
    assert 'data-testid="proof-operator-center-queue-not-grant"' in src
    assert "Operator queue request is a REQUEST, not a grant." in src
    # Each operator request item carries data-kind=request and a routesTo.
    assert 'data-kind="request"' in src
    assert "data-routes-to={r.routesTo}" in src


def test_programbench_read_only_from_claude_lane_caption():
    src = _src()
    assert 'data-testid="proof-operator-center-programbench-read-only-from-claude-lane"' in src
    assert "ProgramBench / provenance is read-only from the Claude lane." in src
    # The default text also mentions read-only mirror.
    assert "read-only mirror from Codex lane" in src


def test_source_mutation_gates_list_visible():
    src = _src()
    assert "approval + verifier + snapshot + body hash + symlink refusal" in src


def test_no_grant_kind_anywhere():
    src = _src()
    assert 'data-kind="grant"' not in src
    assert "Authorized" not in src or "NOT authorized" in src.lower()


def test_no_mutating_command_invoked():
    src = _src()
    assert "invokeUnifiedProductCommand(" in src
    assert '"get_proof_operator_center_state"' in src
    for forbidden in ("apply_source", "approve_packet", "write_training", "release_workflow"):
        assert forbidden not in src


def test_ready_does_not_mean_authorized_present():
    src = _src()
    assert "READY_DOES_NOT_MEAN_AUTHORIZED" in src


def test_lock_manifest_exists_and_validates():
    assert LOCK_PATH.is_file()
    blob = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert blob["lock_id"] == "DETERMINEX_REACT_PROOF_OPERATOR_CENTER_PANEL_LOCK_001"
    sd = blob["scope_discipline"]
    assert sd["source_mutation_authorized"] is False
    assert sd["training_eligible"] is False


def test_evidence_artifact_present():
    assert sorted(EVIDENCE_DIR.glob("run_*.json"))


def test_evidence_index_entry_present():
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    assert "DETERMINEX_REACT_PROOF_OPERATOR_CENTER_PANEL_LOCK_001" in ids
