# Determinex Diagnostics Layer — "Deep Senses"

## What It Is

The Senses layer enriches the compiler-oracle retry loop with three ranked
diagnostic signals.  The **Compiler Oracle remains the sole verdict**.  Senses
are inputs to the Architect's correction prompt, not judges.

```
Gate FAIL
   → enrich(workspace, lang, failure_context)
      → DiagnosticBundle (token-budgeted, Cloak-safe)
         → injected into retry prompt AFTER compiler errors
            → Architect generates correction
               → Gate again (oracle decides)
```

## Package: `scripts/determinex_senses/`

```
determinex_senses/
  __init__.py        DiagnosticSection, DiagnosticBundle, render()
  lsp_sidecar.py     Module 1 — LSP headless client
  divergence.py      Module 2 — gdb/delve divergence capture
  syscall_diff.py    Module 3 — strace differential (Linux only)
  enrich.py          enrich() entry point — assembles all sections
```

## Module 1 — LSP Sidecar (`lsp_sidecar.py`)

**What it sees:** publishDiagnostics notifications from a headless language
server (rust-analyzer / gopls / clangd / pyright / typescript-language-server)
run over stdio against the candidate workspace.

**When it runs:** Before the compile gate as an early-warning pass; also
attached to the retry prompt when the gate fails.

**Output schema per item:**
```json
{
  "file": "src/lib.rs",
  "line": 42,
  "severity": "ERROR",
  "code": "E0308",
  "message": "mismatched types: ...",
  "related_symbols": ["T", "U"]
}
```

**Limits:** 10 files max per pass (most-recently-modified); 30s timeout/file;
per-language enable/disable in `.determinex/senses.toml`.

---

## Module 2 — Divergence Capture (`divergence.py`)

**What it sees:** The candidate binary's abort/exit/panic path under a
scripted debugger (gdb batch mode for Rust/C/C++, delve for Go).

**When it runs:** When a behavioral test fails with non-obvious stdout diff
and a candidate binary path is provided in `failure_context`.

**Output schema:**
```json
{
  "test_id": "eval.tests.test_foo.test_bar",
  "divergence_point": "captured",
  "stack": "#0  ...\n#1  ...",
  "locals_excerpt": "x = 42\nresult = None",
  "exit_code": 1
}
```

**Platform:** Linux (Hetzner).  Skipped on Windows with a WAL note.
**Timeout:** 60s hard limit with Job Object / cgroup isolation.
**Rule:** Debugger is ONLY attached to the candidate.  Reference stays
black-box (Module 3 observes the reference dynamically via strace, never statically).

---

## Module 3 — Syscall Differential (`syscall_diff.py`)

**What it sees:** The delta between `strace -f -e trace=file,desc,process`
runs of the reference and candidate executables against an identical input.

**When it runs:** When a reference binary path is available and the failing
test is a behavioral mismatch (not a compile error).

**Output schema:**
```json
{
  "first_diff": "line 47: ref='openat(AT_FDCWD, \"/etc/passwd\"...' | cand='openat...'",
  "file_access_delta": ["open#3: ref=... cand=..."],
  "exit_path_differs": true,
  "ref_syscall_count": 312,
  "cand_syscall_count": 298,
  "summary": "1 file-order delta; exit differs=true"
}
```

**Platform:** Linux only.  `strace` must be in PATH.  Returns empty section
with WAL note on Windows or if strace is unavailable.

## BRIGHT LINE — Enforced in Code

> **Dynamic observation ONLY**: run, trace, fuzz.
> **NO** objdump / disassembly / decompilation / symbol-dumping of the
> reference binary.

`syscall_diff.py::refuse_static_re()` raises `ValueError` before any
subprocess exec if a static-RE tool name appears in the binary path.
`scripts/pb_senses_guard.py --guard` scans all session WALs and fails CI
if any static-RE tool name is found.

Blocked tools: `objdump`, `readelf`, `nm`, `strings`, `radare2`, `r2`,
`ghidra`, `ida/ida64`, `iaito`, `binaryninja`, `rizin`, `rz-bin`,
`capstone`, `unicorn`, `angr`, `pwndbg`, `peda`.

---

## Token Budget and Section Ranking

Sections are ranked; lowest rank is highest priority.  The compiler-error
section (rank 0) is injected externally (by the retry loop).

| Rank | Section      | Truncated first? |
|------|-------------|-----------------|
| 0    | compiler    | No — oracle output always first |
| 1    | lsp         | Last           |
| 2    | divergence  | Second         |
| 3    | syscall_diff| First          |

Default budget: 2000 tokens.  Configurable per run via `TOKEN_BUDGET`
on `DiagnosticBundle`.

---

## Cloak Integration

Every `DiagnosticBundle.render()` output passes through the existing
Project Cloak re-obfuscation path before any cloud call.  LSP symbol names,
file paths, and strace function names are all re-obfuscated as `x_NNNN`
tokens.  The cloud AI sees only obfuscated identifiers — same guarantee as
compiler errors.  Zero leakage.

---

## WAL Integration

Each retry attempt's WAL record gains a `senses` field:

```json
{
  "attempt": 2,
  "patch": "...",
  "compile_errors": ["..."],
  "senses": {
    "lang": "rust",
    "workspace": "/workspace",
    "cloak_applied": true,
    "sections": [
      {"kind": "lsp", "rank": 1, "items": 3, "token_estimate": 120},
      {"kind": "syscall_diff", "rank": 3, "items": 1, "token_estimate": 45}
    ]
  }
}
```

These become flywheel training pairs: (error + senses → fix), same corpus
pipeline as today's (error → fix) pairs.

---

## Guard Chain

All three guards must pass before archiving any new ProgramBench lock:

```bash
python scripts/pb_board_guard.py --guard      # lock invariants
python scripts/pb_override_scan.py --guard    # no collection caps
python scripts/pb_senses_guard.py --guard     # no static-RE in WALs
```

---

*Determinex · Ryan Gurganious · Lunarian Data Systems · June 2026*
