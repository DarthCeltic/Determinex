# Family: text_diff

> Diff renderers / highlighters. Take unified diff text (often via stdin) and re-emit with formatting.

## Purpose

Sprint exemplar: `mookid__diffr` — 36.32% → 69.18% across 3 versions.

## Tests-the-family-typically-faces

| Category | Modules | Checks |
|---|---|---|
| ANSI emission | `test_diffr` | Output contains `\x1b[` escape codes on `-` / `+` lines |
| Color spec | `test_colors_*` | `--colors <FACE>:<attr>:<value>` parsing + validation |
| Line numbers | `test_line_numbers_*` | `--line-numbers [STYLE]` with default + aligned/compact |
| Help / version | `test_help_output`, `test_version_flag` | Specific description strings |
| Debug output | `test_debug_flag` | `--debug` writes timing info to stderr |

## Common flags

| Flag | Purpose |
|---|---|
| `--colors <COLORS>...` | Configure face/color/style |
| `--line-numbers [STYLE]` | Show line numbers (default "aligned" if no value) |
| `--large-diff-threshold <N>` | Summarize hunks > N lines |
| `--debug` | Stderr debug |

## Error conventions (DIFFR-SPECIFIC, not standard CLAP)

- **Unknown flag** → rc=2, `"error: bad argument: '<flag>'"`
- **Validation errors** (face name, color value, line-numbers style) → rc=**255**, wording specific:
  - `"error: unexpected face name '<v>' in '<spec>'"`
  - `"error: unexpected color value '<v>' in '<spec>'"`
  - `"error: unexpected line number style '<v>'"`
- **All errors emit USAGE block + `For more information try --help`**

## Output conventions

- Read diff from stdin if not TTY, return rc=0 on empty
- Emit ANSI codes by default (RED for `-`, GREEN for `+`, CYAN for `@@ ...`)
- `--line-numbers`: TAB-separated columns (NOT spaces)
- `--debug`: stderr lines including `"hunk processing time (ms): X.XX"`

## Known traps

1. **rc=255 vs rc=2 split**: NOT all errors are 255. Unknown-flag is rc=2; validation errors are rc=255. (diffr v2 had rc=255 everywhere → regressed unknown-flag tests; v3 split them.)
2. **`--line-numbers` no-value defaults to "aligned"**: tests pass `--line-numbers` alone and expect rc=0. (diffr v2 errored.)
3. **RGB colors are valid**: `R,G,B` triples (each 0-255) are accepted. Don't reject as v2 did.
4. **ANSI 256 is valid**: numeric 0-255 is a valid color value. Error wording includes `'ansi256'` if out of range.
5. **`--colors` accepts both styles AND attribute=value**: `added:foreground:red:bold` — `bold` is a style, `foreground` is an attr-then-value pair.
6. **Help description first**: tests expect description ("diffr adds word-level diff highlights...") in early output, not just the version line.

## Generator pseudocode

```python
def generate(instance_id, probe):
    # 1. Two error helpers: _err_clap (rc=255, validation) + _err_arg (rc=2, unknown flag)
    # 2. ANSI emission ON by default; --no-color toggle
    # 3. Read stdin (skip if TTY)
    # 4. Parse `@@ -A,B +C,D @@` for line numbers
    # 5. --line-numbers default = "aligned" on no value
    # 6. Validate --colors face name + color value (named / 0-255 / RGB triple / #RRGGBB)
    # 7. Debug: print elapsed_ms after rendering
```

## Exemplar tool

| Tool | Best | Best dir |
|---|---|---|
| `mookid__diffr` | 69.18% | `T:/determinex-programbench/determinex_pb_diffr_v3/` |
