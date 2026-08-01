---
name: fd-behavioral-spec
description: Empirical build brief for fd, derived from 519 CATCHES docstrings + 177 byte-exact golden output files across 10 ProgramBench test branches (1,365 active test functions). Injected into the builder prompt to drive a one-shot 100% lock.
type: behavioral-spec
---

# fd — Behavioral Build Spec

> **Read order.** Section 1 (binary contract) and Section 6 (pre-flight self-tests) are mandatory. Sections 4.4-4.6 (size filter, exec placeholders, output prefix) are the dominant 90→100% gap.
>
> **Empirical basis.** Extracted from `T:/determinex-programbench/_extracted_tests/sharkdp__fd.40d8eb3/`. 10 branches, heaviest is `ed161504d233` (527 tests across 17 files). Conftest uses **text mode** (`text=True`), 30-second timeout, custom `create_test_files` fixture for building file structures.

---

## Section 1 — Binary Contract

| Property | Value |
|---|---|
| Path | `./executable` (relative to build dir → `/workspace/executable` at test time) |
| Permissions | must be executable (`chmod +x`) |
| Invocation | `executable [FLAGS...] [PATTERN] [PATH...]` |
| Stdin | rare (some `--files-from` style flows); usually unused |
| Stdout | matched paths, one per line, prefixed with `./` for cwd-relative |
| Stderr | error messages, color codes when `--color always` |
| Working dir | tests use `pytest.tmp_path` set as `cwd` |
| Default search root | `.` (current working dir) when no positional path given |
| Env vars | `LLVM_PROFILE_FILE` is set by conftest (set yourself if not present) |

The conftest fixture (heavy branch `ed161504d233`):

```python
fd_binary = Path(__file__).parent.parent.parent / "executable"

@pytest.fixture
def run_fd(tmp_path):
    def _run(args, cwd=None, input_data=None, check=False):
        if cwd is None: cwd = tmp_path
        cmd = [str(fd_binary)] + args
        env = os.environ.copy()
        if "LLVM_PROFILE_FILE" not in env:
            env["LLVM_PROFILE_FILE"] = "/tmp/fd_test_%p.profraw"
        result = subprocess.run(cmd, cwd=str(cwd), capture_output=True,
                                text=True, input=input_data, timeout=30, env=env)
        if check: result.check_returncode()
        return result
    return _run

@pytest.fixture
def create_test_files(tmp_path):
    def _create(structure: dict, base=None):
        # structure[path] = None (dir), str (content), or int (size in bytes of '#')
        ...
    return _create
```

**Critical**: tests build a fresh tmp_path file structure per test, then run fd from that cwd with relative-path output. Output paths start with `./`. **Never emit absolute paths.**

---

## Section 2 — Test Invocation API

| Param | Meaning |
|---|---|
| `args` | List of CLI flags + pattern + paths |
| `cwd` | Working directory for the subprocess (defaults to `tmp_path`) |
| `input_data` | Optional stdin string |
| `check` | Default False; True asserts non-error exit |

The `create_test_files(structure)` fixture builds:
- `"dir1": None` → `tmp_path/dir1/` (directory)
- `"dir1/file.txt": "content"` → file with text
- `"large.bin": 1024` → file with 1024 `'#'` bytes

Tests then invoke `run_fd(args, cwd=tmp_test_dir)` and assert on `result.stdout` and `result.returncode`.

---

## Section 3 — Implementation Constraints

### Language: Rust (recommended) or Python

**Rust** matches the reference; uses `clap`, `ignore`, `regex`, `globset`, `rayon` crates. Compile cost in container: 90-180s cold.

**Python** workable for ~80% of tests but loses ground on:
- gitignore semantics (`pathspec` is close but not identical)
- regex engine differences (Python's `re` ≠ Rust's `regex`)
- parallel walker performance on the heavy branch

For first lock, **Python is acceptable**. For final 100%, Rust is safer.

### File layout

