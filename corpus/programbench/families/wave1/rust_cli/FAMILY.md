# Family: rust_cli

> The dominant ProgramBench tool family. Rust CLIs typically use `clap` for argument parsing, which dictates much of the expected behavior.

## Purpose

Tools written in Rust that expose a clap-based CLI. Roughly 60% of in-scope ProgramBench tools are Rust CLIs.

Sprint exemplars:
- `yaa110__nomino` — batch file renamer (+36.39pp base → v2)
- `wgunderwood__tex-fmt` — LaTeX formatter (+32.93pp)
- `riquito__tuc` — cut alternative (+40.03pp)
- `foriequal0__git-trim` — git branch cleaner (+40.57pp)
- `konradsz__igrep` — interactive grep (+29.97pp)
- `mookid__diffr` — diff renderer (+25.70pp)

## Tests-the-family-typically-faces

| Category | Typical test_module names | What's checked |
|---|---|---|
| Help output | `test_help_*` | `--help` produces text containing tool description + Usage line + Options section |
| Version output | `test_version_*` | `--version` produces exactly `"<tool> <semver>\n"` |
| Unknown-flag | `test_unknown_*`, `test_argparse_*` | rc=2 (NOT 255 or 1), wording: `"error: unexpected argument '<flag>' found"` |
| Missing value | `test_missing_value_*` | rc=2, wording: `"error: a value is required for '<flag> <NAME>' but none was supplied"` |
| Invalid enum value | `test_invalid_*` | rc=2, wording: `"error: invalid value '<v>' for '<flag> <NAME>'\n  [possible values: a, b, c]"` |
| File not found | `test_file_not_found_*`, `test_missing_file_*` | rc=1 (NOT 2; clap exits 2 only for argparse) |
| Conflicting flags | `test_*_conflict*` | rc=1, wording: `"error: the argument '<X>' cannot be used with '<Y>'"` |

## Common flags

| Short | Long | Purpose |
|---|---|---|
| `-h` | `--help` | Print help (stdout, rc=0) |
| `-V` | `--version` | Print `<tool> <ver>` (stdout, rc=0) |
| `-q` | `--quiet` | Suppress non-essential output |
| `-v` | `--verbose` | More output |
| | `--no-color` | Disable ANSI |
| | `--color` | Force ANSI |

## Error conventions (CLAP)

- **Unknown flag** → rc=2, `"error: unexpected argument '<flag>' found\n\nUsage: <tool> [OPTIONS]...\n\nFor more information, try '--help'.\n"`
- **Invalid enum value** → rc=2, `"error: invalid value '<v>' for '<flag> <NAME>'\n  [possible values: a, b, c]\n"`
- **Missing value** → rc=2, `"error: a value is required for '<flag> <NAME>' but none was supplied\n"`
- **File not found** (runtime, not argparse) → rc=1, varies per tool. Common: `"<tool>: cannot access '<path>': No such file or directory"`
- **Conflicting flags** → rc=1 (sometimes 2), `"error: the argument '<X>' cannot be used with '<Y>'"`

## Output conventions

- Help: stdout, rc=0
- Version: stdout, rc=0 (some tools also write to stderr — be permissive)
- Errors: stderr only
- ANSI by default when stdout is a TTY; honor `--no-color` and `NO_COLOR` env

## Known traps (do not do this)

1. **rc=2 vs rc=1**: clap argparse errors are rc=2. Runtime/IO errors are rc=1. Mixing them up costs ~10 tests per tool.
2. **rc=255 is NOT clap**: diffr uses rc=255 for *validation* errors but rc=2 for unknown-flag. Most Rust CLIs do NOT use 255 anywhere. Only override if probe confirms.
3. **`--editor`-like flags**: store as string, NEVER `shutil.which()` validate. Tests pass `--editor vim` etc. in containers where vim isn't installed. ([[feedback-surgical-revert-pattern]] — igrep v2 lost 49 tests this way)
4. **TUI tests need pty**: search-result-rendering tests that use box-drawing chars (`╭...╮`) are often pty-driven. A scaffold that emits to a pipe won't satisfy them. (igrep v3 hit this ceiling — flattened at 73%.)
5. **Default-value semantics**: flags like `--line-numbers` with optional value should DEFAULT (not error). Tests pass them alone and expect rc=0.
6. **rc-convention split** ([[feedback-rc-convention-split]]): some tools' tests assert `rc in [2, 78]` or `rc == 2` for usage errors. Universal `rc=1` for unknown-flag broke 11 skeema tests. Probe per-tool before changing.

## Generator pseudocode

```python
# scaffold_generator.py
def generate(instance_id: str, probe: dict) -> tuple[str, str]:
    flags = probe['flags']        # Counter
    err_wordings = probe['err_wordings']
    exit_codes = probe['exit_codes']
    tool_name = derive_tool_name(instance_id)

    # 1. Boilerplate with clap-style _err_clap helper (rc=2 default)
    # 2. Help text: tool name + description + Usage + Options block
    # 3. Version: "<tool> <VER>"
    # 4. Recognize every flag in `flags` (with sensible value/bool inference)
    # 5. Validate enum values where probe found `[possible values: ...]` in errors
    # 6. File-not-found path: rc=1 with POSIX wording
    # 7. Optional: if probe shows TUI box-drawing → emit single-box format
    return main_py, compile_sh
```

## Exemplar locked tools

| Tool | Locked dir | Sprint | Best score |
|---|---|---|---|
| `riquito__tuc` | `T:/determinex-programbench/determinex_pb_tuc_v2/` | 2 | 42.51% (+40.03pp) |
| `foriequal0__git-trim` | `T:/determinex-programbench/determinex_pb_git-trim_v2/` | 2 | 49.72% (+40.57pp) |
| `yaa110__nomino` | `T:/determinex-programbench/determinex_pb_nomino_v2/` | 2 | 41.12% (+36.39pp) |

## Generation cost

- First-time generator author: ~45 min (this file)
- Per-new-tool cost: ~5 min probe + ~3 min generator run + ~10 min hand-tuning
