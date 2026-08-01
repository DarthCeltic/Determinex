# Parity Artifact — pingu (sheepla__pingu.926d475)

**Classification**: Tier A (unconditional `@pytest.mark.skip` decorators)
**Status**: near-lock ceiling confirmed (416/419 passed, 3 skipped, 0 failed, 0 not_run)
**Date**: 2026-06-11
**Eval**: determinex_pb_pingu_native_v28 on Hetzner (CPX41, Ubuntu 22.04)

---

## Claim

pingu achieves **416/419** on ProgramBench's official metric (passed/total). The 3 missing tests
are **not fixable by any binary implementation**. They are unconditional `@pytest.mark.skip`
decorators placed in the ProgramBench test source code, not in pingu's code.

The reference pingu binary skips these same 3 tests for the same reason — confirmed by the
skip classification: Tier A (the skip decorator fires before the binary is ever called).

---

## Skipped Tests (all from branch d7a5dbbf1b14)

| Test Name | File:Line | Skip Reason |
|-----------|-----------|-------------|
| `tests.test_art_rendering.test_renderASCIIArt_wraparound_at_40` | `eval/tests/test_art_rendering.py:92` | Too slow (45 pings); core wraparound logic tested in wraparound_at_20 |
| `tests.test_art_rendering.test_renderASCIIArt_wraparound_high_index` | `eval/tests/test_art_rendering.py:108` | Too slow (105 pings); core wraparound logic tested in wraparound_at_20 |
| `tests.test_art_rendering.test_wraparound_preserves_exact_art` | `eval/tests/test_art_rendering.py:406` | Too slow (45 pings); core wraparound logic tested in wraparound_at_20 |

---

## Why Tier A (Unconditional)

**Tier A definition**: the skip decorator fires unconditionally — no environment check, no
runtime check, no binary capability check. The skip applies regardless of which pingu
binary is under test.

**Evidence**:
- Skip reason is "Too slow (N pings)" — referencing the number of ICMP ping packets the
  test would send. This is a test-design decision by the PB benchmark authors: these tests
  are valid but send 45-105 real pings, making them too slow for CI.
- The skip fires at collection time, before pytest invokes the binary.
- The wraparound tests are explicitly noted to have their core logic tested elsewhere
  (`wraparound_at_20`), confirming the benchmark authors intentionally skipped these as
  redundant-for-CI, not as binary-capability limitations.

---

## Tier B Would Require

If these were Tier B (environment-conditional), we would need to:
- Run the reference binary in the same Docker container
- Show that it also skips these 3 tests for the same reason
- Confirm the skip is triggered by a runtime environment check

This is NOT the case here. These are compile-time/collection-time decorators.

---

## Evidence: eval.json JUnit Output

From `determinex_pb_pingu_native_v28/sheepla__pingu.926d475/sheepla__pingu.926d475.eval.json`:

```json
{
  "name": "tests.test_art_rendering.test_renderASCIIArt_wraparound_at_40",
  "branch": "d7a5dbbf1b14",
  "status": "skipped",
  "extra": {
    "text": "/workspace/eval/tests/test_art_rendering.py:92: Too slow (45 pings); core wraparound logic tested in wraparound_at_20"
  }
}
```

---

## Board Impact

- **Strict lock count**: unchanged (pingu is NOT a strict lock — skips prevent passed==total)
- **Parity count**: +1 (first Tier A parity banked)
- **Published score**: 416/419 with Tier A parity = effective ceiling achieved

---

## Reproducibility

To reproduce on any machine with Docker + ProgramBench:

```bash
# Instance: sheepla__pingu.926d475
# Submission: corpus/programbench/locked/pingu/submission.tar.gz (once locked)
PYTHONUTF8=1 programbench eval pb_repro --filter sheepla__pingu --force

# Expected: 416/419 passed, 3 skipped (all on branch d7a5dbbf1b14)
# Skip reason confirms Tier A: "Too slow (N pings)"
```

---

*Determinex — Lunarian Data Systems — 2026-06-11*
