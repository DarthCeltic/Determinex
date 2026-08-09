"""Guards on chip-flow config handling and the search driver.

Every test here exists because a dry run against Dinesh Annayya's real RISCduino configs caught
the bug first -- before a single hour of place-and-route was spent. That is the argument for
`--dry-run` being a first-class mode rather than a testing afterthought.

The three:

  1. FORMAT DETECTION READ ONLY THE FIRST LINE. The Tcl and Make patterns are `^`-anchored and
     were searched WITHOUT re.MULTILINE, so `search()` tested only line one. RISCduino's
     config.tcl opens with `set script_dir [file dirname ...]` -- not an `::env` assignment -- so
     detection fell through to the filename, and `loads(text)` has none. A Tcl file was parsed as
     a Makefile: zero assignments, an empty config, every default silently substituted. The
     module's own docstring warns about exactly this failure.

  2. CLOCK PERIOD WAS TUNABLE. The search discovered that relaxing the clock improves slack and
     "optimised" toward a slower chip. The metric got better because the requirement got weaker
     -- TNS_END_PERCENT's trap in different clothes, and obvious to anyone who has closed timing.

  3. THE STUB NEVER FAILED. With every candidate passing, the congestion and timing feedback
     branches never executed. A dry run that always succeeds certifies nothing.
"""

from __future__ import annotations

import random
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "scripts"))

import determinex_eda_config as cfgmod  # noqa: E402
import determinex_eda_drive as drive  # noqa: E402

BASELINE_DIR = _ROOT / "corpus" / "eda" / "riscduino_baseline"
REAL = BASELINE_DIR / "wb_interconnect.config.tcl"


# ── 1. format detection ──────────────────────────────────────────────────────


def test_tcl_is_detected_from_content_with_no_filename():
    """The bug. A real OpenLane config, passed as text, parsed as a Makefile."""
    text = REAL.read_text(encoding="utf-8")
    cfg = cfgmod.loads(text)
    assert cfg.fmt == "tcl", "a Tcl config was detected as Make"
    assert cfg.get("PL_TARGET_DENSITY") == "0.20"
    assert cfg.get("CLOCK_PERIOD") == "10"


def test_detection_survives_a_tcl_preamble_before_the_first_env_assignment():
    """RISCduino's real files open with `set script_dir ...`. Detection must not stop there."""
    text = "set script_dir [file dirname [info script]]\n" * 5 + 'set ::env(FOO) "1"\n'
    assert cfgmod.loads(text).fmt == "tcl"


def test_makefile_content_is_still_detected():
    assert cfgmod.loads("CORE_UTILIZATION = 40\nPLACE_DENSITY = 0.6\n").fmt == "mk"


def test_a_config_that_parses_to_nothing_is_not_silently_empty():
    """An empty result must be distinguishable from a file we could not read."""
    assert cfgmod.loads("# only comments\n\n").entries == {}


# ── 2. the clock is a specification, not a knob ──────────────────────────────


def test_clock_period_is_pinned():
    """A search allowed to relax the clock converges on a slower chip and reports an improvement."""
    spec = cfgmod.TUNABLE["CLOCK_PERIOD"]
    assert spec["lo"] == spec["hi"], "CLOCK_PERIOD is tunable again; the search will game slack"


def test_tns_end_percent_is_pinned():
    """The same trap, in the parameter that made it famous."""
    spec = cfgmod.TUNABLE["TNS_END_PERCENT"]
    assert spec["lo"] == spec["hi"] == 100


def test_the_search_never_proposes_a_pinned_parameter():
    """Pinning in the table is worthless if propose() ignores it."""
    cfg = cfgmod.load(REAL)
    rng = random.Random(0)
    for _ in range(40):
        for name in drive.propose(cfg, rng, feedback="timing"):
            assert cfgmod.TUNABLE[name]["lo"] != cfgmod.TUNABLE[name]["hi"], (
                f"{name} is pinned but was proposed"
            )


def test_proposals_stay_inside_their_documented_bounds():
    """PL_TARGET_DENSITY 0.99 costs an hour of place-and-route to discover what the corpus
    already records: it congests rather than degrading gracefully."""
    cfg = cfgmod.load(REAL)
    rng = random.Random(1)
    for _ in range(60):
        for name, value in drive.propose(cfg, rng, feedback="congestion").items():
            spec = cfgmod.TUNABLE[name]
            assert spec["lo"] <= float(value) <= spec["hi"], f"{name}={value} out of bounds"


# ── 3. the dry run must be able to fail ──────────────────────────────────────


