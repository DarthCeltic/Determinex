#!/usr/bin/env python3
"""determinex_rtl_oracle.py -- formal equivalence as a Determinex oracle.

WHY THIS IS THE STRONGEST ORACLE IN THE PROJECT. Every other oracle here samples. A compiler
proves a program typechecks; a test suite proves behaviour on the vectors somebody wrote. Formal
equivalence proves two designs are functionally identical **over all inputs**. That is a proof,
not evidence, and it is what makes `P = 1 - (1-p)^K` sound rather than merely encouraging: a
transformation that survives is not "probably" behaviour-preserving.

It applies to exactly one situation, and the distinction decides whether any of this works:

    TRANSFORMING RTL THAT ALREADY WORKS  ->  the original IS the reference. Use this.
    GENERATING NEW RTL FROM A SPEC       ->  nothing to be equivalent to. Use determinex_synthesize
                                             and prove stated properties instead, which is
                                             strictly weaker and honest about being weaker.

THE FAILURE THIS MODULE IS BUILT AROUND. `eqy` does not answer one question -- it PARTITIONS the
design into many small equivalence problems and answers each. So a run can come back with 47
partitions proven, 3 unresolved. That design is **not** proven equivalent. It is 94% checked,
which is a different thing and a useless thing: the bug is as likely to live in the 3 as the 47.
An adapter that reports the majority verdict, or that reads "no counterexample found" as success,
would be the exact failure this project exists to prevent -- an oracle that silently passes.

So: PROVEN requires every partition proven and none unresolved. Anything else is UNKNOWN, and
UNKNOWN is a distinct verdict from NOT_EQUIVALENT. "We could not decide" and "we found a
difference" call for opposite responses -- the first needs a better strategy or more time, the
second means the transformation is wrong.

Running eqy is INJECTED, so the loop and the parsing are testable without a toolchain.

    python scripts/determinex_rtl_oracle.py --gold orig.v --gate opt.v --top my_module
    python scripts/determinex_rtl_oracle.py --parse path/to/eqy_outdir
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

_HERE = str(Path(__file__).resolve().parent)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

#: Verdicts. Deliberately four, not two.
PROVEN = "proven_equivalent"
NOT_EQUIV = "not_equivalent"
UNKNOWN = "unknown"
ERROR = "error"


@dataclass
class RtlFailure:
    """Duck-types determinex_adjudicator.Failure (.test_id / .name / .text)."""

    test_id: str
    name: str
    text: str = ""


@dataclass
class RtlOracleResult:
    """Duck-types determinex_verified_search.OracleLike (.passed / .failures)."""

    passed: bool
    failures: list[RtlFailure] = field(default_factory=list)
    verdict: str = UNKNOWN
    detail: str = ""
    partitions_total: int = 0
    partitions_proven: int = 0
    partitions_unresolved: int = 0
    counterexamples: list[str] = field(default_factory=list)

    @property
    def coverage(self) -> float:
        """Fraction of partitions decided. Reported, never used as a pass condition."""
        return (self.partitions_proven / self.partitions_total) if self.partitions_total else 0.0


# ── writing the .eqy job file ────────────────────────────────────────────────


def write_eqy_config(
    gold: Path | str,
    gate: Path | str,
    top: str,
    out: Path | str,
    strategy: str = "sat",
    depth: int = 10,
    extra_options: dict[str, str] | None = None,
) -> str:
    """The `.eqy` job file eqy consumes.

    `strategy` is `sat`, `sby` or `dummy`. **`dummy` is never a default here**: it is a
    placeholder that decides nothing, and an oracle wired to it would return a clean result
    having verified precisely nothing -- the most dangerous possible misconfiguration, because it
    fails in the direction of confidence.
    """
    if strategy == "dummy":
        raise ValueError(
            "strategy 'dummy' decides nothing; an oracle using it would report success having "
            "verified nothing. Use 'sat' or 'sby'."
        )
    opts = {"depth": str(depth)}
    opts.update(extra_options or {})
    opt_lines = "\n".join(f"{k} {v}" for k, v in opts.items())
    cfg = f"""[options]
{opt_lines}

