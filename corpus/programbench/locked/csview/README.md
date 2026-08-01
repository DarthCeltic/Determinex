# csview lock

Tool: `wfxr__csview.8ac4de0`

Locked on: 2026-05-21

Official ProgramBench eval:

- Score: `100/100`
- Runnable denominator: `347/347 passed`
- Extra manifest entries: `0 not_run`, `1 skipped`
- Eval artifact: `eval_report.json`
- Submission artifact: `submission.tar.gz`
- Source: `source/main.py` (or main.<ext>)

Notes:

- Mechanical archive produced by `scripts/pb_lock_archiver.py`.
  The structural skeleton is in place. Author `lessons.md` from the
  closing sequence and replace `lessons.md.stub` when ready.
- Executable hash: `10ae9420fa6a4546`

## NATIVE CONVERSION (2026-06-03)
Converted from Python reimpl to the REAL Rust upstream (github.com/wfxr/csview)
built at the PINNED commit `8ac4de0`. Official ProgramBench Docker eval:
**347/347 passed** + 1 environmental skip (test_unreadable_file_permission_denied_exit_1,
identical to the original lock's denominator). Now genuine native support.
