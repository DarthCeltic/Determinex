---
title: "MORPH_REGISTER — Architecture Areas In Flux and Filing Implications"
status: LIVING DOCUMENT — update whenever architecture decisions change
date: 2026-06-10
purpose: >
  Track which parts of the Determinex architecture are actively evolving and flag
  implications for claim scope and filing timing. A claim covering a feature
  that is about to change structurally may need to be written at a higher
  abstraction level, or delayed until the design stabilizes.
  For attorney/inventor review. Not a legal opinion.
---

# MORPH_REGISTER

This register tracks architecture areas that are actively in flux as of the filing-prep date.
Each entry documents: current state, known change vectors, and implications for claim language.

---

## M-01: Rosetta Stone Layer — Input Embedding vs. KV State

**Current state:** Layer 1 (active) = Semantic DSL text messages. Layer 2 (v1.5) = soft prefix injection via llama-cpp-python (mean-pooled input embeddings, `llama_batch.embd != NULL` mode). Layer 3 (Phase 3) = KV-cache broadcast (not yet built).

**Change vector:** Layer 3 will move the communication mechanism from input embedding space to mid-network KV-state space — a structurally different level of operation. Claims drafted specifically for "input embedding projection" survive Layer 3 addition but may need to be broadened to cover both.

**Filing implication:**
- Layer 2 is implemented and validated (`rosetta_v1.pt`, April 2026) → stable for immediate claiming
- Layer 3 is published in WHITE_PAPER.md §13 as a design record → establishes prior art but may benefit from provisional claiming before the LatentMAS / KV-cache-alignment prior art space gets more crowded
- Claim language for Layer 2: "projecting input embedding vectors through trained MLP encoder/decoder" — does NOT need to be amended when Layer 3 ships
- Claim language for Layer 3: "capturing and re-projecting KV cache states" — separate claim family or dependent claims
- **Recommendation for attorney:** Write independent claims for Layer 2 now. Include Layer 3 as continuation/CIP claims tied to same provisional filing date.

---

## M-02: Project Cloak Language Coverage (Python only → 10 languages)

**Current state:** As-deployed Cloak is Python-specific (AST via `ast.NodeVisitor`). CLAUDE.md and PROJECT_CLOAK.md note "C-Style: NOT NOW — SWE-bench is Python only; generalize post-launch." The CLAUDE.md pipeline-hardening section documents Ruby/PHP/Java compile handling, suggesting multi-language work is in progress.

**Change vector:** Multi-language extension is planned. The same pipeline (StdlibManifest → IdentifierClassifier → SymbolMap → ASTTransformer → ...) will be extended with language-specific AST parsers (tree-sitter) for Go, Rust, Java, TypeScript, JavaScript, Ruby, PHP, C, C++.

**Filing implication:**
- Claims drafted specifically for "Python AST via `ast.NodeVisitor`" are narrow — they miss the generalizable architecture
- Claims should be drafted at the level of "AST-aware identifier classification using a language-appropriate parser" to cover the multi-language generalization
- The core inventive concept (AST-level parsing → deterministic opaque token map → compilability-preserving transform → local semantic key → bidirectional restoration) is language-agnostic and claims should reflect this
- **Recommendation for attorney:** Draft independent claims at the abstract pipeline level. Use Python implementation as a preferred embodiment example. Include generic "language-appropriate AST parser" language.

---

## M-03: D\_ROSETTA Dimensionality (Fixed at 4096) — RESOLVED 2026-06-11

**RESOLVED — NO SPEC/CODE MISMATCH. Two different generations of training code.**

**rosetta_v1.pt (validated production artifact — verified by SHA256):**
Metadata embedded in artifact (read 2026-06-11):
- `d_rosetta: 4096` — WHITE PAPER IS CORRECT ✓
- `anchor: pure_infonce` — WHITE PAPER InfoNCE claim IS CORRECT ✓
- 5 architecture families: llama (4096), mistral (4096), qwen2 (3584), phi3 (3072), deepseek2 (4096)
- SHA256 integrity check: PASS — `7589dd55512c9333f370a483ff8fcb60297ca50a44be1fb7057a3d54805a1eab`
  (computed over tensor values in sorted key order, excluding sha256 field — correct implementation)

**rosetta_v1_4arch.pt (4-arch ablation variant):**
- `d_rosetta: 4096`, `anchor: pure_infonce`, 4 families (llama dropped)