def test_the_dry_runner_reaches_every_verdict_the_feedback_reads():
    """A stub where everything passes cannot exercise the feedback branches, which are the only
    part of the loop worth debugging.

    Asserts the SPECIFIC verdicts propose() branches on -- congestion and timing -- not merely
    that outcomes differ. An earlier version checked "more than one verdict occurred" and was
    proved worthless by negative control: disabling both congestion and timing still left the
    DRC path varying, so the test passed while the two branches it exists to protect were dead.
    """
    run = drive.make_dry_runner(random.Random(5))
    verdicts = set()
    for density in ("0.22", "0.30", "0.45", "0.55", "0.60", "0.70", "0.75", "0.90"):
        _ok, m = run(f'set ::env(CLOCK_PERIOD) "10"\nset ::env(PL_TARGET_DENSITY) "{density}"\n')
        ws = m.get("finish__timing__setup__ws", 0)
        if m.get("route__congestion"):
            verdicts.add("congestion")
        elif m.get("finish__design__violations"):
            verdicts.add("drc")
        elif ws is not None and ws < 0:
            verdicts.add("timing")
        else:
            verdicts.add("clean")

    assert "clean" in verdicts, "nothing ever passes; the model is unsatisfiable"
    for needed in ("congestion", "timing"):
        assert needed in verdicts, (
            f"the dry model never produces '{needed}', so propose()'s {needed} branch is never "
            "exercised and a dry run certifies nothing about it"
        )


# ── surgical edits ───────────────────────────────────────────────────────────


def test_changing_one_setting_changes_exactly_one_line():
    """A config carries hand-written comments and per-block reasoning. A rewrite from a parsed
    dict throws that away and hands the reviewer a diff they cannot read."""
    cfg = cfgmod.load(REAL)
    new = cfg.with_value("PL_TARGET_DENSITY", "0.34")
    a, b = cfg.text.splitlines(), new.text.splitlines()
    assert len(a) == len(b)
    assert sum(1 for x, y in zip(a, b, strict=True) if x != y) == 1
    assert new.get("PL_TARGET_DENSITY") == "0.34"


def test_quoting_style_is_preserved():
    """An unnecessary reformat is noise in a diff a person has to review."""
    braced = cfgmod.loads("set ::env(PL_RESIZER_MAX_SLEW_MARGIN) {1.5}\n")
    assert "{2.0}" in braced.with_value("PL_RESIZER_MAX_SLEW_MARGIN", "2.0").text
    quoted = cfgmod.loads('set ::env(PL_TARGET_DENSITY) "0.2"\n')
    assert '"0.5"' in quoted.with_value("PL_TARGET_DENSITY", "0.5").text


def test_a_missing_setting_is_appended_not_refused():
    """A parameter a block never set is the one most worth trying."""
    cfg = cfgmod.loads('set ::env(CLOCK_PERIOD) "10"\n')
    out = cfg.with_value("GLB_RT_ADJUSTMENT", "0.3")
    assert out.get("GLB_RT_ADJUSTMENT") == "0.3"
    assert out.get("CLOCK_PERIOD") == "10"


def test_comments_and_unrelated_settings_survive():
    cfg = cfgmod.load(REAL)
    new = cfg.with_value("PL_TARGET_DENSITY", "0.44")
    for line in cfg.text.splitlines():
        if line.strip().startswith("#") and line.strip():
            assert line in new.text, "a comment was lost"


# ── the driver reports honestly ──────────────────────────────────────────────


def test_the_hand_tuned_baseline_is_evaluated_as_attempt_zero():
    """Without it, "we found a passing config" is a far weaker claim than "we beat the one they
    shipped" -- and only the second is worth showing anyone."""
    cfg = cfgmod.load(REAL)
    res = drive.drive(cfg, drive.make_dry_runner(random.Random(3)), "wb_interconnect", k=3, seed=3)
    assert res.baseline, "the baseline config was not recorded"
    assert "PL_TARGET_DENSITY" in res.baseline


def test_no_improvement_is_reported_as_a_result_not_hidden():
    """The shipped config was tuned by someone with 15 tapeouts. Failing to beat it is the
    expected outcome and must be said plainly, not papered over."""
    cfg = cfgmod.load(REAL)
    res = drive.drive(cfg, lambda _c: (True, {"finish__timing__setup__ws": -5.0}), "x", k=2, seed=0)
    assert res.best_index is None
    assert "NO candidate beat" in drive.render(res)


def test_one_crashed_candidate_does_not_end_the_search():
    calls = {"n": 0}

    def flaky(_c):
        calls["n"] += 1
        if calls["n"] == 2:
            raise RuntimeError("docker died mid-run")
        return True, {"finish__timing__setup__ws": 0.3, "finish__design__violations": 0}

    cfg = cfgmod.load(REAL)
    res = drive.drive(cfg, flaky, "x", k=4, seed=0)
    assert len(res.attempts) == 4, "the search stopped early on one bad candidate"
    assert any(a.verdict == "crashed" for a in res.attempts)


def test_every_vendored_riscduino_block_parses():
    """These are the real files the demo runs against. One that silently parses to nothing would
    be tuned with entirely default values and the report would look fine."""
    files = sorted(BASELINE_DIR.glob("*.config.tcl"))
    assert len(files) >= 19, f"expected the vendored RISCduino blocks, found {len(files)}"
    for f in files:
        cfg = cfgmod.load(f)
        assert cfg.fmt == "tcl", f"{f.name} detected as {cfg.fmt}"
        assert len(cfg.entries) > 5, f"{f.name} parsed to {len(cfg.entries)} settings"
        assert cfg.get("DESIGN_NAME"), f"{f.name} has no DESIGN_NAME"
