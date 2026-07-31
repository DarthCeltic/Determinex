---
title: "Claim Triage — NEEDING NARROWING (partial prior art; structural limitations needed)"
status: DRAFT — for attorney/inventor review only. Not a legal opinion.
date: 2026-06-10
source_sections: WHITE_PAPER.md §3.4, §9.1–9.9, §10, §13; PROJECT_CLOAK.md
---

# Claims Needing Narrowing

These claims have partial prior art coverage but contain distinguishing structural elements.
As drafted below, they likely survive the 7-reference prior art set. However, they may face
103 (obviousness) arguments and benefit from additional limitation to be prosecution-robust.
Attorney judgment required on which limitations to include in independent vs. dependent claims.

---

## NARROW-01: InfoNCE-Trained MLP Bridge for Heterogeneous Architectures

**Staged claim (narrow form):**
> A method for enabling semantic communication between a first language model having a first embedding dimensionality (d1) and a second language model having a second embedding dimensionality (d2), wherein d1 ≠ d2, the method comprising:
> - extracting, from each model separately, mean-pooled input embedding vectors for a shared set of training prompts, without executing a full model forward pass;
> - training, using InfoNCE contrastive loss with temperature ≤ 0.10, a first multilayer perceptron (MLP) encoder that maps d1-dimensional embedding vectors to a shared intermediate space of fixed dimensionality D\_ROSETTA;
> - training a second MLP encoder that maps d2-dimensional embedding vectors to the same D\_ROSETTA space, wherein same-prompt pairs across models are treated as positive pairs and different-prompt pairs as negatives;
> - training corresponding decoder MLPs for each architecture;
> - at inference time, projecting a first model's embedding through its encoder into D\_ROSETTA space and through the second model's decoder into d2-dimensional space; and
> - injecting the projected vector as a soft prefix into the second model's inference context.

**Prior art differentiation:**
- **vs. Moschella 2023:** Trained MLP (not analytical cosine-to-anchors); works across models with different pretraining corpora (not same-distribution requirement); fixed shared space D\_ROSETTA (not relative coordinates)
- **vs. LatentMAS:** Trained artifact (not training-free ridge regression); nonlinear MLP (not linear W\_a); requires d1 ≠ d2 (not same-family assumption)
- **vs. arXiv:2601.06123:** Input embeddings layer (not KV states at layer N); InfoNCE contrastive (not task-specific adapter training)

**Key limitation to preserve:** "d1 ≠ d2" or "different model families" — this is what distinguishes from LatentMAS most cleanly.

**Filing risk:** MEDIUM — combined 103 over Moschella + LatentMAS remains possible; attorney should evaluate whether "trained MLP with InfoNCE + heterogeneous d\_h" is a sufficient combination.

---

## NARROW-02: Compiler-Oracle WAL Training Pair Generation

**Staged claim (narrow form):**
> A method for generating training data for a code-generating language model, comprising:
> - receiving a code modification produced by a language model;
> - applying the code modification to an isolated workspace copy of a repository;
> - invoking a deterministic compiler for the programming language of the repository against the modified workspace;
> - upon compiler failure, recording a write-ahead log entry comprising: the attempted modification, the full compiler error output, and a correction prompt derived from the compiler error; and
> - upon compiler success, marking the modification as training-eligible and adding the (modification, compiler-output) pair to a training corpus;
> - wherein no training sample enters the corpus without passing the deterministic compiler.

**Prior art differentiation:**
- **vs. CodeRL/AlphaCode:** Those use test-execution outcomes as rewards; Determinex specifically uses the **compiler itself** (before tests) as the sole gating signal — a tighter determinism that doesn't require test case coverage
- **vs. SWE-bench eval harness:** Determinex's gate is inline during generation (not post-hoc evaluation); the WAL structure capturing (patch, compile\_errors, correction\_prompt) as a training triplet is distinct from evaluation harnesses

**Key limitation to preserve:** "isolated workspace copy" (git worktree) + "no training sample enters the corpus without passing the deterministic compiler" + WAL structure.

**Filing risk:** LOW-MEDIUM — The specific WAL training-pair structure and inline compile-gate with automated corpus ingestion appears to be a genuinely novel combination.

---

## NARROW-03: AST-Aware Compilation-Valid Code Obfuscation with Semantic Key

