# Family: shell_coreutils

> Re-implementations of POSIX coreutils (`cut`, `tr`, `head`, `tail`, `sort`, `uniq`, etc.). Heavy crossover with `rust_cli`.

## Purpose

Sprint exemplar: `riquito__tuc` — 2.48% → 42.51% (+40.03pp). Cut-alike text-transformation tool.

## Tests-the-family-typically-faces

| Category | Modules | Checks |
|---|---|---|
| Field selection | `test_fields` | `-f 1,3:5,-2` range parsing |
| Char / byte selection | `test_char_byte_line` | `-c`, `-b`, `-l` ranges |
| Delimiter handling | `test_delimiters` | `-d <DELIM>` with `\t` / `\n` escape sequences |
| Output joining | `test_output` | Default joins with delimiter; `--no-join` empty; `-r REPL` custom |
| Stdin / file input | `test_input_advanced` | Positional file path OR stdin; multiple files rejected |
| JSON output | `test_output` | `-j/--json` emits JSON array (flat across input lines) |

## Common flags

| Short | Long | Purpose |
|---|---|---|
| `-d` | `--delimiter <D>` | Field delimiter (default `\t`) |
| `-f` | `--fields <RANGES>` | Field ranges |
| `-c` | `--characters <RANGES>` | Char ranges |
| `-b` | `--bytes <RANGES>` | Byte ranges |
| `-l` | `--lines <RANGES>` | Line ranges |
| `-r` | `--replace <STR>` | Output separator |
| `-s` | `--only-delimited` | Skip lines without delimiter |
| `-m` | `--complement` | Invert selection |
| `-j` | `--json` | JSON output |
| `-z` | `--zero-terminated` | NUL line terminator |
| | `--no-join` | Join with empty string |
| | `--compress-delimiter` | Collapse consecutive delimiters |

## Range syntax

- `N` — single (1-indexed)
- `N-M` or `N:M` — inclusive range
- `-N` — Nth from end (negative)
- Comma-separated combinations
- `:M` — from start to M; `N:` — from N to end

## Error conventions

- **Unknown flag** → rc=2 (CLAP)
- **File not found** → rc=1, `"error: cannot read '<path>': No such file or directory"`
- **Too many files** → rc=1, `"error: too many input files (got N, expected at most 1)"`
- **Invalid int (e.g. `--max-fields=abc`)** → rc=2, `"invalid value 'abc' for '<flag> <NAME>'"`

## Output conventions

- Default join: the delimiter character itself (e.g. `-d -` → join with `-`)
- `--no-join`: empty string
- `-r REPL`: REPL string
- `-j/--json`: flat JSON array across ALL input lines (NOT per-line nested arrays)
- Stdin if no positional file; positional file overrides stdin

## Known traps

1. **Default join MUST be delimiter, not empty**: v1 confused `--no-join` with default → broke 100+ tests.
2. **JSON output is FLAT**: per-line processing returns lists of pieces; main aggregates into ONE flat array. Per-line `json.dumps` then wrap = double-encoded → all tests fail. (tuc v1 → v2 fix)
3. **Positional file argument is REQUIRED to be supported**: even if tool reads stdin, tests pass file paths as positionals and expect the tool to read from them.
4. **Escape sequences in `-d`**: `\\t`, `\\n`, `\\0` strings should be converted to actual `\t`, `\n`, `\x00`. (tuc v2 fix)
5. **Empty input = rc=0**: don't process or error on zero-byte stdin/file.

## Generator pseudocode

```python
def generate(instance_id, probe):
    # 1. _parse_ranges(spec, length) handling N, N-M, N:M, -N, partial
    # 2. _resolve_delim converts \\t → \t etc.
    # 3. _read_input: 0 positional = stdin, 1 = file, 2+ = error
    # 4. _process_line_to_pieces (returns list, not joined string)
    # 5. main aggregates into single JSON array OR joins per line
    # 6. -z/--zero-terminated: split on \x00 instead of \n
```

## Exemplar tool

| Tool | Best | Best dir |
|---|---|---|
| `riquito__tuc` | 42.51% | `T:/determinex-programbench/determinex_pb_tuc_v2/` |
