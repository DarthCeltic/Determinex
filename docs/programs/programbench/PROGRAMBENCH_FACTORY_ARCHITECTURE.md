# ProgramBench Factory Architecture

Date: 2026-05-19
Status: design (Task A of factory infra packet)

This document defines how the ProgramBench lock factory operates after `255d8124`. It exists so that any LLM - Claude, Gemini, GPT, or a fine-tuned local model - can pick up a packet, do work, and produce a verifiable result without touching the load-bearing oracles (official eval JSON, locked archives, shared scripts) in unsafe ways.

The factory is **not** a code-generation pipeline. It is a **gated improvement loop** where every accepted patch has to clear the same official-eval rule: pass count must strictly improve and runnable count must stay stable. The LLM is the worker; the official Docker eval is the judge.

---

## 1. Factory objective

Produce a verifiable 100/100 for as many of the 200 ProgramBench tools as possible, with:

- **Zero edits** to upstream tests, fixtures, or eval harness.
- **Zero fixture cheating** (no tightening assertions to match buggy code).
- **Zero locked-archive corruption** (locks are append-only and read-only outside the lock-archiver).
- **Every improvement provably ratchets** - the official eval JSON before/after is preserved, and the gate refuses ties or regressions.

The factory's success metric is **count of tools with a reproducible locked archive at display 100**, not LOC of generated code, not number of patches attempted, not any local-mini-eval score.

---

## 2. Data flow

```
+----------------------+      +----------------------+
| corpus/per_tool_     |      | T:/determinex-          |
|   overrides/<slug>/  |      |   programbench/      |
|   - main.py / main.go|      |   <run>/<slug>/      |
|   - compile.sh       |      |   - source/          |
----------+-----------+      |   - submission.tar.gz|
           | pb_pack_         |   - <slug>.eval.json |
           | candidate.py     ----------+-----------+
           v                              |
+----------------------+                  | pb_score_audit.py
| .determinex_staging/    |                  v
|   pb_<short>/<slug>/ |      +----------------------+
|   - source/          |      | logs/programbench_   |
|   - submission.tar.gz|      |   lock_board.{json,  |
----------+-----------+      |     csv}             |
           |                  ----------+-----------+
           | programbench_                |
           | eval_runner.py               | pb_make_packet.py
           v                              |
+----------------------+                  |
| <slug>.eval.json     |<--- official     |
| (Docker cleanroom)   |     ProgramBench |
----------+-----------+     Docker eval  v
           |              +------------------------------+
           |              | logs/programbench_factory/   |
           |              |   <slug>/PACKET.md           |
           |              ------------------------------+
           |
           | pb_cluster_from_eval.py
           v
+--------------------------------------+
| logs/programbench_failure_inventory/ |
|   <slug>.official_cluster_report.    |
|     {json,md}                        |
----------+---------------------------+
           |
           | <LLM reads PACKET.md + cluster report,
           |  edits ONLY corpus/per_tool_overrides/<slug>/>
           v
       (back to top: pack -> eval -> gate)

When official eval reaches 100:
+----------------------+
| pb_lock_archiver.py  |   (TODO - Codex authors; not in this packet)
----------+-----------+
           v
+----------------------------------------+
| corpus/programbench/locked/<tool>/     |
|   - README.md (gping style)            |
|   - eval_report.json (verbatim copy)   |
|   - lessons.md (post-mortem)           |
|   - source/<artifacts>                 |
|   - submission.tar.gz                  |
----------------------------------------+
```

Every arrow is a single named script. There is **no implicit step** - no shell glue, no manual copying, no "just rerun this and it'll work." If an arrow doesn't exist as a script in `scripts/`, it's a TODO, not the factory.

---

## 3. Model roles

| Role | Responsibility | Allowed actions |
|---|---|---|
| **Worker LLM** (Claude/Gemini/GPT/local) | Patch one cluster, pack, run official eval, gate, report. | Edit ONLY `corpus/programbench/per_tool_overrides/<slug>/`. Run pack + runner + gate scripts. Write logs under `logs/programbench_factory/<slug>/`. |
| **Architect / Reviewer (Codex)** | Decide scope, review patches, archive locks, commit, push, edit shared scripts. | Everything. Sole authority for `corpus/programbench/locked/*` writes and any `scripts/*.py` changes. |
| **Oracle (Docker)** | Run the official eval. Return pass/fail counts and per-test JSON. | None - it is read-only ground truth. |
| **Reference upstream binary** (`cargo build --release`) | Adjudicate between contradictory tests by running the original Rust/Go binary. | None - read-only ground truth used when goldens disagree. |

The worker LLM does not pick targets, does not commit, does not edit shared infra. Its blast radius is exactly one override directory per packet. Its score claim must always cite an eval JSON path.

---

## 4. Official gate rules

A candidate patch is **accepted** if and only if all of:

