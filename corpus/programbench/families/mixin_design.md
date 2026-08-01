# Family Mixin Architecture (sprint 4 onward)

> Move from "26 isolated generators" to "base family + composable mixins + per-tool probe".
> Each sprint-2/v3 win surfaces a reusable mixin extracted from the per-tool fix.

## The current problem

Today every family has its own complete `FamilySpec` with `behavior` field.
Behaviors are flat: `generic | search | diff | rename | git | coreutils | formatter | passthrough`.

But real tools are unions of behaviors:
- `igrep` = rust_cli + **search** + **tui** + **editor_config**
- `diffr` = rust_cli + **diff** + **ansi_output**
- `tex-fmt` = rust_cli + **formatter** + **latex_document**
- `git-trim` = rust_cli + **git_wrappers** + **config_env**
- `nomino` = rust_cli + **file_renamers** + **table_output**
- `tuc` = rust_cli + **shell_coreutils** + **csv-ish**

The flat behavior model can't compose these. Each `behavior_<X>` function in
`generator_lib.py` is mutually exclusive. So `igrep` had to be hand-coded after
the search generator emitted a non-TUI version.

## The mixin model

Replace single `behavior: str` with `behavior: str` PLUS `mixins: tuple[str, ...]`:

```python
@dataclass(frozen=True)
class FamilySpec:
    family: str
    behavior: str                        # primary execution path
    mixins: tuple[str, ...] = ()         # composed behaviors layered on top
    description: str = ""
    extra_flags: tuple[str, ...] = ()
    value_flags: tuple[str, ...] = ()
    version: str = "0.1.0"
```

A mixin is a self-contained module that:
1. Exposes additional flags (added to `extra_flags` at scaffold-render time)
2. Optionally provides a function that runs BEFORE the primary behavior
3. Optionally provides a function that runs AFTER the primary behavior
4. Optionally transforms the output (e.g. `ansi_output` wraps lines in escape codes)

## Mixin registry

```python
# corpus/programbench/families/mixins/
MIXINS: dict[str, MixinSpec] = {
    "ansi_output":     MixinSpec(...),    # wrap outputs with \x1b[...] codes
    "table_output":    MixinSpec(...),    # ASCII-bordered markdown table
    "tui":             MixinSpec(...),    # box-drawing chars, --query, --filter
    "editor_config":   MixinSpec(...),    # --editor / --theme / --context-viewer
    "file_walker":     MixinSpec(...),    # --hidden / --follow / -t / -g / globs
    "json_io":         MixinSpec(...),    # --json / --pretty / --compact-output
    "config_env":      MixinSpec(...),    # --config / --no-config / RIPGREP_CONFIG_PATH
    "stdin_handler":   MixinSpec(...),    # --stdin / fallback when no positional
    "dry_run":         MixinSpec(...),    # --dry-run / -t / --test
    "verbose_levels":  MixinSpec(...),    # -v / -vv / -vvv / --verbose
}
```

## Composition examples

```python
"search_grep": FamilySpec(
    family="search_grep",
    behavior="search",
    mixins=("file_walker", "ansi_output", "editor_config", "config_env"),
),

"text_diff": FamilySpec(
    family="text_diff",
    behavior="diff",
    mixins=("ansi_output", "stdin_handler"),
),

"formatters": FamilySpec(
    family="formatters",
    behavior="formatter",
    mixins=("stdin_handler", "dry_run", "verbose_levels", "config_env"),
),

"file_renamers": FamilySpec(
    family="file_renamers",
    behavior="rename",
    mixins=("file_walker", "table_output", "dry_run"),
),

"git_wrappers": FamilySpec(
    family="git_wrappers",
    behavior="git",
    mixins=("dry_run", "verbose_levels", "config_env"),
),
```

## Build order (next sprint)

1. **Extract mixins from existing sprint-1/2/3 winners** (the proof-points):
   - `table_output` from nomino v2 (ASCII border + column widths)
   - `ansi_output` from diffr v2/v3 (color codes for +/- lines)
   - `tui` from igrep v3 (single-box format, counter line)
   - `editor_config` from igrep v2b (store editor/theme as string, NEVER `shutil.which`)
   - `file_walker` from igrep + nomino (hidden/follow/type/glob handling)
   - `dry_run` from nomino + git-trim
   - `config_env` from git-trim (`class=Config (7)` rc=7 wording)

2. **Add `mixins` field to FamilySpec, default empty tuple** (backward-compatible)

3. **Extend `render_main` to compose mixin code into the generated main.py**:
   - Mixin flags added to `KNOWN_FLAGS` and `VALUE_FLAGS`
   - Mixin pre-hooks run before behavior
   - Mixin output transforms wrap the behavior's stdout

4. **Re-run bulk generate** — every tool gets its family's mixin composition automatically

5. **Re-run smoke + ranked eval** — mixin-composed scaffolds should outscore flat-behavior v1s

## Promotion rule re-stated for mixin world

When a per-tool v2 wins +10pp+, ask:
- Was the lift due to a flag/wording fix? → already in family spec
- Was the lift due to a NEW BEHAVIOR PATTERN? → extract as mixin, register in MIXINS
- Was the lift due to a SCAR (e.g. "don't validate editor")? → encode in mixin docstring

Then re-run bulk-gen on every family that uses that mixin. Every win compounds.

## Status

- Sprint-4 phase 1-3 done with flat FamilySpec (105 generated, 105 smoke OK)
- Mixin architecture: DESIGN COMPLETE (this doc)
- Implementation: queued (sprint 4 phase 5 / sprint 5 depending on tier-10 eval outcome)
- The first mixins to extract are listed in step 1 above
