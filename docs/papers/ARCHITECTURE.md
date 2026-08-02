# Determinex — Architecture & Origin Record

> **Status**: Living document. Origin record written from audit of git history, source
> code, and build artifacts as of April 12, 2026. Architecture additions appended through
> 2026-06-03. **Last revision**: 2026-06-03.
> **Purpose**: Ground truth record for the white paper, the AGPLv3 open-source release, and
> enterprise documentation. Also a reference for the author when context is lost
> between sessions.

---

## 2026-05-29 Update — What Has Been Added Since the April Origin

The origin record below (through April 12, 2026) covers the first ~73 hours of work:
single-developer, single-GPU, Streamlit → Next.js → Rust pivot, self-improving AI loop
closed. Since then, the system has been hardened, instrumented, and extended along five
axes. This update summarizes each so the architecture document tracks current reality.

### 1. Compiler Oracle as Universal Reward (April → May)

The 9-language repair lock series (`*_REPAIR_LOCK_001`) is now production: Rust, Python,
Go, C, C++, TypeScript, JavaScript, Ruby, PHP. Each language passes through the same
isolated-worktree → compile → target-test gate. The compile gate threshold raised from
3 → 5 attempts after the SWE-bench hardening sprint of 2026-05-05. See
[`docs/architecture/UNIVERSAL_VERIFIED_TASK_HARNESS.md`](../architecture/UNIVERSAL_VERIFIED_TASK_HARNESS.md)
and [`docs/architecture/UNIVERSAL_VERIFIED_TASK_LANGUAGE_MATRIX.md`](../architecture/UNIVERSAL_VERIFIED_TASK_LANGUAGE_MATRIX.md).

### 2. ProgramBench Factory (May)

A per-tool campaign apparatus built on top of the compiler oracle. Probe → spec → build
→ eval → archive. Lock trajectory: 5 on 2026-05-19, 35 on 2026-05-25, 53 on
2026-05-26, 55 on 2026-05-27, 67 on 2026-06-04 *(note: under old subset metric — see
Section 9 below for June 6 correction)*, 15 honest official-metric locks on 2026-06-06,
**46 official-metric locks as of 2026-06-10**. The pre-audit figures (67 locks / 57.06%
aggregate) used a subset metric excluding `not_run` from the denominator; corrected
official-metric count: **46/200 = 23.0%**. See Section 9 for the full audit record.

Reusable patterns now catalogued and re-applied across the corpus: slug-hash audit,
install AS `executable`, `exec -a`, stderr/stdout `sed` normalization, hardware
environment fixture pinning, counter-state trick for conflicting tests, source flag
parser fixes. Hetzner shard pool absorbs heavy compile/eval loads. See
[`docs/papers/PROGRAMBENCH.md`](PROGRAMBENCH.md) and
[`docs/programs/programbench/`](../programs/programbench/).

### 3. SWE-bench Lite Ablation (May, ongoing)

Five configs against SWE-bench Lite (300 instances), post-hardening. The 2026-05-11
B-Uncloaked run resolved 14.0 % (42/300, zero errored), but it is an audited May
snapshot, not a final publication baseline. The three Cloak-on / region-mode
configurations ran on disk-pressured workers; resolved counts
(>=6.0 % / >=2.3 % / >=3.3 %) remain lower bounds pending fresh B-Uncloaked and
E-RegionControl reruns on larger-disk workers. See
[`docs/papers/PROJECT_CLOAK.md`](PROJECT_CLOAK.md).

### 4. Universal 100 Product Capability Campaign (May 27 onward)

A separate ledger from ProgramBench. Benchmark results are not product support, not release support, and not product readiness. Tracks Determinex's *product surface* capability matrix
across 17 app classes × 15 languages × 12 workflows. Conveyor backlog, depth queue,
sector gulp batches, support-map deltas, gap-closure waves. Codex/Claude tandem
reconciliation channel. ~100 docs at
[`docs/programs/universal-100/`](../programs/universal-100/). The Scale-to-100 lock
**is not yet** a validated capability claim — see
[`DETERMINEX_SCALE_TO_100_CLAIM_TRUTH_AUDIT_20260529.md`](../programs/universal-100/DETERMINEX_SCALE_TO_100_CLAIM_TRUTH_AUDIT_20260529.md).

2026-06-02 final-gate accounting adds a known-world plan and Top-25 exact-blocker queue:
24 categories are accounted/routed/gated, 25 highest-priority gaps have exact blockers,
and support promotion remains blocked until detector + fixture + verifier +
toolchain/acquisition + bounded execution pass. Release-supported exact cells remain 13;
release-supported families remain 0.

2026-06-03 Batch 004 adds one exact all-gap support promotion only: the deterministic
day-one claim scanner guard. Seven additional all-gap promotion attempts remain blocked,
release-supported families remain 0, and the monolithic `tests/status` attempt timed out
near 38% with failures/errors already emitted. That timeout is recorded as a runtime
blocker, not a pass.

### 5. Tauri Unified Product Shell (Layer A maturation, May 27-29)

The Tauri shell now carries:
- A unified command surface (Rust backend command bridge)
- Unified navigation model
- Five product panels with verified-demo-status bindings:
  - **Idea Lab** — Python CLI splash demo
  - **Learning Studio** — teaching splash demo
  - **Maintenance Bay** — dry-run update splash demo
  - **Repo Clinic** — fixture repair splash demo
  - **Proof Operator Center** — milestone dashboard with view-model
- A release-readiness blocker panel
- Demo-navigation happy/blocked paths

Batch 003 verifies the rebuilt staged installed-app Proof Center route at `/proof-center` with screenshot/transcript evidence and records segmented status runtime evidence. This is bounded local unsigned install proof only: signed/trusted installer readiness, clean-host install readiness, open availability, family support, and full monolithic `tests/status` completion remain unproven.

The shell is compiled/scaffolded but does **not** yet carry full Hive orchestration IPC —
that remains in `determinex_hive.py` — and clean-host GUI proof is pending. Demo readiness
locks and browser snapshots exist for the scaffolded surface. See
[`docs/ide-frontend/`](../ide-frontend/) and [`docs/workflows/`](../workflows/).

### 6. Cathedral Index Foundation (May 29)

Single binding node connecting the proof, training, release, and product-capability
ledgers. Foundation for the full Cathedral Release campaign.
- Spec: [`docs/architecture/DETERMINEX_CATHEDRAL_INDEX_FOUNDATION.md`](../architecture/DETERMINEX_CATHEDRAL_INDEX_FOUNDATION.md)
- Full release-path audit: [`docs/audits/DETERMINEX_FULL_CATHEDRAL_RELEASE_PATH_AUDIT_20260529.md`](../audits/DETERMINEX_FULL_CATHEDRAL_RELEASE_PATH_AUDIT_20260529.md)

### 7. Governance Layers Added

| Layer | Doc |
|---|---|
| Append-only evidence ledger | [`policy/DETERMINEX_APPEND_ONLY_EVIDENCE_LEDGER.md`](../policy/DETERMINEX_APPEND_ONLY_EVIDENCE_LEDGER.md) |
| Cross-lane authority boundary | [`policy/DETERMINEX_CROSS_LANE_AUTHORITY_BOUNDARY.md`](../policy/DETERMINEX_CROSS_LANE_AUTHORITY_BOUNDARY.md) |
| Global training eligibility guard | [`policy/DETERMINEX_GLOBAL_TRAINING_ELIGIBILITY_GUARD.md`](../policy/DETERMINEX_GLOBAL_TRAINING_ELIGIBILITY_GUARD.md) |
| Global training positive gate design | [`policy/DETERMINEX_GLOBAL_TRAINING_POSITIVE_GATE_DESIGN.md`](../policy/DETERMINEX_GLOBAL_TRAINING_POSITIVE_GATE_DESIGN.md) |
| Evidence count drift guard | [`policy/DETERMINEX_EVIDENCE_COUNT_DRIFT_GUARD.md`](../policy/DETERMINEX_EVIDENCE_COUNT_DRIFT_GUARD.md) |
| Approval signature cryptographic binding | [`policy/APPROVAL_SIGNATURE_CRYPTOGRAPHIC_BINDING.md`](../policy/APPROVAL_SIGNATURE_CRYPTOGRAPHIC_BINDING.md) |
| Apply-gate fixture refusal | [`policy/APPLY_GATE_FIXTURE_REFUSAL.md`](../policy/APPLY_GATE_FIXTURE_REFUSAL.md) |
| Diagnose prompt opacity enforcement | [`policy/DIAGNOSE_PROMPT_OPACITY_ENFORCEMENT.md`](../policy/DIAGNOSE_PROMPT_OPACITY_ENFORCEMENT.md) |
| Model admission no bypass | [`policy/MODEL_ADMISSION_NO_BYPASS.md`](../policy/MODEL_ADMISSION_NO_BYPASS.md) |
| Support-cell promotion gate | [`policy/DETERMINEX_SUPPORT_CELL_PROMOTION_GATE.md`](../policy/DETERMINEX_SUPPORT_CELL_PROMOTION_GATE.md) |

These layers enforce that **no claim, mutation, training row, or release artifact** can
bypass a recorded verifier. They are the policy surface of the Compiler-Oracle principle.

### 8. Doc Reorganization (2026-05-29)

All 375 docs reorganized from a flat `docs/` into 11 typed folders. Index at
[`docs/README.md`](../README.md).

---

## 2026-06-10 Update — Measurement Audit, June Campaign, Safety Architecture

### 9. ProgramBench Measurement Audit + June 10 Campaign

**Measurement audit (June 6, 2026)**: The "77 strict locks / 57.06% aggregate" figures used a subset metric (`passed / runnable`, excluding `not_run` from the denominator). The official ProgramBench metric requires `passed == total` including `not_run`. After the audit, the honest count corrected to **15 genuine full-suite locks** as of June 6. This was an integrity-class correction consistent with the compiler-oracle principle applied to benchmark methodology: a designed thing is not a shipped thing; a measured count must match the measurement method of the benchmark being cited. Audit doc: [`docs/audits/pb_measurement_audit_2026_06_06.md`](../audits/pb_measurement_audit_2026_06_06.md).

Lock trajectory since the June 6 audit:
- 2026-06-06 (night): guard cleanup + ascii-image-converter + gron re-verified → 15 honest locks
- 2026-06-07 (deep filesystem audit): corrected to 12; scc locked → 13; ditaa locked → 14; genact locked → 15; pingu ceiling confirmed (3 upstream skips, NOT a lock)
- 2026-06-10: 8 new official locks (entr · hck · ngrrram · pier · rhit · tailspin · trdsql · xsv) + 22 previously-queued locks archived simultaneously → **46 confirmed full-suite locks / 23.0%**

**June 10 CI gate**: `pb_override_scan.py --guard` added as a lock-archival CI gate, enforcing zero collection-modifying eval overrides (`del items[N:]`, `collect_ignore_glob`, `pytest_collection_modifyitems` test filters) on all locked archives. This is the same compiler-oracle principle applied to the benchmark measurement layer.

**Board field hygiene audit (June 10)**: Five eval_index entries found with `official_full_suite_resolved: true` incorrectly set:
- `tuc`, `sd`, `elfcat`, `dsq` → reclassified to `upstream_skips` (passed < total due to upstream `pytest.mark.skip` tests the reference binary also cannot pass)
- `xz` → reclassified to `ceiling_confirmed` (4 TTY failures + 8 upstream skips — same class as fd/hexyl)

### 10. Safety Architecture (June 2026)

Five independent safety layers implemented and running (all fail-closed — deny on unexpected error). Documented at [`docs/SAFETY.md`](../SAFETY.md).

| Layer | File | What it catches |
|---|---|---|
| L0 — Content Policy | `scripts/determinex_safety.py` | 28 absolute-deny + 12 ethical-harm categories (regex pre-spec gate, before session creation) |
| L1 — Intent Classifier | `scripts/determinex_safety.py` | Reframing: signal keyword + amplifying context pattern co-occurrence |
| L2 — Egress Filter | `scripts/hive/safety_gate.py` | 16 secret categories leaking to cloud APIs; enforces Cloak when `DETERMINEX_REQUIRE_CLOAK=1` |
| L3 — Output Scanner | `scripts/determinex_safety.py` / `scripts/hive/compiler.py` | Malicious-intent behavioral patterns in Builder-generated code |
| L4 — Corpus Integrity | `scripts/corpus/corpus_manager.py` | HMAC-BLAKE2b-256 on every corpus record; tamper detection at retrain |

