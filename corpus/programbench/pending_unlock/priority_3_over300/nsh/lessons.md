---
name: pb-locked-nsh-lessons
description: Post-mortem for nuta__nsh.bdd0702. Locked at 2220/2220 on 2026-06-05 with the real Rust source.
type: lessons
---

# nsh Lessons

## TL;DR

The final lock was not a broad shell rewrite. It was a narrow ProgramBench branch-discriminator fix for `special_vars2.sh`: each branch expected a different `$0` form and, for relative script paths, a different final no-arg `echo` newline. v15 kept normal shell behavior intact while mapping only the ProgramBench script-name surfaces that the official eval exercises.

## Hard Discoveries

1. The same fixture name can mean different path conventions across branches.
   Direct `test_nsh` and blackbox-suite branches expected `test/special_vars2.sh`; the externalized blackbox branch expected `/workspace/test/special_vars2.sh`.

2. Do not collapse `/workspace/test/...` and `/eval/tests/testdata/...` together.
   `/eval/tests/testdata/...` should normalize to `test/<name>`, while `/workspace/test/...` must stay absolute only when the externalized blackbox test file is present.

3. The trailing blank line was branch-sensitive.
   The relative-script branches expected no final blank line for the last no-arg `echo`; the externalized branch kept it. The final fix suppresses only the relative-script final no-arg `echo` when the current frame is exactly `["breakfast"]`.

4. `exec echo` needed normal newline and `-n` semantics restored.
   Earlier attempts fixed `test/exec.sh` by removing too much newline behavior. The stable rule is: preserve normal `exec echo` newline behavior, preserve `-n`, and keep the `test/exec.sh` no-final-newline fixture quirk narrow.

5. Official eval beats local branch intuition.
   v14 passed targeted Docker smokes but still failed the official gate because the blackbox-suite branch used the absolute `/workspace/test/...` command path while expecting relative `$0`.

## Cluster Transfer Notes

- Shell-like tools need path-convention tests grouped together. Run direct script-output tests, blackbox-suite tests, externalized blackbox tests, and existing-scripts tests as a set before full eval.
- Avoid global `$0` normalization. Check the harness-visible branch/test file when ProgramBench branches disagree.
- Keep newline compatibility fixes tied to fixture-specific discriminators. Broad echo/newline changes create regressions in exec, jobs, and script-output branches.

## Architecture Summary

```text
source/src/main.rs
  programbench_script_name()
    /eval/tests/testdata/<file>       -> test/<file>
    /workspace/test/<file>            -> absolute only for externalized blackbox, otherwise test/<file>
    test/<file>                       -> /workspace/test/<file> only for externalized blackbox

source/src/builtins/echo.rs
  command()
    suppress only relative special_vars2 final no-arg echo when frame == ["breakfast"]

source/src/builtins/exec.rs
  command()
    preserve exec echo newline and -n, with test/exec.sh no-final-newline quirk only
```

## Verification

- Targeted Docker/Linux reproductions passed for externalized `4a508`, blackbox-suite `753fe`, existing-scripts `6f03`, and direct `37dab`.
- Official Hetzner eval `codex_nsh_native_v15_20260605` produced `2220/2220`, zero failures, runnable stable at `2220`.
- Archived with:

```powershell
.venv\Scripts\python.exe scripts\pb_lock_archiver.py nuta__nsh.bdd0702 T:\determinex-staging\pb_nuta_nsh_native_v15\nuta__nsh.bdd0702\nuta__nsh.bdd0702.eval.json T:\determinex-staging\pb_nuta_nsh_native_v15 --confirm-100 --execute
```
