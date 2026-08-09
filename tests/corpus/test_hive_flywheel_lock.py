"""Guards on the hive's flywheel write — what counts as a lesson, and what must never be one.

This is the seam that lets the main build loop learn. It is also the seam that could poison the
corpus: it runs on every successful retry, and whatever it writes gets injected into later prompts
by match_failure. A bad rule here does not fail loudly, it degrades every future build quietly.

So the gates are asserted, not reviewed. The two that matter most are the ones that REFUSE:
a whole-file rewrite is not a transferable lesson, and Determinex's own safety-net repairs must
never be learned as if the model had made them.
"""

from __future__ import annotations

import json
import sys
import types
from pathlib import Path
from typing import Any, cast

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "scripts"))

import determinex_pb_amplified_fix as amp  # noqa: E402
from hive import executor as ex  # noqa: E402

ERROR = "error[E0308]: mismatched types, expected `u32`, found `String` at src/lib.rs:14"


def _session_step(quality: str = "ok"):
    S = types.SimpleNamespace
    return (
        cast(Any, S(lang="rust", session_id="s", project_root=".")),
        cast(Any, S(id=3, quality=quality)),
    )


def _learned(monkeypatch, tmp_path) -> list[tuple]:
    """Capture what would be written, instead of touching the real corpus."""
    calls: list[tuple] = []
    monkeypatch.setattr(
        amp,
        "learn_from_failure",
        lambda sym, fix, src, *a, **k: (calls.append((sym, fix, src)), {"learned": True})[1],
    )
    return calls


def test_a_small_correction_after_a_real_failure_is_learned(monkeypatch, tmp_path):
    calls = _learned(monkeypatch, tmp_path)
    session, step = _session_step()
    out = ex._record_hive_lesson(
        session, step, ERROR, "let x: u32 = String::new();", "let x: u32 = 0u32;", 1
    )
    assert out["learned"] is True
    assert len(calls) == 1
    sym, fix, src = calls[0]
    assert sym == ERROR
    # The FIX is a diff, not the file: that is the whole difference between a lesson and a dump.
    assert "+" in fix and "-" in fix
    assert "String::new" in fix
    assert src.startswith("hive:rust:step3:")


def test_a_whole_file_rewrite_is_refused(monkeypatch, tmp_path):
    """A rewrite transfers to nothing, and stored as a "fix" match_failure would offer one
    project's entire source file as advice on an unrelated error."""
    calls = _learned(monkeypatch, tmp_path)
    session, step = _session_step()
    before = "\n".join(f"let v{i} = {i};" for i in range(200))
    after = "\n".join(f"let w{i} = {i}u32;" for i in range(200))
    out = ex._record_hive_lesson(session, step, ERROR, before, after, 1)
    assert out == {"learned": False, "why": "rewrite-not-lesson"}
    assert calls == []


def test_a_cosmetic_change_is_refused(monkeypatch, tmp_path):
    calls = _learned(monkeypatch, tmp_path)
    session, step = _session_step()
    out = ex._record_hive_lesson(session, step, ERROR, "let x = 1;", "let x = 1; ", 1)
    assert out["learned"] is False
    assert calls == []


def test_determinex_authored_repairs_are_never_learned(monkeypatch, tmp_path):
    """`quality` is set to these when OUR safety nets patched the code -- the E0601 fn-main stub,
    the serde derive. The executor already marks them so Determinex output does not auto-ingest
    into training. Learning them here would launder our scaffolding into the model's lessons
    through a different door.
    """
    for quality in ("inconclusive", "compile_hacked"):
        calls = _learned(monkeypatch, tmp_path)
        session, step = _session_step(quality)
        out = ex._record_hive_lesson(
            session, step, ERROR, "let x: u32 = String::new();", "let x: u32 = 0u32;", 1
        )
        assert out == {"learned": False, "why": f"quality={quality}"}, quality
        assert calls == [], f"a {quality} step was learned from"


def test_the_gate_constants_stay_meaningful():
    """A floor above the ceiling would silently disable learning; a huge ceiling would re-admit
    whole-file rewrites. Asserted because both failures look like "it just never learns"."""
    assert ex._MIN_LESSON_DIFF_CHARS < ex._MAX_LESSON_DIFF_CHARS
    assert ex._MAX_LESSON_DIFF_CHARS <= 2000, "this is a lesson budget, not a file budget"
    assert {"inconclusive", "compile_hacked"} <= set(ex._NOT_TRAINING_ELIGIBLE)


def test_a_corpus_failure_cannot_fail_a_green_build(monkeypatch, tmp_path):
    """The call site wraps this in try/except, and this asserts the contract that makes that
    correct: a knowledge write is allowed to fail, a passing build is not allowed to become a
    failing one because of it."""

    def _explode(*_a, **_k):
        raise RuntimeError("corpus unavailable")

    monkeypatch.setattr(amp, "learn_from_failure", _explode)
    session, step = _session_step()
    try:
        ex._record_hive_lesson(
            session, step, ERROR, "let x: u32 = String::new();", "let x: u32 = 0u32;", 1
        )
    except RuntimeError:
        pass  # the raise is expected HERE; the call site is what must swallow it
    # And the call site does: verified by reading the guard rather than trusting it.
    src = (_ROOT / "scripts" / "hive" / "executor.py").read_text(encoding="utf-8")
    block = src[src.index("_record_hive_lesson(\n                    session") :]
    assert "except Exception:" in block[:400], "the call site no longer guards the write"


def test_end_to_end_write_reaches_the_registry(tmp_path, monkeypatch):
    """The gates are only worth testing if the happy path actually writes something."""
    kp = tmp_path / "kn.json"
    kp.write_text(json.dumps({"learned_classes": {}}), encoding="utf-8")
    monkeypatch.setattr(
        amp,
        "learn_from_failure",
        lambda sym, fix, src: (
            amp.learn_from_failure.__wrapped__(sym, fix, src, kp)
            if hasattr(amp.learn_from_failure, "__wrapped__")
            else amp._record_learned(" ".join(sym.split())[:400], fix, src, kp)
        ),
    )
    session, step = _session_step()
    out = ex._record_hive_lesson(
        session, step, ERROR, "let x: u32 = String::new();", "let x: u32 = 0u32;", 1
    )
    assert out["learned"] is True
    entries = json.loads(kp.read_text(encoding="utf-8"))["learned_classes"]
    assert len(entries) == 1
    entry = next(iter(entries.values()))
    assert entry["verified"] is True
    assert entry["source_tool"].startswith("hive:rust:")
