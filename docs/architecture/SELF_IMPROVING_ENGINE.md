---
name: self-improving-engine
description: The end-to-end autonomous, self-improving ProgramBench engine — robust eval, knowledge-grounded fix, triage/certify, the knowledge flywheel, and the prose/codebase/online absorber. Built/hardened 2026-06-29.
status: active
---

# The Self-Improving Autonomous Engine (ProgramBench)

> **Built / hardened 2026-06-29.** Realizes the operator's vision: *set Determinex any tool — it takes
> it in, gates it, finds the issue, fixes it (knowledge-grounded), proves it works, keeps the best,
> and **learns** — getting permanently smarter from its own work.* **Private by mandate:** all
> results + knowledge stay on the operator's machine + the private Hetzner box; **no git remote
> push** for results/knowledge. **Free by mandate:** the bulk knowledge ingest uses the **local
> model only** (no paid APIs).

## The loop

```
take in → GATE (robust eval) → TRIAGE (winnable / proven-ceiling / slop)
        → ROUTE (winnable → knowledge-grounded close ; ceiling → certify + drop)
        → PROVE (sound compiler/test oracle) → KEEP BEST (private capture) → LEARN (flywheel)
```

Each turn the system either closes a winnable tool, certifies an impossible one (honestly, with
proof), or surfaces NEEDS_WORK — and every verified close **teaches it a new class**, so the next
similar tool is right the first time. Driver: `scripts/determinex_pb_autodrive.py --all --watch`
(box7).

## 1. Eval robustness — "any code that hangs still gets scored"

**The hang (diagnosed via host py-spy).** PB runs each branch's pytest in Docker via the harness's
`subprocess.run(...)→communicate→select`, with **no timeout**. A test launches the CLI; for a TUI
tool the **tmux server double-forks and reparents to PID 1**, escaping pytest's process tree and
holding the inherited stdout fd, so Docker's pipe never sees EOF — the harness `select()` blocks
**forever, even after pytest exits**. `pytest --timeout-method=signal` can't kill the escaped child.
`ov` hung **15.7 min**; the dominant other class is a tool **blocking on a stdin read** (filter mode,
no input) → 5s timeout × reruns = the slow "hang".

**The fix — `scripts/determinex_subprocess_guard.py`** (a pytest11 plugin, bulk-injected into all 222
tools via `determinex_pb_inject_guard.py`), four mechanisms:
1. default `subprocess.run` stdin → `/dev/null` when no input — a filter tool gets EOF, no block;
2. default timeout + `killpg` the child group on any `communicate`/`run`/bare-`wait` exit;
3. `pytest_sessionfinish` + a per-test watchdog **kill the ESCAPERS by cmdline** (tmux + the tool
   binary) so Docker's pipe closes and the tool gets SCORED;
4. the watchdog also covers a hung manual `select`/`read`.
Lock-safe: eval containers run `OpenStdin=false`, so for a clean tool every mechanism is a no-op.

**The stall detector — `scripts/pb_eval_unified.py:run_local_eval`.** Was CPU-based: a *stuck* eval
keeps spinning tmux/tool/xdist threads above 5%, so it read "busy forever" and rode the 30-min cap.
Now **test-progress based**: the md5 of the `PYTEST_CURRENT_TEST` set across the tool's *parallel
branch containers* + the log size, **concurrency-scoped to the slug** (so a sibling eval can't mask
it) → a stuck eval is cut in **4 minutes**. `scripts/determinex_orphan_reaper.py` (`*/5` cron) reaps
reparented orphan tool binaries, including nested `python -c` probes.

## 2. Best-eval retention + private capture

- **`_persist_best`** (`determinex_pb_autodrive.py`): write `eval_report.json` only if BETTER (more
  passed / a full lock / existing missing). A flaky or memory-starved re-eval (the 0-passed
  starvation case) can **never clobber a good result**.
- **`pb_sync.py capture-scores`**: one tar+scp pulls every box `eval_report.json` +
  `autodrive_results.json` + `build_knowledge.json`, keeping the BEST per tool and **union-merging**
  the box's flywheel-learned classes into the repo.
- **`pb_capture_local.py`** + a Windows scheduled task (`DeterminexPBCapture`, every 30 min):
  capture-scores → commit **LOCAL** (no push) → **deploy `build_knowledge` down to the box** so
  box7's fixer applies the absorbed + learned knowledge. **Private** — nothing reaches a remote.

