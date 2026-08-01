---
name: fzf-corpus-impact
description: What fzf adds to the Determinex Oracle. Adds the entire "interactive TUI" failure-category space — termios, render diff, event decoding — plus the single most-reused match-scoring fixture in the bench.
type: corpus-impact
---

# fzf — Corpus Impact

## What this teaches the Oracle

Locking fzf adds five distinct training-pair categories — none of which exist in the current corpus (which is JSON-pipeline-shaped from jq, yj, htmlq):

1. **TTY raw-mode failure pairs**
   - `tcsetattr` flag combinations that break echo or canonical-mode
   - Restore-on-signal handling
   - Cross-platform termios divergence (Linux vs Darwin syscall numbers)
   These are *non-deterministic without compiler oracle* — only a real test against a real terminal can validate them. PB's pytest suite drives via pipes (no real TTY), but the *non-interactive* paths still flush the corpus with new error→fix patterns.

2. **Score-table arithmetic failure pairs**
   - Off-by-one bonuses in fuzzy match
   - Tie-break ordering bugs
   These are precisely the kind of bug a Compiler Oracle CANNOT catch (compiles fine, scores wrong) — but the **probe** catches them at exactly one test resolution. Highest-density failure → fix dataset in the bench.

3. **Event-loop / state-machine failure pairs**
   - State transition errors (modal pattern: search → preview → result)
   - Race conditions between input reader goroutine and matcher goroutine
   Adds Go-concurrency pairs to the corpus (currently dominated by Python and Rust pairs).

4. **Render-diff failure pairs**
   - Cursor positioning errors on viewport scroll
   - ANSI escape sequence accumulation (color leak across redraws)

5. **Query-language parsing pairs**
   - Token-class confusion (`!^` vs `^!`)
   - Escape-sequence handling in query
   These mirror jq's filter-language pairs, reinforcing the corpus's "small DSL" parsing competence.

## What this makes faster beyond the immediate cluster

- **Every future TUI in any project** in C:\Dev\ becomes drastically faster. Hook's CLI, Aide's developer console, Determinex's own Tauri-frontend test harness — all benefit when the Oracle has fzf's TTY fixture as a reference.
- **The `_lib/fuzzy.go` artifact** is reusable across any fuzzy-search problem in the codebase (ranked results in IDE autocomplete, ranked file picker, etc.). Once locked, it becomes the canonical fuzzy-rank implementation Determinex ships.
- **The `_lib/tty_unix.go` artifact** is reusable for any future "interactive selector in a Go program" need.

## Compounding with already-locked tools

| Locked tool | Compounding effect |
|-------------|--------------------|
| zoxide      | None direct. |
| yj          | None direct. |
| ripsecrets  | None direct. |

(Anchor 2's compounding is forward-only — it builds the TUI fixture for downstream cluster tools.)

## Compounding with currently in-progress tools

| In-progress tool | Current % | Lift from fzf lock |
|------------------|-----------|--------------------|
| htmlq | 91.6% | None (no TUI; this is jq cluster). |
| shellharden | 87/100 | None (sharkdp/shell-lexer cluster). |
| **csview** | ~81% | **Significant**. csview's TUI rendering for CSV viewing maps onto fzf's render fixture. Expected lift to 90%+ in 1-2 attempts after fixture extraction. |
| **dutree** | ~54% | **Significant**. dutree's interactive disk-usage TUI maps onto fzf's render layer + tree-walker pattern (similar to broot). Expected lift to 70%+. |

## Training data emitted

For a 2,164-test target with ~7 attempts: **~30-50 high-quality training rows**.

## Strategic value

**fzf is the second highest-value anchor lock**, behind jq:
1. Builds the corpus's *only* interactive-tool fixture (jq, yj, htmlq, etc. are all non-interactive).
2. The matcher's score-arithmetic training pairs are uniquely high-density — every bug shows up exactly once and has exactly one correct fix.
3. The cluster has the highest absolute test count (5,452) of any anchor, so fixture reuse compounds maximally.
4. The Go ecosystem expansion means C1 (Engineer-v10-dsl, Qwen2.5-Coder fine-tune) gains domain coverage where Determinex was previously thin.

## Action when locked

1. Move artifact from `T:/determinex-programbench/<run>/junegunn__fzf.b56d614/source/` into `corpus/programbench/locked/fzf/`.
2. Extract:
   - `corpus/programbench/_lib/go/tty_unix.go`
   - `corpus/programbench/_lib/go/render.go`
   - `corpus/programbench/_lib/go/events.go`
   - `corpus/programbench/_lib/go/fuzzy.go`
3. Append WAL training pairs to `data/programbench_corpus.jsonl`.
4. Update `corpus/programbench/README.md` status board.
5. Smoke-test on csview with new render fixture — confirm projected lift.
6. Commit with tag `programbench-anchor-2-locked`.
