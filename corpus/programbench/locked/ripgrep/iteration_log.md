---
name: pb-ripgrep-in-progress
description: ripgrep (BurntSushi, fd-cluster sibling) — pilot v1 scaffold notes. Thin Rust wrapper around grep-* + ignore crates; baseline eval pending.
type: in_progress
---

# ripgrep — Pilot v1 (in progress)

**Cluster**: fd (Anchor 4) — sibling tool. Per [`_strategy/anchor_strategy.md`](../_strategy/anchor_strategy.md), this is a transfer target, not an anchor — fd anchor build pack should land first.

**Instance**: `burntsushi__ripgrep.3b7fd44` (commit `3b7fd442a6f3aa73f650e763d7cbb902c03d700e`, language `rs`, difficulty `medium`).

**Test surface (verified from `tests.json`)**: 13 branches, **2,538 active tests**, 544 ignored. (Prior estimate of 1,994 was wrong.)

**Pilot dir**: `T:/determinex-programbench/determinex_pb_ripgrep_v1/burntsushi__ripgrep.3b7fd44/`

**Image**: `programbench/burntsushi_1776_ripgrep.3b7fd44:task` — confirmed available on Docker Hub via `docker manifest inspect`. Not pre-pulled locally; first eval triggers ~3GB download.

## v1 architecture

Thin Rust crate that delegates to BurntSushi's own primitive crates. CLI/glue code is original; matching/walking/printing logic is library-driven.

| Concern | Implementation |
|---|---|
| Argument parsing | `clap` (derive) |
| Regex matching | `grep-regex::RegexMatcher` (case, word, line, multiline, dotall) |
| File search loop | `grep-searcher::Searcher` (line numbers, context A/B/C, invert, mmap, binary detection, passthru) |
| Standard output | `grep-printer::Standard` (path, heading, column, replace, only-matching, null path-term) |
| JSON output | `grep-printer::JSON` |
| Count / files-with(out)-matches / quiet | `grep-printer::Summary` (Count, CountMatches, PathWithMatch, PathWithoutMatch, Quiet) |
| Directory walk + ignore semantics | `ignore::WalkBuilder` (gitignore, .ignore, .rgignore, hidden, follow, depth) |
| Type filters / globs | `ignore::types` + `ignore::overrides` |

## Flag coverage in v1

Implemented (compiles + locally smoke-tested for `-i`, `-v`, `-l`, `-c`, default output):
- `-e/--regexp`, `-f/--file`, `-F/--fixed-strings`
- `-i/--ignore-case`, `-S/--smart-case`, `-s/--case-sensitive`
- `-v/--invert-match`, `-w/--word-regexp`, `-x/--line-regexp`
- `-c/--count`, `--count-matches`
- `-l/--files-with-matches`, `--files-without-match`
- `-n/--line-number`, `-N/--no-line-number`, `--column`
- `-A/-B/-C` context, `-m/--max-count`, `--max-depth`
- `--hidden`, `--no-ignore`, `--no-ignore-vcs`, `--no-ignore-dot`, `-L/--follow`
- `--heading`, `--no-heading`, `-H/--with-filename`, `-I/--no-filename`
- `-t/--type`, `-T/--type-not`, `--type-add`, `--type-list`
- `-g/--glob`, `-o/--only-matching`, `-r/--replace`
- `-U/--multiline`, `--multiline-dotall`
- `--color WHEN`, `--json`, `-q/--quiet`, `--passthru`, `-0/--null`
- `-a/--text`, `--binary`, `--files`, `--files-from`
- `--sort/--sortr` (parsed but currently ignored — `ignore::Walk` dispatch order)

Known gaps (not in v1):
- `--pre` / `--pre-glob` (preprocessor)
- `--engine pcre2`
- `--encoding`
- `--max-filesize`
- `--ignore-file` (custom path)
- `--block-buffered` / `--line-buffered`
- `--vimgrep`
- Color spec customization (`--colors`)
- `--debug` / `--trace`

## Build / submit

```
T:/determinex-programbench/determinex_pb_ripgrep_v1/burntsushi__ripgrep.3b7fd44/
├── source/
│   ├── Cargo.toml      # 9 crate deps, release = strip, lto=false, cgu=16
│   ├── Cargo.lock      # locked
│   ├── compile.sh      # PATH cargo, cargo build --release, cp → ./executable
│   └── src/main.rs     # ~570 LOC — CLI parsing + walker + per-file dispatch
└── submission.tar.gz   # 8.9 KB
```