[gold]
read -sv {Path(gold).as_posix()}
prep -top {top}

[gate]
read -sv {Path(gate).as_posix()}
prep -top {top}

[strategy basic]
use {strategy}
depth {depth}
"""
    Path(out).write_text(cfg, encoding="utf-8", newline="\n")
    return cfg


# ── reading what eqy decided ─────────────────────────────────────────────────

#: Partition outcomes, as they appear in eqy's status output. Anything not listed here is
#: treated as UNRESOLVED rather than guessed at -- a status this parser does not recognise is
#: exactly when it must not assume success.
_PROVEN_TOKENS = ("pass", "proven", "equivalent", "unsat")
_FAILED_TOKENS = ("fail", "not equivalent", "counterexample", "sat")
_UNRESOLVED_TOKENS = ("unknown", "timeout", "error", "inconclusive", "skip")


def parse_partition_status(text: str) -> tuple[int, int, int, list[str]]:
    """(total, proven, unresolved, counterexample lines) from eqy status output.

    Line-oriented and tolerant, because eqy's exact formatting varies by version. The tolerance
    is deliberately one-directional: an unparseable line counts as UNRESOLVED, never as proven.
    """
    total = proven = unresolved = 0
    cexs: list[str] = []
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not line or line.startswith(("#", "//")):
            continue
        low = line.lower()
        # A partition verdict line names a partition and a status.
        if not re.search(r"partition|module|cell|\bstatus\b", low):
            continue
        total += 1
        if any(t in low for t in _FAILED_TOKENS) and "unsat" not in low:
            cexs.append(line[:220])
        elif any(t in low for t in _PROVEN_TOKENS):
            proven += 1
        else:
            unresolved += 1
    return total, proven, unresolved, cexs


def _read_status_sources(outdir: Path) -> str:
    """Everything eqy wrote that could carry a verdict.

    Several files are read rather than one, because the status file's name has moved between
    versions and reading a single missing file would yield an empty parse -- which, without this,
    would look like "no failures found".
    """
    chunks: list[str] = []
    for pattern in (
        "status",
        "status.*",
        "*.status",
        "logfile.txt",
        "*.log",
        "PASS",
        "FAIL",
        # Markers this module writes itself. Omitting these made the timeout path silently
        # broken: the runner recorded a timeout, nothing read the file, the parse came back
        # empty, and an undecided run was reported as ERROR -- which routes to "fix your
        # invocation" instead of "the proof did not close".
        "determinex_*",
    ):
        for p in sorted(outdir.glob(pattern)):
            if p.is_file():
                try:
                    chunks.append(p.read_text(encoding="utf-8", errors="replace"))
                except OSError:
                    continue
    return "\n".join(chunks)


def parse_result(outdir: Path | str, returncode: int | None = None) -> RtlOracleResult:
    """Decide PROVEN / NOT_EQUIVALENT / UNKNOWN / ERROR from an eqy output directory.

    The ordering is the whole point. A counterexample means NOT_EQUIVALENT regardless of how many
    other partitions passed. Any unresolved partition means UNKNOWN regardless of how few. PROVEN
    requires a positive count of partitions and zero of everything else -- an empty output
    directory parses to zero partitions, and zero partitions proven is not a proof.
    """
    d = Path(outdir)
    if not d.is_dir():
        return RtlOracleResult(
            passed=False, verdict=ERROR, detail=f"no eqy output directory at {d}"
        )

    text = _read_status_sources(d)
    if not text.strip():
        return RtlOracleResult(
            passed=False,
            verdict=ERROR,
            detail="eqy produced no readable status output; nothing was established",
            failures=[RtlFailure("eqy:no_output", "no_output", "no status files found")],
        )

    total, proven, unresolved, cexs = parse_partition_status(text)

    if cexs:
        return RtlOracleResult(
            passed=False,
            verdict=NOT_EQUIV,
            detail=f"{len(cexs)} partition(s) are NOT equivalent; the transformation changed behaviour",
            partitions_total=total,
            partitions_proven=proven,
            partitions_unresolved=unresolved,
            counterexamples=cexs[:10],
            failures=[
                RtlFailure(f"eqy:cex:{i}", "not_equivalent", c) for i, c in enumerate(cexs[:10])
            ],
        )

    if total == 0:
        return RtlOracleResult(
            passed=False,
            verdict=UNKNOWN,
            detail="no partition verdicts were parsed; eqy ran but decided nothing readable",
            failures=[RtlFailure("eqy:no_partitions", "no_partitions", text[-400:])],
        )

    if unresolved:
        return RtlOracleResult(
            passed=False,
            verdict=UNKNOWN,
            detail=(
                f"{proven}/{total} partitions proven, {unresolved} UNRESOLVED. This is not a "
                f"proof of equivalence -- the difference is as likely to live in the unresolved "
                f"partitions as anywhere else. Raise depth, change strategy, or partition "
                f"differently; do not read this as a pass."
            ),
            partitions_total=total,
            partitions_proven=proven,
            partitions_unresolved=unresolved,
            failures=[
                RtlFailure("eqy:unresolved", "unresolved", f"{unresolved} partition(s) undecided")
            ],
        )

    if returncode not in (None, 0):
        return RtlOracleResult(
            passed=False,
            verdict=UNKNOWN,
            detail=f"every parsed partition passed but eqy exited {returncode}; treating as undecided",
            partitions_total=total,
            partitions_proven=proven,
        )

    return RtlOracleResult(
        passed=True,
        verdict=PROVEN,
        detail=f"all {total} partition(s) proven equivalent over all inputs",
        partitions_total=total,
        partitions_proven=proven,
    )


# ── the oracle ───────────────────────────────────────────────────────────────


def preflight(
    gold: Path | str, gate: Path | str, top: str, workdir: Path | str, jobs: int = 1
) -> RtlOracleResult:
    """Validate the whole pipeline WITHOUT running a solver.

    Uses eqy's `-m/--setup`: it reads both designs, matches signals and builds the partitions,
    then stops. That exercises everything that usually goes wrong first -- a design that will not
    elaborate, a top module name that does not exist, ports that do not match -- for a fraction of
    the cost of a real proof.

    The verdict is deliberately NOT a pass. No partition was decided, so `parse_result` reports
    UNKNOWN, which is the truthful answer: the plumbing works and nothing has been verified.
    """
    work = Path(workdir)
    work.mkdir(parents=True, exist_ok=True)
    cfgp = work / "preflight.eqy"
    outdir = work / "preflight_out"
    try:
        write_eqy_config(gold, gate, top, cfgp)
        rc, produced = _default_runner(cfgp, outdir, jobs=jobs, setup_only=True, timeout_s=600)
    except Exception as exc:
        return RtlOracleResult(
            passed=False,
            verdict=ERROR,
            detail=str(exc)[:400],
            failures=[RtlFailure("eqy:preflight", "preflight", str(exc)[:400])],
        )
    res = parse_result(produced, rc)
    res.detail = f"[preflight, no solver run] {res.detail}"
    return res


def make_verify_fn(
    gold: Path | str,
    top: str,
    workdir: Path | str,
    run_fn: Callable[..., tuple[int, Path]] | None = None,
    strategy: str = "sat",
    depth: int = 10,
    jobs: int = 1,
    timeout_s: int = 3600,
) -> Callable[[str], RtlOracleResult]:
    """A `verify(candidate_rtl) -> OracleLike` for determinex_verified_search.

    The candidate is RTL TEXT -- whatever a model proposed. It is written to disk, checked
    against the unchanged golden reference, and accepted only on a full proof.

    `run_fn(eqy_config, outdir) -> (returncode, outdir)` is injected so the loop and the parsing
    are testable without a Yosys toolchain. The default shells out to `eqy`.
    """
    gold_p = Path(gold)
    work = Path(workdir)
    work.mkdir(parents=True, exist_ok=True)
    runner = run_fn or _default_runner

    def verify(candidate_rtl: str) -> RtlOracleResult:
        gate = work / "gate.v"
        cfgp = work / "job.eqy"
        outdir = work / "job"
        try:
            gate.write_text(candidate_rtl, encoding="utf-8", newline="\n")
            write_eqy_config(gold_p, gate, top, cfgp, strategy=strategy, depth=depth)
            # Injected runners in tests take only (config, outdir); the real one accepts the
            # tuning knobs. Passed positionally-compatible so both shapes work rather than
            # forcing every test double to mirror the production signature.
            if runner is _default_runner:
                rc, produced = runner(cfgp, outdir, jobs=jobs, timeout_s=timeout_s)
            else:
                rc, produced = runner(cfgp, outdir)
        except Exception as exc:  # a broken run is a verdict, not an exception to leak upward
            return RtlOracleResult(
                passed=False,
                verdict=ERROR,
                detail=str(exc)[:400],
                failures=[RtlFailure("eqy:crashed", "crashed", str(exc)[:400])],
            )
        return parse_result(produced, rc)

    return verify


def toolchain_status() -> dict[str, Any]:
    """Which parts of the toolchain are actually present. Costs nothing to ask.

    Reported per tool rather than as one boolean, because the remedies differ and "eqy failed"
    with no further detail sends someone debugging their design when the real problem is that
    yosys is not on PATH.
    """
    out: dict[str, Any] = {}
    for tool, probe in (
        ("eqy", ["eqy", "--help"]),
        ("yosys", ["yosys", "-V"]),
        ("sby", ["sby", "--help"]),
    ):
        exe = shutil.which(tool)
        version = ""
        if exe:
            try:
                p = subprocess.run(probe, capture_output=True, text=True, timeout=30)
                version = (p.stdout or p.stderr or "").strip().splitlines()[0][:80]
            except (OSError, subprocess.SubprocessError):
                version = "present but did not respond"
        out[tool] = {"found": bool(exe), "path": exe or "", "version": version}
    out["ready"] = out["eqy"]["found"] and out["yosys"]["found"]
    return out


#: Flags verified against eqy's own argument parser (YosysHQ/eqy, src/eqy.py):
#:   -f  remove the workdir if it already exists   -d  set the workdir name
#:   -j  allow N parallel make jobs                -m  generate partitions and EXIT
#:   -k  keep going when some targets fail
#: `-m` is what makes a no-solve preflight possible: it builds the partitions and stops before
#: any solver runs, so the whole pipeline can be validated for a fraction of the cost.
def _default_runner(
    config: Path, outdir: Path, jobs: int = 1, setup_only: bool = False, timeout_s: int = 3600
) -> tuple[int, Path]:
    """Invoke eqy. Fixed argv -- no shell; the only variables are paths we wrote.

    Refuses up front when the toolchain is absent, with an actionable message. Without that the
    failure surfaces as a bare FileNotFoundError several layers away, and the obvious next move
    -- debugging the RTL -- is the wrong one.
    """
    if not shutil.which("eqy"):
        raise RuntimeError(
            "eqy is not on PATH. Install YosysHQ's OSS CAD Suite (which bundles yosys, eqy and "
            "sby) or build eqy from https://github.com/YosysHQ/eqy. Nothing was verified."
        )
    if not shutil.which("yosys"):
        raise RuntimeError(
            "yosys is not on PATH; eqy is a front-end for it and cannot run alone. "
            "Nothing was verified."
        )

    cmd = ["eqy", "-f", "-d", str(outdir)]
    if jobs > 1:
        cmd += ["-j", str(jobs)]
    if setup_only:
        # Build partitions and stop before any solver. A cheap structural check, not a proof --
        # parse_result will correctly report UNKNOWN because no partition was decided.
        cmd.append("-m")
    cmd.append(str(config))

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout_s)
    except subprocess.TimeoutExpired:
        # A timeout is UNDECIDED, never a failure of the design. Surfacing it as a crash would
        # send the next attempt at fixing a transformation that may be perfectly correct.
        (outdir / "determinex_timeout").parent.mkdir(parents=True, exist_ok=True)
        (outdir / "determinex_timeout").write_text(
            f"partition timeout status: timeout after {timeout_s}s\n", encoding="utf-8"
        )
        return 1, outdir

    # eqy's own stderr/stdout carries the reason when it fails before writing any status file.
    # Kept alongside the outputs so parse_result can quote it rather than reporting silence.
    try:
        outdir.mkdir(parents=True, exist_ok=True)
        (outdir / "determinex_invocation.log").write_text(
            f"$ {' '.join(cmd)}\nexit={proc.returncode}\n\n"
            f"--- stdout ---\n{proc.stdout or ''}\n--- stderr ---\n{proc.stderr or ''}\n",
            encoding="utf-8",
        )
    except OSError:
        pass
    return proc.returncode, outdir


def explain(result: RtlOracleResult) -> str:
    """What to do next, conditioned on WHICH failure happened.

    Undecided and disproven want opposite responses: the first is a verification-effort problem,
    the second means the transformation itself is wrong. Collapsing them wastes the next attempt.
    """
    if result.verdict == PROVEN:
        return "Accepted. Functionally identical to the reference over all inputs."
    if result.verdict == NOT_EQUIV:
        return (
            "REJECT the transformation. A counterexample exists, so behaviour changed. Do not "
            "raise the depth -- that does not make a real difference go away."
        )
    if result.verdict == UNKNOWN:
        return (
            "UNDECIDED, which is not a failure of the transformation. Raise `depth`, try the "
            "`sby` strategy instead of `sat`, or split the partitions differently. The "
            "transformation may well be correct; the proof did not close."
        )
    return "The run itself failed. Fix the invocation before drawing any conclusion."


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--gold", help="golden reference RTL")
    ap.add_argument("--gate", help="transformed RTL to check")
    ap.add_argument("--top", help="top module name")
    ap.add_argument("--workdir", default="eqy_work")
    ap.add_argument("--strategy", default="sat", choices=("sat", "sby"))
    ap.add_argument("--depth", type=int, default=10)
    ap.add_argument("--parse", help="parse an existing eqy output directory instead of running")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    reconf = getattr(sys.stdout, "reconfigure", None)
    if reconf is not None:
        reconf(encoding="utf-8")

    if args.parse:
        res = parse_result(args.parse)
    else:
        if not (args.gold and args.gate and args.top):
            print("  --gold, --gate and --top are required (or use --parse)", file=sys.stderr)
            return 2
        verify = make_verify_fn(
            args.gold, args.top, args.workdir, strategy=args.strategy, depth=args.depth
        )
        res = verify(Path(args.gate).read_text(encoding="utf-8"))

    if args.json:
        print(
            json.dumps(
                {
                    "verdict": res.verdict,
                    "passed": res.passed,
                    "detail": res.detail,
                    "partitions_total": res.partitions_total,
                    "partitions_proven": res.partitions_proven,
                    "partitions_unresolved": res.partitions_unresolved,
                    "counterexamples": res.counterexamples,
                },
                indent=2,
            )
        )
        return 0 if res.passed else 1

    print(f"  verdict    : {res.verdict}")
    print(f"  passed     : {res.passed}")
    print(
        f"  partitions : {res.partitions_proven}/{res.partitions_total} proven, "
        f"{res.partitions_unresolved} unresolved"
    )
    print(f"  why        : {res.detail}")
    for c in res.counterexamples[:5]:
        print(f"    cex: {c}")
    print(f"  next       : {explain(res)}")
    return 0 if res.passed else 1


if __name__ == "__main__":
    sys.exit(main())