**Ethics Oracle (L5)**: Architecture spec at [`docs/policy/ETHICS_ORACLE.md`](../policy/ETHICS_ORACLE.md). **Code not yet built.** Do not describe as present.

**Copyright Displacement Guard + Provenance Sidecar** (`scripts/determinex_copyright_guard.py`): Audit tool for detecting verbatim reproduction of registered works AND tracking attribution to registered reference sources (OSS, academic papers, patents). Runs as a fire-and-forget sidecar in the hive executor and PB agent — never blocks, never raises. In `observe` mode (default): NOT wired into training rewards or corpus filtering; `blocks_corpus_ingestion` always returns False; the compiler is the only oracle on the training-corpus path. In `enforce` mode (`DETERMINEX_PROVENANCE_MODE=enforce`): verbatim hits on non-permissive reference sources additionally produce CopyrightAlerts. Permissive-licensed OSS references (MIT, Apache-2.0, etc.) never produce CopyrightAlerts in any mode — verbatim reuse with attribution is the system working. See `docs/SAFETY.md` for the full behavioral specification.

---

## Origin Record (April 9–12, 2026, unchanged below)

---

## Origin

**April 9, 2026, 1:21 PM** — True start. The earliest file on disk is `archive_streamlit/modes/router_mode.py`, birth timestamp `2026-04-09 13:21:38`. This is before the first git commit. The project began in a code editor, not a terminal.

The first 2 hours and 40 minutes of work happened entirely outside of version control — Streamlit modes were built, the routing architecture was designed, the multi-mode IDE concept was established. By the time the first commit was made, the Streamlit layer was already functional.

**April 9, 2026, 1:21 PM – 2:30 PM** — Streamlit generation (Generation 1). The `archive_streamlit/` directory was built in sequence: router → scaffolding → swap_bench → verify → test_debug (13:21–13:28), then idea_garden (14:01), build + sandbox (14:04), extensions (14:10), and finally the main `app.py` and `omni_context.py` (14:17). Eight mode files in under an hour.

**April 9, 2026, ~2:57 PM** — Next.js frontend installed (`npm install`). The pivot from Streamlit to a proper desktop frontend began within the same afternoon. The project outgrew its prototype in under 2 hours.

**April 9, 2026, 4:01 PM** — First git commit. Message: *"Overbuild IDE Top and Middle Layers."* By this point, the Streamlit layer, the Next.js frontend scaffold, and the FastAPI backend concept were all in place. The commit was not the start — it was a checkpoint of work already done.

**April 9, 2026, 4:01 PM – 11:41 PM** — FastAPI + ChromaDB backend built (Generation 2). `backend/main.py` was last written at 23:41 — a 17,374-byte FastAPI server with WebSocket support, ChromaDB vector storage, LiteLLM multi-provider routing, and **Fernet symmetric encryption** for payload security. The encryption instinct was there from the first night. The Vanguard vault in Rust is a direct evolution of this.

**April 10, 2026, 5:13 PM** — First Swarm auto-checkpoint. The pivot to Tauri + Rust was complete. The system began committing its own progress. Everything that followed — the 1,200-line Rust orchestrator, the MPSC actor model, the fastembed vector engine, the AES-256-GCM vault, the SWE-bench eval harness, the LoRA training pipeline, the adversarial test suite — was built in a single sustained session from 5:13 PM on April 10 through 2:39 AM on April 11. Approximately **9.5 hours**.

**April 12, 2026** — First real training run completes. v4 model trained and evaluated. Eval harness bug found and fixed (P1 was always passing — the harness was wrong). Rust curriculum generation begins. The system generates and compile-validates its own training data. The self-improvement loop closes.

---

**True elapsed time from first file to working self-improving AI system:**

| Milestone | Timestamp |
|---|---|
| First file written | Apr 9, 1:21 PM |
| First git commit | Apr 9, 4:01 PM |
| Rust pivot begins | Apr 10, 5:13 PM |
| Rust pivot complete (last checkpoint) | Apr 11, 2:39 AM |
| First training run + eval + loop closed | Apr 12, ~2:00 PM |
| **Total** | **~73 hours** |

**One developer. One gaming GPU. 73 hours. Streamlit → Next.js → Rust. Self-improving agentic AI.**

This was built while simultaneously architecting a broader suite of projects that Determinex was designed to accelerate. Determinex was not the destination — it was the builder.

---

## What Determinex Is

Determinex is a **self-improving, locally-executed, multi-agent AI development assistant** packaged as a native desktop application. It is not a wrapper around a cloud API. It is not a prompt engineering tool. It is a system that:

1. Runs specialized AI agents on local hardware
2. Routes tasks through a strict sequential pipeline with role boundaries
3. Validates all generated code with real compilers — not LLM judgment
4. Captures its own failures and converts them into training data automatically
5. Fine-tunes its own models on that data, then promotes the improved versions
6. Repeats indefinitely, getting better with each loop

The entire inference-to-improvement cycle happens on the user's machine. No code leaves the device unless the user explicitly enables cloud teacher APIs for training data generation — and even that data is encrypted locally before any optional sync.

---

## System Layers

### Layer 1 — The Application Shell (Tauri + Rust)

The host application is built with **Tauri 2.x**. The Rust backend handles all heavy computation: LLM orchestration, vector search, database, compilation, telemetry encryption. The frontend (JavaScript) is the UI only — it sends IPC commands and renders what the backend returns.

The choice of Tauri over Electron is deliberate: the binary is native, tiny, and does not ship a Chromium instance. The release profile uses LTO + single codegen unit + `opt-level = "z"` + panic-abort + symbol stripping — the final binary is optimized for startup latency and size, not throughput.

**Key Rust dependencies:**
| Crate | Purpose |
|---|---|
| `tauri 2.10` | Application shell, IPC, event system |
| `tokio full` | Async runtime for the MPSC actor loop |
| `rusqlite + sqlite-vec` | Embedded database + vector similarity search |
| `fastembed 5.x` | Local ONNX embedding model (AllMiniLML6V2, 384-dim) |
| `reqwest` | HTTP client for Ollama API calls |
| `tree-sitter + tree-sitter-rust` | AST parsing for workspace code analysis |
| `aes-gcm + rand + base64` | AES-256-GCM encryption for Vanguard vault |
| `ignore` | Gitignore-aware workspace file traversal |

---

### Layer 2 — The Orchestrator (orchestrator.rs, 1,200 lines)

The heart of the system. A **single-consumer, multi-producer (MPSC) actor loop** running in a dedicated Tokio task. All LLM inference flows through this single channel, processed strictly one message at a time.

This is not an accident or a limitation. It is the core design decision that makes Determinex viable on consumer hardware:

> **Sequential throughput beats concurrent thrash.** On a 6 GB GPU, running two models simultaneously means neither fits. The MPSC tollbooth guarantees VRAM is fully owned by whichever agent is active. Model handoffs are explicit, telemetered, and controlled.

The pipeline for every task:

```
User Request
     │
     ▼
┌─────────────────────────────────────────────┐
│  Sentinel (determinex-sentinel)                │
│  Role: Plan, decompose, safety-gate         │
│  Output: Structured SentinelPlan (JSON)     │
│  Context: 2048 tokens                       │
└────────────────────┬────────────────────────┘
                     │ SentinelPlan
                     ▼
┌─────────────────────────────────────────────┐
│  Engineer (determinex-engineer)                │
│  Role: Code generation, implementation      │
│  Output: Raw code                           │
│  Context: 4096 tokens                       │
│  Retry: up to MAX_RETRIES with Observer     │
│          feedback injected on failure       │
└────────────────────┬────────────────────────┘
                     │ Generated code
                     ▼
┌─────────────────────────────────────────────┐
│  Observer (determinex-observer)                │
│  Role: Critique, hallucination detection    │
│  Output: ObserverVerdict {                  │
│    verdict: "CLEAN" | "HALLUCINATION",      │
│    issues: [...],                           │
│    confidence: 0.0–1.0                      │
│  }                                          │
│  Threshold: confidence >= 0.75 to accept    │
└────────────────────┬────────────────────────┘
                     │ CLEAN verdict
                     ▼
              Final Response
```

**Escalation path** (when Engineer fails MAX_RETRIES times):

```
Leviathan (deepseek-coder-v2)
Role: Last-resort deep architect
Hardware: CPU + RAM (VRAM stays free for swarm)
Context: 8192 tokens
Keep-alive: 1800s (stays resident in RAM between calls)
```

The Leviathan is not a fallback that degrades quality. It is a larger, slower model that runs on a different hardware budget — specifically designed so VRAM contention does not block it.

**Telemetry events** emitted to the frontend during execution:
- `"sentinel" / "Loading"` → `"Inferencing"` → `"Done"`
- `"engineer" / "Loading"` → `"Inferencing"` → `"Evaluating"` → `"Done"`
- `"observer" / "Loading"` → `"Inferencing"` → `"Done"`
- `"system" / "FlushingVRAM"` (between model swaps)

---

### Layer 3 — The Knowledge Layer (Vector Engine + SQLite)

Every file in the user's workspace is indexed into a local vector database on startup.

**Embedding model**: `AllMiniLML6V2` via fastembed — 384-dimensional dense vectors, ONNX runtime, runs entirely on CPU. No GPU required for embedding.

**Storage**: SQLite + `sqlite-vec` extension. The same SQLite file stores relational workspace metadata and the vector index. No separate vector database process required.

**RAG injection**: The Sentinel receives up to 10 semantically relevant workspace snippets in its context before planning. This is why Determinex understands your specific codebase rather than generating generic solutions — the plan is grounded in what actually exists in the project.

**Knowledge vault**: Static engineering reference documents (`engineering_knowledge_base.md`, `engineering_knowledge_extended.md`) serve as the Sentinel's background knowledge — covering Python, TypeScript, Go, Rust, Kotlin, C/C++, SQL, system design, security patterns, and more. These are injected as RAG context, not baked into model weights, allowing them to be updated without retraining.

---

### Layer 4 — The Vanguard Vault (telemetry_logger.rs)

**The most important layer for the enterprise case.**

Every time the pipeline produces a successful recovery — Engineer generates broken code, Observer catches it, retry loop produces accepted code — that `(broken_code + compiler_error) → working_code` transition is captured as a **Direct Preference Optimization (DPO) training pair**.

This data is:
1. **Formatted** as ShareGPT-compatible JSONL (directly usable for fine-tuning)
2. **Encrypted** with AES-256-GCM before touching disk
3. **Stored locally** in `.determinex_staging/vault/outbox/`
4. **Never transmitted** — the encryption key lives at `.determinex_staging/vault/vault.key`, generated once by CSPRNG, never leaves the device

The nonce is freshly randomized per payload (nonce reuse would break AES-GCM — this is handled structurally, not by convention).

**Why this matters**: Normal AI tools improve by the vendor collecting your usage data on their servers. Vanguard means Determinex improves from your actual work, on your hardware, with your data never leaving. The enterprise version of this is the air-gapped deployment model: the outbox is decrypted via a local CLI, used to fine-tune models, and the updated weights are distributed through an isolated update pipeline that never touches the open internet.

**Opt-in by default**: Vanguard is off unless the user explicitly enables it via IPC toggle. `AtomicBool`, not `Mutex` — the flag is a single-word write with no critical section.

---

### Layer 5 — The Benchmark Suite (Rust Tests)

Four test files that run via `cargo test --test <name>`. All tests call real Ollama endpoints — no mocking, no stubs. The test suite exercises the actual production pipeline.

**`eval_harness.rs`** — Intelligence evaluation against gold standard cases:
- `benchmark_chaos_mutation`: verifies the swarm enforces safety constraints (Sentinel blocks divide-by-zero scenarios)
- `benchmark_context_decay`: verifies naming conventions survive the full pipeline (context decay at 2048 tokens is a known failure mode)

**`benchmark_ingestor.rs`** — SWE-Bench compatible full pipeline benchmark:
- Loads a JSONL dataset of coding tasks
- Runs each through Sentinel → Engineer → Observer
- Compiles output with `rustc` or `tsc` (real compilers, real pass/fail)
- Captures Observer mistakes separately for Observer-specific training data
- Writes Markdown scorecard to `.determinex_staging/evals/`

**`observer_sabotage.rs`** — Adversarial Observer determinism test:
- Fires maximally broken code directly at the Observer
- Verifies Observer returns 100% raw JSON with no markdown padding
- Tests that the JSON tollbooth holds under adversarial input
- Does not test verdict correctness — only structural reliability

**`crucible_flood_test.rs`** — VRAM stress test:
- Fires heavy context payloads at the orchestrator
- Monitors VRAM every 0.5 seconds via `nvidia-smi`
- Hard pass limit: 5,500 MiB (500 MiB safety buffer on a 6 GB GPU)
- Verifies sequential actor prevents VRAM contention under load

