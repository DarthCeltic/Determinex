# DETERMINEX_PROGRAMBENCH_STRICT_LOCK_EXPANSION_BATCH_003_CANDIDATES

Date: 2026-06-02

## Current Board Truth

- Rows: `200`.
- Strict archived 100% locks: `55`.
- Unarchived score-100 rows: `1`.
- Aggregate runnable: `84,957 / 161,099 = 52.74%`.
- Factory-accepted non-locked rows on the current board query: `71`.

## Candidate Wave Toward 75 Strict Locks

1. `trasta298__keifu.3331426`
   - Current board: score 100, `274/274` runnable, not archived.
   - Required evidence: archive lock, `eval_report.json`, `submission.tar.gz`, source snapshot, board refresh.
   - Risk: stale board state if archive occurs without regenerating `logs/programbench_lock_board.json`.

2. `doxygen__doxygen.966d98e`
   - Current board: near-lock, `249/250`.
   - Required evidence: reconcile the remaining failure and existing operator/security-policy blocker.
   - Risk: one-test gap may hide policy or invocation mismatch.

3. `facebookresearch__fasttext.1142dc4`
   - Current board: near-lock, `349/352`.
   - Required evidence: fixture diff for the 3-test gap, re-eval, archive only at 100.
   - Risk: native behavior quirks likely require upstream binary comparison.

4. `kyoh86__richgo.313114f`
   - Current board: `775/786`.
   - Required evidence: 11-test failure cluster, re-eval, archive only at 100.
   - Risk: Go toolchain/output formatting edge cases.

5. `jqlang__jq.b33a763`
   - Current board: high-impact anchor, `1394/1521`.
   - Required evidence: native build/behavior reconciliation before lock push.
   - Risk: broad surface; not a fast strict-lock candidate.

## Paper Update Requirement

Papers may say `55 strict locks + 1 unarchived score=100 at 52.74% aggregate runnable`. They must not say ProgramBench total-100 or imply benchmark locks are product-support families.
