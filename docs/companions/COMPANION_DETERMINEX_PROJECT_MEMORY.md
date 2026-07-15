---
name: determinex-project-memory
description: |
  Load when the user asks about Determinex project memory, agent instruction files,
  IDE companion memory, cross-agent handoffs, project-specific operating rules,
  proof boundaries, or how Claude, Codex, Gemini, and the IDE should share context
  without overwriting each other. Load before broad Determinex planning or restart
  reconciliation. Do NOT load as proof that a companion answer is correct.
depends: [cloak-safety, vibe-coding]
---

# Determinex Project Memory Companion

This companion gives the IDE a stable memory spine for Determinex itself. It is not
a campaign status board. It is a routing and context document that helps any
agent find the correct proof-bearing source before acting.

## Layered Instruction Model

Determinex uses layered markdown instead of one giant mutable prompt.

Shared truth lives in `PROJECT.md`. Tool-specific behavior lives in `AGENTS.md`,
`CLAUDE.md`, and `GEMINI.md`. Campaign state lives in the active campaign docs
and machine ledgers. The IDE companion memory reads `docs/companions/COMPANION_*.md`.

When layers conflict, the current user request and live tool file win for the
task, but the conflict should be preserved in handoff evidence instead of hidden.

## Tool Overlays

Codex uses `AGENTS.md` for execution discipline, workspace safety, and local test
behavior. Claude uses `CLAUDE.md` for driver, reviewer, and broad project context.
Gemini uses `GEMINI.md` for wide-context review and synthesis until it has a
stronger execution record.

Tool-specific files should stay thin. Durable project rules belong in
`PROJECT.md` or in a companion document that the IDE can retrieve.

## Current Truth Surfaces

Use proof-bearing sources for factual claims.

ProgramBench truth comes from `corpus/programbench/eval_index.json`, verified
lock archives, and active protocol docs. Product readiness comes from
`locks/sentinel/`, `docs/proof/`, and `assurance/evidence/`. Safety boundaries
come from `docs/policy/`, `docs/SAFETY.md`, and claim scanners.

Do not rely on old handoff prose when a ledger or verifier exists.

## Companion RAG Boundary

Companion RAG provides local context and citation material. It does not prove answer correctness.
It also does not prove product readiness, release support, or training eligibility.

If a response uses companion memory, it still needs evidence from the appropriate
source file, verifier, lock, or command output before making a claim.

## Cross-Agent Coordination

Shared coordination docs are append-only unless the active handoff explicitly
authorizes rewriting. Preserve reviewer history, lane ownership, and raw evidence.

When one agent learns a durable root cause, record it in the corpus, companion
memory, or active handoff surface. The project improves only when the finding is
made retrievable for the next agent.

## ProgramBench Boundary

ProgramBench work is role- and protocol-bound. Executors work only claimed tools
and hand raw evidence to the driver. Drivers certify locks from raw reports and
guard checks. A stated score is never enough.

Under the reimplementation mandate, upstream-source builds are not solves.
Consult the corpus, extract behavior, write native reimpl code, run the local
oracle, then run official eval.

## IDE Memory Shape

Good IDE memory chunks are short, specific, and independently useful after
splitting by `##` headers. Put routing terms in the frontmatter description.
Avoid burying commands or rules inside long narrative sections.

If a concept should be retrieved during work, give it its own `##` section.

## Safety And Claim Discipline

Do not blur detector, verifier, admitted, supported, and release-ready. Do not
turn benchmark evidence into product support unless the support proof exists.
Do not treat refusal gates as fairness metrics.

Generated or untrusted code must run through hardened runners, bounded sandboxes,
or explicit containers. Never print secrets or copy `.env` content into prompts.

## Restart And Handoff Recovery

After a restart, read the live directive stack and active handoff before acting.
Earlier work-in-progress may be stale. Reconcile current files, current git state,
and current machine-readable ledgers before continuing.

If the task is ambiguous and could mutate shared truth, ask the smallest useful
clarifying question first.

## Maintenance Rule

When a tool-specific file accumulates general Determinex rules, move the durable
rule into `PROJECT.md` or this companion. Leave the tool file as an overlay for
that runner's behavior.