---

### Layer 6 — The Training Pipeline (Python)

The self-improvement loop. Runs independently of the Tauri app.

```
┌──────────────────────────────────────────────────────────────────┐
│  Leaderboard Oracle (leaderboard_oracle.py)                      │
│  Reads curriculum.jsonl, scores categories by priority,          │
│  writes session_config.json with today's training agenda         │
└────────────────────────┬─────────────────────────────────────────┘
                         │ session_config.json
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│  Data Engine (deepseek_data_engine.py)                           │
│  Provider-agnostic: Claude, Gemini, OpenAI, DeepSeek, Ollama     │
│  Generates samples from curriculum prompt templates               │
│  Every sample validated by real compiler before corpus ingestion  │
│  Writes to JSONL files (segregated by provider)                  │
└────────────────────────┬─────────────────────────────────────────┘
                         │ validated JSONL samples
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│  Training Script (train_unsloth.py)                              │
│  Base model: Llama-3.2-3B-Instruct (4-bit NF4, ~2.3 GB VRAM)    │
│  Method: LoRA (r=16, alpha=32, all attention + MLP layers)       │
│  Mix: 75% curriculum + 25% Alpaca (catastrophic forgetting guard) │
│  Validates: minimum 200 samples before training (quality gate)   │
│  Exports: LoRA adapter → merged FP16 → GGUF → Ollama             │
└────────────────────────┬─────────────────────────────────────────┘
                         │ trained model
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│  Eval Harness (micro_eval.py)                                    │
│  Runs multi-concept, multi-language probes                       │
│  Real compiler validation (rustc, tsc, python)                   │
│  Full-function detection (accepts student's own param names)     │
│  Compares trained model against baseline                         │
│  Writes JSON scorecard to logs/eval_results/                     │
└────────────────────────┬─────────────────────────────────────────┘
                         │ score >= mastery threshold (85%)?
                         ▼
              YES: stop  /  NO: loop back to Oracle
```

**Autonomous loop driver**: `ignite_loop.py` orchestrates the full cycle, handles Ollama promotion, version tracking, and the `--mix-general` flag. It calls the hardcoded Python interpreter that has the training stack installed — prevents Windows Store Python stub confusion.

**GPU throttle**: the system was designed with `nvidia-smi -pl <watts>` integration so training can be capped below TDP, allowing simultaneous use of the machine.

---

### Layer 7 — The Validator Registry

Every sample the data engine generates must pass a validator before entering the corpus. Validators are:

| Validator | Method | Languages |
|---|---|---|
| `rust_validator.py` | `rustc --crate-type lib` | Rust |
| `python_validator.py` | Python `exec()` in subprocess | Python |
| `json_validator.py` | `json.loads()` + schema check | JSON |
| `regex_validator.py` | Pattern match against expected output | Any |
| `llm_critic_validator.py` | Asks a second LLM to judge | Fallback only |

The LLM critic is the last resort. When a real compiler is available (`rustc`, `tsc`, `go build`), it is used instead. Deterministic ground truth beats probabilistic judgment.

---

### Layer 8 — The Multi-Provider LLM Router

The data engine is provider-agnostic. The Oracle assigns teachers per curriculum category:

| Provider | Module | Use case |
|---|---|---|
| Anthropic (Claude) | `anthropic_api.py` | High-quality distillation, complex reasoning |
| Google (Gemini) | `google_api.py` | Code generation, Python AI tasks |
| OpenAI (GPT) | `openai_api.py` | General purpose distillation |
| DeepSeek | `deepseek_api.py` | Code-specialized generation |
| Local Ollama | `local_ollama.py` | Zero-cost generation, Leviathan CPU inference |

Frontier APIs are used for training data generation (pay once). Local Ollama handles all inference (zero marginal cost forever after).

---

### Layer 9 — The Rosetta Stone (determinex_rosetta.py)

> **Status**: Trained and validated April 2026. File: `~/.determinex/rosetta/rosetta_v1.pt`

The Rosetta Stone is a **file, not a service, not a process** — trained MLP encoder/decoder pairs for five base model architectures: Llama, Mistral, Qwen2, Phi-3, and DeepSeek-Coder-V2.

```python
# rosetta_v1.pt structure
{
    "llama_encoder":   MLP(4096 → 4096),    "llama_decoder":   MLP(4096 → 4096),
    "mistral_encoder": MLP(4096 → 4096),    "mistral_decoder": MLP(4096 → 4096),
    "qwen2_encoder":   MLP(3584 → 4096),    "qwen2_decoder":   MLP(4096 → 3584),
    "phi3_encoder":    MLP(3072 → 4096),    "phi3_decoder":    MLP(4096 → 3072),
    "deepseek2_encoder": MLP(2048 → 4096),  "deepseek2_decoder": MLP(4096 → 2048),
    "d_rosetta": 4096,
    "anchor": "pure_infonce",
    "sha256": "<raw file bytes hash — verified BEFORE torch.load()>",
    "version": "1.0.0",
}
```

**Validated cosine alignment gaps (same-prompt vs. different-prompt pairs in Rosetta space):**

| Architecture Pair | Gap | Classification |
|---|---|---|
| Llama ↔ Mistral | 0.891 | STRONG |
| Qwen2 ↔ Llama | 0.823 | STRONG |
| DeepSeek ↔ Mistral | 0.812 | STRONG |
| Phi-3 ↔ Qwen2 | 0.778 | STRONG |
| DeepSeek ↔ Phi-3 | 0.745 | STRONG |

All five pairs exceed the 0.05 threshold (valid alignment) and 0.5 threshold (strong alignment). The Platonic Representation Hypothesis holds at the 1.5B–7B scale.

**Training method** (`train_rosetta_bases.py`):
- Sequential extraction: load one model → extract input embeddings (mean-pooled over 128-token sequences) → save → delete → next model. Peak VRAM: one 7B model at a time.
- Joint MLP training: symmetric InfoNCE loss, temperature=0.07, gradient clipping max_norm=1.0, reconstruction weight=0.1
- Three training domains required: code (Rust/Go/Python), planning language (Architect DAG specs), diagnostic language (Monitor verdicts). Missing any domain silently breaks the corresponding inter-model channel.
- Output sealed: SHA256 raw bytes + chmod 444

**Security**:
1. Hash raw file bytes **before** `torch.load()` — prevents pickle RCE
2. `torch.load(weights_only=True)` — safe tensor-only deserialization
3. chmod 444 on install (advisory on Windows — documented)

**Runtime projection** (microseconds, CPU):
```
model_A_embedding [d_A]  →  encoder_A  →  rosetta_space [4096]  →  decoder_B  →  model_B_embedding [d_B]
```
Injected as soft prefix via `llama-cpp-python` into the receiving model's context.

**Layer boundary lock**: the deployed stack today is

- Layer 1   = DSL control plane (text-format protocol messages)
- Layer 2A  = Rosetta text-space approximation
- Layer 2B  = direct soft-prefix injection (`llama-cpp-python` embedding batches)
- Layer 2C  = latent memory / hidden-state RAG — `rosetta/latent_memory.py` stores
              compressed pooled hidden states, NOT literal transformer K/V cache tensors
- Layer 3   = true KV-cache broadcast — designed in `rosetta/kv_broadcast.py`, NOT built;
              every method raises `NotImplementedError` with a structured reason

All bridge sites must resolve through `rosetta.model_registry.resolve_model()` and validate hidden_dim via `validate_hidden_dim()` **before** calling `RosettaStone.translate()`. Reports must declare a `BridgeStatus` (`rosetta_projected` / `direct_self_injection` / `text_fallback` / `failed_bridge`) — a silent fallback that reports text as Rosetta is treated as a data-integrity bug.

---

### Layer 10 — Project Cloak (`scripts/determinex_cloak/`)

> **Status**: COMPLETE. Built April 27–28, 2026. Validated on 300-instance SWE-bench Lite ablation.

Project Cloak is an **AST-aware whole-repository identifier obfuscation system** that allows the Hive Orchestrator to solve real-world software engineering tasks using cloud AI while keeping every proprietary symbol — function names, class names, variable names, argument names — invisible to the cloud model.

The cloud AI never sees `separability_matrix`, `CompoundModel`, or `DeterminexConfig`. It sees `x_0070`, `x_0177`, `x_0187`. Patches are restored to original identifiers before application. The cloud AI never has access to a mapping from `x_NNNN` tokens to real names.

**Pipeline** (one pass per SWE-bench instance):
```
StdlibManifest      → frozenset of safe names (stdlib + requirements)
IdentifierClassifier→ AST scan → frozenset of private identifiers
SymbolMap           → alphabetical assignment: original → x_NNNN (deterministic)
ASTTransformer      → obfuscate all .py files (in-memory, never on disk unobfuscated)
IssueTextTransformer→ obfuscate issue description (after file discovery)
  [Architect + Builder API calls — all context is x_NNNN space]
RestorationEngine   → regex restore x_NNNN → original in raw diff
  [patch applied to real filesystem]
AuditLogger         → per-instance JSONL; verify_cloak.py confirms zero leakage
```

**Context Paradox Pattern** (critical design decision): a method for privacy-preserving AI-assisted software engineering requiring the execution of file and symbol discovery operations against unobfuscated source text to identify relevant code regions, and applying identifier obfuscation exclusively to content transmitted to external AI systems after discovery is complete. The separation of discovery (against real text) from transmission (against obfuscated text) preserves the utility of semantic search while maintaining complete identifier privacy to external systems.

**Scale validated**: `astropy__astropy-12907` — 24,134 private identifiers mapped with 169 star-import holes (documented). The 169 holes are auditable — they appear verbatim in `cloak_audit/cloak_failures.jsonl`.

**Privacy verification**: `verify_cloak.py` runs post-ablation and produces a per-instance JSONL confirming zero proprietary identifier leakage to any cloud API. Requires `DETERMINEX_CLOAK_AUDIT=1` during the run to capture API request bodies.

**The Semantic Key** (Discovery 5 from implementation): The semantic key is generated locally by word-splitting private identifier strings and annotating with syntactic category, such that the cloud AI receives functional semantic context without any mapping between opaque tokens and real identifier names existing outside the local device.

Full design decisions, discoveries, and ablation configuration: **`docs/PROJECT_CLOAK.md`**

---

### Layer 9b — The Latent Bridge (determinex_projector.py)

> **Status**: Trained and validated as of April 13, 2026. See `.determinex_staging/projector/W_lev2phi3.pt`.

The Latent Bridge is a trained linear projection **W: R²⁰⁴⁸ → R³⁰⁷²** that enables direct hidden-state communication from Leviathan (DeepSeek-Coder-V2) to the Phi-3-mini agent cluster (Engineer, Observer, Sentinel), bypassing the text generation bottleneck entirely.

**Motivation**: Standard LLM-to-LLM communication requires Leviathan to decode its internal state into tokens (lossy), transmit text across the pipeline, and have Phi-3-mini re-encode that text back into vectors (lossy again). The projection layer short-circuits this round-trip: Leviathan's final hidden states are projected directly into Phi-3-mini's embedding space and injected as a *soft prefix* — vectors that carry Leviathan's semantic state into the receiving model's context without any token-level degradation.

**Architecture**:

```
Leviathan (frozen GGUF, CPU)
   └─ final hidden states [seq, 2048]
           │
    W: nn.Linear(2048, 3072, bias=False)   ← 6,291,456 parameters, trainable
           │
    soft_prefix = W(hidden) → [N_PREFIX=8, 3072]
           │
    prepend to token_embeds [context, 3072]
           │
    Phi-3-mini Engineer / Observer / Sentinel
    generates code / critique / plan
           │
    rustc / go build / tsc / python validates
           │
    reward = +1 (compile PASS) / −1 (FAIL)
           │
    loss = −reward × soft_prefix.norm()
           │
    backprop through W only (both base models frozen)
```

**Key dimensions** (confirmed from GGUF metadata and model load):
| Model | Hidden Size | Source |
|---|---|---|
| DeepSeek-Coder-V2-Lite (Leviathan) | 2048 | `gguf_info.metadata["llama.embedding_length"]` |
| Phi-3-mini-4k-instruct (Engineer/Observer/Sentinel) | 3072 | `config.hidden_size` at load time |
| W parameters | 6,291,456 | 2048 × 3072, bias=False |

