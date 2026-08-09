#!/usr/bin/env python3
"""determinex_eda_oracle.py -- a sound oracle over an OpenROAD physical-design run.

WHAT THIS IS FOR. A chip-design flow takes a configuration and produces power/performance/area
numbers. That is a search problem where every candidate can be scored objectively, which is
exactly the shape verified search wants -- and unlike every other domain Determinex has entered,
the oracle already exists. OpenROAD-flow-scripts writes the metrics itself and already compares
them against a golden baseline. Nothing has to be synthesized.

NO HDL SUPPORT IS REQUIRED, and that is the point. The artifact generated here is a `config.mk`;
the artifact verified is a metrics report. Determinex has no Verilog oracle and does not need one
for this. RTL generation is the application that would -- and its honest oracle is formal
equivalence, not "it synthesized", because a synthesizable netlist can be functionally wrong.

THE TRAP THIS IS BUILT AROUND. A physical-design run has several distinct bad endings that pull
the same knobs in opposite directions, and one of them looks like success. `TNS_END_PERCENT` and
`SKIP_CTS_REPAIR_TIMING` buy runtime by giving up on timing repair, so a config that finished
fast may have finished fast because it stopped trying. An optimiser that scores the final number
rewards exactly that. So `verify()` refuses to call a run passed when the flow was told to stop
early, and reports "gave up" as its own verdict rather than folding it into "slow" or "failed".

RUNNING A FLOW IS INJECTED, NOT ASSUMED. `verify()` takes a `run_fn`, so the whole loop is
testable without Docker, without a PDK, and without an hour of place-and-route. The default
`run_fn` shells out to ORFS; the tests use a stub. That separation is deliberate: a component
that can only be exercised by a one-hour job is a component nobody exercises.

    python scripts/determinex_eda_oracle.py --metrics path/to/metrics.json
    python scripts/determinex_eda_oracle.py --metrics m.json --rules rules.json
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

_HERE = str(Path(__file__).resolve().parent)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)


@dataclass
class EdaFailure:
    """Duck-types determinex_adjudicator.Failure (.test_id / .name / .text)."""

    test_id: str
    name: str
    text: str = ""


@dataclass
class EdaOracleResult:
    """Duck-types determinex_verified_search.OracleLike (.passed / .failures)."""

    passed: bool
    failures: list[EdaFailure] = field(default_factory=list)
    #: The parsed metrics, so a caller can rank passing candidates against each other. `passed`
    #: is a gate, not a score -- two configs can both meet the rules and one still be better.
    metrics: dict[str, Any] = field(default_factory=dict)
    verdict: str = "unknown"
    detail: str = ""


#: Metric keys, in the several spellings ORFS and METRICS2.1 have used. Read by ALIAS rather than
#: by one exact name because the flow's key names have moved between versions, and an oracle that
#: silently reads None for worst slack would pass every design ever built.
_METRIC_ALIASES: dict[str, tuple[str, ...]] = {
    "worst_slack": ("worst_slack", "finish__timing__setup__ws", "timing__setup__ws", "ws"),
    "tns": ("tns", "finish__timing__setup__tns", "timing__setup__tns"),
    "drc_violations": ("drc_violations", "finish__design__violations", "route__drc_errors", "drc"),
    "area": ("area", "finish__design__instance__area", "design__instance__area"),
    "power": ("power", "finish__power__total", "power__total"),
    "clock_period": ("clock_period", "constraints__clocks__details", "sdc__clk__period"),
    "wirelength": ("wirelength", "route__wirelength", "detailedroute__route__wirelength"),
    "congestion": ("congestion", "route__congestion", "globalroute__congestion__worst"),
}

#: Config settings that trade timing quality for runtime. Their presence is not an error -- they
#: are legitimate during exploration -- but a run that used them has not demonstrated timing
#: closure, and must never be scored as though it had.
_GIVE_UP_SETTINGS: dict[str, Callable[[str], bool]] = {
    "TNS_END_PERCENT": lambda v: _as_float(v) is not None and _as_float(v) < 100,  # type: ignore[operator]
    "SKIP_CTS_REPAIR_TIMING": lambda v: _as_float(v) not in (None, 0.0),
    "SKIP_REPORT_METRICS": lambda v: _as_float(v) not in (None, 0.0),
}


def _as_float(v: Any) -> float | None:
    try:
        return float(str(v).strip())
    except (TypeError, ValueError):
        return None


def read_metrics(source: str | Path | dict) -> dict[str, Any]:
    """Normalise an ORFS metrics blob to the names this module reasons about.

    Accepts a path or an already-parsed dict. Unknown keys are preserved under their original
    names so nothing is lost; the normalised names are added alongside.
    """
    if isinstance(source, dict):
        raw = source
    else:
        try:
            raw = json.loads(Path(source).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}
    if not isinstance(raw, dict):
        return {}

    # ORFS nests per-stage blocks in some versions. Flatten one level so `finish__timing__...`
    # and {"finish": {"timing": ...}} both resolve.
    flat: dict[str, Any] = {}
    for k, v in raw.items():
        if isinstance(v, dict):
            for k2, v2 in v.items():
                flat[f"{k}__{k2}"] = v2
        flat[k] = v

    out: dict[str, Any] = dict(flat)
    for norm, aliases in _METRIC_ALIASES.items():
        for a in aliases:
            if a in flat and flat[a] is not None:
                out[norm] = flat[a]
                break
    return out


def read_rules(source: str | Path | dict | None) -> dict[str, Any]:
    """ORFS `rules.json` -- the tolerances a new run is judged against."""
    if source is None:
        return {}
    if isinstance(source, dict):
        return source
    try:
        data = json.loads(Path(source).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def parse_config(text: str) -> dict[str, str]:
    """The assignments out of a `config.mk`. Tolerant of `=`, `:=`, `?=` and comments."""
    out: dict[str, str] = {}
    for line in (text or "").splitlines():
        line = line.split("#", 1)[0].strip()
        if not line or "=" not in line:
            continue
        name, _, value = line.partition("=")
        name = name.rstrip(":?+").strip()
        if name.startswith("export "):
            name = name[len("export ") :].strip()
        if name:
            out[name] = value.strip()
    return out


def classify(metrics: dict[str, Any], config: dict[str, str], completed: bool) -> tuple[str, str]:
    """The verdict, and why. Distinct endings get distinct names.

    Ordered most-decisive first. A run that did not finish has no PPA to judge, and asking
    whether its slack was acceptable is a category error -- so that case returns before any
    metric is read.
    """
    if not completed:
        return "incomplete", "the flow did not finish; there is no result to judge"

    ws = _as_float(metrics.get("worst_slack"))
    drc = _as_float(metrics.get("drc_violations"))
    cong = _as_float(metrics.get("congestion"))

    if cong is not None and cong > 0:
        return (
            "congestion",
            f"global route reports congestion {cong}; PLACE_DENSITY or "
            "ROUTING_LAYER_ADJUSTMENT is too aggressive -- loosen, do not tighten timing",
        )
    if drc is not None and drc > 0:
        return "drc", f"{int(drc)} DRC violation(s) after detailed routing"
    if ws is not None and ws < 0:
        return "timing", f"negative worst slack {ws}; timing did not close"

    gave_up = [k for k, test in _GIVE_UP_SETTINGS.items() if k in config and test(config[k])]
    if gave_up:
        return (
            "gave_up",
            f"metrics are clean but {', '.join(gave_up)} told the flow to stop early -- "
            "this run has not demonstrated timing closure and must not be scored as if it had",
        )
    return "clean", "completed with no congestion, no DRC violations and non-negative slack"


def check_rules(metrics: dict[str, Any], rules: dict[str, Any]) -> list[EdaFailure]:
    """Compare against ORFS's own tolerances. Empty rules means nothing to check, not a pass."""
    out: list[EdaFailure] = []
    for key, bound in rules.items():
        value = _as_float(metrics.get(key))
        limit = _as_float(bound if not isinstance(bound, dict) else bound.get("value"))
        if value is None or limit is None:
            continue
        # ORFS rules are upper bounds on badness for counts/area, and worst_slack is the
        # exception: more negative is worse, so it is a LOWER bound.
        worse = value < limit if "slack" in key.lower() else value > limit
        if worse:
            out.append(
                EdaFailure(
                    test_id=f"rule:{key}",
                    name=key,
                    text=f"{key} = {value}, golden tolerance {limit}",
                )
            )
    return out


