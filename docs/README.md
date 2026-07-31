# Determinex Documentation Index

> The repo-level entry point is [`/README.md`](../README.md). This index organizes the
> **555 Markdown files** in `docs/` by folder so anyone can find the right starting point
> without grepping.
> **Last refreshed**: 2026-06-30 — corrected file count (was stale at "1,865"); pointed at the
> new local knowledge-query tooling built this session (see "Ask the corpus" below); and
> corrected the ProgramBench headline to **0/200 legitimate locks** after a full provenance
> audit found the prior "67 official locks / 33.5%" claim counted upstream source builds, not
> reimplementations — see `docs/papers/PROGRAMBENCH.md`'s correction banner for evidence.
> If a number in this index and a number in `corpus/programbench/eval_index.json` /
> `verified_locks.json` disagree, the corpus JSON wins — this index is a map, not the truth.
>
> **Last reorganized**: 2026-05-29 — flat `docs/` (366 files) → 11 typed folders.

## Ask the corpus (added 2026-06-30)

Before grepping: two tools query Determinex's own knowledge instead of you doing it by hand.
- `python scripts/determinex_knowledge_query.py "<keywords>"` — instant, no model call, no DB.
  Searches `build_knowledge.json`'s 72 dated findings (indexed by topic — see
  `--topics`/`--topic <NAME>`) plus live PB status (`--status`). Use this first.
- `python scripts/determinex_ask.py ask "<question>"` — routes through the local 7B model with
  RAG/WAL/git context for actual reasoning, not just lookup. Slower (multi-minute on CPU).
  `determinex_ask.py where` is instant and gives a git+session survey with no model call.
- `determinex_rag_index.py` (needs Postgres, never provisioned) and `determinex_code_rag.py`
  (needs a symbol index, never built) exist in `scripts/` but do not currently work —
  don't reach for them until one is actually wired up.

---

## Start Here

| Doc | When to read |
|---|---|
| [`/README.md`](../README.md) | Top-level pitch + quickstart. |
| [`/PROJECT.md`](../PROJECT.md) | Shared project contract for all agents and IDE memory surfaces. |
| [`DETERMINEX_DEEP_AUDIT.md`](DETERMINEX_DEEP_AUDIT.md) | **Start here for the full picture** — what Determinex is, how it works, how it's safe/unsafe, how it teaches, capabilities. Grounded end-to-end (2026-06-14). |
| [`/CLAUDE.md`](../CLAUDE.md) | Operator directive — what the system is, current focus, role assignments. |
| [`/CHANGELOG.md`](../CHANGELOG.md) | Sentinel-lock-grouped timeline of major changes. |
| [`papers/WHITE_PAPER.md`](papers/WHITE_PAPER.md) | The academic write-up. **Current as of 2026-06-14.** |
| [`papers/ARCHITECTURE.md`](papers/ARCHITECTURE.md) | High-level system architecture + origin record. **Current as of 2026-06-14.** |

### The correctness substrate (2026-06) — the engine that makes any model correct

| Doc | What it covers |
|---|---|
| [`architecture/CORRECTNESS_AMPLIFIER.md`](architecture/CORRECTNESS_AMPLIFIER.md) | Verified search + 7 pieces: any model → correct; greenfield idea → verified program. |
| [`architecture/IMPOSSIBILITY_ADJUDICATOR.md`](architecture/IMPOSSIBILITY_ADJUDICATOR.md) | No cop-out / no slop: the 4-step gate, Test Validator, the full self-correcting loop. |
| [`architecture/SYSTEM_COHERENCE_MAP.md`](architecture/SYSTEM_COHERENCE_MAP.md) | One picture of the whole system: capability → module → CLI/IDE/frontend, the transport chain, the heir-to-VS-Code path. |

---

## Folder Map

Benchmark results are not product support, not release support, and not product readiness.
| Folder | Files | What's there |
|---|---:|---|
| [`papers/`](papers/) | 7 | **Canonical publication-grade docs.** Updated each rev. WHITE_PAPER, ARCHITECTURE, PROJECT_CLOAK, PROGRAMBENCH, BENCHMARK_EXPANSION, DETERMINEX_NODE, LICENSING. |
| [`architecture/`](architecture/) | 28 | System designs, verifier harnesses, model routing, ops stack, unified product foundation, Cathedral Index spec. |
| [`policy/`](policy/) | 27 | Governance, threat models, training/evidence/approval gates, action safety, authority boundaries. |
| [`companions/`](companions/) | 5 | Operator-facing and project-memory companion essays (project memory, cloak safety, flow AI, MoA/MoE, vibe coding). Skill-load files. |
| [`programs/programbench/`](programs/programbench/) | 55 | ProgramBench campaign: board status snapshots, factory architecture, operator apparatus, batch state, fix queues, audits. |
| [`programs/universal-100/`](programs/universal-100/) | 102 | Universal 100 product capability matrix campaign (started 2026-05-27): sector conveyor, support map, gap closures, matrix probes, gulp batches, React bindings. |
| [`programs/swebench/`](programs/swebench/) | 0 | (Reserved; SWE-bench narrative still lives in `papers/PROJECT_CLOAK.md` + `papers/WHITE_PAPER.md`. Move-in pending.) |
| [`ide-frontend/`](ide-frontend/) | 77 | Tauri shell, Rust command bridge, React panels (Idea Lab / Learning Studio / Maintenance Bay / Repo Clinic / Proof Operator Center), local model wizard, IDE state contracts. |
| [`proof/`](proof/) | 35 | Verifier traces, real-model admission/health/diagnose, evidence ledger, source-mutation/rollback flows, proof-source registry. |
| [`workflows/`](workflows/) | 10 | Per-surface workflow specs and splash-demo specs (Idea Lab, Learning Studio, Maintenance Bay, Repo Clinic, unified product UX). |
| [`handoffs/`](handoffs/) | 66 | Cross-session handoffs, Codex/Claude tandem reconciliations, Antigravity handoff, splash-path reconciliation, and 2026-06-02 known-world final-gate/all-gap Batch 003 plans and final report. |
| [`audits/`](audits/) | 13 | All audit reports — docs audit, folder audit, capability audit, cathedral release path, IDE tech debt, security monitor roadmap, recent-work log. |
| [`_audit/`](_audit/) | 3 | Pre-existing drive inventory + reference map. |

