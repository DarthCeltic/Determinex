# CEILING CERTIFICATE — pingu

> **Certified by** `determinex_pb_certify_ceiling.py` (Impossibility Adjudicator) on 2026-06-22.
> Generated from eval data — not asserted. A ceiling is certified ONLY when EVERY
> non-passing unit adjudicates IMPOSSIBLE (upstream-skip or identical-context-conflict).

**Score:** 416/419 passed (99.28% — fail=0, not_run=0, skipped=3).
**Gap to 100%:** 3 unique non-passing unit(s), ALL proven IMPOSSIBLE. 0 reopenable.

## Why 100% is unreachable (the proof)

### upstream-skip — 3 unit(s)
Genuine upstream @pytest.mark.skip (network/too-slow/tty/flaky). Not winnable without editing fixtures. Counts as a near-lock ceiling.

Representative units:
- `tests.test_art_rendering.test_renderASCIIArt_wraparound_at_40`
- `tests.test_art_rendering.test_renderASCIIArt_wraparound_high_index`
- `tests.test_art_rendering.test_wraparound_preserves_exact_art`

## Verdict
**LOCKED AT CEILING** at 416/419. The remaining 3 unit(s) cannot be satisfied by any single from-source binary without editing the benchmark fixtures. This is the maximum attainable score.