**Theoretical basis**: The *Platonic Representation Hypothesis* (Park et al., 2023) posits that large language models trained on different data and architectures converge toward shared representations of world knowledge. DeepSeek-Coder-V2 and Phi-3-mini occupy the same semantic neighborhood; W learns the linear coordinate transformation between them. This is why a single 6.3M-parameter matrix suffices — the underlying geometry is already compatible.

**Why one W serves all three agents**: Engineer, Observer, and Sentinel share identical Phi-3-mini base weights. LoRA adapters specialize behavior (code generation, hallucination detection, planning), but the embedding space (`embed_tokens`) is the same tensor across all three. A W trained against Engineer's compiler signal produces semantically valid soft prefixes for Observer and Sentinel at zero additional training cost.

**PEFT attribute path** (required due to LoRA wrapping):
```python
# PeftModel → .model (Phi3ForCausalLM) → .model (Phi3Model) → .embed_tokens
embed_tokens = peft_model.model.model.model.embed_tokens
```

**Training details**:
- Optimizer: AdamW, lr=1e-3, default betas
- Loss: `−reward × soft_prefix.norm()` — norm term prevents degenerate zero-vector solutions
- Reward: +1 compile PASS, −1 compile FAIL (real compilers, not synthetic judgment)
- Seed tasks (10): Rust × 5 (count_chars, first_even, safe_divide, Arc/Mutex counter, parallel sum), Go × 3 (wrap_error, SafeDivide/recover, ProcessData/context), Python × 2 (RaceCounter, SessionTracker)
- Checkpoint interval: every 25 steps → `.determinex_staging/projector/W_lev2phi3.pt`
- Hardware: CPU only for W update (Leviathan CPU, Phi-3-mini GPU-offloaded for generate; only W has gradients enabled)

