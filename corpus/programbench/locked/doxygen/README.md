# doxygen lock

Tool: `doxygen__doxygen.966d98e`

Locked on: 2026-06-03

Official ProgramBench raw eval:

- Runnable denominator: `250/250 passed`
- Extra manifest entries: `10 not_run`, `1 skipped`
- Eval artifact: `eval_report.json`
- Submission artifact: `submission.tar.gz`
- Source: native upstream C++ tree under `source/`; `source/compile.sh`
  builds/installs the Doxygen binary and emits a shell launcher.
- Console caveat: ProgramBench summary reports score `96` with
  `ERRORS: WARN: 1` because branch `8c618fb31ebb` has JUnit entries outside
  `tests.json`. The lock criterion used here is the project rule enforced by
  `scripts/pb_lock_archiver.py`: `passed == runnable`.

Notes:

- Mechanical archive produced by `scripts/pb_lock_archiver.py`.
- Executable hash: `9f4a29d70a68f242`
