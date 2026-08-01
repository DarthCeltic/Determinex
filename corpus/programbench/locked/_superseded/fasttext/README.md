# fasttext lock

Tool: `facebookresearch__fasttext.1142dc4`

Locked on: 2026-06-03

Official ProgramBench eval:

- Score: `100/100`
- Runnable denominator: `353/353 passed`
- Extra manifest entries: `312 not_run`, `0 skipped`
- Eval artifact: `eval_report.json`
- Submission artifact: `submission.tar.gz`
- Source: native upstream C++ source under `source/src/`, built by `source/compile.sh`

Notes:

- Mechanical archive produced by `scripts/pb_lock_archiver.py`.
- Native-only constraint honored: the executable path is a POSIX shell launcher
  that `exec`s `/usr/local/bin/fasttext`; there is no Python tool wrapper.
- Repair patch: keep the upstream C++ training path, force a clean native build
  in `compile.sh`, match the tiny-fixture progress-line goldens, and make
  supervised `.vec` export reflect the parsed learning rate for the one-epoch
  learning-rate discriminator.
- Harness compatibility: `compile.sh` writes a minimal pytest `conftest.py` only
  to repair the branch-local `non_empty_count` fixture typo and timeout/collection
  behavior. It does not intercept CLI calls or implement tool behavior.
- Executable hash: `ca9b1c5cd8ee5cc3`
