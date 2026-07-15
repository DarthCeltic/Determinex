#!/usr/bin/env python3
"""
determinex_repair.py -- the canonical brownfield repair engine
===========================================================
The dual of determinex_build_from_idea: that builds NEW code from a synthesized
oracle; this fixes EXISTING code against its real oracle (its tests/compiler).
Both sit on the same amplifier core -- no second repair engine.

One flow, composing the canonical pieces (nothing reimplemented):

    ingest      determinex_ingest        understand language / oracle / spec
    verify      determinex_oracle        run the real ground truth, collect failures
    adjudicate  determinex_adjudicator   per failure: the move (ROUTE/MATCH/UNBLOCK/...)
    validate    determinex_test_validator is the failing test correct, or slop?
    explain     determinex_explainer     CODE / ENVIRONMENT / TEST + expected/actual/delta
    fix (opt)   determinex_amplified_solve  best-of-K against the SAME oracle

This is what the IDE "Repo Clinic" runs -- the same proven governor + amplifier
as the rest of the system, instead of a separate legacy repair path.

    from determinex_repair import repair_workspace
    r = repair_workspace(Path("repo/"))            # diagnosis only (no model)
    r = repair_workspace(Path("repo/"), generate=model, opt_in=True)  # + amplified fix
"""
from __future__ import annotations

import sys
import tempfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable

_HERE = str(Path(__file__).resolve().parent)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from determinex_adjudicator import Failure, Verdict, classify_failure  # noqa: E402
from determinex_test_validator import TestVerdict, validate_eval_report  # noqa: E402
from determinex_explainer import explain_eval_report  # noqa: E402

GenerateFn = Callable[[str, float], str]


@dataclass
class RepairResult:
    healthy: bool                      # oracle already passes
    language: str
    oracle: str
    n_failures: int
    blame: dict                        # CODE / ENVIRONMENT / TEST counts
    verdicts: dict                     # adjudicator strategy -> count
    proven_slop: int                   # tests the validator proved wrong
    fixed: bool = False                # an amplified fix passed the oracle
    fix_code: str = ""
    notes: list[str] = field(default_factory=list)
    # Per-failure CODE/TEST/ENVIRONMENT explanations (determinex_explainer),
    # serialized via dataclasses.asdict(Explanation) -- the actual "why is this
    # blocked, not just that it's blocked" detail, not just aggregate counts.
    explanations: list[dict] = field(default_factory=list)


def _oracle_for(language: str):
    from determinex_oracle import get_oracle  # lazy: keeps repair importable w/o oracle deps
    return get_oracle(language)


def repair_workspace(workspace: Path, generate: GenerateFn | None = None,
                     opt_in: bool = False, k: int = 6) -> RepairResult:
    """Diagnose (always) and, with opt-in + a model, attempt an amplified fix."""
    from determinex_ingest import ingest
    u = ingest(workspace)
    lang = u.language
    notes: list[str] = list(u.notes)

    # 1. run the real oracle
    try:
        oracle = _oracle_for(lang)
        if not oracle.available():
            return RepairResult(False, lang, "unavailable", 0, {}, {}, 0,
                                notes=notes + [f"oracle toolchain for {lang} not installed"])
        result = oracle.verify(workspace)
    except Exception as e:
        return RepairResult(False, lang, "error", 0, {}, {}, 0,
                            notes=notes + [f"oracle error: {e}"])

    if result.passed:
        return RepairResult(True, lang, oracle.name, 0, {}, {}, 0,
                            notes=notes + ["oracle passes -- nothing to repair"])

    failures: list[Failure] = list(getattr(result, "failures", []) or [])
    n = len(failures)

    # 2. adjudicate + 3. validate (slop) + 4. explain -- all canonical
    from collections import Counter
    verdicts: Counter = Counter()
    blame: Counter = Counter()
    for f in failures:
        a = classify_failure(f)
        verdicts[a.strategy] += 1
        if a.verdict == Verdict.MATCH:
            blame["ENVIRONMENT"] += 1
        elif a.verdict == Verdict.IMPOSSIBLE:
            blame["TEST"] += 1
        else:
            blame["CODE"] += 1

    # slop check + per-failure explanations via a synthetic eval-report shape
    # both the validator and the explainer already accept.
    slop = 0
    explanations: list[dict] = []
    try:
        rep = _failures_as_eval_report(failures)
        for j in validate_eval_report(rep):
            if j.verdict == TestVerdict.SLOP:
                slop += 1
        explanations = [asdict(e) for e in explain_eval_report(rep)]
    except Exception:
        pass

    res = RepairResult(False, lang, oracle.name, n, dict(blame), dict(verdicts),
                       slop, notes=notes, explanations=explanations)

    # 5. optional amplified fix (opt-in + a model), against the SAME oracle
    if opt_in and generate is not None and lang in ("python", "py"):
        res.fixed, res.fix_code = _amplified_python_fix(workspace, generate, k)
        if res.fixed:
            res.notes.append("amplified fix PASSES the oracle (temp-only; not applied)")
    elif opt_in and generate is not None:
        res.notes.append(f"amplified fix path for '{lang}' not yet wired (python only)")
    return res


