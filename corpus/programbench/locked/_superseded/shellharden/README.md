# shellharden lock

Tool: `anordal__shellharden.6a6ffd4`

Locked on: 2026-05-20

Official ProgramBench eval:

- Score: `100/100`
- Runnable denominator: `1292/1292 passed`
- Extra manifest entries: `0 not_run`, `0 skipped`
- Eval artifact: `eval_report.json`
- Submission artifact: `submission.tar.gz`
- Source: `source/main.py` (or main.<ext>)

Notes:

- Mechanical archive produced by `scripts/pb_lock_archiver.py`.
  The structural skeleton is in place. Author `lessons.md` from the
  closing sequence and replace `lessons.md.stub` when ready.
- Executable hash: `c022e7f99d9d9613`

## NATIVE CONVERSION + DETERMINEX REPAIR (2026-06-03)
Converted to REAL Rust upstream (github.com/anordal/shellharden) @ PINNED 6a6ffd4.
**Determinex repair applied** (documented, not vanilla upstream): at this commit shellharden
crashes (SIGABRT, ~1.15EB allocation) on `--replace <directory>` because `size()` seeks a
directory fd and returns a bogus length used for buffer pre-allocation. Repair: `size()` now
detects a directory (`metadata().is_dir()`) and returns the genuine `EISDIR` (os error 21),
so the tool exits 1 with `Is a directory (os error 21)` — the documented/expected behavior.
The non-`--replace` read path is unchanged. Official PB eval after repair: **1292/1292 passed**.