1. **Official Docker eval ran to completion** for the target instance.
2. **No new infra failure** - eval JSON exists, has `test_results`, no `error_code`.
3. **Runnable total is stable** - `(passed + failed)` of the candidate equals the baseline `(passed + failed)`. A drop in runnable usually indicates a test infrastructure failure or a regression that prevents tests from being collected; either way, it's a reject.
4. **Pass count strictly increases** - candidate `passed > baseline passed`. Ties are rejects. Improvements are mandatory because the gate's purpose is to ratchet, not to coast.
5. **No newly failing test in any branch the model wasn't supposed to touch** - the gate computes the per-test diff and flags any flip from `passed` to `failure`. The gate still emits exit-code 0 if pass count strictly increases (net positive is sufficient), but it records the regression list in `gate_result.json` so the LLM/Codex can decide whether to surgically revert the offending sub-change.

A rejected candidate triggers an immediate revert - `git checkout -- corpus/programbench/per_tool_overrides/<slug>/`. The factory does not "iterate on" a rejected patch in the same packet. A new packet may follow with a narrower scope.

When the gate accepts an improvement, the LLM's job is done. **The LLM does not commit.** Codex commits.

---

## 5. How corpus / RAG is updated

Two append-only flows:

### 5.1. Failure inventories
- Every official eval (whether accepted, rejected, or just for diagnosis) writes its cluster report to `logs/programbench_failure_inventory/<slug>.official_cluster_report.{json,md}`.
- These files are RAG-indexable by `scripts/seed_knowledge_base.py --reseed-programbench` (already wired). The corpus index uses the markdown form for retrieval and the JSON form for structured lookups.
- The cluster report is **regenerated**, not appended - it always reflects the latest eval JSON for that slug.

### 5.2. Lock-archive lessons
- When a tool reaches official display 100, Codex (not the worker) runs `pb_lock_archiver.py` (TODO). The archiver:
  - Copies `submission.tar.gz`, `source/`, and `<slug>.eval.json` into `corpus/programbench/locked/<short>/`.
  - Authors `README.md` (in gping style) and `lessons.md` (post-mortem of the closing sequence) from worker-emitted artifacts.
  - Adds a `cluster_transfer.md` if patterns are reusable across cluster siblings (see existing zoxide/htmlq/ripsecrets `lessons.md` for the format).
- The archive is the canonical record. Every future worker that ingests RAG sees the lessons immediately.

### 5.3. Rejected patches
- A rejected patch's `gate_result.json` is preserved under `.determinex_staging/pb_<short>/gate_result.json` for the duration of the staging dir. Once the LLM emits its packet report and Codex reviews, Codex may move the gate JSON into `logs/programbench_factory/<slug>/rejected/<timestamp>.json` for permanent retention.
- Rejected-patch records contribute to the RAG corpus as "what didn't work" lessons. The format includes: what was changed, what the gate rejected on, and (where computed) which sub-change caused the regression.

---

## 6. How rejected patches are recorded

Every gate run writes `gate_result.json` with this shape:

```json
{
  "slug": "owner__repo.hash",
  "baseline": {
    "passed": 516,
    "failed": 187,
    "skipped": 1,
    "runnable": 703,
    "total": 704,
    "eval_path": "T:/.../konradsz__igrep.aa75630.eval.json"
  },
  "candidate": {
    "passed": 519,
    "failed": 184,
    "skipped": 1,
    "runnable": 703,
    "total": 704,
    "eval_path": ".determinex_staging/pb_igrep_c4/.../konradsz__igrep.aa75630.eval.json",
    "executable_hash": "10ae9420fa6a4546"
  },
  "delta": {
    "passed": +3,
    "runnable": 0,
    "newly_passing": ["test_a", "test_b", "test_c"],
    "newly_failing": ["test_d"]
  },
  "decision": "accept",   // or "reject"
  "reason": "passed +3, runnable stable",
  "exit_code": 0
}
```

For a reject, `decision: "reject"` and `reason` cites which rule failed (e.g. `"passed delta = 0 (tie); rule 4 requires strict improvement"`). The exit code is `1` for tie/regression and `2` for eval infra errors. The LLM uses the exit code to decide whether to surgically revert and stop, or escalate to Codex.

The rejected `gate_result.json` is the durable record. The worker's packet report cites it.

---

## 7. Why this is benchmark-valid and not fixture cheating

The factory is bound by five mechanical guarantees that make every accepted lock honest:

1. **Tests and fixtures are immutable.** Worker LLMs cannot edit any file under `T:/Dev/ProgramBench/`, any `eval/tests/*`, any `tests/*`, or any task `.bash` / golden file. The only writable path is `corpus/programbench/per_tool_overrides/<slug>/`.

2. **The oracle is Docker, not the worker.** Every score is produced by `programbench eval` inside a cleanroom container (`programbench/<owner>_1776_<repo>.<hash>:task_cleanroom`). The worker has zero ability to alter the eval harness, the runtime image, or the test runner. The eval JSON is whatever Docker writes.

3. **Score claims must cite the eval JSON path.** No packet can claim a score from a local mini-eval, from a partial run, from a cache hit lookup, or from a model's self-assessment. Every numeric claim in every report links to `<staging>/<slug>/<slug>.eval.json`. If the path doesn't exist or the JSON doesn't match the claim, the claim is invalid.

