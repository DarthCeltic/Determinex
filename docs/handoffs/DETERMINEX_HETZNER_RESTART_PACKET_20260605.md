# Determinex Hetzner Restart Packet - 2026-06-05

Status: `OPERATOR_OFFLINE`

Ryan intentionally powered off the Hetzner server after the paid overnight window. Until Ryan turns it back on, agents must not poll SSH, launch remote ProgramBench/SWE-bench work, or interpret SSH timeouts as a host failure.

## Last Known Remote State

- Host: `root@5.78.192.163`
- Last active run path: `/root/results_ablation_20260605_lowdisk`
- Workload: B-Uncloaked SWE-bench low-disk chunked rerun
- Last documented free disk before operator shutdown: 11 GB on `/` after exact inactive ProgramBench task-image cleanup
- Current remote run state: unknown until the server is powered back on

## Local Work While Offline

- Continue local ProgramBench repair work only.
- Do not claim official lock movement without a completed official eval where `passed == runnable_total`.
- Continue IDE Lane D Builder routing/preflight work locally.
- Keep C: in Ryan's requested 80-100 GB free band; use T: for scratch.

## First Commands After Ryan Powers Hetzner Back On

From PowerShell:

```powershell
ssh -o BatchMode=yes -o ConnectTimeout=10 -o IdentitiesOnly=yes -i $env:USERPROFILE\.ssh\id_determinex root@5.78.192.163 "date -u; hostname; df -h /; free -h; ps -eo pid,ppid,stat,etime,cmd | grep -E 'run_swebench|swebench|programbench|docker|python' | grep -v grep | head -40"
```

If SSH fails after the server is back on, use the existing AGENTS.md runbook to verify `/root`, `/root/.ssh`, and `authorized_keys` permissions. Do not set `/root` to `777`.

## Required Remote Triage Before Any Relaunch

1. Check whether `/root/results_ablation_20260605_lowdisk` exists.
2. Check whether any `swebench.harness.run_evaluation` process is still alive.
3. Check available disk on `/`.
4. If a report exists, copy it locally before any cleanup:

```powershell
scp -o IdentitiesOnly=yes -i $env:USERPROFILE\.ssh\id_determinex -r root@5.78.192.163:/root/results_ablation_20260605_lowdisk T:\determinex-staging\hetzner_returns\results_ablation_20260605_lowdisk
```

5. Only after copying results, decide whether to resume, relaunch, or mark exact blocker.

## Cleanup Policy

Allowed only when disk is critically low and only after checking active containers/images:

- Exact inactive, rebuildable ProgramBench task images with no attached containers.
- Generated SWE-bench environment images only when no active run uses them.
- Cache directories only when the active chunk has completed and results are already copied.

Never run broad `docker system prune`, never delete `/root/results_ablation_20260605_lowdisk`, never remove predictions/results/repos/locks, and never remove active SWE-bench images or containers.

## Restart Queue

1. Pull/copy the low-disk B-Uncloaked results if they exist.
2. Record exact SWE outcome or exact missing-result blocker.
3. Run only one remote heavy lane at a time:
   - first: complete SWE-bench result recovery or relaunch decision
   - second: ProgramBench candidate gates for locally repaired near-lock tools
4. Log each sample in `assurance/evidence/overnight_resource_monitor/resource_log.md`.

## Current Local Candidate Queue

Use this queue only after local repairs have focused evidence:

1. `sheepla__pingu`: version string and JUnit namespace cleanup.
2. `nuta__nsh`: whitespace/read/unset/redirection regression repair.
3. `segmentio__chamber`: reconcile current local result vs board, then gate.
4. `ekzhang__bore`: reconcile Rule B result vs board, then gate.
5. `mfridman__tparse`: use v7 baseline (`533/556`) and avoid the v5 regression path.
6. `dalance__amber`: repair gate regressions before official eval.
7. `hatoo__oha`: run only after timeout/cwd diagnosis is ready.
8. `kyoh86__richgo`: quarantine the current regressing candidate direction before more official eval time.

## Claim Boundary

This packet is an operational restart guide. It does not claim the remote run completed, does not claim SWE-bench progress, and does not claim ProgramBench lock movement.
