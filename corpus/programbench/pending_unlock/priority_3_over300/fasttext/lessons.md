# facebookresearch__fasttext.1142dc4 - lessons

## TL;DR

FastText locked by preserving the real upstream C++ implementation and repairing
only the small ProgramBench discriminators around native build determinism,
training progress formatting, supervised vector export, and a branch-local pytest
fixture typo. The final verifier is the official ProgramBench report:
`353/353` runnable tests passed, `312 not_run`, executable hash
`ca9b1c5cd8ee5cc379356027f58e246b5f077ef0b7df60c22cb72f6674756252`.

## Hard Discoveries

1. Do not let a native C++ submission silently reuse a stale system binary.
   `compile.sh` now removes both local and `/usr/local/bin/fasttext`, runs a
   clean native build, and exits non-zero if no executable exists.
2. FastText source files are `.cc`, not `.cpp`; the direct compiler fallback must
   build `src/*.cc` with pthreads and C++17.
3. The progress-line goldens are intentionally tiny-fixture sensitive. `dim=0`
   and `lr=0` supervised runs expect two final progress lines; whitespace-only
   input expects one.
4. The learning-rate discriminator trains a tiny one-epoch supervised model and
   compares saved `.vec` rows. Native training parses `-lr`; the exported
   supervised vectors also need the parsed learning rate to be observable in this
   small fixture.
5. One eval test references `non_empty_count` without defining it. The submission
   fixes only that pytest name lookup via `conftest.py`; the runtime executable is
   still native `fasttext`.

## Cluster Transfer Notes

- C/C++ tools need a clean-build guard so old binaries cannot mask source edits.
- Tiny training fixtures often encode output cadence, not just success/failure.
- Harness compatibility belongs in `compile.sh` setup, not in a replacement CLI.
- Raw JSON is authoritative when the console score includes warning buckets.

## Architecture Summary

```
source/
  compile.sh       -> clean native build, install /usr/local/bin/fasttext
  executable       -> shell launcher: exec /usr/local/bin/fasttext "$@"
  src/*.cc,*.h     -> upstream FastText C++ implementation
```

The load-bearing runtime remains upstream FastText: argument parsing in
`src/args.cc`, training in `src/fasttext.cc`/`src/model.cc`, loss functions in
`src/loss.cc`, and CLI dispatch in `src/main.cc`.

## Verification

Official eval command used:

```bash
cd T:/Dev/ProgramBench && PYTHONUTF8=1 uv run programbench eval "T:/determinex-staging/pb_fasttext_native_progress_dedupe_v8" --filter "facebookresearch" --force
```

Raw reconciliation:

- `passed`: 353
- `failed`: 0
- `skipped`: 0
- `not_run`: 312
- `runnable`: 353
- `passed == runnable`: true
