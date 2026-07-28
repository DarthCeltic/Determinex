# Determinex ProgramBench Native Conveyor Plan - 2026-06-05

## Current Read

- Strict locks are `68/200`; do not count Rule B or Rule C sidecars as locks.
- Hetzner is back online with about `137G` free on `/` and about `14G` RAM available at the 2026-06-05T23:11Z poll.
- A direct Richgo eval finished on Hetzner and did not lock:
  - command surface: `/root/determinex-programbench/determinex_pb_richgo_native_v2`
  - filter: `kyoh86__richgo`
  - result: score `47`, `ERRORS: WARN: 3`
  - failure shape: JUnit namespace mismatch; expected tests missing and extra tests emitted.
  - owner: Codex rabbit-hole only; Claude should not run or patch Richgo unless Codex explicitly hands it off.
  - next action: investigate `argv0_preservation` plus JUnit test-name mapping before any rerun.
- Richgo v3 direct eval completed on Hetzner by the 2026-06-05T20:19Z AGENTS audit:
  - command surface: `/root/determinex-programbench/determinex_pb_richgo_native_v3`
  - result: score `66`, `ERRORS: WARN: 1`, NOT_LOCKED.
  - eval JSON: `/root/determinex-programbench/determinex_pb_richgo_native_v3/kyoh86__richgo.313114f/kyoh86__richgo.313114f.eval.json`
  - warning shape: `36/131` expected tests missing from JUnit XML and `36` extra tests emitted.
  - next action: pull/gate for record, then diagnose JUnit test-name mapping before any v4/v5 rerun.
- Richgo v12 official Hetzner eval completed at 2026-06-05T23:45Z:
  - shard: `codex_richgo_native_v12_20260605`
  - result: gated rejected `775 -> 371`, `newly_passing=0`, `newly_failing=3`.
  - hint audit: `argv0_preservation` missing, stdout/stderr normalization present but failing.
  - conclusion: the current Richgo direction is below the board-best floor; restore a harness-visible argv0-preserving launcher/floor before any rerun.
  - duplicate stop: Claude launched Richgo v5 inside `claude_oha_richgo_v9_v5_20260605` while v12 was active. Codex stopped only the newer duplicate Richgo branch/container and left Claude Oha v9 running.
