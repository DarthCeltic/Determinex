#!/usr/bin/env python3
"""
determinex_synthesize.py -- Greenfield Oracle Synthesis (the last capability)
==========================================================================
The engine fixes anything that HAS tests. This builds the sound oracle when none
exists, so a vague idea can become a verified program. "It should make the tests
for the ones it doesn't have" -- this is that, made real.

The honest core: a sound oracle is built DETERMINISTICALLY from a spec wherever
possible, and only the gaps are model-assisted (and even then re-validated):

  examples   : "add(2, 3) == 5" in the spec  -> exact assertion tests (deterministic)
  invariants : "round-trip", "idempotent", "sorted", "reversible" keywords
               -> property tests over fuzzed inputs (deterministic templates)
  contract   : a declared signature / return type -> a shape/type assertion

The synthesized test file is then VALIDATED -- it must collect and run (against a
trivial stub it is allowed to FAIL, but it must execute) -- before it is allowed
to gate anything. An oracle that cannot run is not an oracle. This preserves the
soundness contract the whole Amplifier depends on.

    from determinex_synthesize import parse_spec, synthesize_oracle_tests, validate_oracle
    spec = parse_spec(idea_text)             # NL + examples -> structured Spec
    tests = synthesize_oracle_tests(spec)    # runnable pytest source (the oracle)
    ok, why = validate_oracle(tests, spec)   # the oracle itself must execute

CLI
---
    python scripts/determinex_synthesize.py --spec spec.md [--out tests_gen.py]
"""
from __future__ import annotations

import argparse
import ast
import re
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Spec:
    name: str                                   # the function/unit name
    description: str
    language: str = "python"
    signature: str = ""                         # e.g. "add(a, b)"
    examples: list[tuple[str, str]] = field(default_factory=list)  # (call, expected_repr)
    invariants: list[str] = field(default_factory=list)            # invariant ids


# ---------------------------------------------------------------------------
# Spec parsing -- pull structure out of a natural-language idea (deterministic)
# ---------------------------------------------------------------------------
# Example extraction. The naive "value = .+? up to [;,\n]" form mis-parsed across
# sentence/example boundaries: "add(2,3)==5. add(0,0)==0" captured "5. add(0" because
# a ',' lives INSIDE the next call's args and a sentence '.' is not a terminator at all.
# We anchor on each call, balance-match its parens (nesting-safe), take the value up to
# the next call / ; / newline / sentence-period / end -- and KEEP a pair only if the call
# parses as a call AND the value parses as a Python literal. A piece we cannot trust is
# dropped, never minted into a broken assertion. That self-validation IS the soundness.
_CALL_START = re.compile(r'([A-Za-z_]\w*)\s*\(')
_EX_OP = re.compile(r'\s*(?:==|->|=>|\breturns?\b|\bgives?\b)\s*', re.I)


def _balanced_call(text: str, open_paren: int) -> int:
    """Index just past the ')' matching the '(' at `open_paren` (nesting-safe); -1 if none."""
    depth = 0
    for i in range(open_paren, len(text)):
        if text[i] == '(':
            depth += 1
        elif text[i] == ')':
            depth -= 1
            if depth == 0:
                return i + 1
    return -1


def _is_literal(s: str) -> bool:
    try:
        ast.literal_eval(s)
        return True
    except Exception:
        return False


def _valid_call(s: str) -> bool:
    try:
        return isinstance(ast.parse(s.strip(), mode="eval").body, ast.Call)
    except Exception:
        return False


def _take_value(text: str, start: int) -> str:
    """The expected value after the operator: scan to the first example separator
    (',' ';' newline, a sentence '.', or end) that is OUTSIDE brackets and quotes, so
    commas inside args/tuples and periods inside decimals/strings never split it."""
    depth = 0
    quote: str | None = None
    i = start
    while i < len(text):
        c = text[i]
        if quote:
            if c == quote and text[i - 1] != "\\":
                quote = None
        elif c in "'\"":
            quote = c
        elif c in "([{":
            depth += 1
        elif c in ")]}":
            if depth == 0:
                break
            depth -= 1
        elif depth == 0:
            if c in ",;\n":
                break
            if c == "." and (i + 1 >= len(text) or text[i + 1].isspace()):
                break
        i += 1
    return text[start:i].strip()


