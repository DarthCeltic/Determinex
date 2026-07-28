# ProgramBench 200/200 Lock Plan

Date: 2026-05-18

This is the reset plan after the failed full-sweep/RAG replacement run. The core decision is: **valid tests are the oracle; hand/test-guided patches are the production path.** Model output can assist, but no model-written full-file replacement is allowed to count unless it passes the same gate as hand code.

## Current Audit

- Extracted local test surfaces: 194 tools under `T:/determinex-programbench/_extracted_tests`.
- Override dirs: 175 under `corpus/programbench/per_tool_overrides`.
- Locked corpus dirs: 4 (`zoxide`, `ripsecrets`, `htmlq`, `ripgrep`).
- Action sheets: 195.
- Eval artifacts found by `scripts/pb_score_audit.py`: 195 evaluated tools, 204 total observed tool keys including local extras/locked-only entries.
- Best-known routing from eval JSON: 3 `lock-now`, 4 `push-to-lock`, 170 `hand-test-iterate`, 22 `create-override`.
- Latest-vs-best regressions: 11 tools. This confirms that latest artifact is not always the artifact to promote.
- Missing override for extracted surface: 23 tools, including `anordal__shellharden`, `burntsushi__xsv`, `facebook__zstd`, `sharkdp__bat`, `tukaani-project__xz`.
- Override but no currently extracted local surface: 4 tools (`burntsushi__ripgrep`, `jqlang__jq`, `mgdm__htmlq`, `sirwart__ripsecrets`).

The latest matrix says 195/200 evaluated, 1/200 resolved, and 3 near/almost resolved, but that Markdown is not safe as machine truth. It has parse hazards and conflicts with the corpus lock directory. Automation must consume eval JSON/TSV artifacts, not scrape the Markdown.

The generated board lives at:

- `logs/programbench_lock_board.json`
- `logs/programbench_lock_board.csv`

## What Failed

1. Full-file generation is the wrong interface for the tuned Observer-3B. It emits marker tokens and sketch diffs (`[MARKER: UPDATE_HERE]`) instead of complete runnable Python.
2. Override priming does not make the model preserve working behavior. It still rewrites/regresses.
3. The local mini-eval harness was incomplete on Windows: it patched `utils.py` and `conftest.py`, but some tests define `EXE`/`EXECUTABLE` directly inside `test_*.py`.
4. Reporting mixed matrix baseline deltas with local mini-eval deltas, which created fake wins.
5. Some target hashes were wrong (`gping`, `hyperfine`) and some high-priority tools have no override dir (`shellharden`).

## Fixes Already Applied

- `scripts/full_sweep_iterate.py`: mini-eval now patches `test_*.py` runner variables as well as `utils.py` and `conftest.py`.
- `scripts/patch_iterate.py`: rejects marker-contaminated outputs, requires target-test pass, reports `local_delta` separately from `matrix_delta`.
- `corpus/programbench/per_tool_overrides/orf__gping.26eb5b9/main.py`: hand/test-guided lift from `125/221` to `195/221` in local mini-eval.

## Non-Negotiable Lock Gate

A tool only counts as locked when all of these are true:

1. Official ProgramBench eval reaches display 100 or the accepted xdist/dependency skip equivalent.
2. Final eval JSON is archived under `corpus/programbench/locked/<tool>/eval_report.json`.
3. Winning `submission.tar.gz` and source are archived under `corpus/programbench/locked/<tool>/`.
4. The final override/scaffold is reproducible from the repo.
5. Any edited or suspect fixture is verified against the upstream binary first. No fixture edits without proof.

Partial local mini-eval improvements are useful for steering, but they do not count as locks.

## Lock Factory Workflow

For each tool:

1. Establish source of truth.
   - Locate latest official eval JSON.
   - Run local mini-eval on the current override.
   - Record official score, local score, total tests, branch count, and top failure clusters.

2. Build failure inventory.
   - Run patched local harness and collect every failing pytest node.
   - Group by exact assertion family: help golden, version, unknown flag, missing arg, file IO, format output, runtime error, parser semantics, algorithm.
   - For contradictory tests, build upstream binary and compare before changing code.

3. Patch one cluster at a time.
   - Make the smallest code change for one cluster.
   - Run local mini-eval.
   - Keep only if pass count increases and total test count is stable.
   - Revert immediately on regression.

4. Promote to official eval.
   - After local mini-eval reaches a meaningful plateau, apply override to scaffold.
   - Run official eval with one-worker guarded lane.
   - Archive logs and score.