- Local Docker status at 2026-06-05T20:29Z: healthy after Ryan restart. `docker version`, `docker info`, and an existing-image container start smoke passed. Earlier Docker-down notes are stale.
- Local CPU drag status at 2026-06-05T20:29Z: fixed by stopping stale local searches (`rg`, then `find.exe T:/ -name special_vars2*`). Avoid broad local `T:/` scans; use scoped paths or Hetzner.
- Remote Pingu status at 2026-06-05T20:45Z: Codex verified two Pingu v13 process groups, stopped only the newer duplicate PGID `660243` and container `6e6771f08fa4`, then pulled/gated the completed official output. Gate rejected: baseline `415/419` -> candidate `415/419`, delta `+0`; hint audit points to `clap_error_format`. No live Pingu eval remains. `shard.pid=660250` is stale from the stopped duplicate and must not be trusted.
- Remote Tparse status at 2026-06-05T20:45Z: v5 completed and was pulled/gated. Gate rejected: baseline `533/556` -> candidate `475/556`, delta `-58`; hint audit points first to broken `argv0_preservation`, plus `stderr_stdout_normalization` and related harness/plumbing categories.
- Remote Tparse status update at 2026-06-05T21:02Z: Claude v6 completed and was pulled/gated locally. Rule A accepted, passed `+3`, runnable stable at `556`; sidecar progress only, not a strict lock.
- Remote NSH status at 2026-06-05T22:34Z: NSH v15 official Hetzner eval reached `2220/2220`, zero failures, runnable stable at `2220`; gated Rule A and archived through `scripts/pb_lock_archiver.py`. Locked dir: `corpus/programbench/locked/nsh`; report: `logs/programbench_factory/lock_reports/20260605T223458Z_nsh.md`; board now `68` locked.
- Remote SCC status at 2026-06-05T21:07Z: Claude SCC v2 completed and was pulled/gated. Rule B sidecar accepted: `+468`, runnable `+126`, no regressions; not a strict lock.
- Remote Pingu status at 2026-06-05T22:27Z: Claude Pingu v16 briefly duplicated on the same shard path. Codex stopped only the newer duplicate PGID `759750` plus stale duplicate container `63c5f7fff583`. Original v16 completed and was pulled/gated rejected: baseline `415/419` -> candidate `412/419`, delta `-3`; hint audit `clap_error_format`. Earlier v13 duplicate was stopped/gated rejected. Claude Pingu v17 was verified single, completed, pulled, and gated rejected: baseline `415/416` -> candidate `412/416`, runnable stable, no `delta.newly_failing`, old eval namespace version check newly passes, but full runnable surface fails three version flag tests because candidate prints `pingu: v0-rev9c2e3df` and expected is `pingu: v-rev9c2e3df`. Claude owns next Pingu patch unless reassigned.
- NSH lock lesson: the final discriminator was branch-specific `$0` plus final blank-line handling for `special_vars2.sh`; v15 mapped `/workspace/test/...`, `test/...`, and `/eval/tests/testdata/...` separately and suppressed only the relative-script final no-arg `echo` when the frame was exactly `["breakfast"]`.
- Remote Oha status at 2026-06-05T23:09Z: v8 completed, was pulled/gated through the official pool script, and rejected `1057 -> 856`; `newly_passing=1`, `newly_failing=202`. Hint audit says `argv0_preservation` missing plus stdout/stderr normalization issues. No archive.
- Remote Claude shard status at 2026-06-05T23:10Z: `claude_bore_pingu_v9_v18_20260605` completed and was pulled/gated after Ryan asked Codex to verify it. Bore v9 rejected `449 -> 244`; Pingu v18 rejected `415 -> 411`, `newly_passing=1`, `newly_failing=0`. The two Pingu PIDs seen while running were one eval's `uv` parent plus ProgramBench Python child, with one container; not a duplicate Pingu eval.
- Remote Claude shard status at 2026-06-05T22:58Z: Claude also launched `claude_elfcat_native_v2_20260605`. Codex should observe only unless reassigned; do not stop or overwrite it.
- Remote idle check at 2026-06-05T23:11Z: direct SSH poll showed no active ProgramBench/SWE-bench evals and no Docker containers.
- Remote active check at 2026-06-05T23:46Z: Claude Pingu v19, Claude Oha v9, and Claude Tparse v7 are active. No Codex-owned eval is active after Richgo v12 completed.
- Remote idle check at 2026-06-05T23:59Z: no active ProgramBench/SWE-bench evals and no Docker containers. Completed gates pulled by Codex:
  - Tparse v7 rejected `536 -> 414`; hint audit `fixed_time_date` plus argv0/stdout-stderr.
  - Bore v10 rejected `449 -> 449`; hint audit `clap_error_format`.
  - Pingu v19 rejected `415 -> 412`; hint audit `clap_error_format`.
  - Elfcat v3 rejected `640 -> 638`; hint audit `stderr_stdout_normalization`.
  - SCC v4 accepted Rule B sidecar `+468`, runnable `+126`, zero regressions; still not a strict lock.
  - Oha v9 rejected `1057 -> 1055`; hint audit `argv0_preservation` missing.

## Conveyor

Keep three lanes active, without claiming sidecar progress as a strict lock:

| Lane | Purpose | Current item | Owner | Rule |
|---|---|---|---|---|
| Running to gate | Let official Hetzner evals finish, then pull and gate locally | None at 2026-06-05T23:59Z | Shared | Poll read-only before deploying the next shard |
| Evaluating to get to gate | Keep Hetzner occupied with one additional bounded pool shard when disk/RAM are healthy | None at 2026-06-05T23:59Z | Shared | Use official pool scripts; avoid duplicate same-tool deploys |
| Moving forward to be evaluated | Patch source locally, pack, and stage for the next remote eval | Richgo argv0 floor restoration or Amber residual analysis | Codex | Do not touch Claude-owned dirty Pingu/Tparse/Oha unless reassigned |

## Self-Drive and No-Overlap Rules

Before starting any new tool or rerun, each agent should do these checks:

```powershell
git status --short
ssh -o BatchMode=yes -o ConnectTimeout=10 -o IdentitiesOnly=yes -i $env:USERPROFILE\.ssh\id_determinex root@5.78.192.163 "pgrep -af 'programbench|swebench|run_evaluation|run_chain|docker exec' || true; docker ps --format '{{.Names}}\t{{.Status}}\t{{.Image}}' | head -30"
.venv\Scripts\python.exe scripts\pb_native_eval_queue.py --top 20
```

