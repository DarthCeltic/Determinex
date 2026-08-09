#!/usr/bin/env python3
"""determinex_eda_drive.py -- verified config search over a real chip-design flow.

THE LOOP. Propose a configuration, run the flow, read the metrics, keep what the oracle accepts,
feed the failure back. `P = 1 - (1-p)^K`: with a sound oracle, any generator with p > 0 is driven
toward a passing result by sampling. The oracle here is `determinex_eda_oracle`, which is sound
because OpenROAD writes the metrics itself.

WHAT MAKES THIS DIFFERENT FROM AUTOTUNER. OpenROAD already ships a Ray/Tune hyperparameter search,
so sampling the space is not novel and must not be pitched as such. Two things here are not in
that box:

  * The oracle REFUSES a run that stopped trying. Lowering TNS_END_PERCENT or setting
    SKIP_CTS_REPAIR_TIMING buys runtime by abandoning timing repair, so a scorer that reads the
    final number converges on a config that gave up and calls it a win. That parameter is pinned
    rather than tuned, and the verdict exists rather than being folded into "fast".
  * Failures are DIAGNOSED, not just counted. Congestion and negative slack pull the same knobs
    in opposite directions, so the next proposal is conditioned on which one happened.

DRY RUN IS A FIRST-CLASS MODE, not a testing afterthought. `--dry-run` exercises the entire loop
against a model of the flow's real trade-offs, so the orchestration can be debugged in seconds
instead of hours. A driver whose only execution path takes an hour per iteration is a driver that
gets debugged in production.

    python scripts/determinex_eda_drive.py --config <path> --dry-run -k 12
    python scripts/determinex_eda_drive.py --config <path> --design wb_interconnect -k 8
"""

from __future__ import annotations

import argparse
import json
import random
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

_HERE = str(Path(__file__).resolve().parent)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from determinex_eda_config import TUNABLE, FlowConfig, load, loads  # noqa: E402
from determinex_eda_oracle import EdaOracleResult, evaluate, score  # noqa: E402


@dataclass
class Attempt:
    index: int
    values: dict[str, str]
    verdict: str
    detail: str
    passed: bool
    metrics: dict[str, Any] = field(default_factory=dict)
    score: float | None = None
    seconds: float = 0.0


@dataclass
class DriveResult:
    design: str
    attempts: list[Attempt] = field(default_factory=list)
    best_index: int | None = None
    baseline: dict[str, str] = field(default_factory=dict)
    baseline_score: float | None = None

    @property
    def pass_rate(self) -> float:
        return (
            (sum(1 for a in self.attempts if a.passed) / len(self.attempts))
            if self.attempts
            else 0.0
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "design": self.design,
            "attempts": [asdict(a) for a in self.attempts],
            "best_index": self.best_index,
            "baseline": self.baseline,
            "baseline_score": self.baseline_score,
            "pass_rate": round(self.pass_rate, 3),
        }


# ── proposing configurations ─────────────────────────────────────────────────


def propose(
    base: FlowConfig, rng: random.Random, feedback: str = "", temperature: float = 0.6
) -> dict[str, str]:
    """The next configuration to try.

    Deterministic and explainable rather than model-driven, on purpose: the loop, the oracle and
    the reporting must be trustworthy BEFORE a model is introduced, or a bad result is
    unattributable between the search and the generator. Swapping this for a model call is one
    function, and `feedback` is already the hook it will read.

    The feedback branches encode the corpus's failure classes -- congestion and timing want
    opposite moves, and applying the wrong one wastes a full flow run.
    """
    present = {k: v for k, v in base.as_dict().items() if k in TUNABLE}
    out: dict[str, str] = {}
    for name, current in present.items():
        spec = TUNABLE[name]
        if spec["lo"] == spec["hi"]:  # pinned; TNS_END_PERCENT lives here deliberately
            continue
        try:
            cur = float(current)
        except (TypeError, ValueError):
            continue

        lo, hi = float(spec["lo"]), float(spec["hi"])
        span = (hi - lo) * temperature

        bias = 0.0
        if "congestion" in feedback and name in ("PL_TARGET_DENSITY", "PLACE_DENSITY"):
            bias = -span * 0.5  # congested -> spread out
        elif "congestion" in feedback and name == "GLB_RT_ADJUSTMENT":
            bias = +span * 0.4  # give routing more capacity
        elif "timing" in feedback and name == "CLOCK_PERIOD":
            bias = +span * 0.3  # relax the clock rather than fight it
        elif "timing" in feedback and name in ("PL_TARGET_DENSITY", "PLACE_DENSITY"):
            bias = -span * 0.2  # sparser placement shortens critical nets

        nxt = cur + bias + rng.uniform(-span / 2, span / 2)
        nxt = max(lo, min(hi, nxt))
        out[name] = str(int(round(nxt))) if spec["kind"] == "int" else f"{nxt:.3f}"
    return out


