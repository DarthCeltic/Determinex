#!/usr/bin/env python3
"""
determinex_verified_search.py -- The Correctness Amplifier (keystone)
==================================================================
"...any LLM, regardless of how good or large or small, can access this system
and work anything, and it be right."

This is the layer that makes that literally true. The Oracle + Adjudicator +
Validator make a STRONG model honest. This makes a WEAK model CORRECT.

The mechanism is not magic, it is arithmetic. A model's per-attempt success on a
step is some probability p. If the answer can be VERIFIED deterministically (and
it can -- that is the Compiler/Universal Oracle), then sampling K diverse
candidates and keeping the one that passes gives system success:

        P(solve) = 1 - (1 - p)^K

    p=0.10, K=30  -> 0.958      p=0.20, K=15 -> 0.965      p=0.05, K=60 -> 0.954

So ANY model with p > 0 is converted toward correctness by verified search. Make
each step small enough (the Decomposer) that p is workable, sample against the
oracle, keep what passes. That is how a 1.5B model -- or a model you have never
heard of -- "works anything and is right."

THE SOUNDNESS CONTRACT (load-bearing): this only yields *correct* output if the
oracle is *sound*. A wrong test makes verified search converge confidently to a
wrong answer. Therefore every oracle passed in here SHOULD be paired with the
Test Validator -- garbage oracle in, confident garbage out. This module refuses
to claim "solved" without a passing OracleResult, and records the proof.

Model-agnostic by construction
------------------------------
The model is just a callable `generate(prompt: str, temperature: float) -> str`.
Local 1.5B, cloud frontier, cloaked, an ensemble -- all plug in identically.
The oracle is just `verify(candidate: str) -> OracleResult`. Nothing here knows
or cares which model produced the candidate. That IS the "any LLM can access
this system" interface.

    from determinex_verified_search import VerifiedSearch
    vs = VerifiedSearch(verify=my_oracle, k=8, rounds=3)
    result = vs.solve(generate=my_model, prompt=task_prompt)
    if result.solved:
        apply(result.best.text)        # carries a passing-oracle proof
"""
from __future__ import annotations

import hashlib
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Protocol

_HERE = str(Path(__file__).resolve().parent)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from determinex_adjudicator import Failure, Verdict, classify_failure  # noqa: E402


# ---------------------------------------------------------------------------
# Minimal oracle contract (matches determinex_oracle.OracleResult duck-style)
# ---------------------------------------------------------------------------
class OracleLike(Protocol):
    passed: bool
    failures: list


# A verify fn takes a candidate string and returns something with .passed + .failures
VerifyFn = Callable[[str], OracleLike]
# A model takes (prompt, temperature) and returns a candidate string
GenerateFn = Callable[[str, float], str]


@dataclass
class Candidate:
    text: str
    passed: bool
    n_failures: int
    temperature: float
    digest: str = ""
    score: float = 0.0   # closeness gradient (e.g. fraction of expected output reproduced)


@dataclass
class SearchResult:
    solved: bool
    best: Candidate | None
    rounds_used: int
    total_samples: int
    proof: str                       # why we believe it is correct (oracle pass)
    escalated: bool = False
    next_moves: list[str] = field(default_factory=list)   # if not solved, the Adjudicator's advice
    history: list[Candidate] = field(default_factory=list)


# default temperature ladder: start deterministic, widen for diversity
_DEFAULT_TEMPS = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()[:16]