---

## Canonical Papers (always start here)

| Doc | Last rev | Purpose |
|---|---|---|
| [`papers/WHITE_PAPER.md`](papers/WHITE_PAPER.md) | 2026-06-03 | Lead publication: compiler-verified distillation, Rosetta Stone, Hive Mind, Project Cloak, ProgramBench results, SWE-bench ablation, Batch 004 claim-safe support-accounting, and known-world boundaries. |
| [`papers/ARCHITECTURE.md`](papers/ARCHITECTURE.md) | 2026-06-03 | Origin record + living architecture. Origin Apr 9-12 unchanged; appended updates cover repair locks, ProgramBench factory, SWE-bench ablation, Universal 100, Tauri shell, Cathedral Index, governance layers, known-world exact blockers, and Batch 004 lock expansion. |
| [`papers/PROJECT_CLOAK.md`](papers/PROJECT_CLOAK.md) | 2026-05-29 | Cloak implementation + SWE-bench ablation status. B-Uncloaked 14.0 %; lower-bound configs pending larger-disk rerun. |
| [`papers/PROGRAMBENCH.md`](papers/PROGRAMBENCH.md) | 2026-06-30 (corrected) | ProgramBench strategy. **0/200 legitimate locks** — prior "confirmed lock" counts were upstream source builds, invalidated 2026-06-30 by provenance audit; 62 archives retained as Native Reimplementation Loop reference corpus; eval_index.json is canonical board. |
| [`papers/BENCHMARK_EXPANSION.md`](papers/BENCHMARK_EXPANSION.md) | 2026-05-18 | Forward plan for HumanEval/MBPP/BigCodeBench/CodeContests/LiveCodeBench. |
| [`papers/DETERMINEX_NODE.md`](papers/DETERMINEX_NODE.md) | 2026-05-18 | Long-range strategy. |
| [`papers/LICENSING.md`](papers/LICENSING.md) | current | License + commercial-use boundary. |

---

## Where to Look By Question

Benchmark results are not product support, not release support, and not product readiness.
| Question | Look here |
|---|---|
| What is Determinex? | [`papers/WHITE_PAPER.md`](papers/WHITE_PAPER.md) |
| Why this architecture? | [`papers/ARCHITECTURE.md`](papers/ARCHITECTURE.md) |
| Why does the cloud AI never see real code? | [`papers/PROJECT_CLOAK.md`](papers/PROJECT_CLOAK.md) + [`policy/CLOAK_THREAT_MODEL.md`](policy/CLOAK_THREAT_MODEL.md) |
| How many ProgramBench tools have been locked? | [`papers/PROGRAMBENCH.md`](papers/PROGRAMBENCH.md) + [`../corpus/programbench/README.md`](../corpus/programbench/README.md) (filesystem-of-record status board) |
| What's the Universal 100 campaign? | [`programs/universal-100/`](programs/universal-100/) — start at the sector coverage scoreboard binding |
| What does the Tauri product shell look like? | [`ide-frontend/DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_FINAL_STATE.md`](ide-frontend/DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_FINAL_STATE.md) + [`workflows/`](workflows/) |
| What governance prevents bad training rows / approvals / mutations? | [`policy/`](policy/) — see the gate / guard / boundary docs |
| What evidence backs a specific claim? | [`proof/EVIDENCE_INDEX.md`](proof/EVIDENCE_INDEX.md) + [`assurance/evidence/`](../assurance/evidence/) |
| Latest audit report? | [`audits/DETERMINEX_FULL_CATHEDRAL_RELEASE_PATH_AUDIT_20260529.md`](audits/DETERMINEX_FULL_CATHEDRAL_RELEASE_PATH_AUDIT_20260529.md) |
| Where do session-to-session handoffs live? | [`handoffs/`](handoffs/) |

---

## Conventions

- Benchmark results are not product support, not release support, and not product readiness.
- **Lock manifests** in `locks/sentinel/<NAME>_LOCK_001.json` are the authoritative source for any invariant a doc claims. If a doc and a lock disagree, the lock wins.
- **Status boards** (e.g. `programs/programbench/PROGRAMBENCH_BOARD_STATUS_*.md`) are dated snapshots; the latest one supersedes earlier copies.
- **Companion docs** (`companions/COMPANION_*.md`) are operator-facing and project-memory essays. They carry retrieval context, not proof by themselves.
- **The white paper** is the publication-grade narrative; it must match the locks, but is the slowest of the three (paper / architecture / locks) to update.
- **Universal 100 docs** under `programs/universal-100/` form a *product-surface* ledger, not a benchmark. Locks there describe board updates, not validated capability claims unless the audit doc says so.

---

## How to Add a New Doc

1. Pick the folder by purpose — if no folder fits, ask whether the doc is actually two docs.
2. If the new doc updates a paper's headline numbers, also update the paper in the same commit.
3. Update this index in the same commit (one-line entry, link, purpose).
4. Sentinel locks come last and only for invariants that should not silently change.

---

*Last full reorganization: 2026-05-29. If you add or remove a doc, update this index in the same commit.*
