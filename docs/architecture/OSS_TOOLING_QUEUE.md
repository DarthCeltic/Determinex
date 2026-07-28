# OSS Tooling Queue

> Created 2026-07-26. Nine open-source tools evaluated against what Determinex
> specifically is — a compiler-oracle-driven, local-first, privacy-sovereign
> correctness system — rather than against "what's popular in AI tooling."
>
> Ranked by payoff. Each entry states the concrete integration point, so this is
> a work queue, not a reading list. Per the AUDIT-BEFORE-BUILD mandate in
> `CLAUDE.md`, every item names the existing canonical module it extends; none
> of these may land as a parallel duplicate.
>
> **Status: none started.** Item 1 has a verified finding attached; the rest are
> evaluated but unproven. Nothing here is a claim about a fix that exists.

---

## 1. tree-sitter — DONE. Found and fixed a real plaintext leak, not just a test gap.

**Correction chain, same item, same week.** First pass called it a security
finding ("`lang_extractor.py` is 42 regex ops for 6 languages"). That was wrong
— tree-sitter is the authoritative extractor. Second pass concluded from that
correction that "the architecture is sound... the 9 tree-sitter grammars have no
leak assertion behind them" and scoped the remaining work as test-only. That was
also wrong: writing the leak tests found a real, live plaintext leak.

**What was actually true, measured 2026-07-26, before the fix:**
`TS_SUPPORTED_LANGUAGES` (the constant the second pass printed as "verified live")
is a hardcoded frozenset of 9 — a declaration of which languages have queries
written, not a probe of which grammars are installed. Actually installed at the
time: **3 of 9** (rust, go, javascript — `pyproject.toml [cloak]` never declared
the other 6). TypeScript had neither a grammar nor a `_LANG_DEF_PATTERNS` regex
entry, so `extract_treesitter_identifiers` returned empty, the regex fallback
returned empty, `SymbolMap.build({})` produced an empty map, and
`obfuscate_source` became an identity function. **A `.ts` file went to the cloud
LLM byte-for-byte unmodified while the pipeline reported success** — the exact
failure `CloakObfuscationError`'s fail-closed design exists to prevent.

**Fixed:**
1. Installed the 6 missing grammars (`pip install tree-sitter-{typescript,java,
   ruby,php,c,cpp}`) and added them to `pyproject.toml [cloak]`.
2. Every language's query was missing parameter/field/local-variable captures —
   a systematic gap in every `_QUERIES` entry, not a per-language quirk. Added
   captures for all 9.
3. `_build_cloak_context_nonpython` now fails closed: scanning real files and
   extracting 0 identifiers raises `CloakObfuscationError` instead of returning
   an identity context. `DETERMINEX_CLOAK_ALLOW_DEGRADED=1` still downgrades it
   to a warning, matching the existing import-time tree-sitter check.
4. `loadable_languages()` added — probes what actually imports and compiles, so
   capability can be reported honestly instead of from the static list.

**Result:** 8 of 9 languages now obfuscate their fixture completely (`tests/
test_cloak_language_coverage.py`, 42 passing). One gap remains, `xfail(strict=
True)`: JavaScript's `this.zzqField = 0` is a `member_expression` assignment,
not a `field_definition` — capturing those naively would also rewrite external
API property access (`res.status`, `JSON.parse`), so it needs a safe-list-aware
rule, not a raw query. Deferred, not silently accepted.

**Bonus already banked:** because the grammars are installed, items 4 (ast-grep)
and 9 (difftastic) are cheaper than they would otherwise be — the tree-sitter
dependency they share is present, now for all 9 languages instead of 3.

**Method note, reinforced twice in one item:** the first correction disproved a
claim by running one command. The second "correction" *should* have but didn't
— it accepted a printed constant as evidence instead of testing behavior. The
lesson generalizes past this one item: printing a capability list is not the
same as invoking the capability.

---

## 2. Mutation testing — measure oracle completeness instead of asserting it

`cargo-mutants` (Rust), `mutmut` / `cosmic-ray` (Python), `go-mutesting` (Go).

