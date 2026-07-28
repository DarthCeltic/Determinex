"""Per-language identifier-leak regression net for Project Cloak.

tests/test_cloak_smoke.py has 11 tests and every one is Python-only. Cloak's whole claim is
whole-repo obfuscation across 10 languages before source reaches a cloud LLM, so the nine
NON-Python languages -- the ones the privacy moat actually depends on -- had no leak assertion
behind them at all. Nothing failed loudly if a grammar stopped matching a declaration form,
or was never installed in the first place.

What this file pinned when first written, measured 2026-07-26 (before the fix in this same
commit series):

  * ACTUALLY AST-covered (tree-sitter grammar installed and its query compiles):
        go, javascript, rust   (only 3 of 9 -- pyproject's [cloak] extra declared just these)
  * Advertised by TS_SUPPORTED_LANGUAGES but NO grammar installed:
        c, cpp, java, php, ruby, typescript
  * NEITHER a working grammar NOR a regex fallback:  typescript  -- silent plaintext leak

Fixed same day: the 6 missing grammars were installed (pip install tree-sitter-{typescript,
java,ruby,php,c,cpp}), and every language's query was missing parameter/field/local captures
entirely -- not a per-language quirk, a systematic gap in every _QUERIES entry. Both fixed.
Current state: 8 of 9 languages obfuscate their fixture completely. javascript is the one
remaining gap, and it is a structural one, not a missing-grammar one -- see _KNOWN_GAPS.

TS_SUPPORTED_LANGUAGES is a hardcoded frozenset of 9, not a probe of what loads, so printing
it "verifies" nothing -- that was the original audit's mistake. test_advertised_languages_are_
actually_loadable is the standing guard against that gap reopening silently.

Fixtures deliberately use zzq-prefixed names: nonsense to any safe-list, so anything surviving
into the output is a genuine leak and not a stdlib/framework keep-list hit.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import determinex_cloak_treesitter as ts_mod  # noqa: E402
from determinex_cloak import (  # noqa: E402
    CloakObfuscationError,
    _build_cloak_context_nonpython,
    obfuscate_source,
)
from determinex_cloak._treesitter_bridge import TS_SUPPORTED_LANGUAGES  # noqa: E402
from determinex_cloak.lang_extractor import _LANG_DEF_PATTERNS  # noqa: E402

# language -> (filename, source, identifiers that MUST NOT survive obfuscation)
#
# Go is the one language where case is semantic: the extractor deliberately skips
# uppercase/exported names as public API, so the Go fixture uses unexported names only.
# Using exported names here would report a designed behavior as a leak.
CASES: dict[str, tuple[str, str, list[str]]] = {
    "rust": (
        "lib.rs",
        "pub struct ZzqRec { pub zzq_field: i64 }\n"
        "pub fn zzq_fn(zzq_param: &ZzqRec) -> i64 {\n"
        "    let zzq_local = zzq_param.zzq_field;\n"
        "    zzq_local\n"
        "}\n",
        ["ZzqRec", "zzq_field", "zzq_fn", "zzq_param", "zzq_local"],
    ),
    "go": (
        "m.go",
        "package main\n"
        "type zzqRec struct { zzqField int64 }\n"
        "func zzqFn(zzqParam zzqRec) int64 { zzqLocal := zzqParam.zzqField; return zzqLocal }\n",
        ["zzqRec", "zzqField", "zzqFn", "zzqParam", "zzqLocal"],
    ),
    "javascript": (
        "a.js",
        "class ZzqRec { constructor() { this.zzqField = 0; } }\n"
        "function zzqFn(zzqParam) { const zzqLocal = zzqParam.zzqField; return zzqLocal; }\n",
        ["ZzqRec", "zzqField", "zzqFn", "zzqParam", "zzqLocal"],
    ),
    "typescript": (
        "a.ts",
        "class ZzqRec { zzqField: number = 0; }\n"
        "function zzqFn(zzqParam: ZzqRec): number { const zzqLocal = zzqParam.zzqField; "
        "return zzqLocal; }\n",
        ["ZzqRec", "zzqField", "zzqFn", "zzqParam", "zzqLocal"],
    ),
    "java": (
        "A.java",
        "public class ZzqRec {\n"
        "  private long zzqField;\n"
        "  public long zzqFn(long zzqParam) { long zzqLocal = zzqParam; return zzqLocal; }\n"
        "}\n",
        ["ZzqRec", "zzqField", "zzqFn", "zzqParam", "zzqLocal"],
    ),
    "c": (
        "a.c",
        "struct ZzqRec { long zzq_field; };\n"
        "long zzq_fn(struct ZzqRec *zzq_param) {\n"
        "    long zzq_local = zzq_param->zzq_field;\n"
        "    return zzq_local;\n"
        "}\n",
        ["ZzqRec", "zzq_field", "zzq_fn", "zzq_param", "zzq_local"],
    ),
    "cpp": (
        "a.cpp",
        "class ZzqRec { public: long zzqField; };\n"
        "long zzqFn(ZzqRec* zzqParam) { long zzqLocal = zzqParam->zzqField; return zzqLocal; }\n",
        ["ZzqRec", "zzqField", "zzqFn", "zzqParam", "zzqLocal"],
    ),
    "ruby": (
        "a.rb",
        "class ZzqRec\n"
        "  def zzq_fn(zzq_param)\n"
        "    zzq_local = zzq_param\n"
        "    zzq_local\n"
        "  end\n"
        "end\n",
        ["ZzqRec", "zzq_fn", "zzq_param", "zzq_local"],
    ),
    "php": (
        "a.php",
        "<?php\nclass ZzqRec { public $zzqField = 0;\n"
        "  function zzqFn($zzqParam) { $zzqLocal = $zzqParam; return $zzqLocal; } }\n",
        ["ZzqRec", "zzqField", "zzqFn", "zzqParam", "zzqLocal"],
    ),
}

# Languages whose grammar genuinely loads AND whose query compiles right now.
_AST_REAL = sorted(
    lang for lang in TS_SUPPORTED_LANGUAGES if ts_mod._load_language_obj(lang) is not None
)


def _cloak(tmp_path: Path, language: str) -> tuple[str | None, list[str]]:
    """Run the documented public path.

    Returns (output, leaked). A CloakObfuscationError is SAFE, not a failure: refusing to
    produce output is the fail-closed behavior, and nothing reaches an API. It is reported as
    (None, []) so the leak assertions below treat a refusal as clean.
    """
    filename, source, declared = CASES[language]
    (tmp_path / filename).write_text(source, encoding="utf-8")
    try:
        ctx = _build_cloak_context_nonpython(f"t-{language}", tmp_path, language)
        out = obfuscate_source(source, ctx.symbol_map)
    except CloakObfuscationError:
        return None, []
    return out, [name for name in declared if name in out]


# Known, MEASURED coverage gaps. xfail(strict=True) rather than a weakened fixture: the
# assertion stays honest, CI stays green, and the moment a gap is actually closed the test
# XPASSes and forces this list to be updated. Never soften a fixture to make one of these pass.
#
# 2026-07-26: all 9 tree-sitter grammars installed (were 3 of 9), plus parameter/field/local
# query captures added for every one of them. 8 of 9 languages are now a clean fixture pass.
# javascript is the one remaining gap, and it is NOT a missing-grammar problem -- the grammar
# and query both work; the leak is structural (see reason below).
_KNOWN_GAPS: dict[str, str] = {
    "javascript": (
        "`this.zzqField = 0` is a member_expression assignment, not a field_definition. "
        "Capturing (member_expression property: ...) would also rewrite external API property "
        "access (res.status, JSON.parse), so it needs a safe-list-aware rule, not a raw query."
    ),
}


def test_advertised_languages_are_actually_loadable():
    """TS_SUPPORTED_LANGUAGES is a hardcoded list, so it CAN advertise grammars that are not
    installed -- and callers gate on it (`lang in TS_SUPPORTED_LANGUAGES`) to decide whether
    AST extraction applies. When they disagree, a language silently drops to regex (or to
    nothing at all) while still reporting as covered. Green now that all 9 are installed; if
    this ever regresses (a fresh environment, a dependency removed), it should fail loudly.
    """
    advertised = set(TS_SUPPORTED_LANGUAGES)
    loadable = set(_AST_REAL)
    missing = sorted(advertised - loadable)
    assert not missing, (
        f"advertised as tree-sitter-covered but no grammar installed: {missing}. "
        f"pyproject.toml [cloak] declares only rust/go/python/javascript. "
        f"Install: pip install " + " ".join(f"tree-sitter-{m}" for m in missing)
    )


def test_every_advertised_language_has_some_extraction_path():
    """A language with neither a working grammar nor a regex fallback extracts NOTHING, so
    obfuscation is an identity function and the file goes to the cloud API in plaintext."""
    uncovered = sorted(
        lang for lang in TS_SUPPORTED_LANGUAGES
        if lang not in _AST_REAL and lang not in _LANG_DEF_PATTERNS
    )
    assert not uncovered, (
        f"advertised languages with NO extraction path at all (silent plaintext "
        f"passthrough): {uncovered}"
    )


@pytest.mark.parametrize(
    "language",
    [
        pytest.param(
            lang,
            marks=pytest.mark.xfail(strict=True, reason=_KNOWN_GAPS[lang]),
        ) if lang in _KNOWN_GAPS else lang
        for lang in sorted(CASES)
    ],
)
def test_no_declared_identifier_survives_obfuscation(tmp_path, language):
    """The core privacy assertion, per language: every identifier the fixture DECLARES must be
    absent from the obfuscated output. Green for go/rust/typescript; the rest are xfail with a
    measured reason in _KNOWN_GAPS."""
    _, leaked = _cloak(tmp_path, language)
    assert not leaked, f"{language}: identifiers leaked in plaintext: {leaked}"


@pytest.mark.parametrize("language", _AST_REAL)
def test_ast_covered_languages_extract_something(tmp_path, language):
    """Narrower guard that stays green even where full coverage is still incomplete: a language
    with a working grammar must extract SOMETHING. Zero means the query stopped matching."""
    if language not in CASES:
        pytest.skip(f"no fixture for {language}")
    filename, source, _ = CASES[language]
    (tmp_path / filename).write_text(source, encoding="utf-8")
    ctx = _build_cloak_context_nonpython(f"t-{language}", tmp_path, language)
    assert ctx.symbol_map.forward, (
        f"{language}: grammar loads but extracted 0 identifiers -- query no longer matches"
    )


@pytest.mark.parametrize("language", sorted(CASES))
def test_obfuscation_is_not_an_identity_function(tmp_path, language):
    """The single most dangerous silent failure: extraction yields nothing, obfuscate_source
    returns the input unchanged, and the caller ships plaintext believing it is cloaked.

    A refusal (out is None) passes -- that IS the fail-closed path. Only a successful return of
    the untouched input is a defect, because that is indistinguishable from real obfuscation to
    every caller.
    """
    out, _ = _cloak(tmp_path, language)
    if out is None:
        return  # failed closed -- nothing was emitted, nothing can leak
    _, source, _ = CASES[language]
    assert out.strip() != source.strip(), (
        f"{language}: obfuscated output is byte-identical to the input -- nothing was cloaked"
    )


@pytest.fixture()
def _force_zero_extraction(monkeypatch):
    """Simulate "no extraction path" for a language that DOES have one today.

    All 9 languages now extract something for real (2026-07-26), so there is no longer a
    naturally-uncovered language to point this test at -- and pinning it to one that happens to
    still be broken would make the test fragile (it'd need rewriting the next time a gap
    closes, same as the _KNOWN_GAPS entries do). Instead this monkeypatches BOTH extraction
    paths to empty, which exercises the guard's actual trigger condition directly: real files
    scanned, zero identifiers found, regardless of why.
    """
    import determinex_cloak.lang_extractor as lx

    monkeypatch.setattr(lx, "extract_treesitter_identifiers", lambda *a, **k: frozenset())
    monkeypatch.setattr(lx, "_extract_lang_identifiers", lambda *a, **k: frozenset())
    return lx


def test_uncovered_language_fails_closed_instead_of_passing_plaintext(tmp_path, _force_zero_extraction):
    """The guard added 2026-07-26 in _build_cloak_context_nonpython.

    Before it, a language with no extraction path produced an EMPTY symbol map, obfuscate_source
    returned the input verbatim, and the agent loop shipped proprietary source to a cloud LLM
    believing Cloak had run. TypeScript was in exactly that state at the time this was written
    (since fixed -- see the module docstring). Cloak's documented invariant is 'NO plaintext
    source ever reaches a cloud LLM API call', so extracting nothing from real source files must
    raise, not return.
    """
    (tmp_path / "lib.rs").write_text(
        "pub struct ZzqRec { pub zzq_field: i64 }\n", encoding="utf-8"
    )
    with pytest.raises(CloakObfuscationError) as exc:
        _build_cloak_context_nonpython("t", tmp_path, "rust")
    assert "rust" in str(exc.value)


def test_empty_repo_does_not_trip_the_fail_closed_guard(tmp_path, _force_zero_extraction):
    """Zero identifiers because there were zero FILES is not a leak -- there is nothing to leak.
    The guard keys on files_scanned so a legitimately empty scan stays a normal empty context."""
    ctx = _build_cloak_context_nonpython("t", tmp_path, "rust")
    assert ctx.symbol_map.forward == {}


def test_degraded_opt_out_downgrades_the_refusal_to_a_warning(tmp_path, monkeypatch, _force_zero_extraction):
    """DETERMINEX_CLOAK_ALLOW_DEGRADED=1 is the operator's explicit accept-reduced-privacy
    switch, and it must keep working for the new guard exactly as it does for the import-time
    tree-sitter check -- otherwise the guard is unbypassable and would strand real runs."""
    import determinex_cloak.lang_extractor as lx

    monkeypatch.setattr(lx, "_ALLOW_DEGRADED", True)
    (tmp_path / "lib.rs").write_text("pub struct ZzqRec { pub zzq_field: i64 }\n", encoding="utf-8")
    ctx = lx._build_cloak_context_nonpython("t", tmp_path, "rust")
    assert ctx.symbol_map.forward == {}   # proceeds, uncloaked, by explicit operator choice
