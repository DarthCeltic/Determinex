---
title: "Prior Art Analysis — arXiv:2605.22863 (Latent Cache Flow)"
status: DRAFT — for attorney/inventor review only. Not a legal opinion.
date_fetched: 2026-06-10
---

# Prior Art: arXiv:2605.22863

## Bibliographic Details

| Field | Value |
|---|---|
| **Title** | Latent Cache Flow: Model-to-Model Communication Without Text |
| **Authors** | Maximillian Rossi, Prajwal Raghunath, Eugene Wu |
| **arXiv ID** | 2605.22863 |
| **Submission Date (v1)** | May 19, 2026 |
| **Last Revision (v2)** | June 6, 2026 |
| **Priority Date (102/103)** | May 19, 2026 |

## Primary Mechanism Disclosed

Latent Cache Flow (LCF) extends the Cache-to-Cache (C2C) paradigm by introducing joint compression of KV matrices to create a compact adapter (~13 MB vs ~956 MB for full C2C) that carries model-to-model communication payloads. When the sending and receiving models operate on divergent contexts, the adapter transmits only a condensed representation of the novel information absent from the receiving model's existing KV cache. The paper reports 7.5% F1 and 23% Exact Match improvements over text-based baselines in different-context settings, with 8.5x faster throughput.

## What This Reference Does NOT Disclose

1. **No AST-aware code obfuscation.** The paper addresses communication efficiency between model agents, not source code confidentiality, identifier transformation, or compilable-code privacy.
2. **No cross-architecture bridge (different d\_h).** Focus is on KV matrix compression within same-architecture agent instances. No mechanism for bridging models with different embedding dimensionalities.
3. **No MLP encoder/decoder pairs in the Rosetta Stone sense.** LCF uses KV-matrix compression (quantization of K and V tensors); the Rosetta Stone trains MLP encoder/decoder networks to map between heterogeneous input embedding spaces.
4. **No compiler-verified patch generation or restoration.** No concept of a code patch, compilation oracle, or iterative error-injection retry loop.
5. **No Eval-in-Loop gating.** Evaluation is offline accuracy measurement.
6. **No Context Paradox Pattern.** No separation of discovery vs. transmission phase.
7. **No semantic key generation.** No local word-splitting approach to providing functional context without identifier disclosure.

## Closest-Claim Overlap Assessment

**Risk area (for attorney review):** This reference was submitted May 19, 2026 — **after** the WHITE_PAPER.md initial publication date (May 2026). If the Determinex white paper was publicly accessible before May 19, 2026 (GitHub commit history), this reference may be **post-date** relative to Determinex's disclosure.

Assuming this reference is treated as prior art, it hits the same broad concept space as Latent RAG (Section 13.2): compressing KV states for efficient model-to-model communication. The distinguishing features are:
- Determinex's Latent RAG operates cross-architecture via Rosetta Stone re-projection (LCF does not)
- Determinex's retrieval is **query-driven** (cosine search against indexed KV states); LCF's is **push-based** (sender transmits to receiver)
- Determinex uses **Lloyd-Max scalar quantization per channel** applied to stored KV states in an offline index; LCF uses a learned adapter for compression

**Low direct risk to core Rosetta Stone claim**, which operates at input embeddings, not KV states.

## Filing Note

Priority date May 19, 2026. If the provisional is filed in June 2026 or later, this is a prior art reference. If Determinex's GitHub repository (with WHITE_PAPER.md) was publicly committed before May 19, 2026, the Determinex disclosure itself may pre-date this reference for 102/103 purposes — verify git history of docs/papers/WHITE_PAPER.md.

---
*This document is a risk assessment for attorney/inventor review. It does not constitute legal advice and does not assert legal conclusions about patentability, validity, or freedom to operate.*
