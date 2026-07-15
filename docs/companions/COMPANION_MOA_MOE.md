---
name: moa-moe
description: |
  Load when user asks how Determinex compares to Mixture of Experts, Mixture of Agents,
  multi-agent frameworks (AutoGen, CrewAI, LangGraph), or ensemble methods. Load when
  user asks what makes Determinex architecturally different from standard multi-agent systems,
  or how the Rosetta Stone / latent-space coordination works at a high level.
  Do NOT load for UX or developer experience questions. Do NOT load for cloak/privacy questions.
depends: []
---

# Mixture of Agents vs. Mixture of Experts: What Determinex Is and Is Not

*A companion to the Determinex white paper. Ryan Gurganious · Lunarian Data Systems · 2026*

---

## The Naming Problem

AI architecture terminology is imprecise. "Multi-agent," "mixture of experts," "mixture of agents," "ensemble," "swarm" — these terms overlap, conflict, and are used inconsistently across papers and products.

Determinex is often described as a multi-agent system. That is correct. It is sometimes compared to Mixture of Experts (MoE) architectures. That comparison is mostly wrong in the ways that matter. And the emerging term Mixture of Agents (MoA) — distinct from MoE — describes something closer to what Determinex actually does.

This document clarifies the distinctions and explains where Determinex sits.

---

## Mixture of Experts (MoE): What It Is

MoE is an **intra-model** architecture. A single neural network contains multiple "expert" sub-networks (FFN layers). A router (another learned component) selects which experts are activated for each token.

**Key properties:**
- One model, one forward pass
- Experts are sub-networks within the model, not separate models
- The router is learned jointly with the experts
- Experts see the same token representations — they differ in their learned mappings
- Sparse activation: only 2–8 experts typically activate per token

**What MoE is optimizing:** Model capacity at constant inference cost. A 140B MoE model might activate only 22B parameters per forward pass, achieving 140B-scale quality at 22B-scale cost.

**Examples:** Mixtral-8x7B, DeepSeek-V3, GPT-4 (rumored), Grok-1.

---

## Mixture of Agents (MoA): What It Is

MoA is an **inter-model** architecture. Multiple separate models each produce an output. A synthesizer (another model, or a deterministic aggregator) combines the outputs.

**Key properties:**
- Multiple models, multiple forward passes (often run in parallel)
- Each model is a full, independent model — not a sub-network
- The models may have different architectures, sizes, or training
- Output combination is explicit: concatenation, voting, weighted average, or LLM synthesis
- No shared weights; coordination happens at the output level

**What MoA is optimizing:** Output quality through ensemble diversity. Different models make different mistakes. Combining outputs reduces variance.

**Examples:** Together AI's MoA paper (2024), Claude's multi-turn synthesis patterns.

---

## Where Determinex Sits

Determinex is **neither pure MoA nor MoE**. It is a role-specialized, compiler-gated multi-agent system with a latent-space communication layer.

The key distinctions:

### Role specialization, not ensemble diversity

In MoA, multiple models produce the **same type of output** (e.g., all models answer the same question, then a synthesizer combines). The diversity benefit comes from independent error patterns on the same task.

In Determinex, each model produces a **different type of output** for a different role:
- The Architect produces a DAG (planning output)
- The Builder produces code (implementation output)
- The Monitor produces a score and verdict (evaluation output)

These outputs are not alternatives to be combined — they are sequential dependencies in a pipeline. The Architect's output is the input to the Builder. The Monitor's verdict gates the next step.

### Compiler gate, not LLM synthesizer

In MoA, the synthesis step is typically another LLM or a voting aggregator. The "ground truth" is whatever the synthesizer or vote produces.

In Determinex, the synthesis step is the Compiler Oracle. The compiler is not a model — it is a deterministic correctness check with zero hallucination. There is no LLM judge anywhere in the critical path.

### Latent-space coordination, not text-based handoffs

In MoA, models communicate via text: model A's output is the text input to the synthesizer. This is token-efficient at small scale but expensive at the scale of large codebases.

In Determinex, models communicate via the Rosetta Stone: the Monitor's final hidden state is projected into a shared 4096-dimensional latent space and injected directly into the Builder's attention mechanism. The communication happens in continuous embedding space, not token space. This is 6× more token-efficient for structured intent transfer.

### Dynamic routing, not static ensemble

MoA typically uses a fixed ensemble of models for all queries. Determinex routes dynamically: the Architect decides which build steps need escalation (Monitor review), which steps can be executed directly, and which steps need Sentinel involvement. The routing changes based on the current state of the session.

---

## The Honest Comparison

