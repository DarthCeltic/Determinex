# CEILING CERTIFICATION: sheepla__pingu.926d475

**Tier:** T2 ceiling_certified
**Eval:** 416/419 (sk=3, fail=0, nr=0)
**Certified:** 2026-06-13T23:16:27Z, Driver (Claude Sonnet 4.6)

## Addendum Fields

| Field | Value |
|-------|-------|
| `eval_report_sha256` | `9d01c574eea5301b2404a381e9c23887b5a5dfe74b38f10451d507e9032e7b94` |
| `eval_source` | `hetzner_d1_harvest_20260613` |
| `eval_date` | `2026-06-13` |
| `unique_skip_count` | `3` (3 unique (no bidir for these skips)) |

## Skip Analysis

Too-slow ping tests (45-105 pings each).

| Test | Skip Reason |
|------|-------------|
| `test_renderASCIIArt_wraparound_at_40` | Too slow (45 pings); core wraparound logic tested in other tests |
| `test_renderASCIIArt_wraparound_high_index` | Too slow (105 pings); core wraparound logic tested in other tests |
| `test_wraparound_preserves_exact_art` | Too slow (45 pings); core wraparound logic tested in other tests |

## Skip Category

**Performance timeout - upstream @pytest.mark.skip annotations.**

Tests send 45-105 ICMP pings to localhost to verify ASCII art wrapping. Marked skip due to runtime. Core logic covered by other tests. Permanent upstream skip.

**Ceiling parity:** The real upstream binary would also fail/skip these under identical Docker constraints.
Ceiling of 416/419 is permanent.

**Verdict:** T2 ceiling_certified.
