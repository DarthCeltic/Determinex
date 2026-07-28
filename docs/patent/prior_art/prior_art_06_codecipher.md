---
title: "Prior Art Analysis — CodeCipher (arXiv:2410.05797)"
status: DRAFT — for attorney/inventor review only. Not a legal opinion.
date_fetched: 2026-06-10
---

# Prior Art: CodeCipher

## Bibliographic Details

| Field | Value |
|---|---|
| **Title** | CodeCipher: Learning to Obfuscate Source Code Against LLMs |
| **Authors** | Yalan Lin, Chengcheng Wan, Yixiong Fang, Xiaodong Gu |
| **Affiliation** | Fudan University |
| **arXiv ID** | 2410.05797 |
| **Submission Date** | October 8, 2024 |
| **Priority Date (102/103)** | October 8, 2024 |

## Primary Mechanism Disclosed

CodeCipher addresses cloud code-LLM privacy by transforming the LLM's embedding matrix such that each row corresponds to a different word in the original matrix — a learned **token-to-token confusion mapping**. A trainable perturbed embedding matrix E' is optimized by minimizing task-specific loss while applying a discrete optimization strategy that snaps updated continuous vectors to the nearest valid vocabulary token before each gradient update. The paper requires **white-box access** to the target LLM during optimization but reports empirical transfer to black-box models. Evaluation uses CodeLlama-7B for code completion, summarization, and translation tasks.

**Critical finding from the paper:** CodeCipher produces a **0% compilation rate** on obfuscated code. The obfuscated source is explicitly not compilable.

## What This Reference Does NOT Disclose

1. **Does not preserve compilation validity.** The paper explicitly reports 0% compilation success on obfuscated code. Project Cloak's central design invariant is that obfuscated code **passes the compile check** in an isolated worktree before any AI call — enabling the compile-gate pipeline. This is the exact inverse property.

2. **No deterministic reverse-mapping for patch application.** CodeCipher reports ~34% token recovery via LLM-based deobfuscation — far below the threshold required for reliable code patch application. Project Cloak's RestorationEngine uses a deterministic bidirectional SymbolMap (`\bx_\d{4}\b` regex on diff lines), achieving complete restoration.

3. **Requires white-box LLM access.** CodeCipher's optimization phase requires gradient access to the LLM's embedding matrix. Project Cloak requires no model modification and works with any black-box API (DeepSeek, Claude).

4. **No AST-level structural analysis.** The CodeCipher method operates at the embedding/token level with no awareness of code syntax, scoping rules, or identifier semantic roles.

5. **No Context Paradox Pattern.** No separation of discovery vs. transmission phases.

6. **No semantic key generation.** No functional context mechanism to prevent semantic blindness in the LLM.

7. **No compile-gate integration.** With 0% compile rate, integration with a compiler oracle is impossible.

8. **No MLP encoder/decoder latent bridge for inter-model communication.**

## Closest-Claim Overlap Assessment

**Risk area (for attorney review):** This is the **closest prior art specifically for source code obfuscation before LLM transmission**. Both CodeCipher and Project Cloak address the same problem: hiding proprietary source code from cloud LLMs.

However, the approaches are architecturally opposite in a claim-significant way:
- CodeCipher obfuscates at the **embedding matrix level** (model weight modification) → produces code that cannot be compiled
- Project Cloak obfuscates at the **AST identifier level** → produces code that **can** be compiled

**Distinguishing claim language (attorney to validate):**
- "Wherein the obfuscated source code retains syntactic validity such that it is accepted by the language compiler for the corresponding programming language"
- "AST-level identifier transformation that preserves program structure"
- "Deterministic bidirectional identifier map enabling complete patch restoration"
- "Without requiring access to or modification of the language model's parameters or embedding matrix"

The compilation-validity invariant is the strongest single differentiator over CodeCipher. Any independent claim reciting this property is not anticipated by CodeCipher.

**Combined 103 risk:** An examiner might combine CodeCipher's "obfuscate code before LLM" concept with a compiler-integration reference. The response would be: the combination would not be obvious because CodeCipher's own authors show 0% compilation rate, teaching away from compiler integration.

## Filing Note

Priority date October 8, 2024. Predates all known Determinex disclosures. This is the **most technically relevant prior art reference** for the Project Cloak claims and should be prominently addressed in the specification and claim differentiation.

---
*This document is a risk assessment for attorney/inventor review. It does not constitute legal advice and does not assert legal conclusions about patentability, validity, or freedom to operate.*
