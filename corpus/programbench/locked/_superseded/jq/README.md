# jq lock

Tool: `jqlang__jq.b33a763`

Locked on: 2026-06-03

Official ProgramBench eval:

- Score: `100/100`
- Runnable denominator: `6874/6874 passed`
- Extra manifest entries: `0 not_run`, `0 skipped`
- Eval artifact: `eval_report.json`
- Submission artifact: `submission.tar.gz`
- Source: `source/` (upstream jq C source at the pinned ProgramBench commit)

Notes:

- Mechanical archive produced by `scripts/pb_lock_archiver.py`.
- The executable path is native jq C. The shell launcher only wires the
  ProgramBench test environment before delegating to `jq.real`.
- Executable hash: `3056b3c130e5ac95`
