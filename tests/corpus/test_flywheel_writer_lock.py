"""Guards on the flywheel's registry writer and the corpus feedback loop.

`learn_class` was the ONLY caller-facing writer of a verified learned class, and it had no tests
at all -- the mechanism the whole architecture is named for was unguarded. It also had exactly one
caller, `determinex_pb_autodrive`, so the flywheel turned for ProgramBench and for nothing else:
every hive build that failed, was corrected, and then passed the Compiler Oracle produced the
(error, fix) pair this project exists to harvest and discarded it.

`learn_from_failure` opens that path for any build loop. Both write through `_record_learned`, so
the bound, the dedup and the `verified: True` invariant cannot drift between them -- two copies of
a bounded deduping registry update is how one path grows past its limit while the other does not.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "scripts"))

import determinex_pb_amplified_fix as amp  # noqa: E402

from corpus import corpus_feedback as fb  # noqa: E402


def _registry(tmp_path: Path, entries: dict | None = None) -> Path:
    p = tmp_path / "build_knowledge.json"
    p.write_text(json.dumps({"learned_classes": entries or {}}), encoding="utf-8")
    return p


# ── the shared writer ────────────────────────────────────────────────────────


def test_a_verified_pair_is_recorded_once_and_then_counted(tmp_path):
    kp = _registry(tmp_path)
    sym = "error[E0308]: mismatched types, expected u32 found String"
    first = amp.learn_from_failure(sym, "annotate the literal as 0u32", "hive:step_3", kp)
    again = amp.learn_from_failure(sym, "annotate the literal as 0u32", "hive:step_3", kp)

    assert first["learned"] is True
    assert again["learned"] is False, "the same lesson was recorded twice"
    assert again["uses"] == 1, "a repeat should count a use, not duplicate the entry"
    assert len(json.loads(kp.read_text(encoding="utf-8"))["learned_classes"]) == 1


def test_a_lesson_with_no_signal_is_refused(tmp_path):
    """A two-word symptom matches everything, so it would fire on unrelated errors forever."""
    kp = _registry(tmp_path)
    assert amp.learn_from_failure("oops", "do the thing", "hive", kp)["learned"] is False
    assert amp.learn_from_failure("a symptom line long enough to be real", "", "hive", kp) == {
        "learned": False,
        "why": "no-fix",
    }
    assert json.loads(kp.read_text(encoding="utf-8"))["learned_classes"] == {}


def test_both_paths_write_through_the_same_function(tmp_path):
    """If they diverge, the bound and the dedup drift on one path and not the other."""
    kp = _registry(tmp_path)
    amp.learn_from_failure("a generic symptom from any build loop", "the fix", "hive", kp)
    amp.learn_class(
        "sometool",
        "FAILED tests/test_x.py::test_y with a distinctive message",
        "#!/bin/sh\nbuild",
        "#!/bin/sh\nbuild --offline",
        kp,
    )
    entries = json.loads(kp.read_text(encoding="utf-8"))["learned_classes"]
    assert len(entries) == 2
    for e in entries.values():
        assert e["verified"] is True
        assert set(e) >= {"detect", "symptom", "fix", "source_tool", "verified", "learned", "uses"}


def test_the_registry_stays_bounded(tmp_path):
    """Unbounded growth would eventually make the playbook too large to inject anywhere."""
    kp = _registry(tmp_path)
    for i in range(70):
        amp.learn_from_failure(
            f"a distinct symptom number {i} with enough text", f"fix {i}", "hive", kp
        )
    assert len(json.loads(kp.read_text(encoding="utf-8"))["learned_classes"]) <= 60


def test_an_unverified_entry_is_dropped_before_a_verified_one(tmp_path):
    """determinex_pb_absorb also writes here with verified=false. When the bound bites, an
    absorbed prose hint must go before an oracle-confirmed solve -- the proven half is the part
    that cannot be recovered by re-absorbing."""
    seed = {
        f"absorbed_{i}": {
            "detect": f"prose hint {i}",
            "symptom": f"prose hint {i}",
            "fix": "guess",
            "verified": False,
            "learned": "2026-01-01",
            "uses": 0,
        }
        for i in range(59)
    }
    seed["proven_one"] = {
        "detect": "an oracle confirmed symptom",
        "symptom": "an oracle confirmed symptom",
        "fix": "the proven fix",
        "verified": True,
        "learned": "2026-01-01",
        "uses": 0,
    }
    kp = _registry(tmp_path, seed)
    for i in range(6):
        amp.learn_from_failure(f"a brand new distinct symptom {i} here", f"fix {i}", "hive", kp)
    entries = json.loads(kp.read_text(encoding="utf-8"))["learned_classes"]
    assert "proven_one" in entries, "a verified solve was dropped while prose hints survived"


def test_a_missing_registry_is_reported_not_raised(tmp_path):
    """This runs inside a build loop. A telemetry write that raises turns 'we failed to learn'
    into 'the build crashed', which is strictly worse."""
    result = amp.learn_from_failure(
        "a symptom with enough text to count", "fix", "hive", tmp_path / "nope.json"
    )
    assert result["learned"] is False
    assert "kn-read" in result["why"]


# ── the feedback loop ────────────────────────────────────────────────────────


def test_gap_recording_never_raises_and_survives_a_bad_path(monkeypatch, tmp_path):
    """note_gap is called from the query path, so it must never be able to break a query."""
    monkeypatch.setattr(fb, "GAP_LOG", tmp_path / "nested" / "deep" / "gaps.jsonl")
    fb.note_gap("a question", 0, "ask", 0.0)  # must not raise
    assert fb.GAP_LOG.exists()

    monkeypatch.setattr(fb, "GAP_LOG", Path("\x00 invalid"))
    fb.note_gap("another question", 0)  # must still not raise


def test_gaps_rank_by_how_often_a_question_went_unanswered(monkeypatch, tmp_path):
    """A gap hit once is curiosity; a gap hit nine times is a hole with a queue behind it."""
    monkeypatch.setattr(fb, "GAP_LOG", tmp_path / "gaps.jsonl")
    for _ in range(3):
        fb.note_gap("How do I fix the thing?", 0)
    fb.note_gap("something else entirely", 1)
    rows = fb.gaps()
    assert rows[0]["times_asked"] == 3
    # Case and spacing are normalised, or one question becomes several gaps.
    fb.note_gap("how do i fix the thing?", 0)
    assert fb.gaps()[0]["times_asked"] == 4


def test_effect_refuses_to_call_a_winner_on_thin_data():
    """ "grounded prompts pass 8% more often" from n=12 is the kind of number that reaches a
    README and never leaves."""
    rep = fb.effect(wal_root=Path("does-not-exist"))
    assert rep["records_scanned"] == 0
    assert rep["verdict"] == "insufficient data"
    assert "never proof of causation" in rep["caveat"]


def test_effect_reads_grounding_from_the_prompt_not_from_a_flag(tmp_path):
    """A flag records our INTENT to ground. The prompt records what the model actually received,
    and those differ exactly when the injection failed -- the case worth measuring."""
    wal = tmp_path / "run"
    wal.mkdir()
    rows = [
        {"system_prompt": "…KNOWN FAILURE CLASSES…", "outcome": {"compile_ok": True}},
        {"system_prompt": "plain prompt", "outcome": {"compile_ok": False}},
        {"system_prompt": "…WE HAVE SEEN THIS BEFORE…", "outcome": {"compile_ok": True}},
    ]
    (wal / "x.jsonl").write_text(
        "".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8", newline="\n"
    )
    rep = fb.effect(wal_root=tmp_path)
    assert rep["records_scanned"] == 3
    assert rep["arms"]["packets"]["attempts"] == 1
    assert rep["arms"]["matched_fix"]["attempts"] == 1
    assert rep["arms"]["none"]["attempts"] == 1
    assert rep["verdict"] == "insufficient data", "3 records must not produce a verdict"