#### Rust:
```
compile.sh          ← cargo build --release && cp target/release/fd ./executable
Cargo.toml          ← [dependencies] clap = {derive}, ignore, regex, globset, rayon, atty, humantime
src/main.rs         ← entry + arg parse
src/walker.rs       ← ignore::WalkBuilder driver
src/filter.rs       ← type/size/extension/mtime filters
src/pattern.rs      ← regex/glob/literal compilation + smart-case
src/exec.rs         ← --exec / --exec-batch + placeholder substitution
src/output.rs       ← path formatting, --color, -l
src/error.rs        ← stderr conventions
```

#### Python:
```
compile.sh          ← chmod +x main.py; ln -sf main.py executable
main.py             ← entry point + argparse
walker.py           ← os.walk wrapper with gitignore (pathspec)
filter.py           ← all filter predicates
exec.py             ← subprocess + placeholder substitution
```

### compile.sh skeleton (Rust)

```bash
#!/bin/bash
set -e
export CARGO_HOME=/tmp/cargo
export CARGO_TARGET_DIR=/tmp/target
cargo build --release 2>&1 | tail -10
cp target/release/fd ./executable

# Pre-flight smoke (Section 6) — must pass or compile fails
mkdir -p /tmp/_smoke && cd /tmp/_smoke
touch a.txt b.txt
out=$(./executable txt 2>&1)
echo "$out" | grep -q "./a.txt" || { echo "smoke 1 fail (basic search)"; exit 1; }
exit 0
```

### Forbidden shortcuts

