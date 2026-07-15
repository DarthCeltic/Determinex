"""
hive/amplifier_bridge.py -- wires the Correctness Amplifier into the hive build loop
====================================================================================
The executor's normal build loop is single-shot-per-attempt: generate once, apply,
validate, retry on fail. This bridge swaps that inner generation for VERIFIED
SEARCH against the SAME Compiler Oracle -- sample K builder candidates at varied
temperature, apply+validate each, keep the first that passes. A weak local builder
(1.5B) thereby converges on steps it could never one-shot, with zero change to the
oracle that judges it.

It is decoupled by design: the executor passes two closures bound to its real
primitives, so this module never imports litellm or knows the builder's internals.

    generate_at_temp(temp: float) -> str            # the real Builder, at temp
    apply_and_validate(code: str) -> (bool, str)     # apply_step_output + validate_project

    result = amplified_build(generate_at_temp, apply_and_validate, k=6, rounds=2)
    if result.passed:
        code = result.code      # the verified-search winner (oracle already PASSED)

Opt-in: the executor calls this only when DETERMINEX_AMPLIFY=1; otherwise behavior is
unchanged. Candidates overwrite the same target file, so sequential sampling needs
no extra workspace isolation -- the winning code is left applied on return.
"""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

# the amplifier lives in scripts/; make it importable from scripts/hive/
_SCRIPTS = str(Path(__file__).resolve().parent.parent)
if _SCRIPTS not in sys.path:
    sys.path.insert(0, _SCRIPTS)
from determinex_verified_search import VerifiedSearch  # noqa: E402
from determinex_adjudicator import Failure  # noqa: E402

GenerateAtTemp = Callable[[float], str]
ApplyValidate = Callable[[str], "tuple[bool, str]"]

# diversity ladder for the K builder samples (deterministic-ish -> exploratory)
_AMP_TEMPS = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]


@dataclass
class AmplifiedBuildResult:
    passed: bool
    code: str
    output: str          # last compiler output (proof on pass, diagnosis on miss)
    samples: int
    next_moves: list[str]


class _OracleResult:
    """Duck-typed to satisfy VerifiedSearch (.passed, .failures)."""
    __slots__ = ("passed", "failures", "output")

    def __init__(self, passed: bool, output: str):
        self.passed = passed
        self.output = output
        self.failures = [] if passed else [
            Failure(test_id="compile", name="compile", text=output[:1500])]


def amplified_build(generate_at_temp: GenerateAtTemp,
                    apply_and_validate: ApplyValidate,
                    k: int | None = None, rounds: int = 2) -> AmplifiedBuildResult:
    """Run verified search over the real Builder + real Compiler Oracle."""
    k = k or env_k()
    last_output = ""

    def generate(_prompt: str, temperature: float) -> str:
        return generate_at_temp(temperature)

    def verify(code: str) -> _OracleResult:
        nonlocal last_output
        passed, output = apply_and_validate(code)
        last_output = output
        return _OracleResult(passed, output)

    vs = VerifiedSearch(verify=verify, k=k, rounds=rounds, temps=_AMP_TEMPS)
    # prompt is unused (generate closes over the executor's real prompt)
    res = vs.solve(generate=generate, prompt="")
    if res.solved and res.best is not None:
        # re-apply the winner so the workspace ends in the passing state
        apply_and_validate(res.best.text)
        return AmplifiedBuildResult(True, res.best.text, last_output,
                                    res.total_samples, [])
    best_code = res.best.text if res.best else ""
    return AmplifiedBuildResult(False, best_code, last_output,
                                res.total_samples, res.next_moves)


def amplify_enabled() -> bool:
    return os.environ.get("DETERMINEX_AMPLIFY", "") in ("1", "true", "yes", "on")


def env_k(default: int = 6) -> int:
    try:
        return max(1, int(os.environ.get("DETERMINEX_AMPLIFY_K", default)))
    except ValueError:
        return default
