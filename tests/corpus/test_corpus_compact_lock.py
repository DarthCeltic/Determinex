"""Guards on memory-packet compaction and on the builder prompt that consumes it.

WHY A LOCK TEST. The corpus has repeatedly grown artifacts that were loaded by nothing -- a
playbook sat unread for months, canonical_tasks.json was unwired for a week. Prompt grounding is
the same shape of risk and worse: it degrades silently. If `for_prompt()` starts returning [] the
hive keeps building, keeps passing, and simply stops applying anything it ever learned. Nothing
goes red. So the wiring is asserted here, at the seam, rather than trusted.

The quality thresholds are guarded too, because compaction's failure mode is not a crash. Loose
clustering produced a "family" of 102 entries whose carrier text described one specific tool --
a packet asserting that a hundred lessons share a point while quoting a sentence about `chafa`.
That is a confident falsehood injected into every prompt, which is strictly worse than no packet.
"""

from __future__ import annotations

import json
import os
import sys
import types
from pathlib import Path
from typing import Any, cast

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "scripts"))

import determinex_corpus_api as api  # noqa: E402

from corpus import corpus_compact as cc  # noqa: E402

# ── the packets themselves ────────────────────────────────────────────────────


def test_every_packet_names_the_entries_it_replaced():
    """Provenance is the property that separates compaction from lossy summarisation.

    A packet whose sources are unknown cannot be checked against the entries it claims to speak
    for, and an unverifiable summary of verified knowledge discards the only thing that made the
    corpus worth keeping.
    """
    packets = cc.compact()
    assert packets, "compaction produced nothing; the corpus is not empty"
    for p in packets:
        assert p["sources"], f"{p['id']} names no source entries"
        assert p["covers"] == len(p["sources"]), f"{p['id']} covers count disagrees with sources"
        assert p["covers"] >= cc.MIN_FAMILY, f"{p['id']} is below the minimum family size"
        assert p["origins"], f"{p['id']} does not say which corpus file it came from"


def test_no_packet_exceeds_the_carry_budget():
    """Over the cap it is a document, not a packet -- and a prompt cannot carry documents."""
    for p in cc.compact():
        assert len(p["packet"]) <= cc.MAX_PACKET_CHARS, f"{p['id']} is {len(p['packet'])} chars"


#: An ABSOLUTE floor, deliberately not read from the module under test. An earlier version of
#: this file asserted against cc.MIN_CARRIER_COVERAGE and was proved worthless by negative
#: control: setting that constant to 0.0 disabled the rejection AND lowered the test's own bar to
#: match, so the suite stayed green while every quality gate was off. A test that imports its
#: threshold from the code it guards can only ever confirm the code agrees with itself.
_CARRIER_COVERAGE_FLOOR = 0.5


def test_a_packets_carrier_actually_carries_the_shared_lesson():
    """The false-summary guard, asserted on real corpus output rather than a fixture.

    This is the check that rejected the 102-entry family whose carrier text was about one tool.
    A carrier that does not contain the family's shared vocabulary is describing its own case and
    cannot speak for the others -- so the packet asserts something nobody verified, in every
    prompt, which is strictly worse than carrying no packet at all.
    """
    assert cc.MIN_CARRIER_COVERAGE >= _CARRIER_COVERAGE_FLOOR, (
        "MIN_CARRIER_COVERAGE was lowered past the floor at which a packet stops describing its "
        "family; raise it back or justify a new floor here deliberately"
    )
    for p in cc.compact():
        shared = set(p["shared_terms"])
        if not shared:
            continue
        covered = len(cc._tokens(p["packet"]) & shared) / len(shared)
        assert covered >= _CARRIER_COVERAGE_FLOOR, (
            f"{p['id']} quotes text covering only {covered:.0%} of its family's shared terms"
        )


def test_compaction_never_modifies_the_corpus():
    """Compaction is a VIEW. A summary that rewrites its inputs is data loss with a nicer name."""
    before = api.DEFAULT_PATH.stat()
    cc.compact()
    after = api.DEFAULT_PATH.stat()
    assert (before.st_mtime_ns, before.st_size) == (after.st_mtime_ns, after.st_size)


# ── the prompt budget ─────────────────────────────────────────────────────────


def test_for_prompt_respects_its_budget_and_never_truncates_a_lesson():
    """Fewer whole packets, never a severed one -- half a lesson misleads where none would not."""
    whole = {p["packet"] for p in cc.compact()}
    for budget in (200, 700, 1500):
        lines = cc.for_prompt(budget_chars=budget)
        assert sum(len(x) for x in lines) <= budget, f"budget {budget} exceeded"
        for line in lines:
            assert line.startswith("- ")
            assert line[2:] in whole, "a returned line is not a whole packet"


