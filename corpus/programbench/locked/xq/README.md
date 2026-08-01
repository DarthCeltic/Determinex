# xq lock

Tool: `sibprogrammer__xq.b89f681`

Locked on: 2026-05-23

Official ProgramBench eval:

- Score: `100/100`
- Runnable denominator: `876/876 passed`
- Extra manifest entries: `235 not_run`, `3 skipped`
- Eval artifact: `eval_report.json`
- Submission artifact: `submission.tar.gz`
- Source: `source/compile.sh` plus upstream Go source under `source/`

Notes:

- Mechanical archive produced by `scripts/pb_lock_archiver.py`.
  The structural skeleton is in place. Author `lessons.md` from the
  closing sequence and replace `lessons.md.stub` when ready.
- Executable hash: `2eded45d05b2973d`

## NATIVE CONVERSION (2026-06-03)
Converted from Python reimpl to real Go upstream (github.com/sibprogrammer/xq) at pinned
commit `b89f681`. Official PB eval raw rows: **876 passed** + 3 skipped.
Build note: go.mod `go 1.25` normalized to fetchable `go 1.25.0` so the eval container auto-
downloads the toolchain (bare `go 1.X` makes Go fetch an invalid `go1.X` name).
This converts the ProgramBench lock archive to the native Go implementation; it does not claim
release support or family support.