- **Do NOT** shell out to system `fd`. Behavior diverges from pinned commit.
- **Do NOT** emit absolute paths. Tests assert `"./file.txt"`, not `/tmp/.../file.txt`.
- **Do NOT** include `.profraw` files in stdout (some tests filter them out, but ideally don't write them in the cwd at all — set `LLVM_PROFILE_FILE` in your binary if needed, or leave the env-var alone).
- **Do NOT** sort output by default — fd's parallel walker emits in walk order. Tests that need sorting call `sorted(result.stdout.strip().split('\n'))`.

---

## Section 4 — Behavioral Surface

### 4.1 — Exit-code matrix (1,092 returncode assertions)

| Code | When |
|---|---|
| `0`  | Search completed successfully (matches found OR exec succeeded). |
| `1`  | No matches found AND `-x` was not used. |
| `2`  | Argument parse error (clap error). |
| 3+  | When `-x` runs commands, can pass through subprocess exit codes. |

Subtleties:
- Default behavior on no-match: exit `1`. Tests asserting `result.returncode == 0` for matched cases imply this.
- With `--exec` / `-x`: exit code reflects subprocess success.
- Empty result + `-x`: exit `1` (no commands run because no matches).

### 4.2 — Pattern modes

```
fd PATTERN              # regex, basename match (default)
fd -F PATTERN           # literal substring (--fixed-strings)
fd -g PATTERN           # glob (--glob)
fd -p PATTERN           # full-path regex (--full-path)
fd                      # no pattern → match everything (= `fd .`)
```

Smart-case is the default — pattern is case-insensitive iff it's all-lowercase. `-i` forces insensitive, `-s` forces sensitive.

| Pattern syntax | Mode | Example | Matches |
|---|---|---|---|
| `\.txt$` | regex | `\.txt$` | files ending `.txt` |
| `file[0-9]` | regex char class | `file1`, `file2` |
| `(rs\|py\|c)` | regex alternation | `test.rs`, `test.py`, `test.c` |
| `*.txt` | glob (with `-g`) | files ending `.txt` |
| `?.txt` | glob single-char | `a.txt` not `ab.txt` |
| `[abc].txt` | glob char class | `a.txt`, `b.txt`, `c.txt` |
| `app` | regex (substring fuzzy) | `apple`, `application` |

### 4.3 — Output prefix and path formatting

When fd is invoked from a cwd and finds a match, the output is the **relative path** with `./` prefix:

```bash
$ cd /tmp/test && touch a.txt
$ fd txt
./a.txt
```

If a positional path is given, the prefix uses that path:
```bash
$ fd txt /tmp/test
/tmp/test/a.txt
```

Tests in `test_path_display.py` assert this exact prefixing. **Don't strip `./`. Don't add it when search root is absolute.**

### 4.4 — Filter flags

#### Type filter (`-t`)

```
-t f      regular file
-t d      directory
-t l      symlink
-t x      executable
-t e      empty
-t s      socket
-t p      named pipe
-t b      block device
-t c      character device
```

Multiple `-t` are OR'd. `fd -t f -t d` matches files OR directories.

Compound: `-tf`, `-td` (no space) is also accepted: `fd -tf` ≡ `fd -t f`.

#### Extension filter (`-e`)

```
-e py    files ending in `.py` (case-insensitive)
-e PY    same
-e ""    files with no extension
-e a -e b   files ending in `.a` OR `.b`
```

#### Hidden / ignore

```
-H, --hidden          include hidden files (starting with .)
-I, --no-ignore       ignore .gitignore, .ignore, .fdignore
--no-ignore-vcs       only ignore .gitignore (keep .fdignore)
--no-ignore-parent    don't read parent dir ignore files
-u                    alias for --no-ignore --hidden
-uu                   alias for --no-ignore --hidden --no-ignore-vcs
-uuu                  alias for --no-ignore --hidden --binary
```

#### Depth

```
--max-depth N / -d N
--min-depth N
--exact-depth N
```

Default: unlimited. `--max-depth 1` means only direct children.

#### Size (the syntax that bites)

```
-S +1k          files >= 1000 bytes (SI: 1k = 1000)
-S -1k          files <= 1000 bytes
-S +1ki         files >= 1024 bytes (binary: 1ki = 1024)
-S 100b         files exactly 100 bytes
-S +1m          files >= 1,000,000 bytes
-S +1mi         files >= 1,048,576 bytes
```

Multiplier table (decimal/binary):
- `b` = 1
- `k` = 1000, `ki` = 1024
- `m` = 1,000,000, `mi` = 1,048,576
- `g` = 1,000,000,000, `gi` = 2^30
- `t` = 1,000,000,000,000, `ti` = 2^40

Multiple `-S` are AND'd: `fd -S +1k -S -2k` finds 1k-2k files.

**Off-by-one trap**: `+1k` means `>= 1000` (boundary INCLUDED). `-1k` means `<= 1000`. Tests verify boundary inclusion explicitly.

#### Mtime / atime / ctime

```
--changed-within DURATION    e.g. "1d", "30min", "2h", "1w"
--changed-before DURATION
--changed-within "2024-01-01"  ISO date also works
```

#### Owner (`--owner USER:GROUP`) — Unix only.

#### Glob filter (in addition to pattern):
```
-E PATTERN       --exclude (gitignore-style)
--ignore-file PATH
```

### 4.5 — Exec subsystem (`--exec` / `--exec-batch`)

```
fd PATTERN -x CMD ARGS... \;       # exec per match (one subprocess per file)
fd PATTERN -X CMD ARGS...          # exec batch (one subprocess, all files as args)
```

**Placeholder substitution** in CMD ARGS:

| Placeholder | Substituted with | Example: `./subdir/file.tar.gz` |
|---|---|---|
| `{}`  | full path | `./subdir/file.tar.gz` |
| `{.}` | path with extension stripped | `./subdir/file.tar` |
| `{/}` | basename | `file.tar.gz` |
| `{//}` | parent dir | `./subdir` |
| `{/.}` | basename without extension | `file.tar` |

**Implicit `{}`**: if no placeholder appears in ARGS, fd appends `{}` automatically:
```
fd txt -x echo
# ≡ fd txt -x echo {}
# Output: ./file1.txt\n./file2.txt
```

**For the root cwd**, `{//}` returns `.` (not empty, not `./`). Test verifies:
```
fd file -x echo {//} → "."  (for files in cwd)
                      → "./subdir" (for files in subdir)
```

**`{.}` strips ONLY the last extension**: `file.tar.gz` → `file.tar`. NOT `file`.

Multiple `-x` chains: `-x A {} \; -x B {}` runs both for each match.

### 4.6 — Output flags

```
-0, --print0      NUL-separator instead of newline
-l, --list-details  ls-like long format with mode, size, date
--color always|auto|never   default: auto (off when piped)
--hyperlink always|auto|never  OSC-8 terminal hyperlinks (test surface)
-1                limit to first match
-c, --count       print count instead of paths (rare)
-p, --full-path   pattern matches full path not basename
--strip-cwd-prefix   omit the `./` prefix
--format FORMAT   custom format string with placeholders
```

Format string placeholders for `--format`:
```
{}       full path
{/}      basename
{//}     parent dir
{.}      no-extension path
{/.}     basename no-extension
```

`--format "Path: {}"` prints `Path: ./file.txt` per match.

### 4.7 — Validation errors

| Trigger | Stderr substring (must appear) |
|---|---|
| Invalid regex `[unclosed` | `regex parse error` (exact format varies; clap+regex crate) |
| Invalid size `--size foo` | `invalid value 'foo' for '--size'` |
| Invalid type `-t z` | `invalid value 'z' for '--type'` |
| Invalid duration `--changed-within zzz` | `unknown duration` or similar |
| Unknown flag `--xyz` | `unexpected argument '--xyz'` (clap default) |
| Missing arg | clap-style usage error |

Exit `2` for argument parse errors. Stderr non-empty.

### 4.8 — Help / version

```
fd -h           # short help → stdout, exit 0
fd --help       # long help → stdout, exit 0
fd -V           # version → stdout, exit 0
fd --version    # alias
```

Help format: starts with `Usage: fd [OPTIONS] [pattern] [path]...`

Version format: `fd <version>`.

### 4.9 — Search-root behavior

```
fd                       # search ./ for everything
fd PATTERN               # search ./ for PATTERN
fd PATTERN PATH          # search PATH for PATTERN
fd PATTERN P1 P2 P3      # search multiple paths (multi-root)
```

When no PATTERN is given, fd matches everything. When no PATH is given, fd uses cwd.

The search root **does not appear in output** (only its descendants):
```
$ cd /tmp/test && touch a.txt
$ fd txt
./a.txt    # NOT "/tmp/test"
```

### 4.10 — Hidden / gitignore / dotfile behavior

By default fd:
- **Excludes** hidden files (starting with `.`)
- **Honors** `.gitignore`, `.ignore`, `.fdignore` in the search tree
- **Honors** parent-dir `.gitignore` (walks up to find them)
- **Honors** global gitignore at `$XDG_CONFIG_HOME/git/ignore`

Each is toggleable:
- `-H` to include hidden
- `-I` to ignore all ignore-files
- `--no-ignore-vcs` to keep `.fdignore` but ignore `.gitignore`
- `--no-ignore-parent` to not walk up

### 4.11 — Color output

`--color auto` (default): emit ANSI codes only when stdout is a TTY. PB tests always pipe → no color by default.

`--color always`: emit codes regardless. Color codes:
- directory: `1;34` (bold blue)
- symlink: `1;36` (bold cyan)
- executable: `1;32` (bold green)
- file: default (no codes)

Tests using `--color always` assert specific ANSI codes appear in stdout.

### 4.12 — Hyperlinks

`--hyperlink always` emits OSC-8 sequences:
```
\x1b]8;;file:///tmp/test/file.txt\x1b\\file.txt\x1b]8;;\x1b\\
```

27 tests touch this in the heavy branch. Implement only after the rest passes.

---

## Section 5 — Per-branch test landscape

10 branches, 1,365 active test functions.

| Branch | Tests | Focus |
|---|---|---|
| `ed161504d233` | 527 | Master suite — patterns, filtering, exec, edge cases, hyperlinks |
| `7af3fcb896a2` | 226 | Coverage improvements — edge cases, hidden/ignored, output format |
| `b05ae0c243fa` | 188 | Default-env vs custom-env vs and-extra-env (env-var handling) |
| `035fc64252a5` | 181 | Pattern matching, file types, hidden/ignored, output formatting, basic invocation |
| `c04bee337c86` | 172 | Edge cases, output, errors, filters, exec, hidden/ignored |
| `ff0f590898ed` | 50 | Spot |
| `d88e32789489` | 25 | `test_fd_behavior.py` — broad smoke tests |
| `e71fb88b88f4` | 25 | Spot |
| `6923ee32674b` | 1 | Single |
| `73abc4f3b5c7` | (varies) | Spot |

**Heavy file inventory in `ed161504d233`:**

| File | Tests | What |
|---|---|---|
| `test_harvest.py` | 99 | Cross-cutting: combos of flags |
| `test_output.py` | 46 | Output formatting, --color, --print0, -l |
| `test_exec.py` | 40 | --exec / --exec-batch + placeholders |
| `test_patterns.py` | 38 | regex / glob / fixed-strings |
| `test_type_filtering.py` | 36 | -t f/d/l/x/e/s/p, -e ext |
| `test_edge_cases.py` | 35 | misc edges |
| `test_filtering.py` | ~33 | size, time, owner |
| `test_traversal.py` | ? | depth, hidden, gitignore |
| `test_hyperlinks.py` | ? | OSC-8 |
| `test_exec_errors.py` | ? | exec failure paths |
| ... | ... | ... |

---

## Section 6 — Pre-flight self-tests (must pass in compile.sh)

```bash
mkdir -p /tmp/_fd_smoke && cd /tmp/_fd_smoke
rm -rf a.txt b.txt sub
touch a.txt b.txt
mkdir -p sub
touch sub/c.txt

# 1. Basic pattern match emits ./prefix paths
out=$(./executable txt | sort)
expected="./a.txt
./b.txt
./sub/c.txt"
[ "$out" = "$expected" ] || { echo "smoke 1 fail (basic search): $out"; exit 1; }

# 2. No-match exits 1
./executable nonexistent_xyz ; rc=$?
[ "$rc" -eq 1 ] || { echo "smoke 2 fail (no-match should be exit 1)"; exit 1; }

# 3. -t f filters to files only
out=$(./executable -t f | sort)
[ "$(echo "$out" | grep -c txt)" -ge 3 ] || { echo "smoke 3 fail (-t f)"; exit 1; }

# 4. -t d filters to dirs only
out=$(./executable -t d)
echo "$out" | grep -q "./sub" || { echo "smoke 4 fail (-t d)"; exit 1; }

# 5. -e txt extension filter
out=$(./executable -e txt | wc -l)
[ "$out" -ge 3 ] || { echo "smoke 5 fail (-e txt)"; exit 1; }

# 6. --max-depth 1
out=$(./executable -d 1 -t f | sort)
echo "$out" | grep -v "/sub/" >/dev/null && \
  ! (echo "$out" | grep "/sub/c.txt") || { echo "smoke 6 fail (depth)"; exit 1; }

# 7. -x exec with implicit {}
out=$(./executable txt -x echo)
[ "$(echo "$out" | wc -l)" -ge 3 ] || { echo "smoke 7 fail (-x echo)"; exit 1; }

# 8. -x echo {/} basename
out=$(./executable txt -x echo {/} | sort)
echo "$out" | grep -q "^a.txt$" || { echo "smoke 8 fail (-x {/})"; exit 1; }

# 9. -V exits 0
./executable -V > /dev/null || { echo "smoke 9 fail (-V)"; exit 1; }

# 10. -h exits 0
./executable -h > /dev/null || { echo "smoke 10 fail (-h)"; exit 1; }

echo "all smoke tests pass"
```

---

## Section 7 — Common failure modes (the 90→100% gap)

From inspection of 519 CATCHES docstrings.

### 7.1 — Output prefix traps

- Emitting absolute path instead of `./relative` → loses entire test_output / test_path_display cluster (~50 tests).
- Adding `./` even when search root was absolute → wrong format.
- Stripping `./` when `--strip-cwd-prefix` not given.

### 7.2 — Size filter traps

- `+1k` interpreted as `>1k` instead of `>=1k` (boundary not included) → loses ~15 size tests.
- `1k` (no sign) treated as exact match instead of typo → check spec.
- `1ki` confused with `1k` (binary vs SI).
- Multiple `-S` not AND'd correctly.

### 7.3 — Exec placeholder traps

- `{.}` stripping multiple extensions instead of last only (`file.tar.gz` → `file` not `file.tar`).
- `{//}` returning empty string for cwd-root files instead of `.`.
- Implicit `{}` not appended when no placeholder in ARGS.
- `\;` terminator not recognized for `-x`.

### 7.4 — Smart-case traps

- Case-detection not Unicode-aware → `Köln` treated as lowercase.
- `-i` overridden by smart-case detection instead of overriding it.

### 7.5 — Gitignore traps

- Not reading parent-dir `.gitignore`.
- `!important.txt` re-include rule not honored.
- `.fdignore` not read.
- Hidden-file rule applied AFTER gitignore instead of independently.

### 7.6 — Hidden-file traps

- `-H` not including dotfiles.
- `-H` re-enabling files that are also gitignored (should still respect gitignore unless `-I` too).

### 7.7 — Empty / no-match traps

- Returning 0 instead of 1 on no match.
- Crashing on empty cwd.
- Outputting empty line when no match.

### 7.8 — Color traps

- `--color auto` emitting codes when stdout is piped.
- `--color always` not emitting codes.
- Wrong color-class assignment (dirs not blue, etc.).

### 7.9 — Help/version traps

- Help to stderr instead of stdout.
- Version missing the version number.
- Format not starting with `Usage:`.

---

## Section 8 — Recommended implementation order

### Phase A — Walker + basic pattern (target: 30-45%)

1. clap argv parser: pattern positional, paths positional, `-h`/`-V`/`-i`/`-s`.
2. Walker over cwd (or given paths) using stdlib `os.walk` or `ignore::WalkBuilder`.
3. Default gitignore + hidden-file exclusion.
4. Regex pattern match against basename.
5. Output paths with `./` prefix, one per line.
6. Smart-case rule.
7. Exit 0 on match, 1 on no-match, 2 on parse error.

### Phase B — Filters (target: 60-72%)

8. `-t` type filter with multi-OR and compound `-tf` form.
9. `-e` extension filter, multi-OR, case-insensitive.
10. `-H` hidden, `-I` no-ignore, `--no-ignore-vcs`, `-u`/`-uu`/`-uuu`.
11. `--max-depth`, `--min-depth`, `--exact-depth`.
12. `-S` size filter with all multipliers (b/k/ki/m/mi/g/gi/t/ti) and +/-/= prefixes.
13. `--changed-within` / `--changed-before` mtime filters.

### Phase C — Pattern modes (target: 75-85%)

14. `-F` literal substring.
15. `-g` glob mode (use globset crate or fnmatch).
16. `-p` full-path matching.
17. `-E` exclude patterns.

### Phase D — Output formatting (target: 85-92%)

18. `-0` / `--print0` NUL separator.
19. `-l` long format (ls-like).
20. `--color auto|always|never` with TTY detection.
21. Color scheme (dirs blue, symlinks cyan, exec green).
22. `--strip-cwd-prefix`.
23. `--format` custom format string.

### Phase E — Exec (target: 92-97%)

24. `-x` per-result exec with `\;` terminator.
25. Implicit `{}` insertion when no placeholder.
26. `{}`, `{/}`, `{//}`, `{.}`, `{/.}` placeholder substitution.
27. `-X` batch mode.
28. Multiple `-x` chains.

### Phase F — Polish (target: 97-100%)

29. `--hyperlink` OSC-8.
30. `--owner` Unix-only filter.
31. Validation errors (clap-shaped).
32. Edge cases for symlink loops with `-L`.

---

## Section 9 — Failure-category triage

```
test_patterns_*       → §4.2 / Phase A or C
test_type_*           → §4.4 / Phase B
test_size_*           → §4.4 / Phase B
test_exec_*           → §4.5 / Phase E
test_output_*         → §4.6 / Phase D
test_path_display_*   → §4.3 / Phase A
test_hidden_*  / test_ignored_* / test_traversal_*  → §4.10 / Phase B
test_filtering_*      → §4.4 / Phase B
test_hyperlinks_*     → §4.12 / Phase F
test_format_*         → §4.6 / Phase D
test_edge_cases_*     → multiple categories — read each individually
```

---

## Section 10 — Reference behaviors (worked examples)

```bash
# Basic search
mkdir -p /tmp/t && cd /tmp/t
touch a.txt b.txt
mkdir -p sub && touch sub/c.txt
fd txt
# ./a.txt
# ./b.txt
# ./sub/c.txt

# Smart-case
fd Foo               # case-sensitive — query has uppercase
fd foo               # case-insensitive — query is lowercase

# Type
fd -t f                    # files only
fd -t d                    # dirs only
fd -t f -t d               # files OR dirs

# Extension
fd -e txt                  # *.txt
fd -e txt -e log           # *.txt OR *.log

# Size
fd -S +1k                  # files >= 1000 bytes
fd -S -1k                  # files <= 1000 bytes
fd -S +1ki                 # files >= 1024 bytes (binary)
fd -S +1k -S -2k           # 1k-2k

# Depth
fd -d 1                    # only direct children

# Hidden + ignore
fd -H                      # include dotfiles
fd -I                      # ignore .gitignore
fd -uu                     # both above

# Exec
fd txt -x echo             # echo each match (implicit {})
fd txt -x echo {/}         # basename only
fd txt -x echo {.}         # extension stripped
fd txt -X wc -l            # batch: one wc, all files

# Output
fd -0                      # NUL-separated
fd -l                      # long format
fd --color always          # ANSI codes always
```

---

## Section 11 — Golden file conventions

177 golden files exist across the 10 branches. Live under `eval/test_resources/<test_module>/`.

- `*.golden` — expected stdout (string-comparison after `text=True` decoding)
- File creation done dynamically per test via `create_test_files(structure)` — NOT pre-staged input files.

The golden contains ALL expected output lines including `./` prefix and trailing newline. Tests assert `result.stdout == golden_text` (exact string equality).

When walk order matters, tests sort first: `sorted(result.stdout.strip().split('\n'))`. But many goldens preserve fd's natural walk order — be careful.

---

## Section 12 — How this document was built

1. Pulled 10 test branches via `huggingface_hub.snapshot_download`.
2. Extracted via `tar --force-local -xzf`.
3. Scanned 79 test files: 1,365 functions, 519 CATCHES, 177 goldens.
4. Read conftest + `test_patterns.py`, `test_exec.py`, `test_type_filtering.py`, `test_output.py`.
5. Aggregated flag inventory (`--format`, `--type`, `--and`, `--exec` dominate), exit codes (0, 1, 2), validation patterns.

---

## Section 13 — Use this spec

1. Pilot dir: `T:/determinex-programbench/<run>/sharkdp__fd.40d8eb3/source/`.
2. Inject this document into the builder prompt.
3. Implement Phases A→F from §8.
4. Embed the §6 smoke tests in `compile.sh`.
5. Triage by §9 after first eval.

---

*Determinex · Lunarian Data Systems · 2026-05-09*
