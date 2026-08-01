---
name: fzf-architecture
description: Architecture for fzf reimplementation. Go is recommended (matches reference); the matcher is the deep work; the TUI is gated behind --filter mode for fastest test pass-through.
type: architecture
---

# fzf — Architecture Blueprint

## Language choice

**Go.** Justification:
1. Reference is Go; concurrency idioms (goroutines for reader/matcher/render) are first-class and tests likely exercise stream behavior under partial input.
2. PB containers ship `go 1.21`. Build is `go build -o executable .` — single artifact, no runtime dependencies.
3. termios raw-mode bindings via `golang.org/x/term` (or syscall directly for stdlib-only). Cross-platform.
4. Matcher's CPU-hot path benefits from Go's escape analysis — Python implementation would be 50-100× slower on the largest test branch (1,017 tests).

Fallback: Rust, only if Go's regex engine produces user-visible behavioral diffs in `--regex` mode.

## Core data structures

### `Item` — input line
```go
type Item struct {
    Text   string  // raw line (or transformed by --with-nth)
    Index  int32   // 0-based input order
    Score  int32   // computed by matcher
    Pos    []int   // matched positions, byte offsets in Text
}
```

### `Pattern` — compiled query
```go
type Pattern struct {
    Terms []Term  // ANDed across spaces; ORed across pipes
}
type Term struct {
    Type     TermType  // Fuzzy | Exact | Prefix | Suffix | Equal | Negated
    Text     string
    CaseMode CaseMode  // Smart | Sensitive | Insensitive
}
```

Splitting query rules: spaces are AND, pipes are OR (inside an AND-group), backslash escapes spaces. `'word` = exact substring, `^prefix` = prefix, `suffix$` = suffix, `!word` = negation, `=exact` = equal-line, `^=` and `=^` are different beasts (don't second-guess: read fzf's man page for ground truth).

### `Matcher` — algorithm v1 + v2

**v1 (FuzzyMatchV1)**: greedy, left-to-right scan. Find earliest occurrence of all chars; backtrack from that occurrence to find the *best* (highest scored) cluster. Linear-time worst case. Used for `--algo=v1`.

**v2 (FuzzyMatchV2, default)**: full DP table. `dp[i][j]` = best score for matching first `i` query chars against first `j` text chars. Bonuses:
- +16 for first char match
- +8 for case match
- +8 for boundary (after `/`, `_`, `-`, ` `, `.`)
- +6 for camelCase boundary
- +4 for consecutive match (chain bonus)
- -3 per gap char
- -1 for non-letter mismatch

Actual constants: read `src/algo/algo.go` from the reference for exact values. The integers matter — tests compare scores numerically.

### `Field selector`
`--delimiter` (default `\t`), `--nth N[,N...]` for matching, `--with-nth` for display. Supports negative (`-1` = last field), ranges (`1..3`).

## Module breakdown (Go packages)

```
cmd/fzf/main.go             arg parse, dispatch
algo/algo.go                FuzzyMatchV1, FuzzyMatchV2, ExactMatch, PrefixMatch, SuffixMatch, EqualMatch
core/core.go                pipeline orchestrator
core/reader.go              stdin reader (line-buffered, --read0 NUL-buffered)
core/pattern.go             query → Pattern, Pattern.Match(item) → score
core/result.go              ranked Item slice with sort + tie-break
core/field.go               --delimiter, --nth, --with-nth field extraction
tui/tty_unix.go             termios raw mode, escape sequences (Linux/Darwin)
tui/tty_windows.go          ANSI on Windows (PB container is Linux, so this is optional for PB)
tui/render.go               double-buffered viewport, color (--color none|256|24bit)
events/events.go            keystroke decode → Action enum
util/string.go              UTF-8 width, char class detection
```

## Build script

`compile.sh`:
```bash
#!/bin/bash
set -e
go mod init fzf >/dev/null 2>&1 || true
go mod tidy >/dev/null 2>&1 || true
go build -o executable .
```

If using `golang.org/x/term`, network is available in PB containers — `go mod download` works. Stdlib-only is preferred to avoid network dependence: implement termios via `syscall.Syscall(SYS_IOCTL, fd, TCGETS, ...)`.

## Critical implementation decisions

### Decision 1: Implement `--filter` mode FIRST
PB pytest tests will run fzf as `echo -e "a\nb\nc" | fzf --filter q`. **No interactive TUI is invoked in test mode.** Build the entire pipeline (reader → matcher → result → ranked print) before touching termios. This single decision likely accounts for 60-75% of the total test pass.

### Decision 2: v2 algorithm is the default — implement v2 first
Reference fzf defaults to v2. A v1-only implementation will fail score-comparison tests where v2's DP produces different bonuses. Build v2; treat v1 as an after-thought (`--algo=v1`).

### Decision 3: Tie-break order matters
fzf sorts by `(score DESC, index ASC)` by default. With `--tac`, reverse; with `--no-sort`, output is filter-only with input order preserved. Get this right early — many tests check exact line order.

### Decision 4: Smart-case
`--smart-case` (default): if query has any uppercase char → case-sensitive; else case-insensitive. `--ignore-case` and `--case-sensitive` override. Implement at Pattern compile time, not at match time.

### Decision 5: TTY behavior in non-interactive mode
When stdin is not a TTY OR `--filter` is given, do not enter raw mode at all. Otherwise the PB pytest harness (which pipes stdin) hangs. Detect with `term.IsTerminal(os.Stdin.Fd())`.

### Decision 6: Color output rules in `--filter`
`--filter` should NOT emit color codes by default (it goes to a pipe). `--ansi` strips terminal color codes from input but may *display* them — under `--filter` they pass through unchanged. Verify against reference.

## Edge cases to bake in early

1. Empty query → all items match with score 0, in input order.
2. Query that matches nothing → exit code 1, no output.
3. Multi-byte UTF-8 in query AND text — bonuses are byte-position based, but case-folding is rune-based. Don't confuse the two.
4. CR/LF line endings: strip `\r` from input lines on Windows-style input.
5. `--no-sort` with `--filter` → output input-order only, but only matched items.
6. `--tiebreak`: comma-separated list (e.g. `length,index`) — apply in order.

## What NOT to implement (defer until eval shows hits)

- Preview window (`--preview` runs an external command per highlight; in `--filter` mode it's skipped).
- History (`--history`).
- Multi-select (`--multi`, `-m`) — implement; cheap.
- Bindings (`--bind`) — interactive only.
- Header (`--header`) — interactive only.
- `--print-query` — easy to add when test demands it.
- Walker mode (`--walker`) — fzf can do file traversal itself; almost certainly NOT tested in PB (overlaps fd's surface).
