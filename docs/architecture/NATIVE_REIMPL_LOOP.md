# The Native Reimplementation Loop — Determinex's ProgramBench Engine

> Canonical record, 2026-06-25. The autonomous, native-language, compiler-verified loop that
> lets ANY model (down to a cheap/local one) reverse-engineer a CLI tool from its binary and
> rebuild it correctly. This is the engine behind the march to ProgramBench 200/200.

## The problem (and why everyone is at 0%)

ProgramBench (facebookresearch/programbench): given **only a compiled binary + docs** (source
removed from the image), rebuild a codebase that reproduces the program's behavior. Scored on
held-out, LM-fuzzed behavioral tests; ignored tests (`gold_fail`/`gold_flaky`/`dummy_pass`/…)
dropped from both numerator and denominator; **solved iff `n_resolved == len` exactly.**

**Every public model scores 0% fully-resolved** (Opus 4.7 leads "almost-resolved ≥95%" at 3.0%;
best single-task by anyone = 98.2%). They plateau 2–10% short on even the easiest tools because
they **generate-and-pray**: no oracle, no completeness loop, and a training-induced
*Python-bandaid reflex* (make it work, not right).

## The thesis

**The system — not the model — is the unit of correctness.** Correctness is bounded by an
oracle's soundness and completeness, both of which Determinex controls. A weak model sampled K
times against a sound oracle is driven toward correct (`1−(1−p)^K`). So the levers are:

```
score  =  oracle-completeness  ×  technique-coverage  ×  search-budget(+escalation)
```

All three are system-controlled. The model is swappable.

## The two laws

1. **Native-only (Determinex rule, stricter than PB which is language-agnostic).** Submissions are
   rebuilt in the tool's REAL language (Go/Rust/C/C++/Haskell), **compiled and verified by the
   compiler oracle** — never a Python lookalike. This is the truest rebuild, the only path to
   the C/C++/Haskell bottom tier, and the thing that engages Determinex's actual moat.
2. **Legitimacy.** PB's three hard rules: black-box only, **no internet at inference**,
   submission is a genuine codebase. Determinex honors all three; the offline-inference rule means
   the release endpoint is a **local** model. NOT cheating: a knowledgeable workshop, heavy
   coaching, and retraining are all allowed — only shipped source / binary wrappers / embedded
   held-out goldens are forbidden (caught by the provenance/integrity scanners).

## The loop (components, all composed — never duplicated)

```
            binary + docs (black box)
                    │
   determinex_observe  ▼  probe battery (stdin/file/flags) + PROVISIONED environments
   ─ build_probes ─ ─ URL: loopback http.server under --network none (serve probes)
                   ─ (roadmap) PTY (determinex_pb_pty), env, multi-file, archive fixtures
                   ─ edge/malformed battery (exit-code & error-path coverage)
                   ─ nondeterminism guard (run-twice, drop volatile)
                    │
                    ▼  observe_in_image → Observations (exact stdout/stderr/rc)
                    │
   make_verify(runner) ── SOUND oracle: candidate must reproduce every probe
   make_native_runner(lang) ── COMPILER ORACLE: compile once (cached) → run the real binary;
                               compile-failure = reject with the compiler error fed back
   discrimination_estimate ── faithfulness number (trivial mutants must all be rejected)
                    │
   GENERATE (any model via determinex_providers; router escalates cheap→strong on a miss;
             contract-guarded so malformed candidates never waste an oracle slot;
             corpus coach injects cross-tool pitfalls + TECHNIQUE RECIPES + case memory)
                    │
   ┌─ monolithic: VerifiedSearch best-of-K + feedback rounds + closeness gradient
   └─ decompose:  assembly-line — add ONE behavior/station, each compiled+verified, no regress,
                  router escalates the station the cheap model can't clear
                    │
                    ▼  candidate (native source)
   determinex_pb_official_eval ── native compile.sh → ./executable → official metric
                    │
   corpus.record_run + case_memory.add (verified only) ── LEARN; lock a verified skill
```

### Autonomous self-improvement — `determinex_reimpl_drive`

Removes the human from the inner loop:

```
repeat:
  1. workshop run → candidate (native, compiler-verified)
  2. fuzz_diagnose → random BLACK-BOX inputs on reference vs candidate; every divergence is an
                     oracle blind spot (the same method PB uses to make tests; no held-out access)
  3. corpus.add_probes → persist divergences into the corpus-OWNED oracle (<tool>_probes.json);
                         next run loads them → the search is forced to fix them; the oracle compounds
  4. saturation → fuzzing finds no new divergence → black-box-complete → official eval
```

The operator just watches the per-iteration report and tweaks knobs (budget, escalation tier).

## Verifier Skills

Each fully-resolved tool *is* a compiler-verified, evidence-backed capability — the loop already
emits the raw materials: native code + the oracle (`<tool>_probes.json`) + verified case memory
+ compile evidence + failure corpus. Packaging them per solve turns "200 benchmark locks" into
"200 deterministic, reusable skills" (`Skill → Planner → Compiler Oracle → Verifier → Evidence
→ Skill improves`). An added layer; no existing architecture changes.

## Continuous analysis & design invariants

`determinex_reimpl_analyze` self-reports every run: did the model APPLY the injected recipes, is the
oracle sound (discrimination = 1.0), is verified capability accumulating? It caught the cycle-4
regression (enriching edges without pinning the bare-stdin core let verified search trade the
core away) and localized it to a single missing probe — proof the loop self-diagnoses.

## The roadmap (waves)

- **Wave 1 — first full-resolves in the world.** ~23 tools where the frontier plateaus at 90–98%
  (gron, csview, jq, hck, loop, htmlq, sd, brotli, elfcat, nnn, BLAKE3, cmatrix, pingu). Determinex's
  fuzz-grow oracle closes the last 2% nobody closes → 100%. Many have corpus groundwork already.
- **Wave 2 — the middle (~100 tools, 50–90%).** Provisioning breadth (PTY/env/binary/archive
  class-unlockers) + domain fuzzers + escalation.
- **Wave 3 — the hard tail (~55 tools <50%, incl. ffmpeg/php/sqlite/quickjs).** Native (the moat),
  decompose depth, escalation, retrain. The genuine research frontier; even partials are world-first.

## Status (2026-06-25)

- Engine complete & regression-green (`tests/test_autofix_pipeline.py`: 47 passed, 1 env-skip).
- Toolchains: go, rustc, gcc/g++ present; GHC installing to `T:\ghcup` (Haskell/pandoc).
- gron: 96/224 (43%) Python (prior); native-Go drive in flight (compiler oracle holding).
- Frontier reference: 0 tools fully resolved by any public model.

## Key modules

| Module | Role |
|---|---|
| `scripts/determinex_observe.py` | probes, provisioning (URL server), sound oracle, **native runner (compiler oracle)**, discrimination, **fuzz_diagnose** |
| `scripts/determinex_pb_reimpl.py` | the workshop: observe → coach → router+contract+case → verified search / decompose → record; `--lang` native |
| `scripts/determinex_reimpl_drive.py` | the autonomous loop (workshop→fuzz→self-feed→official) |
| `scripts/determinex_reimpl_corpus.py` | coach (pitfalls + technique recipes) + learner + **corpus-owned oracle** (probe persistence) |
| `scripts/determinex_reimpl_analyze.py` | continuous corpus↔LLM design-invariant analyzer |
| `scripts/determinex_pb_official_eval.py` | native packaging + official metric |
| `determinex_providers` / `determinex_router` / `determinex_contract` / `determinex_case_memory` | any-model registry, escalation ladder, well-formed floor, verified transfer |
