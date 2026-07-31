---
title: "FILING_READINESS — Provisional Patent Application Checklist"
status: NOT READY — STAGING
date: 2026-06-10
inventor: Ryan Gurganious
assignee: Ryan Gurganious (Pending Registration)
warning: >
  DO NOT change PATENT_FILED status anywhere in this repository until a provisional
  application number has been assigned by the USPTO. This document is a staging
  checklist only.
---

# Filing Readiness Checklist

**Overall status: NOT READY — STAGING**

This document tracks readiness for a USPTO provisional patent application covering the
four novel architectural contributions of Determinex. It does not constitute legal advice.
Attorney engagement is required before filing.

---

## Claim Set Summary (84 Staged Claims Across 5 Contribution Areas)

| Contribution | Claim Concepts | Triage Status | Priority |
|---|---|---|---|
| **Project Cloak** (AST-aware privacy sovereignty) | ~25 | 1 at risk (broad), 2 needing narrowing, 6 likely novel | HIGH |
| **Rosetta Stone** (Latent Bridge) | ~20 | 2 at risk (broad), 2 needing narrowing, 3 likely novel | HIGH |
| **Compiler Oracle / Eval-in-Loop** | ~12 | 1 at risk (broad), 1 needing narrowing, 2 likely novel | MEDIUM |
| **Latent RAG + Task-Vector Routing** (Phase 3) | ~8 | 2 at risk (broad), 1 needing narrowing, 2 likely novel | MEDIUM |
| **Determinex Node** (Fleet Signal Aggregation) | ~19 | 0 at risk, 1 needing narrowing (NARROW-04), 5 likely novel (NOVEL-10–14; NOVEL-14 needs triage) | HIGH — file before announce |

For full claim triage, see:
- [`claim_charts/claims_at_risk.md`](claim_charts/claims_at_risk.md)
- [`claim_charts/claims_needing_narrowing.md`](claim_charts/claims_needing_narrowing.md)
- [`claim_charts/claims_likely_novel.md`](claim_charts/claims_likely_novel.md)

---

## Checklist — Required Before Provisional Filing

### A. Technical Documentation

| # | Item | Status | Notes |
|---|---|---|---|
| A1 | White paper with full architecture description | DONE | `docs/papers/WHITE_PAPER.md` (rev. 2026-06-10) |
| A2 | Project Cloak detailed technical spec | DONE | `docs/papers/PROJECT_CLOAK.md` |
| A3 | Rosetta Stone training methodology documented | **DONE — VERIFIED 2026-06-11** | Artifact inspection confirms WHITE_PAPER.md is correct: D_ROSETTA=4096, InfoNCE (anchor=pure_infonce), 5 families. `rosetta/train_rosetta.py` is a v2 redesign, not the script that produced rosetta_v1.pt. SHA256 PASS: 7589dd55... See M-03 in MORPH_REGISTER.md. |
| A4 | Compiler Oracle design documented | DONE | WHITE_PAPER.md §3.6 |
| A5 | Eval-in-Loop architecture documented | DONE | WHITE_PAPER.md §8.4 |
| A6 | Latent RAG design documented (Phase 3) | DONE | WHITE_PAPER.md §13.2 |
| A7 | Task-Vector Routing design documented (Phase 3) | DONE | WHITE_PAPER.md §13.3 |
| A8 | Ethics Oracle design documented | DONE | `docs/policy/ETHICS_ORACLE.md` |
| A9 | Benchmark validation results (ProgramBench) | **NEEDS REDO** — historical "47 locks" claim invalidated 2026-06-30 by provenance audit (counted upstream source builds, not reimplementations; honest count is 0/200 legitimate). Do not cite the old figure in any filing. | `corpus/programbench/eval_index.json`, `docs/papers/PROGRAMBENCH.md` correction banner |
| A10 | Rosetta Stone validation results (5 architecture pairs) | DONE | WHITE_PAPER.md §3.4 (Table) |
| A11 | Cloak zero-leakage audit pass | DONE | `logs/swebench/clean_ablation/SUMMARY_clean.md` |
| A12 | Determinex Node v0 fleet architecture documented | DONE | `docs/papers/DETERMINEX_NODE.md` — provisional written-description material; all [NEW] mechanisms design-only, post-announce build |

### B. Prior Art Analysis