def test_a_smaller_budget_never_returns_more_than_a_larger_one():
    assert len(cc.for_prompt(200)) <= len(cc.for_prompt(1500))


# ── the cache: fast, but never stale ──────────────────────────────────────────


def test_cache_regenerates_when_the_corpus_is_written():
    """The whole requirement is that this GROWS. A cache that serves packets from before the
    flywheel's last lesson defeats the point precisely when the new lesson matters most.

    A first version keyed the cache on a constant name that does not exist; `getattr(..., None)`
    swallowed it and the main corpus silently dropped out of the key. The cache looked correct
    and would never have invalidated. This asserts the behaviour, not the implementation.
    """
    cc.compact()  # prime
    assert cc._CACHE is not None
    first = cc._CACHE[0]

    st = os.stat(api.DEFAULT_PATH)
    os.utime(api.DEFAULT_PATH, (st.st_atime, st.st_mtime + 1))
    try:
        cc.compact()
        assert cc._CACHE is not None
        assert cc._CACHE[0] != first, "a corpus write did not invalidate the packet cache"
    finally:
        os.utime(api.DEFAULT_PATH, (st.st_atime, st.st_mtime))


def test_an_unresolvable_source_disables_the_cache_rather_than_narrowing_it():
    """Fail closed. A missing source must cost speed, never freshness."""
    original = cc._FINGERPRINT_ATTRS
    cc._FINGERPRINT_ATTRS = original + ("NO_SUCH_CONSTANT_ON_THE_API",)
    try:
        assert cc._fingerprint() is None
    finally:
        cc._FINGERPRINT_ATTRS = original
    assert cc._fingerprint() is not None, "the real source list must resolve"


def test_every_named_fingerprint_source_exists_on_the_api():
    """Catches the exact typo class that broke this once: a name that quietly resolves to None."""
    for name in cc._FINGERPRINT_ATTRS:
        assert getattr(api, name, None) is not None, f"{name} is not a real corpus API path"


# ── the seam that matters: does the Builder actually receive it ───────────────


def _stub_session_and_step():
    """The minimum surface `_build_builder_messages` actually reads.

    Deliberately a stub rather than a real ManifestSession: constructing one drags in a session
    directory, a manifest and a workspace, and this asserts a property of the PROMPT. A fixture
    heavy enough to be skipped when the environment is imperfect would guard nothing.
    """
    S = types.SimpleNamespace
    session = S(lang="python", correctness_test_harness=None, cargo_toml=None, md_spec_path=None)
    step = S(
        id="s1",
        instruction="write a function",
        write_mode="create",
        target_file="a.py",
        dsl_context=None,
    )
    return cast(Any, session), cast(Any, step)


def test_the_builder_prompt_actually_carries_accumulated_knowledge():
    """The regression guard for the wiring itself.

    Everything else here can pass while the hive is prompted with nothing -- that was the state
    for the project's whole history, with the ProgramBench fixer grounded in class_patterns while
    the component that GENERATES the code got none of it. This asserts the string arrives in the
    message the model is actually sent.
    """
    from hive import prompt_builder as pb

    session, step = _stub_session_and_step()
    msgs = pb._build_builder_messages(session, step, _ROOT)
    system = "\n".join(m.get("content", "") for m in msgs if m.get("role") == "system")

    assert "KNOWN FAILURE CLASSES" in system, "the builder prompt lost its corpus grounding"
    packets = cc.for_prompt(budget_chars=700)
    assert packets, "compaction returned nothing to ground the prompt with"
    assert packets[0][2:] in system, "the densest packet did not reach the prompt"


def test_a_broken_corpus_can_never_break_a_build(monkeypatch):
    """Best-effort is load-bearing. A knowledge layer that can fail a build is worse than none,
    so a corpus that throws must degrade to an unground prompt rather than an exception.
    """
    from hive import prompt_builder as pb

    def _explode(*_a, **_k):
        raise RuntimeError("corpus is on fire")

    monkeypatch.setattr(cc, "for_prompt", _explode)
    session, step = _stub_session_and_step()
    msgs = pb._build_builder_messages(session, step, _ROOT)  # must not raise
    system = "\n".join(m.get("content", "") for m in msgs if m.get("role") == "system")
    assert system, "a corpus failure emptied the builder prompt"
    assert "KNOWN FAILURE CLASSES" not in system


def test_packets_are_json_serializable_for_the_ide_surface():
    json.dumps(cc.compact())