# ── running the flow ─────────────────────────────────────────────────────────


def _find_metrics(run_dir: Path) -> dict[str, Any]:
    """The metrics a finished run produced, wherever this version of the flow put them.

    Searched by several names because ORFS and OpenLane have used different ones and moved them
    between releases. Returning {} when nothing is found is correct and is treated as "no
    result" by the caller -- never as a clean run.
    """
    for pattern in (
        "**/metrics.json",
        "**/metadata.json",
        "**/final_summary_report.csv",
        "**/runs/*/reports/metrics.json",
    ):
        for p in sorted(run_dir.glob(pattern)):
            try:
                if p.suffix == ".json":
                    data = json.loads(p.read_text(encoding="utf-8"))
                    if isinstance(data, dict) and data:
                        return data
            except (OSError, json.JSONDecodeError):
                continue
    return {}


def make_real_runner(flow_dir: Path, design: str, config_path: Path, timeout_s: int = 7200) -> Any:
    """A run_fn that invokes the actual flow. Requires Docker and a built ORFS/OpenLane.

    Writes the candidate to the design's real config path and shells out. Deliberately NOT
    `shell=True`: the command line is fixed and the only variable is a path we control.
    """

    def run(candidate_text: str) -> tuple[bool, dict]:
        config_path.write_text(candidate_text, encoding="utf-8", newline="\n")
        cmd = ["make", f"DESIGN_NAME={design}"] if (flow_dir / "Makefile").exists() else None
        if cmd is None:
            raise RuntimeError(f"no Makefile in {flow_dir}; is the flow built?")
        proc = subprocess.run(
            cmd, cwd=str(flow_dir), capture_output=True, text=True, timeout=timeout_s
        )
        completed = proc.returncode == 0
        return completed, _find_metrics(flow_dir)

    return run


def make_dry_runner(rng: random.Random) -> Any:
    """A model of the flow's real trade-offs, for exercising the loop without an hour per run.

    Encodes what the corpus records: density too high congests instead of degrading gracefully,
    and a tighter clock costs slack. Calibrated to be neither trivially easy nor impossible --
    a stub where everything passes would hide exactly the bugs this mode exists to find.
    """

    def run(candidate_text: str) -> tuple[bool, dict]:
        cfg = loads(candidate_text).as_dict()

        def num(name: str, default: float) -> float:
            try:
                return float(cfg.get(name, default))
            except (TypeError, ValueError):
                return default

        density = num("PL_TARGET_DENSITY", num("PLACE_DENSITY", 0.55))
        clk = num("CLOCK_PERIOD", 10.0)
        # Congestion threshold sits INSIDE the search range on purpose. A stub where every
        # candidate passes cannot exercise the congestion and timing feedback branches, which
        # are the only parts of the loop worth debugging -- and a dry run that always succeeds
        # is a dry run that certifies nothing.
        if density > 0.62:
            return True, {
                "route__congestion": round((density - 0.80) * 50, 2),
                "finish__design__violations": 0,
                "finish__timing__setup__ws": 0.05,
            }
        slack = (clk - 9.6) * 0.45 - (density - 0.34) * 1.6 + rng.uniform(-0.03, 0.03)
        return True, {
            "finish__timing__setup__ws": round(slack, 4),
            "finish__design__violations": 0 if density < 0.58 else int((density - 0.58) * 80),
            "route__congestion": 0,
            "finish__design__instance__area": round(150000 * density, 0),
        }

    return run


# ── the search ───────────────────────────────────────────────────────────────