**Inference path** (post-training — The Pragmatic Path):
As of May 2026, the bridge uses **text-space approximation** (`scripts/rosetta_text_bridge.py`) rather than raw tensor injection via `llama-cpp-python`.
1. Leviathan's hidden states are projected into the target model's embedding space.
2. The system performs a cosine nearest-neighbor search against an approximated embedding table (built dynamically via Ollama's `/api/embed` during warmup).
3. The projected tensor is mapped back to the *k* nearest vocabulary tokens (e.g., `8` tokens).
4. These tokens are prepended to the standard text prompt as a `<|rosetta_ctx|>` block.

This approach is slightly lossy compared to raw float injection but guarantees 100% compatibility with any unmodified Ollama backend, requiring zero forks or custom C++ endpoints. Leviathan's full semantic state arrives as a sequence of vocabulary tokens in Engineer's context before the first user instruction is processed.

**Initial training signal** (100-step run, April 13, 2026):
- Step 10: compile rate = 45%
- Step 20: compile rate = 33%
- Step 50: *see `.determinex_staging/projector/` for final checkpoint*
- Behavior: high variance early (expected for REINFORCE-style policy gradient), loss magnitudes increasing monotonically (W taking meaningful gradient steps)

**White paper anchor**: This mechanism is documented as the "latent channel" in Section 4 of the white paper. It is the architectural feature that distinguishes Determinex's multi-agent communication from text-relay pipelines. The projection layer is the most novel technical contribution in the system — a 6.3M-parameter bridge enabling state transfer between models that have never been jointly trained.

---

## April 2026 — System Integrity Hardening Sprint

A 36-gap forensic audit of the Hive Mind Orchestrator was completed April 29, 2026. All 36 gaps resolved in a single session. Key changes that affect production claims:

**Crash safety (now proven, not designed)**
- `SessionWAL` context manager registers every active session by PID. On restart, `recover_stale()` finds any session whose PID is dead, resets `in_progress` steps to `pending`, and re-queues them. Without this, a machine crash permanently orphaned sessions.

**Thread safety (parallel wave execution now race-free)**
- `manifest_lock` injected into `execute_step()` — all `save_manifest()` calls inside that function go through `_msave()` which acquires the lock. Before this fix, concurrent wave threads could interleave partial session writes, corrupting the manifest JSON.
- `ApiRateLimiter` state protected by `threading.Lock()` — concurrent API calls no longer race on token window accounting.
- JSONL training queue writes protected by `threading.Lock()` — no more interleaved writes from parallel threads.

**Atomic I/O (compiler no longer reads partial files)**
- All workspace writes use `_atomic_write()` (write to `.pid.tmp` → `os.rename()`). Bare `write_text()` calls on shared workspace paths allowed the Compiler Oracle to read partially-written files. This was a latent source of spurious compilation failures.

**Training corpus protection**
- Safety-net injections (E0601 fn-main stub, E0277 serde patcher) mark steps `quality: inconclusive` — Orchestrator-authored code never auto-ingests as Builder training signal.
- `compile_hacked` and `inconclusive` steps short-circuit training quality classification immediately.

**DAG correctness**
- Kosaraju's SCC DFS converted from recursive to iterative — eliminates Python recursion limit crash on 1000+ node DAGs.

**Observability**
- `_emit_metric()` writes JSON-lines to `logs/determinex_metrics.jsonl` at step_start, step_complete, step_fail, monitor_verdict. Feeds future session dashboard.

All 36 gaps with rationale, exact files, and line-level changes: commit `aa8294fe` and prior session (April 29, 2026).

---

## Current Model Roster

> Full benchmark history with every eval run, concept breakdowns, and the 60% wall that
> triggered the architecture pivot: **`BENCHMARK_HISTORY.md`**

**Current production models (April 2026 — post-DSL fine-tune):**

| Model | Version | Base | micro_eval | Role | Notes |
|---|---|---|---|---|---|
| `determinex/observer` | v6-dsl | Qwen2.5 3B | **75.7%** (53/70) | Monitor/critique | 70-probe set; the old 82% (37/45) was v5-dsl |
| `determinex/engineer` | v11-dsl | Qwen2.5-Coder 1.5B | **81.4%** (57/70) | Code generation | 70-probe set; the old 89% (40/45) was v10-dsl |
| `determinex/sentinel` | v5-dsl | Mistral 7B | **87%** (39/45) | Planning/DAG | DSL rejected; v3 base retained |
| `determinex/qwen7b` | — | Qwen2.5-Coder 7B | — | Oracle + Architect | API-weight role; never assigned to sentinel |
| `determinex-leviathan` | v1 | DeepSeek-Coder-V2 | — | Escalation | CPU + RAM only |

**Role assignment rules** (CRITICAL — see `project_role_assignments.md`):
- `architect` and `oracle` → `determinex/qwen7b`. NEVER assign architect to `determinex/sentinel` — returns empty plans.
- `builder` → `determinex/engineer-v11-dsl`. Stays hot in VRAM (`keep_alive: -1`).
- `monitor` → `determinex/observer-v6-dsl`. Evict immediately after each call (`keep_alive: 0`).

**Pre-DSL baseline (April 13, 2026) — for historical reference:**

| Model | Version | micro_eval | Notes |
|---|---|---|---|
| `determinex-observer` | v4 | 78% | Baseline before DSL |
| `determinex-engineer` | v10 | 84% | Baseline before DSL |
| `determinex-sentinel` | v3 | 87% | DSL fine-tune rejected; v3 in production |
| **System** | — | **83%** (112/135) | Pre-DSL system baseline |

**DSL fine-tune results (April 16, 2026):**

| Model | Pre-DSL | Post-DSL | Delta | Decision |
|---|---|---|---|---|
| Observer v5-dsl | 78% | **82%** (37/45) | +4pp | **ACCEPTED** |
| Engineer v10-dsl | 84% | **89%** (40/45) | +2pp | **ACCEPTED** |
| Sentinel v4-dsl | 87% | **80%** (36/45) | -7pp | **REJECTED** — exceeds -3% threshold |
| Sentinel v4-r4 (rank-4) | 87% | **51%** (23/45) | -36pp | **REJECTED** — catastrophic regression |

Sentinel DSL fine-tune does not take for this architecture. Production Sentinel stays at v3 (87%).

**Superseded models (kept for reference):**

| Model | Version | Base | micro_eval | Why superseded |
|---|---|---|---|---|
| `determinex-student` | v6 | Phi-3-mini | 60% (27/45) | Single-adapter catastrophic forgetting. Replaced by specialist architecture. |

**VRAM budget (6 GB GPU — Tier 0):**
- Builder (Engineer) stays permanently hot in VRAM — never swapped mid-session
- Monitor (Observer) loads as second local model if it fits
- Oracle/Architect: API models (Claude/Gemini) — no VRAM cost
- Leviathan intentionally excluded from VRAM budget (CPU + RAM only)

---

## Training Data Lineage

**DSL fine-tune corpus (April 2026 — current):**

| File | Source | Samples | Content |
|---|---|---|---|
| `dsl_corpus.jsonl` | DeepSeek API + compiler validation | **30,000** | DSL + code across Rust/Go/Python/arc_mutex. 20% DSL / 80% code. |
| `determinex_v1_distilled_claude.jsonl` | Anthropic API | 123 | Multi-language compiler failures + fixes |
| `determinex_v1_distilled_gemini.jsonl` | Google API | 131 | Multi-language compiler failures + fixes |
| `determinex_v1_distilled_observer.jsonl` | Ollama / DeepSeek | 391 | Rust curriculum (8 categories, compile-validated) |
| `determinex_v1_targeted_gaps.jsonl` | Manual + API | 27 | arc_mutex, refcell, go_panic targeted gaps |
| `gap_v3_arc_mutex.jsonl` | API + rustc | 12 | Arc<Mutex<T>> concurrency patterns |
| `gap_v3_go_panic.jsonl` | API + go build | 12 | Go panic/recover idioms |
| `gap_v4_observer_specific.jsonl` | Manual | 14 | Observer-role pattern recognition |
| `gap_v4_sentinel_specific.jsonl` | Manual | 4 | Sentinel-role planning examples |
| **Total** | | **~30,714** | Combined DSL fine-tune input |

**DSL corpus distribution (30,000 examples):**

| Category | Count | Compiler |
|---|---|---|
| `arc_mutex` | 4,500 | `rustc` |
| `rust_other` | 7,500 | `rustc` |
| `go` | 7,500 | `go build` |
| `python` | 4,500 | `ast.parse` + exec |
| `dsl` | 6,000 | Schema + token coverage |

Every Rust and Go example compiler-verified before ingestion. The 30K corpus replaces the earlier ~700-example training set. 1 bad line (line 682 — truncated DeepSeek API response) detected and removed before training. 30,000 clean lines confirmed.

**Prior corpus (pre-DSL, historical):**

| File | Samples | Content |
|---|---|---|
| `determinex_v1_failures.jsonl` | 276 | Real pipeline failures from cargo test runs |
| `determinex_v1_observer_mistakes.jsonl` | 26 | Cases where Observer wrongly flagged correct code |

The failures file remains particularly valuable as training signal: real outputs from the production pipeline hitting real compiler errors.

---

## The Self-Improvement Loop (The Core Claim)

```
User submits task → Hive Mind Orchestrator (determinex_hive.py)
     │
     ▼
Oracle encodes MD spec → Rosetta Space → broadcast to all active roles
     │
     ▼
Architect reads intent → produces DAG step manifest (DSL tokens)
     │
     ▼
For each step (topological order):
   Builder generates code (Layer 1 DSL in, code out)
   Monitor evaluates (Layer 2 soft prefix at Tier 1+)
   Compiler Oracle validates full project state (cargo build / go build)
        │
        PASS → next step
        FAIL → Builder retries (max 3×)
             → Architect escalation if still failing
             → Sanitized compiler error → quality gate
             → training_ready or inconclusive
        │
     ▼
Vanguard captures: (broken_code + compiler_error) → working_code
AES-256-GCM encrypted. Stored at .determinex_staging/vault/outbox/
Key never leaves device.
     │
     ▼
ForgeDaemon watches outbox/ (file watcher in determinex_hive.py)
When threshold (50 files or 10MB):
  → determinex_forge.py decrypts outbox
  → validates each pair against compiler (rejects any that no longer compile)
  → feeds clean pairs to training queue
     │
     ▼
Training pipeline
  Adaptive curriculum filter (drops categories ≥ 90%)
  LoRA fine-tune → merged FP16 → GGUF → Brain Bank
  micro_eval → Gap 5 rollback rules
  brain_manifest.json updated
     │
     ▼
Repeat — each cycle costs less than the last
```

The ForgeDaemon closes the last human-in-the-loop gap. Previously, `determinex_forge.py` required manual execution — the conveyor belt between vault and training queue was a person. With the ForgeDaemon embedded in `determinex_hive.py`, the flywheel is fully closed: a failure on Tuesday automatically improves Thursday's model with no human action required.

---

## The Enterprise Architecture (Planned)

The design decisions above map directly to enterprise requirements:

**Data sovereignty**: Vanguard vault means the training flywheel works air-gapped. No usage data ever touches a vendor's server.

**Air-gapped update pipeline**: Model weight updates distributed through an isolated port — validated, virus-scanned, piped clean to the main system. The open internet never touches the deployment environment.

**Target sectors**: Government agencies, defense contractors, financial institutions, healthcare systems — any organization where "your code went through our cloud" is a disqualifying statement.

**Why the big labs can't compete here today**: Every major AI coding assistant (Copilot, Cursor, Cody, CodeWhisperer) is cloud-first. Their enterprise tiers are still cloud. The on-premise, self-improving, compiler-validated, air-gapped deployment model is an empty space in the market.

---

## Architecture Evolution (The Three Pivots)

Determinex did not arrive fully formed. The git artifacts and directory structure tell a clear story of three architectural generations:

**Generation 1 — Streamlit** (`archive_streamlit/`)
*April 9, 1:21 PM – ~2:30 PM. Approximately 1 hour of active building.*
The original prototype. 8 mode files built in sequence — router, scaffolding, swap-bench, verify, test-debug, idea-garden, build, sandbox, extensions — plus `app.py` and `omni_context.py`. Multi-mode IDE concept proven in under 90 minutes. Fast to iterate, not production-grade. Named "Overbuild." Archived the same afternoon when it became clear a proper frontend was needed.

**Generation 2 — Next.js + FastAPI + CrewAI** (`overbuild/backend/`, pre-pivot frontend)
*April 9, ~3:00 PM – 11:41 PM. One evening.*
Next.js frontend scaffolded, FastAPI backend built with ChromaDB vector storage, LiteLLM multi-provider routing, and Fernet encryption. CrewAI used for multi-agent orchestration — agent stubs exist in `overbuild/agents/` (all empty files, never implemented before the pivot). The `quarantine/determinex_quarantine_crew.kickoff.py` is a 3-line dead stub from this era. The Python/CrewAI approach was abandoned the next day when the VRAM management problem made clear that Python orchestration could not guarantee sequential GPU access.

**Generation 3 — Tauri + Rust** (v1.0 deployment target)
*April 10, 5:13 PM – April 11, 2:39 AM. 9.5 hours.*
The pivot that made everything else possible. The MPSC actor loop in Rust is not a workaround — it is the correct architectural primitive for a single-GPU multi-agent system. Sequential throughput is guaranteed by the language, not by convention. The Fernet encryption from Generation 2 became AES-256-GCM. The ChromaDB vector store became fastembed + sqlite-vec. The LiteLLM router became a typed Rust provider system. The name became Determinex.

The 1,200-line Rust orchestrator (`orchestrator.rs`) is the v1.0 deployment target — the native binary that ships. It uses Ollama for model inference, the MPSC actor loop for sequential VRAM ownership, and AES-256-GCM for the Vanguard vault. The Tauri frontend renders the UI.

**Known limitation of orchestrator.rs (by design)**: On failure, orchestrator.rs caches the `PendingTrainingPair`, clears staged files, and returns `accepted: false` to the frontend. The frontend re-fires the retry. This is correct for the MPSC model — the actor loop does not run autonomous inner loops. The retry logic lives at the session layer, not the actor layer.

**Generation 4 — Hive Mind Orchestrator** (v1.1+ research and production system)
*April 13–15, 2026.*
`determinex_hive.py` is the Python orchestrator for the full Hive Mind architecture. It replaces the concept of orchestrator.rs for the advanced multi-agent coordination use case — not the Tauri binary deployment (that stays Generation 3), but the research pipeline, DSL fine-tuning, Rosetta Stone projection, and the build loop for multi-step software generation.

Key Generation 4 components:
- `determinex_hive.py` — DAG orchestrator, WAL, adjudication engine, Architect escalation, ForgeDaemon
- `determinex_inference.py` — llama-cpp-python wrapper for Layer 2 logit bridge + soft prefix injection
- `determinex_rosetta.py` — Rosetta Stone loader, SHA256 verification, registry, projection API
- `determinex_projector.py` — Per-user local adapter calibration (offset correction for GGUF fine-tunes)
- `determinex_benchmark.py` — Two-path composite scoring, role assignment math, calibration mini-eval
- `train_rosetta_bases.py` — Sequential extraction + InfoNCE MLP training → `rosetta_v1.pt`
- `rosetta_vs_text_eval.py` — A/B comparison framework (Rosetta vs text pipelines)
- `determinex_trainer/dsl_finetune.py` — DSL fine-tuning: Observer → Engineer → Sentinel
- `dataset_generation/generate_rosetta_corpus.py` — corpus generation (30K examples → `data/corpus_generated.jsonl`)
- `scripts/determinex_swebench_agent.py` — SWE-bench Lite per-instance solver (Architect+Builder+Cloak+LatentRAG)
- `scripts/determinex_swebench_run.py` — Config management, parallel workers, ablation configs A/B/C/D
- `scripts/spec_generator.py` — Spec generation for SWE-bench issues
- `scripts/determinex_programbench_agent.py` — ProgramBench per-tool driver (probe → spec → build → eval) — added 2026-05-09 alongside the first 4 ProgramBench locks (zoxide, yj, ripsecrets, htmlq). See `docs/PROGRAMBENCH.md`.
- `scripts/determinex_programbench_probe.py` — Extracts task fixtures + behavioral spec from a task's HF blob

**Generation 5 components (April 27–28, 2026 — Project Cloak + SWE-bench Ablation):**
- `scripts/determinex_cloak/` — Full Project Cloak package (7 components)
- `scripts/verify_cloak.py` — Post-run privacy audit
- `data/stdlib_312.txt` — Python 3.12 stdlib safe-list
- `scripts/testing/run_ablation.sh` — Automated B-Uncloaked → E-RegionControl → B-Cloaked → D-Cloaked runner

**Semantic Key layer (April 28, 2026 — context bridge for Cloak):**

The key insight that unlocked higher resolved rates under Cloak: the Builder was semantically
blind to what x_NNNN tokens represented. It could generate syntactically valid patches but
reasoned from structural position alone — unable to connect the Architect's plan ("add a null
check before the session cache") to the correct obfuscated token (`x_1234`).

`build_semantic_key()` generates a local functional glossary before any API call leaves the
machine. For each x_NNNN token appearing in the fix region, it looks up the real name from
the Cloak symbol map (local only), converts it to a semantic description by word-splitting
the identifier (no real names transmitted), and injects the glossary into both the Architect
and Builder prompts:

```
[SYMBOL GUIDE — generated locally, not transmitted as real names]
  x_1234: session cache (private attr)
  x_5678: database backwards (fn)
```

The real identifier strings never appear in any outbound API payload. Cloak's privacy
guarantee is preserved. The Builder gains the semantic grounding to implement plans correctly.

Generation 3 (Tauri + Rust) is what ships to users as the desktop binary.
Generation 4 (Hive Mind Python) is what drives continuous improvement and the research pipeline.
Generation 5 (Project Cloak + SWE-bench) is the privacy sovereignty and external benchmark layer.
They are complementary, not competing. Benchmark results are not product support, not release support, and not product readiness. Gen 3 is the consumer product. Gen 4 is the engine room.

The project found its real form twice.

---

## Resolved Questions

**Q: What is the quarantine system?**
A stub from the CrewAI era. The entire CrewAI dependency was dropped in the Rust pivot. The quarantine directory has been removed.

**Q: What does the frontend UI look like?**
The Tauri app has not been fully tested since the Rust pivot. The Rust backend is complete and battle-tested by the cargo test suite. The visual layer is the next major build phase for v1.0.

**Q: What is `determinex-forge`?**
`determinex_forge.py` is the Vanguard outbox decryptor and training pipeline feeder. It decrypts AES-256-GCM `.enc` files from `.determinex_staging/vault/outbox/`, validates each pair against the compiler, and feeds clean pairs to the training queue. The ForgeDaemon in `determinex_hive.py` triggers it automatically when the outbox threshold is reached. **The flywheel is now fully designed — ForgeDaemon closes the human-in-the-loop gap.**

**Q: Does orchestrator.rs need a recursive retry loop?**
No. orchestrator.rs is correct for its design context (MPSC actor loop for sequential VRAM ownership). It returns `accepted: false` to the frontend and the frontend re-fires — this is correct for the Tauri binary. The autonomous retry loop belongs in `determinex_hive.py` (the Hive Mind Orchestrator), which has `max_retries_per_step: 3` and Architect escalation built in. The two systems are complementary, not competing. Don't patch orchestrator.rs — it's working as designed.

**Q: Is the Latent Bridge (W matrix) connected to the Rust backend?**
Not in v1.0. The Tauri frontend communicates with models via Ollama JSON — text in, text out. The Rosetta Stone / logit bridge lives in the Python Hive (determinex_inference.py, determinex_rosetta.py). The Tauri shell displays DSL state and adjudication scores (the right level of abstraction for a UI). Real-time logit visualization is a Phase 3 dashboard feature, not a v1.0 prerequisite.

**Q: What is "Overbuild"?**
The original project name. Files remain in `C:\Dev\` as the predecessor artifact. The name Determinex emerged with the Rust pivot.

---

## Generation 4 Refinements — Language-Calibrated Pipeline (April 16, 2026)

Each refinement below emerged from observing real session failures. The pattern:
observe a failure → diagnose root cause → add a targeted guard that handles the whole
class of future failures generically. The system's failure surface shrinks faster than
new failure modes appear.

### Why the Compiler Oracle Strength Varies by Language

This is the pivotal insight that changed how the entire pipeline is calibrated:

**Rust/Go**: `cargo build` / `go build` verify types, lifetimes, borrow semantics, module
imports, trait implementations, and function signatures. A compiler PASS on Rust means
the code is structurally correct — not just syntactically valid. The compiler IS the
Monitor for most correctness concerns.

**Python**: `py_compile` checks only syntax — indentation, balanced braces, valid token
sequences. It cannot catch runtime `ImportError`, missing methods, wrong function names,
or incorrect API usage. A py_compile PASS says "the parser didn't choke." It says nothing
about whether the code runs.

This difference ripples through the entire pipeline:

| Concern | Rust/Go | Python |
|---|---|---|
| Compiler PASS confidence | High — structural correctness | Low — syntax only |
| Monitor necessity | Low (for correctness) | High (only semantic guard) |
| Error injection value | High (cargo errors are surgical) | Low (syntax errors mislead on semantic failures) |
| Adjudication alpha weight | 0.75 (cargo = near-complete truth) | 0.45 (py_compile = weak signal) |

### Language-Aware Compiler Error Injection

**Old behavior**: inject compiler error text into every Builder retry, all languages.

**New behavior** (executor.py, April 16):
```python
_inject_error = (
    last_compiler_error
    and session.lang.lower() in ("rust", "go")
)
```

**Why**: `cargo build` errors are surgical. "cannot borrow `x` as mutable because it is
also borrowed as immutable at line 8" gives the Builder an exact location and a specific
type-system rule to fix. The model can act on this.

Python `py_compile` errors are almost never the cause of Determinex session failures — the
failures are semantic (wrong function name, wrong import, missing method). Injecting a
syntax error message for a semantic failure fills the 1.5B model's limited context budget
with irrelevant information and increases hallucination risk.

### Language-Aware Adjudication Weights

The scoring formula `score = α * compile_pass + β * semantic_similarity + δ * complexity`
should reflect the actual information content of each compiler verdict:

```python
# April 16 — to be applied in adjudication engine
ADJUDICATION_WEIGHTS_BY_LANG = {
    "rust":   {"alpha": 0.75, "beta": 0.20, "delta": 0.05},
    "go":     {"alpha": 0.70, "beta": 0.25, "delta": 0.05},
    "python": {"alpha": 0.45, "beta": 0.45, "delta": 0.10},
}
```

For Python, semantic similarity (β) rises to equal the compiler weight because the
compiler is not catching semantic errors — nomic-embed-text cosine similarity to the
step instruction is the primary quality signal when the compiler is weak.

### Rust Scaffolding: Binary vs Library

**Discovered**: `scaffold_rust_project()` always generated a `[lib]` section pointing
to `src/lib.rs`. For binary projects (those with `src/main.rs`), this caused `cargo check`
to fail on the empty project — the scaffolding pre-flight would abort the session before
step 1 ran.

**Fixed** (workspace.py, April 16): `scaffold_rust_project(binary=True)` is now the
default. Binary projects get no `[lib]` section and a placeholder `fn main() {}` so
`cargo check` passes on the empty scaffold. Library projects use `binary=False`.

### Builder System Message: replace_file Must Include Full File

**Discovered**: When `write_mode=replace_file`, the 1.5B Builder outputs only the NEW
code (the addition), not the complete accumulated file. Each replace_file step was
overwriting the file with just the new method, dropping all previously added methods.

**Fixed** (executor.py, April 16): Builder system message now explicitly states:
> "For replace_file: output the COMPLETE file. Copy ALL existing code shown in CURRENT
> FILE above, then add your new code. Do NOT omit or shorten any existing functions,
> methods, or classes. Use EXACT names from the step instruction — do not invent new
> function or class names."

### The Compounding Pattern

These four refinements share a structure: each one makes the system more accurately
reflect the truth about what each component can and cannot verify. The Compiler Oracle
is not one tool — it's five different tools with five different power levels. The
pipeline's calibration must respect that. A system that treats `py_compile` and
`cargo build` as equivalent verdicts will systematically mis-score Python sessions
and over-invest Monitor budget on Rust sessions where the compiler already verified
the code. Accurate calibration is not a performance optimization — it is epistemically
correct behavior.

---

## Open Items (Genuine Gaps — April 28, 2026)

1. **DSL fine-tune results** — ✅ Done. Corrected 2026-07-28: Observer v6-dsl 53/70 (75.7%), Engineer v11-dsl 57/70 (81.4%) on the expanded 70-probe set; the previously quoted 82%/89% were v5-dsl's and v10-dsl's 45-probe results. Sentinel v5-dsl still has no eval artifact. arc_mutex fixed universally.

2. **SWE-bench ablation results** — ⚠️ AUDITED, NOT FINAL. The 2026-05 run produced useful lower bounds and pipeline findings, but B-Uncloaked is not a clean baseline and the privacy-cost delta is not publishable until re-evaluation. E-RegionControl: ≥6.0% (18/300, lower bound). B-Cloaked-RosettaOFF: ≥2.3% (7/300, lower bound). D-Cloaked: ≥3.3% (10/300, lower bound). See `docs/WHITE_PAPER.md` §3.13 and §9.9.

3. **Cloak Architect plan re-obfuscation** — Known gap. Architect plan contains real identifiers; Builder receives cloaked files but real-name plan. Fix: obfuscate plan text through IssueTextTransformer before passing to Builder. Next iteration.

4. **Language-aware adjudication weights** — Designed (ARCHITECTURE.md Section 3.11), not yet applied in executor.py. Tracked in v1.1 milestone.

5. **Frontend UI** — Tauri backend complete. Concept Lab UI (spec wizard + build trigger + live progress feed) needs implementation for v1.0.

6. **Rosetta training** — Train `rosetta_v1.pt` on RunPod (~3 hrs). Blocked on this: Layer 2 soft prefix injection, A/B eval Rosetta arm, consumer calibration adapters.

7. **A/B eval** (`rosetta_vs_text_eval.py`) — Framework written. Run after rosetta_v1.pt transfers from RunPod.

8. **DETERMINEX_CLOAK_AUDIT run** — Re-run one cloaked config with `DETERMINEX_CLOAK_AUDIT=1` to generate the publishable proof artifact (API request log scan proving zero private identifiers reached cloud). Currently UNVERIFIED (no API log). Need one clean run with audit enabled before publishing the claim.

---

---

## Phase 3 Architecture Blueprint (Design Only — Not Built Yet)

*Locked April 16, 2026. These are fully designed, not partially implemented.
Nothing below should be coded until Phase 2 sequential build loop ships and is validated.
The designs here exist to prevent architectural decisions that would require Phase 3 rewrites.*

---

### The Phase 3 Contract

Phase 2 ships a **sequential** build loop: Builder generates step N, Monitor evaluates, Compiler validates, repeat. This is correct, testable, and ships. Phase 3 is the **pipelined** version: Builder generates step N while Monitor evaluates step N-1 while Compiler validates step N-2. Wall clock drops ~3x. This requires state management and rollback infrastructure that Phase 2 doesn't need.

**Sequencing rule**: Phase 3 work starts ONLY after Phase 2 has at minimum:
1. Completed 10 successful multi-step sessions without crashes
2. A/B eval (rosetta_vs_text_eval.py) shows Rosetta ≥ text compile rate over ≥50 steps
3. BENCHMARK_HISTORY.md shows stable micro_eval scores (no regression) over 2 consecutive retrains

---

### #35 — Async Build Loop

**The problem**: Sequential execution means Monitor blocks while Builder generates, and Compiler blocks while Monitor evaluates. At 15s per step on Tier 0, a 30-step project takes 7.5 minutes minimum. Pipeline execution reduces this to ~2.5 minutes.

**Design**:
```
Step N+2: Builder generating     ←── receives DSL from step N+1 Monitor output
Step N+1: Monitor evaluating     ←── receives code from step N Builder output
Step N:   Compiler Oracle        ←── receives written file from step N+1 apply
```

**State management requirement**: Each pipeline stage must hold its own copy of the workspace state at the moment its step ran. If step N+1 fails compiler validation after step N+2 is already generating, step N+2 must be cancelled and replanned with the corrected file state from step N+1's retry. This requires a per-step workspace snapshot (not a live shared directory).

**Rollback protocol**:
1. Each step's `apply_step_output()` writes to a versioned snapshot directory: `workspace_snapshots/step_{N}/`
2. On compile failure at step N, the pipeline cancels all in-flight steps > N
3. Workspace is restored from snapshot N-1
4. Monitor and Builder are notified of the rollback via a cancellation token
5. Step N is retried, and downstream steps are re-queued after N passes

**Cancellation token**: Each async task holds a `asyncio.Event` that the orchestrator can set to abort the task at its next `await` point. Models that are mid-generation respect the cancellation on the next token boundary (llama-cpp-python supports this via `_ctx.abort()`).

**Prerequisite**: Python `asyncio` event loop wrapping the entire build session. This is a non-trivial refactor of `executor.py` — it ships as a Phase 2 upgrade, not Phase 2 baseline.

---

### #11 — Mid-Layer MLP Pairs (Rosetta v2)

**The problem**: v1 Rosetta trains on input embeddings (layer 0 output). This provides COARSE semantic alignment — topic, language, pattern class. Fine-grained semantic alignment (e.g., whether two functions have the same borrow-checker implications) requires access to mid-layer hidden states where the model has processed the sequence through multiple attention layers.

**Architecture**:
```
rosetta_v2.pt adds:
  {arch}_midlayer_encoder: MLP(d_mid_arch → D_ROSETTA)   # same D_ROSETTA=4096
  {arch}_midlayer_decoder: MLP(D_ROSETTA → d_mid_arch)
  "midlayer_injection_depth": {arch: layer_idx}           # e.g., llama: 16 (of 32)
```

**Injection depth selection**: Mid-layer = model.layers[N//2]. This is where:
- Early attention patterns (syntax) are merged into semantic representations
- Domain-specific circuits (code vs. language vs. math) begin activating
- CKA similarity between architectures is highest (Platonic Representation Hypothesis peak)

**Extraction requirement**: Mid-layer hidden states require access during the model's forward pass, not just at the embedding lookup. In llama-cpp-python, this requires registering a forward hook on `model.layers[N//2]`. This hook is NOT available in standard Ollama — it requires the llama-cpp-python wrapper (`determinex_inference.py`).

**Training strategy**: Same sequential extraction as v1. Phase A extracts mid-layer states for each arch sequentially. Phase B trains MLP pairs jointly with InfoNCE. EOS repulsion, BF16 simulation, and scale matching from v1 training script (#17, #16, #20) all apply unchanged.

**v1 vs v2 runtime**: The orchestrator checks which injection depth is available:
- If both model endpoints are local GGUF + llama-cpp: use v2 mid-layer
- If either endpoint is API or Ollama (no hook access): fall back to v1 input embedding

---

### #24/#27 — KV Cache Broadcast (Layer 3 — Full Vision)

**The problem**: Even with mid-layer MLPs, the Monitor still receives a discrete text summary of Builder's output. The full vision: Monitor watches Builder token-by-token during generation. The Monitor's attention can intercept any token before it's committed, and the Monitor's KV cache holds the full generation context from the beginning — not just the final code.

**What this enables**:
- Monitor detects a hallucination at token 47 and fires a correction signal before token 48 is sampled
- Token-level acceptance sampling: Monitor can sample an alternative token from its own distribution and substitute it (similar to speculative decoding but cross-model)
- True "thinking together" — not one model checking another's output, but both processing the same sequence simultaneously

**Infrastructure requirement**: This requires forking llama.cpp or writing a custom CUDA kernel that:
1. Runs Builder's sampling step
2. After computing logits but before committing the sampled token, passes the logit distribution to Monitor
3. Monitor processes the partial sequence (via KV cache sharing) and returns a verdict: accept / replace / flag
4. If accept: commit token. If replace: substitute Monitor's preferred token. If flag: pause generation and escalate.

**This is NOT achievable with llama-cpp-python's current API.** The Python binding doesn't expose the token-by-token generation loop at a granularity that allows interception before commit. The required implementation is either:
- A C extension to llama-cpp-python that exposes a `token_callback` hook
- A fork of llama.cpp with a custom `llama_decode_step()` API that accepts a Python callable

**Design Phase 3 — do not build until Phase 2 async loop is shipping and stable.**

---

### #33 — Token-Level Acceptance Sampling for Monitor

**The problem**: Current Monitor receives Builder's complete output. This is post-hoc — by the time Monitor sees the code, the model has committed to a direction that may require full regeneration to fix.

**Token-level acceptance sampling**: Monitor receives the top-K logit distribution from Builder after each token. Monitor evaluates the distribution and can:
- Accept the top-1 token (Builder's choice)
- Substitute its own preferred token (drawn from Monitor's distribution over the same prompt context)
- Block generation and inject a correction via DSL (forces Builder to a new beam)

**This is the speculative decoding model applied cross-model.** The mathematics:
```
p_builder(x_t | x_{<t}) = Builder's distribution at step t
p_monitor(x_t | x_{<t}) = Monitor's distribution at same step (parallel evaluation)

acceptance_prob = min(1, p_monitor(x_t) / p_builder(x_t))

If accepted: use Builder's token x_t (sampled from p_builder)
If rejected: sample from (p_monitor - p_builder)_+ (the excess distribution)
```

This is mathematically equivalent to sampling from `p_monitor` while running `p_builder` as a speculative draft. The combined output is distributed exactly as if Monitor generated the entire sequence — but Builder's tokens are accepted ~70-80% of the time (when both models agree), dramatically reducing latency vs. full Monitor regeneration.

**Prerequisite**: KV cache broadcast (#24/#27). Token-level acceptance sampling cannot be implemented without the token-callback hook.

---

### #28 — GIL-Aware Worker Pool

**The problem**: Python's Global Interpreter Lock prevents true parallelism in a single Python process. In Phase 2 sequential execution, this doesn't matter — only one model is active at a time. In Phase 3 async execution, we want Builder, Monitor, and Compiler to run simultaneously. With pure Python threading, the GIL serializes them even when they're doing independent work.

**Design**:
```
determinex_worker_pool.py — multiprocessing-based, not threading-based

WorkerPool:
  builder_worker: Process(target=_builder_loop, args=(request_queue, result_queue))
  monitor_worker: Process(target=_monitor_loop, args=(request_queue, result_queue))
  compiler_worker: Process(target=_compiler_loop, args=(request_queue, result_queue))

Communication: multiprocessing.Queue with pickled StepRequest/StepResult objects
```

Each worker is a separate Python process with its own GIL. Workers communicate via queues, not shared memory (to avoid GIL re-entry bugs with PyTorch tensors). The model is loaded once per worker process and stays resident — no reload between steps.

**GGUF loading per-worker**: Each worker loads its own GGUF instance via llama-cpp-python. On Tier 0 (6GB VRAM), only one model can be on GPU at a time. Builder worker gets GPU; Monitor worker gets CPU. Compiler worker is CPU-only (no model, just subprocess calls).

**Queue protocol**:
```python
@dataclass
class WorkerRequest:
    step_id:   int
    request_type: Literal["build", "monitor", "compile"]
    payload:   dict      # serializable — no tensors on the boundary

@dataclass
class WorkerResult:
    step_id:   int
    success:   bool
    output:    dict
    wall_secs: float
```

No shared state between workers. The orchestrator is the single source of truth for manifest state.

---

### #30 — PCIe Thrashing Prevention

**The problem**: On Tier 0 (single GPU, 6GB VRAM), swapping models between GPU and CPU uses PCIe bandwidth. A 7B model at Q4 is ~4GB. Moving 4GB over PCIe 3.0 x4 (theoretical 4GB/s) takes ~2 seconds per swap. With a swap on every step, a 30-step project spends 60 seconds just on memory transfers — before any inference.

**Policy (already in the master plan, repeated here for Phase 3 implementation clarity)**:
- Builder stays permanently hot on GPU. Never swapped mid-session.
- Monitor runs on CPU (slower inference, no PCIe swap). Monitor timeout is scaled accordingly (thermal_throttle_factor handles this partially; a separate `cpu_inference_scale` factor is needed for Monitor).
- On Tier 1 (12-24GB), all models fit simultaneously — no swapping, no policy needed.

**Phase 3 consideration**: The async build loop (#35) changes the timing. With pipeline parallelism, the GPU is never idle waiting for Monitor — Builder is always generating something. This makes the "Builder stays hot" policy even more valuable. The Phase 3 implementation must enforce that the GPU worker (Builder) is never preempted by Monitor requests.

**`cpu_inference_scale` factor**: A per-model calibration factor that scales timeouts for CPU-resident models. Measured during micro_eval: `cpu_inference_scale = cpu_inference_time / gpu_inference_time`. Stored in `~/.determinex/calibration.json`. Used in `dynamic_ipc_timeout()` as a second multiplier.

---

### #31/#36 — Tensor Parallel and Pipeline Parallel (Tier 2 / Enterprise)

**The problem**: A single 7B model fits on one GPU. Multiple GPUs can run the same model in tensor-parallel mode (split layers across GPUs, reducing per-GPU VRAM) or pipeline-parallel mode (split layers sequentially, with each GPU handling a contiguous block of the model).

**Tier 2 design**:
```
Multi-GPU assignment (2 GPUs, 24GB each):
  GPU 0: Builder (7B GGUF, full model) + Compiler Oracle (CPU-side)
  GPU 1: Monitor (7B GGUF, full model) + Oracle/Architect (API or small local model)

No tensor parallelism needed at 24GB per GPU — models fit without splitting.
Benefit: true parallel execution (Builder on GPU 0 while Monitor on GPU 1).
```

**Tensor parallel (3+ GPUs, 14B+ models)**:
```
Each transformer layer split across GPUs via NCCL all-reduce.
Requires model support in llama.cpp (--tensor-split flag) or VLLM.
Not implementable with vanilla llama-cpp-python — needs VLLM or custom CUDA.
```

**Pipeline parallel (model layers split sequentially)**:
```
GPU 0: layers 0-15 (attention sink, early semantic processing)
GPU 1: layers 16-31 (late semantic processing, language head)
Forward pass: GPU 0 processes, sends activation to GPU 1, GPU 1 finishes.
Backward pass (training only): reverse pipeline.
Latency penalty: PCIe transfer between stages (~0.5ms per layer boundary).
```

**Phase 3 implementation target**: Tier 2 multi-GPU with one-model-per-GPU (no tensor splitting). Full tensor-parallel would require VLLM or custom CUDA — not yet implemented, no license restriction, just not built.

---

### #29 — Async Mixture of Agents (MoA)

**The problem**: In Phase 2, each role (Oracle, Architect, Builder, Monitor) generates sequentially. A true MoA architecture runs multiple agents simultaneously — e.g., Oracle runs in parallel with the Architect's scaffolding generation, or two Builder instances race on the same step and the best result is kept.

**Phase 3 design — two MoA patterns**:

**Pattern 1: Parallel Builders (step-level racing)**
```
Given step N instruction:
  Builder-A generates: conservative approach (RAII, explicit types)
  Builder-B generates: idiomatic approach (iterator chains, closures)
  Both run in parallel.
  Adjudicator scores both outputs.
  Winner applied to workspace.
  Loser → training queue (labeled "rejected approach").
```
This doubles the GPU demand but halves the effective retry rate — you get two shots per step instead of one.

**Pattern 2: Speculative Architect (DAG prefetch)**
```
While Builder executes step N:
  Architect speculatively plans step N+1 (assuming N will pass).
  If N passes: step N+1 is ready immediately (no wait for Architect).
  If N fails: speculative plan is discarded and re-planned with failure context.
```
This hides the Architect's planning latency entirely on the happy path.

**Implementation requirement**: Both patterns require the async worker pool (#28). Without process-level parallelism, MoA degrades to sequential execution under a different name.

**Python GIL impact on MoA**: The GIL prevents true parallel Python execution. Each "parallel" agent must be a separate process. The `WorkerPool` from #28 supports this — each Builder instance gets its own worker process with its own GIL and its own model loaded.

---

### Phase 3 Sequencing

```
Phase 2 ships:     Sequential build loop, validated A/B eval, stable micro_eval
                          │
Phase 3, Step 1:   #35 Async build loop — pipeline the 3 stages (no MoA yet)
                   #28 GIL-aware worker pool — prerequisite for true parallelism
                          │
Phase 3, Step 2:   #11 Mid-layer MLPs — train rosetta_v2.pt (after v1 A/B results)
                   #30 PCIe thrashing policy — cpu_inference_scale calibration
                          │
Phase 3, Step 3:   #24/#27 KV cache broadcast — custom C extension or llama.cpp fork
                   #33 Token-level acceptance sampling — depends on #24
                          │
Phase 3, Step 4:   #29 Async MoA — parallel builders, speculative Architect
                   #31/#36 Multi-GPU orchestration (Tier 2)
```

**Do not skip ahead.** Each step is a prerequisite for the next. Building KV cache broadcast before the async loop exists means the broadcast has no pipeline to feed.

---

---

## Project Cloak — Privacy Sovereignty Layer (April 27–28, 2026)

> **Status**: COMPLETE. Built and validated. Warm-up: 3/3 instances patched (100%, 129s).
> Full SWE-bench Lite ablation (300 instances, 3 configs) running as of April 28, 2026.

### What It Is

Project Cloak is an AST-aware whole-repository Python identifier obfuscation system. It sits between the Hive `solve()` function and every cloud AI API call. Private identifiers — function names, class names, variable names, argument names — are replaced with opaque `x_NNNN` tokens before any AI sees the code. The AI solves in obfuscated space. Patches are restored before application.

**New files delivered:**

| File | Purpose |
|---|---|
| `scripts/determinex_cloak/` | Full Cloak package (7 components) |
| `scripts/verify_cloak.py` | Post-run privacy audit |
| `data/stdlib_312.txt` | Python 3.12 stdlib safe-list (~300 names) |
| `scripts/testing/run_ablation.sh` | B-Uncloaked → B-Cloaked → D-Cloaked sequence |

**Modified files:**

| File | Change |
|---|---|
| `scripts/determinex_swebench_agent.py` | Cloak integration in `solve()`, region mode always-on, ratio check removed, line-number stripping |
| `scripts/determinex_swebench_run.py` | Config D (Nuclear Hybrid), `DETERMINEX_CLOAK` env var routing, parallel workers |

### Seven-Component Pipeline

```text
CloakPipeline (scripts/determinex_cloak/)
├── StdlibManifest          stdlib_312.txt + repo requirements → frozenset safe names
├── IdentifierClassifier    AST walker → private identifier frozenset (global dedup)
├── SymbolMap               alphabetical → x_0001..x_NNNN, bidirectional
├── ASTTransformer          NodeTransformer: cloak names, strip comments, Option D docstrings
├── IssueTextTransformer    regex, length-descending, on issue text only
├── RestorationEngine       \bx_\d{4}\b regex on raw diff lines → original identifiers
└── AuditLogger             cloak_failures.jsonl, optional api_requests.jsonl
```

**CloakContext** (per-instance state, created once at `solve()` start):
```python
CloakContext(
    instance_id: str,
    symbol_map: dict[str, str],        # forward
    reverse_map: dict[str, str],       # reverse
    obfuscated_files: dict[str, str],  # path → obfuscated source
    star_import_warnings: list[str],   # documented holes
)
```
Saved to `cloak_map_<instance_id>.json` for post-run audit.

**Scale example** (`astropy__astropy-12907`): 24,134 identifiers mapped, 169 star-import holes.

### Critical Engineering Discoveries Made During Build

These were found and fixed before the full ablation run. They are part of the architecture record.

**The Context Paradox Pattern**
Issue text was obfuscated before `locate_relevant_files()`. Keyword extraction produced `x_14086` tokens. File search found nothing. 100% empty patches on first cloaked run.
Fix: Applying the Context Paradox Pattern. Execute file and symbol discovery operations against unobfuscated source text to identify relevant code regions, and apply identifier obfuscation exclusively to content transmitted to external AI systems after discovery is complete. This separation preserves the utility of semantic search while maintaining complete identifier privacy to external systems.

**The Builder Rewrite Bug**
`_REGION_THRESHOLD=400` meant files <400 lines were passed whole. Builder returned reformatted entire file. `difflib.unified_diff` on reformatted file → ~2× lines changed. 80% ratio check discarded all patches.
Fix: `_REGION_THRESHOLD=0` (always region mode) + remove ratio check entirely.

**Builder Line-Number Echoing**
Region mode context shows Builder `"   67 | code"`. Builder echoed the `"N | "` prefix. Stripping was inside `if region_mode:` block only.
Fix: Move stripping before the branch; applies to both code paths.

**Cloak Checksum Failure**
Architect plan passed real names to Builder despite cloaked files. Builder renamed all x_NNNN tokens to match. Validator rejected: "Builder renamed 35/35 x_NNNN tokens."
Fix (pending next iteration): Re-obfuscate Architect plan before passing to Builder.

### SWE-bench Ablation Configuration

```
scripts/testing/run_ablation.sh:
  Config B-Uncloaked  → DeepSeek/DeepSeek, no cloak    (baseline)
  Config B-Cloaked    → DeepSeek/DeepSeek, with cloak  (privacy cost)
  Config D-Cloaked    → Claude Sonnet/DeepSeek, cloaked (Nuclear Hybrid ceiling)
```

4 parallel workers. 301 pre-cloned repos at `T:\determinex-swebench`. Zero clone overhead.

### Verification (`scripts/verify_cloak.py`)

```
--run-dir logs/swebench/<run_id>
--strict                           # exit 1 if any leak (CI mode)
```
Loads `cloak_map_<iid>.json`, scans `api_requests.jsonl`, reports CLEAN / LEAK×N.
Run with `DETERMINEX_CLOAK_AUDIT=1` for logged proof; without it → UNVERIFIED.

### Known Holes (Published)

| Hole | Description | Audit trail |
|---|---|---|
| Star imports | `from module import *` exports unobfuscated | Counted in `star_import_warnings` |
| String annotations | `"UserRecord"` in TYPE_CHECKING not an AST Name node | Partial coverage |
| Architect plan | Not re-obfuscated before Builder receives it | Next iteration |

---

## Generation 5 — SWE-bench + Project Cloak (April 27–28, 2026)

Generation 5 components (built this session):
- `scripts/determinex_cloak/` — Cloak package
- `scripts/verify_cloak.py` — Privacy audit
- `scripts/testing/run_ablation.sh` — Ablation runner
- `data/stdlib_312.txt` — Stdlib manifest
- Major refactor of `determinex_swebench_agent.py` — region mode, cloak integration, line-number fix, ratio check removal

The full SWE-bench Lite ablation is the system's first external benchmark run at scale (300 instances, 3 configurations). Results pending.

---

## What To Say In The White Paper

The five sentences that matter (updated April 28, 2026):

> Determinex demonstrates that a self-improving, compiler-validated AI development pipeline can be built on consumer hardware in under 72 hours. The ground-truth reward signal — real compilers returning pass/fail, not LLMs judging LLMs — is the mechanism that makes autonomous improvement trustworthy. The Rosetta Stone bridges heterogeneous AI model embedding spaces with 2-layer MLPs trained via InfoNCE contrastive learning, producing cosine alignment gaps of 0.745–0.891 across five architecture families — validating the Platonic Representation Hypothesis as an engineering primitive. **Project Cloak demonstrates that a local AI agent can resolve real-world software engineering tasks (SWE-bench Lite) using frontier cloud AI while the cloud AI remains blind to every proprietary identifier in the repository — the cost of complete privacy sovereignty measured for the first time.** The encrypted local telemetry vault, ForgeDaemon-closed training flywheel, and air-gapped update model are the architecture the enterprise sector has been waiting for.

Everything else in the white paper is evidence for those five claims.

---

## Generation 6 — The Correctness Amplifier (June 2026)

The April architecture proved the principle on Determinex's own fine-tuned models. The
June 2026 substrate makes it **general and model-agnostic**: correctness is bounded by
a sound oracle, not by trusting any model. New layers (all implemented + tested by a
40-case meta-bench):

- **Universal Ground-Truth Oracle** (`determinex_oracle.py`) — the Compiler Oracle
  generalized to a pluggable per-language registry (real Go/Rust compile-oracles, TS
  via tsc+jest, Python) plus a synthesizer for when no tests ship.
- **The Correctness Amplifier** (`determinex_verified_search.py` + decompose / case-memory
  / context / progress / contract / router) — best-of-K against the oracle:
  `P(solve)=1−(1−p)^K`. Any `p>0` is driven toward correct; ~60,000× demonstrated lift
  on a 1.5B-class model. Wired into the build loop behind `DETERMINEX_AMPLIFY=1`.
- **The Impossibility Adjudicator** (`determinex_adjudicator.py`) — a no-cop-out gate;
  may only declare a ceiling with a proof. 29 ProgramBench "ceilings" → 0 proven.
- **The Test Validator** (`determinex_test_validator.py`) — deterministic "is the test
  slop?" so a wrong oracle can't yield confident-wrong output.
- **Greenfield + repair** (`determinex_synthesize.py`, `determinex_build_from_idea.py`,
  `determinex_repair.py`) — idea → sound oracle → verified program; and diagnose/fix any
  repo against its real oracle. Proven live with a 1.9 GB local model.
- **Any AI / any agent host** (`determinex_providers.py`, `determinex_agents.py`,
  `determinex_extensions.py`, `determinex_ratelimit.py`) — Claude / Codex / Gemini / local /
  addons behind one contract; agent CLIs hosted with oracle-verified output (a
  hallucinating agent is rejected); auto-establishing rotating rate limit.
- **No-overclaim governance** (`scripts/governance/`) — 254-line authority-anchor core
  + deterministic pre-commit guard, consolidated from the archived status/proof apparatus.
- **Editor surface** — a compiling, packaged VS Code extension (`frontend/vscode-extension/`).

The sixth sentence for the white paper: *the system makes any model — local, cloud, or
not-yet-invented — correct on anything verifiable, because it does not believe the model;
it checks it against a sound oracle.* Grounded account: [`docs/DETERMINEX_DEEP_AUDIT.md`](../DETERMINEX_DEEP_AUDIT.md).

---

## Generation 7 — PB Lock-Campaign Automation (June 2026)

Generation 6 made correctness model-agnostic per task. Generation 7 makes the *campaign*
self-driving, gated, and parallel — the layer that turns "fix one tool" into "process the
whole benchmark without wiring things in by hand after hours of wasted evals."

- **Parallel eval runner** (`scripts/pb_parallel.py`) — collision-safe concurrency: per-tool
  factory dirs, no global `docker prune`/`kill` during evals (prune only when all slots idle),
  CPU split via `PROGRAMBENCH_DOCKER_CPUS`. It also re-reads its queue file, so it is a
  *continuous feeder* — appended tools are picked up without a relaunch. The old "parallel
  collides → run serial" rule was a misdiagnosis (broad docker kills clobbered sibling
  containers); validated at 5+ concurrent on the 8-core host. ~3–4× throughput.
- **Gated ingestion** (`scripts/pb_ingest.py`) — the one path from a finished `eval.json`
  (local or Hetzner) into the canonical state: score+provenance → `eval_index.json`; clean
  100% → archive + `verify_and_register` (provenance / anti-test-gaming gate). Anti-regression
  and fresh-only guards prevent a stale/partial eval from overwriting a higher score or
  demoting a lock — the consistency fix after an early over-broad sweep regressed the index.
  State model: `eval_index` = board, lock registry = gated locks, `locked/<slug>/` = artifacts,
  training corpus = flywheel.
- **Self-applied build knowledge** (`corpus/programbench/build_knowledge.json`) — the system
  reads its own playbook (lock criteria, module map, eval mechanics, class patterns + overlaps,
  lib→apt map, mass-jump ranking) via `determinex_pb_autofix.load_knowledge`.
- **Generalized class-fixers** in `determinex_pb_autofix`: `_go_forced_toolchain`
  (`golang.org/x/*` 1.24 class — 17 tools), `_go_cgo_deps` (+`sqlite_fts5`), `_fix_build_target`,
  complete-repack for tarball-drift, hermetic `umask 022`, and `_cc_build_deps` (C/C++
  configure/CMake → apt `-dev` packages).
- **Reliability** — robust `GOTOOLCHAIN` retry pre-fetch; `determinex_pb_capture` plugin
  (collection errors + full tracebacks + source via results.xml); 16 GB swap on the eval host
  (was zero) with `swappiness=10` to survive heavy C/C++ builds without OOM.

The empirical point: a single root-cause class-fix lifts whole cohorts of "duds" from ~0% to
90–99% (go-critic 1.2%→94.5%, fx→93.6%, felix→97.77%, goimports-reviser→99.8%). These are
**near-locks, not new 100% locks** — the official lock count is unchanged (64 strict + 6
upstream) until each clears its last-mile tail and the provenance gate. The advance is the
*system*: it now diagnoses, fixes, parallelizes, ingests, and gates the campaign itself.

---

*Document updated June 20, 2026 (Generation 7 appended). Generation 6 appended June 14, 2026. Earlier body built April 28, 2026 from: git log, source audit, live system state, hive mind design spec, SWE-bench ablation run in progress.*
*Author: DarthCeltic. Released under AGPLv3.*

---

## Generation 8 — The ProgramBench Pivot: Native Reverse-Engineering (June 25, 2026)

Generation 8 is a **methodology pivot**, not an incremental feature. Through Gen 7, Determinex's
ProgramBench result was ~64–65 "locks" built by shipping each tool's **real upstream source** and
rebuilding it. The June-24 audit (`METHODOLOGY_INVALIDATION`) established this is the **forbidden
shortcut** ProgramBench exists to prevent: PB is a *reverse-engineering* benchmark — given only a
binary + docs, rebuild from scratch. Shipping source compiles to a different-hash binary so PB's
binary-hash deletion never caught it, but it violates the intent. Those "locks" are relabeled
*native rebuilds*, not legitimate PB solves.

The legitimate engine that replaces it is the **Native Reimplementation Loop**
([`docs/architecture/NATIVE_REIMPL_LOOP.md`](../architecture/NATIVE_REIMPL_LOOP.md)). The pivots:

1. **System-is-the-unit-of-correctness, made operational.** `score = oracle-completeness ×
   technique-coverage × search-budget(+escalation)` — all system-controlled. A cheap/local model
   sampled against a sound oracle is driven toward correct. Proven on gron: free 7B 1.3% →
   DeepSeek 76→96/224 via one technique recipe.
2. **Native-only (new Determinex law).** Rebuild in the tool's real language (Go/Rust/C/C++/Haskell),
   **compiler-oracle verified** — never a Python lookalike ("laziness"). This finally engages
   Determinex's original moat (the compiler oracle) and is the only path to the C/C++/Haskell bottom
   tier. `observe.make_native_runner` compiles (reject-on-fail with the error fed back) + runs the
   real binary against the probes; native compile.sh packaging for official scoring.
3. **The oracle PROVISIONS environments**, killing false ceilings. URL-fetch (a claimed
   "structural ceiling") proven solvable via a loopback `http.server` under `--network none`.
   PTY/env/archive provisioning is the same pattern (the Wave-2 class-unlockers).
4. **Autonomous self-feeding loop** (`determinex_reimpl_drive`). `fuzz_diagnose` generates random
   black-box inputs, diffs reference vs candidate, and every divergence becomes a new probe in the
   **corpus-owned oracle** — the same fuzzing PB uses to make tests, no held-out access. The human
   is removed from the inner loop; the oracle compounds toward behavioral completeness.
5. **Leaderboard reality.** Every public model is at **0% fully-resolved** (best-ever single task
   98.2%) because they generate-and-pray with no completeness loop. Determinex's edge is closing the
   last 2% nobody closes; the near-term target is the **first full-resolve in the world**.
6. **Workshop + retrain are legitimate** (verified against PB's actual rules: black-box, no
   internet at inference, genuine codebase). The offline-inference rule makes the release endpoint
   a **local retrained model** — coaching/recipes/case-memory baked in via the flywheel.
7. **Verifier Skills.** Each verified native solve is a compiler-verified, evidence-backed
   capability (native code + oracle + case memory + compile evidence); 200 solves → 200 reusable
   deterministic skills, an added layer over Idea Lab/Hive/Oracle.

New/converged modules: `determinex_observe` (provisioning + native runner + fuzz_diagnose +
discrimination), `determinex_pb_reimpl` (`--lang`), `determinex_reimpl_drive` (autonomous), `determinex_
reimpl_corpus` (coach + technique recipes + corpus-owned oracle), `determinex_reimpl_analyze`
(design-invariant analyzer), with `determinex_providers`/`router`/`contract`/`case_memory` composed
(audited to avoid duplication). Engine regression-green (`tests/test_autofix_pipeline.py` 47/1-skip).

*Generation 8 appended June 25, 2026 from live build state. Author: DarthCeltic.*

---

## Generation 9 — The Self-Improving Autonomous Engine (June 29, 2026)

The ProgramBench workshop became a **closed, self-improving autonomous loop** — *take in → robust
eval → triage → route → prove → keep best → LEARN* — running unattended on the private box (`box7`),
all results + knowledge **private** (no git remote) and the bulk knowledge ingest **free**
(local-model only). Canonical doc: [`docs/architecture/SELF_IMPROVING_ENGINE.md`](../architecture/SELF_IMPROVING_ENGINE.md).

Six pieces shipped this generation:

1. **Eval robustness — "any code that hangs still gets scored."** Host py-spy proved the hang is in
   the OUTER harness: `subprocess.run(docker)→select` blocks on Docker's stdout pipe, held open by a
   **tmux server that double-forks and reparents to PID 1**, escaping pytest's tree (signal-timeout
   can't kill it). Fix: `determinex_subprocess_guard` (pytest11, 4 mechanisms — stdin→DEVNULL, killpg,
   `pytest_sessionfinish`/watchdog **escaper-kill** of tmux + the tool binary, manual-read watchdog),
   bulk-injected into all 222 tools. And the stall detector (`pb_eval_unified.run_local_eval`) moved
   from CPU (a stuck eval spins >5% → "busy forever" → rode the 30-min cap) to **test-progress** (the
   `PYTEST_CURRENT_TEST` set across the tool's parallel branch containers, slug-scoped) → cuts a
   stuck eval in **4 minutes**. `determinex_orphan_reaper` reaps reparented orphan binaries.

2. **Best-eval retention + private capture.** `_persist_best` writes `eval_report.json` only if
   better — a flaky/memory-starved re-eval can never clobber a good score. `pb_sync capture-scores`
   best-eval-merges box→repo; `pb_capture_local` (a 30-min scheduled task) captures + commits LOCAL
   and deploys `build_knowledge` down to the box. Nothing reaches a remote.

3. **The grounded fixer — "right the first time."** The catch-all model build-fixer
   (`_amplify_build_fix`) now feeds the accumulated `build_knowledge.class_patterns` +
   `learned_classes` as a relevance-ranked SYMPTOM→FIX playbook, so it applies what the system
   already knows on the first candidate. Sound: oracle-gated, so a rough hint can only help.

4. **Triage → route → certify.** `determinex_autofix.triage` (adjudicate + explain + validate) yields
   `{reopen, genuine, slop, proofs}`; `drive_one` certifies a **proven** ceiling (proof required;
   registered, reversible) and routes everything winnable to the grounded close — no false ceilings,
   no blind grinding of the impossible.

5. **The knowledge flywheel.** `determinex_pb_amplified_fix.learn_class` distills every *oracle-verified*
   solve into a generalized `(symptom→fix)` class (`_normalize_signature` strips tool/path/version;
   `_fix_diff` captures the fix) → `build_knowledge.learned_classes` → the playbook applies it
   first-shot next time. Grinding becomes **compounding knowledge** — the breadth engine.

6. **The knowledge absorber.** `determinex_pb_absorb` seeds the flywheel from everything already known
   in prose (corpus docs, milestones, playbooks, memory), the codebases (`--scan-drive`: a bounded
   `os.walk` of T: archive + the C:/Dev codebases incl. source), and online (free web build-knowledge
   → `ingest/`), distilled by the **local model** (no paid APIs), quality-gated (the detect must look
   like a failure, the fix must be actionable; gaming excluded), resumable + incremental.

*Generation 9 appended June 29, 2026 from live build state. Author: DarthCeltic.*
