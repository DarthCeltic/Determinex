# Family: formatters

> Code/text formatters with `--check` / `--print` modes.

## Purpose

Sprint exemplars:
- `wgunderwood__tex-fmt` — LaTeX formatter (38.79% v2, ceiling ~50% due to wrapping complexity)

Related cluster: prettier-likes, black-likes, gofmt-likes (none in active sprint but pattern is the same).

## Tests-the-family-typically-faces

| Category | Modules | Checks |
|---|---|---|
| Args parsing | `test_args_parsing` | Standard flag matrix + `--` separator |
| Check mode | `test_*check*` | `--check` returns rc=1 if changes needed, rc=0 if clean |
| Print mode | `test_print_*` | `--print/-p` writes formatted output to stdout, doesn't modify |
| File ops | `test_file_ops` | Directory without `--recursive` → error |
| Wrapping | `test_wrapping` | Line wrap at `--wraplen` (default 80) |
| Indent | `test_indent_*` | Domain-specific indent rules (LaTeX `\begin/\end`, etc.) |
| Format substitutions | `test_format_subs` | Domain-specific replacements |
| Stdin handling | `test_io_behavior` | `--stdin` reads from stdin, writes formatted to stdout |

## Common flags

| Short | Long | Purpose |
|---|---|---|
| `-c` | `--check` | Check only, rc=1 if changes needed |
| `-p` | `--print` | Print formatted to stdout |
| | `--stdin` | Read from stdin, write to stdout |
| `-r` | `--recursive` | Walk dirs |
| | `--config <FILE>` / `--noconfig` | Config file handling |
| `-l` | `--wraplen <NUM>` | Wrap line length |
| `-t` | `--tabsize <NUM>` | Spaces per indent |
| | `--usetabs` | Use tabs instead of spaces |
| | `--fail-on-change` | Exit 1 if any file changed |
| `-q` | `--quiet` / `-s` `--silent` | Suppress output |

## Error conventions

- **Unknown flag** → rc=2, tip: `"tip: use '-- <flag>'"` (suggests `--` before flag-shaped path)
- **`--check` finds mismatch** → rc=1, stderr `"ERROR: <tool> <path>: Incorrect formatting."`
- **Directory without `--recursive`** → rc=1, `"ERROR: <tool> <path>: Is a directory (use --recursive to walk it)."`
- **File not found** → rc=1, `"ERROR: <tool> <path>: No such file or directory."`

## Output conventions

- Default mode: write formatted content in-place
- `--print`: stdout, don't modify
- `--check`: stderr error message on mismatch, no file modification
- `--stdin`: read stdin, write stdout, no file involved
- Always end formatted output with trailing newline

## Known traps

1. **`--check` rc=1, NOT rc=2**: tests assert `rc == 1` for mismatch. (tex-fmt v1 had rc=2.)
2. **`--` separator captures next tokens as paths**: even `--bogus` after `--` is a file path. File-not-found = rc=1.
3. **Domain-aware indent**: pure space-stripping loses structure. LaTeX needs `\begin/\end` tracking; YAML needs map nesting; etc.
4. **Don't collapse all blank lines to zero**: keep 1 blank as separator. (Multiple blanks → 1.)
5. **Wrap then indent, NOT indent then wrap**: wrap operates on assigned indent; reversing reverses both.

## Generator pseudocode

```python
def generate(instance_id, probe):
    # 1. Tip helper: tip="use '-- <flag>'" when unknown flag found
    # 2. _expand_files returns (files, rc) — non-recursive dir = error
    # 3. _process_file: --check returns 1 on diff (NOT 2)
    # 4. _format: indent based on domain syntax (override per tool)
    # 5. Always end output with newline
```

## Exemplar tool

| Tool | Best | Best dir |
|---|---|---|
| `wgunderwood__tex-fmt` | TBD (v3 eval in flight) | `T:/determinex-programbench/determinex_pb_tex-fmt_v3/` |
