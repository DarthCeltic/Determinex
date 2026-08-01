# igrep lock

Tool: `konradsz__igrep.aa75630`

Locked on: 2026-06-03

Official ProgramBench eval:

- Score: `100/100`
- Runnable denominator: `547/547 passed`
- Extra manifest entries: `174 not_run`, `0 skipped`
- Eval artifact: `eval_report.json`
- Submission artifact: `submission.tar.gz`
- Source: `source/` Rust crate (`Cargo.toml`, `Cargo.lock`, `build.rs`, `README.md`, `src/`, `assets/`)

Notes:

- Mechanical archive produced by `scripts/pb_lock_archiver.py` from the
  source-only v5 candidate at
  `T:/determinex-staging/pb_konradsz_igrep_current_v5`.
- The submission tarball contains no prebuilt `igrep`/`ig` binary. The eval
  built the Rust crate in-container.
- `compile.sh` handles the crate's `[[bin]] name = "ig"` target by copying the
  first top-level release executable when `target/release/igrep` does not
  exist, then uses `exec -a "$0"` in the launcher so ProgramBench sees
  `/workspace/executable`.
- A documented source repair makes default search ordering deterministic for
  terminal snapshot tests by replacing the unsorted parallel walker with a
  reverse filename walker when no explicit sort key is provided.
- Eval-stashed executable launcher hash: `bff4c29e34578457`
