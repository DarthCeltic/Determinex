# CEILING CERTIFICATION: bellard__quickjs.d7ae12a

**Tier:** T2 ceiling_certified
**Eval:** 6076/6088 (sk=12, fail=0, nr=0)
**Certified:** 2026-06-13T23:16:27Z, Driver (Claude Sonnet 4.6)

## Addendum Fields

| Field | Value |
|-------|-------|
| `eval_report_sha256` | `66953670c0a639fe38e64097678f6a7aa036ef951d674d3767f9a25cf773799a` |
| `eval_source` | `hetzner_d1_harvest_20260613` |
| `eval_date` | `2026-06-13` |
| `unique_skip_count` | `6` (bidir x2 = 12 total) |

## Skip Analysis

bjson.so shared library not built; HTTP gold-env limitations (5 tests).

| Test | Skip Reason |
|------|-------------|
| `test_bjson` | bjson.so not available - shared library not built in default build |
| `test_basic_http_get` | gold-env-limitation: requires reliable HTTP server |
| `test_http_status_codes` | gold-env-limitation: requires reliable HTTP server |
| `test_header_parsing` | gold-env-limitation: requires reliable HTTP server |
| `test_url_formats` | gold-env-limitation: requires reliable HTTP server |
| `test_content_type_header` | gold-env-limitation: requires reliable HTTP server |

## Skip Category

**Missing optional build artifact (bjson.so) plus gold-env network limitation.**

bjson.so is optional, not included in default quickjs builds. HTTP tests require reliable server in Docker. Both are permanent structural limits.

**Ceiling parity:** The real upstream binary would also fail/skip these under identical Docker constraints.
Ceiling of 6076/6088 is permanent.

**Verdict:** T2 ceiling_certified.