| # | Item | Status | Notes |
|---|---|---|---|
| B1 | arXiv:2601.06123 (KV cache alignment) analyzed | DONE | [`prior_art/prior_art_01_kv_cache_alignment.md`](prior_art/prior_art_01_kv_cache_alignment.md) |
| B2 | arXiv:2605.22863 (Latent Cache Flow) analyzed | DONE | [`prior_art/prior_art_02_latent_cache_flow.md`](prior_art/prior_art_02_latent_cache_flow.md) |
| B3 | LatentMAS analyzed | DONE | [`prior_art/prior_art_03_latentmas.md`](prior_art/prior_art_03_latentmas.md) |
| B4 | US 12,566,889 analyzed | DONE | [`prior_art/prior_art_04_us12566889.md`](prior_art/prior_art_04_us12566889.md) |
| B5 | US 20250086310A1 analyzed | DONE | [`prior_art/prior_art_05_us20250086310a1.md`](prior_art/prior_art_05_us20250086310a1.md) |
| B6 | CodeCipher analyzed | DONE | [`prior_art/prior_art_06_codecipher.md`](prior_art/prior_art_06_codecipher.md) |
| B7 | Moschella 2023 analyzed | DONE | [`prior_art/prior_art_07_moschella2023.md`](prior_art/prior_art_07_moschella2023.md) |
| B8 | **Full professional prior art search (attorney-directed)** | **NOT DONE** | Required before filing. The 7 references above are inventor-identified, not a complete search. |
| B9 | CodeRL, AlphaCode, SWE-bench compiler-reward prior art search | NOT DONE | Needed for Compiler Oracle claims |
| B10 | vLLM multi-LoRA prior art search | NOT DONE | Needed for Task-Vector Routing claims |
| B11 | Git worktree isolation prior art search | NOT DONE | Needed for Compile-Gate claims |

### C. Attorney Engagement

| # | Item | Status | Notes |
|---|---|---|---|
| C1 | Patent attorney engaged | NOT DONE | Required. No provisional can be filed without attorney review. |
| C2 | Inventor disclosure meeting scheduled | NOT DONE | Ryan Gurganious + attorney walkthrough of architecture |
| C3 | Assignment agreement drafted | NOT DONE | Ryan Gurganious (pending registration) |
| C4 | Entity status determination (micro/small entity) | NOT DONE | Affects filing fees |
| C5 | NDA with attorney for confidential source code review | NOT DONE | Attorney will need access to scripts/determinex_cloak/ |

### D. Claim Drafting

| # | Item | Status | Notes |
|---|---|---|---|
| D1 | Independent claim 1 — Project Cloak (NARROW-03) | NOT DONE | Highest-priority independent claim; see claim_charts/ |
| D2 | Independent claim 2 — Rosetta Stone (NARROW-01) | NOT DONE | Second-highest priority |
| D3 | Independent claim 3 — Compiler Oracle WAL (NARROW-02) | NOT DONE | |
| D4 | Dependent claims — Context Paradox Pattern (NOVEL-01) | NOT DONE | |
| D5 | Dependent claims — Semantic Key (NOVEL-02) | NOT DONE | |
| D6 | Dependent claims — Compile-Gate Error Re-Obfuscation (NOVEL-03) | NOT DONE | |
| D7 | Dependent claims — L2 Egress Filter (NOVEL-04) | NOT DONE | |
| D8 | System claims (method + apparatus + computer-readable medium) | NOT DONE | |
| D9 | Phase 3 claims (Latent RAG, Task-Vector Routing) | NOT DONE | Publish as specification embodiments if not claimed independently |
| D10 | Independent claim — Replay-verification ingestion gate (NOVEL-10) | NOT DONE | Highest-priority Node claim; design-only, but include as written-description spec |
| D11 | Dependent claims — Corpus-release gating by frozen benchmark (NOVEL-11) | NOT DONE | |
| D12 | Dependent claims — Per-submission namespace re-mapping (NOVEL-12) | NOT DONE | |
| D13 | Dependent claims — Symmetric OTA verified_locked gate (NOVEL-13) | NOT DONE | PRIOR mechanism enabled; fleet framing is new |
| D14 | System claim — Combined fleet privacy pipeline (NARROW-04) | NOT DONE | Requires NOVEL-10 + NOVEL-12 as required elements |
| D15 | Dependent/independent claim — Tier-gated corpus promotion (NOVEL-14) | NOT DONE | Needs triage; may be dependent on NOVEL-10/NOVEL-11 family or separate system claim |

### E. Business / Organizational

