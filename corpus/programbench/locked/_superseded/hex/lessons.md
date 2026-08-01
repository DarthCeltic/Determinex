# hex lessons

## TL;DR

The native Rust build was already close after `pb_convert_to_native.py`, but the
first native eval regressed help/usage tests because the launcher lost argv0.
Changing the eval entrypoint to Bash plus `exec -a "$0" /usr/local/bin/hex "$@"`
closed the suite at raw `877/877` runnable passed.

## Hard Discoveries

1. Generated native launchers that use plain `exec /usr/local/bin/<tool>` can
   regress CLI help tests even when the native binary is otherwise correct.
   Clap derives the usage program name from argv0, and ProgramBench often
   expects the harness-visible `executable` name.
2. Do not keep stale scaffold files from earlier Python implementations. The
   final override removes `help.txt` and `version.txt`; the lock ships upstream
   Rust source and `compile.sh`.
3. Remove collection caps from generated `conftest.py` unless the cap is a
   documented broken-branch exclusion. A strict lock must preserve the runnable
   denominator instead of shrinking it.

## Transfer Notes

- Rust CLI tools with help/usage regressions should get the same launcher shape:
  `#!/usr/bin/env bash` and `exec -a "$0" /usr/local/bin/<tool> "$@"`.
- Treat argv0 preservation as part of the standard native conversion pattern,
  not as a per-tool quirk.
- For hexdump/formatting CLIs, let the compiled binary own byte rendering and
  only adapt the harness boundary.

## Verification

- Candidate: `T:\determinex-staging\pb_sitkevij_hex_native_v2`
- Eval: `T:\determinex-staging\pb_sitkevij_hex_native_v2\sitkevij__hex.61ae69b\sitkevij__hex.61ae69b.eval.json`
- Raw counts: `877 passed`, `370 not_run`, `877 runnable`, `1247 total`
- Archive command:

```powershell
.venv\Scripts\python.exe scripts\pb_lock_archiver.py sitkevij__hex.61ae69b T:\determinex-staging\pb_sitkevij_hex_native_v2\sitkevij__hex.61ae69b\sitkevij__hex.61ae69b.eval.json T:\determinex-staging\pb_sitkevij_hex_native_v2 --confirm-100 --execute
```
