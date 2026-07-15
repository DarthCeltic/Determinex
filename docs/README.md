# Determinex Documentation Index

> The repo-level entry point is [`/README.md`](../README.md). This index organizes
> `docs/` by folder so anyone can find the right starting point without grepping.
> If a number in this index and `corpus/programbench/eval_index.json` (not shipped
> in this public export) disagree elsewhere, treat this index as a map, not ground truth.

## Ask the corpus

Two tools query Determinex's own knowledge instead of you doing it by hand.
- `python scripts/determinex_knowledge_query.py "<keywords>"` — instant, no model call, no DB.
  Searches `build_knowledge.json`'s dated findings (indexed by topic — see
  `--topics`/`--topic <NAME>`). Use this first.
- `python scripts/determinex_ask.py ask "<question>"` — routes through a local model with
  RAG/WAL/git context for actual reasoning, not just lookup. Slower (multi-minute on CPU).
  `determinex_ask.py where` is instant and gives a git+session survey with no model call.

---

## Start Here

| Doc | When to read |
|---|---|
| [`/README.md`](../README.md) | Top-level pitch + quickstart. |
| [`DETERMINEX_DEEP_AUDIT.md`](DETERMINEX_DEEP_AUDIT.md) | Full picture — what Determinex is, how it works, how it's safe/unsafe, how it teaches, capabilities. |
| [`/CHANGELOG.md`](../CHANGELOG.md) | Timeline of major changes. |
| [`papers/WHITE_PAPER.md`](papers/WHITE_PAPER.md) | The academic write-up. |
| [`papers/ARCHITECTURE.md`](papers/ARCHITECTURE.md) | High-level system architecture + origin record. |

### The correctness substrate — the engine that makes any model correct

| Doc | What it covers |
|---|---|
| [`architecture/CORRECTNESS_AMPLIFIER.md`](architecture/CORRECTNESS_AMPLIFIER.md) | Verified search + 7 pieces: any model → correct; greenfield idea → verified program. |
| [`architecture/IMPOSSIBILITY_ADJUDICATOR.md`](architecture/IMPOSSIBILITY_ADJUDICATOR.md) | No cop-out / no slop: the 4-step gate, Test Validator, the full self-correcting loop. |
| [`architecture/SYSTEM_COHERENCE_MAP.md`](architecture/SYSTEM_COHERENCE_MAP.md) | One picture of the whole system: capability → module → CLI/IDE/frontend, the transport chain. |

---

## Folder Map

| Folder | What's there |
|---|---|
| [`papers/`](papers/) | Canonical publication-grade docs: WHITE_PAPER, ARCHITECTURE, PROJECT_CLOAK, PROGRAMBENCH, BENCHMARK_EXPANSION, LICENSING. |
| [`architecture/`](architecture/) | System designs, verifier harnesses, model routing, ops stack, product foundation. |
| [`policy/`](policy/) | Governance, threat models, training/evidence/approval gates, action safety, authority boundaries. |
| [`companions/`](companions/) | Operator-facing companion essays (project memory, cloak safety, flow AI, MoA/MoE, vibe coding). |
| [`ide-frontend/`](ide-frontend/) | Tauri shell, Rust command bridge, React panels, local model wizard, IDE state contracts. |
| [`workflows/`](workflows/) | Per-surface workflow specs (Idea Lab, Learning Studio, Maintenance Bay, Repo Clinic). |
| [`release/`](release/) | Download setup, extension compatibility contract, model/third-party notices. |
| [`security/`](security/) | Security posture, scans, and hardening notes. |
| [`public/`](public/) | Documents specifically cleared for public/installer-proof consumption. |

---

## Canonical Papers (always start here)

| Doc | Purpose |
|---|---|
| [`papers/WHITE_PAPER.md`](papers/WHITE_PAPER.md) | Lead publication: compiler-verified distillation, Rosetta Stone, Hive Mind, Project Cloak, ProgramBench results, SWE-bench ablation, known-world boundaries. |
| [`papers/ARCHITECTURE.md`](papers/ARCHITECTURE.md) | Origin record + living architecture. |
| [`papers/PROJECT_CLOAK.md`](papers/PROJECT_CLOAK.md) | Cloak implementation + SWE-bench ablation status. |
| [`papers/PROGRAMBENCH.md`](papers/PROGRAMBENCH.md) | ProgramBench strategy. **0/200 legitimate locks** under the native-reimplementation methodology — prior "confirmed lock" counts were upstream source builds, invalidated by provenance audit. |
| [`papers/BENCHMARK_EXPANSION.md`](papers/BENCHMARK_EXPANSION.md) | Forward plan for HumanEval/MBPP/BigCodeBench/CodeContests/LiveCodeBench. |
| [`papers/LICENSING.md`](papers/LICENSING.md) | License + commercial-use boundary. |

---

## Where to Look By Question

Benchmark results are not product support, not release support, and not product readiness.

| Question | Look here |
|---|---|
| What is Determinex? | [`papers/WHITE_PAPER.md`](papers/WHITE_PAPER.md) |
| Why this architecture? | [`papers/ARCHITECTURE.md`](papers/ARCHITECTURE.md) |
| Why does the cloud AI never see real code? | [`papers/PROJECT_CLOAK.md`](papers/PROJECT_CLOAK.md) + [`policy/CLOAK_THREAT_MODEL.md`](policy/CLOAK_THREAT_MODEL.md) |
| How does ProgramBench scoring work? | [`papers/PROGRAMBENCH.md`](papers/PROGRAMBENCH.md) |
| What does the Tauri product shell look like? | [`ide-frontend/`](ide-frontend/) + [`workflows/`](workflows/) |
| What governance prevents bad training rows / approvals / mutations? | [`policy/`](policy/) — see the gate / guard / boundary docs |

---

## Conventions

- Benchmark results are not product support, not release support, and not product readiness.
- **Lock manifests** in `locks/sentinel/<NAME>_LOCK_001.json` are the authoritative source for any invariant a doc claims. If a doc and a lock disagree, the lock wins.
- **Companion docs** (`companions/COMPANION_*.md`) are operator-facing essays. They carry retrieval context, not proof by themselves.
- **The white paper** is the publication-grade narrative; it must match the locks, but is the slowest to update.

---

## How to Add a New Doc

1. Pick the folder by purpose — if no folder fits, ask whether the doc is actually two docs.
2. If the new doc updates a paper's headline numbers, also update the paper in the same commit.
3. Update this index in the same commit (one-line entry, link, purpose).