The stated thesis is
`score = oracle-completeness × technique-coverage × search-budget(+escalation)`.
Two of those three are measured today; **oracle-completeness is asserted.**
Mutation testing measures it directly: inject a semantic mutation, re-run the
oracle, and if the oracle still passes, that mutation is a hole in the oracle.

Two places this plugs in:
- `scripts/determinex_test_validator.py` — currently proves "slop" via
  contradiction / env-baked / tautology / reference-fail. A surviving-mutant
  score adds a fifth deterministic signal: a suite that catches no mutants is
  provably incomplete, with a reproducible artifact and no LLM judgement.
- `scripts/determinex_synthesize.py` — after `synthesize_oracle()` manufactures
  a suite, mutation score is the natural acceptance gate before that oracle is
  trusted to declare anything `solved`. This directly hardens the soundness
  contract that `docs/architecture/CORRECTNESS_AMPLIFIER.md` calls load-bearing.

**Risk:** low. **Cost:** CPU time — mutation runs are slow; scope to synthesized
oracles first, not the whole PB corpus.

---

## 3. Constrained decoding — Outlines / llguidance / llama.cpp GBNF

Forces model output to satisfy a grammar or JSON schema *at the sampling level*:
tokens that would violate the grammar are masked out and literally cannot be
emitted.

The amplifier's lift is `1−(1−p)^K` — it raises the number of samples. Constrained
decoding raises `p` itself, by deleting an entire failure class (malformed JSON,
truncated code blocks, prose where a patch was required) rather than resampling
past it. The two compound.

Integration points: `scripts/determinex_contract.py` (Output Contract Enforcer —
today it validates *after* generation; this moves enforcement into generation) and
`scripts/determinex_verified_search.py`'s `generate(prompt, temp) -> str` contract.
Ollama already supports GBNF grammars, so the local 1.5B/3B/7B path can use this
with no new inference server.

**Highest expected multiplier on the small-local-model path.** **Risk:** medium —
an over-tight grammar can suppress valid outputs; measure `p` before/after.

---

## 4. ast-grep — retire the regex anchor hacks in the SWE-bench patcher

`CLAUDE.md` documents a series of hard-won regex workarounds in
`scripts/determinex_swebench_agent.py`: "Strategy 5 paren-stripped anchor",
line-number-prefix stripping, the feedback-injection anchor fix. Each was a real
bug fixed with a more careful string comparison — which is the signature of
doing structural work with a lexical tool.

