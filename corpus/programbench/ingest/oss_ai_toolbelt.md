# OSS AI Toolbelt — "10 tools that feel illegal" → Determinex applicability map

> Source: video "10 open source AI tools that feel illegal to know about" (2026). Captured here so
> the corpus + RAG know these exist and WHERE each slots into Determinex. Honest split: what we already
> run, what's a high-value add, what's optional. Two of these directly address live Determinex problems.

## Already core to Determinex
- **Ollama** (github.com/ollama/ollama) — local model runner. **HAVE IT**: `DETERMINEX_MODELS_DIR`,
  `OLLAMA_MODELS=T:\OllamaModels`, the local builder + the box's local-only fixer.
- **LiteLLM** (github.com/BerriAI/litellm) — one API for every model (routing, fallback, cost). **HAVE
  IT (partial)**: `scripts/providers/` LiteLLM configs + `determinex_providers.py` (model-agnostic
  `generate()`). Adoption note: could consolidate the hand-rolled provider rotation onto LiteLLM's
  router for unified fallback + spend caps (relevant after the DeepSeek-credit lock).

## HIGH value — fixes a live Determinex problem
- **Crawl4AI** (github.com/unclecode/crawl4ai) — website → clean, LLM-ready markdown. **APPLIES TO**:
  the absorber's ONLINE ingestion (`determinex_pb_absorb` web rounds, `ONLINE_SOURCES.md`). I just did
  those rounds by hand with urllib/WebFetch; Crawl4AI is the right tool — clean extraction of SO
  build-errors + the PB tools' GitHub Issues (the dynamic pages urllib can't fetch). FREE + local.
- **Outlines** (github.com/dottxt-ai/outlines) — constrained/structured generation (regex / JSON /
  grammar / CFG). **APPLIES TO**: the model fixer (`determinex_pb_amplified_fix`, `determinex_contract.py`
  Output Contract Enforcer). Today the fixer emits free-text compile.sh and can drift into malformed
  or *gaming* output (the `PYTEST_CURRENT_TEST` shim I just de-gamed in the adjudicator). Constraining
  generation to a valid-fix grammar **structurally prevents** malformed + gaming output at generation
  time, not post-hoc. This is the structural complement to the integrity fix.
- **Instructor** (github.com/567-labs/instructor) — pydantic-typed structured output. **APPLIES TO**:
  the verdict/DSL schemas (adjudicator verdicts, the Determinex DSL, JSON CLI payloads). Same anti-
  malformed value as Outlines; pairs with the typed records already in `scripts/models/`.

## MED value
- **Chonkie** (github.com/chonkie-ai/chonkie) — fast RAG chunking (token / sentence / semantic /
  recursive). **APPLIES TO**: `seed_knowledge_base.py` + `determinex_pb_absorb` + `determinex_code_rag`
  (today: naive `[:1500]` snippets / line-based). Better chunk boundaries → better retrieval.
- **DSPy** (github.com/stanfordnlp/dspy) — programmatic prompting + prompt/weight optimization against
  a metric. **APPLIES TO**: the reimpl/fixer prompts (`build_prompt`, `build_fix_prompt`) — auto-tune
  them against the ORACLE (the metric is already sound), a natural fit for the amplifier.

## LOW / optional
- **Marker** (github.com/VikParuchuri/marker) — PDF/doc → markdown. Use: ingest PDF papers/specs into
  the corpus (the absorber is md/txt only today). Niche until we ingest PDFs.
- **Qdrant** (github.com/qdrant/qdrant) — vector DB. Use: semantic vector RAG vs the current
  keyword/symbol code-RAG. Determinex deliberately chose keyword (free/fast/local, no service); Qdrant
  only earns its keep if we scale RAG to semantic search.
- **Langfuse** (github.com/langfuse/langfuse) — LLM observability/tracing/eval. Use: trace model
  calls in the hive/fixer. Complements the existing WAL + eval reports; lower marginal value.

## Adoption priority for Determinex
1. **Crawl4AI** → absorber online ingestion (replaces my manual web rounds; free + local).
2. **Outlines / Instructor** → constrained fixer output (structural anti-gaming + anti-malformed —
   ties directly to the adjudicator de-gaming work).
3. **Chonkie** → RAG chunk quality. **DSPy** → oracle-metric prompt optimization.
4. Marker / Qdrant / Langfuse → only when the specific need (PDFs / semantic RAG / deep tracing) lands.

## Integration status (2026-06-29) + credit — "do them if they benefit"
- **Crawl4AI** (unclecode/crawl4ai) — **INTEGRATED**: optional backend in the absorber's `_fetch_clean`
  (clean JS-rendered markdown for the SO / GitHub-Issues pages urllib can't read; urllib fallback).
  Credited in code + commit `fa09b3ea1`.
- **Outlines / Instructor** (dottxt-ai/outlines, 567-labs/instructor) — **PRINCIPLE APPLIED**: their
  "accept only legitimate, constrained output" idea drove closing the auto-gaming hole (de-gamed
  `_routing_shim`, `pytest-current-test-routing` GREEN→RED), commit `c4ebadf87`. The literal packages
  constrain model logits — they don't fit our Ollama+shell fixer — so this is the idea, credited, not
  the dependency.
- **Ollama, LiteLLM** — already core to Determinex.
- **Chonkie / DSPy / Marker / Qdrant / Langfuse** — **DEFERRED, honestly**: the absorber's
  markdown-aware split is already decent (Chonkie), keyword RAG is the deliberate free/local choice
  (Qdrant), no PDFs ingested yet (Marker), the WAL covers tracing (Langfuse), DSPy is a later
  oracle-metric prompt-optimization play. Credited above; wired the day the specific need lands.

Full credit to the OSS authors (repos linked above). Source: the "10 open-source AI tools that feel
illegal to know about" video.
