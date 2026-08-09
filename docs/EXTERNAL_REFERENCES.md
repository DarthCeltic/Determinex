# External references — checked against what Determinex claims

Sources fetched and read, not judged from titles. Each entry says why it matters *here*, and
where it **challenges or sharpens** a claim we have already made — which is more useful than
anything that merely agrees with us.

**Coverage is partial and stated as such.** The reading list this came from has ~30 entries;
the ones below were fetched and read in priority order (prefix caching, vLLM internals,
speculative decoding — the three that overlap our own measured findings). The rest are listed
at the bottom as unread. Nothing here is summarised from a title.

---

## Directly relevant — touches a claim we make

### vLLM prefix caching — mechanism behind our 93.5% vs ~1% measurement
`gdymind.com/2025/04/11/vLLM-03-prefix-caching/` — **read**

This explains the result we measured rather than merely agreeing with it. vLLM hashes tokens
in fixed 16-token blocks, and "hash of the current block" combines "the previous block hash
value, block tokens, and extra keys" — a *chain*. So a single differing token at the front
invalidates the first block's hash and every block after it, which is exactly why our
one-distinct-token-per-request arm collapses from **93.5% to ~1%** rather than degrading
gracefully. The block size matches what the instance reports (`block_size="16"` in
`cache_config_info`).

Two details worth carrying into our own text: "incomplete blocks are not eligible for
sharing", and divergence is positional — "ABCDE" vs "ABCDF" diverge at the final token.

**It contains no measured hit rates.** Ours does. So our number is the empirical complement to
this mechanism, not a restatement of it — worth saying plainly rather than implying we
discovered the mechanism.

### Speculative decoding / DSpark — the word "verify" means something else there
`gdymind.com/2026/06/29/DSpark/` — **read**

This is the most important entry, because it uses our vocabulary for a different thing and a
judge could reasonably conflate them.

In speculative decoding, "a small drafter model proposes γ tokens quickly" and "all γ tokens
are fed into the target model in one forward pass". **The verifier is a model.** The source
notes the approach "trades output determinism for speed, using probabilistic confidence
estimates rather than guaranteed correctness", and does not claim output identical to running
the target model alone.

Determinex's verifier is a compiler or a test suite. Same word, opposite epistemics: theirs
asks *does the bigger model agree*, ours asks *does it compile and pass*. Speculative decoding
makes the same model cheaper; verified search makes a weaker model *correct*.

They are also **composable, not competing** — spec decoding lowers the cost of each candidate,
which lowers the cost of K candidates. Nothing in our loop would need to change.

---

## Adjacent — useful context, no direct claim overlap

- `gdymind.com/2026/04/04/vLLM-Omni-deep-dive/` — **listed, not read.** Multimodal vLLM;
  Determinex is text-to-code, so no overlap expected, but not verified.
- `gdymind.com/2026/03/02/sliding-window-attention/` — **listed, not read.** KV cache under
  sliding-window attention. Potentially relevant to the K-ceiling arithmetic
  (`K < floor(kv_cache_tokens / max_model_len)`) if a served model uses sliding windows.
- `gdymind.com/2026/07/06/Ragged-Paged-Attention-on-TPU/` — TPU, not ROCm. Off-hardware.
- `gdymind.com/2026/04/27/DeepSeek-V4-attention-deep-dive.../` — architecture-level.

## Not fetched

The following were in the reading list and are **not** covered here: P/D disaggregation,
vLLM v1, RoPE, MoE history / OpenMoE, Perplexity DeepSeek MoE, FastAGI spec-decoding talk,
JAX 101, CUDA 101, `jax.jit`/`torch.compile`/CUDA graph, XLA01/XLA02, Pallas 101 and Pallas
examples, training memory, 5D parallelism, knowledge distillation, loss in pretraining/SFT,
truncated importance sampling, PPO, and the two conference QA posts.

Several of those link paths 404 from the shortlinks — the blog appears to have reorganised its
URLs since the list was published. Rather than guess at content from titles, they are recorded
as unread.

## What changed as a result

Nothing measured. One framing sharpened: the submission should distinguish its use of
"verified" from speculative decoding's, because the terms collide and only one of them means
ground truth.