`ast-grep` does structural pattern-match and rewrite across languages (Rust core,
tree-sitter grammars — shares item 1's dependency). Anchor matching becomes
"find this function node," which is exactly what those workarounds approximate.

**Risk:** medium — this is the patch path; needs the SWE-bench harness green
before and after, so sequence it after item 1 lands the grammars.

---

## 5. DSPy — optimize prompts against the compiler oracle

DSPy optimizes prompts against a metric. The hard part of using it is normally
that no sound metric exists. **Determinex already has one:** the Compiler Oracle
returns a deterministic pass/fail with zero hallucination.

Feed `validate_project` / `OracleResult` as the DSPy metric and let it optimize
the Architect and Builder prompts. Every optimization step is compiler-verified,
so this cannot drift into rewarding plausible-looking output.

Natural home: `scripts/hive/` prompt construction + `determinex_router.py`.
**Risk:** medium — adds a dependency with its own LLM-call patterns; must respect
the PRIVATE + FREE mandates (local models only for bulk optimization runs).

---

## 6. SQLite FTS5 — proper BM25, zero new dependency — **DONE 2026-07-26**

Shipped as `scripts/corpus/corpus_fts.py`, blended into `hybrid_search()`, 19 tests in
`tests/test_corpus_fts.py`. Notes on what the work actually found:

- The predicted win was real but the *reason* was bigger than "no BM25". `_tokens()`
  uses `[a-z0-9_]+`, which **keeps underscores**, so a snake_case corpus key is one
  unmatchable token. Query "provenance restore" scored the entry literally named
  `_provenance_restore_2026_06_22` a **1**, in a five-way tie including two unrelated
  smolvlm2 entries. BM25 ranks it 1.000, next result 0.537.
- Two real bugs surfaced while wiring it:
  1. **Key-namespace mismatch.** `corpus_embeddings._entries()` namespaces
     `class_pattern::X`; `search()` emits bare `X`. So `hybrid_search` blended them as
     two *competing* rows — a class_pattern could never reinforce itself. Fixed with
     `_blend_key()`.
  2. **Global-index contamination.** The BM25 and semantic legs read prebuilt indexes
     built from the *default* corpus and ignore the `corpus=` argument. Passing an
     explicit corpus therefore scored it against the full corpus's documents. Caught by
     an existing test. Both legs now disable when `corpus` is supplied.
- `.sqlite3` was missing from `corpus_wiring_census._ARTIFACT_SUFFIXES`, so the census
  was blind to an entire artifact class. Added.

Original evaluation follows.

---


`determinex_corpus_api.search()` is raw token overlap; its own docstring admits
"no embeddings, no BM25, no reranking, deliberately." FTS5 ships **inside Python's
stdlib `sqlite3`** — BM25 ranking, phrase and prefix queries, no new dependency
and no service.

This is the cheapest quality win available and completes the retrieval triangle:
BM25 (lexical) + embeddings (paraphrase, `corpus_embeddings.py`) + heading-tree
navigation (structural, `corpus_tree_index.py`). All three then blend in
`hybrid_search()`.

**Risk:** very low. **Do this one first if a quick win is wanted** — it is hours,
not days.

---

## 7. Property-based testing — Hypothesis / proptest / fast-check

`scripts/determinex_synthesize.py` hand-rolls "type-aware property tests" and
deliberately skips what it cannot type soundly. These libraries are the mature
form of exactly that mechanism, with shrinking (minimal counterexamples) and
stateful testing that a hand-rolled generator will not match.

Hypothesis's `ghostwriter` can emit property tests directly from a signature,
which is the greenfield path in `determinex_build_from_idea.py`. Per-language:
`proptest` (Rust), `fast-check` (TS), `gopter`/`rapid` (Go).

**Risk:** low, and it strengthens the same soundness contract as item 2.

---

## 8. cargo-fuzz / AFL++ / libFuzzer — real fuzzers for `fuzz_diagnose`

`docs/architecture/NATIVE_REIMPL_LOOP.md` has a `fuzz_diagnose` stage in the
autonomous driver (`determinex_reimpl_drive`). Coverage-guided fuzzers are the
mature version of that stage and produce differential findings directly: run the
upstream binary and the native reimplementation on the same generated input and
diff observable behavior. That is the reimplementation loop's core question,
answered mechanically.

**Risk:** medium — fuzzing is slow and needs a corpus; scope to one tool as proof.

---

## 9. difftastic — structural diff for provenance

`project_pb_upstream_identity_scan_20260716` built an upstream-diff dimension for
provenance checking. Textual diff is noisy for that question: reformatting reads
as change, while a renamed identifier over identical structure reads as small.
`difftastic` diffs ASTs (tree-sitter again — shares item 1's grammars), which
matches what provenance actually asks: *is this the same program?*

**Risk:** low, narrow blast radius — reporting only, no behavior change.

---

## Suggested order

1. **6 (FTS5)** — hours, zero dependency, immediate retrieval quality.
2. **1 (Cloak leak tests)** — test-only, small, and it guards the subsystem
   named paramount. Not the rebuild originally written here; tree-sitter is
   already in place.
3. **2 (mutation testing)** — makes the completeness term measurable.
4. **3 (constrained decoding)** — biggest lift for the local-model path.
5. Then 7, 4, 9, 5, 8 as capacity allows.

## Method note

Item 1 was drafted as a "regex where AST was claimed" security finding and was
wrong — the check that disproved it took one command. The queue is written so
every entry names the file it touches, which makes that check cheap. **Verify
each item against the code before starting it; several of these may already be
partly built.** This repo's own history (`METHODOLOGY_INVALIDATION`, the
provenance audit, the measurement audit) is a record of claims that survived
because nobody ran the cheap check.
