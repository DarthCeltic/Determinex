# Model Weight Redistribution Licensing (audited 2026-07-01)

> Triggered by the Tier 3 legal-review todo ("model weight redistribution
> licensing"). Ground truth for base models pulled from
> `T:/determinex-models/brain_manifest.json` (`base_model` field per version) —
> not from CLAUDE.md's own Model Family table, which was found wrong for
> Observer during this audit (see correction below).

## Base models actually in use

| Family | Ollama tag | Base model (per brain_manifest.json) | License |
|---|---|---|---|
| C1 Engineer | `determinex-engineer-v*-dsl` | `Qwen2.5-Coder-1.5B-Instruct` | Apache 2.0 |
| C3 Observer | `determinex-observer-v*-dsl` | `meta-llama/Llama-3.2-3B-Instruct` | **Llama 3.2 Community License** |
| C7 Sentinel | `determinex-sentinel-v*-dsl` | `mistralai/Mistral-7B-Instruct-v0.3` | Apache 2.0 |

**Correction to CLAUDE.md**: the Model Family table listed C3 Observer as
"3B (Qwen2.5)" — this is wrong. `brain_manifest.json` records
`base_model: "meta-llama/Llama-3.2-3B-Instruct"` consistently for every
Observer version it tracks (v4, v5); no version anywhere is recorded as
Qwen-based. v6-dsl (the current CLAUDE.md-referenced tag) isn't itself
logged in this manifest, but LoRA/fine-tune version chains don't silently
change base architecture without a note, and none exists — treat Observer
as Llama-3.2-3B-derived until/unless proven otherwise. Fixed in CLAUDE.md
2026-07-01.

## Why this matters

Engineer and Sentinel are Apache 2.0 — fully permissive. Fine-tuning,
redistributing derivative weights, commercial use: no special obligations
beyond standard Apache 2.0 notice/license inclusion.

**Observer is different.** The Llama 3.2 Community License is Meta's
custom open-weight license, not Apache 2.0. It attaches real obligations to
any distribution of the model or a fine-tuned derivative:

1. **Attribution**: distributed derivatives must include a "Built with
   Llama" notice.
2. **Naming**: any AI model created using Llama Materials — including a
   fine-tune like `determinex-observer` — must include "Llama" in its name
   when distributed to others.
3. **License pass-through**: a copy of the Llama 3.2 Community License must
   accompany any redistribution of the model or its weights.
4. **Acceptable Use Policy**: distributees must comply with Meta's AUP
   (prohibits certain use categories).
5. **>700M MAU carve-out**: if Determinex (or a licensee) ever serves a
   product/service built on Llama Materials to more than 700 million
   monthly active users, the standard license terms stop applying and a
   separate license must be requested from Meta. Not a near-term concern
   at Determinex's current stage, but worth knowing exists.

## Current exposure

**Low, but latent.** As of this audit, Determinex does not ship or distribute
model weights externally — Engineer/Observer/Sentinel run locally via
Ollama for the operator's own use, and the product is model-agnostic
(any model, local or cloud, plugs into the `generate()` contract).
No current distribution channel triggers the Llama license's obligations.

**This becomes live the moment weights ship** — e.g. if a future release
bundles a pre-trained Observer GGUF with the installer, publishes it to
Hugging Face, or otherwise hands the fine-tuned weights to a third party.
At that point, before shipping:

- [ ] Include "Built with Llama" attribution in the release notes / model card
- [ ] Ensure any public-facing name for the Observer model includes "Llama"
      (the internal codename `determinex-observer` can stay internal; anything
      distributed to third parties needs the Llama-inclusive name)
- [ ] Bundle a copy of the Llama 3.2 Community License with the distribution
- [ ] Confirm the intended use doesn't violate Meta's Acceptable Use Policy
- [ ] Re-check the >700M MAU threshold isn't relevant at the time of shipping

No action is required today. This doc exists so the obligation isn't
discovered for the first time during an actual release, and so CLAUDE.md's
model-family table doesn't keep asserting the wrong base model.

## Training corpus licensing (separate concern, not audited here)

This audit covers *base model* redistribution terms only. It does not cover
whether the fine-tuning corpus itself (ProgramBench-derived training data,
SWE-bench data, etc.) carries its own licensing constraints on distribution
of the resulting fine-tuned weights — that's a separate question and remains
open. The Ethics Oracle's Layer 5 (`determinex_safety.check_license`) guards
against copyleft *code* entering the corpus, which is a different, narrower
concern than base-model redistribution terms.
