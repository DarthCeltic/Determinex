<div align="center">

<img src="frontend/public/determinex-logo.jpg" alt="Determinex" width="360" />

# Determinex

**Compiler-verified multi-agent AI that gets smarter from its own failures.**

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org)
[![Rust](https://img.shields.io/badge/Rust-1.75%2B-orange)](https://rustup.rs)
[![White Paper](https://img.shields.io/badge/Paper-WHITE__PAPER.md-green)](docs/papers/WHITE_PAPER.md)
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-♥-pink)](https://github.com/sponsors/DarthCeltic)

*Built by [Ryan Gurganious](https://github.com/DarthCeltic)*

</div>

---

Determinex is a **local-first, privacy-sovereign, self-improving multi-agent AI coding system**. Three specialist models — Engineer, Observer, Sentinel — coordinate through a shared latent space to break complex engineering tasks into compiler-verified build steps. Failure-to-training conversion is separately gated: `training_eligible = false` by default and no raw user code training by default. The system gets smarter from operator-approved, compiler-verified evidence without leaving your machine.

**The core idea (2026-06 architecture):** correctness is bounded by a deterministic **oracle** (real compilers/tests), not by trusting the model. The model proposes; the oracle disposes. This makes Determinex **un-hallucinatable wherever ground truth exists** and lets *any* AI — a 1.5B local model, a frontier cloud model, an agent CLI, or a future one — plug in and be made correct. The **Correctness Amplifier** turns a model with per-attempt success `p` into a system that succeeds with `1−(1−p)^K` by sampling against the oracle: any `p > 0` is driven toward correct. On top of the build loop, Determinex can now **build a verified program from a plain-language idea** (synthesizes a sound test-oracle first), **diagnose and repair any repo** (honest CODE / ENVIRONMENT / TEST blame), and **host any AI model or coding agent** (Claude / Codex / Gemini / local / addons) — each verified through the same oracle, so a hallucinating model or agent is *rejected*. A reproducible 40-case meta-bench (`tests/test_autofix_pipeline.py`) scores the system's own reasoning. See [`docs/DETERMINEX_DEEP_AUDIT.md`](docs/DETERMINEX_DEEP_AUDIT.md) for the grounded end-to-end account.

Current readiness boundary: the release-cell registry contains 13 exact release-supported cells and 0 release-supported families. These are proof cells, not broad support. Batch 003 verifies the rebuilt staged installed-app Proof Center route at `/proof-center` with screenshot/transcript evidence. Batch 004 archives `trasta298__keifu` as a strict ProgramBench lock and promotes exactly one narrow all-gap row: the deterministic day-one claim scanner guard. Full monolithic `tests/status`, all gaps closed, family support, and ProgramBench total-100 remain open; open availability remains false.

**The current SWE-bench boundary**: The May 2026 B-Uncloaked run resolved **14.0% of SWE-bench Lite** (42/300, zero errored), but it is an audited snapshot, not the final publication baseline. The Cloak-on / region-mode configurations are currently reported as lower bounds because disk-pressured Docker workers produced per-instance image-export errors: E-RegionControl **>=6.0%**, B-Cloaked RosettaOFF **>=2.3%**, D-Cloaked **>=3.3%**. Fresh B-Uncloaked and E-RegionControl reruns are required before publishing privacy-cost claims.

**Plus, on [ProgramBench](docs/papers/PROGRAMBENCH.md)** — the 200-tool benchmark where every frontier model currently scores 0–0.5% fully resolved — Determinex's honest headline (corrected 2026-06-30) is **0/200 legitimate locks**, matching public leaderboard reality. A full provenance audit found the historical, prior "65 confirmed full-suite locks / 32.5%" claim counted upstream source builds (`go.mod`/`Cargo.toml` identity matching the real project verbatim), not native reimplementations. The 62 archived builds under `corpus/programbench/locked/<tool>/` are retained as reference corpus for the Native Reimplementation Loop — the legitimate path to a real lock — not counted as solves. Source of truth: `corpus/programbench/eval_index.json`. Benchmark results are not product support, not release support, and not product readiness.

---

## What Makes This Different

| Property | Determinex | Typical agent system |
|---|---|---|
| **Reward model** | `rustc` / `go build` / `python` / `tsc` — deterministic, zero hallucination | LLM judge (circular) |
| **Privacy** | 100% of repo identifiers obfuscated before any cloud call | Source code sent to cloud |
| **Training signal** | Every session failure → labeled corpus → next retrain | Static weights |
| **Model size** | 1.5B + 3B + 7B, runs on 6GB VRAM | 70B+ cloud-only |
| **Architecture** | DAG build loop, compiler gate, WAL, oscillation detector | Linear chain |
| **Any model correct** | Verified search: `1−(1−p)^K` against a sound oracle | Best single shot |
| **Bring your own AI** | Claude / Codex / Gemini / local / agents — all oracle-verified | Locked to one vendor |
| **No cop-out / no slop** | Adjudicator proves impossibility; Validator proves a test is slop | Gives up or guesses |

---

## Beyond the Build Loop (2026-06)

The same oracle-bounded engine now powers three things any developer can use directly:

- **Build from an idea** — `python scripts/determinex_build_from_idea.py --idea idea.md --provider local` synthesizes a *sound* test-oracle from your description (exact examples + type-aware property tests, validated to run), then drives any model with verified search until a program **passes those tests**. Proven live: a 1.9 GB local model produced a verified `rle` implementation.
- **Repair any repo** — `python scripts/determinex_repair.py path/to/repo` ingests the project, runs its real oracle, and reports honest blame (**CODE / ENVIRONMENT / TEST**) + whether a failing test is provable *slop*; with opt-in it amplified-fixes to oracle pass.
- **Host any AI or agent** — `determinex_providers.py` exposes Claude/Codex/Gemini/DeepSeek/local behind one `generate(prompt, temperature)` contract (with an **auto-establishing, rotating rate limiter**); `determinex_agents.py` hosts coding-agent CLIs (Codex CLI, Claude Code, …) whose edits are **verified through the oracle** — a no-op or hallucinating agent is rejected. New providers/oracles/commands plug in via `determinex_extensions.py`.
- **In your editor now, and toward its own IDE** — a compiling, packaged VS Code extension (`frontend/vscode-extension/`) remains the bridge for developers who live in VS Code. The standalone Tauri/Next Determinex IDE is the successor direction: proof-native workbench, agent lanes, oracle evidence, privacy policy, and release gates in one product surface. Current status and blockers are tracked in [`docs/ide-frontend/DETERMINEX_IDE_SUCCESSOR_ROADMAP.md`](docs/ide-frontend/DETERMINEX_IDE_SUCCESSOR_ROADMAP.md).

Full grounded account, including the honest safety/unsafe surface and the teaching model: [`docs/DETERMINEX_DEEP_AUDIT.md`](docs/DETERMINEX_DEEP_AUDIT.md).

---

## The Model Family

| Model | Params | Role | HuggingFace | Ollama Tag |
|-------|--------|------|-------------|-----------|
| **C1 · Engineer v11-dsl** | 1.5B (Qwen2.5-Coder) | Builder — fast code generation, DSL-tuned | [🤗 Download](https://huggingface.co/darthceltic85/determinex-engineer) | `determinex-engineer-v11-dsl` |
| **C3 · Observer v6-dsl** | 3B (Llama-3.2) | Monitor — error diagnosis, adjudication | [🤗 Download](https://huggingface.co/darthceltic85/determinex-observer-llama-3.2) | `determinex-observer-v6-dsl` |
| **C7 · Sentinel v5-dsl** | 7B (Mistral) | Architect / Oracle — DAG planning, escalation | [🤗 Download](https://huggingface.co/darthceltic85/determinex-sentinel) | `determinex-sentinel-v5-dsl` |

All three run locally via Ollama. No subscription. No cloud required for the core build loop.

> You don't need the fine-tuned GGUFs to get started — any Ollama-hosted model in the same tier works. See [Option A](#option-a--bring-your-own-models) below. Note: `determinex-observer` is a Llama-3.2 derivative and ships under the Llama 3.2 Community License, not Apache 2.0 — see [Model Notices](docs/release/MODEL_NOTICES.md).

---

## Benchmarks

### Model Quality (Compiler-Validated, Post-DSL Fine-Tune)

135 probes across 9 task types × 3 models. Every probe passes a real compiler — no LLM judges.

| Model | Score | Probes Passed | Delta vs Baseline |
|-------|-------|---------------|------------------|
| C1 · Engineer v11-dsl | **89%** | 40/45 | +5pp |
| C3 · Observer v6-dsl | **82%** | 37/45 | +4pp |
| C7 · Sentinel v3 | **87%** | 39/45 | — (pre-dates DSL fine-tune; v5-dsl re-eval queued) |
| **System combined** | **86%** | 116/135 | +3pp |

### SWE-bench Lite (300 instances, post-hardening ablation)

Real software engineering tasks from production repositories. Patches verified by each repo's own test suite in Docker.

| Config | Architect | Builder | Cloak | Resolved | Status |
|--------|-----------|---------|-------|----------|--------|
| B-Uncloaked | DeepSeek V4 | DeepSeek V4 | off | **14.0%** (42/300) | Audited May snapshot; fresh rerun required for publication |
| E-RegionControl | DeepSeek V4 | DeepSeek V4 | off, region forced | **>=6.0%** | Lower bound, disk-export errors |
| B-Cloaked RosettaOFF | DeepSeek V4 | DeepSeek V4 | on | **>=2.3%** | Lower bound, disk-export errors |
| D-Cloaked | Claude Sonnet 4.6 | DeepSeek V4 | on | **>=3.3%** | Lower bound, disk-export errors |
| D-Cloaked (pre-hardening historical) | Claude Sonnet 4.6 | DeepSeek V3 | on | **11.7%** | Historical, pre-hardening |

**What the delta framework measures:**
```
B-Uncloaked 14.0%      -> audited May snapshot; final baseline pending fresh rerun
E-RegionControl >=6.0% -> lower-bound region-mode control
B-Cloaked >=2.3%       -> lower-bound sovereignty result
D-Cloaked >=3.3%       -> lower-bound hybrid Architect result
```

*Privacy audit: B-Cloaked run verified 1,813,760 identifiers across 300 instances - 0 restoration failures, 0 privacy leaks. Cryptographic proof artifact via `DETERMINEX_CLOAK_AUDIT=1`. TinyCorpusReplay, when referenced, is an answer-key corpus replay diagnostic for eval-path mechanics only; it is not a clean benchmark score, not a model score, and not training-eligible.*

---

## Architecture

```
User writes a Markdown spec (Goal, Language, Constraints, Files)
        ↓
C7 Architect — reads spec, emits DAG of ordered build steps via Semantic DSL
        ↓  [6× more token-efficient than prose]
C1 Builder — executes each step; writes code to the workspace
        ↓
Compiler Oracle  ──  rustc / go build / python / tsc  ──  ground truth
   PASS → lock step to WAL → next step
   FAIL → inject exact error → Builder retries (max 3×, escalating temperature)
        → Architect re-plans on 3rd failure
        ↓
C3 Monitor — scores output; submits competing approach if score gap > 0.1
        ↓
Every session → training queue → flywheel retrain → smarter models
```

### Project Cloak — Privacy-Sovereign Cloud AI

Before any cloud API call, Determinex transforms every private identifier in the entire repository into an opaque `x_NNNN` token. The cloud AI solves the problem in obfuscated space. Patches are restored to real identifiers locally before application.

```
Source repo  →  [AST obfuscation]  →  x_NNNN tokens  →  Cloud API
                                                              ↓
Real patch  ←  [symbol restoration]  ←  obfuscated patch  ←──┘
```

The cloud model never sees `authenticate_user`, `validate_payment`, or any other business-critical symbol — only `x_4421`, `x_9103`. **Privacy cost measured directly**: B-Cloaked vs E-RegionControl in the 5-config ablation.

### The Rosetta Stone — Latent-Space Model Communication

`rosetta_v1.pt` — MLP encoder/decoder pairs bridging C1, C3, and C7 embedding spaces into a shared 4096-dim semantic space. Models communicate via compressed latent vectors rather than prose — 6× more token-efficient, lossless for structured intent.

- **Layer 1 (active)**: Semantic DSL — structured inter-model messages
- **Layer 2 (v1.5)**: Soft prefix injection via llama-cpp-python
- **Layer 3 (Phase 3)**: KV cache broadcast — full mid-layer hidden state sharing

---

## Quick Start

### Requirements

- [Ollama](https://ollama.ai) installed and running
- Python 3.11+
- At least one compiler: `rustc`, `go`, or `python` (for the Compiler Oracle)
- 6GB+ VRAM **or** 16GB+ RAM (CPU inference supported)

### Install

```bash
git clone https://github.com/DarthCeltic/determinex
cd determinex

# Inference-only (CLI, ~200MB dependencies)
pip install -r scripts/requirements.txt

# Full stack with training tools (~4GB, requires PyTorch)
# pip install -r requirements.txt
```

### Option A — Bring Your Own Models

The architecture works with any Ollama model. No training required.

```bash
# Pull base models
ollama pull qwen2.5-coder:7b-instruct
ollama pull qwen2.5-coder:1.5b-instruct
ollama pull qwen2.5-coder:3b-instruct
```

Edit `.env` to point the roles at your models:
```env
DETERMINEX_ARCHITECT_MODEL=ollama/qwen2.5-coder:7b-instruct
DETERMINEX_ENGINEER_MODEL=ollama/qwen2.5-coder:1.5b-instruct
DETERMINEX_OBSERVER_MODEL=ollama/qwen2.5-coder:3b-instruct
```

### Option B — Use the Fine-Tuned Models

```bash
cp .env.example .env
# Set DETERMINEX_MODELS_DIR to wherever your GGUFs are

# Windows
.\register_models.ps1

# Linux / macOS
bash register_models.sh
```

GGUFs available at [huggingface.co/darthceltic85](https://huggingface.co/darthceltic85).

### Run a Build Session

```bash
cat > my_spec.md << 'EOF'
# Line Counter

## Goal
A Rust function that reads a file and counts lines.

## Language
rust

## Constraints
- No unsafe blocks
- Returns Result<usize, std::io::Error>

## Files
- src/lib.rs — core logic
EOF

python scripts/determinex_hive.py new-session --spec my_spec.md --lang rust
python scripts/determinex_hive.py generate-dag --session <session-id>
python scripts/determinex_hive.py run-session --session <session-id>
```

### Desktop App (Tauri + Next.js)

```bash
cd frontend
npm install
npm run tauri dev
```

Requires [Node.js 18+](https://nodejs.org) and the [Rust toolchain](https://rustup.rs).

---

## Project Structure

```
scripts/
  determinex_hive.py            # Main orchestrator (DAG build loop)
  determinex_swebench_agent.py  # SWE-bench solve loop with Cloak

  # Correctness substrate (2026-06) — oracle-bounded, makes any model correct
  determinex_oracle.py          # Universal pluggable ground-truth oracle (+ synthesizer)
  determinex_verified_search.py # The amplifier core: best-of-K vs the oracle
  determinex_amplified_solve.py # Decompose + route + verified search (brownfield)
  determinex_adjudicator.py     # No cop-out: ROUTE/MATCH/UNBLOCK/IMPOSSIBLE gate
  determinex_test_validator.py  # No slop: is the TEST itself correct?
  determinex_explainer.py       # Per-failure blame (CODE/ENV/TEST) + delta + proof
  determinex_synthesize.py      # Idea -> sound test-oracle
  determinex_build_from_idea.py # Greenfield: idea -> verified program
  determinex_repair.py          # Brownfield: diagnose + amplified-fix any repo
  determinex_providers.py       # Any AI model behind one generate() contract
  determinex_agents.py          # Host coding-agent CLIs, oracle-verified
  determinex_extensions.py      # Addon protocol (providers/oracles/commands)
  determinex_ratelimit.py       # Auto-establishing rotating per-model rate limit
  governance/                # No-overclaim authority anchors + guard

  determinex_cloak/             # Project Cloak — AST obfuscation pipeline
  determinex_rosetta.py         # Rosetta Stone — latent-space model bridge
  hive/                      # Build-loop execution, Compiler Oracle, safety gates
  ide/                       # IDE backend command surface + Tauri bridge
  security/                  # SBOM / dependency / license / container scans
determinex_trainer/             # LoRA / Unsloth fine-tuning
frontend/
  vscode-extension/          # VS Code extension (brain in your editor)
  src-tauri/ + src/          # Tauri desktop app (Next.js + Rust)
docs/
  DETERMINEX_DEEP_AUDIT.md      # Grounded end-to-end audit (what/how/safe/teach)
  papers/WHITE_PAPER.md      # Full academic paper
  papers/ARCHITECTURE.md     # System design specification
  architecture/              # CORRECTNESS_AMPLIFIER, IMPOSSIBILITY_ADJUDICATOR, ...
rosetta/                     # Rosetta Stone training artifacts
```

---

## Roadmap

| Milestone | Status | Highlights |
|---------|--------|-----------|
| Build engine | **Built** | DAG build loop · Compiler Oracle · Rosetta v1 · Project Cloak · SWE-bench ablation |
| Correctness substrate | **Built (2026-06)** | Correctness Amplifier · Adjudicator · Test Validator · build-from-idea · repair · any-AI/agent host · governance |
| Editor surface | In progress | VS Code extension bridge; standalone Determinex IDE roadmap + Tauri shell; release blockers remain explicit |
| Next | Planned | Rosetta Layer 2 · model re-eval · Docker-scale field-prove · KV cache broadcast |

> No released versions exist yet. "Built" means implemented + tested in-repo; it is not a claim of launch/release/production readiness, which remain governed by the no-overclaim authority anchors (all `false`).

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Read [docs/papers/WHITE_PAPER.md](docs/papers/WHITE_PAPER.md) and [docs/papers/ARCHITECTURE.md](docs/papers/ARCHITECTURE.md) before submitting a PR — the design philosophy (the oracle is the only judge) is non-negotiable.

**Priority contributions:**
- Additional language validators (`scripts/validators/`)
- Alternative model registrations for the Rosetta Stone
- SWE-bench instance analysis and failure pattern documentation

---

## Support the Project

Determinex is free and open source (AGPLv3) and built by a solo developer.
There's no paywall and no commercial tier — if it's useful to you or your
organization, the best way to support continued development is:

- ⭐ Star the repo
- 💬 Open a [Discussion](https://github.com/DarthCeltic/determinex/discussions) — research questions welcome
- 💖 [Sponsor on GitHub](https://github.com/sponsors/DarthCeltic)
- 🐛 [Report bugs](https://github.com/DarthCeltic/determinex/issues/new?template=bug_report.md) or [request features](https://github.com/DarthCeltic/determinex/issues/new?template=feature_request.md)

---

## Citation

```bibtex
@software{determinex2026,
  author    = {Gurganious, Ryan},
  title     = {Determinex: Compiler-Verified Multi-Agent Code Intelligence with Privacy-Sovereign Cloud AI},
  year      = {2026},
  url       = {https://github.com/DarthCeltic/determinex},
  note      = {AGPLv3}
}
```

---

## License

GNU Affero General Public License v3.0 (AGPLv3) — see [LICENSE](LICENSE) and
[docs/papers/LICENSING.md](docs/papers/LICENSING.md). OSI-approved open source.
Fine-tuned model weights and adapters, once published, are covered by the
same license unless a model card states otherwise. Base model licenses apply:
[Qwen2.5](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B),
[Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-v0.1).

---

<div align="center">

*Determinex · Ryan Gurganious · 2026*

</div>

