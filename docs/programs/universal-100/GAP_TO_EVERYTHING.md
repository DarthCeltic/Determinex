# Determinex — Gap To Everything (what's missing after ProgramBench 200)

> **This is the destination map**, not a support claim. ProgramBench 200/200 proves one
> thing: cleanroom CLI reimplementation, compiler/test-verified, across a handful of
> languages. "Do it all" is much larger. This doc is the single index of **what is still
> missing to do everything, and exactly how we acquire or _mathematically manufacture_ the
> golden standard for each gap.** Membership in a taxonomy here is routing, NOT proof —
> every gap cell defaults to NOT_CLAIMED until a sound oracle + a verified solve exist.
>
> **Gating:** the production line does not execute beyond-PB work until PB is 200/200 clean
> locks (operator rule). This map may grow; closing any cell is gated behind that.

Last updated 2026-06-15. Live PB capability: [`corpus/programbench/CAPABILITY.md`](../../../corpus/programbench/CAPABILITY.md).

---

## 0. The base — ALREADY IN PLACE (you don't build one, you fill its rungs)

Audited 2026-06-15: the substrate to "do the rest" exists. There is no new base to stand up;
the work is wiring the remaining rungs into it and driving them to proof.

| Base component | Where | State |
|---|---|---|
| **Universal task substrate** (`TaskSpec`: workspace, instruction, setup, validate, limits, scoring, Cloak) | `scripts/verified_task/` (+ adapters, runner, corpus writer) + `verified_task_cli.py` | ✅ real, benchmark-neutral |
| **Oracle registry** (never silently passes; `OracleUnavailable` w/ install hint) | `scripts/determinex_oracle.py` | ✅ REAL: python, go, rust, js/ts/node, **C#/.NET** · ⚠ STUB: java, kotlin, swift |
| **Oracle synthesizer** (manufacture sound ground truth) | `determinex_synthesize.py` → `determinex_build_from_idea.py` | ✅ real, proven (`rle`) |
| **Correctness amplifier** (any model → correct vs sound oracle) | `determinex_verified_search.py` | ✅ real, proven 200/200 @p=.20 |
| **Coverage ledger** (the matrix: cells by language/platform/sector/workflow, blocker buckets, next-recommended-rung, signed, claim-bounded) | `assurance/evidence/universal_100_support_depth_ledger/` (+ `scripts/ide/…_ledger_status.py`) | ✅ exists; 26/40 families have evidence; **release_supported = 0** |

**So the "rest" plugs into this base.** The only genuinely missing rungs:
1. **3 oracles to wire:** Java, Kotlin, Swift (stubbed — need their toolchains; everything else is real).
2. **Domain adapters** for the empty sectors (web / mobile / desktop / visual) — the harness accepts
   their `TaskSpec`s, but nothing generates the tasks yet (the empty trace buckets).
3. **Drive the ledger scaffold → proof:** `release_supported = 0` today; the same triage→oracle→
   amplify→register loop the PB campaign uses raises each cell — gated behind PB 200/200.

---

## 1. The destination: what "everything" means

Determinex's north star: **the IDE natively tackles ALL code/systems with any model combo
(tiny-local / cloud / cloaked), and is right — bounded only by oracle soundness.** That
universe has three orthogonal axes. PB exercises a thin slice of each; "everything" is the
full product.

```
  EVERYTHING  =  Languages  ×  Domains/Sectors  ×  Task-types
                 (≥20)         (40, Universal-100)   (≥8)
   ... each cell needs: a SOUND ORACLE (ground truth) + a VERIFIED SOLVE.
```

The bound is not the model. The Correctness Amplifier (`determinex_verified_search.py`) drives
**any** generator `p>0` toward correct against a sound oracle. So "can we do cell X?" reduces
to **"do we have a sound oracle for X?"** — which is the entire subject of §4.

---

## 2. What the 200 PB locks PROVE (the slice we have)

From the live capability map:

- **Languages (6):** rust, go, c/c++, python, haskell, jvm(partial)
- **Domain (1 of 40 sectors):** CLI / terminal tools — reimplementation from behavioral tests
- **Task-type (1 of ≥8):** *reimplement-from-shipped-tests* (the golden standard is given)
- **14 eval/build techniques + 10 behavioral surfaces** (TTY, ANSI, datetime, exit-code,
  output-mode, encoding, …) — transferable skills the corpus has banked.

