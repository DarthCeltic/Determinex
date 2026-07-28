---
name: flow-ai
description: |
  Load when user asks about developer experience, cognitive load, why the IDE is designed
  the way it is, feedback loop latency, context switching, burnout detection, or the
  UX rationale behind specific Determinex design decisions. Load when user is frustrated by
  wait times or unclear outputs and wants to understand the design intent.
  Do NOT load for architecture comparison questions (MoA vs MoE) or privacy/cloak topics.
depends: []
---

# Flow AI: Designing Systems That Preserve Developer Cognitive State

*A companion to the Determinex white paper. Ryan Gurganious · Lunarian Data Systems · 2026*

---

## The Central Claim

The bottleneck in AI-assisted software development is not model quality. It is cognitive interruption.

A developer in flow state — fully engaged, context loaded, all relevant state in working memory — produces more in one uninterrupted hour than in four fragmented hours. AI coding tools that interrupt flow (with long waits, confusing outputs, or decisions that force context switching) destroy the advantage they are trying to provide.

Determinex is designed around this constraint. Every architectural decision in the build loop has a corresponding flow-preservation rationale.

---

## What Flow State Requires

Flow state in programming requires:

1. **Tight feedback loops.** Errors appear immediately after the action that caused them. Long waits between action and feedback break the causal chain in working memory.
2. **Predictable system behavior.** Surprises are cognitively expensive. A system that behaves consistently allows the developer to build a mental model and stay inside it.
3. **Appropriate challenge level.** Tasks that are too easy produce boredom. Tasks that are too hard produce anxiety. Flow lives in the corridor between.
4. **Minimal context switching.** Every time attention shifts — to a new file, a new error format, a new tool — working memory partially flushes. The cost is higher than it appears.

---

## How Determinex Addresses Each Property

### Tight feedback loops

The Compiler Oracle provides sub-second feedback on every step. Errors are not buffered or batched — they are injected immediately into the next attempt. The build loop runs at machine speed, not human speed.

The developer's feedback loop is: write spec → see DAG → watch steps execute → see compile results. The loop is tight because the compiler is fast.

### Predictable system behavior

The Determinex DSL (Semantic DSL) is the key mechanism here. Instead of prose instructions between models (which produce variable outputs), the Architect emits structured DAG steps in a defined format. The Builder always receives the same input format. The Monitor always scores the same output format.

This predictability propagates upward: because the build loop behaves consistently, the developer can predict what will happen when they run a session. Surprises are rare. When they occur (escalation, oscillation), they are surfaced explicitly rather than silently swallowed.

### Appropriate challenge level

The Determinex task structure (Spec → DAG → steps) decomposes complex problems into sub-tasks with defined scope. Each step has a single objective. The Builder is not asked to solve the whole problem at once.

This decomposition serves flow: the developer defines the challenge level in the spec, and the Architect maps it to appropriately-sized steps. Steps that are too large (by line count or complexity) trigger an automatic subdivision.

### Minimal context switching

The build loop is designed to minimize the number of times the developer needs to look at different things simultaneously.

- Error messages are classified and summarized before display, not shown raw
- The workspace file viewer shows only files relevant to the current step
- The Monitor verdict is a single score + brief rationale, not a long critique
- Escalations surface to the developer as a single decision point, not a stream of failures

The developer's attention is managed, not just provided with information.

---

## The Tunnel Vision Problem

When a developer (or an AI model) gets stuck on a wrong approach, they often cannot see the error clearly enough to escape it. They make small variations on the same wrong solution. This is Tunnel Vision.

Determinex detects Tunnel Vision via AST structural delta analysis:

1. After each attempt, the AST of the current output is hashed
2. The structural delta between successive attempts is computed
3. If delta falls below threshold ε for T successive steps, the system interrupts

The interrupt is not an error message. It is a re-planning event: the Architect receives the full failure context and produces a different approach. The Builder is not told to "try again differently" — it receives a new DAG node with different structure.

This is the AI equivalent of a rubber duck conversation: the external interrupt forces the problem to be restated from scratch.

---

## What "Flow AI" Means as a Design Principle

Flow AI is not a product category. It is a design constraint:

*Any AI tool that reduces developer cognitive load at the cost of increasing attention management load is a net negative.*

Concretely:
- A tool that requires the developer to monitor its output for hallucinations is not a flow tool
- A tool that produces long, uncertain outputs that require developer judgment to use is not a flow tool
- A tool that interrupts to ask for clarification at unpredictable intervals is not a flow tool
- A tool that behaves differently each run (due to non-determinism at critical decision points) is not a flow tool

By this standard, most current AI coding assistants are not flow tools. They are interrupt generators that happen to produce useful code sometimes.

Determinex's design commitment: the developer should be able to look away while the build loop runs and return to a clear, actionable status report. The loop should not require monitoring.

---

## The Burnout Prevention Architecture

*(From docs/ARCHITECTURE.md Section 3.9 — Burnout Events)*

Determinex tracks developer engagement state across sessions. The Burnout Event detection system monitors for:

- Session length exceeding threshold (time at keyboard without break)
- Error rate spike without corresponding progress
- Oscillation pattern detected at the session level (developer cycling between approaches)

When a Burnout Event fires, the system does not continue. It surfaces a session summary, stores the current state to WAL, and suggests a break.

This is not a wellness feature. It is an architectural decision: a developer in burnout produces lower-quality specs, lower-quality decisions, and lower-quality training data. Protecting developer cognitive state protects the quality of the training corpus.

---

## Open Questions

- What is the optimal AST delta threshold ε for Tunnel Vision detection? The current value (1.5× structural delta) was arrived at empirically. Is there a principled derivation?
- Does the Architect's temperature during re-planning need to be higher than during initial planning, to escape local attractors?
- Can the Burnout Event detector be trained on session-level metrics to personalize thresholds per developer?
- What does it mean for a multi-agent AI system to be "in flow"? Is there an analog to developer flow at the system level?

---

---

## Gotchas — Known Failure Modes

**Do NOT load this Skill when:** The user is asking about model architecture internals (MoE routing, Rosetta Stone, DSL token structure). Those route to COMPANION_MOA_MOE or the white paper directly.

- **Burnout detector firing on legitimate long sessions:** The burnout threshold is set empirically. A developer running a deliberate all-night SWE-bench evaluation will trigger burnout events that interrupt the session. The detector should check for *error rate spikes*, not just session length, before interrupting a productive flow.
- **Tunnel Vision threshold too tight (ε too small):** A low epsilon means any small structural change resets the oscillation counter, hiding a genuine loop. The current value (1.5× structural delta) was tuned for the existing test suite. Verify against new language targets if the system is extended to new languages.
- **Monitor verdict latency breaking flow:** If the Monitor model takes >3s to produce a verdict, it becomes the bottleneck in the tight feedback loop Determinex promises. On Tier 0 hardware, Monitor is swapped out of VRAM between invocations. The VRAM tollbooth is the primary flow-breaker on constrained hardware — not the model quality.
- **Error summary over-compression:** Summarizing compiler errors before display (to reduce cognitive load) can hide the precise error line. The policy is to inject the exact error for compile failures and only summarize for multi-error cascades. Don't over-compress.

---

*Related documents: COMPANION_VIBE_CODING.md · COMPANION_MOA_MOE.md · docs/WHITE_PAPER.md Section 3*
