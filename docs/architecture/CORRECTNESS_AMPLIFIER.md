# The Correctness Amplifier — making any model correct on anything

> **Status**: keystone shipped 2026-06-14 (`scripts/determinex_verified_search.py`),
> proven (weak model p=0.20 → 100% solved). The remaining 6 pieces are specified
> below with their build order.

## The thesis

The Oracle + Adjudicator + Validator make a *strong* model **honest**. The
Correctness Amplifier makes a *weak* model **correct**. The goal — *"any LLM,
regardless of how good or large or small, can access this system and work
anything, and it be right"* — is achievable because of one fact:

> If an answer can be **verified** deterministically, a model with per-attempt
> success **p** sampled **K** times succeeds with probability **1 − (1−p)^K**.
> So any model with **p > 0** is driven toward correct. Decompose until p is
> workable; sample against the oracle; keep what passes.

Demonstrated: a generator right 20% of the time, under verified search (K=15),
solved **200/200** tasks (avg 4.8 samples). This is not a model improvement — the
model stayed weak. The *system* made it correct.

## The soundness contract (load-bearing)

Verified search yields *correct* output **only if the oracle is sound.** A wrong
test makes the search converge *confidently to a wrong answer*. Therefore every
oracle is paired with the **Test Validator** (`determinex_test_validator.py`):
garbage oracle in → confident garbage out. The keystone refuses to report
`solved` without a passing `OracleResult` and records the proof.

## The 7 pieces (all shipped 2026-06-14)

| # | Piece | File | Role |
|---|-------|------|------|
| 1 | **Verified Search Orchestrator** | `determinex_verified_search.py` | best-of-K against the oracle; converts p→1. Model-agnostic: `generate(prompt,temp)->str` + `verify(str)->OracleResult`. |
| 2 | **Adaptive Decomposer** | `determinex_decompose.py` | split into independently-verifiable leaves sized to capability (TINY=1 check/leaf … WHOLE=no split). |
| 3 | **Solution Retrieval / Case Memory** | `determinex_case_memory.py` | retrieve *oracle-verified* past fixes at inference; refuses unverified cases (no poisoning). |
| 4 | **Context Provisioner** | `determinex_context.py` | minimal-sufficient, ranked, budget-bounded context (token-overlap, no embeddings needed). |
| 5 | **Progress / Loop Detector** | `determinex_progress.py` | CONTINUE / WIDEN / RE_DECOMPOSE / ESCALATE from a stream of (digest, score). Anti-thrash. |
| 6 | **Output Contract Enforcer** | `determinex_contract.py` | reject malformed patch/JSON/syntax *before* the oracle → well-formed floor; `guard()` wraps any model. |
| 7 | **Model-Agnostic Router** | `determinex_router.py` | any LLM registers via the universal contract; routes each leaf to the cheapest model that clears it, escalates up the tier ladder, stops honestly on a proven ceiling. |

**Unified orchestrator** `determinex_amplified_solve.py` composes all seven, plus
`make_hive_solver()` to drop it into the hive as the builder's patch generator
(local model under verified search against the Compiler Oracle, escalating to a
stronger model per leaf).

### Proven (meta-bench, 26 cases)

- Verified search: weak p=0.20 → 200/200 solved.
- Router: tiny (p=0.10) escalating to strong (p=0.95) → 100/100.
- **Unified: a 1.5B-class model (p=0.15/check) on a 6-check task — one-shot
  success ≈ 0.15⁶ ≈ 1-in-90,000 — solves 68% via decompose + verified search.**
  A ~60,000× lift from the *system*, not the model. That is the whole thesis.

## How a tiny model "works anything" end to end

1. **Ingest** (`determinex_ingest.py`) understands the task + picks the oracle.
2. **Decompose** (#2) splits it into leaves small enough for the model's p.
3. For each leaf, **Verified Search** (#1) samples K candidates from *any* model,
   filters by the **Oracle**, keeps the one that passes — with **Retrieval** (#3)
   and **Context** (#4) raising p, and the **Contract Enforcer** (#6) guaranteeing
   well-formedness.
4. On exhaustion, the **Adjudicator** decides: reopenable (re-decompose / raise K /
   route up) vs genuine ceiling (with proof). Never a false surrender.
5. **Explainer + Validator + Remediation** handle the failure surface.
6. Every verified solve feeds the **flywheel** + **Case Memory** (#3), so p rises
   over time and the next task is easier for the same small model.

## Why this is the moat

Other systems make a *better model* the unit of progress. Determinex makes the
*system* the unit of progress: a sound oracle + verified search means correctness
is bounded by the oracle's soundness, not the model's strength. That is what lets
*any* model — including ones that do not exist yet — plug in and be right.

## Greenfield: idea -> verified program (shipped 2026-06-14)

The last capability gap -- building when NO tests exist -- is closed.

- **`scripts/determinex_synthesize.py`** turns an idea/spec into a SOUND oracle:
  example assertions extracted exactly (deterministic); invariants become
  TYPE-AWARE property tests (input type inferred from the examples); a property it
  cannot type soundly is SKIPPED, never emitted wrong (no slop). The synthesized
  oracle is validated to run before it may gate anything.
- **`scripts/determinex_build_from_idea.py`** chains it end to end: idea -> synthesize
  sound oracle -> amplified solve (any model) -> a program returned ONLY if the
  oracle passes, with proof. Proven live: a 1.9 GB local model produced a verified
  `rle` implementation against a 5-check synthesized oracle, first try.
- **`scripts/determinex_doctor.py`** (pre-existing, verified) reports the machine's
  capability tier (0 pure-python -> 1 +local model -> 2 +docker -> 3 +cloud), so
  "runs on any computer" is inspectable with graceful degradation.

Honest boundary: synthesis is fully sound when the idea carries examples/invariants
(the common case). An example-free vague idea degrades to a symbol-exists smoke
test; richer model-assisted test inference (re-validated by the language oracle)
is the next increment. Meta-bench: 32 cases.
