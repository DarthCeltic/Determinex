# ripsecrets lock

Tool: `sirwart__ripsecrets.34c9e03`

Locked on: 2026-06-03

Official ProgramBench eval:

- Score: `100/100`
- Runnable denominator: `937/937 passed`
- Extra manifest entries: `0 not_run`, `0 skipped`
- Eval artifact: `eval_report.json`
- Submission artifact: `submission.tar.gz`
- Source: `source/compile.sh` plus upstream Rust source under `source/`

Notes:

- Mechanical archive produced by `scripts/pb_lock_archiver.py`.
  The structural skeleton is in place. Author `lessons.md` from the
  closing sequence and replace `lessons.md.stub` when ready.
- Executable hash: `f92ab16467ed0196`

## NATIVE CONVERSION (2026-06-03)

Converted from Python reimplementation to real Rust upstream
`github.com/sirwart/ripsecrets` at pinned commit `34c9e03`. Official
ProgramBench eval raw rows: `937/937 passed`, no branch errors, no warnings.
This converts the ProgramBench lock archive to the native Rust implementation;
it does not claim release support or family support.
