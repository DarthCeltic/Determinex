# hex lock

Tool: `sitkevij__hex.61ae69b`

Locked on: 2026-06-04

Official ProgramBench eval:

- Score: `100/100`
- Runnable denominator: `877/877 passed`
- Extra manifest entries: `370 not_run`, `0 skipped`
- Eval artifact: `eval_report.json`
- Submission artifact: `submission.tar.gz`
- Source: `source/` contains the pinned upstream Rust crate plus `compile.sh`

Notes:

- Mechanical archive produced by `scripts/pb_lock_archiver.py`.
- Native source only: no Python wrapper or reimplementation is in the execution path.
- Closing repair: `compile.sh` launches the compiled Rust binary through Bash
  with `exec -a "$0"` so help/usage output reports the harness-visible
  executable name.
- Executable hash: `4b3fb73d36b503cc`
