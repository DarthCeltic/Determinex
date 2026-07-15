# Determinex Model Notices

Determinex's source distribution (this repository) does not bundle model
weights — GGUFs are hosted separately on HuggingFace under the `darthceltic85`
account and pulled at setup time (`register_models.ps1`/`.sh`).

| Model | Base | License |
|---|---|---|
| `determinex-engineer` | Qwen2.5-Coder-1.5B-Instruct | Apache 2.0 |
| `determinex-observer-llama-3.2` | Llama-3.2-3B-Instruct | **Llama 3.2 Community License** |
| `determinex-sentinel` | Mistral-7B-Instruct-v0.3 | Apache 2.0 |

**Observer is a Llama 3.2 derivative, not Apache 2.0.** Per the Llama 3.2
Community License, the published repo name includes "Llama", carries a
"Built with Llama" notice, and links the full license text and Meta's
Acceptable Use Policy. See `docs/security/MODEL_LICENSING.md` for the full
audit. If you further fine-tune or redistribute Observer, these obligations
pass through to you.

Local model use beyond these three is operator-provided and separately
configured. Provider API keys, benchmark datasets, and third-party
checkpoints are not granted release approval by this notice. Operators are
responsible for complying with the license and usage terms of any model
they install or connect.

The release gate treats model notices as a public-distribution hygiene check, not
as a claim that every optional model backend is admitted, benchmarked, or
redistributable.
