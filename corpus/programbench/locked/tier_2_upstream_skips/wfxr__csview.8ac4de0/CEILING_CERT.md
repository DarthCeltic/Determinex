# CEILING CERTIFICATION: wfxr__csview.8ac4de0

**Tier:** T2 ceiling_certified
**Eval:** 347/348 (sk=1, fail=0, nr=0)
**Certified:** 2026-06-13T23:16:27Z, Driver (Claude Sonnet 4.6)

## Addendum Fields

| Field | Value |
|-------|-------|
| `eval_report_sha256` | `297e7a079976d0e5e346398532dbdbce7c451c52862e80429a6543c846e9acdc` |
| `eval_source` | `hetzner_d1_harvest_20260613` |
| `eval_date` | `2026-06-13` |
| `unique_skip_count` | `1` (1 unique (eval.tests. prefix only - 1 total)) |

## Skip Analysis

Root container cannot make file unreadable for permission test.

| Test | Skip Reason |
|------|-------------|
| `test_unreadable_file_permission_denied_exit_1` | Running as root; cannot reliably make file unreadable |

## Skip Category

**Docker root-user limitation.**

chmod 000 has no effect when running as root. Real binary behaves correctly as non-root. Permanent Docker structural limit.

**Ceiling parity:** The real upstream binary would also fail/skip these under identical Docker constraints.
Ceiling of 347/348 is permanent.

**Verdict:** T2 ceiling_certified.