def _failures_as_eval_report(failures: list[Failure]) -> Path:
    import json
    results = [{"status": "failed", "classname": "", "name": f.name or f.test_id,
                "extra": {"text": f.text}} for f in failures]
    p = Path(tempfile.mkstemp(suffix=".json")[1])
    p.write_text(json.dumps({"test_results": results}), encoding="utf-8")
    return p


def _amplified_python_fix(workspace: Path, generate: GenerateFn, k: int) -> tuple[bool, str]:
    """Amplified solve against the workspace's own pytest oracle. Temp-only."""
    import shutil
    from determinex_verified_search import VerifiedSearch

    class _OR:
        __slots__ = ("passed", "failures")

        def __init__(self, ok, out):
            self.passed = ok
            self.failures = [] if ok else [Failure("oracle", "tests", out[:600])]

    def verify(code: str) -> "_OR":
        with tempfile.TemporaryDirectory() as d:
            dp = Path(d)
            shutil.copytree(workspace, dp / "ws", dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns(".git", "__pycache__", "node_modules"))
            # naive single-file target: overwrite solution.py if present
            target = dp / "ws" / "solution.py"
            if target.exists():
                target.write_text(code, encoding="utf-8")
            else:
                return _OR(False, "no single-file target (solution.py) to amplify")
            # candidate is MODEL-GENERATED (untrusted) -> hardened runner (no network),
            # reusing the existing sandbox; no new module.
            from intake.hardened_runner import run as _hrun
            res = _hrun([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
                        workspace=dp / "ws", cwd=dp / "ws", timeout=60, allow_network=False)
            return _OR(res.exit_code == 0, (res.stdout + res.stderr)[-600:])

    prompt = "Fix the implementation so its tests pass. Return ONLY the corrected module."
    out = VerifiedSearch(verify=verify, k=k, rounds=2).solve(generate, prompt)
    return (out.solved, out.best.text if (out.solved and out.best) else "")


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Determinex brownfield repair (Repo Clinic engine)")
    ap.add_argument("workspace", type=Path)
    args = ap.parse_args()
    r = repair_workspace(args.workspace)
    print(f"=== REPAIR DIAGNOSIS: {args.workspace} ===")
    print(f"language={r.language} oracle={r.oracle} healthy={r.healthy} failures={r.n_failures}")
    if r.n_failures:
        print(f"blame: {r.blame}")
        print(f"moves: {r.verdicts}")
        print(f"proven slop tests: {r.proven_slop}")
        for exp in r.explanations[:10]:
            print()
            head = {"CODE": "FIX THE CODE", "TEST": "THE TEST IS WRONG (proven)",
                    "ENVIRONMENT": "MATCH THE ENVIRONMENT"}.get(exp["responsible"], exp["responsible"])
            print(f"[{exp['responsible']}] {head}  ({exp['test_id']})")
            print(f"  why  : {exp['why']}")
            print(f"  delta: {exp['delta']}")
            if exp.get("proof"):
                print(f"  PROOF: {exp['proof'][:140]}")
    for n in r.notes:
        print(f"  - {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
