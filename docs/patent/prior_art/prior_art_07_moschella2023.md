---
title: "Prior Art Analysis — Moschella et al. 2023, Relative Representations (ICLR 2023)"
status: DRAFT — for attorney/inventor review only. Not a legal opinion.
date_fetched: 2026-06-10
---

# Prior Art: Relative Representations — ICLR 2023

## Bibliographic Details

| Field | Value |
|---|---|
| **Title** | Relative Representations Enable Zero-Shot Latent Space Communication |
| **Authors** | Luca Moschella, Valentino Maiorca, Marco Fumero, Antonio Norelli, Francesco Locatello, Emanuele Rodolà |
| **Affiliations** | Sapienza University of Rome / ETH Zurich / IST Austria |
| **arXiv ID** | 2209.15430 |
| **arXiv Submission (v1)** | September 30, 2022 |
| **Venue** | ICLR 2023 Oral (top 5%) |
| **Priority Date (102/103)** | September 30, 2022 (arXiv v1 = earliest public disclosure) |

## Primary Mechanism Disclosed

The paper demonstrates that neural network latent spaces preserve angular structure: the angles between encodings of data points within distinct but similarly-trained latent spaces are invariant. Data point representations are expressed as cosine similarity to a fixed set of anchor points, producing "relative representations" that are invariant to latent isometries and rescalings. Because two models trained on the same data with the same architecture produce isomorphic relative representations, model stitching (composing encoder from one model with decoder from another, without joint training) becomes possible with zero-shot transfer. Validated across images, text, and graph modalities with CNNs, GCNs, and Transformers.

**Core property:** Zero-shot stitching, no training required. Relies on models being trained on the same or overlapping data distributions.

## What This Reference Does NOT Disclose

1. **Requires shared training data distribution.** Zero-shot stitching works when models are trained on overlapping data. The Rosetta Stone is designed explicitly for models that have **different pretraining corpora, different tokenizers, and different architecture lineages** — Qwen2.5-Coder (code-specialized, Chinese company), Mistral-7B (general English), Phi-3 (Microsoft synthetic data). These models share no common training anchor set.

2. **Analytical coordinate transform, not trained artifact.** Relative representations are computed analytically (cosine similarity to anchor points). The Rosetta Stone is a **trained artifact** (`rosetta_v1.pt`) — a persisted set of MLP encoder/decoder network weights. This is a structurally different claim element: a trained model vs. a mathematical transform.

3. **No nonlinear MLP projection networks.** The relative representation method uses cosine-similarity computation (linear inner products), not trained 2-layer MLP networks with ReLU activation.

4. **No InfoNCE contrastive training.** The training-free approach of Moschella et al. does not use or require InfoNCE contrastive learning.

5. **No shared fixed-dimensional intermediate space.** Relative representations map each architecture into its own similarity-to-anchors space; these spaces have the same structure only if the anchor sets match. The Rosetta Stone explicitly projects all architectures into a single shared 4096-dimensional intermediate space.

6. **No code-specific application.** The paper covers images, text (NLP), and graphs. No disclosure of source code, compiler oracles, or code patch pipelines.

7. **No AST-aware obfuscation, no Context Paradox Pattern, no compile-gate.**

8. **No text-space approximation step.** Moschella et al. do not address the problem of injecting projected latent vectors into an unmodified GGUF inference backend via nearest-vocabulary-token approximation.

## Closest-Claim Overlap Assessment

**Risk area (for attorney review):** This is the theoretical foundation cited in the WHITE_PAPER.md Section 10 ("vs. Relative Representations (Moschella et al., ICLR 2023)"). The paper establishes the theoretical basis (angular invariance of latent spaces) that motivates why MLP-trained bridges might work. An examiner could argue Rosetta Stone is obvious over Moschella combined with standard MLP training techniques.

**Counter-argument elements (attorney to validate):**
- Moschella's result is explicitly limited to models trained on **overlapping data**; the Rosetta Stone trains a bridge for models with no shared training data — a technically distinct problem
- The trained MLP artifact vs. analytical transform distinction is a real claim element ("trained encoder/decoder network" appears in claims; "cosine similarity to anchor points" does not)
- WHITE_PAPER.md Section 10 explicitly distinguishes the two approaches: "Determinex uses trained MLP encoder/decoder pairs instead — a supervised approach that trades the zero-shot property for higher alignment accuracy (0.745–0.891 cosine gaps)"
- The per-GGUF offset correction for fine-tune drift is novel over Moschella (fine-tune drift is specific to the GGUF/llama-cpp deployment context, which didn't exist at ICLR 2023)
- The text-space approximation step (nearest-vocab-token injection via llama-cpp-python) has no analog in Moschella

## Key Claim Language That Survives This Reference

- "Training MLP encoder/decoder pairs using InfoNCE contrastive loss on embeddings extracted from models with different architectures and different pretraining corpora"
- "Projecting to a shared intermediate space of fixed dimensionality (D\_ROSETTA) using a trained nonlinear network"
- "Per-architecture offset correction for fine-tune drift"
- "Text-space approximation via nearest-vocabulary-token lookup to enable soft-prefix injection into unmodified inference backends"
- Any claim combining the latent bridge with AST obfuscation (no such combination in Moschella)
- Any claim combining the latent bridge with a compiler oracle / Eval-in-Loop architecture

## Filing Note

Priority date September 30, 2022. Earliest prior art reference in the set. All Determinex disclosures postdate this. It is prior art under 35 USC 102. The differentiation strategy — trained vs. analytical, heterogeneous vs. same-distribution, fixed shared space vs. relative coordinates — is critical.

---
*This document is a risk assessment for attorney/inventor review. It does not constitute legal advice and does not assert legal conclusions about patentability, validity, or freedom to operate.*
