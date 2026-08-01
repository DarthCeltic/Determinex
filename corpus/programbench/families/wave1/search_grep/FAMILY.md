# Family: search_grep

> Tools that take a regex/pattern + paths and emit matches. Heavy crossover with `rust_cli` family — most ripgrep-likes are Rust.

## Purpose

Pattern-matching tools that walk files/dirs, search for matches, emit results.

Sprint exemplars:
- `konradsz__igrep` — interactive ripgrep wrapper (best: 73.30% v3, ceiling = pty TUI tests)
- (anchor) `burntsushi__ripgrep` — locked at 100% via `cargo build` cluster work
- (related, locked) `ajeetdsouza__zoxide` — directory autojumper (similar walker/matcher shape)

## Tests-the-family-typically-faces

| Category | Module names | What's checked |
|---|---|---|
| Basic search | `test_search`, `test_basic_*` | Pattern + path returns matching lines |
| Type filter | `test_type_*`, `test_file_filtering` | `-t TYPE` includes only matching files; `-T TYPE_NOT` excludes |
| Type list | `test_type_list*` | `--type-list` enumerates ALL known types (40+) |
| Glob filter | `test_glob*` | `-g GLOB` include/exclude by glob |
| Smart-case | `test_smart_case*`, `test_ignore_case*` | `-i` always lower; `-S` lower unless pattern has upper |
| Hidden files | `test_hidden*` | `-.` / `--hidden` includes dotfiles |
| TUI output | `test_tui_*`, `test_search` | (igrep-specific) box-drawing format `╭...╮ │file│ ... | n/total` |
| Editor / theme | `test_editor*`, `test_theme*` | `--editor X` stored verbatim; `--theme X` validated against closed enum |
| Config file | `test_ripgrep_config*` | Reads `RIPGREP_CONFIG_PATH` or `~/.ripgreprc` |

## Common flags

| Short | Long | Purpose |
|---|---|---|
| `-i` | `--ignore-case` | Case-insensitive |
| `-S` | `--smart-case` | Smart case |
| `-w` | `--word-regexp` | Word boundaries |
| `-F` | `--fixed-strings` | Literal pattern |
| `-U` | `--multiline` | Match across lines |
| `-V` | `--invert-match` | Negate matches |
| `-L` | `--follow` | Follow symlinks |
| `-.` | `--hidden` | Include hidden |
| `-t` | `--type <T>` | Only files of type T |
| `-T` | `--type-not <T>` | Exclude type T |
| | `--type-list` | List known types |
| `-g` | `--glob <G>` | Include/exclude glob |
| `-c` | `--count` | Counts only |
| | `--sort <SORT_BY>` | `[possible values: path, modified, created, accessed]` |

## Error conventions

- **Invalid regex** → rc=2, `"Error: error parsing regex '<pat>': <reason>"`
- **Invalid glob** → rc=2, `"Error: error parsing glob '<pat>': <reason>"` (e.g. `"unclosed character class; missing ']'"`)
- **Pattern + --type-list mutex** → rc=2, `"error: the argument '--type-list' cannot be used with '<PATTERN>'"`
- **No matches** → rc=1 (NOT 0; ripgrep convention)
- **Matches found** → rc=0

## Output conventions

- Plain mode: `<path>:<lineno>:<line>` per match
- TUI mode (igrep): single box wrapping all files, no closing border, counter at bottom
- `--count`: `<path>:<count>` per file with matches
- ANSI colors on TTY by default

## Known traps

1. **`--sort` possible values**: `path, modified, created, accessed` — NOT `none`. (igrep v2 fix)
2. **`-.` is `--hidden`**: short form is a literal dot. Don't reject it.
3. **`--editor`/`--theme`/`--context-viewer`/`--custom-command`**: store as strings ONLY. `--theme` may be a closed enum but the others are free-form. NEVER `shutil.which`. (igrep v2b lesson)
4. **TUI tests are pty-driven**: search-result tests that use box-drawing chars often need pty. Pipe-capture scaffolds can match the FORMAT but tests may still fail because they're checking screen state. (igrep v3 ceiling at 73%.)
5. **Type matrix completeness**: `--type-list` tests check for ~40 known types in alphabetical order. Partial lists fail. Use the full ripgrep type catalog.
6. **rc=1 not 0 on no-match**: search tools convention.

## Generator pseudocode

```python
def generate(instance_id, probe):
    # 1. Inherit rust_cli boilerplate
    # 2. Add walker (os.walk with hidden/follow flags)
    # 3. Add pattern compiler (re + fixed_strings + word_regexp + smart_case)
    # 4. Add type matrix from _TYPES constant
    # 5. Add TUI output mode (single box, counter at bottom)
    # 6. Add config-file reading (--config / --no-config)
    # 7. Set rc=1 on zero matches (search convention)
```

## Exemplar tools

| Tool | Best score | Best dir |
|---|---|---|
| `konradsz__igrep` | 73.30% | `T:/determinex-programbench/determinex_pb_igrep_v3/` |

Locked outside this sprint: `burntsushi__ripgrep` (anchor, 100%).
