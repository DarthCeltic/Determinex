# Determinex — Full Folder Audit (C:\ + T:\)

> Comprehensive layout audit of the Determinex IDE codebase and the T:\ data drive that backs it. **Generated 2026-05-26.** Includes drive footprints, dir-by-dir purpose, monolith identification, and consolidation recommendations.

---

## 1. Two-drive split

Determinex is laid out across two physical drives by deliberate policy:

| Drive | Total Determinex footprint | Role |
|---|---:|---|
| `C:\Dev\Determinex\` | ~107 GB | **Source of truth** for code, configs, docs, logs, the React+Tauri IDE, the Python orchestration, the corpus metadata, and an unusually large staging area. Git-tracked subset. |
| `T:\` | ~648 GB | **Data lake.** Model weights (170 GB), Docker volumes (287 GB), Ollama models (117 GB), ProgramBench instance dataset (35 GB), datasets/logs/HF cache. None of T:\ is git-tracked. |

`.env` sets `DETERMINEX_MODELS_DIR=T:/determinex-models`. The split exists because the model artifacts alone would fill a consumer SSD; T:\ is the 4 TB working drive.

### 1.1 T:\ breakdown

| Path | Size | Files | What it holds |
|---|---:|---:|---|
| `T:\DockerData` | 287.26 GB | 2 | Docker Desktop's VHDX images (ProgramBench eval containers live here) |
| `T:\determinex-models` | 170.88 GB | 1,198 | All GGUF model weights, adapters, version trees, Rosetta MLPs |
| `T:\OllamaModels` | 117.24 GB | 125 | Ollama model store (via `OLLAMA_MODELS` env var; symlink avoided per memory) |
| `T:\determinex-programbench` | 35.56 GB | 1,512,419 | Per-tool ProgramBench staging — extracted tests, factory work roots, compile staging |
| `T:\determinex-datasets` | 13.07 GB | 1,340,895 | SWE-bench Lite/Verified/Full corpora |
| `T:\determinex-target` | 11.75 GB | 13,910 | Cargo target cache for Tauri builds (kept off C:\ to save SSD wear) |
| `T:\huggingface_cache` | 9.72 GB | 2,349 | HF model/dataset cache |
| `T:\determinex-logs` | 0.77 GB | 2,533 | Older log archives (active logs are on C:\) |
| `T:\determinex-staging` | 0 | 0 | Empty — was the prior staging location, migrated to `C:\Dev\Determinex\.determinex_staging` |

### 1.2 C:\Dev\Determinex breakdown (top dirs by size)

| Dir | Size | Files | Role |
|---|---:|---:|---|
| `.determinex_staging/` | **36.9 GB** | 905,358 | **Loose ProgramBench candidate dirs.** 1,146 `pb_*` directories. Biggest concentration of redundant/disposable files in the repo. |
| `scripts/` | 28.9 GB | 2,676 | **Hides** factory-worker scratch space (`scripts/.uv-cache`, `scripts/benchmarks/`, etc.) inside the script tree. Real source is ≤5 MB of `.py` files. |
| `logs/` | 19.3 GB | 1,454,873 | Eval and session logs; 1,112 top-level entries including 13 published ProgramBench reports and per-shard log directories. |
| `corpus/` | 11.9 GB | 129,559 | ProgramBench overrides + locked archives + training corpus JSONL. |
| `frontend/` | 8.1 GB | 33,044 | Tauri + Next.js IDE. The `node_modules/` and `src-tauri/target/` make this size — actual TSX + Rust source is ~1 MB. |
| `data/` | 1.4 GB | 374 | DSL oracle corpora, captured datasets. |
| `bundler/` | 339 MB | 21 | PyInstaller sidecar build output (determinex-hive sidecar binary). |
| `work/` | 145 MB | 347 | Loose run artifacts; should probably be archived or deleted. |
| `.venv/` | 10 MB | 730 | Python virtual environment (most deps installed system-wide). |
| `dataset_generation/` | 4.6 MB | 120 | Monolithic generators (see §3). |
| `docs/` | 0.7 MB | 35 | Markdown docs (separately audited in `DOCS_AUDIT_2026-05-26.md`). |
| `unsloth_compiled_cache/` | 1.3 MB | 18 | LoRA training compile cache. |

**Top-level files at repo root:** 2,065 entries (mostly `.determinex_staging/*` and `logs/*` pollution showing through). Untracked working-state count from `git status -s`: **2,072 lines**.

---

## 2. The application stack (what's actually shipped)

Determinex is a **two-layer architecture** (per `AGENTS.md` and `docs/ARCHITECTURE.md`):

- **Layer A — Tauri desktop app** (Rust backend + Next.js frontend): the user-facing IDE.
- **Layer B — Python orchestrator** (`scripts/`): the hive-mind, training pipeline, and benchmark runners.

### 2.1 Layer A — `frontend/`

```
frontend/
├── src/                              ← Next.js React UI (50 .tsx/.ts files)
│   ├── app/                          ← layout.tsx, page.tsx, globals.css
│   ├── components/                   ← 27 components (BenchmarkRunner, ProgramBenchCockpit,
│   │                                   HiveBuildLoop, PipelineDashboard, IdeationBoard,
│   │                                   ConceptLab, OmniscienceHarvester, PathWireframe, …)
│   │   ├── LoadingThemes/
│   │   └── modals/
│   ├── contexts/                     ← IterationThemeContext.tsx, SettingsContext.tsx
│   ├── hooks/                        ← useBootstrap.ts, useMoaTelemetry.ts
│   └── lib/                          ← api.ts (Tauri IPC client)
│
├── src-tauri/                        ← Rust backend (30 .rs at top level)
│   ├── src/
│   │   ├── main.rs, lib.rs           ← Tauri entry + command registration
│   │   ├── agents/                   ← Multi-agent logic
│   │   ├── ipc_hive/                 ← mod, oracle, roles, session, workspace
│   │   ├── orchestrator/             ← mod, pipeline_models, rag, transport, types
│   │   ├── bin/                      ← Standalone binaries (sidecar?)
│   │   ├── ast_editor.rs   (19 KB)   ← Largest module — tree-sitter editor backbone
│   │   ├── fs.rs            (17 KB)
│   │   ├── ollama_installer.rs (15 KB)
│   │   ├── ipc_benchmark.rs (14 KB)
│   │   ├── sidecar.rs       (13 KB)
│   │   ├── compiler.rs      (12 KB)
│   │   ├── companion_seeder.rs (12 KB)
│   │   ├── lib.rs           (12 KB)
│   │   ├── hardware.rs      (11 KB)
│   │   ├── workspace_search.rs (10 KB)
│   │   └── (20 more smaller modules)
│   ├── tests/
│   │   └── benchmark_ingestor.rs (113 KB) ← largest .rs file in the repo (test data)
│   ├── target/                       ← cargo build output (large; pinned to T:\determinex-target via CARGO_TARGET_DIR)
│   ├── icons/, capabilities/, gen/
│   └── tauri.conf.json
│
├── node_modules/                     ← bulk of frontend's 8 GB
├── package.json, next.config.ts, tsconfig.*
└── out/                              ← Next.js export output
```

**Layout health:** good. 27 React components is reasonable. Largest component file: `BenchmarkRunner.tsx`. No single React file is a monolith.

**Tauri Rust health:** good. 30 modules at the top level; biggest is `ast_editor.rs` at 19 KB. No Rust module breaches the "monolith" threshold (I'd call >50 KB or >2,000 lines a yellow flag; nothing does).

**Notable:** `frontend/src-tauri/tests/benchmark_ingestor.rs` is 113 KB but it's a test fixture, not production code.

### 2.2 Layer B — `scripts/` (Python orchestration)

```
scripts/
├── (260 entries total)
├── Subpackages (well-organized):
│   ├── hive/                         ← Core hive-mind: api_client, budget, code_utils,
│   │                                   compiler, concurrent_guard, ctx_config, dag, …
│   ├── providers/                    ← anthropic_api, deepseek_api, google_api,
│   │                                   local_ollama, openai_api
│   ├── validators/                   ← bash, dockerfile, go, json, llm_critic, powershell,
│   │                                   python, regex (compiler oracles per language)
│   ├── determinex_cloak/                ← Cloak obfuscation package (privacy layer)
│   ├── fine_tuning/                  ← LoRA training driver scripts
│   ├── swe_agent/, swe_run/          ← SWE-bench execution
│   ├── quality_oracle/               ← Quality scoring
│   ├── analysis/                     ← Post-hoc analysis tools
│   ├── testing/                      ← Test runners (`run_chain.sh`, etc.)
│   └── benchmarks/                   ← Benchmark-specific drivers
│
├── determinex_*.py (~45 top-level entry points):
│   determinex_hive.py             ← THE orchestrator (new-session / generate-dag / run-session)
│   determinex_swebench_agent.py (162 KB) ← Largest .py monolith. SWE-bench solve loop.
│   determinex_programbench_agent.py (99 KB) ← PB solve loop with Cloak hooks
│   determinex_cloak.py            ← Cloak obfuscation pipeline
│   determinex_rosetta.py (42 KB)  ← Rosetta MLP register/verify/project
│   determinex_specialist.py (34 KB)
│   determinex_fullbench.py (37 KB), determinex_benchmark.py (31 KB)
│   determinex_flywheel.py         ← Retrain trigger
│   determinex_swebench_run.py (32 KB) ← Config B/D/E runner
│   determinex_inference.py        ← Layer 2 logit bridge
│   determinex_validate.py, determinex_db.py, determinex_doctor.py
│   determinex_pb_taxonomy.py, determinex_programbench_probe.py
│   determinex_setup.py, determinex_metrics.py, determinex_wandb.py
│   determinex_log_watch.py, determinex_otel.py, determinex_notify.py
│   determinex_forge.py, determinex_queue.py, determinex_rag_index.py
│   determinex_codeclash_agent.py, determinex_swelancer_feature_agent.py
│   determinex_langgraph_orchestrator.py, determinex_livecode_run.py
│   determinex_limits_test.py, determinex_bigcode_run.py
│   determinex_projector.py (52 KB), determinex_vllm_serve.sh
│   determinex_ask.py, determinex_vision.py
│
├── pb_*.py (~30 ProgramBench helpers):
│   pb_pool_status.py, pb_lock_archiver.py, pb_candidate_gate.py,
│   pb_apply_gate_decision.py, pb_hetzner_pool.py, pb_export_hetzner_shard.py,
│   pb_import_hetzner_shard.py, pb_register_gate_result.py, pb_lesson_writer.py,
│   pb_pack_candidate.py, pb_native_source_guard.py, pb_native_eval_queue.py,
│   pb_score_audit.py, pb_factory_worker_loop.py (64 KB), pb_upstream_oracle.py,
│   pb_verdict_corpus.py, pb_wal.py, pb_refresh_rag_after_accept.py, …
│
├── programbench_*.py (~15 PB infrastructure):
│   programbench_eval_runner.py, programbench_image_preflight.py,
│   programbench_argv_miner.py, programbench_classify_family.py,
│   programbench_classify_subtype.py, programbench_compare_runs.py,
│   programbench_fixture_extractor.py, programbench_inspect_tool.py,
│   programbench_live_monitor.py, programbench_oracle_miner.py,
│   programbench_patch_advisor.py, programbench_patch_applier.py,
│   programbench_pool_status.py, programbench_resource_guard.py,
│   programbench_failure_analyzer.py
│
├── rosetta_*.py (~5): rosetta_healthcheck, rosetta_recall_eval,
│                       rosetta_softprefix_smoke, rosetta_text_bridge,
│                       rosetta_vs_text_eval (53 KB), train_rosetta_bases (59 KB)
│
├── sprint4_*.py (~9): sprint4_auto_promote, sprint4_bulk_generate,
│                       sprint4_factory_validation, sprint4_preflight,
│                       sprint4_rank_eval_queue, sprint4_smoke_pass, …
│
├── fix_retrain_*.py, fix_*.py: per-role retrain repair scripts
│
├── gap_v*.jsonl files: hand-curated gap corpora (gap_v10 through gap_v23,
│                       one per language/topic — at top level (probably should
│                       move to data/))
│
├── *.sh / *.ps1: shell runners (sync_hetzner_evals.ps1, run_chain.sh, etc.)
│
└── _add_go_curriculum.py, _batch_apply_pending.py, _pb_full_audit.py
    (3 "_" prefixed helpers I authored this session — disposable)
```

**Scripts health:**

- ✅ Well-organized subpackages (`hive/`, `providers/`, `validators/`, `swe_agent/`, etc.) — clear separation of concerns.
- ⚠️ **`scripts/` directory is overloaded.** 260 entries at the top level is hard to navigate. ~190 are `.py` files.
- ⚠️ **`determinex_swebench_agent.py` (162 KB)** is the largest module by a wide margin — likely a monolith candidate.
- ⚠️ **`determinex_programbench_agent.py` (99 KB)** is the second-largest. Both grew organically; both have natural split points.
- ⚠️ **`gap_v10_retry.jsonl` through `gap_v23_data_science.jsonl`** sit at top level of `scripts/` but they're data, not code. Should move to `data/curricula/`.

### 2.3 Layer B — `corpus/`

```
corpus/
├── programbench/
│   ├── locked/                       ← 53 archived locks + README
│   │   └── <tool>/                   ← eval_report.json, submission.tar.gz,
│   │                                   source/, lessons.md.stub, README.md
│   ├── per_tool_overrides/           ← One subdir per of 200 tools (override code/compile.sh)
│   ├── in_progress/                  ← Working-state for each tool (specs, drafts)
│   ├── anchors/                      ← Five anchor packs (jq, fzf, lz4, fd, curlie)
│   ├── families/                     ← Tool-family classifiers + generators
│   ├── results/                      ← Snapshot files (PB_WORK_MATRIX_200, action_sheets, …)
│   ├── prompts/, _lib/, _strategy/, _snippets/
│   ├── training_corpus/              ← Verdict corpus (per-gate ground truth)
│   ├── README.md, reproducible_eval_overrides.json
│
├── auto_curriculum.jsonl
├── gap_gen_*_2k.jsonl                ← One per language (bash, cpp, csharp, dsl, go, java, javascript)
├── corpus_extract.jsonl, ARCHITECTURE.md, OPERATOR_PLAYBOOK.md
```

**Corpus health:** Mostly clean; the heavy weight is in `per_tool_overrides/` (200 tool sources with `compile.sh` + source files). `programbench/results/` has captured snapshot docs that double up with `docs/PROGRAMBENCH_*`.

### 2.4 `bundler/` — PyInstaller sidecar

```
bundler/
├── _pyinstaller_work/
│   ├── spec/
│   ├── work/
│   │   └── determinex-hive/
│   │       ├── build_hive_sidecar.py
│   │       ├── determinex_sidecar.py
│   │       └── setup_sidecar.py
│   └── sidecar/
```

Single-purpose: packages `scripts/hive` as a standalone Windows binary that ships inside the Tauri app. 21 files, 339 MB (includes the bundled Python interpreter and binaries).

### 2.5 Other top-level dirs

| Dir | Purpose | Health |
|---|---|---|
| `archive/` | Old retired code | OK, isolation by name |
| `archive_streamlit/` | Pre-Tauri Streamlit UI | Dead, can probably delete |
| `benchmarks/` | Standalone benchmark drivers (`run_immune_gauntlet.py`, `vram_crucible.py`) | Active |
| `book/`, `dashboards/` | Tiny — likely demo/marketing material | Verify before deleting |
| `dataset_generation/` | **Monolith files** — see §3 | ⚠️ Refactor candidate |
| `docker/`, `Dockerfile`, `docker-compose.yml` | Container infra | Active |
| `k3s/` | Kubernetes manifests | Sprint-0 artifact, may be stale |
| `landing/` | Marketing landing page | Active |
| `modelfiles/` | Ollama Modelfiles (Engineer, Sentinel, Observer, …) | Active |
| `registry/` | Model registry metadata | Active |
| `rosetta/` | Rosetta MLP training artifacts | Active |
| `runpod/` | RunPod-specific setup scripts (training) | Periodic use |
| `sessions/` | Live session WAL records | Runtime state |
| `specs/`, `test_specs/`, `tests/` | Spec corpora + unit tests | Active |
| `tools/` | Misc utilities | Verify contents |
| `unsloth_compiled_cache/` | LoRA training compile cache | Auto-managed |
| `work/` | Loose run artifacts (145 MB, 347 files) | ⚠️ Old; consider cleanup |
| `executors/`, `determinex_memory/`, `determinex_trainer/` | Active subsystems | OK |

---

## 3. Monoliths and hotspots

Files that are unusually large for their kind:

### 3.1 Source monoliths

| File | Size | Notes |
|---|---:|---|
| `scripts/determinex_swebench_agent.py` | **162 KB** | The SWE-bench solve loop. Natural splits: patch generation, gate logic, retry strategy, Cloak hooks, telemetry. |
| `scripts/determinex_programbench_agent.py` | **99 KB** | The ProgramBench probe → spec → build → eval driver. Similar splittable structure. |
| `corpus/programbench/families/generator_lib.py` | **102 KB** | Family-classifier generator library. Single-purpose; OK as monolith for now. |
| `scripts/micro_eval.py` | **95 KB** | Fast eval driver (45-probe suite). |
| `scripts/micro_eval_extra.py` | **91 KB** | Extended eval suite (135-probe). |
| `dataset_generation/_gen_java_mass.py` | **189 KB** | Java curriculum mass-generator. |
| `dataset_generation/_gen_java_batch11.py` | **176 KB** | One of 11 Java batch generators. Copy-paste duplication suspected. |
| `dataset_generation/_gen_java_batch9.py` | **138 KB** | Same family. |
| `data/gen_dsl_oracles.py` | **85 KB** | DSL oracle generator. |
| `dataset_generation/gen_real_scale_v4.py` | **84 KB** | |
| `frontend/src-tauri/tests/benchmark_ingestor.rs` | **113 KB** | Test data, not production code. Keep. |

**Refactor recommendations:**
- **`determinex_swebench_agent.py`** → split into `swe_agent/{solve_loop, patch_generation, gate, retry, telemetry}.py`. The `swe_agent/` package already exists alongside.
- **`determinex_programbench_agent.py`** → same pattern; `programbench_agent/{probe, spec, build, eval, hooks}.py`.
- **`dataset_generation/_gen_java_batch{2,3,5,7,8,9,10,11}.py`** — 8 nearly-identical batch files. Consolidate to one parameterized generator. ~1 MB of duplicated Java curriculum code.

### 3.2 Heavyweight directories (footprint, not code quality)

| Path | Size | Issue |
|---|---:|---|
| `.determinex_staging/` | 36.9 GB | **1,146 `pb_*` working copies**. Most are stale candidate dirs from gate attempts that didn't lock. Garbage-collect to keep most-recent-3 per tool. |
| `logs/` | 19.3 GB | 1.4M files. Includes per-shard `hetzner_*` subdirs. Archive everything pre-2026-05-19; keep eval ledger JSONLs. |
| `scripts/` | 28.9 GB | Real source ≤5 MB; the rest is `__pycache__`, `.uv-cache`, factory worker scratch under `scripts/benchmarks/`. Add to `.gitignore` and don't ship in source distributions. |
| `corpus/` | 11.9 GB | 200 tool override trees + 53 locked archives + JSONL training corpora. Largest legitimate footprint. |
| `frontend/node_modules/` | ~6 GB | Standard Next.js. Not in repo. |
| `frontend/src-tauri/target/` | ~2 GB | Cargo build cache. Should be pinned to T:\ via CARGO_TARGET_DIR (some of it is). |
| `T:\DockerData` | 287 GB | Docker Desktop's VHDX. Holds the cleanroom + compiled ProgramBench images. Required at runtime. |

---

## 4. State / runtime dirs (not source)

These are runtime artifacts that pollute the file count but aren't part of the codebase:

| Path | What | Action |
|---|---|---|
| `__pycache__/` (everywhere) | Python bytecode | Already in `.gitignore`; ignore in audits |
| `.uv-cache/`, `.pytest_cache/` | Tooling cache | Already in `.gitignore` |
| `.determinex/chrono.db` | Chrono DB (SQLite, 73 KB) | Runtime; keep |
| `.determinex_staging/cargo-target-check/` | Cargo target check artifacts | Periodic cleanup |
| `.determinex_staging/cloud_outputs/` | API response cache from cloud providers | Periodic cleanup |
| `.determinex_staging/evals/` | Per-eval ephemeral state | Periodic cleanup |
| `.determinex_staging/hetzner_returns/` | Returned shard manifests | Important — gate flow reads from here |
| `.determinex_staging/hetzner_shards/` | Outbound shard tarballs | Cleaned after deploy |
| `.determinex_staging/pb_*/` (1,146 dirs) | Per-attempt PB candidate working dirs | **Biggest cleanup target.** GC policy needed. |
| `sessions/` | Live session WAL records | Runtime; rotate periodically |
| `work/` (145 MB) | Loose run artifacts | Likely archive/delete |

---

## 5. Concrete cleanup recommendations

### 5.1 Disk reclamation (low effort, high reward)

| Action | Reclaim | Effort |
|---|---:|---|
| **Garbage-collect `.determinex_staging/pb_*`** to most-recent-3 per tool (currently 1,146 dirs across ~150 tools) | ~25 GB | 30 min (script) |
| **Archive `logs/*` older than 2026-05-19** to a tarball, delete originals | ~15 GB | 15 min |
| **Delete `archive_streamlit/`** (pre-Tauri UI) | <100 MB | 5 min |
| **Audit `work/`** (145 MB, 347 files) — likely all archivable | 145 MB | 15 min |
| **Audit `scripts/benchmarks/` cache content** — looks like scratch | ~25 GB if matches my guess | 30 min |
| **Total potential reclaim** | **~65 GB** of the 107 GB C:\ footprint | ~2 hr |

### 5.2 Source refactors (medium effort, structural)

| Action | Why | Effort |
|---|---|---|
| **Split `determinex_swebench_agent.py` (162 KB) into `swe_agent/` package** | Module is too large to reason about in a single file; natural seams exist | 1 day |
| **Split `determinex_programbench_agent.py` (99 KB) similarly** | Same problem; same natural seams | 1 day |
| **Consolidate 8 `dataset_generation/_gen_java_batch*.py` files** | Copy-paste duplication, ~1 MB total | 4 hours |
| **Move `scripts/gap_v*.jsonl` (14 files) to `data/curricula/`** | They're data, not code; clutter `scripts/` tree | 15 min |
| **Move `scripts/_*.py` (3 disposable helpers) into `scripts/archive/`** | Authored ad-hoc, shouldn't be top-level | 5 min |

### 5.3 Organization (low effort)

| Action | Why |
|---|---|
| Add `.gitignore` rule for `scripts/.uv-cache/`, `scripts/benchmarks/*.bin`, `scripts/__pycache__/`, etc. — clean up `git status` output | `git status -s` currently returns **2,072 dirty lines**; most are auto-generated noise that shouldn't be visible. |
| Top-level `Modelfile.*` should move to `modelfiles/` (already has a `modelfiles/` dir) | 4 files (engineer, leviathan, observer, sentinel) at repo root duplicate the `modelfiles/` directory. |
| Top-level `eval_engineer_v10.txt`, `determinex_system_audit_report.md`, `ux_dx_audit_report.md`, `codebase_structure.md` are leftover artifacts | Archive or move to `docs/_archive/`. |

---

## 6. Architecture map (the mental model)

```
┌─────────────────────────────────────────────────────────────┐
│  USER                                                       │
│   └─→ Tauri app (frontend/)                                 │
│        Next.js UI ↔ Rust IPC ↔ Python sidecar (bundled)     │
└────────────────────────────┬────────────────────────────────┘
                             │ spec / command
                             ▼
┌─────────────────────────────────────────────────────────────┐
│  PYTHON HIVE  (scripts/determinex_hive.py)                     │
│                                                             │
│  Spec → C7 Architect (DAG) → C1 Builder (code)              │
│              ↓                      ↓                       │
│         C3 Monitor ← Compiler Oracle (rustc/go/python/tsc)  │
│              ↓                      ↓                       │
│         WAL (sessions/)        Verdict corpus               │
│              ↓                      ↓                       │
│         Flywheel retrain ← LoRA on RunPod                   │
└────────────────────────────┬────────────────────────────────┘
                             │ models live on
                             ▼
        T:\determinex-models  +  T:\OllamaModels  +  Rosetta MLPs

┌─────────────────────────────────────────────────────────────┐
│  BENCHMARKS                                                 │
│                                                             │
│  SWE-bench: determinex_swebench_agent.py + swe_agent/          │
│  ProgramBench: determinex_programbench_agent.py + pb_*.py      │
│  Eval queues:                                               │
│    Local Docker (target/DockerData)                         │
│    Hetzner shard pool (pb_hetzner_pool.py → root@5.78…)     │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Quick reference — where things live

| You want… | Look here |
|---|---|
| User-facing IDE source | `frontend/src/` (React) + `frontend/src-tauri/src/` (Rust) |
| Hive orchestrator | `scripts/determinex_hive.py` + `scripts/hive/` |
| Compiler oracles | `scripts/validators/{bash,go,python,…}_validator.py` |
| Cloud provider integrations | `scripts/providers/{anthropic,deepseek,google,openai,local_ollama}_api.py` |
| Rosetta Stone | `scripts/determinex_rosetta.py` + `rosetta/` + `T:\determinex-models\rosetta\rosetta_v1.pt` |
| Project Cloak | `scripts/determinex_cloak.py` + `scripts/determinex_cloak/` + `scripts/determinex_cloak_*.py` |
| SWE-bench runner | `scripts/determinex_swebench_run.py` + `scripts/determinex_swebench_agent.py` + `scripts/swe_agent/` |
| ProgramBench agent | `scripts/determinex_programbench_agent.py` + `scripts/pb_*.py` + `scripts/programbench_*.py` |
| Lock archives | `corpus/programbench/locked/<tool>/` |
| Tool overrides | `corpus/programbench/per_tool_overrides/<tool>.<hash>/` |
| Training corpus | `corpus/programbench/training_corpus/` + `data/*.jsonl` + `scripts/gap_v*.jsonl` |
| Model weights | `T:\determinex-models\*.gguf` + `T:\determinex-models\adapters\` |
| RunPod training | `runpod/` + `determinex_trainer/` + `scripts/fine_tuning/` |
| Hetzner shard infra | `scripts/pb_hetzner_pool.py` + `scripts/pb_export_hetzner_shard.py` + `scripts/pb_import_hetzner_shard.py` |
| Live session state | `sessions/*.json` + `.determinex/chrono.db` |
| Eval logs | `logs/` (most recent) + `T:\determinex-logs\` (older archives) |
| ProgramBench instance dataset | `T:\determinex-programbench\` (35 GB, 1.5M files — pre-cloned tool repos) |
| Docker container images | `T:\DockerData\` (287 GB — Docker Desktop's VHDX) |
| Bundled sidecar (for Tauri ship) | `bundler/_pyinstaller_work/sidecar/` |
| Modelfiles (Ollama) | `modelfiles/` + 4 stale duplicates at repo root |
| Docs | `docs/` (separately audited in `DOCS_AUDIT_2026-05-26.md`) |

---

## 8. Summary

**Code health:** strong. Tauri Rust is small (~30 modules, none monolithic). Frontend has 27 React components, reasonable. Python orchestration has clean subpackages (`hive/`, `providers/`, `validators/`, `swe_agent/`). The two real source monoliths are `determinex_swebench_agent.py` (162 KB) and `determinex_programbench_agent.py` (99 KB) — both refactorable into their existing sibling packages.

**Disk health:** poor. 107 GB on C:\, but ~65 GB is reclaimable (1,146 stale `pb_*` staging dirs, old logs, archive_streamlit, work/). The 1.4 million log files plus 905k staging files make `git status` show 2,072 dirty entries.

**Organization:** mostly clean, with a few specific eyesores:
- 4 stale `Modelfile.*` at repo root (duplicate of `modelfiles/`)
- 14 `gap_v*.jsonl` in `scripts/` that are data not code
- `archive_streamlit/` (pre-Tauri UI) is dead

**The biggest win available**: garbage-collect `.determinex_staging/pb_*` to most-recent-3 per tool. That alone reclaims ~25 GB and drops the staging file count by ~80 %. Pair with a `logs/` archive sweep for another ~15 GB.

**Tracked separately:** the docs audit (`docs/DOCS_AUDIT_2026-05-26.md`) and the ProgramBench board status (`docs/PROGRAMBENCH_BOARD_STATUS_2026-05-26.md`).
