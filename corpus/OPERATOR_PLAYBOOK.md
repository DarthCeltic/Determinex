---
name: mass-run-operator-playbook
description: "If X then Y" reference card for the operator running the mass bench attempt. Covers every common failure mode + the recovery action. Read this before starting; keep it open during the run.
type: operator-playbook
---

# Determinex Mass-Run Operator Playbook

> **Purpose.** When something breaks during a 25-55 hour mass run, you don't have time to think — you need a lookup table. This is that table.

---

## VRAM realities — pick the right model FIRST

**Hardware**: GTX 1660 Ti, 6 GB VRAM. Models that actually fit:

| Model | Disk | VRAM (loaded + 8K ctx) | Verdict on 6GB |
|-------|------|------------------------|----------------|
| qwen2.5-coder:32b-instruct-q4_K_M | 19.9 GB | ~21 GB | ❌ Massive CPU spill, 50× slower. Don't use. |
| qwen2.5-coder:14b-instruct-q4_K_M | 9.0 GB | ~9.8 GB | ⚠️ Spills to RAM ~3 GB. 5-10× slower. Avoid. |
| determinex-sentinel-v5-dsl | 7.7 GB | ~8.4 GB | ⚠️ Spills slightly. Tolerable but slow. |
| **qwen2.5-coder:7b-instruct** | 4.7 GB | ~5.1 GB | ✅ **Fits, sweet spot for 6GB cards.** Borderline at >16K ctx. |
| **determinex-observer-v6-dsl** | 3.3 GB | ~3.8 GB | ✅ Architect role pick. Fast and fits. |
| qwen2.5-coder:3b-instruct | 1.9 GB | ~2.3 GB | ✅ Plenty of headroom. Quality drop vs 7b. |
| **determinex-engineer-v11-dsl** | 1.6 GB | ~2.0 GB | ✅ Determinex's fine-tuned 1.5b. Surprisingly strong. |

**Auto-pick the right model:**
```bash
python scripts/vram_monitor.py --recommend
# → echoes the largest model that fits your current free VRAM
```

**Watch VRAM during the run** (separate terminal):
```bash
python scripts/vram_monitor.py --watch 30
# Updates every 30s; alerts on warn (>=90%) or alarm (>=95%)
```

**Recommended config for 6GB VRAM:**
- PB agent: `--model local --local-model qwen2.5-coder:7b-instruct` (or omit to default to 14b → too big)
- SWE-bench: `--config a` (no `--local-builder-14b` override; uses 7b builder + 3b architect)

**If 14b/32b is desired:** close ALL other GPU apps (browser, OBS, etc.) first. Run `vram_monitor.py --watch 5` aggressively. Be ready to kill the run if alarm triggers.

---

## Pre-launch sanity

```bash
python scripts/preflight_mass_run.py
# Must exit 0 (all green) before kicking off.
# Exit code 1 = blocker. Exit 2 = warnings — proceed with caution.
```

If preflight reports **rag.programbench_chunks < 7000** or **rag.swebench_chunks < 900**:
```bash
python scripts/seed_knowledge_base.py --reseed-programbench --reseed-swebench
```

If preflight reports **agents.local_builder_flag = WARN** for PB:
- That's only an issue if you intend to run local-only. For local: `--model local` on PB agent.
- Default `--model anthropic` will hit the API.

---

## Launch commands (canonical)

### Smoke 1a — 4-tool validation gate (~30-60 min, ~$0 local / ~$8 Sonnet)

```bash
# LOCAL (no outside calls):
python scripts/determinex_programbench_agent.py --workers 2 \
  --run-name mass_run_v1_smoke \
  --model local \
  --tasks psampaz__go-mod-outdated.bb79367 \
          rbakbashev__elfcat.52f8cc7 \
          agourlay__zip-password-finder.704700d \
          sstadick__hck.b66c751
```

If 3+ lock → proceed. If <2 → **STOP and debug method** before the full run.

### Full PB mass run (115 in-scope residuals + 5 anchors + 14 hand-polished)

