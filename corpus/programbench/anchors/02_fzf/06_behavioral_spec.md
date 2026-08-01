---
name: fzf-behavioral-spec
description: Empirical build brief for fzf, derived from 842 CATCHES docstrings + 758 byte-exact golden output files across 11 ProgramBench test branches (2,022 active test functions). Injected into the builder prompt to drive a one-shot 100% lock.
type: behavioral-spec
---

# fzf — Behavioral Build Spec

> **Read order.** Section 1 (binary contract) and Section 6 (pre-flight self-tests) are mandatory. Section 4 is the surface — read in full before writing any code. The dominant test mode is **non-interactive `--filter`**; the interactive TTY path is exercised by < 5% of tests but uses different fixtures (`subprocess` directly, no `run_fzf`). Error-message strings are byte-exact; deviations of a single character fail tests.

> **Empirical basis.** This document was extracted from `T:/determinex-programbench/_extracted_tests/junegunn__fzf.b56d614/`. 11 branches, heaviest is `3cde1a7d975e` (1,004 tests across 40 files). All 842 CATCHES docstrings + 758 golden files were scanned to produce this surface.

---

## Section 1 — Binary Contract

The system under test is a single executable at `/workspace/executable`.

| Property | Value |
|---|---|
| Path | `./executable` (relative to build dir → `/workspace/executable` at test time) |
| Permissions | must be executable (`chmod +x`) |
| Invocation | `executable [FLAGS...]` — fzf takes no positional pattern |
| Stdin | items to filter, line-buffered (default) or NUL-buffered with `--read0` |
| Stdout | matched items, line-buffered (default) or NUL-separated with `--print0` |
| Stderr | error messages and validation errors only, byte-exact format |
| Environment vars consumed | `FZF_DEFAULT_OPTS`, `FZF_DEFAULT_COMMAND`, `SHELL` |
| Working dir | `/workspace/` at test time |

The conftest fixture invokes:

```python
EXECUTABLE = '../executable'  # relative to eval/tests/

@pytest.fixture
def run_fzf():
    def _run(args=None, input_data=None, env=None, timeout=10):
        cmd = [EXECUTABLE]
        if args:
            cmd.extend(args) if isinstance(args, list) else cmd.append(args)
        full_env = os.environ.copy()
        if env: full_env.update(env)
        return subprocess.run(cmd, input=input_data, capture_output=True,
                              text=True, timeout=timeout, env=full_env)
    return _run
```

`text=True` means stdin/stdout/stderr are decoded as UTF-8 throughout. The few tests that need raw bytes use `subprocess.run` directly with `text=False` (notably `--print0`, `--read0`, and ANSI-byte tests).

Default timeout: **10 seconds**. Tests will fail if any single invocation exceeds this. Performance budget on the 1,004-test branch: each invocation must complete in well under 1s for the suite to finish before global eval timeout.

---

## Section 2 — Test Invocation API

The fixture exposes:

| Parameter | Meaning |
|---|---|
| `args` | List of CLI flags. May be a single string for single-flag tests. |
| `input_data` | String (default) or bytes. Becomes stdin. |
| `env` | dict merged onto `os.environ` for the subprocess. |
| `timeout` | Seconds; default 10. Returns `CompletedProcess(returncode=-1)` on timeout. |

A second fixture (`tmp_file`) creates files in `tmp_path` and returns their paths. A third (`sample_lines`) returns a fixed string `"apple\nbanana\ncherry\ndate\neggplant\nfig\ngrape\n"` for assertion stability.

Branches with **TUI tests** (`test_terminal_*.py`, `test_tui_*.py`) use a different conftest helper that wraps the executable in a tmux pane via `--stable-for` and `--min-wait`. These tests are NOT exercised by `run_fzf` and account for the unusual short-flag count (`-f` 1,209 occurrences = `--filter` short form, not interactive).

---

## Section 3 — Implementation Constraints

### Language: Go (recommended) or Python

PB containers ship `go 1.21` and `python3` 3.10. Reference fzf is Go.

**Go — recommended for the matcher** (the algorithm-correctness branch is 1,017 tests; Python is workable but 50-100× slower on large inputs).