def evaluate(
    config_text: str,
    metrics: str | Path | dict,
    rules: str | Path | dict | None = None,
    completed: bool = True,
) -> EdaOracleResult:
    """Score one finished run. Pure: no subprocess, no Docker -- given the artifacts, decide."""
    m = read_metrics(metrics)
    cfg = parse_config(config_text)
    verdict, detail = classify(m, cfg, completed)

    failures = check_rules(m, read_rules(rules))
    if verdict != "clean":
        failures.insert(0, EdaFailure(test_id=f"flow:{verdict}", name=verdict, text=detail))

    return EdaOracleResult(
        passed=(verdict == "clean" and not failures),
        failures=failures,
        metrics=m,
        verdict=verdict,
        detail=detail,
    )


def make_verify_fn(
    run_fn: Callable[[str], tuple[bool, Any]],
    rules: str | Path | dict | None = None,
) -> Callable[[str], EdaOracleResult]:
    """A `verify(candidate) -> OracleLike` for determinex_verified_search.

    `run_fn` takes a config.mk body and returns (completed, metrics). It is injected so the
    search loop can be exercised against a stub -- a component that can only be run by a
    one-hour place-and-route job is a component that never gets tested.
    """

    def verify(candidate: str) -> EdaOracleResult:
        try:
            completed, metrics = run_fn(candidate)
        except Exception as exc:  # a crashed run is a real outcome, not an exception to leak
            return EdaOracleResult(
                passed=False,
                failures=[EdaFailure(test_id="flow:crashed", name="crashed", text=str(exc)[:400])],
                verdict="crashed",
                detail=str(exc)[:400],
            )
        return evaluate(candidate, metrics or {}, rules, completed=completed)

    return verify


