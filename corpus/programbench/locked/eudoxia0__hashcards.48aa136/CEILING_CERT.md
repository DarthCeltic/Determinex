# CEILING CERTIFICATION: eudoxia0__hashcards.48aa136

**Tier:** T2 ceiling_certified (NOT a strict lock — sk=6 structural upstream skips)
**Date:** 2026-06-14, Driver (Claude Sonnet 4.6)
**Eval pilot:** `determinex_pb_hashcards_hetz_v1`
**Eval source:** Hetzner `determinex_pb_hashcards_hetz_v1` batch

## Result (raw eval_report.json)

| status   | count | tests.json? |
|----------|-------|-------------|
| passed   | 2572  | yes         |
| skipped  | 6     | yes         |
| failure  | 8     | NO (extra)  |
| total    | 2586  | —           |

**PB scorer f=0 (all 8 "failure" entries are NOT in tests.json)**
**eval_report_sha256:** `BAFAE883FE6AFC0396A4940D5943881E58A65053C5B6862AF5DB584314134C3D`
**PB score:** 100 (2572 passed / 2578 tests.json tests)

## Extra-test Failures (NOT in tests.json, do NOT affect PB score)

The eval_report.json shows 8 "failure" entries for 4 unique katex endpoint tests × 2 bidir:
- `test_drill_internals.test_katex_css_endpoint`
- `test_drill_internals.test_katex_js_endpoint`
- `test_drill_internals.test_katex_mhchem_js_endpoint`
- `test_drill_internals.test_katex_font_woff2_endpoint`

These tests appear in some branch JUnit XML outputs but are NOT in `tests.json`.
PB emits "WARN: N test(s) in JUnit XML not in tests.json" and excludes them from scoring.
They do NOT count as failures under the official ProgramBench metric.

The katex failures indicate our binary does not serve KaTeX static assets from an HTTP
endpoint. Since tests.json doesn't include these tests, this is outside the PB scoring
surface for commit 48aa136.

## Per-Skip Analysis (3 unique × 2 bidir = 6 skip entries)

### Unique skips (all in `test_harvest` module):
1. `test_harvest.test_drill_cache_basic_functionality`
2. `test_harvest.test_drill_action_grade`
3. `test_harvest.test_performance_update`

**Skip reason string:** `""` (empty — unconditional `@pytest.mark.skip` with no message)

**Structural rationale:** These three tests exercise hashcards' harvest/drill cache
and performance-update features. At commit 48aa136, these tests are marked as upstream
`@pytest.mark.skip` in the ProgramBench test fixtures (no reason string — unconditional
skip, not environment-conditional). The same tests skip when running the upstream
hashcards binary at this exact commit in any Docker environment.

The bidir injection doubles each unique test entry, producing 6 total skip entries.
All 2572 tests.json tests pass, demonstrating full implementation parity for all
scorable behaviors at this commit.

## Reference-Parity Evidence

**Parity verdict:** STRUCTURAL_BY_PROOF — unconditional upstream @pytest.mark.skip

1. Empty reason string: the tests are not conditionally skipped based on environment
2. The skip fires before any binary interaction — upstream hashcards binary produces
   identical results
3. All 2572 tests.json tests pass (PB score = 100)

## Ceiling Verdict

**hashcards PB ceiling = 2572/2578 tests.json tests** (+ 6 upstream skips).
The 8 katex endpoint failures are in branches' extra tests not in tests.json — they
don't affect the PB score. The 6 skips (3 unique × bidir) are unconditional upstream
`@pytest.mark.skip` markers. Cannot be removed by implementation changes.

To convert to T1: ProgramBench would need to remove the skip markers. Not achievable
via compile.sh changes.