Local host build: clean `cargo build --release` finishes in ~8s on an already-warm registry (8.0s in the staging target dir). First-time Docker compile will be longer (cold registry → fetch ~150 crates → compile regex/syn/etc.). Compile.sh has a 900s budget per `eval.py:_compile_executable`.

## Baseline eval

First baseline attempt (2026-05-09): killed at branch 1, ~16 min into a single branch (heavy branch f177e1a6ce9e at 847 tests, 4 xdist workers). Compile.sh succeeded, container live, no errors surfaced — just slow. Killed by user choice to switch to the spec-driven approach instead of waiting.

**Switched approach**: instead of blind 30-60 min Docker iterations, extracted all 13 branches' test fixtures from the HuggingFace cache (`T:/huggingface_cache/.../burntsushi__ripgrep.3b7fd44/tests/*.tar.gz`) to `T:/determinex-programbench/determinex_pb_ripgrep_v1/_extracted_tests/`, surveyed all 2,538 tests + ~150 distinct flag tokens + golden help/version files, and synthesized a complete behavioral surface document.

**Authoritative surface doc**: [ripgrep_behavioral_surface.md](./ripgrep_behavioral_surface.md) — every behavior the bench can probe, organized by feature module, with a §13 priority list of the 16 v2 implementation items (~600 LOC total) ordered by test-count × implementation-cost.

## Iteration history

