#!/usr/bin/env python3
"""
determinex_build_from_idea.py -- describe an idea, get a verified program
======================================================================
The full greenfield loop, end to end, closing the last gap:

    idea (NL + examples)
      -> parse_spec            (determinex_synthesize)
      -> synthesize_oracle      sound tests, VALIDATED to run   (the ground truth)
      -> amplified solve        any model, best-of-K vs that oracle  (determinex_*)
      -> verified program       only returned if the oracle PASSES + proof

Correctness is bounded by the synthesized oracle's soundness -- which is why the
synthesizer emits exact example-assertions + type-checked property tests and
refuses to emit a wrong-typed test. No sound oracle, no claim.

Model-agnostic: pass any `generate(prompt, temperature) -> code`. A local-Ollama
generator is provided so it runs on any machine with a small local model.

    from determinex_build_from_idea import build_from_idea
    result = build_from_idea(idea_text, generate=my_model)
    if result.solved:
        print(result.code)        # a program that PASSES the synthesized tests

CLI
---
    python scripts/determinex_build_from_idea.py --idea idea.md [--model NAME] [--k 8]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

_HERE = str(Path(__file__).resolve().parent)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from determinex_synthesize import parse_spec, synthesize_oracle_tests, validate_oracle  # noqa: E402
from determinex_verified_search import VerifiedSearch  # noqa: E402
from determinex_adjudicator import Failure  # noqa: E402

GenerateFn = Callable[[str, float], str]


@dataclass
class BuildResult:
    solved: bool
    code: str
    oracle_tests: str
    n_checks: int
    samples: int
    proof: str
    next_moves: list[str]
    oracle_proposed: bool = False   # oracle examples were model-proposed (confirm!)


class _OracleResult:
    __slots__ = ("passed", "failures", "output")

    def __init__(self, passed: bool, output: str):
        self.passed = passed
        self.output = output
        self.failures = [] if passed else [Failure("oracle", "tests", output[:800])]


def _strip_fence(text: str) -> str:
    # GREEDY to the LAST fence -- so code containing ``` inside a docstring/comment
    # is not truncated (non-greedy stopped at the first inner fence -> SyntaxError).
    m = re.search(r"```(?:python|py)?[ \t]*\n(.*)\n```", text, re.S)
    if m:
        return m.group(1).strip()
    m = re.search(r"```(?:python|py)?\s*(.+?)```", text, re.S)
    return (m.group(1) if m else text).strip()


def ollama_generator(model: str = "determinex-coder-base-tiny:latest",
                     host: str = "http://localhost:11434") -> GenerateFn:
    def _gen(prompt: str, temperature: float) -> str:
        body = json.dumps({"model": model, "prompt": prompt, "stream": False,
                           "options": {"temperature": temperature, "num_predict": 500}}).encode()
        req = urllib.request.Request(host + "/api/generate", data=body,
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as r:
            return _strip_fence(json.loads(r.read()).get("response", ""))
    return _gen


def build_from_idea(idea_text: str, generate: GenerateFn,
                    language: str = "python", k: int = 8, rounds: int = 2) -> BuildResult:
    spec = parse_spec(idea_text, language)
    proposed = False
    # Vague idea with no examples -> ask the model for consensus examples so we have
    # SOME provisional ground truth (better than a symbol-exists smoke test). These
    # are the model's interpretation -> the result is flagged oracle_proposed.
    if not spec.examples and language in ("python", "py"):
        from determinex_synthesize import propose_examples
        ex = propose_examples(spec.description, spec.name, generate, k=5)
        if ex:
            spec.examples = ex
            proposed = True
    tests = synthesize_oracle_tests(spec)
    ok, why = validate_oracle(tests, spec)
    if not ok:
        return BuildResult(False, "", tests, 0, 0,
                           f"oracle not sound: {why}", ["refine-spec-or-examples"],
                           oracle_proposed=proposed)
    n_checks = len(re.findall(r"def test_", tests))

    def verify(code: str) -> _OracleResult:
        with tempfile.TemporaryDirectory() as d:
            dp = Path(d)
            (dp / "solution.py").write_text(code, encoding="utf-8")
            (dp / "tests_gen.py").write_text(tests, encoding="utf-8")
            # The candidate is MODEL-GENERATED (untrusted) -> run it through the
            # existing hardened runner (workspace-bounded, env-scrubbed, no network),
            # not a raw subprocess. Reuses intake.hardened_runner; no new sandbox.
            try:
                from intake.hardened_runner import run as _hrun
                res = _hrun([sys.executable, "-m", "pytest", "tests_gen.py", "-q",
                            "-p", "no:cacheprovider"], workspace=dp, cwd=dp,
                           timeout=30, allow_network=False)
                return _OracleResult(res.exit_code == 0, (res.stdout + res.stderr)[-800:])
            except Exception as e:
                return _OracleResult(False, f"run error: {e}")

    prompt = (f"Write a complete Python module defining `{spec.name}`.\n\n"
              f"Specification:\n{spec.description}\n\n"
              f"Return ONLY the code in a ```python block. It must satisfy these "
              f"behaviors exactly.")
    res = VerifiedSearch(verify=verify, k=k, rounds=rounds).solve(generate, prompt)
    caveat = (" NOTE: the oracle examples were MODEL-PROPOSED from a vague idea -- "
              "confirm they match your intent." if proposed else "")
    if res.solved and res.best is not None:
        return BuildResult(True, res.best.text, tests, n_checks, res.total_samples,
                           f"program PASSES all {n_checks} synthesized checks "
                           f"(oracle-verified, {res.total_samples} samples).{caveat}",
                           [], oracle_proposed=proposed)
    best = res.best.text if res.best else ""
    return BuildResult(False, best, tests, n_checks, res.total_samples,
                       f"no program passed the {n_checks} checks ({res.total_samples} samples).{caveat}",
                       res.next_moves, oracle_proposed=proposed)


def main() -> int:
    ap = argparse.ArgumentParser(description="Determinex: idea -> verified program")
    ap.add_argument("--idea", type=Path, required=True)
    ap.add_argument("--provider", default="local",
                    help="any registered AI: local/claude/codex/gemini/deepseek/<addon>")
    ap.add_argument("--model", default="")
    ap.add_argument("--lang", default="python")
    ap.add_argument("--k", type=int, default=8)
    args = ap.parse_args()
    idea = args.idea.read_text(encoding="utf-8", errors="replace")
    # any provider in the universal registry plugs in here unchanged
    try:
        from determinex_extensions import load_extensions
        load_extensions()  # host any addons first
        from determinex_providers import get_generator
        gen = get_generator(args.provider, args.model or None)
    except Exception:
        gen = ollama_generator(args.model or "determinex-coder-base-tiny:latest")
    res = build_from_idea(idea, gen, args.lang, k=args.k)
    print(f"=== BUILD FROM IDEA ({args.model}) ===")
    print(f"synthesized oracle: {res.n_checks} checks")
    print(f"result: {'SOLVED' if res.solved else 'not solved'}  samples={res.samples}")
    print(f"proof: {res.proof}")
    if res.solved:
        print("\n--- verified program ---\n" + res.code)
    else:
        print(f"next moves: {res.next_moves}")
    return 0 if res.solved else 1


if __name__ == "__main__":
    sys.exit(main())