This is real and rare (frontier models score ~0%). But it is **one column** of the matrix.

---

## 2.5 Audit reconciliation — what we ALREADY have, by evidence level (2026-06-15)

A full corpus/docs audit, so the gap below is honest and not overstated. Three evidence
tiers — only the first is a capability claim:

- **PROVEN (sound oracle + verified solve + proof):**
  - PB CLI reimplementation — 6 languages (the 200, being re-locked).
  - Greenfield-from-idea — `determinex_synthesize.py`→`build_from_idea.py`, proven live (a 1.9 GB
    local model produced a verified `rle` vs a synthesized 5-check oracle).
- **IN FLIGHT — scaffold / corpus / audited-run (intake exists, NOT yet proven, still NOT_CLAIMED):**
  - **Bug-fix task-type:** SWE-bench corpus is real (268 files — per-repo specs, `locked/`,
    instance index across **Python / JS(axios) / Go(multilingual)**) + **audited eval runs**
    (`logs/swebench/…/predictions.jsonl`; results are lower-bound/audited, not clean locks).
    → so bug-fix is *further than "wired"*, but below the proof bar.
  - **40-sector taxonomy:** 26/40 families carry scaffold/smoke/classified evidence
    (universal intake + routing exist) — but **release_supported = 0 cells / 0 families.**
  - **Languages:** validators wired for 12 (Python/Bash/Go/Rust/TS/JS/Java/C/C++/Ruby/PHP/SQL)
    via the language matrix + `determinex_oracle.py` registry.
- **EMPTY — scaffold dir only, no evidence (genuine gap):**
  - `browser_trace`, `mobile_trace`, `desktop_trace`, `terminal_trace`, `visual_repair`,
    `safety_refusal` on `T:/determinex_corpus` are all **0 files**. Web/mobile/desktop/visual are
    not started beyond an empty bucket.

**Net:** the *proven* surface is thin (PB CLI + greenfield-rle) — the doc does NOT overstate
capability. But meaningful **intake/scaffold/audited-run** work already exists for bug-fix
(SWE-bench, multi-language) and 26/40 sectors; the gap is "raise these from scaffold→proof,"
not "build from nothing." Everything below the PROVEN tier stays NOT_CLAIMED until a sound
oracle + verified solve + proof exists.

---

## 3. The GAP (what's missing), by axis

### Axis A — Languages not yet PROVEN
Canonical source: [`docs/architecture/UNIVERSAL_VERIFIED_TASK_LANGUAGE_MATRIX.md`](../../architecture/UNIVERSAL_VERIFIED_TASK_LANGUAGE_MATRIX.md) (validators + benchmark targets per language).

| Status | Languages |
|---|---|
| PROVEN (PB) | rust, go, c, c++, python, haskell* |
| Validator wired, not PB-proven | TypeScript, JavaScript, Java, Ruby, PHP, SQL, Bash |
| Not yet wired | Kotlin, Swift, C#/.NET, Scala, Zig, Lua, Dart, R, Julia, Elixir, OCaml, Clojure |

### Axis B — Domains/sectors (PB covers 1 of 40)
Canonical source: [`DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING.md`](DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING.md) (40 sectors; every sector defaults NOT_CLAIMED). Representative gap sectors beyond CLI:
web-frontend · backend-services/APIs · mobile (iOS/Android/RN) · GUI/desktop · libraries/SDKs ·
databases/queries · data/ML pipelines · embedded/firmware · systems/kernel · infra/IaC ·
games · scientific-computing · security-tooling · …(40 total).

### Axis C — Task-types (PB covers 1 of ≥8)
| Task-type | Have? | Where it comes from |
|---|---|---|
| Reimplement-from-tests | ✅ PB | golden standard shipped |
| Bug-fix on real repo | ▶ wired | SWE-bench / SWE-bench Pro adapter |
| Greenfield from spec/idea | ▶ built | `determinex_synthesize.py` → `determinex_build_from_idea.py` |
| Refactor / optimize / migrate | ✗ | characterization-oracle (synthesize) |
| Security-harden | ✗ | property/contract oracle (synthesize) |
| Test-writing / review / debug | ✗ | contract + differential oracles |