**rosetta/train_rosetta.py (v2 redesign — NOT the script that produced rosetta_v1.pt):**
- `HUB_DIM = 2048`, cosine_alignment+MSE loss, 6 families (smaller/newer model variants)
- Different save format (directory-based) — incompatible with rosetta_v1.pt flat-file format
- This is a redesign targeting future v2 training, not yet run to produce a validated artifact
- The spec describes rosetta_v1.pt correctly; this file is irrelevant to the patent description

**Claim language implication (unchanged from original M-03):**
- Claims should NOT recite "4096" as a numeric requirement
- Correct form: "a shared intermediate dimensionality fixed across all participating model families"
- InfoNCE can be named as the specific training method in preferred embodiment section

**Separate finding — NOVEL-07 description is inaccurate (see claims_likely_novel.md):**
The SHA256 verification order in WHITE_PAPER.md is described incorrectly. The actual implementation
(correct, documented in `scripts/determinex_rosetta.py`) uses `torch.load(..., weights_only=True)` to
prevent pickle RCE, THEN computes tensor-value SHA256 for weight integrity. The white paper says
"verified before torch.load()" which is backwards. NOVEL-07 claim language updated accordingly.

**Current state:** D\_ROSETTA = 4096 is hardcoded, matching Llama-8B/Mistral-7B native dimension. Per WHITE_PAPER.md §3.4: "D_ROSETTA = 4096 (matches Llama-8B/Mistral-7B natively — minimal overhead for the dominant model sizes)."

**Change vector:** As larger model families (Llama-70B with d\_h = 8192, or new architecture families) become deployment targets, D\_ROSETTA may need to be 8192 or dynamically configurable.

**Filing implication:**
- Claims should NOT recite "D\_ROSETTA = 4096" as a specific numeric limitation
- Claims should recite "a shared intermediate space of fixed dimensionality" or "a shared intermediate dimensionality selected from the set of embedding dimensionalities of the model families" — leaving room for 4096, 8192, or other values
- **Recommendation for attorney:** Avoid specific numeric dimensionality in independent claims. Include the 4096 value only in dependent claims as an exemplary embodiment.

---

## M-04: Text-Space Approximation Path (Layer 2) vs. Direct KV Injection (Layer 3)

**Current state:** Layer 2 uses a text-space approximation: the Rosetta-projected vector is mapped to nearest-vocabulary-tokens and injected as token embeddings via llama-cpp-python. This is described as "the currently deployed text-space approximation path" with "honest limitation: mean-pooling compresses the full sequence to a single vector."

**Change vector:** Layer 3 bypasses text-space approximation entirely, injecting KV states directly at mid-network layers.

**Filing implication:**
- "Text-space approximation via nearest-vocabulary-token lookup" is a claim element specific to Layer 2 — it may be characterized as an engineering workaround for the llama-cpp-python interface limitation, not as a core inventive concept
- The core inventive concept of Layer 2 is the "trained MLP projection + injection as soft prefix" — the nearest-vocab-token step is implementation detail
- **Recommendation for attorney:** Do not make "nearest vocabulary token lookup" a required element of independent claims. It can be a dependent claim or specification embodiment.

---

## M-05: Ethics Oracle (L5) — Designed but Not Built

**Current state:** The Ethics Oracle is documented in `docs/policy/ETHICS_ORACLE.md` and WHITE_PAPER.md §5 as designed but not yet implemented.

**Change vector:** Implementation is planned as part of the L0–L5 safety architecture. Design is complete. The specific mechanism (deterministic behavioral compliance gate via formal rules + static analysis, not LLM-based) is documented.

**Filing implication:**
- The Ethics Oracle design is published and constitutes a prior art disclosure for third parties
- As an unbuilt feature, it cannot be claimed as "reduced to practice" — only as a design record
- If the Ethics Oracle implements patentable concepts (deterministic behavioral compliance checking for AI systems without LLM judges), a provisional covering these concepts would be valuable
- **Recommendation for attorney:** Include Ethics Oracle architecture description in the specification as a system embodiment. Consider whether its core claim (deterministic behavioral compliance gate) warrants inclusion in the claim set.

---

## M-06: Eval-in-Loop — Benchmark Expansion (ProgramBench → SWE-bench → HumanEval → ...)

**Current state:** Eval-in-Loop is validated on ProgramBench (46 confirmed locks). SWE-bench uses the same pattern with Docker harness. Extension to HumanEval, LiveCodeBench, Terminal-Bench planned.

