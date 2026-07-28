# Determinex Patent Disclosure Draft

**Status:** draft for attorney review
**Prepared UTC:** `2026-06-02T22:31:15Z`

This document is not legal advice and does not claim legal sufficiency. Do not publish or rely on this as a filed patent application.

## Working Title

Local-first compiler-oracle agent system with privacy-preserving cloud assist, proof-gated release claims, and compiler-verified closed-loop training data generation.

## Inventive Concepts To Review

1. Compiler-oracle feedback loop
   - A coding agent pipeline routes generated patches through isolated worktrees and deterministic compiler/test oracles.
   - Failed attempts produce labeled error-to-fix training pairs.
   - Successful attempts are locked as proof artifacts.

2. Cloak-safe error feedback
   - Repository identifiers are obfuscated before cloud model exposure.
   - Compiler/test failures from real code are re-obfuscated before retry prompts.
   - The cloud model receives exact failure structure without proprietary identifier disclosure.

3. Multi-agent DAG execution with evidence WAL
   - Architect, builder, monitor, and compiler oracle roles produce ordered build steps.
   - Each attempt records patch, errors, tests, prompts, and outcomes.
   - WAL records are atomic and become training candidates only after proof gates.

4. Latent bridge / Rosetta communication
   - Model-specific embedding spaces are projected into a shared semantic space.
   - Structured inter-model messages can be routed without ordinary prose as the only transport.

5. Release-cell proof registry with non-claim guardrails
   - Exact release-supported cells are promoted only through source artifacts and signoff gates.
   - Family support, clean-host proof, signed/trusted installer proof, and public readiness remain separate gates.
   - Historical evidence and current registry truth are tracked separately.

6. Terminal guard policy for proof-heavy suites
   - Expensive anti-god/status guard checks are run terminally and reported separately.
   - Segmented proof runs cannot be represented as full-suite passes.

## Current Evidence Anchors

- `scripts/determinex_hive.py`
- `scripts/determinex_swebench_agent.py`
- `scripts/determinex_cloak/`
- `scripts/verify_cloak.py`
- `scripts/cloak_audit.py`
- `scripts/proof/release_cell_registry.py`
- `scripts/status/anti_god_script_rule_check.py`
- `docs/handoffs/DETERMINEX_100_PERCENT_COMPLETION_RELEASE_AND_PUBLIC_LAUNCH_PREP_WAVE_001_DIRTY_STATE_TRIAGE.md`
- `docs/handoffs/DETERMINEX_RELEASE_REGISTRY_MUTATION_SIGNOFF_LOCK_001_REPORT.md`
- `docs/handoffs/DETERMINEX_STATUS_SUITE_TERMINAL_GUARD_POLICY_001.md`

## Non-Claims

- No patentability opinion is made here.
- No freedom-to-operate opinion is made here.
- No filing date is claimed here.
- No public disclosure is authorized by this draft.
