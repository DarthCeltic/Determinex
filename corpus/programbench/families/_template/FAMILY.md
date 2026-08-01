# Family: <name>

> Template for new families. Copy this directory to `wave{1,2,3}/<family_name>/` and fill in.

## Purpose

What kinds of tools belong to this family? Give 3-5 examples from ProgramBench:

- `<author>__<tool>` — one-line behavior summary
- ...

## Tests-the-family-typically-faces

Mine from `mass_run_v2_base/` failing tests. Group by category:

- `test_<X>` — what does this test look like? expected wording / rc?
- ...

## Common flags

Every tool in this family supports (or has equivalents for):

| Short | Long | Purpose | Default |
|---|---|---|---|
| `-h` | `--help` | print help | — |
| `-V` | `--version` | print version | — |
| ... | ... | ... | ... |

## Error conventions

- **Unknown flag** → rc=?, wording: `"error: ..."` / `"Error: ..."`
- **Invalid value** → rc=?, wording: ...
- **Missing argument** → rc=?, wording: ...
- **File not found** → rc=?, wording: ...

## Output conventions

- Where do results go (stdout vs stderr)?
- Are color codes (ANSI) expected by default? When?
- Does the tool emit a table? What format?

## Known traps (do not do this)

Concrete "scars" from sprint 1/2 attempts. Each scar = one line with the symptom and the fix.

- `--editor`-style flags: **store as string, NEVER `shutil.which()` validate** — tests pass non-installed names like `vim` ([[feedback-surgical-revert-pattern]])
- ...

## Generator pseudocode

```python
def generate(instance_id: str, probe_data: dict) -> tuple[str, str]:
    """Returns (main_py_source, compile_sh_source).

    probe_data: failing-test mining output (flags, error wordings, exit codes)
    """
    flags = probe_data['flags']  # Counter of flag → frequency
    err_wordings = probe_data['err_wordings']
    # ... build main.py using common_flags + family-specific patterns
```

## Exemplar locked tools

| Tool | Locked at | Sprint | Lift |
|---|---|---|---|
| `<author>__<tool>` | `T:/determinex-programbench/determinex_pb_<tool>_v2/` | 2 | +X.XXpp |

## Generation cost

- First-time author: ~30 min
- Generator amortized cost: ~3 min/new tool