| Property | MoE | MoA | Determinex |
|---|---|---|---|
| Scope | Intra-model | Inter-model | Inter-model |
| Model count | 1 (with sub-networks) | N parallel | 3 sequential with roles |
| Communication | Internal (FFN routing) | Text (output concatenation) | Latent space (Rosetta Stone) |
| Synthesis | Router (learned) | LLM synthesizer or vote | Compiler Oracle (deterministic) |
| Role specialization | No | Typically no | Yes — Architect, Builder, Monitor |
| Training coupling | Joint (router + experts) | Independent | Independent (DSL fine-tune per role) |
| Ground truth | LLM judge or task loss | LLM judge or vote | Compiler |

---

## Why This Distinction Matters

The field is moving toward ensemble methods as a way to improve AI output quality without scaling individual models further. MoA is a genuine improvement over single-model approaches for many tasks.

But MoA and Determinex are optimizing for different things:

- **MoA** optimizes for output quality on a single question, by combining diverse answers
- **Determinex** optimizes for correctness over a multi-step build process, by gating each step with a compiler and routing failures through role-specialized correction

For software engineering tasks, Determinex's approach has a structural advantage: the compiler is a better judge than any LLM synthesizer. It is not a matter of the synthesizer model being too small or too simple — it is that a correct/incorrect binary judgment on compiled code is categorically more reliable than a soft scoring judgment from an LLM.

---

## What Determinex Shares With MoE

One property that Determinex shares with MoE: **sparse activation**.

MoE activates a fraction of its experts per token. Determinex activates a fraction of its agents per step: most steps are handled by the Builder alone. The Monitor activates only when the Builder fails or the session requires adjudication. The Sentinel activates only on Architect escalation.

This means Determinex's effective compute per step is approximately 1.5B parameters (Builder) for most of the session, with 3B and 7B parameters entering only at decision points. The total parameter count is 11.5B (1.5B + 3B + 7B), but the average active parameter count per step is much lower.

---

## The Research Questions This Opens

1. **Optimal role assignment:** The current roles (Architect, Builder, Monitor) were designed by analogy with human software teams. Are these the optimal roles for compiler-gated systems? Would a different decomposition (e.g., Planner, Debugger, Refactorer) perform better?

2. **Latent bridge generalization:** The Rosetta Stone enables latent-space communication between any two models in the trained family set. What is the quality ceiling for latent bridge communication? Does it asymptote at some alignment quality?

3. **MoA + compiler gate hybrid:** Could a standard MoA system (multiple models producing the same output) be improved by adding a compiler gate as the synthesizer? The answer for code is obviously yes — this is exactly what Determinex does for multi-attempt generation. The question is whether this architecture generalizes to other verifiable output domains.

4. **DSL as role-specialization mechanism:** Determinex uses DSL fine-tuning to specialize each model for its role. This is an alternative to MoE routing (which specializes sub-networks by learned routing). Does DSL fine-tuning + role assignment outperform MoE routing for multi-step pipelines with deterministic oracles?

---

## Gotchas — Known Failure Modes

**Do NOT load this Skill when:** The user is asking a general question about what LLMs are, how transformers work, or how to use Ollama. This Skill is for architecture comparison and differentiation, not fundamentals.

- **MoA vs Determinex confusion (parallel vs sequential):** The most common misread is treating Determinex as a parallel ensemble system. It is sequential with role specialization. The Builder does not run in parallel with the Monitor; the Monitor gates the Builder. Clarify this distinction immediately when users compare Determinex to Together AI's MoA paper.
- **Rosetta Stone = latent bridge, not fine-tuning:** The Rosetta Stone projects hidden states between model families via 2-layer MLP encoder/decoder pairs. It is not a fine-tuning technique. It does not change model weights. It adds a lightweight projection layer at inference time. Don't conflate it with LoRA or DSL fine-tuning.
- **Sparse activation claim requires qualification:** Determinex's "sparse activation" analogy to MoE is valid but inexact. MoE sparsity is within a single forward pass. Determinex's sparsity is across sequential calls with VRAM swapping on Tier 0 hardware. The effective compute savings are real but the mechanism is different — don't overstate the analogy.
- **Compiler Oracle is not a model:** Never describe the Compiler Oracle as an "AI judge" or a "verification model." It is `rustc`, `go build`, `tsc`, `python -c`. It is deterministic. The distinction is the entire thesis of the white paper.
- **Role assignment is benchmark-driven, not hardcoded:** Which model fills Architect/Builder/Monitor is determined by the composite scoring formula at runtime, not by fixed model-to-role mapping. If a new model outscores the existing Builder on the micro-eval, it becomes the Builder. Don't describe the role assignments as permanent to a specific model.

---

*Related documents: COMPANION_FLOW_AI.md · COMPANION_VIBE_CODING.md · docs/WHITE_PAPER.md Sections 4 and 12*
