---
name: fzf-transfer-map
description: Per-cluster-tool, the SPECIFIC fixture from fzf that transfers (matcher, TTY layer, render layer, event loop, field selector). Most cluster transfers are partial.
type: transfer-map
---

# fzf → Cluster Transfer Map

| Tool | Bench # | Transfer | Specific knowledge that transfers | Additional work |
|------|---------|----------|------------------------------------|-----------------|
| **peco** | #53 | **Direct** | Whole pipeline. peco is "fzf with simpler defaults and a Lua config". Reuse `algo/algo.go` (FuzzyMatchV2), `core/pattern.go`, `core/result.go`, `tui/render.go`, `tui/tty_unix.go` — almost line-for-line. peco's filter mode is identical syntax. | Lua config loader (PB tests probably skip; verify); slightly different default keybindings; YAML query language for `--query` (~50 LOC). |
| **nnn** | #22 | Partial | TTY raw-mode + render layer (`tty_unix.go`, `render.go`). nnn is a file manager with a fundamentally different model: a **directory listing**, not a **filtered list**. Reuse termios + render; rebuild navigation. | Directory walker (stdlib only — `os.ReadDir`). Selection model (cursor on a row, not multi-match). File-op bindings (delete, rename, copy). Plugin system (probably out of test scope). ~600 LOC over the TTY base. |
| **walk** | #87 | Partial | Same as nnn: TTY layer transfers; navigation model differs. walk is **simpler** than nnn — a tree-walker with arrow keys. Reuse termios + render + event-decoding from `events/events.go`. | Tree-walk model (recursive descent on demand). Result is a path emitted to stdout when Enter is pressed (walk's interactive-but-pipeable use case is almost the same as fzf's `--expect`). ~250 LOC. |
| **tig** | #32 | Partial | TTY layer + render layer + event loop. tig is a Git TUI; the *Git* part is huge (parse `git log`, `git diff`, `git blame` outputs). | Git output parsers (~800 LOC across log/diff/blame/refs/stash). Status views. Pager. tig's match-on-line search reuses fzf's matcher pattern but on a smaller surface. ~1500 LOC over the TTY base. |
| **htop** | #52 | Partial | Render layer (color, columns, headers). htop reads `/proc` for process state — that's the bulk of the new work. | `/proc/<pid>/stat` parser, `/proc/meminfo`, `/proc/cpuinfo`. CPU/MEM bars. Tree mode (parent/child). Sort/filter on column. ~1000 LOC. |
| **broot** | #34 | Partial | TTY raw-mode + render. broot is tree-navigator + integrated commands; ranking by relevance is fzf-adjacent. **Broot's verb engine is novel** — `:rm`, `:mv`, `:cp` etc. as in-TUI commands. | Tree pruner (broot's hallmark: collapsed tree showing only matches). Verb engine. Skin loader. ~1200 LOC. The TTY layer + matcher transfer is a significant kickstart. |
| **xplr** | #80 | Partial | TTY + render. xplr is **plugin-driven** — most behavior loaded from Lua. PB likely tests core file-listing and movement; the plugin system may or may not be on the surface. | File model + nav (~300 LOC). Lua bridge if tested (gopher-lua: ~500 LOC). The lower ceiling (60.5%) suggests Lua plugins are partially tested. |

## Compounding with already-locked / in-progress

- **zoxide (locked)** — no overlap; zoxide is non-interactive `cd`-replacement.
- **yj (locked)** — no overlap.
- **ripsecrets (locked)** — no overlap.
- **htmlq (in progress)** — no overlap with fzf.
- **shellharden (in progress)** — no overlap.
- **csview (in progress, ~81%)** — **has** overlap. csview is a CSV TUI viewer. The render layer + scroll/select cursor are exactly fzf's TTY layer. Once csview's render uses the fzf fixture, expect 81% → 90%+ in a single attempt.
- **dutree (in progress, ~54%)** — **has** overlap. dutree is interactive disk-usage; uses the same render-tree pattern as broot. The 54% indicates the tree model + render is the gap; fzf's render fixture should lift this 15+ points.

## Anti-transfer notes

- **Matcher transfer is high-quality** for peco only. nnn/tig/htop/broot/xplr do not need fuzzy matching at all (they may have *quick search*, not full fuzzy ranking). Don't force fzf's matcher into them.
- **Event loop transfer is partial across the cluster.** Each tool has its own keybinding semantics; the *primitive event-decoder* (read termios, emit `Action`) transfers, the dispatch table does not.
- **Color rendering transfers fully** but specific palettes per tool differ.

## Reusable fixtures to extract after fzf locks

- `_lib/tty_unix.go` — termios raw mode + restore
- `_lib/render.go` — double-buffered viewport with diff-redraw
- `_lib/events.go` — keystroke → `Action` enum decoder
- `_lib/fuzzy.go` — algo v2 with documented constants (peco-only direct reuse)
- `_lib/field.go` — `--delimiter`/`--nth`/`--with-nth` shared with later CSV tools

These go to `corpus/programbench/_lib/` (Go subtree) and the cluster siblings vendor them via `replace` directive in `go.mod`, or copy if module path tooling is too noisy in PB containers.