5. Lock or continue.
   - If official reaches 100, archive lock.
   - If not, regenerate failure inventory from official eval JSON and repeat.

## Required Automation

Build or harden these scripts before scaling beyond one active tool:

1. `pb_score_audit.py`
   - Reads eval JSON/TSV, not Markdown.
   - Emits `programbench_lock_board.json` with official score, local score, override present, extracted tests present, lock status, and next action.

2. `pb_failure_inventory.py`
   - Runs the patched local mini-eval.
   - Writes all failing nodes plus source, assertion message, branch, and cluster label.

3. `pb_single_cluster_gate.py`
   - Applies a candidate patch.
   - Requires target cluster improvement, total count stability, and no regression.
   - Produces a before/after JSON row for training.

4. `pb_lock_archiver.py`
   - Copies final eval JSON, source, submission tarball, and lessons into `corpus/programbench/locked/<tool>/`.

5. `pb_upstream_oracle.py`
   - Builds/runs upstream binaries from task branches for disputed behavior.

## Target Order

### Lane A: Immediate Locks

1. `sirwart/ripsecrets`
   - Matrix says skipped-only near lock. Verify official artifact and archive if already acceptable.

2. `BurntSushi/ripgrep`
   - Matrix says 1 failure / 99.96. Verify whether current corpus lock is the latest final artifact.

3. `anordal/shellharden`
   - High official score, but no `per_tool_overrides` dir in current checkout. Recover winning source from `T:/determinex-programbench/v32_shellharden-openai` or related run and put it under override/locked structure.

### Lane B: Current Hand-Test Targets

1. `orf/gping`
   - Current local mini-eval: `195/221`.
   - Continue from exact failures: color validation, runtime error/no TTY, required host with parser flags, golden help exactness.

2. `nachoparker/dutree`
   - Local harness score diverges from matrix; first fix is harness/official alignment, not code.

3. `sharkdp/hyperfine`
   - Resource-risk lane only. Do not run high-worker evals. Needs official/local harness alignment before code changes.

4. `kyoh86/richgo`
   - Local score 0, likely runner/executable mismatch or missing Go-output behavior. Start with failure inventory, not generation.

5. `sclevine/yj`, `konradsz/igrep`, `ggreer/the_silver_searcher`, `NikolaDucak/caps-log`
   - Highest mid-tier ROI after near-locks.

### Lane C: Missing Overrides

Create first real overrides for the 23 extracted/no-override tools. Start with:

- `anordal__shellharden` (recover source first)
- `burntsushi__xsv`
- `facebook__zstd`
- `tukaani-project__xz`
- `sharkdp__bat`
- `antonmedv__walk`

These should use the same hand-test/failure-inventory flow, not broad generation.

### Lane D: Anchors

The five anchor strategy remains correct, but anchors should not block immediate locks:

1. `jq`
2. `fzf`
3. `lz4`
4. `fd`
5. `curlie`

For each anchor, first milestone is not 100%. First milestone is an upstream-faithful core that passes parser/help/version/golden basics and creates transfer lessons for siblings.

## Staffing/Compute Reality

To reach 200/200, the project needs:

- A stable official ProgramBench eval machine with Docker and no rate-limit churn.
- One guarded one-worker lane for resource-heavy tools.
- A lock board refreshed from eval JSON after every run.
- A no-regression patch gate.
- Upstream binary verification for disputed behavior.
- Human/test-guided implementation for hard logic. The 3B local model is useful for snippets and summaries, not full replacements.

## Path to 200/200

The only credible path is staged:

1. **Stabilize accounting**: one source of truth for all 200.
2. **Close near-locks**: prove the lock factory on 2-4 tools.
3. **Exploit mid-tier hand-test wins**: push 10-20 tools from 30-70% to 100 using exact assertions.
4. **Recover missing overrides**: remove zero/no-override blockers.
5. **Run anchors**: build real implementations where scaffolds plateau.
6. **Family transfer**: once an anchor locks, apply its implementation C:\Users\ryang\AppData\Local\Temp\pytest-of-ryang\pytest-135\test_key_from_file0\test_dir\target.txt to siblings.
7. **Long tail**: for compiler/database/media monsters, port upstream behavior selectively, verified by upstream binary.

This is not a one-night full sweep. It is a lock factory. The win condition is boring: exact tests, exact outputs, one cluster at a time, no fake deltas.
