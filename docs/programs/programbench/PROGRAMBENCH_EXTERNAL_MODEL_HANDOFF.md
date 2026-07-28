# ProgramBench External Model Handoff

Use this file when handing ProgramBench work to Claude/Gemini while Codex usage is conserved.

The goal is not to make external models "solve ProgramBench" by broad generation. The goal is to make them run a disciplined lock factory: one tool, one failure cluster, one official gate at a time.

## Current Truth

As of 2026-05-18:

- Board source: `logs/programbench_lock_board.csv`
- Exact row count: 200 tools
- Locked archives: 5 (`zoxide`, `ripgrep`, `htmlq`, `gping`, `ripsecrets`)
- Current near-lock lane:
  - `anordal__shellharden.6a6ffd4`: `1147/1292`, display `89/100`
  - `psampaz__go-mod-outdated.bb79367`: best `266/337`, display `79/100`, latest run regressed
  - `konradsz__igrep.aa75630`: best `516/703`, display `73/100`

Local mini-eval is useful for fast debugging, but official ProgramBench Docker eval is the only score that counts.

## Hard Rules

1. Do not run `full_sweep_iterate.py`.
2. Do not ask a model for full-file replacement of a working override.
3. Do not edit tests or fixtures unless the upstream binary proves the test is wrong.
4. Do not touch `corpus/programbench/locked/*` unless archiving an official 100.
5. Do not overwrite a best-known T-drive run. Copy to a new versioned run directory.
6. Do not mix local mini-eval deltas with official Docker deltas.
7. Keep a patch only when the official pass count improves, or label it explicitly as local-only research.
8. One work packet means one tool and one failure cluster.

## Division Of Labor

Codex should do:

- Architecture decisions.
- Final review of patches.
- Lock archive creation.
- Git commits and pushes.
- Any change to shared scripts.

Claude/Gemini should do:

- Failure inventory extraction from official eval JSON.
- Small candidate patches to existing overrides.
- Candidate packaging with `scripts/pb_pack_candidate.py`.
- Official eval runs.
- Exact before/after reports.

This keeps expensive reasoning focused on decisions and lets external models do the repetitive gate loop.

## Required Commands

Refresh the board:

```powershell
& 'C:\Users\ryang\AppData\Local\Python\pythoncore-3.11-64\python.exe' scripts\pb_score_audit.py
```

Pack an override candidate for official eval. The packer copies `compile.sh` plus
all source files in the override directory, so it supports Python, Go, Rust, and
other single-directory scaffolds:

```powershell
& 'C:\Users\ryang\AppData\Local\Python\pythoncore-3.11-64\python.exe' scripts\pb_pack_candidate.py <slug> --run-root .determinex_staging\pb_<shortname>
```

Run official eval:

```powershell
& 'C:\Users\ryang\AppData\Local\Python\pythoncore-3.11-64\python.exe' scripts\programbench_eval_runner.py <slug> .determinex_staging\pb_<shortname> --force
```

Pull a missing cleanroom image:

```powershell
docker pull programbench/<owner>_1776_<repo>.<hash>:task_cleanroom
```

Example:

```powershell
docker pull programbench/anordal_1776_shellharden.6a6ffd4:task_cleanroom
```

## Work Packet Contract

Every external-model packet must report:

- Tool slug.
- Starting official score and eval JSON path.
- Failure cluster being targeted.
- Files changed.
- Official before and after pass counts.
- Whether total runnable tests changed.
- Remaining top failure clusters.
- Any skipped/not-run behavior.

If the packet cannot run official eval, it must stop after producing a candidate patch and say why. No score claim is allowed without official eval output.

## Lane 1: Near Locks

### 1. shellharden

Tool: `anordal__shellharden.6a6ffd4`

Current source:

- `corpus/programbench/per_tool_overrides/anordal__shellharden.6a6ffd4/main.py`

Current official best:

- `T:\determinex-programbench\v39_shellharden-openai\anordal__shellharden.6a6ffd4\anordal__shellharden.6a6ffd4.eval.json`
- `1147/1292`

Known remaining clusters:

- 115 transform/syntax/suggest/highlight exactness failures.
- 12 `--check` expected-clean files returning `2` instead of `0`.
- 10 unclosed backtick/subshell syntax errors still returning `0`.

Important warning:

- A broad EOF/syntax regex patch was already rejected because it created false positives on valid shell forms such as `${#var}` and fixture files.
- Next patch must be state-aware and narrow.

Recommended first packet:

- Target only the 12 `--check` false-positive files.
- Compare their input against the current syntax detector.
- Add narrow exemptions for valid constructs, not broad "ignore syntax" logic.

### 2. go-mod-outdated

Tool: `psampaz__go-mod-outdated.bb79367`

Best-known official:

- `266/337`
- Best path from board: `T:\determinex-programbench\v18b_reorder_psampaz\psampaz__go-mod-outdated.bb79367`

Important warning:

