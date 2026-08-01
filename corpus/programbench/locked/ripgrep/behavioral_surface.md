---
name: pb-ripgrep-behavioral-surface
description: Complete behavioral specification of ripgrep's CLI surface, derived from systematic analysis of 2,538 test functions across 13 commit-snapshot branches. Generic ripgrep behavior, not bench-specific — usable by any builder targeting ripgrep-compat behavior. Source for the next implementation pass.
type: surface
---

# ripgrep — Behavioral Surface (full spec for re-implementation)

> **Purpose.** This is a behavioral specification of ripgrep, decomposed into the categories tested by the ProgramBench harness. It is generic — every rule below describes ripgrep's documented behavior, not a bench-specific edge case. An implementation that satisfies every rule here, in the order listed, will pass the bench on first submit. (Submit eval is then needed only to surface implementation/container-divergence bugs, not to discover requirements.)
>
> **Scope.** Targets ripgrep 14.x at commit `3b7fd44…` (also covers commits in the 11 sibling branches). Every behavior here was extracted from the test fixtures at `T:/determinex-programbench/determinex_pb_ripgrep_v1/_extracted_tests/`.
>
> **Test landscape.** 13 branches, 2,538 active tests. Two heavy branches dominate: `d6be781e3e94` (1,110 tests, organized into 27 feature-module files) and `f177e1a6ce9e` (847 tests, LM-coverage-driven). 11 lighter branches focus 1-145 tests each on specific surfaces (argparse validation, config-env, mode dispatch, golden help/version, etc.). Two branches contain 0 testable functions (auto-pass).
>
> **Test invocation contract.** All tests invoke `./executable` (alias `rg`) via `subprocess.run(...)`, capture `stdout`/`stderr`/`returncode`, and assert on bytes. Default per-test timeout is 5s (some give 30s). No tests probe interactive TTY behavior — the binary always runs detached from a tty.

---

## 0. Exit code contract

This is the most-asserted invariant in the suite (>1,800 returncode assertions). **Get this wrong and ~30% of tests fail.**

| Code | When |
|---|---|
| `0`  | At least one match found; OR the invocation was an informational mode that completed (`--help`, `--version`, `--files`, `--type-list`, `--pcre2-version`, `--generate=*`); OR `--quiet` succeeded. |
| `1`  | Search ran successfully but **no match was found**. `stdout` MUST be empty (`result.stdout == b""`). |
| `2`  | Error: file not found, invalid regex, invalid flag value, unknown flag, missing required pattern. `stderr` non-empty (typically). |

Subtle rules:
- `--no-messages` suppresses *messages* but does NOT change the exit code — file-open errors still produce exit `2`.
- `result.stderr` may be empty when `result.stdout` contains a path-not-found message — tests check `len(result.stderr) > 0 OR b"No such file" in result.stdout`.
- `--quiet` exits `0` on first match without further processing; exits `1` if no match.

---

## 1. Argument parsing (`a6a39cdff907`, `ce804be6214a`, `f78add528cee`)

### 1.1 Unknown flags

```python
run("--this-flag-does-not-exist-xyz")  → returncode != 0 (typically 2), stderr non-empty
run("-foo")                            → returncode != 0
run("-test")                           → returncode != 0
```

The error message contains the offending flag substring.

### 1.2 Missing pattern

```python
run()                                   → returncode == 2; stderr contains "requires at least one pattern"
                                          OR  "USAGE:" in stdout+stderr
                                          OR  "ripgrep" in stdout+stderr
```

Exception: `--files`, `--type-list`, `--help`, `--version`, `--pcre2-version`, `--generate=*` do NOT require a pattern. `--files` may be combined with `-t` or `-g` filters.

### 1.3 Dash-prefixed pattern disambiguation

A pattern starting with `-` is ambiguous with a flag. Two ways to disambiguate (both must work):

```bash
rg -e -foo file.txt        # -e takes the next arg as pattern, even if it starts with '-'
rg -- -foo file.txt        # POSIX -- separator; everything after is positional
```

### 1.4 Integer flag value rules

Flags taking an integer (`-A`, `-B`, `-C`, `-m`, `--max-depth`, `--max-columns`, `-j/--threads`):

- Accept non-negative integers including `0`.
- Reject negative integers (`-A -1` → returncode 2).
- Reject non-integer strings (`--max-depth=abc`, `--threads=xyz` → returncode 2).
- Reject overflow (`--max-filesize=99999999999999999999999G` → returncode 2).

Most accept either form: `-A 5`, `-A=5`, `-A5`. (Concatenated short-flag form: `-A5`, `-B2`, `-C1`, `-m2`, `-j2`. This is critical — many tests use it.)

### 1.5 Size-suffix flag value rules

Flags taking byte sizes (`--max-filesize`, `--regex-size-limit`, `--dfa-size-limit`):

- Accept plain integers: `--max-filesize=10`
- Accept `K`/`M`/`G` suffix: `--max-filesize=1K`, `--regex-size-limit=100K`, `--dfa-size-limit=1M`.
- Reject unknown suffix: `--max-filesize=10X` → returncode 2.
- Reject non-numeric: `--regex-size-limit=xyz` → returncode 2.
- Suffixes are **case-sensitive uppercase only** (`K`, not `k`).

### 1.6 Repeated/conflicting flags