4. **The gate is strict and pre-defined.** Section 4 lists the acceptance rule. The gate script is the single point of decision. A worker cannot argue past it. A reviewer cannot lower the bar without modifying the shared script (which only Codex can do, and which would be visible in `git log`).

5. **Upstream binary is the tie-breaker, not the worker's judgement.** When two tests disagree, the factory builds the upstream tool from source (`cargo build --release` against any task branch's source tarball) and runs it against the contradictory fixtures. Whatever the real upstream binary does is what our code must do. The htmlq lock locked using this exact procedure - see `corpus/programbench/locked/htmlq/lessons.md` for the canonical example.

A fixture-cheating attempt would surface as: a `corpus/programbench/per_tool_overrides/<slug>/test_*.py` file (forbidden path), a packet report claiming a score without an eval JSON path, or a gate result where `runnable` dropped. The factory rejects all three mechanically.

The 5 existing locks (`zoxide`, `ripgrep`, `htmlq`, `ripsecrets`, `gping`) were produced under earlier, less formalized variants of this loop. The factory formalizes what already worked and removes the ad-hoc gluing that produced the failed full-sweep run.

---

## 8. How this becomes model-agnostic

Every interface the worker touches is **a file path** or **a shell-callable script** - no model-specific APIs, no LLM-vendor SDKs, no embedded prompts.

- A worker invocation is fully specified by a `PACKET.md` (Section 9, Task D). The packet contains paths, commands, gate rules, allowed scope. A bash agent could execute the packet. A human could execute the packet. A different LLM family could execute the packet.
- Worker output is also files: edited `main.py`/`main.go`/`compile.sh`, a packet report at `logs/programbench_factory/<slug>/REPORT.md`, the gate result at `.determinex_staging/pb_<short>/gate_result.json`.
- Worker context can be a hand-curated set of files (cluster report + lessons of cluster siblings + the override source). RAG-augmented workers can pull from the corpus index. Lightweight workers can run on just the cluster report.

When a new model joins (e.g. Gemini 3.1 Pro, fine-tuned local), no factory change is required. The model reads the same `PACKET.md`, runs the same scripts, gets gated by the same rule. The factory is the contract; the model is a worker.

---

## 9. Packet contract (worker-facing)

`pb_make_packet.py <slug>` writes `logs/programbench_factory/<slug>/PACKET.md`. The packet must include - verbatim, no narrative - the worker-actionable artifacts:

- **Slug + current official score** (cited from board JSON).
- **Source override path** - the directory the worker may edit.
- **Baseline eval JSON path** - for gate comparison.
- **Latest cluster report path** - if present; else a note that the worker should run `pb_cluster_from_eval.py` first.
- **Allowed scope** - single-cluster targeted, one tool, no test edits.
- **Forbidden actions** - locks, shared scripts, fixtures, full-file rewrites.
- **Pack command** - exact PowerShell invocation.
- **Eval command** - exact runner invocation.
- **Report format** - link to the worker-report template (TODO if not yet authored).
- **Keep/revert rule** - strict improvement + stable runnable.

This packet is the **only** instruction a worker needs. Everything else (taste, style, model-specific quirks) is encapsulated outside the factory.

---

## 10. Open work

The architecture is fully designed in this document, but only the following pieces exist as shipped code:

| Component | Status |
|---|---|
| `pb_score_audit.py` (board generator) | exists (commit `7853d1b0`) |
| `pb_pack_candidate.py` (candidate packer) | exists, multi-language (commit `2d4cb823`) |
| `programbench_eval_runner.py` (official eval wrapper) | exists with Windows fixes (commit `2d4cb823`) |
| `pb_cluster_from_eval.py` (Task B of this packet) | **new in this packet** |
| `pb_candidate_gate.py` (Task C of this packet) | **new in this packet** |
| `pb_make_packet.py` (Task D of this packet) | **new in this packet** |
| `pb_lock_archiver.py` (lock promotion) | **TODO** - Codex authors |
| `pb_upstream_oracle.py` (upstream binary build) | **TODO** - Codex authors |
| Worker REPORT.md template | **TODO** - author after first end-to-end packet |
| RAG ingestion of factory artifacts | partially wired (`seed_knowledge_base.py --reseed-programbench`); need to add `logs/programbench_factory/*` indexer |
| CI gate on `corpus/programbench/locked/*` (read-only enforcement) | **TODO** - repo policy hook |

These TODOs do not block the factory from operating on a tool - they harden the long-run invariants. Section 4's gate rule is satisfied by the scripts shipped in this packet.

---

## 11. References

- `docs/PROGRAMBENCH_EXTERNAL_MODEL_HANDOFF.md` - operational runbook for worker LLMs.
- `docs/PROGRAMBENCH_200_LOCK_PLAN.md` - strategic plan and constraints.
- `corpus/programbench/locked/htmlq/lessons.md` - exemplary lock post-mortem; reference for the "build the upstream binary" rule.
- `logs/programbench_lock_board.{json,csv}` - current state of every tool.
- `logs/programbench_failure_inventory/` - per-tool cluster reports (RAG-indexed).
