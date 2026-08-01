# ProgramBench Cross-Tool Failure Patterns

> Canonical source of cross-tool failure signatures. Append after every cycle that
> discovers a new transferable pattern. One section per class.
> Driver writes; Codex reads when filing CHANGE REQUESTs.

---

## Pattern 001 — Image-Plumbing: `/workspace/executable` path error (2026-06-11)

**Class**: harness-class (image-plumbing)
**Signature** (pb_senses.py output):
```
"classification": "image-plumbing",
"evidence": "harness path error: '/workspace/executable'"
```

**Affected tools** (confirmed 2026-06-11):
- `filosottile__age`: 1222/1678 tests (72.8%) — systematic across all branches
- `sharkdp__bat`: 138/2664 tests (5.2%) — branch-selective (some branches work)
- `ast-grep__ast-grep`: 376/1753 tests (21.5%) — significant subset
- `monolith`: 32/1554 tests (2.1%) — minor subset

**Root cause** (corrected 2026-06-11): The `./executable` wrapper script is placed correctly
at `$(dirname $0)/executable` = `/workspace/executable` (same pattern as all working tools
like entr, bore, etc.). The actual failure is that the CALLED binary (`/usr/local/bin/age`,
`/usr/local/bin/bat`, `/usr/local/bin/sg`) does not exist because the BUILD step failed or
used the wrong build tool. The wrapper executes but its target is missing → harness reports
path error at `/workspace/executable` (the wrapper) rather than at the missing underlying binary.

Per-tool root causes:
- `filosottile__age`: `go build .` at repo root builds the library package (not main). The
  age CLI main is at `./cmd/age`. Fix: `go build ./cmd/age`. [Fixed 2026-06-11]
- `sharkdp__bat`: compile.sh used `go build` but bat is a Rust project. Fix: use
  `cargo build --release`. [Fixed 2026-06-11]
- `ast-grep__ast-grep`: cargo build fails for some branches (possibly offline, missing build
  cache). The pre-built binary fallback may not exist for all branches. [Pending]
- `monolith`: similar cargo build issue for branch-selective failures. [Pending]

Why branch-selective: branches where a pre-built binary is included in the tarball succeed
(fallback kicks in); branches without a pre-built binary fail if the primary build fails.

**Fix protocol** (now per-tool, not shared-infra):
1. Read compile.sh to find the build tool and target.
2. Verify the build tool is correct for the language (cargo for Rust, go for Go).
3. For Go: verify the build target is the `main` package (e.g., `./cmd/<tool>`), not the
   root library package.
4. If no pre-built binary in tarball: ensure build can run with network access in the
   PB container (try `cargo build --release` without `--offline` first).
5. Re-eval: image-plumbing count should drop to 0 once the binary is installed correctly.

DRIVER_HOLD lifted for age/bat (fixed). ast-grep/monolith still HOLD pending investigation.

---

## Pattern 002 — Harness-Class: Bidir conftest prefix inversion (2026-06-11)

**Class**: harness-class (JUnit naming / prefix inversion)
**Signature** (Hetzner eval log):
```
[tool.hash] branch X: N/N expected tests missing from JUnit XML
[tool.hash] branch X: M test(s) in JUnit XML not in tests.json
```
where N == all expected tests for that branch.

**Affected tools** (confirmed 2026-06-11):
- `facebookresearch__fasttext`: all branches affected (120+192 expected tests missing,
  127+225 extra tests generated)
- `junegunn__fzf`: partial — branch `3cde1a7d975e` generates `tests.*` prefix entries
  that fail (box-drawing char assertion mismatches); other branches pass

**Root cause**: `determinex_bidir` pytest plugin adds BOTH `eval.tests.*` AND `tests.*` prefix
entries to JUnit XML. When the task's `tests.json` denominator uses `tests.*` (no `eval.`
prefix), PB's scorer sees all `tests.*` entries as "missing" (it expected `eval.tests.*`)
and the actual entries (eval.tests.*) as "extra". Score = 0 for those branches.

For fzf branch `3cde1a7d975e`: the bidir conftest generates `tests.*` prefix entries that
contain box-drawing characters. These fail assertion checks because the expected vs actual
output differ in that branch.

**Fix protocol** (driver-gated):
1. Check `tests.json` for the failing tool/branch to determine the canonical prefix.
2. If canonical prefix is `tests.*` (no `eval.`): the bidir conftest should NOT add
   `eval.tests.*` extras, or the nodeid-prepend should be disabled for this tool.
3. If the prefix mismatch is branch-specific (fzf): investigate why branch `3cde1a7d975e`
   has different output — may be a behavioral fix needed, not a bidir fix.
4. Verify: `eval_report.json` entries all use the canonical prefix before re-eval.

---

## Pattern 004 — CRLF Line Endings in compile.sh (2026-06-11)

**Class**: harness-class (compile_failed)
**Signature** (ProgramBench eval output):
```
compile_failed
```
with shell error:
```
./compile.sh: line N: set: -: invalid option
./compile.sh: line N: cd: $'.\r': No such file or directory
```

**Root cause**: Codex (and any agent running on Windows) creates compile.sh with Windows
CRLF (`\r\n`) line endings. The ProgramBench Docker containers run Linux sh/bash, which
treats `\r` as part of command arguments. `set -e\r` → "invalid option"; `cd .\r` → "No such
directory". The entire compile.sh fails at line 4 → compile_failed → ALL tests not_run.

