---
name: fzf-impl-sequence
description: Build order. --filter mode dominates; build that first. Algorithm v2 must come before v1.
type: implementation-sequence
---

# fzf — Implementation Sequence

> **Run eval after every step.** The 1,017-test branch is the matcher correctness suite — that one branch alone tells you if the algorithm is right.

## Phase A — Pipeline skeleton (target: 30-40%)

1. **Stdin reader (line-buffered)** + **stdout writer**. `--read0`/`--print0` toggles. Gate: `printf 'a\nb\n' | fzf --filter b` → `b` and exit 0.
2. **Empty query in `--filter`** → emit all input lines unchanged. Gate: `printf 'a\nb\n' | fzf --filter ''` → `a\nb\n`.
3. **Identity matching (no scoring)**: any line containing the query as a substring matches, score 0. Gate: substring tests pass; non-matches absent.

## Phase B — Matcher v2 (target: 65-78%)

4. **FuzzyMatchV2 DP table.** Implement with the bonus constants from the reference. Gate: `printf 'apple\nbanana\nappetizer\n' | fzf --filter app` ranks `apple` > `appetizer` > `banana` (banana absent), and **the score numbers match the reference within ±0**. Test the bonus formula on a single line first.
5. **Position tracking.** `Pos` array of byte offsets where chars match. Used in interactive highlighting; in `--filter` it's invisible but tests may probe `--print-query` or future hooks.
6. **Smart-case rule.** Gate: `Foo` is case-sensitive; `foo` is case-insensitive.
7. **`-i` / `--ignore-case` / `+i` / `--case-sensitive`** override smart-case. Gate: matrix.
8. **Tie-break: default `length,index`.** Gate: two same-scored matches order by length asc, then by input index asc.

## Phase C — Query parser (target: 80-88%)

9. **Tokenize query** on unescaped spaces; pipe-split inside groups; **negation prefix `!`**; **type prefixes `'`, `^`, `=`**; **suffix marker `$`**. Gate: every row in the query-syntax matrix table.
10. **AND/OR composition**: line passes if all top-level groups match (each group is OR over its terms). Gate: `app txt` requires both; `app | foo` requires either.
11. **`'`, `^`, `$`, `=` matchers**: implement Exact, Prefix, Suffix, Equal beside Fuzzy. Gate: `^lib` matches `libfoo`, not `liblib` ... wait — yes it does match `liblib` (prefix). Verify the spec.

## Phase D — Field selector (target: 88-92%)

12. **`-d DELIM`** — string OR regex delimiter. Gate: `-d ,` splits on comma.
13. **`-n FIELDS`** — match-only-on-fields. Field syntax: `1`, `2..3`, `..3`, `2..`, `-1`. Gate: `-d ' ' -n 2 --filter x` on `a x b` matches; on `x a b` does not.
14. **`--with-nth FIELDS`** — display-only fields. Same syntax. Gate: matching uses raw line (or `-n`), display uses `--with-nth`.

## Phase E — Output + control flow (target: 92-96%)

15. **`--no-sort`** preserves input order; `--tac` reverses input order. Gate: order matrix.
16. **`--tiebreak=K[,K...]`** — KIND list applied in order. Implement length, chunk, pathname, begin, end, index. Gate: each kind is unit-testable.
17. **`--exit-0` and `--select-1`** affect exit code with no/one match.
18. **`--ansi`**: strip CSI sequences from line for matching but keep them in output.
19. **`--print-query`**: prepend the query as the first output line.

## Phase F — TUI (skip for the bulk; do last)

20. **TTY detection**: only enter raw mode when stdin AND stdout are both TTY. Gate: piped invocation never enters raw mode.
21. **termios raw mode** — Unix only; `golang.org/x/term` or syscall.
22. **Render loop**: double-buffer; print only the changed lines; clear-to-EOL.
23. **Key bindings**: at minimum Enter (accept), Esc/Ctrl-C (cancel), Backspace, arrow up/down, type-to-query.
24. **Multi-select**: Tab to mark, Enter to emit all marked lines (or current if none).

**Most tests will not exercise Phase F.** If eval shows >50% pass after Phase E, lock the pieces and only return to Phase F if specific test names point to interactive paths.

## The 90→100% gap (most likely sites)

1. **Score constant mismatches.** Off-by-one in any bonus → systematic drift across the 1,017-test matcher branch. **First debugging pass: re-derive the constants from reference, character-for-character.**
2. **Tie-break ordering bugs.** Default tie-break can deviate when scores collide — a single misplaced comparator flips dozens of tests.
3. **Field range edge cases.** `-n 1..` includes everything from field 1 onward, NOT field 1 only. Off-by-one with `..3` (inclusive vs exclusive).
4. **`--with-nth` interaction with `-d`.** When delimiter is regex, field positions are still byte offsets, not regex-match offsets. Easy to confuse.
5. **Smart-case + Unicode.** `Köln` has uppercase → case-sensitive. The case-detection must use Unicode, not ASCII isupper.
6. **`--ansi` stripping precision.** Must strip `\x1b\[[0-9;]*m` but not other escape sequences. Regex needs to be tight.
7. **Unicode width in match positions.** CJK takes width 2 but byte offsets count bytes; render uses width.
8. **`--print0` trailing NUL.** No trailing NUL after the last record (vs trailing newline default).
9. **CRLF line endings.** `\r` strip on read but only at end-of-line, not mid-line.
10. **Empty stdin** — exit 1 even with empty query in `--filter` mode.

## Failure-category triage

```
Group A — Score arithmetic mismatch (entire 1,017-test branch likely affected together)
Group B — Query-parser edge case (single test or small cluster)
Group C — Field-selector boundary (small cluster, predictable)
Group D — Output ordering / tie-break
Group E — TTY/interactive only (defer)
```

Score-arithmetic failures cluster in big bursts. If you see >100 consecutive failures all in `test_fuzzy_match_*`, **stop iterating on tests** and re-audit the bonus constants in `algo.go` against the reference. One constant fix unblocks the entire cluster.