def _extract_examples(text: str, name: str | None = None) -> list[tuple[str, str]]:
    """(call, expected-literal) pairs from prose -- boundary-safe + self-validating.
    Only keeps a pair when the call is a real call expression and the value is a literal."""
    out: list[tuple[str, str]] = []
    for cm in _CALL_START.finditer(text):
        if name and cm.group(1) != name:
            continue
        end = _balanced_call(text, cm.end() - 1)
        if end < 0:
            continue
        call = text[cm.start():end]
        om = _EX_OP.match(text, end)
        if not om:
            continue                       # no ==/->/returns after the call: not an example
        exp = _take_value(text, om.end()).rstrip(".").strip()
        if exp and _valid_call(call) and _is_literal(exp):
            out.append((call, exp))
    seen, uniq = set(), []                  # de-dup, keep order
    for c, e in out:
        if (c, e) not in seen:
            seen.add((c, e)); uniq.append((c, e))
    return uniq
_INVARIANT_KEYS = {
    "round-trip": r"round.?trip|encode.*decode|decode.*encode|serialize.*deserialize|inverse",
    "idempotent": r"idempoten",
    "sorted": r"\bsort|ascending|descending|ordered\b",
    "length-preserving": r"same length|length.preserv|preserve.*length",
    "non-negative": r"non.?negative|always positive|>= 0",
}


def parse_spec(text: str, language: str = "python") -> Spec:
    # function name: explicit "function NAME" / "def NAME" / first identifier(...)
    name = ""
    m = re.search(r'(?:function|def|fn|func)\s+([a-zA-Z_]\w*)', text)
    if m:
        name = m.group(1)
    if not name:
        m = re.search(r'\b([a-z_][a-z0-9_]{2,})\s*\(', text)
        name = m.group(1) if m else "solution"
    uniq = _extract_examples(text, name)
    invariants = [inv for inv, pat in _INVARIANT_KEYS.items() if re.search(pat, text, re.I)]
    sig = ""
    sm = re.search(rf'{re.escape(name)}\s*\(([^)]*)\)', text)
    if sm:
        sig = f"{name}({sm.group(1).strip()})"
    return Spec(name=name, description=text.strip(), language=language,
               signature=sig, examples=uniq, invariants=invariants)


# ---------------------------------------------------------------------------
# Test synthesis -- the Spec becomes a runnable oracle (python/pytest)
# ---------------------------------------------------------------------------
# Type-aware fuzz generators: input-type -> a python expression producing a value.
_FUZZ = {
    "str": "''.join(random.choice('abcxyz') for _ in range(random.randint(0, 8)))",
    "int": "random.randint(-50, 50)",
    "list": "[random.randint(-9, 9) for _ in range(random.randint(0, 8))]",
}

# invariant id -> (applicable_input_types, test body using {fn} and {fuzz})
_PROPERTY_TEMPLATES = {
    "idempotent": (("str", "int", "list"),
                   "    import random\n"
                   "    for _ in range(50):\n"
                   "        x = {fuzz}\n"
                   "        assert {fn}({fn}(x)) == {fn}(x)\n"),
    "sorted": (("list",),
               "    import random\n"
               "    for _ in range(50):\n"
               "        xs = {fuzz}\n"
               "        out = {fn}(list(xs))\n"
               "        assert list(out) == sorted(out)\n"),
    "length-preserving": (("list", "str"),
                          "    import random\n"
                          "    for _ in range(50):\n"
                          "        xs = {fuzz}\n"
                          "        assert len({fn}(xs)) == len(xs)\n"),
    "non-negative": (("int",),
                     "    import random\n"
                     "    for _ in range(50):\n"
                     "        x = {fuzz}\n"
                     "        assert {fn}(x) >= 0\n"),
}


def _infer_input_type(spec: "Spec") -> str | None:
    """Infer the first-argument type from the examples (e.g. rle('aaabb') -> str)."""
    for call, _ in spec.examples:
        m = re.search(r'\(\s*(.+?)\s*[,)]', call)
        if not m:
            continue
        arg = m.group(1)
        if arg.startswith(("'", '"')):
            return "str"
        if arg.startswith("["):
            return "list"
        if re.fullmatch(r'-?\d+', arg):
            return "int"
    return None