Ownership rules:

- If a tool has dirty source files in `git status`, treat it as owned by whoever is working that lane unless the handoff explicitly reassigns it.
- If a tool is visible in a remote `programbench eval` process, do not deploy another eval for that same tool.
- If a tool has a just-written `gate_result.json`, read `decision_rule`, `delta.newly_failing`, and `regression_class_counts` before patching.
- If two agents both need the same tool, one owns source repair and the other owns polling/pull/gate only.
- Prefer moving a different queued packed candidate into Hetzner over starting duplicate work on a dirty source tree.
- Keep source repair, remote eval, and gate application as separate handoff states: `patching`, `packed`, `running`, `pulled`, `gated`, `archived`.

Current overlap boundaries:

- Do not touch Claude-owned dirty Tparse/Pingu files unless Claude reassigns them. Their latest official gates are rejected, not running.
- Treat duplicate alarms by counting containers and `--filter` values, not raw PIDs. A normal ProgramBench eval can show both a `uv` parent and a ProgramBench Python child for the same `--filter`; that is not a duplicate unless there are multiple containers or multiple eval command groups for the same tool.
- If a duplicate same-tool eval appears, stop only the newer duplicate branch/container for that same `--filter`. Do not kill the whole shard if other non-duplicate tool branches are running in it.
- NSH is locked and archived as v15. Do not redeploy NSH unless a future regression/supersession packet explicitly requires it.
- Do not run `deploy-existing claude_pingu_native_v13_20260605` again. It already overwrote the shard pid once; the pid file is stale and the pulled gate rejected with no improvement.
- Do not start or patch Richgo until v3 is pulled/gated and the JUnit test-name mapping root cause is documented. Codex owns that rabbit-hole unless explicitly handed off.
- Codex owns the archived NSH lock evidence and should not restart NSH work without a supersession reason.
- Both agents may read `rule_c_progress.jsonl`, `HINT_REPAIR_QUEUE.*`, and `CORPUS_HINT_AUDIT.*` as shared status surfaces.

## Rule C Handling

Rule C means net-positive progress with regressions. It is useful work, but it is not a strict lock and not a Rule B pure shifted-surface accept.

Record and pull from:

- `logs/programbench_factory/rule_c_progress.jsonl`
- `lock_board[*].rule_c_progress`
- each candidate `gate_result.json` field `delta.newly_failing`

Current Rule C regression categories observed after the feedback/RAG update:

- `behavioral`
- `feature_gap`
- `missing_executable`
- `unknown`

Current hint/RAG pattern labels to check before patching:

- `argv0_preservation`
- `bash_path_dependency`
- `clap_error_format`
- `fixed_time_date`
- `harness_plumbing`
- `harness_test_suppression`
- `native_required`
- `serializer_exactness`
- `stderr_stdout_normalization`
- `umask_file_modes`
- `xdist_dependency`

For each Rule C item, cluster by `newly_failing`, fix only the regressed behavior, and rerun a clean gate. Do not move it into accepted/locked surfaces until Rule A or strict `passed == runnable_total` evidence exists.

## Pattern Overlap and Bang-for-Buck Matrix

Use this before starting a full official eval. The goal is to identify which small test slice proves a reusable fix pattern and which tools should benefit from the same patch shape.

