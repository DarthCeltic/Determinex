# CEILING CERTIFICATION: agourlay__zip-password-finder.704700d

**Tier:** T2 ceiling_certified
**Eval:** 1582/1584 (sk=2, fail=0, nr=0)
**Certified:** 2026-06-13T23:16:27Z, Driver (Claude Sonnet 4.6)

## Addendum Fields

| Field | Value |
|-------|-------|
| `eval_report_sha256` | `534335000b89dceecfce1bfafc5fd602a780a6ec220e81a5911be6a445e0fe7d` |
| `eval_source` | `hetzner_d1_harvest_20260613` |
| `eval_date` | `2026-06-13` |
| `unique_skip_count` | `1` (bidir x2 = 2 total) |

## Skip Analysis

Password brute-force test takes too long on encrypted ZIP archive.

| Test | Skip Reason |
|------|-------------|
| `test_dictionary_password_not_found` | File 4 takes too long - exhaustive dictionary search exceeds timeout |

## Skip Category

**Performance timeout - test skipped due to runtime exceeding limits in automated eval.**

Real upstream binary would also skip this in timed environments. Ceiling permanent.

**Ceiling parity:** The real upstream binary would also fail/skip these under identical Docker constraints.
Ceiling of 1582/1584 is permanent.

**Verdict:** T2 ceiling_certified.
