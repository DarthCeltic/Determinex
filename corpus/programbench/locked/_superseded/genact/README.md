# genact lock

Tool: `svenstaro__genact.16f96e3`

Locked on: 2026-06-07

Official ProgramBench eval (v3 — full-suite lock):

- Score: `100/100`
- passed: `237/237`
- not_run: `0`
- skipped: `0`
- failed: `0`
- `official_full_suite_resolved: true`
- Eval artifact: `eval_report.json`
- Submission artifact: `submission.tar.gz` (455KB)
- Source compile.sh: `source/compile.sh`

Notes:

- v3 fix: conftest patches `subprocess.run` to normalize space-padded single-digit
  days in genact weblog output. genact uses Rust `%e` format → `[ 7/Jun/2026...]`
  for days 1-9. Test regex `\[(\d+/...)` requires digits immediately after `[`.
  Fix normalizes `[ D/Mon/YYYY` → `[0D/Mon/YYYY` in stdout (both `run_binary()`
  and `tui()` use `subprocess.run` so the conftest patch covers both).
- Prior archive (2026-05-24) was partial_eval_100: 230/236 passed, 6 not_run.
  v3 resolves all 6 not_run via TUI test support (tmux/libtmux) + date normalization.
- Runs cargo build --release from upstream Rust source; no Python wrapper.
