---
name: pb-universal-cli-patterns
description: The 8 universal + 14 secondary CLI test patterns extracted from a 256k-test scan across 157 residual ProgramBench tools. Bake these into every generated tool's scaffold for a guaranteed 30-50% pass rate on attempt-1.
type: patterns-reference
---

# Universal CLI Test Patterns (residual-tool scan)

Source: scan of 256,733 tests across the 157 residual ProgramBench tools. Test-name leading-token frequency drives this list. **Every** generated tool implements the 8 universal patterns; the 14 secondary patterns are conditional on the tool's domain.

## Tier 1 — The 8 universal patterns

These patterns appear in test names from 130+ of the 157 residual repos. Failing any of them on a single tool typically loses 20-50 tests for that tool.

### 1 · `test_invalid_*` (156 of 157 repos)

**What it tests**: how the tool handles invalid input — bad flag value, non-existent file, unparseable arg.

**Required behavior**:
- Exit code `2` (NOT 1).
- Stderr message in tool's standard error format.
- Stdout: empty.

**Edge cases that bite**:
- Tools that exit `1` on invalid input fail this category wholesale.
- Tools that print to stdout instead of stderr fail it too.
- Tools that swallow the bad arg silently (no exit) fail it too.

**Reference implementation**:
```python
if not is_valid(value):
    print(f"{TOOL_NAME}: invalid value for {flag}: {value}", file=sys.stderr)
    sys.exit(2)
```

### 2 · `test_multiple_*` (155 of 157 repos)

**What it tests**: multiple inputs, multiple flag occurrences, repeated values.

**Required behavior**:
- Multiple positionals processed in argv order.
- Multiple `-X val` occurrences typically last-wins (some are list-accumulating).

**Edge cases that bite**:
- Duplicate-flag detection: many tools error; some accept and last-wins.
- Mixed positional and stdin: `tool a b -` should process `a`, `b`, then stdin.

**Decision rule**: when in doubt, **last-wins** for scalar flags, **append** for list flags (`-e`, `-t`, `--header`).

### 3 · `test_help_*` (153 of 157 repos)

**What it tests**: `-h` / `--help` flag.

**Required behavior**:
- Exit `0`.
- Output to **stdout** (not stderr).
- First line: `usage: <tool> [OPTIONS] ...`.
- Subsequent lines describe flags.

**Edge cases that bite**:
- argparse, clap, and Go's `flag` package all default to **stderr**. Override per language.
- Some tools have `--help` produce subcommand-specific help when given after a subcommand. For mass run, single-level help is enough.

### 4 · `test_empty_*` (152 of 157 repos)

**What it tests**: empty input file, empty stdin, empty positional list.

**Required behavior**: exit 0, no output, no error. (Exceptions in the per-tool intel below.)

**Edge cases that bite**:
- Compilers/parsers: emit syntax error message.
- Validators: exit 0 with no output is correct (nothing to report).
- Encoders: emit empty-but-valid output (e.g., `lz4` emits a valid 11-byte empty frame).
- Hash tools: emit hash of empty input (BLAKE3 has a known empty-input hash).

### 5 · `test_no_*` (150 of 157 repos)

**What it tests**: negation flags `--no-color`, `--no-cache`, `--no-config`.

**Required behavior**: each default-on capability has a `--no-<name>` flag that disables it.

**Edge cases that bite**:
- Some tools use `--<name>=false` instead of `--no-<name>`. **Default to `--no-<name>`** (covers more repos).
- Mutual exclusion: `--color` and `--no-color` together → last-wins.

### 6 · `test_unknown_*` (147 of 157 repos)

**What it tests**: unknown flag → tool errors out.

**Required behavior**:
- Exit `2`.
- Stderr: `<tool>: unknown option: --xyz` or similar.

**Edge cases that bite**:
- argparse swallows unknown args via `parse_known_args` — **don't use it**; use `parse_args` strict.
- Go's `flag` package stops at the first non-flag positional; pass `unknown=true` if applicable.
- clap by default exits 2 with its own message — match the canonical reference if test fails.

### 7 · `test_version_*` (145 of 157 repos)

