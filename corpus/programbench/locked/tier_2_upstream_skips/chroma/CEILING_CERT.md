# CEILING CERTIFICATION: chroma

**Tier:** T2 ceiling_certified
**Eval:** 524/531 (sk=7, fail=0, nr=0)
**Certified:** 2026-06-13T08:15Z, Driver (Claude Sonnet 4.6)

## Addendum Fields

| Field | Value |
|-------|-------|
| `eval_report_sha256` | `15d3d21ce9d3282c6ec11f6d34bc500cf1ed765d1a79fc721fdf811eab4d9142` |
| `eval_source` | `filesystem/tier_2_upstream_skips` |
| `eval_date` | `2026-06-11` |
| `unique_skip_count` | `7` (all in single branch 06dabfabaea7) |
| `parity_evidence_ref` | `corpus/programbench/parity_artifacts/chroma/parity_evidence.md` |

## Per-Skip Analysis

All 7 skips are in `test_harvest.py` branch `06dabfabaea7`:

| Test | Skip Reason |
|------|-------------|
| `test_lexer_analysis[bash]` | Analysis tests require AnalyseText API not exposed in CLI |
| `test_lexer_analysis[c.ifdef]` | Analysis tests require AnalyseText API not exposed in CLI |
| `test_lexer_analysis[c.ifndef]` | Analysis tests require AnalyseText API not exposed in CLI |
| `test_lexer_analysis[c.include]` | Analysis tests require AnalyseText API not exposed in CLI |
| `test_lexer_analysis[cpp.include]` | Analysis tests require AnalyseText API not exposed in CLI |
| `test_lexer_analysis[cpp.namespace]` | Analysis tests require AnalyseText API not exposed in CLI |
| `test_lexer_analysis[mysql.backtick]` | Analysis tests require AnalyseText API not exposed in CLI |

## Skip Category

**Unexposed API skips** — the `AnalyseText` API is a library function inside chroma's Go package that
is not accessible via the CLI. PB tests that exercise this path are skipped with condition
`Analysis tests require AnalyseText API not exposed in CLI`. The chroma upstream binary has the same
limitation. No CLI invocation can reach `AnalyseText`.

**Ceiling parity**: Real upstream `chroma` binary would also skip these tests in any eval environment.
The ceil of 524/531 is permanent without a separate chroma-analyze sub-command.

**Verdict:** T2 ceiling_certified. The word "parity" applies — our binary matches the behavior of
real chroma under identical constraints.
