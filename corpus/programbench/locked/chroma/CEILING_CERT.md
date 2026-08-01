# CEILING CERTIFICATION: chroma

**Tier:** T2 ceiling_certified  
**Eval:** 524/531 (sk=7, fail=0, nr=0)  
**Certified:** 2026-06-12, Driver (Claude Sonnet 4.6)  
**Parity evidence:** `corpus/programbench/parity_artifacts/chroma/parity_evidence.md`  
**Parity verdict:** STRUCTURAL_BY_PROOF — API-not-in-CLI is a binary design invariant

## Per-Skip Analysis

All 7 skips are parameterized instances of the same test at the same line:

### Skips 1–7: tests.test_harvest.test_lexer_analysis[X] (7 parameterized cases)
**Parameterized variants:** `bash`, `c.ifdef`, `c.ifndef`, `c.include`, `cpp.include`,
`cpp.namespace`, `mysql.backtick`  
**Reason string:** "Analysis tests require AnalyseText API not exposed in CLI"  
**Source:** `/workspace/eval/tests/test_harvest.py:96` (same line, all 7 variants)  
**Structural rationale:** The Chroma library exposes an `AnalyseText()` API that scores
text against all known lexers and returns probabilistic confidence values. This API is
designed for programmatic embedding use — it has no CLI counterpart. The `chroma` CLI
binary (`--analyse` is not a valid flag) provides only a syntax highlighter interface;
it cannot surface the internal `AnalyseText` scores through stdin/stdout. Adding this
capability would require a new subcommand or flag in the chroma CLI binary itself, which
is an upstream feature request, not a fixable test configuration issue. The skip decorator
is unconditional (`@pytest.mark.skip`), not conditional on binary version or output.  
**Reference-parity:** Structural by proof — the PB reference chroma binary has the same
CLI interface and also lacks an `--analyse` or equivalent flag exposing `AnalyseText`.
The skip applies equally to any chroma CLI binary built from the upstream source.

## Ceiling Verdict

All 7 skips (7 unique parameterized instances of `test_lexer_analysis`) are unconditional
skips covering a library API (`AnalyseText`) that has no CLI surface in any chroma release.

**chroma ceiling = 524/531.** Structurally confirmed.

To unlock: add `--analyse` or equivalent subcommand to the upstream chroma CLI exposing
`AnalyseText()` output — an upstream feature contribution, outside eval scope.
