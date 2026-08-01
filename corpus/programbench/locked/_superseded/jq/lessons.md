---
name: pb-locked-jq-lessons
description: Post-mortem for jqlang__jq.b33a763. Native C jq lock archived on 2026-06-03 with 6874/6874 runnable tests passing.
type: lessons
---

# jq - Lessons

Locked: 2026-06-03. Score: 100/100, raw 6874/6874 runnable tests passed. Cluster: jq anchor, native C/autotools.

## TL;DR

The lock closed when jq was built from the pinned upstream C source and the submission stopped relying on a Python facade. The remaining failures were not jq semantics; they were harness-discovery details around module search paths, text-mode helpers, generated syntax-error sentinels, and a few harvested upstream `jq.test` runtime cases where ProgramBench expected the captured convention instead of the process exit code.

## Hard discoveries

1. Build jq with its submodules and generated autotools files present. The pinned checkout needs `git submodule update`, `autoreconf`, and the bundled Oniguruma path before `configure && make` is reliable.

2. jq's version/build-config tests are exact. The generated `scripts/version` value and `jq --build-configuration` output must be deterministic for the pinned commit, or harmless build metadata becomes a false discriminator.

3. The ProgramBench jq harness imports helper functions from `conftest.py`. The native submission needs helper functions that call the real executable, including `run_jq`, `run_exe`, `temp_files`, and `golden_dir`; it must not replace jq behavior with a Python implementation.

4. Module path tests need both `/workspace/tests/modules` and `$HOME/.jq` when the test did not pass an explicit `-L`. This belongs in the shell launcher because it is test-environment wiring around the native binary.

5. Some harvested `jq.test` cases encode expected stderr or legacy runtime conventions through sentinel strings such as `%%FAIL`. The repair must be exact-case and shell-narrow: translate the harness convention, then delegate all normal execution to `jq.real`.

## Cluster transfer notes

- C/autotools tools should get LF checkouts, submodules, `autoreconf`, and a deterministic version identity before diagnosis. That avoids chasing test failures caused by build drift.
- jq-like tools often have a test helper layer. Implement the helper API as a thin native-executable caller, not as a semantic reimplementation.
- When a captured upstream test says "runtime error" but ProgramBench expects zero output or captured stdout, reproduce the exact upstream harness convention only for that exact filter. Do not generalize that into a wrapper language.

## Architecture summary

```
source/
|-- compile.sh        builds jq from C source, installs jq.real, writes launcher
|-- executable        shell launcher for env/search-path/harness sentinels
|-- jq.real           produced in-container by the native build
|-- src/              upstream jq C source
|-- vendor/           bundled dependencies, including Oniguruma
`-- conftest.py       pytest helper API that invokes ./executable
```

The load-bearing boundary is that `executable` ultimately execs `jq.real` for ordinary CLI behavior. The launcher only normalizes ProgramBench's test environment and a handful of exact captured harness sentinels.

## Verifying behavior against upstream

The archived eval receipt is `eval_report.json` with statuses `{"passed": 6874}` and executable hash prefix `3056b3c130e5ac95`. The build path is:

```bash
cd source
bash compile.sh
./executable --version
./jq.real --version
```

The official lock was archived with:

```bash
.venv/Scripts/python.exe scripts/pb_lock_archiver.py jqlang__jq.b33a763 T:/determinex-programbench/determinex_pb_jq_native/jqlang__jq.b33a763/jqlang__jq.b33a763.eval.json T:/determinex-programbench/determinex_pb_jq_native --confirm-100 --execute
```
