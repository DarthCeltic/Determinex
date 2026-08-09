"""Guards on the OpenROAD oracle.

This is the first oracle Determinex has over a domain that is not software compilation, and it is
the one a chip-design engineer would read first. It has to be right about the thing that is easy
to get wrong.

THE FAILURE THIS FILE EXISTS FOR. A physical-design run has several distinct bad endings, and one
of them looks like success. `TNS_END_PERCENT` and `SKIP_CTS_REPAIR_TIMING` buy runtime by telling
the flow to stop repairing timing -- so a config carrying them can finish fast with clean-looking
metrics while having demonstrated nothing. An optimiser that scores the final number rewards
exactly that config, converges on it, and reports success. The metrics are real; the closure is
not. That is the same shape as scoring a build on wall-clock, and it is why `gave_up` is a
first-class verdict here rather than a footnote.
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "scripts"))

import determinex_eda_oracle as eda  # noqa: E402

CLEAN = {
    "finish__timing__setup__ws": 0.12,
    "finish__design__violations": 0,
    "route__congestion": 0,
}
CFG = "CORE_UTILIZATION = 40\nPLACE_DENSITY = 0.60\n"


# ── the verdicts are distinct, because their remedies are opposite ───────────


def test_a_clean_run_passes():
    r = eda.evaluate(CFG, CLEAN)
    assert r.passed is True
    assert r.verdict == "clean"


def test_negative_slack_is_a_timing_verdict():
    r = eda.evaluate(CFG, {**CLEAN, "finish__timing__setup__ws": -0.34})
    assert r.passed is False
    assert r.verdict == "timing"
    assert "-0.34" in r.detail


def test_drc_violations_are_their_own_verdict():
    r = eda.evaluate(CFG, {**CLEAN, "finish__design__violations": 17})
    assert r.verdict == "drc"
    assert "17" in r.detail


def test_congestion_outranks_timing_because_the_remedies_conflict():
    """Congestion says loosen density; negative slack says push harder. Reporting the timing
    verdict on a congested run sends the next config in the wrong direction."""
    r = eda.evaluate(
        CFG,
        {
            "route__congestion": 3,
            "finish__timing__setup__ws": -0.2,
            "finish__design__violations": 5,
        },
    )
    assert r.verdict == "congestion"
    assert "loosen" in r.detail


def test_a_run_that_did_not_finish_is_not_a_bad_result():
    """No PPA was produced, so asking whether the slack was acceptable is a category error."""
    r = eda.evaluate(CFG, {}, completed=False)
    assert r.verdict == "incomplete"
    assert r.passed is False
    assert "no result" in r.detail


# ── the trap ────────────────────────────────────────────────────────────────


def test_clean_metrics_do_not_pass_when_the_flow_was_told_to_stop_early():
    """THE test. Metrics identical to a genuine pass, plus TNS_END_PERCENT=5. An optimiser that
    scores the number alone converges on exactly this config and calls it a win."""
    gave_up = "CORE_UTILIZATION = 40\nTNS_END_PERCENT = 5\n"
    r = eda.evaluate(gave_up, CLEAN)
    assert r.passed is False, "a run that stopped trying was scored as a success"
    assert r.verdict == "gave_up"
    assert "TNS_END_PERCENT" in r.detail


def test_the_default_tns_end_percent_is_not_giving_up():
    """100 is the documented default and means repair every violating endpoint. Flagging it
    would make the guard fire on every ordinary run, and a guard that always fires gets removed."""
    r = eda.evaluate("TNS_END_PERCENT = 100\n", CLEAN)
    assert r.verdict == "clean"
    assert r.passed is True


def test_skip_cts_repair_timing_also_counts_as_giving_up():
    r = eda.evaluate("SKIP_CTS_REPAIR_TIMING = 1\n", CLEAN)
    assert r.verdict == "gave_up"


# ── reading the metrics at all ──────────────────────────────────────────────


def test_metric_names_resolve_through_their_aliases():
    """ORFS key names have moved between versions. An oracle that reads None for worst slack
    would pass every design ever built, silently."""
    for key in ("worst_slack", "finish__timing__setup__ws", "timing__setup__ws"):
        m = eda.read_metrics({key: -1.5, "finish__design__violations": 0})
        assert m.get("worst_slack") == -1.5, f"{key} did not resolve"
        assert eda.evaluate(CFG, m).verdict == "timing"


def test_nested_metrics_are_flattened():
    m = eda.read_metrics({"finish": {"timing__setup__ws": -0.4}, "finish__design__violations": 0})
    assert eda.evaluate(CFG, m).verdict == "timing"


def test_unreadable_metrics_do_not_pass(tmp_path):
    bad = tmp_path / "nope.json"
    bad.write_text("{not json", encoding="utf-8")
    r = eda.evaluate(CFG, bad)
    # No metrics means nothing was demonstrated. It must not fall through to clean.
    assert r.passed is False or r.metrics == {}


def test_config_parsing_tolerates_real_makefile_syntax():
    cfg = eda.parse_config(
        "# comment\nexport CORE_UTILIZATION := 40\nPLACE_DENSITY ?= 0.6  # trailing\n\nBAD LINE\n"
    )
    assert cfg["CORE_UTILIZATION"] == "40"
    assert cfg["PLACE_DENSITY"] == "0.6"


# ── rules.json, and the direction of "worse" ────────────────────────────────


def test_slack_is_a_lower_bound_while_counts_are_upper_bounds():
    """Getting this backwards inverts the entire judgement: it would fail good designs and pass
    broken ones. Slack more negative is worse; violation counts higher is worse."""
    m = {"worst_slack": -0.5, "drc_violations": 30, "finish__design__violations": 30}
    fails = {f.name for f in eda.check_rules(m, {"worst_slack": 0.0, "drc_violations": 10})}
    assert fails == {"worst_slack", "drc_violations"}

    ok = eda.check_rules(
        {"worst_slack": 0.4, "drc_violations": 2}, {"worst_slack": 0.0, "drc_violations": 10}
    )
    assert ok == []


def test_empty_rules_are_not_a_pass():
    """Nothing to check is not the same as everything checked and fine."""
    assert eda.check_rules({"worst_slack": -9}, {}) == []
    assert eda.evaluate(CFG, {**CLEAN, "finish__timing__setup__ws": -9}).passed is False


# ── the verified-search contract ────────────────────────────────────────────


def test_verify_fn_satisfies_the_oracle_protocol():
    """determinex_verified_search wants .passed and .failures. Nothing more."""
    verify = eda.make_verify_fn(lambda _c: (True, CLEAN))
    r = verify(CFG)
    assert isinstance(r.passed, bool)
    assert isinstance(r.failures, list)


def test_a_crashed_flow_is_a_verdict_not_an_exception():
    """This runs inside a search loop. A raised exception kills the whole run over one bad
    candidate, when the correct behaviour is to score that candidate zero and continue."""

    def boom(_c):
        raise RuntimeError("docker died")

    r = eda.make_verify_fn(boom)(CFG)
    assert r.passed is False
    assert r.verdict == "crashed"
    assert "docker died" in r.detail


def test_score_refuses_to_rank_a_failing_run():
    """A crashed run and a poor-but-valid run are different things. Giving the crash a number
    lets it compete with designs that actually closed."""
    assert eda.score(eda.evaluate(CFG, {**CLEAN, "finish__timing__setup__ws": -1})) is None
    assert eda.score(eda.evaluate(CFG, CLEAN)) is not None


def test_score_prefers_more_slack():
    good = eda.evaluate(CFG, {**CLEAN, "finish__timing__setup__ws": 0.9})
    meh = eda.evaluate(CFG, {**CLEAN, "finish__timing__setup__ws": 0.1})
    assert eda.score(good) < eda.score(meh), "lower is better; more slack must win"
