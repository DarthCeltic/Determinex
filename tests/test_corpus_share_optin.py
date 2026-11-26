"""Corpus sharing must be off by default, consented explicitly, and redacted provably.

The flywheel's symptom->fix classes are the product's compounding asset and they improve
with more contributors. They are also distilled FROM THE OPERATOR'S SOURCE, which is the one
thing this project exists to keep local. So the upload path gets the same treatment as the
oracle: assume it will be wrong, and make the failure loud.

Three properties, each of which has been a real incident somewhere:

1. **Off by default.** Not "on with an opt-out". A default that shares is a default that
   ships someone's proprietary code to a public dataset the first time they run an update.
2. **A flag is not consent.** `DETERMINEX_CORPUS_SHARE=1` can be set by a wrapper script,
   a Dockerfile, or a teammate. A recorded consent file is a deliberate human act.
3. **Redaction is verified after it runs**, not assumed from the pattern list. A redactor
   nobody re-scans has unknown coverage, and unknown coverage on an upload path is the
   entire risk.
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import determinex_corpus_share as CS  # noqa: E402

PLANTED = {
    "anthropic": "sk-ant-api03-" + "A" * 30,
    "openai_proj": "sk-proj-" + "B" * 24,
    "hf": "hf_" + "C" * 36,
    "github": "ghp_" + "D" * 32,
    "aws": "AKIA" + "E" * 16,
    "google": "AIzaSy" + "F" * 33,
    "email": "someone@example.com",
    "ipv4": "10.0.2.15",
    "win_home": r"C:\Users\ryang\Dev\private",
    "linux_home": "/home/ryang/private",
    "mac_home": "/Users/ryang/private",
    "scratch_drive": "T:/determinex-models/weights.gguf",
    # ASSEMBLED AT RUNTIME, not written literally. `scripts/security/secret_scan.py` reads
    # tracked files and correctly refused to publish this repository when the PEM header
    # appeared verbatim here -- a test fixture is still a leakable location, and the scanner
    # cannot know the key is fake. Building it from parts keeps the test honest (the
    # redactor sees the real shape at runtime) without putting the shape in the source.
    #
    # The alternative -- adding this file to the scanner's exclude list -- is the failure the
    # corpus records as `scanner_exclusion_outlives_its_premise`: the exclusion survives long
    # after the reason for it does.
    "private_key": (
        "-----BEGIN " + "RSA PRIVATE KEY" + "-----\nabc\n-----END " + "RSA PRIVATE KEY" + "-----"
    ),
}


@pytest.mark.parametrize("name,raw", sorted(PLANTED.items()))
def test_every_planted_secret_is_redacted(name: str, raw: str):
    out = CS.redact(raw)
    assert raw not in out, f"{name} survived redaction verbatim"


def test_no_residue_after_redacting_everything_at_once():
    """The re-scan the uploader itself performs. If this can fail, the uploader refuses."""
    blob = "\n".join(PLANTED.values())
    assert CS._residue(CS.redact(blob)) == []


def test_ordinary_technical_prose_is_not_mangled():
    """Negative control. Over-redaction destroys the classes' usefulness, and a useless
    payload is indistinguishable from no payload."""
    prose = (
        "Ollama defaults num_ctx to 2048 and silently truncates; use /api/show to read "
        "the real context length, then cap it. Verified by A/B with a model unload."
    )
    assert CS.redact(prose) == prose


def test_payload_carries_only_generalized_classes():
    """`per_tool` recipes and `absorbed_sources` provenance are ours, do not generalize, and
    raise the chance of leaking something machine-specific. They must not be in the payload."""
    payload = CS.build_payload()
    assert payload["schema"] == "determinex-corpus-share-v2"
    assert set(payload) == {
        "schema",
        "generated_at",
        "n_rows",
        "n_verified",
        "by_source",
        "sha256",
        "rows",
    }
    rows = payload["rows"]
    assert payload["n_rows"] == len(rows) > 0
    assert payload["n_verified"] == sum(row["verified"] for row in rows)
    assert payload["by_source"] == Counter(row["source"] for row in rows)

    metadata = {"id", "source", "confidence", "verified"}
    fields = {
        "class_pattern": {
            "detect",
            "symptom",
            "fix",
            "rule",
            "measured",
            "scope",
            "trap",
            "applies_to",
            "proven",
        },
        "learned_class": {"detect", "symptom", "fix", "learned", "uses"},
        "engineering_lesson": {
            "lesson",
            "why_it_generalizes",
            "category",
            "source_pattern",
            "used_when",
        },
        "design_knowledge": {
            "lesson",
            "why_it_generalizes",
            "category",
            "used_when",
            "reference",
            "verified_by",
        },
    }
    for row in rows:
        assert metadata <= row.keys()
        assert isinstance(row["verified"], bool)
        assert row.keys() - metadata <= fields[row["source"]]


def test_payload_is_content_addressed():
    """A sha256 over the classes, so a recipient can tell two uploads apart and the operator
    can check what was sent after the fact."""
    a, b = CS.build_payload(), CS.build_payload()
    assert a["sha256"] == b["sha256"], "same corpus must hash the same"
    assert len(a["sha256"]) == 64


def test_upload_refuses_without_the_flag(monkeypatch, capsys):
    monkeypatch.delenv("DETERMINEX_CORPUS_SHARE", raising=False)
    monkeypatch.setattr(sys, "argv", ["x", "--push"])
    assert CS.main() == 1
    assert "off by default" in capsys.readouterr().err


def test_upload_refuses_with_the_flag_but_no_consent(monkeypatch, capsys, tmp_path):
    """The property that makes this more than a checkbox: a flag can be set by a script the
    operator never read. Consent is a separate, deliberate act."""
    monkeypatch.setenv("DETERMINEX_CORPUS_SHARE", "1")
    monkeypatch.setattr(CS, "CONSENT", tmp_path / "absent.json")
    monkeypatch.setattr(sys, "argv", ["x", "--push"])
    assert CS.main() == 1
    assert "no consent record" in capsys.readouterr().err


def test_consent_is_revocable(monkeypatch, tmp_path):
    monkeypatch.setattr(CS, "CONSENT", tmp_path / "consent.json")
    monkeypatch.setattr(sys, "argv", ["x", "--consent"])
    assert CS.main() == 0
    assert CS.consent_record() is not None
    monkeypatch.setattr(sys, "argv", ["x", "--revoke"])
    assert CS.main() == 0
    assert CS.consent_record() is None
