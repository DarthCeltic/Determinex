# Determinex Project Contract

> The rename is COMPLETE as of 2026-07-26: `determinex_*` / `DETERMINEX_*` script, env-var
> and model-tag names are the final identifiers, not a temporary state.
>
> This paragraph previously declared those identifiers temporary "until the coordinated
> internal rename", and a mechanical rename pass had rewritten both halves of the sentence
> so that it claimed the project was formerly itself and that its own final identifiers
> were pending a rename to themselves. That mattered beyond tidiness:
> `_internal_rename_gate` in `scripts/release/determinex_release_gates.py` keys on that
> exact sentence, so the `internal_rename` release gate sat permanently `deferred` over a
> self-contradictory statement and could never pass, whatever the code did.

> Shared project context for every agent and the IDE companion memory system.
> Tool-specific files add behavior for each runner; they do not replace this file.

---

## Purpose

Determinex is a local-first, compiler-verified, multi-agent coding system. Its core
loop is: user spec, architect plan, builder patch, deterministic verifier, retry
with exact failure evidence, and durable learning from verified outcomes.

This file is intentionally stable. It explains what must stay true regardless of
which LLM or IDE surface is driving the work. Put volatile campaign status,
current queue ownership, and live benchmark counts in the campaign docs and
machine-readable ledgers, not here.

## Layer Order

Layer order is the durable read contract for Determinex agents and IDE memory.

Read and apply project instructions in this order:

1. User request for the current task.
2. Live local tool file: `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`.
3. This shared `PROJECT.md` contract.
4. Active campaign or handoff docs explicitly named by the task.
5. Domain docs under `docs/`, `assurance/`, `locks/`, and `corpus/`.

If two files conflict, prefer the more specific live instruction. Preserve the
conflict in a handoff note instead of silently rewriting broad project truth.

## Tool Overlays

Tool overlays are runner-specific. They should stay thin enough that one tool can
change behavior without overwriting the main project memory.

Each agent gets its own overlay:

- `AGENTS.md`: Codex execution rules, workspace safety, tests, and commit style.
- `CLAUDE.md`: Claude driver/reviewer rules and broad project orientation.
- `GEMINI.md`: Gemini adapter rules for read-heavy review, synthesis, and future execution.

Tool overlays may say how a tool should act. They must not duplicate volatile
project status or overwrite shared truth. When a tool learns a durable project
rule, add the rule here or to an IDE companion doc, then leave the tool file as a
thin pointer.

## Current Truth Surfaces

Use machine-readable or proof-bearing sources for claims:

- ProgramBench: `corpus/programbench/eval_index.json`, verified lock archives,
  and the active campaign protocol.
- Product and release readiness: `locks/sentinel/`, `docs/proof/`, and
  `assurance/evidence/`.
- IDE companion memory: `docs/companions/COMPANION_*.md`, seeded into
  `knowledge_companion` and `vss_companion`.
- Safety and claim boundaries: `docs/policy/`, `docs/SAFETY.md`, claim scanners,
  and proof gates.

Do not copy volatile campaign counts into this file. Cite the source file and
command output when a count matters.

## Execution Rules

- Prefer deterministic verifiers over model judgment.
- Run generated or untrusted code only through hardened runners, bounded
  sandboxes, or explicit eval containers.
- Treat shared status and handoff docs as append-only unless the active handoff
  explicitly says otherwise.
- Do not edit canonical boards, ledgers, or count files unless the live role
  contract grants that authority.
- Keep proof boundaries exact: detector, verifier, admitted, supported, and
  release-ready are different states.
- If a workflow produces a new durable root cause, feed it back into the relevant
  corpus or companion memory. Otherwise the system does not learn.

## IDE Memory Contract

The IDE reads companion markdown from `docs/companions/COMPANION_*.md`. A good
companion file has YAML frontmatter, a routing `description`, and short `##`
sections that stand alone after chunking.

Companion RAG provides local context and citations. It does not prove answer
correctness, product readiness, or training eligibility by itself.

The native companion seeder records typed provenance in `memory_sources` and
`memory_chunks`. source hash changes must invalidate and reseed the companion
collection; a row-count-only "already seeded" check is not acceptable for
project memory.

Run `scripts/memory_scorecard.py` after changing project memory, companion docs,
or tool overlays. Use `scripts/memory_learning_inbox.py` for raw lessons that
need promotion; inbox entries stay `training_eligible: false` until a verifier
promotes them into a proof-bearing corpus or companion surface.

## Update Discipline

Update this file only for durable project rules. For tool-specific preferences,
edit the relevant tool overlay. For current campaign state, edit the active
campaign-owned surface. For large product narratives, edit the appropriate docs
under `docs/`.
