# ProgramBench — Audit + Roadmap to "All Winnable"

> Written 2026-06-29 after a hard soundness audit. Goal (operator's words): **every PB tool winnable,
> driven to a lock, zero gaming.** This document is the honest path from where we are to there. It
> states the one hard truth up front so nothing here gets walked back later.

## 0. The hard truth this roadmap is built on

Some failing tests are **provably slop**: a *correct* build of the tool fails them too. Proven example:
lua's `test_empty_stdin_interactive` asserts the interactive banner appears for **pipe** stdin, but no
correct lua prints a banner for non-tty input (the eval's own `CompletedProcess(args=['./executable'],
stdout=b'')` proves it used a subprocess pipe, not a PTY). The official PB metric counts that failure
against the tool. We **cannot** edit frozen fixtures and we **will not** game.

So literal "all officially-locked" is blocked by tests that are themselves wrong. The honest, reachable
version of the goal:

> **Every tool is ACCOUNTED — either LOCKED, or a PROVEN CEILING with a built-binary proof that a
> correct implementation fails the remaining tests. 100% accounted, zero unknowns, zero gaming.**

That is the strongest claim a sound system can make, and it is far beyond any public result (all public
frontier models: 0–0.5% fully resolved). The locked count is the real score; the ceiling count is
*proven*, not excused.

## 1. Where we are (verified this session, not claimed)

| Bucket | Count | Status |
|---|---|---|
| **Strict locks** | **67** | guard-verified, build-from-source, no gaming |
| Proven/certified ceilings | ~34 | structural blockers, proof on file |
| Perfect-but-unpromoted | ~17 | provenance-gated (`tier_1_perfect`) |
| **"Open" (unaccounted)** | **~119** | winnable + reject + stale-cache — the work |

**Capabilities built:** hardened **no-gaming** engine (de-gamed adjudicator + remediation + integrity);
the **automated slop detector** (`determinex_test_validator.auto_reference_check` — build a clean
reference, run the real invocation, SLOP **only** when a correct binary fails too; two soundness guards
added *because* testing caught false positives — the nnn helper, masscan's dead temp-files); grounded
autodrive; the knowledge flywheel + code-RAG.

## 2. The rigorous framework — every failing test is exactly one of four

1. **SLOP / CEILING** — a clean reference fails it too → the test is wrong / env-baked. *Not winnable
   by code; provable by the slop detector.*
2. **BUILD-DEFICIENT** — a clean reference **passes**, our submission **fails** → our `compile.sh`
   builds the wrong/incomplete binary. **Winnable: fix the build.**
3. **BEHAVIORAL** — reference and ours both fail, but the test is correct → genuine per-tool work.
   **Winnable: the MATCH grind.**
4. **DEFER** — can't build/run a clean reference yet → **no claim** (sound by construction).

This framework is the audit. Every "open" tool's failures resolve into these four — and three of the
four are winnable.

## 3. The roadmap — each phase produces a hard number, not a vibe

- **Phase 0 — Reconcile (one pass).** `pb_tier_classify --guard` → confirm the 67 locks, the ceilings,
  the open set. Truth before work.
- **Phase 1 — Build-correctness audit (the winnable-finder, the thing being asked for).** For each open
  tool: build a clean reference + check whether our `compile.sh` produces an equivalent binary, and run
  the slop detector. Output: every open tool labelled **build-deficient / behavioral / slop / defer**.
  *This converts "119 open" into named, actionable buckets — it is the audit that tells us the real
  ceiling.*
- **Phase 2 — Convert build-deficient → locks.** Fix the builds (highest ROI, knowledge-grounded).
  Each is a real, from-source lock. (masscan-class "not_run/fail" lives here, if the build is the cause.)
- **Phase 3 — Classify + document ceilings.** Slop detector across the tail → every proven slop becomes
  a documented true-ceiling **with a binary proof**. Tools move from "unknown" to "accounted."
- **Phase 4 — Behavioral grind.** Per-tool MATCH on the genuine tail (autodrive + Claude-in-the-loop +
  the flywheel/code-RAG). Slow, real, one tool at a time. No gaming.
- **Phase 5 — Reach-widening.** Better per-language reference recipes + **eval-as-replay** (the eval
  already runs the real tests against our binary) → fewer defers, more proofs.

## 4. The honest blockers (named, so they don't ambush us)

- **The official metric counts slop against you.** Resolution: the accounted-100% framing (locked +
  proven-ceiling). If PB ever accepts proven-broken-fixture exclusions, ceilings convert to locks.
- **Reach.** The slop detector reliably reaches ~10/190 today (a *correct* reference build is hard per
  tool). Phase 5 widens it; until then, DEFER is honest, not failure.
- **Build correctness is currently unmeasured.** We do **not** yet know how many "open" tools are
  build-deficient (winnable now) vs behavioral vs slop. **Phase 1 produces that number** — and that
  number is the real answer to "how close to all-winnable are we."

## 5. End state

Every one of the ~200 tools is **LOCKED** or a **PROVEN CEILING (built-binary proof)**. 100% accounted,
zero gaming. Reachable because every bucket above has a concrete, non-gaming path — and the one bucket
that isn't code-winnable (slop) is *proven*, not hand-waved.

**Next concrete step: Phase 1 — the build-correctness audit.** It is the single action that turns "119
open / unknown" into "N winnable now (build), M behavioral, K proven-ceiling, J defer" — the map from
here to the goal.
