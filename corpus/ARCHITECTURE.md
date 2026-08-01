---
name: corpus-architecture
description: Authoritative architecture diagram of the Determinex corpus + oracle/compiler pipeline. Master documents → per-node specs → RAG → builder/architect/oracle.
type: architecture
---

# Corpus + Oracle/Compiler Architecture

> **Confirmation: the corpus is NOT a god file.** It's a hierarchy of small per-node files, each with frontmatter for routing, chunked into RAG by H2 sections. Master documents at the top of each subtree describe the structure; per-node files (one per tool / one per repo) hold the actual behavioral specs.

## Top-level layout (5 master docs + 4 subtrees + helper scripts)

```
corpus/
├── ARCHITECTURE.md ← this file (master)
├── OPERATOR_PLAYBOOK.md ← run-time master ("if X then Y")
├── programbench/
│   ├── README.md ← PB master manifest
│   ├── _strategy/         (6 strategy docs ← anchor strategy, mass run plan, residual table, universal patterns, scaffolds, audit)
│   ├── anchors/           (5 anchor packs, 7 files each — README + 6 sections)
│   │   ├── 01_jq/
│   │   ├── 02_fzf/
│   │   ├── 03_lz4/
│   │   ├── 04_fd/
│   │   └── 05_curlie/
│   ├── in_progress/       (190 per-tool dirs, each with 06_behavioral_spec.md)
│   │   ├── <author>__<tool>.<sha>/06_behavioral_spec.md
│   │   └── ... (one dir per residual tool)
│   ├── locked/            (post-mortems for tools at 100%)
│   │   ├── htmlq/
│   │   └── ripsecrets/
│   ├── _lib/              (shared per-language libraries — c, go, py, rs)
│   └── prompts/           (PB-specific architect/builder prompt templates)
└── swebench/
    ├── README.md ← SB master manifest
    ├── swebench_inventory.json       (per-dataset stats)
    ├── swebench_instance_index.jsonl (5,274 instances; lookup by id)
    ├── swebench_repo_clusters.json   (per-repo aggregated metadata)
    └── repos/             (88 per-repo dirs, each with 06_repo_spec.md)
        ├── django__django/06_repo_spec.md
        ├── sympy__sympy/06_repo_spec.md
        ├── ... (one dir per repo)
```

## File-size distribution (proves no god file exists)

| Directory | Files | Avg lines | Largest |
|-----------|-------|-----------|---------|
| `programbench/anchors/` | 35 | 183 | 905 (jq behavioral spec) |
| `programbench/_strategy/` | 6 | 305 | 638 (mass run plan) |
| `programbench/in_progress/` | **190** | **567** | ~1,400 (rumdl) |
| `swebench/repos/` | **88** | **139** | ~330 (scikit-learn polished) |

**Total: 322 markdown files. Largest single file: ~1,400 lines (~50KB). No god file.**

## Master → Node flow

The orchestrator reads from top-of-subtree masters down to per-node specs:

```
                 ┌────────────────────────────────┐
                 │  ARCHITECTURE.md               │
                 │  OPERATOR_PLAYBOOK.md          │  ← human + agent reads
                 └────────────────────────────────┘
                              │
                ┌─────────────┼─────────────┐
                ▼             ▼             ▼
       ┌──────────────┐  ┌──────────┐  ┌──────────────┐
       │ PB README    │  │ SB README│  │ Strategy doc │
       │ (manifest)   │  │ (manifest│  │ (anchor plan,│
       └──────────────┘  └──────────┘  │  mass run,   │
                │             │        │  patterns)   │
                ▼             ▼        └──────────────┘
       ┌──────────────┐  ┌──────────┐
       │ Per-tool dir │  │ Per-repo │
       │ 06_*.md      │  │ 06_*.md  │
       └──────────────┘  └──────────┘
              │                 │
              └─── RAG chunked ──┘  ← seed_knowledge_base.py walks each tree,
                       │              chunks by H2 sections, prefixes metadata
                       ▼              with `programbench |` or `swebench |`
              ┌──────────────────┐
              │  determinex.sqlite  │
              │  wisdom + vss    │  ← 8,869 chunks total
              └──────────────────┘
                       │
              ┌────────┼────────┐
              ▼        ▼        ▼
          ┌──────┐ ┌──────┐ ┌────────┐
          │ C7   │ │ C1   │ │ C3     │
          │Architect│ │Builder│ │Observer│
          │Sentinel │ │Engineer│ │Monitor │
          └──────┘ └──────┘ └────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Compiler Oracle  │  ← rustc / go build / python -c / tsc
              │ (the only judge) │     in isolated git worktree
              └──────────────────┘
                       │
                       ▼
              ┌──────────────────┐
              │  WAL + retrain   │  ← (error → fix) pairs flow back to corpus
              └──────────────────┘
```

## RAG chunking flow

`scripts/seed_knowledge_base.py` walks the corpus tree:

1. For each `*.md` file:
   - Strip YAML frontmatter (preserves `name`, `description`, `type`)
   - Split body on H2 (`## Section X`) boundaries
   - Cap each chunk at 1,200 chars (re-split on paragraph breaks if needed)
   - Tag with metadata: `{collection_prefix} | {relative_path} | {h2_header}`
