---
name: vibe-coding
description: |
  Load when user asks about development philosophy, how Determinex generates code, why the
  compiler is used as a judge instead of an LLM, or how the build loop works at a high
  level. Load when user is curious about iterative/exploratory coding methodology.
  Do NOT load for specific compiler errors, debugging sessions, or architecture comparison questions.
depends: [flow-ai]
---

# Vibe Coding and the Compiler Oracle: Why Intuition-First Development Works

*A companion to the Determinex white paper. Ryan Gurganious · Lunarian Data Systems · 2026*

---

## The Premise

"Vibe coding" is the practice of building software by feel — starting with intuition, iterating on running output, letting the compiler catch what you didn't think about. It sounds informal. It is, in practice, one of the most productive development modes available for solo builders and small teams.

Determinex was built this way. Not by accident — by design.

This document is not an argument against rigor. It is an argument that rigor belongs in the right place: at the compiler gate, not at the planning stage.

---

## What the Compiler Gives You

When you build with a compiler as your oracle, you get something that LLM-based evaluation cannot replicate: a deterministic, zero-hallucination ground truth at every step.

The compiler does not have opinions. It does not give partial credit. It does not reward well-formatted wrong answers. It either accepts your code or it tells you, precisely, what is wrong.

This means the "vibe" phase — the intuitive, fast, exploratory generation phase — can be as loose as you want it to be, because the compiler catches everything. The mental cost of precision planning is offloaded to a machine that can run in milliseconds.

Determinex's entire architecture reflects this. The Architect produces a rough DAG. The Builder generates code with deliberate looseness at the first attempt (temperature 0.4–0.7). The Compiler Oracle provides the ground truth. Only failures go back through the loop.

---

## The Problem with LLM Judges

Most AI coding systems use another LLM to evaluate whether code is correct. This is circular: you use an imprecise tool to judge the output of another imprecise tool.

The result is a system that can hallucinate both the solution and the verification of the solution simultaneously. There is no external ground truth. The "reward" is whatever the judge model finds plausible.

Determinex's claim is simple: **the compiler is the only judge that cannot be fooled.**

This is not a limitation of the approach. It is the entire point.

---

## Flow State and the Build Loop

*(See companion document: COMPANION_FLOW_AI.md)*

The Determinex build loop is designed around a specific insight about cognitive flow: the most expensive part of programming is not writing code — it is context switching.

Every time a developer has to stop, read a long error message, trace a call stack, look up a signature — they break flow. The Determinex build loop is designed to minimize that cost.

- Errors are classified and summarized before injection
- Only the relevant context is shown at each step
- The Architect replans only on repeated failure, not on every error

The result is a build loop that feels fast even when it is correcting — because the developer is never shown the full weight of failure at once.

---

## When Vibe Coding Fails (And What Determinex Does About It)

Vibe coding fails in two ways:

1. **Oscillation** — the Builder cycles between two wrong answers indefinitely. The Tunnel Vision detector (AST structural delta analysis) catches this and interrupts.
2. **Drift** — the solution drifts away from the spec without the developer noticing. The Monitor model catches this by independently scoring each step's output against the original spec.

Both failure modes are handled structurally. The developer doesn't need to monitor for them. The system does.

---

## What This Means for Solo Builders

Determinex was designed for one person doing the work of a team. The vibe coding philosophy is what makes that possible:

- Generate fast, with high temperature
- Compile immediately
- Inject the exact error, not a paraphrase
- Retry with targeted correction
- Escalate only on repeated failure

This is not "throwing code at the wall." It is a disciplined loop where the discipline lives in the infrastructure, not the developer's head.

The result is that the developer can think about the problem, not about the syntax. The compiler handles the syntax. The system handles the retries. The developer handles the architecture.

---

## Practical Takeaways

1. **Use the compiler as your first-pass reviewer.** Don't wait for a human review to catch compile errors. The compiler is faster, cheaper, and never wrong.
2. **Generate at higher temperature, compile immediately.** A fast wrong answer that compiles is more useful than a slow careful answer that doesn't.
3. **Inject exact errors, not summaries.** "The error on line 47 is `undefined variable x_4421`" is more useful than "there was a compilation error." Determinex does this automatically. You can do it manually.
4. **Track structural delta, not line count.** Whether you're making progress on a hard problem is visible in the AST, not in the number of lines changed.
5. **Let the system handle oscillation detection.** If you're cycling between two wrong answers, you need external interrupt logic, not more willpower.

---

---

## Gotchas — Known Failure Modes

**Do NOT load this Skill when:** The user is asking about a specific error message, a compilation failure, or a debugging workflow. Those route to the compiler oracle pipeline directly, not to philosophy.

- **High temperature + tight spec mismatch:** Temperature 0.4–0.7 works for exploratory generation but produces unreliable outputs when the spec contains strict interface contracts (exact function signatures, required field names). Lower temperature or DSL-structured steps are required in those cases.
- **Vibe loop without step decomposition:** Running the full build loop against an underspecified spec causes the Architect to generate ambiguous DAG steps, which the Builder interprets inconsistently across retries. The loop oscillates, not converges. The spec must be well-formed before the loop starts.
- **Oscillation misread as progress:** A Builder that cycles between two wrong approaches will show non-zero structural delta each step, fooling a naive observer into thinking progress is happening. The Tunnel Vision detector uses ε-threshold over T steps, not single-step delta. Do not disable the detector in long sessions.
- **Monitor score inflation:** The Monitor can inflate scores on code that compiles but doesn't meet the original spec. The compiler gate is necessary but not sufficient. Monitor must evaluate against the Architect's original intent, not just compilability.

---

*Related documents: COMPANION_CLOAK_SAFETY.md · COMPANION_FLOW_AI.md · COMPANION_MOA_MOE.md · docs/WHITE_PAPER.md*
