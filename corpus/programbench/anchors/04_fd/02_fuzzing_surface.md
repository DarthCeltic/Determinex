---
name: fd-fuzzing-surface
description: Specific testable behaviors in fd. Heavy on smart-case, gitignore semantics, exec placeholders, depth combinatorics, and the type/extension matrix.
type: fuzzing-surface
---

# fd — Fuzzing Attack Surface

1,405 tests across 10 branches. The 527-test branch is likely the regex/glob/literal pattern matrix. The 226-test branch is likely the type/extension/size filter matrix.

## CLI matrix

### Pattern modes
- (default): regex on basename
- `-p` / `--full-path`: regex on full relative path
- `-F` / `--fixed-strings`: literal substring (still on basename unless `-p`)
- `-g` / `--glob`: glob pattern (basename unless `-p`)

### Case modes
- (default): smart-case (insensitive iff pattern is all lowercase)
- `-i` / `--ignore-case`
- `-s` / `--case-sensitive`

### Type filter (`-t`)
- `f` regular file
- `d` directory
- `l` symlink
- `x` executable
- `e` empty
- `s` socket
- `p` named pipe
- `b` block device
- `c` character device
- Multiple `-t` are OR'd

### Extension filter (`-e`)
- `-e py` matches `*.py` (case-insensitive on extension)
- Multiple `-e` are OR'd
- `-e ""` matches files without extension

### Hidden / ignore
- `-H` / `--hidden` include hidden files (otherwise excluded)
- `-I` / `--no-ignore` ignore `.gitignore`, `.fdignore`, `.ignore`
- `--no-ignore-vcs` ignore `.gitignore` only (keep `.fdignore`)
- `--no-ignore-parent` don't read parent dir ignore files
- `--no-global-ignore-file` don't read `~/.config/fd/ignore`

### Depth
- `--max-depth N` / `-d N`
- `--min-depth N`
- `--exact-depth N`

### Size
- `-S +1k` files larger than 1 KiB
- `-S -2m` files smaller than 2 MiB
- `-S =10b` exactly 10 bytes
- Multiple `-S` are AND'd
- Units: `b`, `k`, `m`, `g`, `t`, `ki`, `mi`, `gi`, `ti` (decimal vs binary)

### Mtime
- `--changed-within DURATION` (last N units ago)
- `--changed-before DURATION`
- DURATION: `30s`, `5m`, `2h`, `1d`, `2w`, `2024-01-01`, etc.

### Output
- `-0` / `--print0` NUL-separated
- `-l` / `--list-details` ls-like long format (with colors, perms, size, mtime)
- `-c always|auto|never` color
- `--strip-cwd-prefix` (newer fd)
- `-1` / `--max-results 1` (limit to N)

### Exec
- `-x CMD args... ;` exec per result
- `-X CMD args...` exec batch
- Placeholders: `{}`, `{.}`, `{/}`, `{//}`, `{/.}`
- `--threads N` / `-j N`

### Search root
- positional `[pattern] [paths...]`
- if no `paths` → current directory
- `-S` is size flag, NOT search root (despite collision name)

## Smart-case rule (very testable)

Pattern: `Foo` → case-sensitive. Pattern: `foo` → case-insensitive. **Detection MUST be Unicode-aware.** `Köln` = uppercase = sensitive. `λambda` = no case-distinct chars = lowercase by default.

## Gitignore semantics (testable subtlety)

- `.gitignore` rules apply per-directory.
- A `.gitignore` rule like `!important.txt` re-includes a previously excluded file.
- `.fdignore` overrides `.gitignore` (fd-specific).
- `.ignore` is a plain ignore file (used by ripgrep too).
- Without `-H`, hidden files (starting with `.`) are excluded REGARDLESS of gitignore.
- With `-H` but without `-I`, gitignore still applies.

## Exec placeholder semantics (testable subtlety)

- `{}` is the full path as fd would output it (relative if root was relative, absolute if root was absolute).
- `{.}` = `{}` minus the last `.ext`.
- `{/}` = basename of `{}`.
- `{//}` = parent of `{}`.
- `{/.}` = basename of `{}` minus extension.

Multiple placeholders in one command: `fd -e jpg -x convert {} {.}.png` — both replaced for each match.

`-x` runs sequentially in default mode; **`-X` is batched and runs once at end**.

## Output format edges (where 90→100% lives)

1. **Trailing newline** — fd prints each result followed by `\n` (or NUL with `-0`). No trailing newline after the last result if input was empty.
2. **Path separator** — fd ALWAYS emits `/` even on Windows. PB containers are Linux so this matches.
3. **Search-root visibility** — fd does NOT include the root in output by default (only its descendants). With `--include-root` (rare) it does.
4. **Symlink loops** — fd does not follow without `-L`. With `-L`, detects and skips already-visited inodes.
5. **`-l` format** — columns: `mode` (rwxr-xr-x style), `users` count, owner, group, size, mtime, path. Spacing matches `ls -l`.
6. **Color codes** — only emitted with `--color always` OR `--color auto` AND TTY. PB pipes always.
7. **`--null` separator** — NUL byte, no newline anywhere.
8. **Exec stdout/stderr** — exec'd command's output passes through to fd's stdout/stderr unchanged.

## Exit codes

- 0: at least one match found OR exec'd commands all succeeded
- 1: no matches found
- 2: bad usage (clap error)
- 3+: exec'd command failed (passes through return code)

## Stderr

- Errors prefixed `[fd error]: ` (with brackets, lowercase 'fd', then colon-space).
- Bad regex: `[fd error]: regex parse error: ...`
- Permission denied during walk: `[fd error]: Could not retrieve information for ...`

## Testable surprise behaviors

1. **`fd '' /etc`** — empty pattern matches everything in `/etc` (regex `''` matches all).
2. **`fd -e ""`** — files with NO extension.
3. **`fd -t f -t d`** — files OR directories (OR'd, not AND'd).
4. **`fd -p '/foo/'`** — full-path match for path containing `/foo/`.
5. **`fd -g '*.{js,ts}'`** — brace expansion in glob mode.
6. **`fd -x echo {.}`** — strips extension before passing.
7. **`fd -X wc -l`** — passes ALL results to single `wc -l`.
8. **`fd --threads 1`** — deterministic order (alphabetic by directory traversal).
9. **`fd -E 'node_modules'`** — exclude pattern at runtime.
10. **`fd -d 1`** — only direct children of search root (depth 1).

## Likely test name structure

- `test_basic_pattern`, `test_regex_pattern`, `test_glob_pattern`, `test_literal_pattern`
- `test_smart_case`, `test_ignore_case`, `test_case_sensitive`
- `test_type_file`, `test_type_dir`, `test_type_symlink`, `test_type_executable`
- `test_extension_single`, `test_extension_multiple`, `test_extension_empty`
- `test_max_depth`, `test_min_depth`, `test_exact_depth`
- `test_hidden`, `test_no_ignore`, `test_gitignore_respect`
- `test_size_greater`, `test_size_less`, `test_size_exact`
- `test_changed_within`, `test_changed_before`
- `test_exec_simple`, `test_exec_placeholder_basename`, `test_exec_placeholder_parent`, `test_exec_batch`
- `test_print0`, `test_list_details`, `test_color_always`
- `test_full_path_match`
