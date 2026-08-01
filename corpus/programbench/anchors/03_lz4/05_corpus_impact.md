---
name: lz4-corpus-impact
description: What lz4 adds to the Determinex Oracle. New category — "wrap-an-existing-pip-module-as-CLI" — with disciplined argparse + filename + stream I/O.
type: corpus-impact
---

# lz4 — Corpus Impact

## What this teaches the Oracle

lz4 is the corpus's first *binary-format* tool. It adds three specific failure-category families:

1. **Filename-derivation failure pairs**
   - Suffix-strip on case-mismatched extensions (`.LZ4` vs `.lz4`)
   - Multi-input handling: per-file vs concatenated
   - Stdin/stdout discipline with `-` placeholder vs implicit
   These are deceptively easy to get *almost* right and uniquely brittle in tests.

2. **Stream-CLI failure pairs**
   - Chunk-size choice and buffering at EOF
   - Progress messages to stderr at the right verbosity level
   - Exit-code mapping per error class
   Generalizable to every "read input, transform, write output" tool — which is most of CLI work.

3. **Binary-frame-format failure pairs**
   - Frame magic detection (multi-magic dispatch: legacy vs frame vs skippable)
   - Truncated-input error reporting
   - Concatenated-frame walking
   The Oracle previously had **zero** binary-format competence; this is a new training direction.

## What this makes faster beyond the immediate cluster

- **Every future CLI that wraps a pip module** gets a known-good template. Determinex itself depends on `lz4`, `zstd`, `brotli`, `cryptography`, `lxml`, `regex`, `numpy` — the wrap-and-CLI pattern recurs.
- **The filename-derivation logic is reusable** for any tool with a "default output suffix" pattern (gzip-likes, image converters, audio transcoders, video encoders).
- **The stream-error-handling pattern** transfers to any `-d` / `-t` / `-l` style mode dispatch.

## Compounding with currently-in-progress tools

| In-progress tool | Lift from lz4 lock |
|------------------|--------------------|
| htmlq    | None. |
| shellharden | None. |
| csview   | Minor — csview's stdin streaming may benefit from `_lib/py/streamer.py`. |
| dutree   | None. |

(This anchor's compounding is mostly forward-only.)

## Training data emitted

For a 1,829-test target with ~6 attempts: **~30-40 high-quality training rows**.

Less than jq or fzf, reflecting that the failure space is denser per attempt (round-trips either work or they don't — fewer fine-grained correction cycles).

## Strategic value

**lz4 is the corpus's diversity play.** Justification:
1. Without it, the corpus is jq/fzf-shaped: text DSLs and TTYs. lz4 introduces binary I/O — orthogonal expertise.
2. The cluster's expected resolve rate (3/5 → 4/5 tools) is the lowest of any anchor, BUT the per-tool cost is also the lowest because the algorithm is delegated to a pip module.
3. After locking, the Oracle gains the ability to confidently scaffold any "wrap a binary-format library as a CLI" task — a recurring pattern in the broader Determinex project (model-format converters, container-image tools, audio/video transcoders).

## Action when locked

1. Move artifact from `T:/determinex-programbench/<run>/lz4__lz4.1519f46/source/` into `corpus/programbench/locked/lz4/`.
2. Extract:
   - `corpus/programbench/_lib/py/cli_compress.py`
   - `corpus/programbench/_lib/py/streamer.py`
   - `corpus/programbench/_lib/py/naming.py`
3. Append WAL training pairs to `data/programbench_corpus.jsonl`.
4. Update `corpus/programbench/README.md` status board.
5. Smoke-test on brotli using new fixtures — confirm fastest-possible cluster lift.
6. Commit with tag `programbench-anchor-3-locked`.

## Risk note

**Pip availability is load-bearing.** If a future PB container revision blocks pip during eval, the Python+pip strategy falls. Mitigation: maintain a parallel C implementation in `corpus/programbench/locked/lz4/c/` that uses only stdlib + the lz4 source dropped in directly. Build cost: ~6 hours; only invest if pip access becomes a recurring blocker.
