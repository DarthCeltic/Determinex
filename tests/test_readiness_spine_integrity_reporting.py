"""Ledger integrity must be reported from evidence, never defaulted.

`public_readiness_spine_dashboard_status` read:

    pre_chain_valid      = bool(pre.get("ledger_chain_valid", True))
    pre_mutation_detected = bool(pre.get("mutation_detected", False))

Both values are display-only -- they populate the dashboard and gate nothing -- which is
precisely why the defaults mattered. A checkpoint that said nothing about the hash chain was
reported as "chain valid, no mutation detected". The dashboard's entire job is to state what
the evidence says, and on absent evidence it stated the reassuring answer.

Found 2026-08-02 by an AST scan for `.get(..., <success literal>)`, the same scan that found
the authority-boundary hole. Latent, not live: the current reconciliation record carries both
keys, which is what made tightening it safe.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

from tests.conftest import missing_private_evidence

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from ide import public_readiness_spine_dashboard_status as M  # noqa: E402


def _stage(tmp_path, mutate=None) -> Path:
    record = {
        "status": "TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_010_PASSED",
        "post_claude_pre_reconciliation_checkpoint": {
            "ledger_chain_valid": True,
            "mutation_detected": False,
        },
    }
    if mutate:
        mutate(record["post_claude_pre_reconciliation_checkpoint"])
    (tmp_path / "run_fixture.json").write_text(json.dumps(record), encoding="utf-8")
    return tmp_path


def test_complete_checkpoint_reports_observed_values(tmp_path):
    st = M.load(reconciliation_dir=_stage(tmp_path))
    assert st.decision.endswith("PASSED"), st.decision
    assert st.ledger_chain_valid is True
    assert st.mutation_detected is False


def test_missing_checkpoint_waits_for_evidence(tmp_path):
    assert M.load(reconciliation_dir=tmp_path).decision.endswith("AWAITING_EVIDENCE")


@pytest.mark.skipif(
    missing_private_evidence(), reason="declared public mirror omits the private evidence archive"
)
def test_the_live_dashboard_still_passes():
    """Load-bearing negative control: tightening a reporting gate must not move it."""
    assert M.load().decision.endswith("PASSED")


@pytest.mark.skipif(
    missing_private_evidence(), reason="declared public mirror omits the private evidence archive"
)
def test_the_real_checkpoint_carries_both_integrity_keys():
    """Documents why the fix was safe, and fails loudly if an evidence generator stops
    emitting them -- instead of the dashboard silently starting to block."""
    blob = json.loads(M._locate_latest_evidence(M._RECON_010_DIR).read_text(encoding="utf-8"))
    pre = blob.get("post_claude_pre_reconciliation_checkpoint") or {}
    for key in ("ledger_chain_valid", "mutation_detected"):
        assert key in pre, f"reconciliation evidence no longer states {key}"


@pytest.mark.parametrize("key", ["ledger_chain_valid", "mutation_detected"])
def test_missing_integrity_key_blocks(tmp_path, key):
    st = M.load(reconciliation_dir=_stage(tmp_path, lambda pre: pre.pop(key)))
    assert "BLOCKED" in st.decision, st.decision
    assert any(key in note for note in st.notes), st.notes


def test_a_genuinely_invalid_chain_is_reported_as_invalid_not_blocked(tmp_path):
    st = M.load(
        reconciliation_dir=_stage(tmp_path, lambda pre: pre.update(ledger_chain_valid=False))
    )
    assert st.decision.endswith("PASSED"), st.decision
    assert st.ledger_chain_valid is False