```bash
python -c "
import json
audit = json.load(open('corpus/programbench/_strategy/_residual_audit.json'))
inscope = [t['instance_id'] for t in audit['residual'] if t['ceiling']>=50 and t['instance_id']]
print(' '.join(inscope))
" | xargs python scripts/determinex_programbench_agent.py \
    --model local --workers 4 --run-name mass_run_v1 --tasks
```

### SWE-bench Verified (500 instances, the headline target)

```bash
python scripts/determinex_swebench_run.py \
  --config a --local-builder-14b \
  --split verified --workers 4 \
  --name mass-run-verified \
  --note "First mass run with empirical-spec injection from corpus/swebench"
```

### Multi-SWE-bench (1,632 instances across 8 languages)

```bash
python scripts/determinex_swebench_run.py \
  --config a --local-builder-14b \
  --split multiswe --workers 4 \
  --name mass-run-multiswe
```

### Live monitoring (split into 4 separate terminals — recommended setup)

```bash
# Terminal 1 — scoreboard (updates every 30s)
python scripts/mass_run_aggregate.py --watch 30

# Terminal 2 — VRAM watch (alerts on OOM risk)
python scripts/vram_monitor.py --watch 30 --alert-on warn

# Terminal 3 — health monitor (stalled containers, disk, failure streaks, ollama daemon)
python scripts/health_monitor.py --watch 60

# Terminal 4 — OBS-friendly text overlay (writes to file, low-noise)
python scripts/live_scorecard.py --refresh 5
```

The 4-terminal layout gives you the full picture: progress, VRAM headroom, run health, and a clean overlay for the recording.

---

## "If X then Y" failure-recovery table

### Resource problems

| Symptom | Diagnosis | Action |
|---------|-----------|--------|
| `Cannot allocate memory` from Docker | RAM exhausted | `docker stop $(docker ps -q)`, restart with `--workers 2` |
| `no space left on device` | C: drive full | `docker system prune -af` (frees pulled-but-unused images), pause until freed |
| Ollama OOMs / 14b model fails to load | VRAM exhausted | Switch to 7b: `--config a` (no `--local-builder-14b` override) — confirm with `vram_monitor.py --recommend` |
| `vram_monitor.py` says ALARM (≥95%) | Other GPU app eating VRAM | Close browser/OBS/Steam/etc. Restart Ollama: `ollama stop && ollama serve` |
| Health monitor reports failure-streak ≥8 | Likely scaffold bug, not bad luck | STOP run. Inspect last 3 failed eval logs; fix root cause; restart with `--tasks <remaining>` |
| Health monitor reports stalled container | Build deadlocked | `docker rm -f <name>`; agent retries; if same tool stalls 3x mark as "skip" |
| Disk fill rate >20 GB/hr warning | Image pulls outpacing prune | `docker image prune -f` mid-run is safe (only removes orphans) |
| Docker container hung at compile | Container deadlock | `docker rm -f <container_id>`; agent will retry the task |
| Whole machine freezing | Too many parallel workers | Drop `--workers` from 4 to 2 |

### Build-cycle problems

| Symptom | Diagnosis | Action |
|---------|-----------|--------|
| Same tool fails 5+ retries | Spec inadequate or tool genuinely too hard | Mark as "skip", continue with rest |
| Many tools all fail with same error class | Common bug in scaffold/spec template | Pause run, fix template, restart with `--tasks` filtered to remaining |
| Builder produces empty output | Local model context exceeded | Switch to smaller model OR shorten spec injection (`max_spec_chars=8000`) |
| Builder produces unparseable output | Model can't follow XML format | Check format-fix retry logic in agent; may need `temperature=0.05` |
| Eval times out | Compile.sh runs forever | Check tool's compile.sh — likely `cargo build` cold cache; add `--release` cache hint |

### RAG / spec-injection problems

