# ProgramBench Two-Ledger Integrity

**Why this exists:** the ProgramBench submission stakes are high. Reviewers
will scrutinize the accepted-runs ledger and ask "under what standard was
this entry certified?" A ledger that mixes accept rules is a harder
conversation than two clearly-separated ledgers with one as the proof and
the other as documented in-progress work.

## The two ledgers

### Official ledger (Rule A only)

- `logs/programbench_factory/accepted_runs.jsonl`
- `logs/programbench_lock_board.json` — fields `best_passed`,
  `best_runnable_total`, `best_total`, `best_eval_path`, `best_score`,
  `best_raw_score`, plus the mirrored `passed`/`runnable_total`/etc.

A row enters this ledger only when the candidate gated under **Rule A**:

> Runnable stable + passed up + 0 newly_failing tests.

That is, the candidate was evaluated against the **same runnable test
surface** as the baseline, scored strictly higher, and never regressed a
previously-passing test. The measurement is directly comparable to the
baseline. This is what ProgramBench's reviewers will look at.

### Sidecar (Rule B)

- `logs/programbench_factory/rule_b_promotions.jsonl`
- `programbench_lock_board.json` field `rule_b_discovery` on the per-tool
  entry (high-water mark only; the official `best_*` fields are untouched)

A row goes to this sidecar when the candidate gated under **Rule B**:

> Runnable changed + passed up + 0 newly_failing tests.

The candidate is real work and zero previously-passing tests regressed,
but the measurement surface shifted (typically because a stub scaffold
became an honest implementation and tests that couldn't run now can).
The improvement can't enter the official ledger directly — the baseline
runnable count doesn't match.

### Reject

Either of:
- passed delta ≤ 0 (no improvement)
- newly_failing > 0 (a previously-passing test now fails)

These do not enter any ledger. The lesson is written and the worker is
expected to revert the source change (`git checkout -- corpus/programbench/per_tool_overrides/<slug>/`).

## Decision flow

```
                 ┌───────────────────────────────────┐
                 │ pb_candidate_gate.py              │
                 │ compares candidate eval vs baseline│
                 │ ALSO writes failure_signal_corpus  │
                 └──────────────────┬────────────────┘
                                    │
                  ┌─────────────────┴────────────────┐
                  │                                  │
            decision=accept                    decision=reject
            decision_rule=A or B                  (lesson only)
                  │
        ┌─────────┴─────────┐
        │                   │
   rule=A (strict)     rule=B (sidecar)
        │                   │
        ▼                   ▼
 _accept_chain         _rule_b_sidecar_chain
   - lesson              - lesson
   - register            - write rule_b_promotions.jsonl
   - refresh_board       - annotate lock_board.rule_b_discovery
   - (optional RAG)      - DO NOT touch accepted_runs.jsonl
   - verdict_corpus      - DO NOT touch lock_board.best_*
                         - verdict_corpus    ←─┐
        │                   │                  │  both chains
        ▼                   ▼                  │  call the same
 Official ledger        Sidecar only           │  verdict-corpus
        │                   │                  │  ingest (non-fatal)
        │                   │                  │
        └────────┬──────────┘                  │
                 │                             │
                 ▼                             │
   pb_verdict_corpus.jsonl   ◄─────────────────┘
   (ShareGPT, idempotent via row_hash,
    eats both Rule A and Rule B passes/fails
    because compiler verdict is ground truth
    regardless of measurement surface)
                            │
                            │ (later, via pb_rule_b_promote.py)
                            │
                            ▼
                  Clean Rule A re-gate against
                  the new baseline. If 0 regressions
                  and runnable stable, promote into
                  the official ledger. Verdict corpus
                  gets new rows from the second eval too.
```

## Three concerns, three destinations

| Concern | Source | Destination | What it certifies |
|---|---|---|---|
| Benchmark score | Rule A gates only | `accepted_runs.jsonl` + `lock_board.best_*` | Stable measurement surface, strictly comparable |
| Training signal (positive + negative) | Every Rule A AND Rule B accept | `pb_verdict_corpus.jsonl` (ShareGPT) | Compiler-verified pass/fail pairs |
| Failure signal | Every gate (accept or reject) | `failure_signal_corpus.jsonl` | Cross-tool error pattern corpus |

The score ledger stays Rule A. The training corpus eats both. The
failure corpus eats everything. They never block each other.

## Rule B → Rule A promotion (the legitimate path)

`pb_rule_b_promote.py <slug> --new-run-root <path>`:

1. Read the Rule B sidecar entry.
2. Repack the same source override into a new run root (same code, no change).
3. Run the official eval against the new run root.
4. Gate the new run with the **Rule B candidate's eval as the new baseline**
   and `min-baseline-passed` set to the Rule B candidate's passed count.
5. If that second eval passes ≥ the Rule B passed count, with runnable
   stable and 0 regressions, the gate produces `decision_rule="A"`.
6. Apply the Rule A gate through the normal chain. The entry now enters
   the official ledger cleanly.

This costs one extra Docker eval per Rule B promotion. The benefit is the
official ledger stays unambiguous: every row was gated against a stable
measurement surface, and reviewers can verify the baseline at any time.

## What we did about bedtools

`arq5x__bedtools2.dd57059` was accepted into the official ledger under the
permissive Rule B before this architecture was put in place. The fix:

1. The line was removed from `accepted_runs.jsonl` and moved to
   `rule_b_promotions.jsonl` with an `_audit` block explaining the move.
2. The lock board entry's `best_*` fields were reverted to the clean
   baseline (passed=7, runnable=349). The Rule B discovery (passed=392,
   runnable=398) is preserved on the same entry as `rule_b_discovery` so
   cortex-pull still has the high-water mark.
3. A backup of the pre-revert ledger and board lives at
   `accepted_runs.jsonl.backup_before_rule_b_audit_*` and the matching
   board backup, so the audit trail is complete.

bedtools is now on the legitimate path. Running
`pb_rule_b_promote.py arq5x__bedtools2.dd57059 --new-run-root <new>` will
do the clean rebase and put it in the official ledger if the second eval
matches.

## What this preserves

- **Failure-signal corpus** still records every gate run (accept or reject,
  Rule A or B). The cross-tool pattern signal is intact.
- **Cortex-pull** still sees Rule B discoveries via the
  `rule_b_discovery` annotation on the lock board.
- **Lessons** are still written for every gate.

What's separated is the *certification* — what
`accepted_runs.jsonl` and the lock board's `best_*` fields stand behind.
Those are now Rule A only.

## The disposition policy in one line

> The official ledger is the proof. The sidecar is the documented
> in-progress work. Both are kept honest by writing the rule of each
> accept into the row.