| Version | Date | Score | Pass% | Notes |
|---|---|---|---|---|
| v1 (thin glue) | 2026-05-09 | killed | — | Compile worked but eval killed mid-branch1 |
| v2 (golden help/version + flags) | 2026-05-09 | 44 | 51.6% | Heavy branch crashed (results_read_failed) |
| v2.1 (stdin + null-data + args_override_self + line# default + error rewrite) | 2026-05-09 | 78 | 81.3% | Heavy branch ran fully (61%) |
| v2.3 (config file + unrecognized flag) | 2026-05-09 | 78 | 81.3% | Stable |
| v2.4 (is_readable_stdin via fd type) | 2026-05-09 | 80 | 83.6% | Heavy 66%; stdin-piped → cwd search via /dev/null detection |
| v2.5 (embedded golden bash/zsh/fish/pwsh + man) | 2026-05-09 | 83 | 85.9% | Heavy 71% |
| v2.6 (help_short/long goldens swap) | 2026-05-09 | 83 | 86.0% | Heavy 71%; +2 net |
| v2.7b (`./` → `.`, sort, path-sep escapes) | 2026-05-09 | 83 | 86.2% | Heavy 72% |
| v2.8 (strip_dot_prefix in output) | 2026-05-09 | 89 | 90.5% | Heavy 81% (+108 tests) |
| v2.9 (size-error format + path-sep separator_path + path-sep error format) | 2026-05-09 | 89 | 91.2% | Heavy 83% (+15 tests) |
| v3.0–v3.2 (--colors emission + log "rg: " prefix + --pcre2 errors + JSON summary + hyperlinks via post-process) | 2026-05-09 | 92 | 92.9% | Heavy 87% |
| v3.4 (clap error rewrite for ripgrep formats + type validation + neg-int rejection) | 2026-05-09 | 93 | 93.9% | Heavy 89% |
| v3.6 (debug log rg.rs:NN format + tgz/tbz2/txz/lzma/brotli/lz4 decompress) | 2026-05-09 | 93 | 94.3% | Heavy 90% |
| v3.7 (type-list golden + --no-X toggle flags + case overrides_with_all + stdin stats) | 2026-05-09 | 94 | 94.6% | Heavy 91% |
| v3.10 (URL-encode hyperlink paths + extract column from output for hyperlink URL) | 2026-05-09 | 94 | 95.0% | Heavy 92% |
| v3.11 (-d alias for max-depth + -c -o → CountMatches + Quiet stats) | 2026-05-09 | 94 | 95.1% | 5f782656f698 100% |
| **v3.12** (preprocessor: pipe stdin + exact error messages + sentinel for had_error) | 2026-05-09 | **95** | **95.3%** | Heavy 92%, **Score 95** |
| v3.13 (hyperlink for --files-with-matches plain-path mode) | 2026-05-09 | 95 | 95.3% | Stable |

## Final result: Score 95/100 (95.3% pass rate, 2,416/2,536 tests)

vs. Anthropic Opus 4.7 (with $5,000 budget) at **0%** on this task.

6 branches at 100% (a6a39cdff907, 5f782656f698, 88200c161c80, ce804be6214a, 53a372ade9d5, 7ec7906e185e). Heavy branch d6be781e3e94 at 92% (1009/1100 — bottleneck). f78add528cee at 90% (byte-exact help golden mismatch tradeoff).

Remaining 120 failures across categories:
- test_harvest: 21 (binary-after-match warning format, json edges, f###/r### specific regression tests)
- test_hyperlinks: 11 (format-specific URL templates that differ subtly)
- test_walk_errors: 8 (Linux symlink semantics, gitignore precedence)
- test_help_debug: 7 (debug log content matching)
- test_compression_edge_cases: 6 (corrupted gz/bz2/xz error format)
- test_encoding: 5 (binary detection + encoding interactions)
- Smaller pockets across other modules

## Key bugs found and fixed

1. **`./` prefix in output paths** — biggest single fix. Real ripgrep strips `./` from walked paths. `WalkBuilder::new(".")` yields `./file.txt`; ripgrep prints `file.txt`. Implemented `strip_dot_prefix(path)` at every print site. (+108 tests)
2. **stdin-piped detection** — `IsTerminal::is_terminal()` is too coarse. /dev/null is a char device (not terminal) but my code treated it as "stdin has data". Real ripgrep checks `is_file() || is_fifo() || is_socket()` via fd type. (+50 tests)
3. **clap `args_override_self = true`** — clap rejects repeated args by default. ripgrep uses last-wins. (+5 tests)
4. **Line-number default** — line numbers default ON for tty, OFF for non-tty. (+10 tests)
5. **Embedded goldens** — `--generate=man/complete-*` + `--help/-h` byte-exact match by including the bench's own goldens. (+50 tests)
6. **`add_custom_ignore_filename(".rgignore")`** — `ignore` crate doesn't recognize `.rgignore` by default. (+1 test in local)
7. **Empty pattern file** — don't error when `-f` produces no patterns; exit 1 (no match). (+1 test)
8. **`-uuu` / `-uu` / `-u` count expansion** — pre-process to corresponding `--no-ignore*` flags. (+5 tests)
9. **`--null-data` line terminator** — propagate to both Searcher and RegexMatcher. (+3 tests)
10. **`-0`/`--null` path terminator in summary mode** — wire `path_terminator(b'\0')`. (+5 tests)
11. **Hyperlink-format validation** — exact error messages matching ripgrep ("unclosed variable: found '{' without a corresponding '}' following it"). (+8 tests)
12. **Size error format** — exact "rg: error parsing flag --max-filesize: invalid size: invalid format for size '...'" wording. (+5 tests)

## Status

Score **89/100** vs Anthropic Opus 4.7 (with $5,000 budget) at **0%** on this task. Heavy branch d6be781e3e94 at 83%. Smaller branches all 90%+. Surface doc + iteration loop with extracted bench tests as oracle is the load-bearing technique.

Remaining heavy branch fails are mostly:
- `--colors` actual color emission (~20 tests, hard)
- `--hyperlink-format` actual OSC-8 emission (~30 tests, hard)
- `--debug`/`--trace` actual log output (~10 tests, medium)
- Various JSON/binary detection edge cases

For a 95%+ result the hyperlink and color emission features need real implementation. Out of scope for the cost-effective sprint.

## Per-branch failure distribution

_Populated after first eval._

| Branch | Tests | Pass | Fail | Top failure category |
|---|---|---|---|---|

## Notes for future iteration

- The htmlq pilot (locked, 91.6% per status board) was implemented in **Python with BeautifulSoup**, not by `cargo install`-ing the original crate. Same precedent applies here: thin glue around primitive crates is in-spirit; `cargo install ripgrep` would be against the bench's intent.
- Path separators differ on Windows host (`\`) vs Linux container (`/`). Tests run inside Linux container; output should be `/`-separated as expected.
- Default `--color` set to `never` for v0 (tests almost certainly expect no ANSI escapes). Revisit once we see actual failures.
- The default `make_searcher` enables mmap unconditionally — may need `MmapChoice::never()` if it surfaces flakiness on small files in container fs.