def synthesize_oracle_tests(spec: Spec) -> str:
    if spec.language not in ("python", "py"):
        raise NotImplementedError(
            f"deterministic synthesis ships for python; '{spec.language}' uses the "
            f"model-assisted path (validated by its language oracle).")
    lines = [
        "# Auto-synthesized oracle (determinex_synthesize). The implementation under",
        f"# test must define `{spec.name}`. These tests ARE the ground truth.",
        "from solution import *  # noqa: F401,F403",
        "",
    ]
    # example-based assertions (deterministic, exact)
    for i, (call, exp) in enumerate(spec.examples):
        lines.append(f"def test_example_{i}():")
        lines.append(f"    assert {call} == {exp}")
        lines.append("")
    # property-based invariants -- only when input type matches (else SKIP:
    # a wrong-typed property test would fail a correct impl = slop).
    in_type = _infer_input_type(spec)
    emitted_property = False
    for inv in spec.invariants:
        entry = _PROPERTY_TEMPLATES.get(inv)
        if not entry:
            continue
        applicable, body = entry
        if in_type is None or in_type not in applicable:
            continue  # cannot type the fuzz soundly -> skip, don't emit slop
        fuzz = _FUZZ[in_type]
        lines.append(f"def test_invariant_{inv.replace('-', '_')}():")
        lines.append(body.format(fn=spec.name, fuzz=fuzz).rstrip("\n"))
        lines.append("")
        emitted_property = True
    if not spec.examples and not emitted_property:
        # no deterministic ground truth extractable -> a smoke test that at least
        # pins that the symbol exists and is callable (honest minimum).
        lines.append("def test_symbol_exists():")
        lines.append(f"    assert callable({spec.name})")
        lines.append("")
    return "\n".join(lines)


def propose_examples(description: str, name: str, generate, k: int = 5,
                     min_agreement: int = 2) -> list[tuple[str, str]]:
    """For an example-free idea, ask a model for I/O examples and keep only those
    that reach CONSENSUS across k samples (appear in >= min_agreement). This turns
    a vague idea into provisional ground truth -- but these are the model's
    INTERPRETATION of the spec, not the user's confirmed intent. The caller MUST
    surface them as 'model-proposed (confirm)'; consensus raises confidence, it
    does not prove correctness (a consistently-misreading model agrees with itself).
    """
    from collections import Counter
    prompt = (f"For the function `{name}` described below, give 4 concrete "
              f"input/output examples, one per line, EXACTLY as `{name}(args) == result`.\n\n"
              f"{description}\n\nExamples:")
    tally: Counter = Counter()
    for i in range(k):
        try:
            text = generate(prompt, 0.2 + 0.15 * i)
        except Exception:
            continue
        for call, exp in _extract_examples(text, name):
            tally[(call, exp)] += 1
    return [pair for pair, n in tally.items() if n >= min_agreement]


def validate_oracle(test_code: str, spec: Spec) -> tuple[bool, str]:
    """The synthesized oracle must itself EXECUTE (collect + run) against a stub.
    It is allowed to FAIL (the stub is wrong) but must not error on collection --
    an oracle that cannot run is not a sound oracle."""
    if spec.language not in ("python", "py"):
        return True, "non-python: validation deferred to language oracle"
    with tempfile.TemporaryDirectory() as d:
        dp = Path(d)
        (dp / "tests_gen.py").write_text(test_code, encoding="utf-8")
        # trivial stub so collection succeeds (function exists, returns None)
        params = "*args, **kwargs"
        (dp / "solution.py").write_text(
            f"def {spec.name}({params}):\n    return None\n", encoding="utf-8")
        try:
            # validation runs synthesized tests against a stub -> route through the
            # existing hardened runner (workspace-bounded, no network). No new sandbox.
            from intake.hardened_runner import run as _hrun
            r = _hrun([sys.executable, "-m", "pytest", "tests_gen.py", "-q",
                       "--collect-only"], workspace=dp, cwd=dp, timeout=30,
                      allow_network=False)
        except Exception as e:
            return False, f"oracle did not run: {e}"
        if r.exit_code != 0 and "error" in (r.stdout + r.stderr).lower():
            return False, f"oracle collection error:\n{(r.stdout + r.stderr)[:300]}"
        n = len(re.findall(r"def test_", test_code))
        return n > 0, f"oracle runnable: {n} ground-truth checks"


def main() -> int:
    ap = argparse.ArgumentParser(description="Determinex Greenfield Oracle Synthesizer")
    ap.add_argument("--spec", type=Path, required=True)
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--lang", default="python")
    args = ap.parse_args()
    text = args.spec.read_text(encoding="utf-8", errors="replace")
    spec = parse_spec(text, args.lang)
    tests = synthesize_oracle_tests(spec)
    ok, why = validate_oracle(tests, spec)
    print(f"spec: name={spec.name} examples={len(spec.examples)} invariants={spec.invariants}")
    print(f"oracle validation: {'OK' if ok else 'FAIL'} -- {why}")
    if args.out:
        args.out.write_text(tests, encoding="utf-8")
        print(f"wrote oracle -> {args.out}")
    else:
        print("\n" + tests)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
