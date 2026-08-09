"""Guards on the HuggingFace publish path.

This is the only code in the project that sends corpus content to a public host. Everything else
can be wrong and fixed; a published secret cannot be unpublished. So the properties are asserted
rather than reviewed, and each refusal is tested by making it fire.

The load-bearing insight is that `_residue()` cannot prove what it appears to prove. It re-scans
using the same patterns that performed the redaction, so it confirms that list is SATISFIED and
never that the list is COMPLETE -- the identical limitation already documented for Cloak's leak
count. A sweep of the real payload found /root/Citadel, /opt/determinex_clock and the operator's
hosting provider passing every check, under a consent record promising "no paths". Hence two
instruments with different pattern sets, and tests for both.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "scripts"))

import determinex_corpus_share as sh  # noqa: E402

# Assembled from pieces so this file never itself contains a literal that a secret scanner or a
# reader would take for a real credential.
_PLANTED = {
    "anthropic key": "sk-ant-api03-" + "A" * 24,
    "github token": "ghp_" + "B" * 32,
    "hf token": "hf_" + "C" * 32,
    "aws key": "AKIA" + "D" * 16,
    "google key": "AIzaSy" + "E" * 30,
    "email": "someone" + chr(64) + "example.com",
    "ipv4": "10.0.0.2",
    "windows user path": "C:" + chr(92) + "Users" + chr(92) + "someone" + chr(92) + "x",
    "unix home": "/home/someone/x",
    "server path": "/root/SomeProject/scripts",
    "hosting provider": "the Hetzner box",
}


def test_redaction_removes_every_class_it_claims_to_catch():
    for label, secret in _PLANTED.items():
        cleaned = sh.redact(f"a lesson mentioning {secret} in passing")
        assert secret not in cleaned, f"{label} survived redaction"


def test_residue_scan_fires_when_redaction_is_skipped():
    """A re-scan that has never been shown to fire is indistinguishable from one hardwired clean."""
    for label, secret in _PLANTED.items():
        if not sh._residue(secret):
            # Not every planted string is in _REDACTIONS' own vocabulary (that is the whole
            # reason the second sweep exists) -- but it must then be caught by that sweep.
            assert sh.completeness_sweep(secret), f"{label} is caught by neither instrument"


def test_completeness_sweep_catches_what_the_redactor_has_no_pattern_for():
    """The instrument that found the real leak. These are ownership markers, not credentials."""
    for text in (
        "reproduced on the Hetzner box",
        "see /root/SomeProject/scripts for the fix",
        "/opt/determinex_clock drifted",
        "key at ~/.ssh/id_something",
    ):
        assert sh.completeness_sweep(text), f"sweep missed: {text}"


def test_completeness_sweep_is_quiet_on_an_ordinary_lesson():
    """A check that fires on normal data is a check somebody disables the week after it lands.

    A generic high-entropy rule was tried here and flagged half the class names plus the
    payload's own content hash. It was removed rather than tuned: on a corpus whose substance is
    long identifiers, entropy cannot separate a secret from a subject.
    """
    for text in (
        "cargo build fails without --offline; add the flag",
        "DETERMINEX_TYPESCRIPT_NODE_CLI_ADAPTER_LOCK_001 pins the adapter",
        "content sha256 " + "a1b2c3d4" * 8,
        "collection_cap_hides_untested_majority",
    ):
        assert not sh.completeness_sweep(text), f"false positive on: {text}"


def test_the_real_payload_passes_both_instruments():
    """The one that actually gates a publish."""
    body = json.dumps(sh.build_payload(), ensure_ascii=False)
    assert not sh._residue(body), "live payload failed the redaction re-scan"
    assert not sh.completeness_sweep(body), "live payload failed the completeness sweep"


# ── provenance: a published claim must carry its own evidence ────────────────


def test_every_published_row_declares_its_confidence():
    """267 of these rows are unconfirmed hints. Publishing them beside oracle-verified classes
    without a per-row marker would be the exact overclaim this project keeps auditing out of its
    own documents."""
    rows = sh._rows()
    assert rows
    valid = {"oracle_verified", "mixed", "generalized", "reference"}
    for r in rows:
        assert r["source"], "row without a source"
        assert r["confidence"] in valid, f"{r['id']} has confidence {r['confidence']!r}"
        assert isinstance(r["verified"], bool)


def test_evidence_text_counts_as_verification_not_just_a_boolean():
    """`proven` holds free text -- "go-critic 1.2%->94.5%" -- not True.

    An identity check against True marked all 84 class patterns unverified, and the dataset card
    would have advertised 5 verified rows out of 381 while the evidence for 50 sat in the file.
    """
    rows = sh._rows()
    verified = [r for r in rows if r["verified"]]
    assert len(verified) > 40, (
        f"only {len(verified)} rows counted as verified; the `proven` evidence string is "
        "probably being compared against True again"
    )
    with_evidence = [r for r in verified if r.get("proven")]
    assert with_evidence, "no verified row carries its evidence text"


def test_a_row_with_no_evidence_is_not_counted_as_verified():
    """39 class patterns carry no `proven` string. Whatever the layer is called, they are not
    individually attested and must not be published as if they were."""
    rows = sh._rows()
    for r in rows:
        if r["source"] == "class_pattern" and not str(r.get("proven") or "").strip():
            assert not r["verified"], f"{r['id']} claims verification with no evidence"


def test_operational_history_is_not_published():
    """Dated write-up entries are this project's session log: host names, drive letters, campaign
    specifics. No amount of redaction turns a session log into transferable knowledge."""
    ids = {r["id"] for r in sh._rows()}
    kn = json.loads(sh.CORPUS.read_text(encoding="utf-8"))
    dated = {
        k
        for k in kn
        if not k.startswith("_")
        and k not in ("class_patterns", "learned_classes")
        and isinstance(kn[k], (str, dict))
    }
    assert not (ids & dated), f"operational entries leaked into the payload: {sorted(ids & dated)}"


# ── the dataset card ─────────────────────────────────────────────────────────


def test_dataset_card_counts_come_from_the_payload():
    """A hand-typed count disagrees with the data the first time the corpus grows, and a dataset
    whose own card is wrong is worse than one with no card -- a reader cannot tell which half to
    believe."""
    payload = sh.build_payload()
    card = sh.dataset_card(payload)
    assert str(payload["n_rows"]) in card
    assert str(payload["n_verified"]) in card
    assert str(payload["n_rows"] - payload["n_verified"]) in card
    assert payload["sha256"] in card


def test_dataset_card_states_the_unverified_share_up_front():
    """ "Learned from real builds" without the number would be true and materially misleading."""
    payload = sh.build_payload()
    head = sh.dataset_card(payload).split("## What is in here")[0].lower()
    assert "were not" in head or "unverified" in head, "the card buries the confidence split"
    assert "verified" in head


def test_dataset_card_declares_a_license():
    assert "license:" in sh.dataset_card(sh.build_payload()).split("---")[1]


# ── the refusals ─────────────────────────────────────────────────────────────


def test_upload_refuses_without_the_environment_flag(monkeypatch, capsys):
    monkeypatch.delenv("DETERMINEX_CORPUS_SHARE", raising=False)
    monkeypatch.setattr(sys, "argv", ["determinex_corpus_share.py", "--push"])
    assert sh.main() == 1
    assert "REFUSING" in capsys.readouterr().err


def test_upload_refuses_without_a_consent_record(monkeypatch, tmp_path, capsys):
    """A flag alone is not consent: a flag can be set by a script nobody read."""
    monkeypatch.setenv("DETERMINEX_CORPUS_SHARE", "1")
    monkeypatch.setattr(sh, "CONSENT", tmp_path / "absent.json")
    monkeypatch.setattr(sys, "argv", ["determinex_corpus_share.py", "--push"])
    assert sh.main() == 1
    assert "consent" in capsys.readouterr().err.lower()


def test_upload_refuses_without_a_token(monkeypatch, tmp_path, capsys):
    consent = tmp_path / "consent.json"
    consent.write_text(json.dumps({"consented_at": "2026-01-01"}), encoding="utf-8")
    monkeypatch.setenv("DETERMINEX_CORPUS_SHARE", "1")
    monkeypatch.delenv("HF_TOKEN", raising=False)
    monkeypatch.delenv("HUGGINGFACE_TOKEN", raising=False)
    monkeypatch.setattr(sh, "CONSENT", consent)
    monkeypatch.setattr(sys, "argv", ["determinex_corpus_share.py", "--push"])
    assert sh.main() == 1
    assert "HF_TOKEN" in capsys.readouterr().err


#: A leak that ONLY the completeness sweep can see. It must have no pattern in _REDACTIONS, or
#: this test passes through the first gate and silently never exercises the second -- which is
#: what happened: the planted text said "Hetzner", _REDACTIONS covers that, and removing the
#: sweep entirely left the test green. A control that can be satisfied by the wrong mechanism
#: measures nothing.
_SWEEP_ONLY_LEAK = "reproduced by ryang locally"


def test_the_planted_leak_is_invisible_to_the_first_gate():
    """Keeps the test below honest as the pattern lists drift apart over time."""
    assert not sh._residue(_SWEEP_ONLY_LEAK), (
        "_REDACTIONS grew a pattern for the planted leak; the sweep test below is now capable of "
        "passing without the sweep. Pick a different marker."
    )
    assert sh.completeness_sweep(_SWEEP_ONLY_LEAK)


def test_a_leak_blocks_the_upload_before_any_network_call(monkeypatch, tmp_path, capsys):
    """The refusal must happen ahead of consent, token and network -- a payload that should not
    leave must not depend on three later gates all being configured correctly."""
    consent = tmp_path / "consent.json"
    consent.write_text(json.dumps({"consented_at": "2026-01-01"}), encoding="utf-8")
    monkeypatch.setenv("DETERMINEX_CORPUS_SHARE", "1")
    monkeypatch.setenv("HF_TOKEN", "not-used-because-we-refuse-first")
    monkeypatch.setattr(sh, "CONSENT", consent)
    monkeypatch.setattr(
        sh,
        "build_payload",
        lambda: {
            "schema": "x",
            "generated_at": "now",
            "n_rows": 1,
            "n_verified": 0,
            "by_source": {},
            "sha256": "x",
            "rows": [{"id": "r", "fix": _SWEEP_ONLY_LEAK}],
        },
    )
    monkeypatch.setattr(sys, "argv", ["determinex_corpus_share.py", "--push"])
    assert sh.main() == 1
    err = capsys.readouterr().err
    assert "REFUSING" in err
    assert "completeness sweep" in err, "refused, but not by the instrument under test"