2. Embed each chunk via fastembed AllMiniLML6V2 (384-dim)
3. Insert into sqlite-vec table; the file's frontmatter `name` becomes a routing identifier

**Result**: any builder/architect query hits the right chunk via cosine similarity, not a giant document scan. Routing example:
- Query: "how should I implement jq's filter compiler?"
- → highest similarity chunk: `programbench | anchors/01_jq/01_architecture.md | Section 3 — Module Breakdown`
- → injected into builder prompt at run-time

## Spec-injection flow at run-time

```
ProgramBench task <iid>:
  agent reads:
    1. T:/Dev/ProgramBench/src/programbench/data/tasks/<iid>/task.yaml
    2. T:/Dev/ProgramBench/src/programbench/data/tasks/<iid>/tests.json
    3. corpus/programbench/in_progress/<iid>/06_behavioral_spec.md   ← per-tool spec
    4. RAG retrieval for any sibling-tool fixtures               ← from anchor cluster
  composes builder prompt → local Ollama OR Anthropic OR DeepSeek

SWE-bench task <iid>:
  agent reads:
    1. instance metadata (issue, base_commit, FAIL_TO_PASS) from parquet
    2. swebench_spec_lookup.inject_block_for(iid)
       → looks up repo from corpus/swebench/swebench_instance_index.jsonl
       → reads corpus/swebench/repos/<sanitized_repo>/06_repo_spec.md  ← per-repo spec
       → composes inject block (spec text + instance metadata)
  composes builder prompt with spec block prepended
```

## Why this is NOT a god file

- **Per-tool specs**: 190 separate files, average 567 lines each. Updating one tool doesn't touch the others.
- **Per-repo specs**: 88 separate files, average 139 lines each. Same isolation.
- **Master manifests**: Each subtree has its own README that lists what's in it. Top-level `ARCHITECTURE.md` (this file) describes the global structure.
- **Strategy docs are separate**: anchor strategy, mass run plan, universal patterns — each is its own file in `_strategy/`, not buried in a single mega-doc.
- **RAG chunking is per-section**: even within a 900-line spec, the H2 boundaries make each section retrievable independently. An architect query hits Section 3, a builder query hits Section 8.
- **Helper scripts are per-concern**: `swebench_spec_lookup.py` (instance lookup), `vram_monitor.py` (GPU), `mass_run_aggregate.py` (results), `health_monitor.py` (run health), etc. — each focused, none a god script.

## What scripts read what

| Script | Reads | Writes |
|--------|-------|--------|
| `determinex_programbench_agent.py` | task.yaml, tests.json, in_progress/<iid>/06_behavioral_spec.md | T:/determinex-programbench/<run>/<iid>/source/, eval JSONs |
| `determinex_swebench_agent.py` | parquet, swebench_spec_lookup → repos/<repo>/06_repo_spec.md | predictions.jsonl, eval JSONs |
| `seed_knowledge_base.py` | corpus/programbench/**/*.md, corpus/swebench/**/*.md | determinex.sqlite (wisdom table) |
| `swebench_spec_lookup.py` | swebench_instance_index.jsonl, repos/<repo>/06_repo_spec.md | (read-only — returns inject block) |
| `preflight_mass_run.py` | docker, ollama, sqlite, hf_cache, corpus | scoreboard to stdout |
| `mass_run_aggregate.py` | T:/determinex-programbench/, T:/determinex-swebench/ eval JSONs | logs/mass_run_aggregates/scoreboard.{txt,json} |
| `vram_monitor.py` | nvidia-smi, ollama /api/ps | stdout (or recommendation string) |
| `health_monitor.py` | docker ps, disk, ollama, eval rates | stdout alerts |
| `live_scorecard.py` | T:/determinex-{pb,sb}/ eval JSONs | c:/tmp/determinex_scoreboard.txt (OBS source) |
| `spec_validity_smoke.py` | corpus/**/*.md | stdout pass/fail |

Each script is bounded — none reads the whole corpus monolithically.

## How to add a new bench (e.g., LiveCodeBench, BigCodeBench, SysMoBench)

The pattern is established. To add a new benchmark:

1. Create `corpus/<bench_name>/` directory with `README.md` master manifest
2. Build per-instance / per-repo spec generators that emit small `.md` files (no god file)
3. Add to `seed_knowledge_base.py`:
   - `<BENCH>_DIR = REPO_ROOT / "corpus" / "<bench>"`
   - `chunks_for_<bench>()` walking the tree
   - `seed_<bench>()` with idempotency check
   - Add `--reseed-<bench>` CLI flag
4. Update `preflight_mass_run.py` with a chunk-count check
5. Update `OPERATOR_PLAYBOOK.md` with launch commands
6. Done — RAG indexing + spec injection happen automatically.

The architecture is **open for extension** — adding LiveCodeBench (or anything else) is a same-pattern repeat, not a re-architecture.

— Determinex · Lunarian Data Systems · 2026-07-08 (Release Candidate)