| # | Item | Status | Notes |
|---|---|---|---|
| E1 | Ryan Gurganious registration | PENDING | "Pending Registration" as of this document |
| E2 | GitHub repository public disclosure date confirmed | **CONFIRMED — PRIVATE** | `DarthCeltic/determinex` verified private as of 2026-06-11 (screenshot). "You don't have any public repositories yet." No grace-period clock is running. PCT is not barred. |
| E3 | Earliest public disclosure date established | **CONFIRMED — NO DISCLOSURE** | Repo is private. No public disclosure of any kind has been made. Filing can occur without grace-period constraint. |
| E4 | PATENT\_FILED status in CLAUDE.md set to `true` | NOT DONE — DO NOT DO UNTIL USPTO NUMBER ASSIGNED | |

---

## Critical Timing Factors

### Competitor Disclosure Dates

| Reference | Date | Implication |
|---|---|---|
| Moschella 2023 | Sep 30, 2022 | Prior art — differentiation required for Rosetta Stone claims |
| IBM US20250086310A1 | Sep 13, 2023 | Prior art — differentiation required for Cloak claims |
| Acronis US12566889 | Apr 2, 2024 | Prior art — differentiation required for Cloak claims |
| CodeCipher arXiv:2410.05797 | Oct 8, 2024 | Prior art — strongest technical overlap with Cloak; compile-validity differentiates |
| LatentMAS arXiv:2511.20639 | Nov 25, 2025 | Prior art — strongest overlap with Rosetta Stone; heterogeneous d\_h differentiates |
| arXiv:2601.06123 (DeepMind) | Jan 4, 2026 | Prior art — overlaps Phase 3 Latent RAG |
| arXiv:2605.22863 (LCF) | May 19, 2026 | May be post-date vs. Determinex white paper — verify git history |

**The LatentMAS reference (Nov 2025) is the most urgent timing pressure.** It is already an ICML 2026 spotlight. The prior art differentiation for Rosetta Stone (heterogeneous d\_h, trained MLP, InfoNCE) must be preserved in all independent claims.

### Grace Period Note (35 USC 102(b))

**CLEARED 2026-06-11**: The GitHub repository (`DarthCeltic/determinex`) is confirmed private. No public disclosure by the inventor has occurred. The 35 USC 102(b)(1)(A) grace period clock has not started. Filing timing is at the inventor's discretion with no urgency from self-disclosure. Non-US filing (PCT/EPO) is not barred by any prior inventor disclosure.

---

## Architecture Status Summary

| Component | Built | Validated | In Flux (see MORPH_REGISTER) |
|---|---|---|---|
| Project Cloak (Python) | YES | YES (warm-up, SWE-bench) | Language extension planned (M-02) |
| Rosetta Stone Layer 1 (DSL) | YES | YES | Stable |
| Rosetta Stone Layer 2 (soft prefix) | YES | YES (rosetta\_v1.pt) | D\_ROSETTA may change (M-03) |
| Rosetta Stone Layer 3 (KV broadcast) | NO — design only | N/A | Not built (M-01) |
| Compiler Oracle | YES | YES | Stable |
| Eval-in-Loop (ProgramBench) | YES | Historical "46 locks" claim invalidated 2026-06-30 (provenance audit found upstream builds, not reimplementations; honest count 0/200) — the Eval-in-Loop mechanism itself is unaffected, only the benchmark evidence figure | Benchmark expansion (M-06); needs a fresh legitimate result before re-citing |
| Latent RAG | NO — design only | N/A | Phase 3 (M-01) |
| Task-Vector Routing | NO — design only | N/A | Phase 3 (M-08) |
| Ethics Oracle | NO — design only | N/A | Not built (M-05) |

---

## Next Steps (in priority order)

1. **Engage a patent attorney** — nothing else on this list matters until this is done
2. **Establish earliest public disclosure date** — run `git log --follow --diff-filter=A docs/papers/WHITE_PAPER.md` to find the first commit, verify if repo was public at that time
3. **Attorney directs full prior art search** — especially for Compiler Oracle claims (CodeRL, AlphaCode space)
4. **Inventor disclosure session** — attorney + Ryan walkthrough of the 7 novel elements
5. **File provisional** — provisional costs $320 (micro entity), gives 12 months before non-provisional is due
6. **Update PATENT\_FILED** in CLAUDE.md after USPTO assigns provisional application number

---

*This document is NOT a legal opinion. It is a staging checklist for attorney/inventor use. DO NOT change PATENT_FILED status until a USPTO application number has been assigned.*