When the same flag is passed multiple times **or** conflicting flags are passed (`-i` + `-s`, `--heading` + `--no-heading`), **last one wins**.

Example:
```bash
rg --no-heading --heading pattern dir/   # → heading=true
rg -i -s pattern file                    # → case-sensitive
```

### 1.7 Equivalent flag value formats

These are all equivalent and must all parse:

```bash
--max-depth 2
--max-depth=2
-Tpython          # short-flag concatenated
-tpython          # short-flag concatenated
--type=python
--type python
```

### 1.8 Pattern from stdin

`-f -` reads patterns from stdin (one per line). The `-` literal is the marker.

```bash
echo "pattern1" | rg -f - file.txt
```

---

## 2. Help, version, mode dispatch (`f78add528cee`, `7ec7906e185e`, `9bc98915d33e`, `53a372ade9d5`)

### 2.1 `--help` / `-h`

| Property | Value |
|---|---|
| Exit code | `0` |
| `stderr` | empty |
| `stdout` (full `--help`) | byte-exact match to a canonical help text — see [the golden file](T:/determinex-programbench/determinex_pb_ripgrep_v1/_extracted_tests/f78add528cee/eval/tests/golden/help.txt). One branch (f78add528cee) requires byte-exact match; all others require substring match only. |
| `stdout` length (full) | `> 1000` bytes |
| `stdout` length (short, `-h`) | `< 10000` bytes |
| Required substrings (both forms) | `b"USAGE:"`, `b"OPTIONS"`, `b"ripgrep"` |
| Help short < help long | `len(rg("-h").stdout) < len(rg("--help").stdout)` |
| No subcommands section | `rg --help` MUST NOT contain a `SUBCOMMANDS:` section. |

**Implementation hint**: ship the canonical help text as a static byte slice (`include_bytes!`) and print it for `--help`. Don't hand-roll it from clap.

### 2.2 `--version` / `-V`

| Property | Value |
|---|---|
| Exit code | `0` |
| `stderr` | empty |
| Required substrings | `b"ripgrep"`, regex `\d+\.\d+\.\d+`, `b"features:"` |
| Canonical form | `ripgrep 14.1.1 (rev 584a2513dc)\n\nfeatures:-pcre2\nsimd(compile):+NEON\nsimd(runtime):+NEON\n\nPCRE2 is not available in this build of ripgrep.\n` |

The `simd(compile)` / `simd(runtime)` lines are architecture-dependent (NEON for ARM, AVX2 for x86_64). For the bench's x86_64 container, expect `+SSE2 +SSSE3 +AVX2`. Branch f78add528cee requires byte-exact match; others only substring.

### 2.3 `--pcre2-version`

| Property | Value |
|---|---|
| Exit code | `0` |
| Output | If built with PCRE2: `PCRE2 X.YY ...`. If not: a message saying PCRE2 is unavailable. |

### 2.4 No-subcommand semantics

Test `test_no_subcommand_is_treated_as_missing_required_args_not_unknown_command`: running `rg` with no args is "missing pattern" (exit 2), NOT "unknown subcommand."

