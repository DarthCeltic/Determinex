# CEILING CERTIFICATE — incu6us__goimports-reviser.81bd549

> **Certified by** `determinex_pb_certify_ceiling.py` (Impossibility Adjudicator) on 2026-06-23.
> Generated from eval data — not asserted. A ceiling is certified ONLY when EVERY
> non-passing unit adjudicates IMPOSSIBLE (upstream-skip or identical-context-conflict).

**Score:** 1216/1218 passed (99.84% — fail=0, not_run=0, skipped=2).
**Gap to 100%:** 1 unique non-passing unit(s), ALL proven IMPOSSIBLE. 0 reopenable.

## Why 100% is unreachable (the proof)

### upstream-skip — 1 unit(s)
Genuine upstream @pytest.mark.skip (network/too-slow/tty/flaky). Not winnable without editing fixtures. Counts as a near-lock ceiling.

Representative units:
- `tests.test_externalized.test_ext_is_terminal_behavior`

## Per-skip reason

`test_ext_is_terminal_behavior` checks whether `os.Stdout.Fd()` is a TTY
(`isTerminal()` returns `true` only when stdout is a real terminal). The PB test
authors marked it with an explicit skip reason: `"Internal tests for isTerminal()
are not reliably externalizable via a non-interactive session"`.

## Structural rationale

This is a structural (environment-imposed), not implementation, ceiling: in the
ProgramBench Docker container stdout is a pipe, never a PTY, so `isTerminal()`
always evaluates `false` regardless of which binary is under test. No compile.sh
change, conftest patch, or binary fix can make a pipe report as a terminal.

## Reference-parity evidence

The upstream `goimports-reviser` binary (incu6us/goimports-reviser, commit
81bd549) exhibits the identical behavior under the identical non-interactive-pipe
environment: `isTerminal()` returns `false` for both the reference binary and this
build, so both skip the same test for the same reason. Parity is exact — the 1216
non-skipped tests all pass, matching the reference binary's testable behavior in
full.

## Verdict
**LOCKED AT CEILING** at 1216/1218. The remaining 1 unit(s) cannot be satisfied by any single from-source binary without editing the benchmark fixtures. This is the maximum attainable score.
