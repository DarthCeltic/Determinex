# Family: git_wrappers

> Tools that wrap `git` subprocess calls — branch cleanup, hook helpers, log formatters, etc.

## Purpose

Sprint exemplar: `foriequal0__git-trim` — 9.15% → 49.72% (+40.57pp). Biggest single sprint-1 lift.

## Tests-the-family-typically-faces

| Category | Modules | Checks |
|---|---|---|
| Bare repo detection | `test_errors` | rc=1, `"Error: Bare repository is not supported"` |
| No remote | `test_errors` | rc=1, `"Error: <tool> requires at least one remote"` |
| No base branch | `test_errors` | rc=1, `"Error: No base branch is found!"` |
| Conflicting flag pairs | `test_argparse_validation` | rc=1, `"Error: Flag '<X>' and 'no-<X>' cannot be used simultaneously"` |
| Config parse | `test_config*` | rc=7, `"Error: failed to parse '<v>' as an integer; class=Config (7)"` |
| Dry-run output | `test_harvest`, `test_core` | Multi-section structured output: `Branches that will remain / would be deleted` |
| Invalid delete range | `test_errors` | rc=1, `"Error: Invalid delete range format \`<bad>\`"` |

## Common flags (git-trim shape; varies by tool)

| Short | Long | Purpose |
|---|---|---|
| `-b` | `--bases <BASE>...` | Base branches (comma-separated) |
| `-p` | `--protected <GLOB>...` | Protected branches |
| | `--update` / `--no-update` | Fetch from remote first |
| | `--update-interval <SECS>` | Skip fetch if recent |
| | `--confirm` / `--no-confirm` | Prompt before deletes |
| | `--detach` / `--no-detach` | Detach HEAD if deleting current |
| `-d` | `--delete <KIND>...` | Categories to delete |
| | `--dry-run` | Preview only |

## Error conventions

- **CLAP argparse errors** → rc=2 (unknown flag, missing value)
- **Repo preflight errors** → rc=1 (`Bare repository`, `requires at least one remote`, `No base branch`)
- **Config parse errors** → rc=7 with `class=Config (7)` suffix (git2 library convention)
- **Conflicting flag pairs** → rc=1 with specific `"Flag 'X' and 'no-X' cannot be used simultaneously"` wording
- **Repository missing** → rc=1, `"Error: could not find repository at '.'; class=Repository (6); code=NotFound (-3)"`

## Output conventions

- Dry-run multi-section structure:
  ```
  Branches that will remain:
    local branches:
      master [base]
      ...
    remote references:
      origin/main
      ...

  Branches that would be deleted:
    local branches:
      ...
    remote references:
      ...

  Delete the above branches and references manually, or rerun with --no-dry-run if you are sure (dry run).
  ```
- Tag `[base]` / `[protected]` after branch name where applicable

## Known traps

1. **rc=7 for config errors**: git2's `class=Config (7)` propagates. Use rc=7, not 1 or 2.
2. **Conflicting flag detection happens AFTER parse**: track `seen_yes` / `seen_no` per flag pair, validate at end. (git-trim v2 pattern.)
3. **Git subprocess MUST be available**: scaffold should detect git missing and emit the repo-not-found error gracefully.
4. **`--no-detach` is real**: don't assume `--detach` is the only form. Handle both.
5. **Delete range KINDS are an enum**: `{merged-local, merged-remote, stray, diverged, merged, local, remote}`. Invalid kind → rc=1 with backtick-quoted error.

## Generator pseudocode

```python
def generate(instance_id, probe):
    # 1. Recognize conflicting flag pairs from probe (find `--X` and `--no-X` siblings)
    # 2. Repo preflight: git rev-parse --is-bare-repository, git remote
    # 3. Branch enumeration: git for-each-ref refs/heads + refs/remotes
    # 4. Base branch resolution: probe defaults from {master, main, develop}
    # 5. Dry-run output: structured sections with [base] / [protected] tags
    # 6. Config error wording with class=Config (7) + rc=7
```

## Exemplar tool

| Tool | Best | Best dir |
|---|---|---|
| `foriequal0__git-trim` | 49.72% | `T:/determinex-programbench/determinex_pb_git-trim_v2/` |
