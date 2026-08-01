# Verification-First Runbook - 2026-05-12

## Current truth

The local aggregate now treats only official ProgramBench eval artifacts as scoring evidence and deduplicates copied corpus reports against their ProgramBench instance ids.

Verified locks visible to the aggregate:

| Tool | Score | Evidence |
|------|-------|----------|
| htmlq | 2056/2056 | official eval JSON |
| ripsecrets | 935/935 | official eval JSON |
| zoxide | 577/577 | official eval JSON |
| ripgrep | 2536/2536 scored | official eval JSON |

Near locks:

| Tool | Score | Next action |
|------|-------|-------------|
| structured data anchor | TBD | choose `jq` or rebuild `yj` |

Important correction: rounded or display-100 scores are not locks. A tool is locked only when `passed == total` in an official eval artifact.

## Run discipline

1. Pick exactly one target tool.
2. Parse the latest official eval JSON before editing.
3. Classify failures into behavior groups, not model guesses.
4. Patch the smallest group that can plausibly close the tool.
5. Rebuild `submission.tar.gz` before every official ProgramBench eval.
6. Run `programbench eval` and archive the resulting eval JSON.
7. Update the corpus only after the official eval has produced a score.

Do not launch broad `--tasks a b c` runs while a near-lock exists. The broad run on `csview dutree shellharden` burned attempts without shipping a submission because it let model retries replace deterministic triage.

2026-05-12 update: `zoxide` was closed by this exact procedure. The first naive patch over-anchored keyword matching and regressed to 570/577. The final patch limited basename anchoring to non-interactive plain final keywords, preserving slash-containing and interactive queries, and produced 577/577 official.

## Architecture comparison

Determinex is not architecturally similar to a Blackwell inference stack. Perplexity-style Blackwell work is about serving model inference fast: kernels, memory layout, throughput, scheduling, and GPU utilization.

Determinex is closer to a verification harness plus learning corpus:

- The model proposes edits.
- The compiler, tests, and ProgramBench eval judge the edits.
- The result is written back into a corpus so the next run starts with better priors.
- Budget and privacy layers decide when local models, cloud models, or obfuscation are allowed.

The real overlap is not GPU architecture. The real overlap is corpus flywheel engineering: both systems improve by capturing failures into reusable implementation knowledge. Determinex's advantage is deterministic verification for code tasks. Its weakness is orchestration maturity: artifacts, scoreboards, and run control must stay stricter than the models.

## Next best move

Close a structured-data anchor next (`jq` or `yj`), then move to `lz4`, `curlie`, and `fzf` for breadth.
