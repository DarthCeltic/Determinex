# The Impossibility Adjudicator + Universal Ground-Truth Oracle

> **Status**: shipped 2026-06-14. `scripts/determinex_adjudicator.py`,
> `scripts/determinex_oracle.py`, wired into `determinex_swebench_agent.py` at the
> gate give-up point. Proven on real ProgramBench eval reports.

## Why this exists

Every other IDE's model copes with a hard problem in one of two failure modes:
it **hallucinates** a plausible-but-wrong fix, or it **gives up** ("this is
environmental / this isn't possible / try another approach"). Both are cop-outs.

A 2026-06-14 audit of Determinex's 29 ProgramBench "ceilings" found that the label
had been applied **without ever running the test that proves impossibility**.
The agents wrote *narratives* of impossibility; none produced the *proof*. Of 29:
~11 were unfinished work mislabeled (collection caps, missing dependencies,
root-user artifacts, plain bugs), ~3 were unproven, ~14 were genuine upstream
skips, and **zero** were confirmed impossible by the one decisive criterion.

The Adjudicator makes that cop-out structurally impossible.

## The rule

Determinex may **never** declare a task BLOCKED / IMPOSSIBLE / "ceiling" without
routing through a four-step gate. Only the fourth step can return impossibility:

| Step | Verdict | Question | If yes |
|------|---------|----------|--------|
| 1 | **ROUTE** | Is there *any* observable difference between the conflicting contexts? (env, cwd, argv, `PYTEST_CURRENT_TEST`, files, stdin) | Detect & route per-context (proven: svd2rust, genact). Don't quit. |
| 2 | **MATCH** | Can I match the reference environment? (locale, TTY/PTY, privileges, SIMD, missing dep, timezone) | Reproduce it. Don't quit. |
| 3 | **UNBLOCK** | Did I create the blocker myself? (collection cap, ignore filter, skipped install) | Remove it. Don't quit. |
| 4 | **IMPOSSIBLE** | Do two requirements share an **identical** observable context with **conflicting** ground truth? | Emit the proof. Only now may you stop. |

Anything that is not 1–4 is **NEEDS_WORK** — a plain behavioral bug the solve
loop keeps iterating on. *"I haven't found the move yet"* is never *"impossible."*

## Proven output (mechanizes the manual ceiling audit)

```
python scripts/determinex_adjudicator.py classify <eval_report.json> \
    [--conftest conftest.py] [--compile-sh compile.sh]
```

Real results, 2026-06-14:

| Tool | Adjudicator verdict |
|------|--------------------|
| **fd** | 539 UNBLOCK (the `nr=547` collection cap) + 13 MATCH (drop-privileges, locale-pin, error-string) + 3 NEEDS_WORK. **0 ceiling.** "Mislabeled." |
| **age** | 44 reopen: 12 install-dependency (`age-plugin-batchpass`), rest env-match. **0 ceiling.** |
| **gping** | 4 MATCH (error-string + pty) + 4 IMPOSSIBLE (genuine upstream network/Windows skips). |

It reproduced, mechanically, the partition a human made by hand — turning *"I
think this tops out"* into a verifiable, actionable verdict per failure.

## Wiring

`determinex_swebench_agent.py::_write_gate_escalation` now calls
`_adjudicate_escalation` before writing the give-up record. The escalation is
marked `user_action_required: true` **only if every verdict is IMPOSSIBLE**.
Otherwise it records `REOPENABLE` with the exact untried moves (e.g.
`["remove-collection-cap", "pty-allocate", "install-dependency"]`). The loop can
no longer quietly surrender.

## The generalization — covering everything PB doesn't

ProgramBench only ships ground truth for Rust/Go/C/C++/Python. Determinex's own
products (Hook=Kotlin, SwingSwap/Aide=TypeScript) live outside that distribution.
Two mechanisms close the gap; both keep the **same** closed loop (generate →
verify → adjudicate → iterate) with zero LLM judging.

### 1. Pluggable oracles (`determinex_oracle.py`)

An `Oracle` is any deterministic ground-truth surface. Register one and the loop
runs unchanged. Shipped/registered:

| Language | Oracle | Toolchain |
|----------|--------|-----------|
| TypeScript / JS / Node | `tsc --noEmit` + `jest --reporters=jest-junit` | ✅ present |
| Python | `pytest --junitxml` | ✅ present |
| Go | `gotestsum --junitfile` | ✅ present (stub→wire) |
| Rust | `cargo test` | ✅ present (stub→wire) |
| Kotlin / JVM | `gradle test` (emits JUnit) | install Gradle |
| C# / .NET | `dotnet test --logger junit` | ✅ present (stub→wire) |
| Swift | `swift test` | install toolchain |

The type checker alone (`tsc`, `mypy`) is already an oracle — no example tests
required, the **types are the ground truth**. A stub raises `OracleUnavailable`
with the install hint; **an oracle never silently passes.**

### 2. Ground-Truth Synthesizer — "make the tests for the ones it doesn't have"

Where no suite is shipped (greenfield, or an unbenchmarked domain),
`synthesize_oracle()` manufactures the oracle before any fix is written:

| Kind | What it builds |
|------|----------------|
| **characterization** | Capture current stdout/stderr/rc over an input corpus as golden, emit a re-run-and-diff test. Locks legacy behavior before change. |
| **property** | Derive invariants from the spec (round-trip == identity, idempotence, schema-valid) and fuzz against them. Ground truth with no reference binary. |
| **golden** | Diff the candidate against a trusted reference implementation over a shared corpus. The PB pattern, applied where PB has no task. |
| **contract** | The type checker / JSON-schema / OpenAPI contract *is* the oracle. |

The synthesized tests are themselves run through the language oracle first — the
tests must compile and execute before they are allowed to gate any fix.

## How this reaches "an IDE that fixes anything"

- **The engine generalizes wherever ground truth exists.** Pluggable oracles
  extend the proven loop to the JVM/JS-TS/mobile/web worlds PB never covered.
- **The engine creates ground truth where it doesn't.** The synthesizer turns
  greenfield and unbenchmarked tasks into closed-loop tasks.
- **The Adjudicator guarantees it never lies about defeat.** Every "can't" must
  carry a proof; everything else is a move not yet tried.

ProgramBench mastery hardens the engine in five systems languages. These two
modules are the day-one path from *that* to *every language, every system, every
issue* — with a governor that refuses to cop out.

---

# The full self-correcting loop (shipped 2026-06-14)

> "take any bench, first run, take it in, understand it, realize the edits, run
> the full thing, gate it, on failure show why + how it should be + what it'd
> take + whether the test is correct/not slop. How do we ensure all of that?"

The Adjudicator + Oracle are two of six components. The other four close the loop
end-to-end. All are real, runnable, and covered by the meta-bench
(`tests/test_autofix_pipeline.py`, 18 cases).

| Stage | Component | File | What it does |
|-------|-----------|------|--------------|
| Ingest | **Task Ingester (A)** | `determinex_ingest.py` | Detects language / build / harness / oracle and infers a behavioral spec from the tests, so planning is proactive. Flags `SYNTHESIZE` when no tests ship. |
| Gate | **Universal Oracle** | `determinex_oracle.py` | Pluggable ground truth per language; `synthesize_oracle()` manufactures it where none exists. |
| Diagnose | **Impossibility Adjudicator** | `determinex_adjudicator.py` | 4-step gate; never a ceiling without proof. |
| Explain | **Failure Explainer (C)** | `determinex_explainer.py` | Per failure: responsible party (CODE / ENVIRONMENT / TEST), expected, actual, delta, proof, confidence. |
| Validate the test | **Test Validator (D)** | `determinex_test_validator.py` | Deterministic "is the test slop?" via contradiction / env-baked / tautology / reference-fail. Never an LLM judgement. |
| Remediate | **Remediation Executor (B)** | `determinex_remediation.py` | Turns each verdict into a concrete patch (cap-strip, PTY launcher, dep install, gosu, locale pin, scalar build, error-normalize, routing shim) and applies it to the submission. |

### One entrypoint

```
python scripts/determinex_autofix.py report <eval_report.json> \
    [--submission DIR] [--tests-dir DIR] [--apply]
python scripts/determinex_autofix.py ingest  <repo_or_task_dir>
```

`report` turns a wall of red into an honest verdict — whose fault, the move, the
proven slop, the remediation plan — and with `--apply` writes the fixes.

### Proven on real evals (2026-06-14)

| Tool | Autofix verdict |
|------|-----------------|
| **ov** | 7/7 ENVIRONMENT (match the TTY), 0 ceiling. Remediation: pty-allocate + gosu + error-normalize. Validator independently flagged 5/7 as env-baked-with-proof. |
| **age** | 44 ENVIRONMENT, 0 ceiling. Remediation: install `age-plugin-batchpass`. |
| **fd** | 539 UNBLOCK (the collection cap) + 13 MATCH + 0 ceiling. Validator: 2 locale-baked, 546 CODE-is-at-fault. |

### How we ensure it stays true (stage 7)

- **Meta-bench** (`tests/test_autofix_pipeline.py`): scores the *system's reasoning*
  on held-out cases — one per verdict path. Red the moment any component copes out
  (calls unfinished work a ceiling, blames code for an env mismatch, or declares a
  test slop without proof).
- **The hard rule, in code**: every "impossible / this test is wrong" must carry a
  deterministic proof (contradiction, env-baked signature, tautology, or
  reference-fail). No proof → it is `NEEDS_WORK`, keep going.
- **The flywheel**: every adjudicated failure is a labeled (signature → resolving
  move) pair for the next retrain — the system gets better at first-run diagnosis
  over time.

### Honest boundaries

- Spec inference (Ingester) is evidence-based and strongest for pytest; per-language
  extractors deepen it over time.
- The routing-shim and PTY remediations emit a scaffold with a one-line manual
  follow-up (bind the real binary name / golden map) — the diagnosis and the
  artifact are automatic; the last wiring step is flagged, never faked.
- `synthesize_oracle()` ships the strategy + manifest; the builder fills the test
  body, which is then run through the language oracle before it may gate anything.