def score(result: EdaOracleResult, weights: dict[str, float] | None = None) -> float | None:
    """A single number for ranking runs that ALL passed. None when the run did not pass.

    Deliberately returns None rather than a bad score for a failing run: a failed run and a
    poor-but-valid run are different things, and collapsing them lets a config that crashed
    compete with one that merely underperformed.
    """
    if not result.passed:
        return None
    w = weights or {"worst_slack": -1.0, "area": 1e-6, "power": 1.0}
    total = 0.0
    for key, weight in w.items():
        v = _as_float(result.metrics.get(key))
        if v is not None:
            total += weight * v
    return round(total, 6)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--metrics", required=True, help="ORFS metrics json from a finished run")
    ap.add_argument("--rules", help="ORFS rules.json to judge against")
    ap.add_argument("--config", help="the config.mk that produced it")
    ap.add_argument("--incomplete", action="store_true", help="the flow did not finish")
    args = ap.parse_args()

    reconf = getattr(sys.stdout, "reconfigure", None)
    if reconf is not None:
        reconf(encoding="utf-8")

    cfg = Path(args.config).read_text(encoding="utf-8") if args.config else ""
    res = evaluate(cfg, args.metrics, args.rules, completed=not args.incomplete)

    print(f"  verdict : {res.verdict}")
    print(f"  passed  : {res.passed}")
    print(f"  why     : {res.detail}")
    for key in ("worst_slack", "tns", "drc_violations", "area", "power", "wirelength"):
        if key in res.metrics:
            print(f"    {key:<16} {res.metrics[key]}")
    if res.failures:
        print(f"  {len(res.failures)} failure(s):")
        for f in res.failures:
            print(f"    [{f.test_id}] {f.text[:110]}")
    s = score(res)
    if s is not None:
        print(f"  score   : {s}")
    return 0 if res.passed else 1


if __name__ == "__main__":
    sys.exit(main())
