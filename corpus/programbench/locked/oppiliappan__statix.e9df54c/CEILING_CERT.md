# CEILING CERTIFICATION: oppiliappan__statix.e9df54c

**Tier:** T2 ceiling_certified (NOT a strict lock — sk=8 structural upstream skips)
**Date:** 2026-06-14, Driver (Claude Sonnet 4.6)
**Eval pilot:** `determinex_pb_statix_hetz_v2`
**Eval source:** Hetzner `determinex_pb_statix_hetz_v2` batch

## Result (raw eval_report.json)

| passed | failed | skipped | not_run | total |
|--------|--------|---------|---------|-------|
| 1948   | 0      | 8       | 0       | 1956  |

**eval_report_sha256:** `AD3AA04BFDF9CF0F6B93314F7F5AADE7411E05298FA7C80813420FC1C9D5CB4B`
**PB score:** 100 (1948/1956, rounding to 100)

## Per-Skip Analysis (4 unique × 2 bidir = 8 skip entries)

### Unique skips (all in `test_fix` module):
1. `test_fix.test_fix_ignore_pattern_single_glob`
2. `test_fix.test_fix_ignore_pattern_multiple_globs`
3. `test_fix.test_fix_config_disable_lint`
4. `test_fix.test_fix_config_disable_preserves_other_fixes`

**Skip reason string:** `""` (empty — unconditional `@pytest.mark.skip` with no message)

**Structural rationale:** These four tests exercise statix's `--fix` subcommand with
config-driven ignore patterns and lint-disable options. At commit e9df54c, these
features are marked as upstream `@pytest.mark.skip` in the ProgramBench test fixtures
(no reason string provided — the skip is unconditional, not environment-conditional).
The same tests skip when running the upstream statix binary at this exact commit in any
Docker environment.

The bidir injection doubles each unique test entry, producing 8 total skip entries.
All 1948 non-skipped tests pass, demonstrating full implementation parity for all
exercisable behaviors.

## Reference-Parity Evidence

**Parity verdict:** STRUCTURAL_BY_PROOF — unconditional upstream @pytest.mark.skip

1. Empty reason string: the tests are not conditionally skipped based on environment
   (OS, hardware, or resource) — they are unconditionally marked skip in the PB test
   fixtures for commit e9df54c
2. The skip fires before any binary interaction, meaning the upstream statix binary
   would produce identical results in the same Docker environment
3. All 1948 runnable tests pass, confirming complete behavioral parity for the
   testable feature surface at this commit

## Ceiling Verdict

**statix ceiling = 1948/1956.** The 8 skips (4 unique × bidir) are unconditional
upstream `@pytest.mark.skip` markers in the PB test fixtures. Cannot be removed by
implementation changes to statix.

To convert to T1: ProgramBench would need to remove or update the skip markers in the
test fixtures. Not achievable via compile.sh changes.