**Change vector:** The specific benchmark (ProgramBench, SWE-bench) is an embodiment; the Eval-in-Loop concept is generalizable to any deterministic test harness.

**Filing implication:**
- Claims should not recite "ProgramBench" or "SWE-bench" as required elements
- The generalizable concept: "inline execution of an official benchmark harness during the generation retry loop, with harness output injected into the next prompt, gating a `verified_locked` state transition on full-suite pass"
- **Recommendation for attorney:** Draft Eval-in-Loop claims at the level of "deterministic external test harness" without naming specific benchmarks.

---

## M-07: Compile-Gate Worktree Isolation (git worktree) — Isolation Method May Change

**Current state:** Compile-gate uses `git worktree add` to create an isolated copy before compile check. This avoids contaminating the main workspace.

**Change vector:** Alternative isolation methods (Docker, sandboxed subprocess, tmpfs copy) may be used in future deployments. The worktree mechanism is Linux/git-specific.

**Filing implication:**
- Claims should recite "an isolated workspace copy" or "an isolated execution environment" rather than "git worktree"
- The inventive concept is the **isolation** (so a failed compile attempt cannot corrupt the main repository state) not the specific git-worktree mechanism
- **Recommendation for attorney:** Use "isolated copy of the repository" as the claim language; git worktree is a preferred embodiment.

---

## M-08: LoRA Adapter Routing — vLLM Dependency

**Current state (Phase 3 — not yet built):** Dynamic Task-Vector Routing depends on vLLM's multi-LoRA serving feature (hot-swap without base weight reload).

**Change vector:** vLLM's API may change. Alternative inference backends (llama-cpp-python native LoRA, Ollama LoRA) could be used instead.

**Filing implication:**
- Claims should not recite "vLLM" as a required element
- The inventive concept: "DAG-step task-type declaration driving dynamic adapter selection based on compile-pass-rate registry, without reloading base model weights"
- **Recommendation for attorney:** Draft as "a serving backend supporting dynamic adapter selection" rather than naming vLLM specifically.

---

## M-09: Provenance / Attribution Sidecar — Implemented 2026-06-10

**Current state:** Built and wired into both generation hot paths (`scripts/hive/executor.py` and `scripts/determinex_programbench_agent.py`) as a fire-and-forget sidecar. Three-tier detection: verbatim reproduction (≥50 tokens), substantial similarity (≥30 tokens or ≥25% filtered-bigram Jaccard), inspiration (≥15% filtered-bigram Jaccard). License-aware policy: permissive OSS (MIT, Apache-2.0, etc.) → attribution tag only; non-permissive → alert (enforce mode) or warning (observe mode). Reference sources seeded from `corpus/references/` with per-directory `metadata.json`.

**Change vector:** Reference corpus will grow as more sources are registered. Thresholds may be tuned after calibration. License-aware policy may be extended (copyleft obligations).

**Filing implication:**
- This represents a bidirectional IP sovereignty system: **Cloak** prevents proprietary outbound leakage; **provenance tagger** documents inbound attribution
- The combined system (outbound obfuscation + inbound attribution tracking on the same corpus pipeline) may constitute a novel IP-sovereignty architecture claim
- The filtered-bigram Jaccard calibration against code (stopword removal for programming keywords) is an engineering choice that distinguishes from naive document-similarity approaches
- Attribution log at `logs/copyright_guard/attribution.jsonl` is an append-only audit trail supporting the "zero-leakage + complete provenance" IP sovereignty narrative
- **Implementation date:** 2026-06-10 (initial wiring: `ff77577d7`; calibration + mode flag: this commit)
- **Recommendation for attorney:** Consider whether the bidirectional IP sovereignty architecture (Cloak + provenance) warrants a combined claim family separate from the Cloak-only claims.

---

## M-10: Lunarian Node v0 — Fleet Signal Aggregation (Design-Only, Post-Announce)

**Current state:** Design document only. `docs/papers/LUNARIAN_NODE.md` drafted 2026-06-11.
Zero code written. Build is explicitly post-announce.

**Design:** Eight-stage ingestion pipeline:
(1) Intake API → (2) Provenance Guard → (3) Replay Verification → (4) Eligibility Gate →
(5) DP Aggregation → (6) Cartridge Router → (7) Training Runs → (8) Signed OTA Deltas.
Submission schema v0.1 defined (JSON, ed25519-signed, Cloaked-pair format). Four
anti-poisoning threat vectors documented with v0 mitigations.