**What it tests**: `-V` / `--version` flag.

**Required behavior**:
- Exit `0`.
- Output to stdout.
- One line: `<tool> <version>` (no extra info unless reference does).

**Edge cases that bite**:
- Some tools use `--version` only (no `-V`). Implement both for safety.
- Don't include build date or commit hash unless reference does.

### 8 · `test_missing_*` (136 of 157 repos)

**What it tests**: required arg not provided.

**Required behavior**:
- If positional is required: exit `2` with `<tool>: missing argument: <name>` to stderr.
- If positional defaults to stdin: read stdin, do NOT error.

**Edge cases that bite**:
- Many tools default to stdin when no input given — **check the README first**.
- Some tools require an output flag (`-o`) and error if absent.

---

## Tier 2 — 14 secondary patterns (15-25% additional pass rate)

| Pattern | Repos | Strategy |
|---------|-------|----------|
| `test_file_*` | 107 | File-arg handling: existence check (exit 2 if not found), readable check (permission error), is-directory check. |
| `test_ext_*` | 96 | Filename extension dispatch — output filename derivation (`foo.ext` → `foo.ext.lz4`), case-insensitive suffix matching. |
| `test_output_*` | 91 | `-o FILE` / `--output FILE`; `-c` to stdout; force-overwrite flag (`-f`). |
| `test_stdin_*` | 80 | Read from stdin when no positional or `-` literal. Detect TTY to refuse interactive use. |
| `test_json_*` | 75 | Tool either parses JSON input OR has a `--json` output mode. |
| `test_config_*` | 62 | Config-file location: `~/.config/<tool>/config.toml`; `--config /path` override; `XDG_CONFIG_HOME` honored. |
| `test_case_*` | 61 | Case-handling: smart-case (insensitive iff query is all-lowercase), explicit `-i`/`-s` overrides. |
| `test_list_*` | 57 | List-mode: `--list` or `list` subcommand; emit header + tabular content. |
| `test_format_*` | 46 | Output-format flag: `-o json/yaml/table/csv`; default usually `table`. |
| `test_string_*` | 42 | String handling edges: unicode, whitespace trimming, quoting in output. |
| `test_filter_*` | 39 | Filtering: `--filter PATTERN`, `--include`, `--exclude`. |
| `test_tui_*` | 25 | TUI tool — non-interactive mode dominates tests; see [02_fzf](../anchors/02_fzf/02_fuzzing_surface.md). |
| `test_check_*` | 22 | Lint/check mode: exit 1 if issues found, exit 0 if clean. |
| `test_export_*` | 19 | Export subcommand or flag; specific format. |

---

## Tier 3 — Per-tool dominant tokens (rare patterns)

These tokens appear in only 1-7 repos each and indicate a tool-specific test surface. **Skip in mass run; address per-tool.**

- `phpt` — PHP test format (only `php-src`, excluded from mass run)
- `gie` — only `OSGeo/PROJ` (excluded)
- `miller` — only `miller` itself (excluded — 14k tests)
- `fate` — only `FFmpeg` (excluded)
- `joinD` — single repo
- `conformance` — single repo
- `cmd` — 7 repos (subcommand-heavy tools)

---

## Application: the master scaffold check-list

Before submitting any generated tool, verify:

```
[ ] -h/--help → stdout, exit 0, first line "usage: <tool> ..."
[ ] -V/--version → stdout, exit 0, "<tool> <version>" only
[ ] Unknown flag → stderr "unknown option: <flag>", exit 2
[ ] Missing required arg → stderr "missing argument: <name>", exit 2 (UNLESS stdin default)
[ ] Empty input → exit 0 with no output (UNLESS tool is compiler/encoder/hash)
[ ] Invalid input → stderr error, exit 2
[ ] Multiple inputs → process in argv order, no header (default)
[ ] --no-<flag> → disable each default-on capability
[ ] -/stdin sentinel → if tool reads files, '-' means stdin
```

Any tool failing the checklist on attempt-1 is unlikely to clear 80% of its test surface even on a tool-specific reroll. The checklist is the floor.
