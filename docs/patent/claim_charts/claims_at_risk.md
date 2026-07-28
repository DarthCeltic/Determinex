---
title: "Claim Triage — AT RISK (prior art overlap, may require abandonment or narrow rewrite)"
status: DRAFT — for attorney/inventor review only. Not a legal opinion.
date: 2026-06-10
source_sections: WHITE_PAPER.md §3.4, §9.1–9.9, §10, §13; PROJECT_CLOAK.md
---

# Claims At Risk

These claim concepts have meaningful prior art overlap. As drafted broadly, they would likely
face 102/103 rejection. Options: (1) narrow with specific structural limitations that survive
the reference set, (2) abandon in favor of narrower dependent claims, or (3) accept 103 risk
and argue patentability with claim-specific arguments. Attorney judgment required.

---

## RISK-01: Broad "Obfuscate identifiers before LLM transmission"

**Staged claim concept:**
> A method comprising: receiving source code containing private identifiers; replacing each
> private identifier with an opaque token; transmitting the obfuscated code to a cloud language
> model; receiving a modified code suggestion; restoring the opaque tokens to original identifiers.

**Blocking prior art:**
- US 12,566,889 B2 (Acronis, April 2024): "intercept document → obfuscate confidential info → transmit to LLM → deobfuscate response" — structurally identical at this level of abstraction
- US 20250086310 A1 (IBM, September 2023): "preprocess prompt to remove sensitive info before LLM"

**Risk level:** HIGH — Independent claim at this abstraction level will not issue as drafted.

**Narrowing path:** Add ALL of: (a) AST-level parsing, (b) compilability invariant, (c) code-patch output type, (d) semantic key generation, (e) deterministic bidirectional map. See `claims_needing_narrowing.md` NARROW-03.

---

## RISK-02: Broad "Train MLP to bridge heterogeneous latent spaces"

**Staged claim concept:**
> A method comprising: extracting embeddings from a first language model; extracting embeddings from a second language model with a different architecture; training a neural network to map between the embedding spaces; using the trained network at inference time to transfer semantic context between the models.

**Blocking prior art:**
- Moschella et al. 2023 (ICLR): establishes angular invariance of latent spaces and zero-shot model stitching — theoretical framework for the approach
- LatentMAS arXiv:2511.20639 (Nov 2025): latent collaboration replacing text, linear alignment matrix
- arXiv:2601.06123 (DeepMind, Jan 2026): trained adapters bridging KV caches between model instances

**Risk level:** MEDIUM-HIGH — The specific combination of InfoNCE + MLP + shared intermediate space survives (see `claims_likely_novel.md` NOVEL-01), but a claim at this abstraction level faces 103 arguments combining Moschella + standard MLP training.

**Narrowing path:** Recite InfoNCE contrastive loss specifically, D\_ROSETTA fixed intermediate dimension, heterogeneous d\_h architectures with different pretraining corpora. See `claims_needing_narrowing.md` NARROW-01.

---

## RISK-03: Broad "KV-state communication between LLM agents"

**Staged claim concept (from §13.2 Latent RAG):**
> A method for retrieval-augmented generation comprising: storing compressed key-value cache states from previous model inferences; retrieving compressed states based on semantic similarity; injecting decompressed states into a target model's context.

**Blocking prior art:**
- arXiv:2601.06123 (DeepMind, Jan 2026): trained adapters for KV cache communication
- arXiv:2605.22863 (LCF, May 2026): compressed KV matrix adapters for inter-model communication
- LatentMAS (Nov 2025): KV cache state sharing between agents

**Risk level:** HIGH for Phase 3 Latent RAG claims — the KV-state-sharing space is crowded as of mid-2026.

**Narrowing path:** The distinguishing element is **cross-architecture Rosetta Stone re-projection** (a model indexed the content; a different-architecture model retrieves and uses it). If the KV state was produced by a different architecture than the consuming model, Rosetta is required — this combination is not disclosed in any reference. See `claims_needing_narrowing.md` NARROW-04.

---

## RISK-04: "Compiler output as training reward signal" (broad)

**Staged claim concept:**
> A system for training a language model wherein: the language model generates code; the code is compiled using a deterministic compiler; the compilation result is used as a training reward signal.

**Blocking prior art:**
- AlphaCode (DeepMind, 2022) and similar compile-and-test approaches use compilation results as part of training evaluation
- SWE-bench and similar frameworks use test execution as evaluation signals
- CodeRL (Le et al., 2022) uses unit test results as RL reward signals

**Note:** Prior art search on this concept specifically requires a focused patent and academic search beyond the 7 references in this package. The references provided do not directly anticipate this claim, but the general space of "use compiler/test output as code model training signal" is likely populated.

**Risk level:** MEDIUM — The specific Determinex combination (WAL records per attempt, (patch, compile\_errors, correction\_prompt) training triplets, `training_eligible` gate, automated flywheel retrain without human review) is likely narrower than what exists in prior art. But broad claims on "compiler as reward" warrant further search.

**Narrowing path:** Narrow to the specific WAL structure and automated flywheel mechanism. See `claims_needing_narrowing.md` NARROW-02.

---

## RISK-05: "Send semantic vector instead of text between models"

**Staged claim concept (Rosetta Stone mobile/edge application §10):**
> A method comprising: generating a semantic representation of context using a large language model; transmitting the semantic representation as a projected vector to a smaller language model; the smaller language model conditioning its generation on the projected vector without receiving the full text context.

**Blocking prior art:**
- LatentMAS (Nov 2025): replaces text-based inter-agent messages with last-layer hidden-state embeddings
- arXiv:2601.06123 (DeepMind): KV cache sharing as alternative to text transmission
- arXiv:2605.22863 (LCF): compact KV adapter transmission

**Risk level:** MEDIUM — The concept of "transmit latent vector not text" is disclosed by LatentMAS and the KV-cache papers. The specific mobile/edge application and the 16KB bandwidth figure are presentation elements, not claim-differentiating structure.

**Narrowing path:** Add specific structural elements (InfoNCE-trained MLP, heterogeneous d\_h, text-space approximation step) and the privacy property (projected vector is not decodable to original text without the local SymbolMap).

---

*All items in this file are risk assessments for attorney/inventor review. Not legal opinions. Attorney should prioritize these for prosecution strategy prior to filing.*