## 3. The grounded autonomous fixer — "right the first time"

The deterministic class-fixers (toolchain / build-target / deps / source-gap, in
`determinex_pb_autofix`) run first — already right-the-first-time for their classes. The catch-all
**model fixer** (`_amplify_build_fix`) used to *guess*; now `determinex_pb_amplified_fix.build_fix_prompt`
feeds the accumulated **`build_knowledge.class_patterns` + `learned_classes`** as a SYMPTOM→FIX
playbook, **relevance-ranked** to the current failures, so the model applies what the system already
knows on the first candidate. **Sound:** the next use is oracle-gated, so a rough hint can only help.

## 4. Triage → route → certify

- **`determinex_autofix.triage`** (the routing brain): `adjudicate_eval_report` + `explain` +
  `validate` → `{reopen, genuine, slop, proofs}`.
- **`drive_one` routes:** `failed>0 ∧ reopen==0 ∧ genuine>0 ∧ slop==0 ∧ proofs` → **certify** (write
  `CEILING_CERT.md` + register in `proven_ceilings.json`; the queue-order drops it); else **winnable**
  → the grounded close. **Sound — no false ceilings** (proof required; elfcat's 3 reopenable are NOT
  certified) and **reversible** (delete the registry entry).

## 5. The knowledge flywheel — the compounding engine

**`learn_class`** (`determinex_pb_amplified_fix.py`): when a fix is *oracle-verified* to improve a tool,
distill it into a generalized class — `_normalize_signature` strips tool/path/version specifics
(`requires go >= <n>.<n>.<n>`), `_fix_diff` captures the exact shell lines — into
`build_knowledge.learned_classes`. The grounded playbook then applies it first-shot on the next tool
with that symptom. Dedup by signature, bounded. **Grinding becomes compounding knowledge.**

## 6. The knowledge absorber — breadth (the bridge beyond grinding)

**`scripts/determinex_pb_absorb.py`** SEEDS the flywheel from everything the system already knows,
**free/local-model only**:
- **prose** — the corpus pattern docs, campaign milestones, playbooks, program docs, memory;
- **codebases** — build configs in the hot path + `--scan-drive` (a *bounded* `os.walk` of T:
  archive + the C:/Dev codebases incl. `.rs/.go/.c/.py` source, junk-dirs pruned, capped) writing a
  cached file list the hot path reads;
- **online** — high-value web build-knowledge (Rust cargo / Go toolchain / C++ cmake) saved as
  ERROR→FIX notes in `corpus/programbench/ingest/`, distilled by the same pipeline.
**Quality-gated:** the detect must look like a FAILURE and the fix must be ACTIONABLE (rejects
meta/strategy prose); gaming patterns excluded. **Resumable + incremental** (`absorbed_sources`),
so a long free run progresses and survives interruption. The hot path `_sources()` is **0.5s**
(non-recursive; deep source comes via the sidecar).

## Privacy & cost posture (operator mandates)

- **No git remote.** Results + knowledge stay on the operator's machine + the private box. The box
  is not a git repo and has no GitHub credentials by design.
- **No paid APIs for bulk ingest.** The absorber is local-model only unless `--allow-paid`.

## Status (2026-06-29)

- **Running:** box7 (`--all --watch`) on the full stack; the absorber ingesting drive + codebases +
  web (free, local); the 30-min private capture + box sync.
- **Proven (unit/integration):** the guard's escaper-kill (5s), the detector's progress logic, the
  triage soundness (elfcat winnable, not certified), the flywheel distill+dedup+playbook-inclusion,
  the absorber's quality gate (meta rejected, real kept). End-to-end lock conversion accumulates as
  box7 solves.

## Key modules

`determinex_subprocess_guard` · `determinex_pb_inject_guard` · `pb_eval_unified` (run_local_eval detector)
· `determinex_orphan_reaper` · `determinex_pb_autodrive` (`_persist_best`, `_triage`, `_certify_ceiling`,
`_amplify_build_fix`, `learn_class` hook) · `determinex_autofix` (`triage`) · `determinex_pb_amplified_fix`
(`learn_class`, `_build_knowledge_playbook`) · `determinex_pb_absorb` · `pb_sync` (`capture-scores`) ·
`pb_capture_local`.

Corpus: `corpus/programbench/build_knowledge.json` (`class_patterns` hand-curated + `learned_classes`
grown by the flywheel + absorber; `roadmap_to_envisioned` the self-documenting needs ledger).
