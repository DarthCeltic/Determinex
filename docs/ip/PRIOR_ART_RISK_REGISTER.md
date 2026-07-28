# Prior Art Risk Register

**Status:** draft risk register for attorney review
**Prepared UTC:** `2026-06-02T22:31:15Z`

| Area | Risk | Notes For Counsel |
|---|---|---|
| Agentic coding loops | High | Compare against SWE-agent, Devin-like systems, AutoGPT-style agents, CI repair loops. |
| Compiler/test feedback | High | Many systems use tests as rewards; focus may need to be on exact pipeline composition and proof/WAL/training gates. |
| Privacy-preserving code obfuscation | Medium | Compare against code anonymization, format-preserving tokenization, and secure code review systems. |
| Error re-obfuscation for retry prompts | Medium | Potential differentiator if exact compiler feedback remains useful without revealing identifiers. |
| Multi-agent orchestration | High | Common in agent literature; narrow to compiler-oracle proof and training-pair lifecycle. |
| Latent-space bridging | Medium | Compare against model routing, adapters, representation alignment, and shared embedding spaces. |
| Proof-gated release claims | Medium | Similar to compliance/evidence ledgers; narrow to software support-cell promotion with explicit non-claims. |
| Terminal anti-god guard policy | Low/Medium | Likely process/policy support, not standalone invention. |

## Required Search Targets

- Academic papers on compiler-guided program synthesis and repair.
- CI-based automated repair systems.
- Code obfuscation/anonymization for LLM use.
- Multi-agent software engineering systems.
- Representation alignment / latent bridge papers.
- Compliance evidence ledgers and release-readiness gates.

## Boundary

This register is a risk organizer, not a patentability search or legal conclusion.
