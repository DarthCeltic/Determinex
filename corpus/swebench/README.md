---
name: swebench-corpus
description: Determinex's SWE-bench-family corpus. 89 per-repo behavioral specs aggregated from 5,274 bug-fix instances across 7 datasets (SWE-bench Lite/Verified/Full, Multilingual, Multi-SWE-bench). Inject into builder prompts to drive bug-fix attempts; routed into the knowledge-base RAG.
type: corpus
---

# SWE-bench Corpus

> **Why this exists.** ProgramBench tests "build this CLI from scratch." SWE-bench-family tests a different skill: **fix this real bug in this real repo**. Different shape (issue + base_commit + FAIL_TO_PASS test list + reference patch), different empirical-spec method. The corpus shifts from "behavioral surface" (PB) to "repo behavioral patterns" (SWE-bench).

## What's here

```
corpus/swebench/
├── README.md                          ← this file
├── swebench_inventory.json            ← per-dataset stats: instance count, columns, sample row
├── swebench_instance_index.jsonl      ← 5,274 instances, one JSON per line, no patches
├── swebench_repo_clusters.json        ← per-repo aggregated metadata
└── repos/<sanitized_repo>/06_repo_spec.md   ← 89 per-repo behavioral specs
```

## Datasets covered

| Dataset | Instances | Source |
|---------|-----------|--------|
| SWE-bench Lite (test) | 300 | Princeton — curated subset, Python only |
| SWE-bench Lite (dev) | 23 | Princeton — dev split |
| SWE-bench Verified (test) | 500 | Princeton — human-verified subset |
| SWE-bench Full (test) | 2,294 | Princeton — full test set |
| SWE-bench Full (dev) | 225 | Princeton — full dev set |
| SWE-bench Multilingual (test) | 300 | Princeton — multi-language extension |
| Multi-SWE-bench (40 repos × 8 langs) | 1,632 | ByteDance Seed — multilingual, real repos |
| **Total** | **5,274 instances across 89 unique repos** | |

## Top-15 repos by instance count (covers ~75% of bench)

| Repo | Instances | Lang |
|------|-----------|------|
| django/django | 1,195 | python |
| sympy/sympy | 538 | python |
| cli/cli | 397 | go |
| scikit-learn/scikit-learn | 284 | python |
| sveltejs/svelte | 272 | js |
| sphinx-doc/sphinx | 247 | python |
| matplotlib/matplotlib | 241 | python |
| mui/material-ui | 174 | ts |
| pytest-dev/pytest | 155 | python |
| pydata/xarray | 137 | python |
| clap-rs/clap | 132 | rust |
| astropy/astropy | 123 | python |
| ponylang/ponyc | 82 | c |
| pylint-dev/pylint | 73 | python |
| pvlib/pvlib-python | 68 | python |

## Per-repo spec structure (`repos/<sanitized>/06_repo_spec.md`)

Each spec has 7 sections:

1. **Dataset coverage** — which datasets contain instances of this repo
2. **Where bugs typically live** — top files touched across all fixes (auto-mined from `diff --git` headers in patches; **only file paths, not patch content**)
3. **Test framework signal** — pytest / Go test / JUnit / jest detected from FAIL_TO_PASS naming
4. **Problem-theme distribution** — issue statements clustered into 15 themes (regression, crash, edge case, perf, etc.)
5. **Sample issues** — 8 representative problem statements (no patches — those are the answer)
6. **Builder guidance** — how to approach a fix in this repo
7. **Index of all instances** — first 20 instance_ids; rest queryable from the JSONL

## What's NOT in the corpus (deliberate)

**No reference patches.** The gold-standard patches are SWE-bench's *answer key*. Including them in any spec or RAG entry would make the eval invalid. The specs describe:
- Where bugs tend to live (file paths)
- What the issue says
- What tests will judge the fix
- Repo conventions (test framework, file organization, problem themes)

But they do NOT include:
- The reference patch body
- Code that resembles the fix
- Hint text that gives away the solution

## Method differences from ProgramBench corpus

| Concern | ProgramBench | SWE-bench |
|---------|--------------|-----------|
| Unit | Tool (200 of them) | Instance (5,274 of them) |
| Spec scope | Per-tool (the whole CLI) | Per-repo (clusters of bugs) + per-instance index |
| Source data | pytest test files + golden output files | Issue text + base_commit + FAIL_TO_PASS test names + reference patch |
| What we mine | CATCHES docstrings, byte-exact assertions, flag inventory | File-touch frequency, problem themes, test framework |
| What's the answer | The full implementation | The fix patch |
| What we exclude from spec | Nothing — full surface | The reference patch (the answer) |

## Run-time injection (when this gets used)

For a SWE-bench instance attempt:

1. Look up instance in `swebench_instance_index.jsonl` by `instance_id`
2. Pull the repo's `06_repo_spec.md` from RAG (or filesystem)
3. Inject into builder prompt:
   - Issue / problem_statement (from instance index)
   - FAIL_TO_PASS test names (from instance index)
   - Repo behavioral spec (file organization, common patterns, where bugs live)
   - Files at base_commit (from `git checkout`)
4. Builder generates patch
5. Apply patch, run FAIL_TO_PASS tests, validate

## Multi-window propagation

This corpus, like the ProgramBench one, lives at filesystem paths shared by all Determinex windows. Once seeded into the RAG (`scripts/seed_knowledge_base.py --reseed-programbench` — same flag covers both since they share the `general` collection), every window can query specs and the per-instance index.

## Status / what's next

- ✅ Inventory + indexing complete (5,274 instances)
- ✅ Per-repo specs generated (89 / 89)
- ✅ `swebench_inventory.json` / `swebench_repo_clusters.json` queryable via
  `determinex_corpus_api.swebench_stats()` / `swebench_repo_info(owner/repo)` (2026-07-19 --
  found orphaned by `corpus_wiring_census.py`'s widened scope, closed same day)
- ⏳ RAG ingestion (next: reseed)
- ⏳ Hand-polish the 5 highest-instance-count repos (django, sympy, cli/cli, scikit-learn, svelte) for anchor-grade depth
- ⏳ Local-builder integration: `determinex_swebench_agent.py` already exists for SWE-bench; needs spec-injection wiring

— Locked 2026-05-09. Treat as canonical until per-repo data is refreshed via re-extract.