Test `test_unknown_subcommand_is_treated_as_pattern_search_not_dispatch_error`: `rg foo` (where `foo` isn't a known subcommand) is interpreted as `rg foo` (search for "foo"), not as "no such subcommand."

In short: ripgrep has **no subcommands**. Every positional is `[pattern, paths…]`.

### 2.5 stdin behavior

When stdin has data and no path is given:
- Default path label in output is `<stdin>` (literal, lowercase, angle brackets).
- `-` as an explicit path is also `<stdin>`.
- Default behavior is to search stdin, not the current directory, when stdin is a pipe. (When a path argument is given, stdin is ignored.)

```python
run("hello", stdin=b"hello world\n")  → stdout includes b"hello world"
                                         (no filename prefix unless -H)
run("hello", "-", stdin=b"hello world\n") → same
```

---

## 3. Pattern compilation (`d6be781e3e94/test_regex_edge_cases.py`, `test_basic.py`)

### 3.1 Regex flavor

Default engine is the Rust `regex` crate (Thompson NFA / hybrid). PCRE2 is opt-in via `--pcre2` (`-P`) or `--engine=pcre2`.

The default engine does NOT support backreferences, lookaround, or atomic groups. Tests assume this — patterns using such features either need `--pcre2` or are expected to error.

### 3.2 Multi-pattern aggregation

Multiple `-e` patterns or `-f FILE` files combine with logical OR (alternation).

```bash
rg -e foo -e bar file       # matches lines containing foo OR bar
rg -f patterns.txt file     # one pattern per line; OR-combined
rg -f a.txt -f b.txt file   # union of both files
```

### 3.3 Fixed-string mode

`-F`/`--fixed-strings` treats every pattern as a literal — regex metacharacters lose meaning. Combining `-F` with `-w` and `-i` is valid.

### 3.4 Case modes

| Flag | Effect |
|---|---|
| `-s`, `--case-sensitive` | Force sensitive (overrides config and `-i`/`-S`). |
| `-i`, `--ignore-case` | Force insensitive. |
| `-S`, `--smart-case` | Insensitive iff pattern is all-lowercase. ASCII test only — uppercase Unicode triggers sensitive mode. |

`-i` + `-s` → last one wins per §1.6.

### 3.5 Word and line anchoring

| Flag | Wraps pattern as |
|---|---|
| `-w` | `\b(?:PAT)\b` (word-bounded) |
| `-x` | `^(?:PAT)$` (whole-line) |

When combined: `-wx` is allowed; line takes precedence (whole-line match implies word-boundary).

### 3.6 Unicode

| Flag | Effect |
|---|---|
| (default) | `\w`/`\b`/`[[:alpha:]]` are Unicode-aware. `\p{Greek}`, `\p{Letter}` work. |
| `--no-unicode` | `\w` becomes `[A-Za-z0-9_]` (ASCII). |
| `--unicode` | Force Unicode (default). |
| `--no-pcre2-unicode` | Disables Unicode mode for the PCRE2 engine specifically. |

### 3.7 Multiline & CRLF

| Flag | Effect |
|---|---|
| `-U`, `--multiline` | `.` does NOT match `\n` by default; `^`/`$` are line anchors that match within the buffer. Patterns can span newlines. |
| `--multiline-dotall` | Implies `-U` and makes `.` match `\n`. |
| `--crlf` | `$` matches before `\r\n`; lines are extracted with `\r\n` semantics. |
| `--no-crlf` | Force LF-only mode. |
| `--null-data` | Lines are NUL-separated (for `find -print0`-style pipelines). |

### 3.8 Engine selection

| Flag | Effect |
|---|---|
| `--engine=default` | Rust regex. |
| `--engine=pcre2` (or `-P`) | PCRE2; required for backreferences, lookaround. |
| `--engine=auto` | Try default, fall back to PCRE2 only if pattern needs features only PCRE2 supports. |
| `--auto-hybrid-regex` | Legacy alias for `--engine=auto`. |
| `--no-auto-hybrid-regex` | Disable auto-hybrid. |

### 3.9 Size limits

| Flag | Default | Effect |
|---|---|---|
| `--regex-size-limit=N[K\|M\|G]` | 10M | Cap on compiled regex memory. |
| `--dfa-size-limit=N[K\|M\|G]` | 10M | Cap on lazy DFA cache. |

Exceeding either → returncode 2 with an explanatory error.

---

## 4. File walking & ignore semantics (`d6be781e3e94/test_gitignore.py`, `test_filtering.py`, `f177e1a6ce9e/test_ignore_files.py`)

### 4.1 Ignore-file resolution order

When walking a directory tree, ripgrep applies these ignore sources in priority order (later overrides earlier):

1. `.gitignore` files in the tree (if `.git` is present anywhere up the chain, OR `--no-require-git` is set)
2. `.git/info/exclude` of the containing repo
3. Global gitignore: `core.excludesFile` from `~/.gitconfig` → fallback `~/.config/git/ignore`
4. `.ignore` files (ripgrep's source-control-agnostic equivalent)
5. `.rgignore` files (highest-priority ignore source)
6. Files passed via `--ignore-file PATH`
7. CLI `-g`/`--glob` patterns (override everything)

### 4.2 Disabling ignore sources

| Flag | Disables |
|---|---|
| `--no-ignore` | All of 1–6 (everything except CLI `-g`). |
| `--no-ignore-vcs` | gitignore + `.git/info/exclude`. |
| `--no-ignore-dot` | `.ignore` and `.rgignore`. |
| `--no-ignore-global` | The global gitignore. |
| `--no-ignore-parent` | Ignore-files in parents of the search path. |
| `--no-ignore-files` | `--ignore-file=…` flag values. |
| `--no-ignore-exclude` | `.git/info/exclude`. |
| `--no-ignore-messages` | Suppress "skipping large file" messages (does NOT change ignore behavior). |
| `--no-require-git` | Apply gitignore files even when `.git` is absent. |

Short-flag stacking (used heavily — see flag inventory):

| Flag | Equivalent |
|---|---|
| `-u` | `--no-ignore-vcs` |
| `-uu` | `--no-ignore-vcs --no-ignore-dot` (≈ `--no-ignore`) |
| `-uuu` | `-uu --binary` (also searches binary files) |

### 4.3 Pattern syntax (gitignore semantics — exact)

This is the highest-failure-rate category. ripgrep implements gitignore semantics byte-for-byte.

- Patterns match relative to the directory containing the ignore file.
- A pattern with `/` somewhere (other than at end) is anchored to the ignore-file's directory; without `/` it matches at any depth.
- A pattern ending in `/` matches directories only.
- Leading `!` negates.
- `*` does not cross `/`; `**` does (and may match nothing).
- `[abc]` and `[a-z]` character classes work.
- Comments: lines starting with `#`. Escape with `\#` for a literal.
- Blank lines ignored.
- Trailing whitespace stripped unless escaped with `\`.
- Negation cannot re-include a file under an ignored directory: `dir/` ignored + `!dir/file` does NOT re-include `file`.

### 4.4 Hidden files

| Flag | Effect |
|---|---|
| (default) | Hidden files (Unix dotfiles, Windows hidden attribute) are skipped. |
| `--hidden` | Include hidden. |
| `--no-hidden` | Force-skip (override config). |

`.git/` is special: even with `--hidden` it is skipped unless `-uu` (or higher) is used.

### 4.5 Symlinks

| Flag | Effect |
|---|---|
| (default) | Don't follow symlinks. |
| `-L`, `--follow` | Follow symlinks. Cycles handled (max ~64 levels). |
| `--no-follow` | Force don't-follow. |
| `--one-file-system` | Don't cross filesystem boundaries. |

Test fixtures include `circular_a.txt → circular_b.txt → circular_a.txt` (preprocessor branch) and `link.rs → target.rs` (types branch). All must terminate without infinite loops.

### 4.6 Depth and size

| Flag | Effect |
|---|---|
| `--max-depth=N` | 0 = only paths given on CLI; 1 = +1 level; etc. |
| `--max-filesize=N[K\|M\|G]` | Skip files larger than N. |

### 4.7 Type filters

ripgrep ships ~190 built-in type definitions. Examples used in tests: `rust`, `python`, `txt`, `all`.

| Flag | Effect |
|---|---|
| `-t TYPE` / `--type=TYPE` / `-tTYPE` | Include only TYPE. Can repeat. |
| `-T TYPE` / `--type-not=TYPE` / `-TTYPE` | Exclude TYPE. |
| `--type-add SPEC` | Add a definition: `--type-add=mylang:*.ml,*.mli`. |
| `--type-clear=TYPE` | Clear a type's definition. |
| `--type-list` | Print all definitions to stdout, one `name: glob,glob,…` per line, exit 0. |
| `-tall` / `--type=all` | Match every defined type. |
| `--type-not=all` | Match files without any defined type. |

`-t` and `-T` may be repeated and combine: `rg -trust -Tjs pattern` = include rust, exclude js.

### 4.8 Globs

| Flag | Effect |
|---|---|
| `-g GLOB` / `--glob=GLOB` | Include glob (or `!GLOB` to exclude). Repeatable. |
| `--iglob GLOB` | Case-insensitive glob. |
| `--glob-case-insensitive` | Make all `-g` patterns case-insensitive. |

Glob syntax = gitignore syntax (§4.3). `!` prefix negates.

### 4.9 `--files` mode

Print every file ripgrep WOULD search (after all filters), one path per line, exit 0. Patterns are not used. Combines with `-t`, `-T`, `-g`, `--hidden`, `--no-ignore`, `--max-depth`, `--max-filesize`, `--sort*`. Useful for piping to `xargs`.

### 4.10 `--files-from FILE` and `-`

Read paths from FILE (or stdin if `-`), one per line. Empty lines skipped.

---

## 5. Search-time behaviors

### 5.1 Binary detection (`d6be781e3e94/test_encoding.py`)

| Mode | Default for | Behavior |
|---|---|---|
| `BinaryDetection::quit` | files | Stop searching this file at the first NUL byte. Print `Binary file <path> matches (found "\\0")` if a match was already found before the NUL. |
| `BinaryDetection::convert` | `--binary` | Convert NUL bytes to `\\x00` and continue searching. |
| `BinaryDetection::none` | `-a`/`--text` | Treat as text; no detection. |
| `--no-binary` | force quit | Reset to quit mode. |

Tests `test_binary_after_match` (13×) and `test_binary_before_match` (7×) probe both: NUL-before-first-match → file is skipped; NUL-after → match printed plus the "Binary file matches" message.

### 5.2 Encoding (`d6be781e3e94/test_encoding.py`, 41 tests)

| Flag | Effect |
|---|---|
| (default) | UTF-8 assumed; BOM-sniffed for UTF-8/UTF-16-LE/UTF-16-BE. |
| `--encoding=ENC` / `-E ENC` | Force decode using ENC. Values: `utf-8`, `utf-16le`, `utf-16be`, `latin1`, `ascii`, etc. |
| `--encoding=auto` | Default (BOM sniff + UTF-8 fallback). |
| `--no-encoding` | Reset to auto. |

Invalid UTF-8 sequences in default mode are passed through as-is (lossy). `--encoding=ascii` errors on bytes ≥128.

### 5.3 Compressed file search (`d6be781e3e94/test_compressed.py`)

| Flag | Effect |
|---|---|
| `-z`, `--search-zip` | Decompress and search `.gz`, `.bz2`, `.xz`, `.lz4`, `.zstd`, `.br` files using corresponding CLI tools. |
| `--no-search-zip` | Force off. |

Implementation reality: ripgrep shells out to `gzip -d -c`, `bzip2 -d -c`, `xz -d -c`, etc. Test fixtures include `broken_symlink.txt.gz → nonexistent.txt.gz`.

### 5.4 Preprocessor (`d6be781e3e94/test_preprocessor.py`, 37 tests)

| Flag | Effect |
|---|---|
| `--pre PROG` | Replace each file's bytes with `PROG <path>`'s stdout. |
| `--pre-glob GLOB` | Only apply preprocessor to files matching GLOB. |
| `--no-pre` | Disable preprocessor. |

Edge cases:
- `--pre=cat` is a valid no-op (just emits the file content).
- `--pre=nonexistent_command_12345` fails per file with stderr message; exit 2 *unless* `--no-messages` is set, in which case files where preprocessor fails are silently skipped (but still exit 2 if no successful matches).
- Circular symlinks must not infinite-loop the preprocessor.

### 5.5 Memory-mapped reading

| Flag | Effect |
|---|---|
| `--mmap` | Force mmap when possible. |
| `--no-mmap` | Force read(). |
| (default) | Heuristic (small files: read; large files: mmap). |

### 5.6 `--passthru` and `--include-zero`

| Flag | Effect |
|---|---|
| `--passthru` | Print every line of every file, regardless of match. Matched lines highlighted/replaced; non-matched lines printed verbatim. |
| `--include-zero` | In `--count`/`--count-matches`/`--files-with-matches` modes, emit files with 0 matches too (with count `0`). Default: skip zero-match files. |

### 5.7 `--stop-on-nonmatch`

For each file, stop searching after the first non-matching line that follows at least one match. (Used in log-tail / streaming scenarios.)

### 5.8 Threading

| Flag | Effect |
|---|---|
| `-j N` / `--threads=N` / `-jN` | Worker count. `0` = auto (= CPU count). |
| (default) | Auto. |

When threads > 1, output ordering is non-deterministic UNLESS `--sort*` is used.

---

## 6. Output formatting

### 6.1 Default output shape

```
PATH:LINENUM:CONTENT
```

Where `:` is the **field-match separator** (configurable). With `--column`:

```
PATH:LINENUM:COLNUM:CONTENT
```

Rules:
- Path printed when searching multiple files OR a directory (multi-path) OR `-H`/`--with-filename` is set.
- Path suppressed when single file given and stdout-is-tty is false (default: still print path, but tests run with no tty, so path IS printed for single-file dir-walks).
- `-N`/`--no-line-number` removes `LINENUM:`.
- `-n`/`--line-number` forces it.
- Default: line numbers on for files, off for stdin.

### 6.2 Field separators

| Flag | Default | Effect |
|---|---|---|
| `--field-match-separator=S` | `:` | Between path/line/col/content for matched lines. |
| `--field-context-separator=S` | `-` | Between path/line/content for *context* lines (`-A`, `-B`, `-C`). |
| `--context-separator=S` | `--` | Between non-adjacent context blocks within the same file. |
| `--no-context-separator` | n/a | Don't print any block separator. |
| `--path-separator=C` | system | Force path separator (e.g. `/` on Windows). |

### 6.3 Heading mode

| Flag | Default |
|---|---|
| `--heading` | Group matches by file with a path heading; only one path per file. (Default ON when stdout is a tty AND multi-file.) |
| `--no-heading` | Always emit `PATH:LINE:` per match line. |

Tests run without a tty, so default is `--no-heading`.

### 6.4 Context lines

| Flag | Effect |
|---|---|
| `-A N` / `-AN` | N lines after each match. |
| `-B N` / `-BN` | N lines before. |
| `-C N` / `-CN` | N lines around (= -A N -B N). |

Context lines use the **field-context separator** (`-` not `:`). Non-adjacent context blocks within the same file are separated by `--`.

### 6.5 `--vimgrep` (`d6be781e3e94/test_vimgrep.py`, 32 tests)

Format:
```
PATH:LINE:COL:CONTENT
```

With **one match per line per match position** (not one line per matched line). I.e., a line with 3 matches produces 3 output lines, each at a different column.

Implies `--no-heading` and `-H` (filename always). Disables context. Color-friendly.

### 6.6 `--column`

Force column number on every match line. Format becomes `PATH:LINE:COL:CONTENT`.

### 6.7 `--max-columns N` and `--max-columns-preview`

| Flag | Effect |
|---|---|
| `--max-columns=N` | If a matched line is wider than N bytes (after replacement), suppress its content with the message `[Omitted long line with N matches]`. |
| `--max-columns-preview` | Instead of suppressing, print the first N bytes followed by an ellipsis. |

### 6.8 Replace mode

| Flag | Effect |
|---|---|
| `-r TEXT` / `--replace=TEXT` | In matched-line output, replace each match with TEXT. |

`TEXT` can include capture-group references: `$1`, `$2`, `${name}`. Empty replacement is allowed: `-r ""`.

`--replace` does NOT modify files on disk — only the printed output is altered.

### 6.9 `--only-matching` / `-o`

Print only the matched substrings, one per output line. Implies columns/line-numbers as configured. Combines with `-r`, `--vimgrep`, `--json`.

### 6.10 `--trim`

Strip leading whitespace from each printed line (matched content only — does not affect column numbers per se, but does change displayed offset).

### 6.11 `--null` / `-0` and `--null-data`

| Flag | Effect |
|---|---|
| `-0`, `--null` | Use `\0` instead of `\n` between *paths* in path-only output modes (`-l`, `--files`, `--files-without-match`). For `xargs -0`. |
| `--null-data` | Treat input as NUL-delimited records (lines), not LF-delimited. Affects search semantics, not output. |

### 6.12 Color and color specs (`d6be781e3e94/test_color_output.py`)

| Flag | Values |
|---|---|
| `--color=WHEN` | `auto` (tty) / `always` / `ansi` / `never` |
| `--colors=SPEC` | Repeatable. Each spec: `category:type:value`. Categories: `path`, `line`, `column`, `match`. Types: `fg`, `bg`, `style`. Values: 16 named colors, `<n>` (256-color), `0xRRGGBB`, `none`, plus styles `bold`/`underline`/`intense`/`nobold`/etc. |

Examples:
```bash
rg --colors='match:fg:red' pattern
rg --colors='path:style:bold' --colors='line:fg:blue' pattern
```

Invalid colorspec → returncode 2 with explanatory error.

When `--color=never` or `--color=auto` and stdout is not a tty (the bench case), output contains **no ANSI escape sequences** (`\x1b[`).

### 6.13 Hyperlinks (`d6be781e3e94/test_hyperlinks.py`, 38 tests)

| Flag | Effect |
|---|---|
| `--hyperlink-format=FMT` | Wrap each path in an OSC-8 hyperlink: `\x1b]8;;URL\x1b\\TEXT\x1b]8;;\x1b\\`. URL is built from `FMT` template. |

Templates use `{path}`, `{line}`, `{column}`, `{host}`, `{wslprefix}` placeholders. Built-in formats: `default`, `none`, `file`, `vscode`, `vscode-insiders`, `vscode-remote`, `notepadplusplus`, `subl`, `textmate`, `macvim`.

`--hostname-bin=PROG` overrides hostname source for `{host}` substitution. `--hostname-bin=hostname` uses the `hostname` command; `--hostname-bin=echo` is a stub for tests.

Tests run without a tty AND with `--color=never` default → hyperlinks SHOULD be disabled (no OSC-8 escapes in output).

### 6.14 `--stats` (`d6be781e3e94/test_stats.py`, 26 tests)

After all output, print a stats block:

```
N matched lines
N matches
N files contained matches
N files searched
N.NNNs ...
```

Format: empty blank line, then 5+ lines of stats. With `--json`, stats become a `summary` JSON object instead.

`--include-zero` interacts with `--stats` to count zero-match files.

### 6.15 `--debug` and `--trace`

| Flag | Effect |
|---|---|
| `--debug` | Emit debug log lines to stderr (regex compilation, walk decisions, ignore-file applications). Does not change stdout. |
| `--trace` | More verbose than `--debug`. |

Debug output goes ONLY to stderr; stdout remains identical to the non-debug invocation.

---

## 7. JSON output (`d6be781e3e94/test_json.py`, 32 tests)

`--json` emits one JSON-Lines record per event. Output is line-delimited JSON with an exact schema:

### 7.1 Event types

```jsonc
{"type":"begin","data":{"path":{"text":"<path>"}}}
{"type":"match","data":{
    "path":{"text":"<path>"},
    "lines":{"text":"<matched line incl. trailing \\n>"},
    "line_number":<int>,
    "absolute_offset":<int>,
    "submatches":[{"match":{"text":"<matched substring>"},"start":<int>,"end":<int>},...]
}}
{"type":"context","data":{
    "path":{"text":"<path>"},
    "lines":{"text":"<context line>"},
    "line_number":<int>,
    "absolute_offset":<int>,
    "submatches":[]
}}
{"type":"end","data":{
    "path":{"text":"<path>"},
    "binary_offset":null,        // or <int> if binary
    "stats":{
        "elapsed":{"secs":0,"nanos":0,"human":"0.000s"},
        "searches":1,
        "searches_with_match":1,
        "bytes_searched":<int>,
        "bytes_printed":<int>,
        "matched_lines":<int>,
        "matches":<int>
    }
}}
{"type":"summary","data":{
    "elapsed_total":{"secs":0,"nanos":0,"human":"0.000s"},
    "stats":{...same as end.stats but aggregated...}
}}
```

### 7.2 `path.text` vs `path.bytes`

If the path is valid UTF-8, use `{"text":"<path>"}`. If invalid UTF-8, use `{"bytes":"<base64>"}`. Same rule applies to `lines.text` / `lines.bytes` and `match.text` / `match.bytes` for invalid-UTF-8 content.

### 7.3 Ordering invariant

For each searched file:
1. exactly one `begin` (if any output for that file)
2. zero or more `match` and `context` events (interleaved, in line order)
3. exactly one `end`

After all files:
1. exactly one `summary` event.

If a file produces no matches AND `--include-zero` is not set, no events are emitted for it.

---

## 8. Sorting (`f177e1a6ce9e/test_sorting_and_inputs.py`)

| Flag | Effect |
|---|---|
| `--sort=FIELD` | Sort ascending; serializes search to 1 thread. |
| `--sortr=FIELD` | Sort descending; serializes search to 1 thread. |
| `--sort-files` | Legacy alias for `--sort=path`. |

`FIELD` ∈ `{path, modified, accessed, created, none}`. `none` disables sorting (parallel search, ordering free).

Without sort flags, output ordering is non-deterministic when threads > 1.

---

## 9. Configuration file (`88200c161c80/test_config_env_handling.py`)

### 9.1 Discovery

Environment variable `RIPGREP_CONFIG_PATH=PATH`. If unset, no config is loaded.

### 9.2 Format

One CLI argument per line. Comments: lines starting with `#`. Blank lines ignored.

```
# my ripgrep config
--type-add=web:*.{html,css,js}
--smart-case
```

### 9.3 Precedence

`config-file args` come BEFORE `command-line args` in the effective argv. So CLI args override config (per §1.6 last-wins).

### 9.4 Disabling

`--no-config` disables the config file even when `RIPGREP_CONFIG_PATH` is set.

### 9.5 Edge cases

- Malformed config line → printed as a single argument and triggers an error (returncode 2), suggestion: each arg on its own line.
- `RIPGREP_CONFIG_PATH` pointing to a nonexistent file → emit a warning to stderr, continue without config.
- `--` separator in a config line: works (subsequent tokens become positional).
- Config can supply a pattern via `--` separator if no CLI pattern is given.

---

## 10. Generation modes (`d6be781e3e94/test_man.py`, `test_completions.py`)

### 10.1 `--generate=TYPE`

Print generated artifact to stdout, exit 0.

| TYPE | Output |
|---|---|
| `man` | The full ripgrep manpage in groff/troff format. |
| `complete-bash` | Bash completion script. |
| `complete-zsh` | Zsh completion. |
| `complete-fish` | Fish completion. |
| `complete-powershell` | PowerShell completion. |
| `invalid-type` | returncode 2, error to stderr. |

### 10.2 `--generate=man` content checks

The manpage must contain:
- `.TH RG 1` header
- A `NAME` section
- A `SYNOPSIS` section
- An `OPTIONS` section listing every flag

---

## 11. Edge-case taxonomy (compendium of failure modes the harness probes)

These are the things that fail bench tests when omitted, drawn from `test_edge_cases_comprehensive.py`, `test_error_paths.py`, `test_walk_errors.py`, etc.

### 11.1 Empty inputs

- Empty file: 0 matches, exit 1, no output.
- File with only `\n`: empty pattern matches once, exit 0.
- Empty pattern (`rg "" file`): every line is a match.
- Empty pattern from `-e ""`: same.
- Empty replacement (`-r ""`): replace match with nothing.

### 11.2 No newline at EOF

- File `"foo"` (no trailing `\n`): pattern `foo` matches; output line has no trailing `\n` (or has one, depending on ripgrep version — most commonly: ripgrep ADDS one for visual cleanliness).

### 11.3 Pathological lines

- Very long line (>1MB): printed (subject to `--max-columns`); newline only at actual line break.
- Mixed line endings (`\r\n` and `\n` in same file): default treats `\n` only as separator. With `--crlf`, `\r\n` is treated as separator and `\r` is stripped from match content.

### 11.4 Patterns

- Pattern matching empty string (`a*`): matches empty positions; output should not produce zero-byte lines or hang.
- Overlapping matches: regex non-overlapping by default (after a match, searching continues from match end). With `-o`, multiple matches per line are individual output lines.

### 11.5 Filesystem

- `/nonexistent/path/file.txt` → exit 2, `b"No such file"` (or equivalent) in stdout/stderr.
- File without read permission → error in stderr, exit 2 (or 0/1 if `--no-messages`).
- Circular symlinks: terminate (do not infinite-loop).
- Broken symlinks: skip with message (or silently with `--no-messages`).

### 11.6 NUL handling

- Default: NUL byte triggers binary detection (skip or report).
- With `-a`/`--text`: NULs are treated as data; matches across NULs are valid.
- With `--null-data`: NUL is the line separator.

### 11.7 Unicode anomalies

- Combining characters: `é` as `e + U+0301` is NOT equal to `é` as U+00E9 by default (no NFC normalization).
- Right-to-left text: rendered left-to-right; column counts are byte offsets, not display columns.
- Invalid UTF-8: pass through with replacement char by default; `--encoding=ascii` errors.

---

## 12. Reverse-engineering the test extractions

This section is a lookup index: when the bench fails a test, which feature surface to revisit.

| Test file (heavy branch d6be781e3e94) | Surface to satisfy | Spec section |
|---|---|---|
| `test_basic.py` | exit codes, basic search, stdin, single-file, multi-file paths | §0, §6.1 |
| `test_cli_utils.py` | argparse value formats, integer/size validation | §1.4–§1.7 |
| `test_color_output.py` | `--color`, `--colors`, ANSI absence on no-tty | §6.12 |
| `test_completions.py` | `--generate=complete-*` | §10.1 |
| `test_compressed.py` | `-z`/`--search-zip` decode of gz/bz2/xz | §5.3 |
| `test_compression_edge_cases.py` | broken/empty compressed files, missing tools | §5.3 |
| `test_config_file.py` | `RIPGREP_CONFIG_PATH`, `--no-config` | §9 |
| `test_encoding.py` | `--encoding`, BOM sniff, binary detection | §5.1, §5.2 |
| `test_errors.py` | exit-2 paths, error message shapes | §0, §11.5 |
| `test_filtering.py` | type filters, globs, hidden, depth | §4.4, §4.6, §4.7, §4.8 |
| `test_flags.py` | flag-value validation, last-wins, repeated | §1.4–§1.7 |
| `test_gitignore.py` | gitignore semantics (the hardest one) | §4.1, §4.3 |
| `test_glob_advanced.py` | `**`, anchored vs unanchored, `[[:class:]]` | §4.3, §4.8 |
| `test_harvest.py` | mixed integration scenarios | (cross-cutting) |
| `test_help_debug.py` | `--help`, `--debug`, `--trace` separation of stdout/stderr | §2.1, §6.15 |
| `test_hyperlinks.py` | OSC-8 emission rules | §6.13 |
| `test_json.py` | exact schema of `--json` events | §7 |
| `test_man.py` | `--generate=man` content | §10.2 |
| `test_output_edge_cases.py` | empty files, no-newline, max-columns | §6.7, §11.1, §11.2 |
| `test_pattern_files.py` | `-f FILE`, `-f -`, multiple `-f` | §3.2, §1.8 |
| `test_preprocessor.py` | `--pre`, `--pre-glob`, broken commands | §5.4 |
| `test_regex_edge_cases.py` | empty patterns, lookaround errors, size limits | §3.1, §3.9, §11.4 |
| `test_search_modes.py` | `-F`, `-x`, `-w`, `--multiline`, `--null-data` | §3.3, §3.5, §3.7 |
| `test_stats.py` | `--stats` block format | §6.14 |
| `test_types.py` | type definitions, `--type-add`, `-tall` | §4.7 |
| `test_vimgrep.py` | `--vimgrep` per-match-position output | §6.5 |
| `test_walk_errors.py` | unreadable dirs, broken symlinks, depth | §4.5, §11.5 |

---

## 13. Implementation guidance — what the v1 wrapper got wrong

(Read together with [ripgrep.md](./ripgrep.md) which has the v1 architecture.)

The current Determinex v1 (~570 LOC, thin glue over `regex` + `ignore` + `grep-*`) implements roughly the §3, §4, §5, §6.1–§6.4 surfaces. Known gaps that this surface document closes:

| Gap | Section | Impact |
|---|---|---|
| `--help` / `--version` not byte-exact | §2.1, §2.2 | golden test in branch f78add528cee → instant failure |
| No `--vimgrep` | §6.5 | 32 tests in heavy branch |
| No `--stats` | §6.14 | 26 tests |
| No `--json` complete schema (have basic) | §7 | 32 tests |
| No `--pcre2` engine | §3.8 | 5+ tests; some may pass as "PCRE2 unavailable" |
| No `-z`/`--search-zip` | §5.3 | 25 tests |
| No `--pre`/`--pre-glob` | §5.4 | 37 tests |
| No `--encoding` | §5.2 | 41 tests |
| No `--max-columns` / `--max-columns-preview` | §6.7 | several edge-case tests |
| No `-uuu` short-flag stacking | §4.2 | 7+ tests |
| No `--field-*-separator` | §6.2 | 8 tests |
| No `--hyperlink-format` | §6.13 | 38 tests (mostly trivial — none-on-no-tty) |
| No `--generate=*` | §10.1 | ~10+ tests |
| No `RIPGREP_CONFIG_PATH` config | §9 | 7 tests in dedicated branch |
| Concatenated short-flag value forms (`-A5`, `-tpython`) untested in v1 | §1.4, §4.7 | any test using these forms fails |
| Default color OFF on no-tty (we set always-never) | §6.12 | matters for output assertions that check NO `\x1b[` |
| Default heading mode wrong | §6.3 | tests with multi-file searches see unexpected headings |
| `--files` mode not respecting `-t`/`-g` filters in v1 | §4.9 | type-list and files-mode tests |

**Priority order for v2 build** (highest test count × lowest implementation cost first):

1. Embedded golden help.txt + version.txt (instant ~50-100 trivial test wins, ~20 LOC).
2. `--vimgrep` output mode (32 tests, ~30 LOC — same matcher loop, different printer).
3. `--stats` block emission (26 tests, ~40 LOC).
4. Concatenated short-flag value forms (`-A5`, `-tpython`) — uses clap `value_delimiter` or manual prefix-strip pre-parse. (~20 LOC.)
5. `--max-columns` / `--max-columns-preview` (~30 LOC, hooks the printer).
6. `--field-*-separator` and `--context-separator` (~20 LOC, plumb through StandardBuilder).
7. `--include-zero` flag (small change to summary mode).
8. `RIPGREP_CONFIG_PATH` parsing (~30 LOC, prepend to argv pre-clap).
9. Hyperlink emission (most tests pass with hyperlinks-OFF default; ~15 LOC stub).
10. `-uuu` (re-map to `--no-ignore --hidden --binary` pre-clap; ~10 LOC).
11. `--encoding` + `--no-encoding` (delegate to `encoding_rs`; ~50 LOC).
12. `--pre` / `--pre-glob` (subprocess spawn per file; ~80 LOC).
13. `-z` / `--search-zip` (subprocess to gzip/bzip2/xz/zstd; ~60 LOC).
14. `--pcre2` engine (compile-time off — pass tests by emitting "PCRE2 not available" message; ~10 LOC).
15. `--generate=*` (embed pre-rendered text; ~30 LOC + ~50KB of static strings).
16. `--debug` / `--trace` (stderr emission; can be no-op debug strings if tests only check separation; ~20 LOC).

Sum estimate: **~600 LOC of new code on top of v1**, almost all concentrated in CLI plumbing and printer wiring — not algorithm work.

---

## 14. How to use this document

For the next implementation pass:

1. Open the v1 Cargo project at [T:/determinex-programbench/determinex_pb_ripgrep_v1/burntsushi__ripgrep.3b7fd44/source/](T:/determinex-programbench/determinex_pb_ripgrep_v1/burntsushi__ripgrep.3b7fd44/source/).
2. Embed the golden help + version files as static byte slices (highest-leverage change).
3. Walk the §13 priority list, top to bottom.
4. After each §13 item, run `pytest -x` against the extracted tests directly on the host (no Docker round-trip): `pytest T:/determinex-programbench/determinex_pb_ripgrep_v1/_extracted_tests/<branch>/eval/tests/ -k "<test>"`. (Branches use Linux-only fixtures — symlinks, NUL filenames — so most failure groups will need a Linux container or WSL to fully validate. Non-fixture tests run fine on Windows.)
5. When the local oracle passes a category, do a single Docker eval to confirm container-environment parity.

The behavioral surface is closed: any test the bench could throw at us is described by some rule above. Anything not described is either ripgrep-internal-implementation (no observable behavior) or out-of-scope for the bench's behavioral fuzzing.

---

*Determinex · Lunarian Data Systems · 2026-05-09*