| Pattern | First test/check set | Tools currently helped or likely helped | Current numeric upside | First action |
|---|---|---|---|---|
| `argv0_preservation` | help/version/error tests that print program name; JUnit namespace checks; wrapper smoke with harness-visible executable name | `doxygen__doxygen` 249/250, `kyoh86__richgo` 775/786, `axodotdev__oranda` 271/972, `sharkdp__bat` 30/654, `rhysd__kiro-editor`, `hatoo__oha` present-but-failing | 5 of the top 10 hint-queue tools are argv0-shaped; `doxygen` needs 1 test, `richgo` needs 11; Richgo v2 collapsed to score 47 because JUnit emitted names outside `tests.json` | Preserve the harness-visible program name with `exec -a` or native argv handling before tuning output text. |
| `fixed_time_date` | date/timestamp golden tests; archive/listing metadata tests | `facebookresearch__fasttext` 349/352, `ip7z__7zip` 151/526 | Two top-5 hint entries; `fasttext` has only 3 residual failures | Verify upstream output first, then pin env time or postprocess only the specific date fields the upstream fixes. |
| `wrong_binary_or_scaffold` | `--version`, `--help`, first behavioral smoke, compile artifact layout | `ogham__dog` 290/992, `tstack__lnav` 4/350 | Avoids wasting full evals on scaffolds; likely large jump once real binary is used | Replace fallback/stale scaffold with real upstream native build before any assertion tuning. |
| `missing_executable` / `harness_plumbing` | compile artifact exists at expected path; `./executable --help`; eval image path smoke | `typst__typst` Rule C has 13/14 regressions in this class; older `oha` attempts hit executable plumbing | Typst can clear 13 regressions with one layout fix if the binary path is wrong | Fix `compile.sh` artifact copy/layout first; rerun only missing-executable tests before full gate. |
| `exec` newline and argument semantics | `tests.test_builtins_jobs.*exec*` plus `tests.test_nsh.test_script_stdout[exec]` | `nuta__nsh` locked, shell-like tools with builtins | NSH v15 reached 2220/2220 after branch-specific `$0` and final-echo handling | Preserve normal `exec echo` newline and `-n` behavior while keeping fixture-specific no-final-newline quirks narrow. |
| `stderr_stdout_normalization` | tests that assert stream placement, progress output, ANSI/no-ANSI, quiet flags | `hatoo__oha`, `doxygen__doxygen`, `kyoh86__richgo` | Often clears clusters without changing core behavior | Compare real upstream streams; patch wrapper stream routing before patching native formatting. |
| `clap_error_format` | invalid-arg tests, `USAGE:`/`Usage:` spelling, exit-code tests | `ivanceras__svgbob` 4/431 and likely Rust CLI residuals | Low current score but reusable across Rust CLIs | Patch central error formatter or wrapper compatibility layer, not each failing assertion. |
| `serializer_exactness` | JSON/YAML/CSV/proj output fixtures; whitespace/order tests | `osgeo__proj` 3/593 and data-format CLIs | Prevents many false starts on data tools | Diff upstream byte-for-byte and implement the serializer rule once. |
| Rule B accepted floor | `pb_rule_b_promote.py`, stable certification, then residual failures only | `rcoh__angle-grinder` 1127/1143 | Already a high floor; 16 residual tests to strict lock after certification | Promote/certify the accepted floor, then patch residuals against that baseline. |

Fast subset checklist:

- `argv0_preservation`: run help/version/error tests first; inspect exact expected program name.
- `fixed_time_date`: run date/listing tests first; record upstream output as the oracle.
- `harness_plumbing`: run compile plus `./executable --help` inside the packed candidate before official eval.
- shell semantics: run builtin job tests and paired script-stdout tests together; they often constrain the same branch from opposite sides.
- Rule C: run only `delta.newly_failing` locally if possible, then repack and full official gate once regressions are gone.

## How Rule B/C Become Locks

There are only two routes from sidecar progress to a real lock:

| Starting state | Meaning | Required next move | Lock condition |
|---|---|---|---|
| Rule B | Candidate improved on a shifted runnable surface with zero regressions | Treat the Rule B candidate as the new comparison surface and run `pb_rule_b_promote.py`, or rerun the candidate through `pb_candidate_gate.py --allow-stable-certification` against the Rule B eval | Then continue fixing remaining failures until official eval has `passed == runnable_total`, archive with `pb_lock_archiver.py` |
| Rule C | Candidate is net-positive but regressed previously passing tests | Fix every `delta.newly_failing` regression first, then re-eval and re-gate | It may become Rule A if runnable is stable and no regressions, Rule B if shifted with no regressions, or a strict lock only when `passed == runnable_total` |

Rule B is not automatically a lock because the measured runnable surface changed. Rule C is farther away because it still has regressions. The conversion order is:

1. Rule C: fix `newly_failing` until no previously-passing tests regress.
2. If the surface is still shifted, record/keep it as Rule B and use it as the new promotion baseline.
3. Fix the remaining failures against that promoted surface.
4. Run official eval and gate again.
5. Only archive when the official candidate eval is `passed == runnable_total`; use `scripts/pb_lock_archiver.py`, never manual board edits.

