# Family: file_renamers

> Batch file rename / file-system manipulation tools. Take a pattern + a directory and produce renamed files (or a dry-run preview).

## Purpose

Sprint exemplar: `yaa110__nomino` — 4.73% → 41.12% (+36.39pp). One of the biggest sprint-1/2 wins.

## Tests-the-family-typically-faces

| Category | Modules | Checks |
|---|---|---|
| Placeholder syntax | `test_placeholder` | `{N}` (capture group), `{N:W}` (padding), `{}` (auto-incr), `{name}` |
| Output table | `test_*` (most) | ASCII-bordered markdown table: `+---+---+ \| Input \| Output \| +---+---+` |
| Modes | `test_*_mode` | regex / sort / map / source modes are mutually exclusive |
| Errors | `test_errors` | Missing dir, malformed JSON map, unopened placeholder all rc=1 |
| Test mode | `test_test_mode_*` | `-t/--test` skips rename but emits table; combined with `--mkdir` still creates parent dirs |
| Help / usage | `test_help_usage` | Full usage including arguments section + placeholder format docs |

## Common flags

| Short | Long | Purpose |
|---|---|---|
| `-d` | `--dir <PATH>` | Input directory |
| `-r` | `--regex <PAT>` | Regex match (alias for positional SOURCE) |
| `-s` | `--sort <ORDER>` | `[asc, desc, none]` |
| `-m` | `--max-depth <N>` | Subdir depth |
| `-e` | `--extension` | Preserve extension (default) |
| `-E` | `--no-extension` | Strip extension |
| | `--map <FILE>` | JSON old→new map |
| `-g` | `--generate <FILE>` | Output JSON map |
| `-t` | `--test` / `--dry-run` | Don't actually rename |
| `-k` | `--mkdir` | Create parent dirs |
| `-w` | `--overwrite` | Overwrite existing targets |
| `-q` | `--quiet` | Suppress table |

## Error conventions

- **Unknown flag** → rc=2 (CLAP convention)
- **Missing `-d` directory** → rc=1, `"error: directory '<path>' does not exist"`
- **`-d` is not a dir** → rc=1, `"error: '<path>' is not a directory"`
- **Map file missing** → rc=1, `"error: cannot read map file '<path>': No such file or directory"`
- **Map references nonexistent files** → rc=1, `"error: map references N file(s) not present in directory '<dir>':"` + list
- **Unopened/unclosed placeholder** → rc=1, `"error: unopened placeholder in OUTPUT template '<template>'"` (or unclosed)
- **Mode conflict** → rc=2, `"error: the argument '--regex' cannot be used with '--map'"`

## Output conventions

- Default table: ASCII border  
  ```
  +-----------+---------------+
  | Input     | Output        |
  +-----------+---------------+
  | file1.txt | renamed_1.txt |
  +-----------+---------------+
  ```
- `-q/--quiet`: no table
- `-g <FILE>`: writes JSON map even in test mode
- Test mode + `--mkdir`: creates parent dirs (but no rename)

## Known traps

1. **NEVER double-append extension**: if output template already ends with `.ext`, don't add `f.suffix` again. (nomino v1 → v2 fix)
2. **Markdown table, NOT space-separated**: tests check for the `+---+` border format. v1 used spaces → 80+ test failures.
3. **`-t` + `--mkdir`** create dirs (don't skip dir creation in test mode; only the rename is skipped).
4. **Validate -d BEFORE walking**: nonexistent dir = rc=1 with error, not silent rc=0.
5. **Placeholder validation**: `_PLACEHOLDER_RE.sub` then check if `{` or `}` remains in the stripped string. Errors as `unopened` / `unclosed`.

## Generator pseudocode

```python
def generate(instance_id, probe):
    # 1. Modes: regex / sort / map / source — mutually exclusive
    # 2. Placeholder substitution: {N}, {N:W}, {}, {name}
    # 3. ASCII-bordered table output (compute column widths)
    # 4. Directory validation before walking
    # 5. Map mode: validate referenced files exist
    # 6. Test mode + mkdir: create parents anyway
```

## Exemplar tool

| Tool | Best | Best dir |
|---|---|---|
| `yaa110__nomino` | 41.12% | `T:/determinex-programbench/determinex_pb_nomino_v2/` |
