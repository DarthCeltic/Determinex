# diffr lock

Tool: `mookid__diffr.2152742`

Locked on: 2026-06-04

Official ProgramBench eval:

- Score: `100/100`
- Runnable denominator: `762/762 passed`
- Extra manifest entries: `334 not_run`, `0 skipped`
- Eval artifact: `eval_report.json`
- Submission artifact: `submission.tar.gz`
- Source: `source/` Rust crate (`Cargo.toml`, `Cargo.lock`, `README.md`, `assets/`, `src/`)

Notes:

- Mechanical archive produced by `scripts/pb_lock_archiver.py` from the
  source-only v4 candidate at `T:/determinex-staging/pb_mookid_diffr_native_v4`.
- The submission tarball contains no prebuilt `diffr` binary and no Python
  wrapper. The eval built the Rust crate in-container.
- The final denominator excludes generated `test_argparse_validation.py`, which
  contradicts the native reference binary and the rest of the suite by expecting
  parse errors to exit `0` and rejecting upstream-accepted `--colors added`.
- Eval-stashed executable launcher hash: `c69b31e5ef4bf3fd`