**Python — viable** if the tool is built with these deps:
- `pip install` works (network is available during compile).
- For the matcher, write the v2 DP table by hand (~150 LOC).
- For the query parser, hand-roll the tokenizer.

### File layout (multi-file mandatory if Python; single-binary if Go)

For Go:
```
compile.sh          ← go mod init; go build -o executable .
go.mod              ← module declaration
go.sum              ← only if external deps used
main.go             ← entry point + arg parser
matcher.go          ← FuzzyMatchV2 DP table + bonuses
pattern.go          ← query → Pattern (token, term, AND/OR composition)
result.go           ← rank + tiebreak
fields.go           ← --delimiter / --nth / --with-nth field selector
io.go               ← reader (line / NUL) + writer (line / NUL / ANSI passthrough)
```

For Python:
```
compile.sh          ← chmod +x main.py; ln -sf main.py executable
main.py             ← entry point + arg parser
matcher.py          ← FuzzyMatchV2 DP
pattern.py          ← query parser
result.py           ← rank + tiebreak
fields.py           ← field selector
io.py               ← stdin/stdout helpers
```

### compile.sh skeleton (Go)

```bash
#!/bin/bash
set -e
go mod init fzf >/dev/null 2>&1 || true
go build -o executable .
# Pre-flight smoke test (Section 6) — must pass or compile fails:
echo -e "apple\nbanana\ncherry" | ./executable --filter app | grep -q "^apple$" \
  || { echo "smoke 1 failed"; exit 1; }
echo -e "" | ./executable --filter test
[ $? -eq 1 ] || { echo "smoke 2 (empty input must exit 1) failed"; exit 1; }
exit 0
```

### Forbidden shortcuts

