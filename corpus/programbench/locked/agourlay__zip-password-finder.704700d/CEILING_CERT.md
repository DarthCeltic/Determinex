# CEILING CERTIFICATE — agourlay__zip-password-finder.704700d

> **Certified by** `determinex_pb_certify_ceiling.py` (Impossibility Adjudicator) on 2026-06-23.
> Generated from eval data — not asserted. A ceiling is certified ONLY when EVERY
> non-passing unit adjudicates IMPOSSIBLE (upstream-skip or identical-context-conflict).

**Score:** 1582/1584 passed (99.87% — fail=0, not_run=0, skipped=2).
**Gap to 100%:** 1 unique non-passing unit(s), ALL proven IMPOSSIBLE. 0 reopenable.

## Why 100% is unreachable (the proof)

### upstream-skip — 1 unit(s)
Genuine upstream @pytest.mark.skip (network/too-slow/tty/flaky). Not winnable without editing fixtures. Counts as a near-lock ceiling.

Representative units:
- `eval.tests.test_zip_password_finder.TestDictionaryAttack.test_dictionary_password_not_foun`

## Verdict
**LOCKED AT CEILING** at 1582/1584. The remaining 1 unit(s) cannot be satisfied by any single from-source binary without editing the benchmark fixtures. This is the maximum attainable score.
