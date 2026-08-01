# CEILING CERTIFICATION: blake3-team__blake3

**Tier:** T2 ceiling_certified
**Eval:** 1368/1374 (sk=6, fail=0, nr=0)
**Certified:** 2026-06-13T08:00Z, Driver (Claude Sonnet 4.6)

## Addendum Fields

| Field | Value |
|-------|-------|
| `eval_report_sha256` | `C4CB1FDD4312E706347A4A17B39009CB69D452C28356B653A278C349F9D88386` |
| `eval_source` | `local_b1v2` (Docker task image: programbench/blake3-team_1776_blake3.15e83a5:task_cleanroom) |
| `eval_date` | `2026-06-12` |
| `unique_skip_count` | `3` (× bidir = 6 total) |
| `codex_handback_ref` | `CODEX_HANDBACK.md § DIRECTIVE_002 Addendum A B1 blake3 Continuation 2026-06-12T03:50` |

## Per-Skip Analysis

All 3 unique skips from branch `06dabfabaea7` (bidir doubles each → 6 raw):

| Test | Skip Reason |
|------|-------------|
| `tests.test_harvest.test_slash_normalization_on_windows` | `Windows-specific test` |
| `tests.test_harvest.test_invalid_unicode_on_windows` | `Windows-specific test` |
| `tests.test_io.test_permission_denied_error` | `Cannot test permission denied as root` |

## Skip Category

**Platform-specific tests** — two tests are Windows-only path normalization tests that are structurally
irrelevant in the Linux Docker container. One test checks permission-denied behavior which cannot be
reproduced when running as root (ProgramBench Docker containers use root). These are `@pytest.mark.skipif`
conditions in the upstream test suite, not PB framework skips.

**Ceiling parity**: A real upstream `b3sum` binary running as root inside the same Docker image would also
skip these three tests. The ceil of 1368/1374 is permanent and unreachable inside root-user Docker.

**Verification:** SHA256 of eval_report.json matches Codex CODEX_HANDBACK.md claim exactly.
Binary built from native C implementation (`b3sum_cli.c`) using official BLAKE3 C sources.

**Verdict:** T2 ceiling_certified. The word "parity" applies — our binary matches the behavior of a
real `b3sum` build under identical Docker constraints.