**Staged claim (narrow form):**
> A method for privacy-preserving code analysis by a cloud language model, comprising:
> - performing file and symbol discovery operations against unobfuscated source code to identify code regions relevant to a target modification;
> - constructing an identifier map by traversing the abstract syntax tree (AST) of the source repository, classifying each private identifier by syntactic role, and assigning a deterministic opaque token (x\_NNNN) to each, wherein assignment is alphabetically ordered to be reproducible across invocations;
> - applying the identifier map to the identified code regions, producing obfuscated source code that remains syntactically valid for the programming language and passes compilation by the language compiler;
> - generating a semantic key by splitting each private identifier string on word boundaries and annotating with its syntactic role, wherein the semantic key is computed locally from the identifier map and is not transmitted to any external system;
> - transmitting, to an external language model API: the obfuscated code regions and the semantic key, and no mapping between opaque tokens and original identifiers;
> - receiving an obfuscated code modification from the external language model;
> - applying the inverse identifier map to the obfuscated modification to restore original identifiers; and
> - verifying the restored modification by compilation before application to the repository.

**Prior art differentiation:**
- **vs. US 12,566,889 (Acronis):** AST-level (not string replacement); compilability invariant (not present in Acronis); code-patch output (not document response); semantic key (Acronis has no equivalent)
- **vs. US 20250086310 (IBM):** Deterministic reversible mapping (IBM's stemming/lemmatization is lossy and irreversible); compilation validity preservation (IBM approach destroys syntactic structure)
- **vs. CodeCipher:** The compilability invariant is the clearest differentiator — CodeCipher explicitly achieves 0% compilation rate; this claim recites the opposite property

**Key limitations to preserve:** "remains syntactically valid and passes compilation" + "semantic key not transmitted" + "inverse map restoration" + "verified by compilation before application."

**Filing risk:** LOW — This combination appears to survive all 7 references. The compilability invariant over CodeCipher is the strongest single differentiator.

---

## NARROW-04: Cross-Architecture Latent RAG via Rosetta Re-Projection

**Staged claim (narrow form):**
> A retrieval-augmented generation system comprising:
> - an offline index storing, for each semantic unit of a codebase: (a) a natural-language embedding vector and (b) a compressed key-value cache state captured from a first language model after processing the unit, wherein the KV state is compressed using scalar quantization;
> - a retrieval component that, given a query embedding, performs cosine similarity search against stored natural-language embeddings to identify the K most semantically similar units;
> - a cross-architecture projection component that, when the first language model and the second (generation) language model have different architectures, re-projects the retrieved compressed KV states through a trained encoder/decoder pair into the second model's embedding space; and
> - an injection component that provides the re-projected states as a soft prefix to the second language model's inference context.

**Prior art differentiation:**
- **vs. arXiv:2601.06123, 2605.22863, LatentMAS (all KV-state sharing):** All three assume same-architecture communication. The cross-architecture re-projection step (via Rosetta Stone) is not disclosed in any of these references.
- **vs. standard RAG:** Standard RAG injects text chunks; this claim injects compressed KV states — different input type, different context budget.

**Key limitation to preserve:** "when the first and second language models have different architectures, re-projects through a trained encoder/decoder pair" — this is the element that is not in any reference.

**Filing risk:** MEDIUM — The cross-architecture re-projection is novel, but it depends on the Rosetta Stone claim surviving (NARROW-01). If NARROW-01 faces rejection, NARROW-04 will likely follow.

---

## NARROW-05: Eval-in-Loop Architecture with verified\_locked State

**Staged claim (narrow form):**
> A method for iterative code patch refinement comprising:
> - generating a candidate code patch using a language model;
> - executing an official benchmark test harness against the patched code in an isolated environment;
> - upon any test failure, injecting the complete test failure output into the language model's next prompt alongside the original task specification;
> - repeating for a bounded number of attempts;
> - upon passing all tests with no failures and no test collection errors, recording the patch as `verified_locked` and archiving the patch and test results as immutable evidence;
> - wherein no patch is recorded as `verified_locked` if any test in the harness is in a `not_run`, `skipped`, or `error` state.

**Prior art differentiation:**
- This is specific to the "no not\_run" invariant and the cryptographically-archived evidence artifact
- General retry loops with test output injection are likely prior art; the specific `verified_locked` state with strict `not_run == 0` gating is more novel
- The immutable archive (eval\_report.json + submission.tar.gz) as a gating condition is a specific claim element

**Key limitation to preserve:** "no test in a not\_run or skipped state" as a condition for the verified\_locked transition.

**Filing risk:** MEDIUM — The strict `not_run == 0` invariant is domain-specific (ProgramBench) and may be characterized as an implementation detail. Attorney should evaluate whether this is claim-worthy or better suited as a specification embodiment.

---

## NARROW-04: Cloaked-Pair + DP Aggregation + Cartridge Routing (Combined Fleet Privacy Pipeline)

`[PRIOR mechanisms — DETERMINEX_NODE.md §2 §5–6 / §9 N-14]`

**Staged claim (narrow form, distinguishing elements bolded):**
> A system for privacy-preserving collection of AI-generated code training signal from a
> distributed fleet of user devices comprising:
> - receiving, from each device, code training pairs wherein all private identifiers have
>   been replaced with opaque surrogates at the AST level before transmission (Cloaked-pair
>   format);
> - **re-mapping the opaque-token namespace of each submission to a fresh, per-submission
>   assignment before any cross-client aggregation, such that token identities in the shared
>   corpus have no semantic relationship to any individual client's namespace;**
> - **re-executing each submitted pair in a sealed container to verify compiler verdicts
>   independently, rejecting any pair whose recomputed verdict diverges from the submitted
>   verdict;**
> - applying k-anonymity thresholds and statistical aggregation (differential privacy noise
>   on aggregate statistics) before any pair enters a shared corpus;
> - routing aggregated pairs to a tier-specific corpus cartridge (community, school-sealed,
>   or enterprise-sealed) based on the submitting client's tier designation and consent record;
> - **routing school-designated pairs into a sealed cartridge (sealed by default), wherein
>   promotion to the community corpus requires a multi-condition gate: applicable regulatory
>   compliance review, data-use agreement amendment, data-specific scrubbing verification,
>   differential privacy aggregation confirmation, and a logged authorization record in an
>   append-only transparency ledger — all conditions positively verified — before any
>   cross-tier migration (see NOVEL-14).**

**Prior art landscape:**
- US 12,566,889 (Acronis): obfuscation pipeline only; no fleet ingestion, no aggregation
- US 20250086310A1 (IBM): semantic preprocessing; no fleet architecture
- Federated learning literature (McMahan 2017 et al.): gradient aggregation; not
  training-pair collection; no compiler verification; no AST-level obfuscation
- Secure aggregation (Bonawitz 2017): cryptographic gradient aggregation; not code pairs
- The combined pipeline (Cloak + namespace re-mapping + replay + DP + cartridge routing)
  has no prior art anticipation as a combined system

**Distinguishing elements that must survive narrowing:**
1. Cloak format (opaque-token code pairs, not gradients or model updates)
2. Per-submission namespace re-mapping (NOVEL-12) — distinguishes from simple aggregation
3. Replay verification (NOVEL-10) — distinguishes from trust-based federated systems
4. Sealed-by-default cartridge routing with multi-condition gated promotion pathway (NOVEL-14) — structural gate before any sealed-tier pair migrates to shared corpus

**Why "at risk"** (requiring narrowing, not likely-novel as-is):
The individual components — obfuscation, DP aggregation, federated training corpus collection
— each have prior art. US 12,566,889 is particularly close on the obfuscation element.
The combination is likely novel, but the combination claim will face §103 obviousness
challenges. The replay gate (NOVEL-10) and namespace re-mapping (NOVEL-12) are the
structural elements that most differentiate this from an obvious combination of Acronis +
standard federated aggregation. These must be required elements of any independent claim.

**Key limitation to preserve:** replay verification as a required pipeline stage (not
optional); per-submission namespace re-mapping (not simple passthrough of client x_NNNN
space); sealed-by-default cartridge routing with multi-condition gated promotion pathway
(NOVEL-14) as a required structural element for school/enterprise tiers.

**Filing risk:** MEDIUM — broadest form is at risk; narrowed form with replay gate +
namespace re-mapping + cartridge sealing is likely defensible. Attorney should consider
whether to file as a system claim (easier to read on infringement) or method claim.

---

*All items in this file are risk assessments for attorney/inventor review. Not legal opinions.*
