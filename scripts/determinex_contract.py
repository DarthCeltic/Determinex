#!/usr/bin/env python3
"""
determinex_contract.py -- Output Contract Enforcer (Amplifier piece #6)
====================================================================
The well-formedness floor. Before any candidate reaches the (expensive) oracle,
it must satisfy a cheap, deterministic OUTPUT CONTRACT: is it a valid unified
diff? does the JSON parse? does the code parse in its language? is the required
shape present? A weak model emits malformed junk a large fraction of the time;
rejecting that junk in microseconds -- before a Docker eval or compile -- both
saves the oracle and guarantees a well-formed floor for whatever model plugs in.

This is a pre-filter for VerifiedSearch: wrap a model so malformed candidates are
rejected and resampled, never counted as a real attempt.

    from determinex_contract import enforce, patch_contract, json_contract, py_contract
    ok, reason = enforce(candidate, patch_contract)
    guarded = guard(generate, py_contract)     # a model that only emits valid python

Contracts are `Callable[[str], tuple[bool, str]]` -> (well_formed, reason).
"""
from __future__ import annotations

import ast
import json
import re
import sys
from typing import Callable

Contract = Callable[[str], "tuple[bool, str]"]


def patch_contract(text: str) -> tuple[bool, str]:
    """A minimal unified-diff sanity check (does not apply it -- that's the oracle)."""
    if not text.strip():
        return False, "empty patch"
    has_header = bool(re.search(r"^(diff --git|--- |\+\+\+ |@@ )", text, re.M))
    if not has_header:
        return False, "no diff header (--- / +++ / @@ / diff --git)"
    # every hunk line should start with a valid prefix
    for ln in text.splitlines():
        if ln and ln[0] not in " +-@\\d" and not ln.startswith(("diff ", "index ",
                "--- ", "+++ ", "new file", "deleted file", "similarity",
                "rename ", "old mode", "new mode", "Binary ")):
            # tolerate context but flag obviously prose lines mid-patch
            if "@@" in text[:text.find(ln)] and not ln.startswith(("+", "-", " ")):
                return False, f"stray non-hunk line in patch body: {ln[:40]!r}"
    return True, "valid unified diff shape"


def json_contract(text: str) -> tuple[bool, str]:
    t = text.strip()
    # tolerate a fenced block
    m = re.search(r"```(?:json)?\s*(.+?)```", t, re.S)
    if m:
        t = m.group(1).strip()
    try:
        json.loads(t)
        return True, "valid json"
    except Exception as e:
        return False, f"invalid json: {e}"


def py_contract(text: str) -> tuple[bool, str]:
    t = _strip_fence(text)
    try:
        ast.parse(t)
        return True, "valid python syntax"
    except SyntaxError as e:
        return False, f"python syntax error: {e}"


def nonempty_contract(text: str) -> tuple[bool, str]:
    return (bool(text.strip()), "nonempty" if text.strip() else "empty output")


def native_code_contract(text: str) -> tuple[bool, str]:
    """Cheap, language-agnostic sanity floor for compiled languages (C/Rust/Go/C++/Haskell).

    Found 2026-07-02: py_contract (ast.parse -- PYTHON syntax) was being applied
    UNCONDITIONALLY, including to native (--lang c/rust/go/...) candidates. Valid
    C/Rust/Go source essentially never parses as Python, so every real candidate in
    native mode was failing its own contract check and burning resample budget on a
    check that could never pass. Real syntax validation for native code already
    happens downstream (the compiler oracle); this pre-filter only needs to catch
    OBVIOUSLY malformed/truncated/prose output cheaply, not fully parse the language.
    """
    t = _strip_fence(text).strip()
    if not t:
        return False, "empty output"
    if t.count("{") != t.count("}"):
        return False, f"unbalanced braces ({t.count('{')} open vs {t.count('}')} close)"
    if t.count("(") != t.count(")"):
        return False, f"unbalanced parens ({t.count('(')} open vs {t.count(')')} close)"
    # a real source file has at least one brace pair; bare prose/explanation text won't.
    if "{" not in t:
        return False, "no brace-delimited block found (looks like prose, not source)"
    return True, "balanced braces/parens, looks like source"


def regex_contract(pattern: str) -> Contract:
    pat = re.compile(pattern, re.S)
    def _c(text: str) -> tuple[bool, str]:
        return (bool(pat.search(text)), f"matches /{pattern[:30]}/" if pat.search(text)
                else f"missing required pattern /{pattern[:30]}/")
    return _c


def all_of(*contracts: Contract) -> Contract:
    def _c(text: str) -> tuple[bool, str]:
        for c in contracts:
            ok, reason = c(text)
            if not ok:
                return False, reason
        return True, "all contracts satisfied"
    return _c


def _strip_fence(text: str) -> str:
    m = re.search(r"```(?:\w+)?\s*(.+?)```", text, re.S)
    return m.group(1) if m else text


# language -> contract, so the Ingester's detected language picks the floor
LANGUAGE_CONTRACT: dict[str, Contract] = {
    "python": py_contract, "py": py_contract,
    "json": json_contract,
    "patch": patch_contract, "diff": patch_contract,
}


def enforce(text: str, contract: Contract) -> tuple[bool, str]:
    return contract(text)


def guard(generate, contract: Contract, max_retries: int = 5):
    """Wrap a generate(prompt,temp)->str so it only returns contract-valid output,
    resampling on malformed candidates (widening temperature). The wrapper raises
    after max_retries so a broken model cannot loop forever."""
    def _wrapped(prompt: str, temperature: float) -> str:
        last = ""
        for i in range(max_retries):
            t = temperature + 0.1 * i
            last = generate(prompt, t)
            ok, _ = contract(last)
            if ok:
                return last
        # return the last (malformed) -> the oracle will reject; never silently pass
        return last
    return _wrapped


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Determinex Output Contract Enforcer")
    ap.add_argument("kind", choices=["patch", "json", "python", "nonempty"])
    ap.add_argument("file", nargs="?", help="file to check (else stdin)")
    args = ap.parse_args()
    text = open(args.file, encoding="utf-8", errors="replace").read() if args.file else sys.stdin.read()
    contract = {"patch": patch_contract, "json": json_contract,
                "python": py_contract, "nonempty": nonempty_contract}[args.kind]
    ok, reason = contract(text)
    print(f"{'OK' if ok else 'REJECT'}: {reason}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
