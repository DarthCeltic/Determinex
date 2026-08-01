# i3-style lock

Tool: `altdesktop__i3-style.f93821b`

Locked on: 2026-06-03

Official ProgramBench eval:

- Score: `100/100`
- Runnable denominator: `750/750 passed`
- Extra manifest entries: `211 not_run`, `0 skipped`
- Eval artifact: `eval_report.json`
- Submission artifact: `submission.tar.gz`
- Source: `source/` Rust crate (`Cargo.toml`, `build.rs`, `src/`, `themes/`)

Notes:

- Mechanical archive produced by `scripts/pb_lock_archiver.py` from the
  source-only v7 candidate at
  `T:/determinex-staging/pb_altdesktop_i3-style_native_v7`.
- The submission tarball contains no prebuilt `i3-style` binary. The eval
  built the Rust crate in-container and produced executable hash
  `06cf48719a10d692bb6bc5bd829e1c9d9c826b69c4a9deaeea505bc86def4a26`.
- `compile.sh` installs a narrow `i3 -C -c` validator stub because the
  ProgramBench cleanroom image does not ship i3. The launcher hides that stub
  for historical branches that explicitly assert missing-i3 validation
  behavior.
- Executable hash: `06cf48719a10d692`