- Latest score regressed to about `12/100`. Start from the best artifact, not latest.

First packet:

- Recover/copy the best source into `corpus/programbench/per_tool_overrides/psampaz__go-mod-outdated.bb79367/`.
- Pack and re-run official eval to confirm `266/337` is reproducible.
- Only then patch one failure cluster.

### 3. igrep

Tool: `konradsz__igrep.aa75630`

Best-known official:

- `516/703`
- Best path from board: `T:\determinex-programbench\determinex_pb_igrep_v3\konradsz__igrep.aa75630`

First packet:

- Recover/copy the best source into `corpus/programbench/per_tool_overrides/konradsz__igrep.aa75630/`.
- Re-run official eval to verify baseline.
- Patch the largest failure cluster only.

## Lane 2: Fast Mid-Tier Pushes

Work these after Lane 1 packets are moving:

| Tool | Best official | Action |
| --- | ---: | --- |
| `mookid__diffr` | `541/782` | hand-test iterate |
| `sclevine__yj` | `525/824` | recover tests/task alignment first |
| `junegunn__fzf` | `702/1212` | hand-test iterate |
| `skeema__skeema` | `825/1547` | hand-test iterate |
| `oppiliappan__eva` | `489/963` | hand-test iterate |
| `foriequal0__git-trim` | `353/710` | hand-test iterate |
| `nikoladucak__caps-log` | `530/1093` | hand-test iterate |

Do not start from scratch. Use the best run path in `logs/programbench_lock_board.csv`.

## Lane 3: Create Overrides By Recovery

For `create-override` rows with non-trivial official scores, the first job is source recovery, not generation.

Start with:

| Tool | Best official | First action |
| --- | ---: | --- |
| `ggreer__the_silver_searcher` | `46.60` | recover best source into override |
| `blacknon__hwatch` | `40.69` | recover best source into override |
| `antonmedv__walk` | `34.82` | recover best source into override |
| `ammarabouzor__tui-journal` | `34.88` | recover best source into override |
| `astaxie__bat` | `33.94` | recover best source into override |
| `canop__rhit` | `30.85` | recover best source into override |

After recovery:

1. Pack with `pb_pack_candidate.py`.
2. Run official eval.
3. Confirm the recovered override reproduces the board score.
4. Then patch one cluster.

## Prompt: Scout Packet

```text
You are Claude working in C:\Dev\Determinex.

Do not edit files.

Tool: <slug>
Best eval JSON: <path from logs/programbench_lock_board.csv>

Task:
1. Read the eval JSON and group failures by root-cause signature.
2. Identify the single highest-ROI cluster.
3. Report exact test names, assertion snippets, expected/actual shape, and likely code area.

Rules:
- No code changes.
- No fixture edits.
- Do not use local mini-eval as official score.
- Output a compact report with the next patch target.
```

## Prompt: Patch Packet

```text
You are Claude working in C:\Dev\Determinex.

Tool: <slug>
Override: corpus/programbench/per_tool_overrides/<slug>/main.py
Target cluster: <cluster from scout packet>

Task:
1. Make the smallest patch for this one cluster.
2. Do not rewrite the full file.
3. Do not touch tests or locked archives.
4. Pack with:
   & 'C:\Users\ryang\AppData\Local\Python\pythoncore-3.11-64\python.exe' scripts\pb_pack_candidate.py <slug> --run-root .determinex_staging\pb_<shortname>
5. Run official eval with:
   & 'C:\Users\ryang\AppData\Local\Python\pythoncore-3.11-64\python.exe' scripts\programbench_eval_runner.py <slug> .determinex_staging\pb_<shortname> --force

Keep the patch only if official passed count improves and runnable total is stable.

Report:
- before passed/total
- after passed/total
- score delta
- files changed
- cluster fixed or not fixed
- remaining top clusters
```

## Prompt: Recovery Packet

```text
You are Claude working in C:\Dev\Determinex.

Tool: <slug>
Best run path: <path from logs/programbench_lock_board.csv>

Task:
1. Recover the best known source into corpus/programbench/per_tool_overrides/<slug>/.
2. Preserve main.py and compile.sh exactly unless a path fix is required.
3. Pack with scripts/pb_pack_candidate.py.
4. Run official eval to confirm the recovered source reproduces the board score.

Rules:
- No behavior edits in the recovery packet.
- No full generation.
- No locked archive edits.
```

## What Gets Us To 200/200

There is no one-night sweep that gets 200 honest locks. The credible path is:

1. Keep the 5 current locks stable.
2. Push the 3 near-locks to 100 using official failure clusters.
3. Recover best-known sources for high-scoring `create-override` rows so they become normal hand-test targets.
4. Run 5-10 external-model packets in parallel, each one cluster-scoped.
5. Archive every official 100 immediately.
6. Feed every accepted patch and failure cluster back into corpus lessons/RAG.

That is the fastest path because it prevents the two things that wasted time: full-file rewrites and local-only fake deltas.