---

## 4. How we get the golden standard for the missing — the two paths

**This is the load-bearing answer to "can it legitimately do everything."** Every missing cell
needs ground truth. There are exactly two ways to get it, and Determinex has both built:

### Path 1 — ACQUIRE (the target ships, or a benchmark provides, tests)
Pull the upstream + its test suite and run the identical closed loop (the PB playbook). The
benchmark targets per language/domain are mapped in the language matrix and the benchmark
strategy. Priority order (memory `project_benchmark_strategy.md`): **SWE-bench Pro → Terminal-Bench
→ LiveCodeBench Pro → BigCodeBench → BIRD (SQL)**. The Universal Oracle registry
(`determinex_oracle.py`) already wires per-language validators (tsc+jest, gradle, .NET, swift, …);
a missing one raises `OracleUnavailable` with an install hint — **an oracle never silently passes.**

### Path 2 — SYNTHESIZE (no tests ship → manufacture a SOUND oracle, mathematically)
For greenfield / unbenchmarked / proprietary targets there is no shipped golden. Determinex
**produces** one:

```
idea/spec ──► determinex_synthesize.py ──►  SOUND ORACLE
                  • exact example-assertions (from given examples)
                  • type-aware property tests (skips what it can't type soundly — no slop)
                  • characterization / golden / contract tests
          ──► determinex_build_from_idea.py:  idea → sound-oracle → amplified-solve → VERIFIED program
```

- **Soundness contract (load-bearing):** a correct output requires a *sound* oracle, so every
  synthesized oracle is paired with the **Test Validator** (`determinex_test_validator.py`) —
  garbage-oracle-in is caught, never claimed solved without a passing OracleResult + proof.
- **Grounded in the locked corpus:** Case Memory (`determinex_case_memory.py`, verified-only) +
  the locked corpus' banked techniques/behaviors give the synthesizer priors for what assertions
  and property classes are correct — this is the "mathematically produce it from our locked
  corpus" path. Proven live: a 1.9 GB local model produced a verified `rle` against a
  synthesized 5-check oracle.
- **Any model, made right:** Correctness Amplifier — `1−(1−p)^K` against a sound oracle drives
  any `p>0` to correct (proven 200/200 at p=0.20, K=15).

**So the rule for "do it all": for every missing cell, either Path 1 finds a golden standard,
or Path 2 manufactures a sound one — and only a passing OracleResult + proof promotes a cell
out of NOT_CLAIMED.**

---

## 5. Canonical sources (where the detail lives)
- **Live PB capability:** [`corpus/programbench/CAPABILITY.md`](../../../corpus/programbench/CAPABILITY.md) + `capability_map.json` + `verified_locks.json`
- **Languages × validators × benchmark targets:** [`docs/architecture/UNIVERSAL_VERIFIED_TASK_LANGUAGE_MATRIX.md`](../../architecture/UNIVERSAL_VERIFIED_TASK_LANGUAGE_MATRIX.md)
- **40-sector taxonomy:** [`DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING.md`](DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING.md)
- **Benchmark priority/targets:** memory `project_benchmark_strategy.md`
- **The math path (components):** `determinex_synthesize.py`, `determinex_build_from_idea.py`, `determinex_oracle.py`, `determinex_verified_search.py`, `determinex_test_validator.py`, `determinex_case_memory.py`
- **Architecture write-ups:** [`docs/architecture/CORRECTNESS_AMPLIFIER.md`](../../architecture/CORRECTNESS_AMPLIFIER.md), [`docs/architecture/IMPOSSIBILITY_ADJUDICATOR.md`](../../architecture/IMPOSSIBILITY_ADJUDICATOR.md)

---

## 6. Status & honesty
- This is a **map + method**, gated behind PB 200/200. Nothing here is claimed-supported by
  appearing in a table. A cell becomes real only with a sound oracle + a verified solve +
  proof — same discipline as the verified-lock registry.
- The next concrete action **after** the line clears 200 PB locks: instantiate this map as a
  coverage ledger (one row per Language×Sector×Task-type cell, default NOT_CLAIMED) and drive
  it with the same triage→oracle→amplify→register loop the PB campaign uses.
