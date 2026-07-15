# Config Root Allowlist

> Locked under `locks/sentinel/CLAUDE_CONFIG_ROOT_ALLOWLIST_LOCK_001.json`.

Remediates **CLAUDE-AUTH-011**: local model config save path was
inside the repo, no allowlist, no dangerous-root denylist.

## Verifier

`scripts/ide/config_root_allowlist.verify(requested_root, allowed_parents=...)`
returns `CONFIG_ROOT_ALLOWLIST_PASSED` iff:

1. `requested_root` is non-empty and contains no NUL
2. The raw input contains no `..` segments
3. The resolved path is not in the dangerous-root denylist
4. The resolved path equals or is inside at least one
   `allowed_parents` entry

## Dangerous-root denylist

**POSIX**: `/`, `/etc`, `/usr`, `/bin`, `/sbin`, `/boot`, `/sys`,
`/proc`, `/dev`, `/root`, `/var`, `/lib`, `/lib64`, `/System`,
`/Library`.

**Windows**: `C:\`, `C:\Windows`, `C:\Program Files`,
`C:\Program Files (x86)`, `C:\ProgramData`, `D:\Windows`, `E:\Windows`.

## Allowed parents

Callers MUST supply `allowed_parents` explicitly. An empty list
refuses every root. The verifier never expands the allowlist on
its own — that's the entire point.

Typical allowed parents:

- the user's profile directory
- the workspace root the operator explicitly selected
- a temp directory (for test fixtures)

## What the verifier does NOT do

- Does NOT create the directory.
- Does NOT write to disk.
- Does NOT authorize source mutation or training.
