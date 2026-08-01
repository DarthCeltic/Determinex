---
name: fd-transfer-map
description: Per-cluster-tool, the SPECIFIC sharkdp-portfolio idiom that transfers from fd. The walker, the clap conventions, the color scheme, the error format are universal across his tools.
type: transfer-map
---

# fd → Cluster Transfer Map

> **The strongest anchor of the five.** sharkdp's portfolio shares not just *patterns* but actual *code idioms* — clap derivations, error-format strings, color-scheme constants. Mastering one means the next four are 60-80% pre-solved.

| Tool | Bench # | Transfer | Specific knowledge that transfers | Additional work |
|------|---------|----------|------------------------------------|-----------------|
| **ripgrep** | #3 | Direct | The `ignore` crate (BurntSushi authored, sharkdp uses). The smart-case rule. The `--color always/auto/never` discipline. The clap-based CLI shape. Pattern parsing (regex/literal/glob). The pivot from path-match to **content-match** is the only big new piece. **The walker fixture transfers 1:1.** | Per-line content matching with multiline regex. `--type` (file-type-by-extension dict). `--context N`, `--before-context`, `--after-context`. `-l` (files-with-matches). `-v` (invert). `-c` (count). PCRE2 fallback. ~1500 LOC over fd's walker. |
| **hexyl** | #45 | Partial | clap conventions, color scheme, error format. hexyl is a hex dumper — entirely different domain. The transferable pieces are CLI plumbing and color/atty/`--color` discipline. | Hex formatting, color-by-byte-class (printable ASCII, control, NUL, etc.). Block/group display. `-n N` byte-count limit. `-s OFFSET` skip. Streaming from stdin. ~400 LOC. |
| **pastel** | #64 | Partial | clap conventions, color output (HEAVY use). pastel is a color-utility CLI. Subcommand structure: `pastel pick`, `pastel sort`, `pastel format`. clap subcommand handling transfers. | Color space conversions (RGB/HSL/Lab/HSV). Color picker in TTY. Color sort algorithm. Distance functions. ~800 LOC. **Color theory is novel** — not derivable from fd. |
| **onefetch** | #38 | Partial | clap conventions, error format, color usage. onefetch reads a Git repo and prints info; the *Git* part is new (libgit2 bindings or shelling to `git`). | git2 crate usage. Repo-stat aggregation. ASCII-art logo selection per language. Display formatting with side-by-side output. ~1000 LOC. |
| **shellharden** *(in progress)* | #78 | Partial | Most wrapper/plumbing lift has already landed in the 87/100 OpenAI comparison copy. shellharden is a bash linter — the remaining gap is shell lexical structure, not fd-style file walking or clap convention. | Shell lexer (POSIX + bash + zsh dialects). Quote-rewriting transformations. `--check` vs `--transform` modes. Next pass needs a lexical word model, not another fd-conformance pass. |
| **dust** | #39 | Partial | Walker fixture (`ignore` crate, depth, hidden) transfers directly. dust is `du` clone with tree-graph output. | Aggregation: sum size up the tree. Tree rendering with box characters. Color heat-map for big subtrees. ~600 LOC. |
| **dua-cli** | #68 | Partial | Walker fixture transfers. dua-cli is interactive (TUI) — has overlap with **fzf cluster** for the TTY layer. | TTY raw mode (lift from fzf if locked first), tree-walker model (lift from fd). Effectively requires both fd AND fzf to be locked first. ~700 LOC. |

## Compounding with already-locked / in-progress

- **shellharden (in progress, 87/100)** — fd-style conformance is no longer the bottleneck. Move toward 100 by building a shell lexical word model; see `corpus/programbench/in_progress/anordal__shellharden.6a6ffd4/iteration_log.md`.
- **dutree (in progress, ~54%)** — **wrong family**. dutree is by `nachoparker`, not sharkdp. Don't expect fd's fixture to lift dutree directly. The walker idea transfers but the conventions don't.
- **csview (in progress, ~81%)** — no overlap.
- **htmlq (in progress, 91.6%)** — no overlap.
- **zoxide / yj / ripsecrets (locked)** — no overlap (different CLI conventions).

## Reusable fixtures to extract after fd locks

- `_lib/rs/sharkdp_cli.rs` — clap derivation template with the standard sharkdp flags (`--color`, `-v`, `-h`, error format)
- `_lib/rs/walker.rs` — `ignore::WalkBuilder` configuration template with all the gitignore/hidden/depth knobs
- `_lib/rs/color.rs` — sharkdp's color scheme constants + `--color` handling
- `_lib/rs/error.rs` — `[<binary> error]: ` prefix formatter
- `_lib/rs/smart_case.rs` — Unicode-aware smart-case detector
- `_lib/rs/exec.rs` — placeholder substitution + spawn loop

These vendored into each cluster sibling's `Cargo.toml` as a path dependency under `corpus/programbench/_lib/rs/`.

## Anti-transfer notes

1. **ripgrep's content-matching engine is novel.** Streaming line-buffered regex with multi-line support is its own beast. Don't try to retrofit fd's filename-match path.
2. **pastel's color theory** is unrelated to fd's color *output*. The CLI scaffold transfers; the math doesn't.
3. **onefetch's libgit2 wiring** is independent of fd. The CLI scaffold transfers; the Git domain doesn't.
4. **dua-cli's TUI layer needs fzf, not fd.** fd contributes only the walker.

## Why this is the highest-quality anchor in the set

1. **Most tightly-coupled cluster.** Five tools by the same author with identical CLI conventions.
2. **Highest test density per shared idiom.** Every clap convention test passes for *every* sharkdp tool simultaneously when the fixture is right.
3. **Deepest cross-tool transfer.** fd → ripgrep is direct (not just CLI shape but actual ignore-crate config).
4. **Best documentation.** sharkdp's man pages and `--help` are extensive and consistent — the tests have ground truth.
5. **Largest cluster reachable**: in the optimistic case, 6 of 7 cluster tools (all except onefetch's Git domain or shellharden's shell-lexer domain) hit 100% with fd's fixture.