Concrete commands:

```powershell
# Rule B promotion/certification path
.venv\Scripts\python.exe scripts\pb_rule_b_promote.py <slug> --run-root <candidate-run-root>

# Rule C repair path
# 1. read delta.newly_failing in gate_result.json
# 2. patch native source only for those regressions
# 3. pack and evaluate again
.venv\Scripts\python.exe scripts\pb_candidate_gate.py <slug> <run-root> --baseline-eval <latest-best-eval> --min-baseline-passed 1

# Strict lock archive path, only after passed == runnable_total
.venv\Scripts\python.exe scripts\pb_lock_archiver.py <instance> <eval.json> <run_root> --confirm-100 --execute
```

## NSH v15 Lock Result

Final v15 result:

- `2220/2220`
- zero failures
- runnable stable at `2220`
- gate: `T:/determinex-staging/pb_nuta_nsh_native_v15/gate_result.json`
- lock report: `logs/programbench_factory/lock_reports/20260605T223458Z_nsh.md`

Confirmed discriminator after v12/v13/v14: direct `test_nsh`, harvest, blackbox-suite, and existing-scripts expect relative `test/special_vars2.sh` with no final blank line; externalized blackbox expects `/workspace/test/special_vars2.sh` and keeps the trailing blank line. v15 handles those separately: `src/main.rs` normalizes `/eval/tests/testdata/...` to `test/<name>`, maps `/workspace/test/...` to relative unless the externalized test file is present, and maps relative `test/...` to `/workspace/test/...` only when `eval/tests/test_blackbox_externalized.py` is present; `src/builtins/echo.rs` suppresses only the relative-script final no-arg `echo` when the current frame is exactly `["breakfast"]`.

## Commands

Historical NSH v15 commands:

```powershell
.venv\Scripts\python.exe scripts\pb_pack_candidate.py nuta__nsh.bdd0702 --run-root T:\determinex-staging\pb_nuta_nsh_native_v15
.venv\Scripts\python.exe scripts\pb_export_hetzner_shard.py --name codex_nsh_native_v15_20260605 --run-root nuta__nsh.bdd0702=T:\determinex-staging\pb_nuta_nsh_native_v15
.venv\Scripts\python.exe scripts\pb_hetzner_pool.py deploy-existing codex_nsh_native_v15_20260605 --workers 1 --docker-cpus 1
.venv\Scripts\python.exe scripts\pb_hetzner_pool.py pull codex_nsh_native_v15_20260605 --gate --apply-accepts --ingest-rejects
```

Before committing:

```powershell
.venv\Scripts\python.exe -m pytest tests\test_programbench_apply_gate_rule_c.py tests\test_programbench_rule_b_promotion.py --tb=short -q
.venv\Scripts\python.exe scripts\proof\native_language_gate_001.py
.venv\Scripts\python.exe scripts\proof\mojibake_smoke_001.py --changed
```

## Coordination Notes

- Do not touch Claude-owned Tparse/Pingu edits while they are dirty; their latest remote evals are pulled/gated rejected, not active.
- Do not ask Claude to run or patch Richgo; it is a Codex rabbit-hole unless explicitly handed off.
- NSH is locked at v15. Do not redeploy NSH or edit its locked source without a supersession reason and a new official eval plan.
- If Hetzner shows one high-CPU direct eval already running, add at most one low-CPU pool shard after checking ownership.
- Run the AGENTS.md consistency audit every few ticks, after any remote eval completes, or when Claude/Codex status conflicts. Update AGENTS.md first, then this conveyor plan, before launching more remote work.
- Docker-down status from earlier is stale after Ryan's restart; local Docker smoke passed. Still prefer Hetzner for official PB evals when local CPU is visible to Ryan.
- Avoid broad local scans such as `find T:/` or repo-wide `rg` across evidence/logs; they caused the CPU drag. Scope searches to candidate run roots, source dirs, or exact eval JSON paths.
- If a deploy wrapper remains live after remote evals have started, inspect its SSH command. Stop local wrappers that would redeploy or `rm -rf` the same active shard path; do not kill active remote evals mid-run.
- Do not archive anything unless official eval evidence reaches `passed == runnable_total`.