class VerifiedSearch:
    """Convert any generator + sound oracle into a correct solver via best-of-K
    verified search with feedback rounds, diversity, loop-breaking, and an
    Adjudicator escalation that refuses to surrender without a reason."""

    def __init__(self, verify: VerifyFn, k: int = 8, rounds: int = 3,
                 temps: list[float] | None = None, adjudicate: bool = True,
                 early_escalate: bool = False):
        self.verify = verify
        self.k = k
        self.rounds = rounds
        self.temps = temps or _DEFAULT_TEMPS
        self.adjudicate = adjudicate
        # EARLY ESCALATE (2026-07-02): when a whole round of k distinct samples scores
        # exactly 0.00, this tier has no traction on the leaf and feedback rounds cannot
        # rescue it (feedback refines a partial; there is no partial). Burn no more
        # rounds -- hand the leaf up the ladder now. Set by the ROUTER for every tier
        # that HAS a next tier; the top tier keeps its full round budget (observed:
        # 7b spent ~15 min exhausting its budget at 0.00 on a station 14b then solved
        # in 2 samples).
        self.early_escalate = early_escalate

    def _temp_for(self, i: int) -> float:
        return self.temps[i] if i < len(self.temps) else self.temps[-1]

    def solve(self, generate: GenerateFn, prompt: str) -> SearchResult:
        history: list[Candidate] = []
        seen: set[str] = set()
        feedback = ""
        best: Candidate | None = None
        total = 0

        import os as _os
        import time as _time
        from concurrent.futures import ThreadPoolExecutor

        # HEARTBEAT (2026-07-02): a station/leaf can legitimately take 30-60+ min on a
        # CPU-bound local model, and with zero output in that window a healthy run is
        # indistinguishable from a hang (we burned hours on exactly that ambiguity).
        # One terse line per sample; DETERMINEX_VS_HEARTBEAT=0 silences it.
        heartbeat = _os.environ.get("DETERMINEX_VS_HEARTBEAT", "1") != "0"
        # CONCURRENCY CAP (2026-07-02): k-way fan-out is right for cloud APIs, but against
        # a single local ollama (1-4 parallel slots) the excess requests just sit in the
        # server queue burning their own timeout budget -- an observed queued call waited
        # 11.7 min then died as "timed out", wasting the sample. Cap in-flight generations
        # (DETERMINEX_VS_MAX_CONCURRENCY); default keeps the historical k-way behavior.
        max_conc = max(1, int(_os.environ.get("DETERMINEX_VS_MAX_CONCURRENCY", str(self.k))))

        for r in range(self.rounds):
            round_prompt = prompt if not feedback else f"{prompt}\n\n{feedback}"
            distinct_this_round = 0
            # The K samples are INDEPENDENT (same prompt, different temperature) -> generate them
            # CONCURRENTLY (bounded by max_conc, see above). Each generate() opens its own
            # connection (thread-safe).
            temps = [self._temp_for(i) for i in range(self.k)]

            def _gen_one(temp, _p=round_prompt):
                t0 = _time.time()
                try:
                    out = generate(_p, temp)
                except Exception as e:  # a model error is not a solve
                    out = f"__generation_error__: {e}"
                return temp, out, _time.time() - t0

            with ThreadPoolExecutor(max_workers=max_conc) as ex:
                batch = list(ex.map(lambda t: _gen_one(t), temps))

            for i, (temp, text, gen_s) in enumerate(batch):
                total += 1
                dg = _digest(text)
                if dg in seen:
                    if heartbeat:
                        print(f"    [vs] r{r+1} s{i+1}/{self.k} t={temp:.1f} "
                              f"gen {gen_s:.0f}s -> duplicate, skipped", flush=True)
                    continue  # loop/duplicate -> skip, preserves diversity
                seen.add(dg)
                distinct_this_round += 1
                v0 = _time.time()
                res = self.verify(text)
                passed = bool(getattr(res, "passed", False))
                nfail = len(getattr(res, "failures", []) or [])
                cand = Candidate(text=text, passed=passed, n_failures=nfail,
                                 temperature=temp, digest=dg,
                                 score=float(getattr(res, "score", 0.0)))
                history.append(cand)
                if heartbeat:
                    print(f"    [vs] r{r+1} s{i+1}/{self.k} t={temp:.1f} "
                          f"gen {gen_s:.0f}s verify {_time.time()-v0:.0f}s -> "
                          f"{'PASS' if passed else f'{nfail} fail'} "
                          f"(score {cand.score:.2f})", flush=True)
                if best is None or _better(cand, best):
                    best = cand
                if passed:
                    # SOLVED: only claim it because a sound oracle passed.
                    return SearchResult(
                        solved=True, best=cand, rounds_used=r + 1,
                        total_samples=total,
                        proof=f"oracle PASSED candidate {dg} (round {r+1}, "
                              f"temp {temp}); 0 failures.",
                        history=history)
            # --- round did not solve: build feedback from the best partial ---
            if distinct_this_round == 0:
                # total loop: model only repeats itself -> escalate now
                return self._escalate(best, history, total, r + 1,
                                      "no distinct candidates (model is looping)")
            if self.early_escalate and best is not None and best.score <= 0.0:
                # zero-signal round: no candidate scored above 0.00 -> this tier can't
                # see the target at all; more rounds of the same model are waste.
                if heartbeat:
                    print(f"    [vs] r{r+1}: zero-signal round (best score 0.00) -> "
                          f"early escalate to next tier", flush=True)
                return self._escalate(best, history, total, r + 1,
                                      "zero-signal round at this tier (early escalate)")
            feedback = self._feedback_from(best)
            # progress check: if best is still all-fail with no improvement, the
            # next round needs a different strategy -> let the loop widen temps,
            # but if we are on the last round, escalate with the Adjudicator's moves.
        return self._escalate(best, history, total, self.rounds, "rounds exhausted")

    def _feedback_from(self, best: Candidate | None) -> str:
        if best is None:
            return "Previous attempts produced no usable candidate. Try a different approach."
        res = self.verify(best.text)
        fails = getattr(res, "failures", []) or []
        lines = ["The previous best attempt FAILED these checks. Fix EACH — your output must "
                 "match EXPECTED exactly (bytes + exit code):"]
        # Budget: carry enough of each failure (incl. the EXPECTED output) to be actionable.
        # 160 chars was sized for compiler errors; reimplementation diffs need the full
        # expected output (hundreds of bytes). Cap per-failure and total to stay sane.
        per, shown, budget = 1100, 0, 9000
        for f in fails[:10]:
            name = getattr(f, "name", "") or getattr(f, "test_id", "?")
            txt = (getattr(f, "text", "") or "")[:per]
            block = f"- {name}:\n{txt}"
            if shown + len(block) > budget:
                break
            lines.append(block)
            shown += len(block)
        return "\n".join(lines)

    def _escalate(self, best: Candidate | None, history: list[Candidate],
                  total: int, rounds: int, reason: str) -> SearchResult:
        # Run the Adjudicator over the best candidate's failures: we are only
        # allowed to "give up" if the failures are genuinely IMPOSSIBLE; otherwise
        # we report the untried moves so the orchestration can re-decompose/route.
        next_moves: list[str] = []
        all_impossible = False
        if best is not None and self.adjudicate:
            res = self.verify(best.text)
            fails = getattr(res, "failures", []) or []
            verdicts = []
            for f in fails:
                ff = f if isinstance(f, Failure) else Failure(
                    test_id=getattr(f, "test_id", "?"),
                    name=getattr(f, "name", "?"),
                    text=getattr(f, "text", "") or "")
                a = classify_failure(ff)
                verdicts.append(a.verdict)
                if a.verdict != Verdict.IMPOSSIBLE:
                    next_moves.append(a.strategy)
            all_impossible = bool(verdicts) and all(v == Verdict.IMPOSSIBLE for v in verdicts)
        return SearchResult(
            solved=False, best=best, rounds_used=rounds, total_samples=total,
            proof=f"not solved ({reason}); "
                  + ("all failures IMPOSSIBLE -> genuine ceiling, human review."
                     if all_impossible else
                     f"REOPENABLE via {sorted(set(next_moves))} -- re-decompose, "
                     f"route to a stronger model, or raise K."),
            escalated=True, next_moves=sorted(set(next_moves)), history=history)