def drive(
    base_config: FlowConfig,
    run_fn: Any,
    design: str,
    k: int = 8,
    seed: int = 0,
    rules: Any = None,
    on_attempt: Any = None,
) -> DriveResult:
    rng = random.Random(seed)
    res = DriveResult(
        design=design, baseline={k2: v for k2, v in base_config.as_dict().items() if k2 in TUNABLE}
    )

    # The hand-tuned config is attempt zero. Without it there is nothing to beat, and "we found a
    # config that passes" is a far weaker claim than "we found one better than the one shipped".
    base_ok, base_metrics = run_fn(base_config.text)
    base_res = evaluate(base_config.text, base_metrics or {}, rules, completed=base_ok)
    res.baseline_score = score(base_res)

    feedback = ""
    best_score: float | None = res.baseline_score
    for i in range(k):
        started = time.time()
        values = propose(base_config, rng, feedback)
        candidate = base_config.with_values(values)
        try:
            completed, metrics = run_fn(candidate.text)
            out: EdaOracleResult = evaluate(
                candidate.text, metrics or {}, rules, completed=completed
            )
        except Exception as exc:  # one bad candidate must not end the search
            out = EdaOracleResult(passed=False, verdict="crashed", detail=str(exc)[:300])

        s = score(out)
        att = Attempt(
            index=i,
            values=values,
            verdict=out.verdict,
            detail=out.detail,
            passed=out.passed,
            metrics={k2: out.metrics.get(k2) for k2 in ("worst_slack", "drc_violations", "area")},
            score=s,
            seconds=round(time.time() - started, 2),
        )
        res.attempts.append(att)
        if on_attempt:
            on_attempt(att)

        feedback = out.verdict
        if s is not None and (best_score is None or s < best_score):
            best_score, res.best_index = s, i
    return res


def render(res: DriveResult) -> str:
    L = [f"  design: {res.design}", ""]
    base_s = "n/a" if res.baseline_score is None else f"{res.baseline_score:.4f}"
    L.append(f"  baseline (hand-tuned): score {base_s}")
    for k, v in sorted(res.baseline.items()):
        L.append(f"      {k:<28} {v}")
    L.append("")
    L.append(f"  {'#':>3} {'verdict':<11} {'slack':>9} {'score':>10}  changed")
    for a in res.attempts:
        ws = a.metrics.get("worst_slack")
        sc = "-" if a.score is None else f"{a.score:.4f}"
        star = "  <-- best" if res.best_index == a.index else ""
        chg = ", ".join(f"{k}={v}" for k, v in sorted(a.values.items()))[:52]
        L.append(f"  {a.index:>3} {a.verdict:<11} {str(ws):>9} {sc:>10}  {chg}{star}")

    L.append("")
    L.append(
        f"  pass rate p = {res.pass_rate:.2f}   P(>=1 pass | K={len(res.attempts)}) = "
        f"{1 - (1 - res.pass_rate) ** max(1, len(res.attempts)):.4f}"
    )
    if res.best_index is None:
        L.append(
            "  NO candidate beat the hand-tuned baseline. That is a real result, not a bug -- "
            "the shipped config was tuned by someone who knew what they were doing."
        )
    else:
        best = res.attempts[res.best_index]
        L.append(f"  best: attempt {best.index}, score {best.score:.4f} vs baseline {base_s}")
        for k, v in sorted(best.values.items()):
            was = res.baseline.get(k, "-")
            if str(was) != str(v):
                L.append(f"      {k:<28} {was} -> {v}")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--config", required=True, help="baseline config.tcl or config.mk")
    ap.add_argument("--design", default="", help="design/block name")
    ap.add_argument("-k", type=int, default=8, help="candidates to sample")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true", help="model the flow; no Docker needed")
    ap.add_argument("--flow-dir", help="ORFS/OpenLane checkout, for a real run")
    ap.add_argument("--rules", help="rules.json to judge against")
    ap.add_argument("--json", help="write the full result here")
    args = ap.parse_args()

    reconf = getattr(sys.stdout, "reconfigure", None)
    if reconf is not None:
        reconf(encoding="utf-8")

    cfg = load(args.config)
    design = args.design or Path(args.config).stem.replace(".config", "")

    if args.dry_run:
        runner = make_dry_runner(random.Random(args.seed))
        print(
            "  MODE: dry run -- the flow is modelled, not executed. No result here is a "
            "measurement of real silicon.\n"
        )
    else:
        if not args.flow_dir:
            print("  --flow-dir is required for a real run (or pass --dry-run)", file=sys.stderr)
            return 2
        if not shutil.which("docker"):
            print("  docker not found; a real flow run needs it", file=sys.stderr)
            return 2
        runner = make_real_runner(Path(args.flow_dir), design, Path(args.config))
        print(f"  MODE: real flow in {args.flow_dir} -- expect ~10-60 min per candidate.\n")

    res = drive(cfg, runner, design, k=args.k, seed=args.seed, rules=args.rules)
    print(render(res))
    if args.json:
        Path(args.json).write_text(
            json.dumps(res.to_dict(), indent=2), encoding="utf-8", newline="\n"
        )
        print(f"\n  wrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