**Change vector:** All four `[NEW]` mechanisms (replay gate, corpus-release gating, namespace
re-mapping, symmetric OTA gate) will be implemented during v0 build. The core pipeline
structure is stable enough for provisional claiming. Open questions in LUNARIAN_NODE.md §10
(test-surface inclusion, influence cap value, school cartridge mix policy) do not block
provisional filing — they affect implementation detail, not the structural claim elements.

**Filing implication:**
- All four `[NEW]` mechanisms are design-only at filing time — treatment identical to Ethics
  Oracle (M-05) and Layer 3 KV broadcast (M-01): include in provisional spec as written-
  description material to establish priority date; label clearly as not yet reduced to practice
- The `[PRIOR mechanism, NEW framing]` element (symmetric OTA gate, NOVEL-13) is directly
  enabled by existing verified_locked code — that element IS enabled, even though the
  full fleet pipeline is not built
- Claims should be drafted at the mechanism level (replay verification as an abstract method
  claim), not at the v0 build scope level (intake API, flat-file corpus store)
- **Recommendation for attorney:** File NOVEL-10 (replay gate) as an independent method
  claim. File NOVEL-11, NOVEL-12, NOVEL-13 as dependent claims or separate independent
  claims. File NARROW-04 as a system claim requiring NOVEL-10 and NOVEL-12 as elements.

---

## M-11: Lunarian Node v0 — Owner Redline Resolution (2026-06-11)

**Current state:** LUNARIAN_NODE.md updated from "DRAFT FOR REDLINE" to "OWNER-RESOLVED v0.2"
via 5-verdict redline session on 2026-06-11. All §10 open questions resolved.

**Resolved verdicts:**
1. **Test surface (§3 + §5.3 + §5.3a):** Dual-mode schema — `test_ref` (harness_id +
   version_hash) preferred; inline `test_surface` fallback for bespoke/enterprise. Node
   replays against own pinned harness mirror when test_ref resolves; submitted content not
   executed if canonical copy exists.
2. **Influence caps (§6.1):** Per-client ≤1% of any training batch; ≤5% of any
   pattern-family slice; new-client ramp 0.25% until reputation threshold met. Shared/
   community corpus only; sealed cartridges exempt. Claim language: "configurable per-source
   influence threshold with reputation-conditioned ramp."
3. **School cartridge (§4):** SEALED-BY-DEFAULT + GATED PROMOTION PATHWAY. Promotion
   requires ALL of: COPPA/FERPA review + district agreement amendment + minor-specific scrub
   audit + DP aggregation + transparency-ledger sign-off. NOVEL-14 added to
   `claims_likely_novel.md` (tier-gated corpus promotion; needs triage).
4. **Replay host (§5.3a):** Dedicated sealed host REQUIRED (not preferred). Zero shared
   hosts/volumes/credentials with eval fleet. No outbound network; ephemeral containers;
   resource caps. Eval-fleet isolation is an integrity requirement for published lock claims.
5. **Consent (§10 Q5):** Resolved as drafted — versioned-consent-hash mechanism is
   provisional disclosure material.

**Filing implication:** All verdicts are design-only. No change to build scope or post-
announce commitment. LUNARIAN_NODE.md §10 all five questions now RESOLVED. Claim count
updated: 83 → 84 (NOVEL-14 added to `claims_likely_novel.md`).

---

## Change Log

| Date | Entry | Change |
|------|-------|--------|
| 2026-06-10 | All | Initial population from architecture review |
| 2026-06-10 | M-09 | Added: provenance sidecar implemented, implementation evidence dated |
| 2026-06-11 | M-03 | RESOLVED: false alarm — rosetta_v1.pt artifact confirmed 4096/InfoNCE (white paper correct); train_rosetta.py is a v2 redesign, not the production training script. SHA256 PASS. NOVEL-07 corrected to reflect actual 3-layer security impl. |
| 2026-06-11 | M-10 | Added: Lunarian Node v0 fleet signal aggregation — design-only, post-announce. NOVEL-10–13 + NARROW-04 added to claim_charts/. |
| 2026-06-11 | M-11 | Added: Lunarian Node v0 owner redline resolution — 5 verdicts applied, spec bumped to OWNER-RESOLVED v0.2, NOVEL-14 added (tier-gated corpus promotion). |

---

*This document is a risk assessment for attorney/inventor review. It does not constitute legal advice. Update this register whenever a significant architecture decision changes that could affect claim scope.*
