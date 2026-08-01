---
name: anchor-fzf
description: Anchor 2 — fzf. Fuzzy match algorithm + termios raw mode + double-buffered TUI render. The rosetta stone for every interactive terminal tool. PB tests almost certainly drive --filter mode (non-interactive) for the bulk of the test count.
type: anchor-pack
---

# Anchor 2 — fzf

| Field | Value |
|-------|-------|
| Repo | `junegunn/fzf` |
| Commit | `b56d614ba2f901c64eed454f181badec0b1cedff` |
| Instance ID | `junegunn__fzf.b56d614` |
| Reference language | Go |
| Recommended impl language | **Go** (matches reference; goroutine concurrency for reader/matcher/render) |
| ProgramBench rank | #1 |
| Test count | **2,164** across 11 branches |
| Difficulty | medium |

## Cluster (unlocks at 100% native)

| # | Tool | Tests | Ceiling | Transfer kind |
|---|------|-------|---------|---------------|
| #53 | peco   | 1,224 | 76.7% | direct (smaller, simpler fzf — same matcher + TUI) |
| #22 | nnn    | 477   | 98.1% | partial (file manager — TTY/render transfers, FS model is new) |
| #87 | walk   | 470   | 74.3% | partial (interactive walker — TTY transfers) |
| #32 | tig    | 1,586 | 83.9% | partial (Git TUI — TTY/event-loop transfers, Git domain is new) |
| #52 | htop   | 693   | 85.1% | partial (process viewer — render layer transfers, /proc is new) |
| #34 | broot  | 539   | 67.0% | partial (tree navigator — TTY transfers, tree model is new) |
| #80 | xplr   | 463   | 60.5% | partial (file explorer — TTY transfers, Lua plugins are extra) |

**Cluster total**: 7 tools, ~5,452 tests downstream.

## Sections

1. [01_architecture.md](01_architecture.md)
2. [02_fuzzing_surface.md](02_fuzzing_surface.md)
3. [03_implementation_sequence.md](03_implementation_sequence.md)
4. [04_transfer_map.md](04_transfer_map.md)
5. [05_corpus_impact.md](05_corpus_impact.md)
6. **[06_behavioral_spec.md](06_behavioral_spec.md)** — empirical behavioral surface from 842 CATCHES + 758 goldens; inject into builder prompt