| Symptom | Diagnosis | Action |
|---------|-----------|--------|
| `swebench_spec_lookup` returns empty for known instance | Index out of date | Re-run `c:/tmp/swebench_index.py` to rebuild |
| RAG queries return programbench specs for SWE-bench tasks | Collection collision | Filter by metadata prefix in queries |
| Spec injection makes prompt >32k tokens | Spec too large for local model | Lower `LOCAL_NUM_PREDICT` or use `inject_block_for(iid, max_spec_chars=8000)` |

### Eval-harness problems

| Symptom | Diagnosis | Action |
|---------|-----------|--------|
| `programbench eval` reports 0 tests for some tools | HF cache stale | `python c:/tmp/batch_hf_pull_v2.py` to re-pull |
| SWE-bench harness fails to find Docker image | Image not pulled | Pre-pull: `docker pull princeton-nlp/swe-bench:latest` |
| Test results inconsistent between runs | Flaky test | Re-run that single instance 2-3 times; if still inconsistent, mark "infra issue" not "method failure" |

### Recording-related problems

| Symptom | Action |
|---------|--------|
| Need to pause for break | `docker pause $(docker ps -q)` then `docker unpause $(docker ps -q)` later |
| Want to skip a tool live on camera | Ctrl-C the agent; restart with `--tasks <remaining>` |
| Want to show a specific spec on camera | `cat corpus/programbench/in_progress/<iid>/06_behavioral_spec.md \| less` |
| Want to show the live scoreboard | `python scripts/mass_run_aggregate.py --watch 5` (smaller refresh interval for camera) |

---

## "Don't do this" anti-patterns

1. **Don't kill a running build with `docker rm -f`** if it's actively writing test results. Wait for the test step or use `Ctrl-C` on the agent (graceful shutdown).
2. **Don't edit a spec file mid-run.** The agent caches specs at instance load. Restart the agent if you need a spec change.
3. **Don't `git pull` mid-run.** Could change the spec format or break helper scripts. Lock the branch for the duration.
4. **Don't enable Cloak (`--cloak`) for the recorded local run** unless you specifically want the privacy-sovereignty story on camera. Cloak adds 3-8% latency per call and is unnecessary for local-only runs (no privacy concern).
5. **Don't try to skip the smoke gate.** A 30-min smoke catches issues that would burn 25 hours otherwise.

---

## Recovery from full crash mid-run

If everything dies (machine reboot, power outage, etc.):

1. `python scripts/preflight_mass_run.py` — confirm RAG + corpus survived
2. Check what was already done: `python scripts/mass_run_aggregate.py` — locks counted from disk
3. Identify what's left:
   ```bash
   # PB residuals not yet attempted:
   python -c "
   import json, os
   audit = json.load(open('corpus/programbench/_strategy/_residual_audit.json'))
   done = set(os.listdir('T:/determinex-programbench/mass_run_v1') if os.path.isdir('T:/determinex-programbench/mass_run_v1') else [])
   remaining = [t['instance_id'] for t in audit['residual'] if t.get('instance_id') not in done and t['ceiling']>=50]
   print(' '.join(remaining))
   " | xargs python scripts/determinex_programbench_agent.py --model local --workers 4 --run-name mass_run_v1 --tasks
   ```
4. SWE-bench: `--instance-ids "iid1,iid2,..."` to resume only the unrun ones.

---

## What the operator does NOT need to do

- Manually clean up Docker containers — they auto-rm with `--rm` flag in agent
- Delete cache files mid-run — only at session end
- Refresh RAG between tools — RAG is read-only during run
- Switch builder models per tool — flag is set at run-launch time

---

## Final-night checklist (pre-recording)

- [ ] preflight green
- [ ] Docker pruned, ≥150GB free on C:
- [ ] Ollama responding, 14b model loaded
- [ ] `mass_run_aggregate.py` runs cleanly (even if 0 results)
- [ ] Disk monitor in second terminal: `watch -n 5 df -h /c /t`
- [ ] OBS or screen recorder armed
- [ ] Audio narration script open in third pane
- [ ] Smoke gate passed (3+ of 4 Tier-1a locks)

When all green: launch the full run.

---

*Determinex · Lunarian Data Systems · 2026-05-09*