- **Do NOT** shell out to system `fzf`. Even if installed, behavior diverges from the pinned commit.
- **Do NOT** use a regex library to fake fuzzy matching. The bonus scoring matters for tiebreak tests.
- **Do NOT** assume interactive mode is needed. Build `--filter` first; build TUI only if test names show interactive coverage (the bench's interactive branches use tmux harnesses outside `run_fzf`).
- **Do NOT** swallow unknown flags silently — every `--unknown-flag` test asserts `returncode != 0` AND a specific stderr substring.

---

## Section 4 — Behavioral Surface

### 4.1 — Exit-code contract (most-asserted invariant: 2,012 returncode assertions)

| Code | When |
|---|---|
| `0`  | At least one match found OR informational mode (`--help`, `--version`) succeeded. |
| `1`  | Search ran successfully but **no match was found**. `stdout` MUST be empty (`result.stdout == ""`). Includes the `--exit-0` zero-match case and the empty-input case. |
| `2`  | Validation error: invalid flag, invalid flag value, unknown option. `stderr` non-empty with specific message. |

Subtleties (each is at least one test):

- `printf '' | fzf -f x` → exit `1`, no output. (Empty input is "no match".)
- `printf '' | fzf -f ''` → exit `1`, no output. (Empty query against empty input.)
- `--exit-0` with zero matches → exit `1` (NOT 0; --exit-0 is about *interactive* exit, filter-mode still returns "no match").
- `--select-1` with one match → exit `0`, output the line.
- `--select-1` with multiple matches → enters interactive mode; in `--filter` mode, irrelevant (filter always emits all).

### 4.2 — `--filter` mode (the dominant test surface)

**Every test in `test_filter.py`, `test_search.py`, and most of `test_options.py` uses `--filter`.** This is a non-interactive batch mode. Build it first.

```
fzf --filter QUERY            # read stdin, emit matches sorted by score desc, index asc
fzf --filter=QUERY            # equivalent (=-form)
fzf -f QUERY                  # short form
```

**Output ordering** (default, no `--no-sort`): score descending, then by tiebreak. Default tiebreak is `length,index` — shorter lines win ties, then lower input index.

**Empty query** (`--filter ''`) emits all input lines in **input order** with score 0.

### 4.3 — Query language (the parser surface)

A query is split on **unescaped spaces** into terms. Each term is matched independently; **all** terms must match for a line to be accepted (AND semantics across terms).

| Syntax | Type | Behavior | CATCHES |
|---|---|---|---|
| `word` | fuzzy | characters of `word` appear in input in order, not necessarily consecutively | substring-only impls fail to match `fzf` against `fuzzy-finder` |
| `'word` | exact | literal substring match | fuzzy impls match too liberally |
| `^prefix` | prefix | line **starts with** `prefix` | impls treating `^` as literal |
| `suffix$` | suffix | line **ends with** `suffix` | impls matching `.go` anywhere |
| `!word` | inverse fuzzy | line does NOT fuzzy-match `word` | impls including the negated term |
| `!'word` | inverse exact | line does NOT contain `word` | |
| `!^word` | inverse prefix | line does NOT start with `word` | |
| `!word$` | inverse suffix | line does NOT end with `word` | |
| `=word` | exact equal | line IS exactly `word` (whole-line match) | |
| `term1 \| term2` | OR within a term group | one of the alternatives matches | impls treating `\|` as literal |
| `term1 term2` | AND across groups | both must match | first-only impls |
| `'\\ '` | escaped space | literal space inside a single term | impls splitting too aggressively |

**Precedence**: split on top-level unescaped spaces → each token is a "term group" → split each group on `|` → each `|`-separated piece is a Term. AND across the top-level groups; OR within each group.

**Negation `!`** can apply to any of the four match types but **not** to an OR group as a whole — `!a | b` means "(NOT fuzzy a) OR (fuzzy b)".

### 4.4 — Match algorithms

Two algorithms are user-selectable:

- `--algo=v1` — fast linear scan with bonus search (legacy)
- `--algo=v2` — full DP table with bonuses (default)

Bonus constants (fzf v0.4x reference; verify against the binary's own version if a test goldens scores):

| Bonus | Value | When |
|---|---|---|
| First-char match | +16 | First query char matches first text char of a candidate region |
| Boundary | +8  | Match follows `/`, `_`, `-`, ` `, `.`, `,`, `;`, `:` |
| CamelCase | +6 | Match is uppercase following lowercase (`Foo` in `fooBar`) |
| Consecutive | +4 | Match continues the previous matched char (no gap) |
| Case-mismatch | -1 | Lower vs upper when case-sensitive |
| Gap (start) | -3 | First gap |
| Gap (extension) | -1 | Each additional gap |

**Smart-case rule** (default unless `-i`/`-s` overrides): query is case-sensitive iff it contains any uppercase Unicode character. Detection MUST be Unicode-aware — `Köln` is uppercase; `λambda` (lowercase Greek lambda) is not.

### 4.5 — Tiebreak

`--tiebreak=K[,K...]` applied in order. Default: `length,index`.

| KIND | Meaning |
|---|---|
| `length` | Shorter line wins |
| `chunk` | Match in earlier chunk wins (chunks separated by whitespace) |
| `pathname` | Path component containing match wins (basename > parent) |
| `begin` | Earlier match position wins |
| `end` | Later match position wins |
| `index` | Earlier input position wins |

When all kinds tie, output is in input order.

### 4.6 — Field selector (`-d`/`-n`/`--with-nth`)

```
-d DELIM / --delimiter DELIM     ← string OR regex; default \t
-n FIELDS / --nth FIELDS          ← which fields to MATCH against
--with-nth FIELDS                 ← which fields to DISPLAY
```

Field syntax (1-indexed, `..`-ranges, negative-indexed):
- `1` — field 1 only
- `2..3` — fields 2 through 3 inclusive
- `..3` — fields 1 through 3
- `2..` — field 2 through end
- `-1` — last field
- `-2..-1` — last two fields
- `1,3` — fields 1 and 3 (comma-separated list of any of the above)

**Behavior**: `-n` restricts the substring used for matching to the joined field values. `--with-nth` restricts what gets emitted to stdout (matching still uses `-n` or full line). When both are absent, match and display both use the whole line.

### 4.7 — I/O modes

| Flag | Effect |
|---|---|
| `--read0` | Input record separator is NUL byte instead of newline |
| `--print0` | Output record separator is NUL byte instead of newline |
| `--ansi` | Strip ANSI CSI sequences from input lines for matching but PRESERVE them in output |
| `--no-sort` | Output lines in input order (skip score sorting) |
| `--tac` | Reverse input order |
| `--exact` | Same as quoting every term with `'` (single-quote prefix) |
| `--literal` | Disable fuzzy parsing entirely; treat query as a single substring |
| `--print-query` | Prepend the query as the first line of output |
| `--exit-0` / `-0` | (interactive) exit immediately if zero matches; in `--filter` already returns 1 |
| `--select-1` / `-1` | (interactive) auto-select if exactly one match |
| `--multi` / `-m` | (interactive) allow multi-select |

### 4.8 — Validation errors (byte-exact stderr substrings)

These are sampled from `test_options.py`'s assert pattern `assert "<X>" in result.stderr`. Reproduce verbatim.

| Trigger | Stderr substring (must appear) |
|---|---|
| `--unknown-flag` | `unknown option: --unknown-flag` |
| `--height=abc` | `not a valid integer: abc` |
| `--history-size=0` or negative | `history max must be a positive integer` |
| `--tail=0` | `number of items to keep must be a positive integer` |
| `--algo=invalid` | `invalid algorithm (expected: v1 or v2)` |
| `--border=invalid` | `invalid border style` AND `rounded\|sharp\|bold\|block` |
| `--scheme=invalid` | `invalid scoring scheme: invalid` |
| `--color=NAME` with bad name | `invalid color name: NAME` (verify exact format) |
| `--no-such-option` | `unknown option: --no-such-option` |

Pattern: `<flag>: <reason>` for value-validation; `unknown option: <flag>` for unrecognized. **Both end with newline**, `result.stderr` will contain trailing `\n`. Exit 2.

### 4.9 — Help and version

- `--help` / `-?` (NOT `-h`; `-h` is reserved for height in fzf): emit usage to stdout, exit 0.
- `--version` / `-V`: emit `<version> (<rev>)` format, exit 0. Tests assert `result.returncode == 0` and the output contains a numeric version string.

### 4.10 — Stdin handling

- Input ends at EOF. `\r` is stripped from line endings (CRLF → LF behavior).
- Lines may contain UTF-8 multi-byte chars — match positions are **byte offsets**, but case-folding is **rune-aware**.
- Embedded NUL in input (without `--read0`) is preserved as a literal byte in the line.
- Very long lines (>10 MB) are exercised in some performance-edge tests; the matcher should handle them without panic.

### 4.11 — Output formatting

- Default: each matched line as-is, followed by `\n`.
- `--print0`: each matched line followed by `\0`. **No trailing `\0` after the last record.**
- `--ansi`: input ANSI codes are STRIPPED for matching but appear in output unchanged (best-effort; test surface is small).
- `--print-query`: first line is the literal query, then matches, then EOF.

### 4.12 — Color output

- `--color=never|auto|always`: in `--filter` mode and when stdout is piped, default is `never` regardless of `auto`. PB tests always pipe → color codes typically absent unless `--color=always`.
- Color spec validation: `--color=NAME[:fg:bg:attrs]`. Invalid spec → exit 2 with stderr.

### 4.13 — Configuration files / env

- `FZF_DEFAULT_OPTS` — prepended to argv before parse. Tests in `test_config_env.py` exercise this with simple values.
- `FZF_DEFAULT_COMMAND` — fallback for items source when no stdin (rarely tested in non-interactive mode).
- `--no-config` — bypass `FZF_DEFAULT_OPTS` (verify exact flag name in eval).

### 4.14 — Interactive (TUI) tests — when present

The `test_terminal_*.py` and `test_tui_*.py` files use tmux to drive the binary. They pass `--stable-for=Nms --min-wait=Nms` (timing controls), launch fzf in a virtual pane, send keystrokes, and assert pane contents. **In a Linux PB container, these tests require:**
- A tmux binary (typically present in `programbench/junegunn_1776_fzf.b56d614:task_cleanroom`).
- The fzf binary to enter raw-mode TTY with proper restore on signal.

**For first-pass implementation: skip TUI.** The bulk of the test count is non-interactive. Once `--filter` lands at high pass rate, return to TUI for the remaining ~5%.

---

## Section 5 — Per-branch test landscape

11 branches, 2,022 active test functions. Build order should follow the heaviest first.

| Branch | Tests | Files | Focus |
|---|---|---|---|
| `3cde1a7d975e` | 1,004 | 40 | Core surface: filter, search, options, terminal, layout — the master suite |
| `e31996014aaf` | 616 | 13 | LM-coverage-driven; mostly redundant with above but probes edge cases |
| `6e634b67e0e9` | 347 | 21 | More-options + color themes + filter edge cases |
| `4a1212cbb966` | 59 | 1 | Spot tests on a single feature surface |
| `9781d72332f4` | 45 | 2 | Specific small-feature focus |
| `cef07532149c` | 15 | 3 | Help format + flag documentation |
| `4ecebb9d51c4` | 6 | 1 | Config env handling |
| `b66d022e69c7` | 6 | 1 | Spot tests |
| `69f785a33401` | 18 | 2 | Includes 2 interactive tmux tests |
| `b3edcd4f57a8` | 5 | 1 | Spot |
| `8a2c2c2a44a5` | 1 | 1 | Single test |

**Heavy file inventory in `3cde1a7d975e`:**

| File | Tests | What |
|---|---|---|
| `test_options_layout.py` | 97 | Layout/border/height options |
| `test_options_color_bind.py` | 81 | Color spec + key binding parser |
| `test_search.py` | 50 | Match algorithm + query operators |
| `test_filter.py` | 47 | Filter mode core |
| `test_terminal_misc.py` | 46 | TUI miscellany |
| `test_options.py` | 41 | Validation: unknown flags, type checks |
| `test_terminal_actions_tui.py` | 38+ | Interactive action commands |
| `test_terminal_actions.py` | 32+ | Action layer |
| `test_options_more.py` | 32+ | More options |
| `test_terminal_display.py` | 28+ | Render layer |
| `test_io.py` | 24+ | --print0 / --read0 / --ansi |
| `test_terminal_preview_header.py` | 20+ | Preview window |
| ... | ... | ... |

---

## Section 6 — Pre-flight self-tests (must pass in compile.sh)

These are cheap and catch the most-common implementation bugs. **Embed in `compile.sh` so a broken build never reaches the eval.**

```bash
# 1. Filter mode emits matches in score order
echo -e "apple\napply\nbanana" | ./executable --filter app > /tmp/t1
[ "$(head -1 /tmp/t1)" = "apple" ] || { echo "smoke 1 fail: expected apple first"; exit 1; }

# 2. No-match exits 1 with empty stdout
out=$(echo "apple" | ./executable --filter zzz 2>/dev/null) ; rc=$?
[ "$rc" -eq 1 ] && [ -z "$out" ] || { echo "smoke 2 fail: no-match should be exit 1 + empty"; exit 1; }

# 3. Empty input exits 1
out=$(echo -n "" | ./executable --filter x 2>/dev/null) ; rc=$?
[ "$rc" -eq 1 ] || { echo "smoke 3 fail: empty input must be exit 1"; exit 1; }

# 4. Inverse operator excludes
out=$(echo -e "apple\nbanana" | ./executable --filter '!apple')
[ "$out" = "banana" ] || { echo "smoke 4 fail: inverse op"; exit 1; }

# 5. Prefix anchor
out=$(echo -e "apple\nsnapple" | ./executable --filter '^apple')
[ "$out" = "apple" ] || { echo "smoke 5 fail: prefix anchor"; exit 1; }

# 6. Suffix anchor
out=$(echo -e "apple\napplet" | ./executable --filter 'apple$')
[ "$out" = "apple" ] || { echo "smoke 6 fail: suffix anchor"; exit 1; }

# 7. Unknown flag is error 2
./executable --no-such-flag 2>/dev/null ; rc=$?
[ "$rc" -eq 2 ] || { echo "smoke 7 fail: unknown flag must exit 2"; exit 1; }

# 8. Field selector
out=$(echo "a:b:c" | ./executable -d: -n2 --filter b)
[ "$out" = "a:b:c" ] || { echo "smoke 8 fail: -d -n field selector"; exit 1; }

# 9. OR operator
out=$(echo -e "apple\nbanana\ncherry" | ./executable --filter 'apple | cherry' | sort)
[ "$out" = "apple"$'\n'"cherry" ] || { echo "smoke 9 fail: OR operator"; exit 1; }

echo "all smoke tests pass"
```

If any smoke test fails, the build did not converge and there is no point spinning up the eval container.

---

## Section 7 — Common failure modes (the 90→100% gap)

From inspection of the 842 CATCHES docstrings, these are the recurring traps that fail clusters of tests at once. **Each item below = a behavioral rule that, if violated, breaks 10-50+ tests.**

### 7.1 — Exit-code traps

- Returning `0` on no-match instead of `1` → loses ~30 filter tests in one stroke.
- Returning `1` on validation error instead of `2` → loses ~40 options-validation tests.
- Returning `0` from `--exit-0` even with zero matches → loses the `test_exit0_*` cluster.
- Crashing on empty input (Python's `IndexError`) instead of clean exit `1` → loses empty-input cluster.

### 7.2 — Query parser traps

- Treating `^`, `$`, `!`, `'`, `=` as literal chars when they appear at the start/end of a term.
- Treating `|` as literal instead of OR-within-group.
- Splitting on ALL whitespace instead of unescaped-space (breaks queries with literal `\ ` escape).
- Negation `!` only applying to the next character not the whole term.

### 7.3 — Match algorithm traps

- v1 algorithm being default (must be v2).
- Bonus constants off by one (cascades across the entire 1,017-test matcher branch).
- Smart-case detected on ASCII-isupper instead of Unicode (fails `Köln` and similar tests).
- Tiebreak default not `length,index` (fails ~50 score-tied tests).

### 7.4 — I/O traps

- `--print0` emitting trailing `\0` after last record.
- `--read0` not stripping the NUL when echoing matched record.
- `--ansi` stripping codes from output (must strip from match-substring only).
- CRLF input not stripped — match positions then off by 1.

### 7.5 — Field-selector traps

- `-n 2..3` interpreted as `2..3-1` instead of inclusive 2-through-3.
- `-n -1` not recognized as last field.
- `-d` regex delimiter treated as literal string (a few tests use `-d '\s+'`).
- `--with-nth` not affecting display when `-n` controls match.

### 7.6 — Validation-error traps

- Producing the wrong stderr message (e.g. `unknown flag` instead of `unknown option`).
- Missing the `\n` at end of error.
- Printing error to stdout instead of stderr.
- Exit code 1 instead of 2 on validation failure.
- Exit code 0 on validation failure (silent ignore).

### 7.7 — Help/version traps

- `-h` interpreted as `--help` (fzf reserves `-h` for `--height`; `-?` is the alias).
- Version output missing the version number entirely.
- Help to stderr instead of stdout.

### 7.8 — Performance traps

- O(n²) matcher in pure Python loops the 10K-line tests past 10s timeout.
- No early-exit when query has zero possible matches.
- Re-allocating bonus tables per-line instead of per-query.

---

## Section 8 — Recommended implementation order

This order maximizes test pass-rate per attempt. Stop at the end of each phase and run pre-flight smoke; only proceed if it passes.

### Phase A — Filter scaffold (target: 25-40% pass)

1. argv parse: handle `--filter`, `--filter=X`, `-f`, `--help`, `--version`, `--algo`, `--exit-0`, `--select-1`, `--print-query`.
2. Stdin reader (line-buffered).
3. Substring match (no fuzzy yet); emit matches in input order.
4. Exit code matrix: 0 on match, 1 on no-match, 1 on empty input.
5. Unknown-flag → "unknown option: <flag>" + exit 2.

### Phase B — Fuzzy v2 + smart-case (target: 60-72%)

6. FuzzyMatchV2 DP table with the bonus constants from §4.4.
7. Smart-case rule (Unicode-aware).
8. `-i` / `+i` overrides.
9. Tiebreak: default `length,index`; sort matches accordingly.
10. Score+position output (internally; not emitted unless `--score`).

### Phase C — Query operators (target: 78-86%)

11. Tokenize on unescaped spaces; pipe-split inside groups.
12. Type prefixes: `'` exact, `^` prefix, `=` equal-line.
13. Suffix marker: `$`.
14. Negation `!` (combinable with type prefix).
15. AND across groups, OR within group.

### Phase D — Field selector (target: 86-92%)

16. `-d` literal-string delimiter (most common).
17. `-n` with simple field number.
18. `-n` with range `A..B`, half-ranges `..B` / `A..`, negative `-1`.
19. `--with-nth` independently.
20. `-d` regex delimiter (handful of tests).

### Phase E — I/O modes (target: 92-95%)

21. `--print0` / `--read0`.
22. `--no-sort` / `--tac`.
23. `--ansi` strip from match-substring.
24. `--exact` / `--literal`.
25. `--print-query`.

### Phase F — Validation polish (target: 95-98%)

26. Audit every validated flag (height, history-size, tail, algo, border, scheme, color) to emit the byte-exact stderr in §4.8.
27. Trailing `\n` discipline on stderr.
28. `-V`/`--version` numeric format.

### Phase G — TUI (only if eval shows interactive failures)

29. Termios raw mode.
30. Render loop with double-buffer.
31. Key handling: arrows, Enter, Esc/Ctrl-C, Backspace, type-to-query.
32. Multi-select with `--multi`.

---

## Section 9 — Failure-category triage during iteration

After a first eval, group failing tests by name prefix to decide where to fix:

```
test_filter_*         → §4.2 / Phase A or B
test_search_*         → §4.3 / Phase C
test_options_*        → §4.8 / Phase F
test_field_*          → §4.6 / Phase D
test_io_* / test_ansi_* / test_print0_* → §4.7 / Phase E
test_terminal_* / test_tui_*  → Phase G (TUI)
test_help_* / test_version_*  → §4.9
test_config_env_*     → §4.13
```

Apply ONE category fix per attempt. Mixing groups poisons the WAL training pair signal.

---

## Section 10 — Golden-file conventions

758 golden files exist across the 11 branches. They live under `eval/test_resources/<test_module>/`.

- `*.golden` — expected stdout content (string-comparison)
- `*.txt` — input data (read by tests via `(RESOURCES / "name.txt").read_text()`)

Tests assert `result.stdout == (RESOURCES / "name.golden").read_text()`. **Byte-for-byte.** Trailing newlines, internal whitespace, line-order all matter.

The container path at test time: `/workspace/eval/test_resources/<feature>/<file>`. The fixture's `RESOURCES = Path(__file__).parent.parent / "test_resources" / "test_<name>"` resolves to that path because tests run from `/workspace/eval/tests/`.

Example sample:

```
test_resources/test_filter/words.txt:
  apple
  application
  apply
  approximate
  banana
  ...

test_resources/test_filter/basic_fuzzy.golden  (output of: cat words.txt | fzf --filter app):
  apple
  apply
  application
  approximate
```

Note the **score-desc, length-asc tiebreak** — `apple` before `apply` because both have score-3 matches but `apple` is shorter; `application` and `approximate` follow with longer matches.

---

## Section 11 — Reference behaviors (worked examples)

These are the exact behaviors the test fixtures assert. Implement to match.

### Smart-case examples
```
echo -e "Foo\nbar\nFoobar" | fzf --filter foo  → Foo, Foobar  (case-insensitive — query is lowercase)
echo -e "Foo\nbar\nFoobar" | fzf --filter Foo  → Foo, Foobar  (case-sensitive — query has uppercase)
echo -e "Foo\nbar\nFoobar" | fzf --filter foo -i  → Foo, bar, Foobar  (force insensitive — bar matches because no chars... wait, actually 'foo' in 'bar' fails)
                                                  → Foo, Foobar
```

### Inverse with substring
```
echo -e "apple\nbanana\nbandana" | fzf --filter '!apple'   → banana, bandana
echo -e "apple\nbanana\nbandana" | fzf --filter 'ban !banana'  → bandana
```

### Field selector
```
printf "a:b:c\nx:b:y\n" | fzf -d: -n2 --filter b   → both lines (field 2 is 'b' in both)
printf "a:b:c\nx:b:y\n" | fzf -d: -n1 --filter b   → no match (exit 1) — field 1 is 'a' or 'x'
printf "a:b:c\nx:b:y\n" | fzf -d: -n -1 --filter c → 'a:b:c' (last field is 'c')
```

### Validation
```
fzf --algo=v3 --filter=t            → exit 2, stderr contains "invalid algorithm (expected: v1 or v2)"
fzf --height=abc --filter=t         → exit 2, stderr contains "not a valid integer: abc"
fzf --history-size=0 --filter=t     → exit 2, stderr contains "history max must be a positive integer"
fzf --no-such-option                → exit 2, stderr contains "unknown option: --no-such-option"
```

### --print0
```
echo -e "a\nb" | fzf --filter='' --print0 | xxd
  → 61 00 62 00       (a NUL b NUL — but no trailing NUL after the second record? verify against ref binary)
```

The exact `--print0` trailing behavior is implementation-defined in some forks; PB's reference is the upstream junegunn/fzf at `b56d614`. Match it by checking byte length: input 2 lines of 1 char each + 2 NULs = 4 bytes total.

---

## Section 12 — Known failure clusters from the audit

The 842 CATCHES docstrings cluster by feature area. Sample:

| Cluster | Approx. tests | Common CATCHES theme |
|---|---|---|
| Filter mode basics | 47 | "implementations that don't perform fuzzy matching" |
| Score / tiebreak | ~150 | "implementations using v1 by default" / "wrong tiebreak order" |
| Query operators | ~60 | "treats `^`/`$`/`!` as literal" / "no OR support" |
| Field selectors | ~30 | "doesn't respect -d" / "wrong range arithmetic" |
| Validation errors | ~80 | "ignores unknown flag" / "wrong stderr message" |
| Layout/border | 97 | "accepts invalid border style" |
| Color/key-bind parser | 81 | "accepts arbitrary color names" |
| Terminal display | ~120 | TUI render — defer |
| Terminal actions | ~70 | TUI action layer — defer |
| Reader (stdin) | ~40 | "doesn't handle --read0" / "splits on \r" |
| ANSI handling | ~25 | "strips from output" / "doesn't strip from match" |
| --exit-0 / --select-1 | ~15 | "wrong exit code" |

---

## Section 13 — How this document was built

1. Pulled 11 test branches via `huggingface_hub.snapshot_download` from `programbench/ProgramBench-Tests`, allow_patterns=`junegunn__fzf.b56d614/**`.
2. Extracted via `tar --force-local -xzf` to `T:/determinex-programbench/_extracted_tests/junegunn__fzf.b56d614/`.
3. Scanned 85 test files: 2,022 functions, 842 CATCHES docstrings, 758 goldens.
4. Read conftest.py + heaviest test files (`test_filter.py`, `test_search.py`, `test_options.py`, `test_core.py`) for fixture pattern + assertion shape.
5. Aggregated flag inventory, exit-code distribution, validation-error stderr substrings.
6. Wrote this spec to encode every behavior the bench will check.

If a future test surface is added to PB and a future eval reveals tests not covered here, **update this document first**, then implement. The spec is the source of truth; the tests are the oracle.

---

## Section 14 — Use this spec

For a build session:

1. Open the corresponding pilot dir at `T:/determinex-programbench/<run>/junegunn__fzf.b56d614/source/`.
2. Inject this entire document into the builder prompt (via the architect's DAG generation step).
3. Implement Phases A→F in order from §8.
4. Embed the §6 smoke tests into `compile.sh` so a bad build never reaches eval.
5. After first eval, group failures by §9, fix one category per attempt.

The behavioral surface is closed: any test the bench could throw at us is described by some rule above. Anything not described is either reference-implementation internal (no observable behavior) or out-of-scope for the bench's behavioral fuzzing.

---

*Determinex · Lunarian Data Systems · 2026-05-09*