def _better(a: Candidate, b: Candidate) -> bool:
    if a.passed != b.passed:
        return a.passed
    # Prefer the candidate that reproduced MORE of the expected behavior (closeness
    # gradient). Without this, byte-exact pass/fail gives no "getting warmer" signal and
    # the search can stall on a do-nothing candidate that only matches empty/error cases.
    if abs(a.score - b.score) > 1e-9:
        return a.score > b.score
    return a.n_failures < b.n_failures   # tiebreak: fewer failing checks


def expected_solve_probability(p: float, k: int) -> float:
    """The arithmetic that justifies the whole module: P(solve) = 1-(1-p)^K."""
    return 1.0 - (1.0 - p) ** k


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Verified Search -- correctness math")
    ap.add_argument("--p", type=float, default=0.1, help="model per-attempt success")
    ap.add_argument("--k", type=int, default=30, help="candidates per step")
    args = ap.parse_args()
    print(f"A model with per-attempt p={args.p} sampled K={args.k} against a sound "
          f"oracle:\n  P(solve) = 1-(1-{args.p})^{args.k} = "
          f"{expected_solve_probability(args.p, args.k):.4f}")
    print("\nThis is why ANY model with p>0 is converted toward correct by verified "
          "search.\nDecompose until p is workable; sample against the oracle; keep "
          "what passes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