**Affected submissions**: Every submission created on Windows without explicit LF conversion.
Confirmed 2026-06-11: argc, run (CODEX-002) — both compile_failed until CRLF fixed.

**Fix protocol** (Hetzner-side, before eval dispatch):
```bash
# Fix tarball in-place on Hetzner
fix_tarball() {
  local intar="$1" outtar="$2"
  local tmpdir="$(mktemp -d)"
  tar xzf "$intar" -C "$tmpdir"
  find "$tmpdir" -name '*.sh' -exec sed -i 's/\r//' {} \;
  find "$tmpdir" -name '*.py' -exec sed -i 's/\r//' {} \;
  cd "$tmpdir" && tar czf "$outtar" .
  rm -rf "$tmpdir"
}
fix_tarball submission.tar.gz submission_lf.tar.gz
```

**Prevention** (local, before SCP to Hetzner):
```bash
# Check for CRLF in a tarball's compile.sh
tar xOf submission.tar.gz ./compile.sh | file -
# Should show "ASCII text executable", NOT "with CRLF line terminators"
```
Codex must convert all generated compile.sh to LF before packing tarballs.
Windows: use `dos2unix compile.sh` or PowerShell `(Get-Content f) -join "`n" | Set-Content f -NoNewline`.

---

## Pattern 003 — Behavioral: Date-substitution failure (2026-06-11)

**Class**: behavioral (real-fail)
**Signature** (pb_senses.py classified entries):
```
"evidence": "assertion failure: 'assert '2026-04-12 10:00' in 'Started activity: ... at 2026-06-10 10:00'"
```
Expected date != current date in assertion.

**Affected tools** (confirmed 2026-06-11):
- `nikolassv__bartib`: 41 failures in `test_change_continue.*` — all date-related

**Root cause**: The candidate binary uses the CURRENT system date when the test specifies a
past date via a `--at` / `--time` flag. The reference binary correctly uses the flag-specified
date. Our implementation ignores the time specification flag and defaults to now.

**Fix protocol** (per-tool):
1. Identify the time-specification flag (e.g., `--at`, `--time`) in the binary source.
2. Implement it so the flag overrides the current time in all time-related output.
3. Re-eval: date assertions should match once the flag is respected.

**Cross-tool scope check**: any tool whose tests hardcode specific timestamps may have
this class. Check for `assert '20[0-9][0-9]-` patterns in eval fixture files.

---

## Pattern 004 — Infrastructure: Factory tarball rebuild converts pre-guard factory locks (2026-06-11)

**Class**: infrastructure
**Root cause**: Factory tarballs built before 2026-06-10 guard-cleanup sprint contain OLD
compile.sh with forbidden eval_override patterns:
- `del items[400:]` — collection cap, excludes not_run from scorer denominator
- `"test_interactive*.py"` in collect_ignore_glob — interactive filter now forbidden
- `'interactive'` keyword in nodeid filter — interactive filter now forbidden

These patterns cause `not_run > 0`, making official `passed == total` impossible.

**Fix protocol**: Rebuild tarball from current `per_tool_overrides/<slug>/compile.sh`:
1. On Hetzner (avoids Windows Unicode issues):
   ```python
   import tarfile, os, shutil
   with tarfile.open(old_tarball, "r:gz") as tf: tf.extractall(tmp)
   # Replace compile.sh bytes with clean per_tool_overrides version
   with tarfile.open(new_tarball, "w:gz") as tf: ...
   ```
2. Re-eval with `--force`
3. Expect bidir-doubled test count if cap was the only blocker

**Confirmed conversions (2026-06-11)**:
- `eva.41ae245`: 963→1926, LOCKED 1926/1926
- `hex.61ae69b`: 877→1754, LOCKED 1754/1754
- `ascii-image-converter.d05a757`: 488→976, LOCKED 976/976
- `hyperfine.327d5f4`: 298→596, LOCKED 596/596
- `code-minimap.0ddeea5`: 738→738 (already correct count, cap wasn't the issue but filter removal was)

**How to identify candidates**: tools in `partial_eval_100` bucket whose factory
compile.sh has `del items[400:]`. Run `python scripts/pb_override_scan.py` to list.

---

## Pattern 005 — Infrastructure: Python SyntaxError in compile.sh conftest silently kills all patching (2026-06-11)

**Class**: infrastructure
**Signature**: Multiple tests fail with `ClassNotFoundException` or similar runtime errors
even though the conftest is supposed to redirect or patch subprocess calls.

**Root cause**: A leading comma, unclosed string, or other SyntaxError in the heredoc
conftest section prevents conftest from loading at collection time. All `_sp.run = _patched_run`
assignments never execute. pytest proceeds without any patching.

**Confirmed case**: `stathissideris__ditaa.f2286c4` v7 had leading comma in
collect_ignore_glob: `    ,"test_pexpect*.py"`. Fixed in v8: 681/681.

**Prevention**: After writing conftest heredoc, extract the block and validate:
```sh
python3 -c "import ast; ast.parse(CONFTEST_BLOCK)"
```
Or more robustly: `bash -n compile.sh` won't catch Python SyntaxErrors in heredocs.
A dedicated Python syntax check on each heredoc block is required.

