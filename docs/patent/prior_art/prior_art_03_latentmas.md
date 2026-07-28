---
title: "Prior Art Analysis — LatentMAS (arXiv:2511.20639)"
status: DRAFT — for attorney/inventor review only. Not a legal opinion.
date_fetched: 2026-06-10
---

# Prior Art: LatentMAS — arXiv:2511.20639

## Bibliographic Details

| Field | Value |
|---|---|
| **Title** | Latent Collaboration in Multi-Agent Systems |
| **Authors** | Jiaru Zou, Ruizhong Qiu, Gaotang Li, Xiyuan Yang, Katherine Tieu, Pan Lu, Ke Shen, Hanghang Tong, Yejin Choi, Jingrui He, James Zou, Mengdi Wang, Ling Yang |
| **arXiv ID** | 2511.20639 |
| **Submission Date (v1)** | November 25, 2025 |
| **Last Revision (v3)** | June 1, 2026 |
| **Conference** | ICML 2026 Spotlight |
| **Priority Date (102/103)** | November 25, 2025 |

## Primary Mechanism Disclosed

LatentMAS enables purely latent collaboration among LLM agents by replacing text-based inter-agent messages with last-layer hidden-state embeddings stored in and transmitted via KV caches. After agent A1 completes its generation pass, the system extracts KV caches from all L transformer layers as paired (K, V) tensors. The successor agent A2 prepends those caches layer-wise to condition its own generation on A1's full internal state without text serialization.

A linear alignment matrix W\_a is computed via ridge regression to map last-layer hidden states back to valid input embeddings, preventing out-of-distribution activations. The framework is training-free and reports 14.6% accuracy gains and 4–4.3x inference speedup across nine benchmarks including MBPP+ and HumanEval+.

## What This Reference Does NOT Disclose

1. **Requires same-architecture, same-family models.** All LatentMAS experiments use Qwen3 models (4B/8B/14B). The framework does not address bridging **architecturally dissimilar** models (different families, different d\_h). The Rosetta Stone's core claim is the trained MLP encoder/decoder bridge enabling communication between heterogeneous architectures (Llama ↔ Mistral ↔ Qwen2 ↔ Phi-3 ↔ DeepSeek2, with d\_h varying from 2048 to 4096).

2. **Linear alignment matrix only.** W\_a is computed via ridge regression — a linear transform. The Rosetta Stone uses trained **nonlinear MLP** encoder/decoder pairs (2-layer MLPs with ReLU activation) and InfoNCE contrastive training. This is a structurally distinct approach.

3. **No training step.** LatentMAS is "training-free" (a claimed feature). Rosetta Stone requires a training phase to produce `rosetta_v1.pt` — a distinct artifact not present in LatentMAS.

4. **No AST-aware code obfuscation.** No code privacy mechanism.

5. **No compiler-verified patch restoration.** No compilation oracle, no patch validation.

6. **No Eval-in-Loop gating.** No iterative compile-fail-retry loop.

7. **No semantic key generation or Context Paradox Pattern.**

8. **No shared intermediate dimensionality target (D\_ROSETTA = 4096).** LatentMAS uses direct KV cache concatenation at native model dimensions; Rosetta Stone projects all architectures into a shared 4096-dim space.

## Closest-Claim Overlap Assessment

**Highest-risk reference in the set** for the Rosetta Stone claim set. LatentMAS:
- Is an ICML 2026 spotlight (high-visibility venue)
- Addresses the same general concept: latent-space inter-model communication replacing text
- Has priority date November 25, 2025

**Distinguishing language needed (attorney to validate):**
- "Training-free via ridge-regression linear alignment" vs. "trained nonlinear MLP encoder/decoder pairs via InfoNCE contrastive loss"
- "Same-architecture model instances (Qwen3 family)" vs. "heterogeneous architectures with different embedding dimensionalities"
- "KV cache layer-wise concatenation at native dimensions" vs. "projection into a shared fixed-dimensional intermediate space (D\_ROSETTA = 4096)"
- "Latent communication between agents in the same model family" vs. "latent bridge enabling a 1.5B Qwen2.5-Coder to receive semantic context from a 7B Mistral"

The Determinex Rosetta Stone is specifically motivated by the **consumer-VRAM constraint** requiring specialist models of different sizes and families to collaborate — a constraint that makes same-architecture assumptions impractical. This is a meaningful technical differentiator.

## Key Claim Language That Survives This Reference

- "InfoNCE-trained MLP encoder/decoder pairs for heterogeneous embedding spaces of different dimensionality"
- "Shared intermediate space D\_ROSETTA projecting architecturally distinct model families"
- "SHA256 pre-load verification of the trained artifact"
- "Per-GGUF offset correction for fine-tune drift"
- Any claim specifically combining Rosetta Stone with Project Cloak (obfuscated latent communication)
- Any claim combining Rosetta Stone with Compiler Oracle / Eval-in-Loop

## Filing Note

Priority date November 25, 2025. If a provisional was not filed before this date, this is a prior art reference requiring careful claim differentiation as described above. **Attorney should evaluate whether the Rosetta Stone can be distinguished on the "heterogeneous architecture" dimension alone as a sufficient distinguishing limitation.**

---
*This document is a risk assessment for attorney/inventor review. It does not constitute legal advice and does not assert legal conclusions about patentability, validity, or freedom to operate.*
