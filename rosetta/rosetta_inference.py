"""
rosetta/determinex_inference.py — Rosetta Stone Soft-Prefix Injection Bridge

Implements Layer 2 of the Determinex latent communication protocol:
    Sender model's pooled hidden state
        → projected through RosettaStone into target embedding space
        → injected as a soft prefix via llama-cpp-python's CTypes interface
        → target GGUF model generates conditioned on sender's latent context
          WITHOUT the sender's content appearing as text tokens

This is the runtime delivery mechanism that closes the loop between:
    - rosetta/train_rosetta.py  (trains the W projection matrices)
    - rosetta/kv_store.py       (stores compressed mid-layer states)
    - rosetta/latent_rag.py     (retrieves semantically relevant states)

Architecture:
    The llama-cpp-python library exposes the underlying llama.cpp C API via
    ctypes. The key function is llama_decode(), which accepts llama_batch
    structs. By constructing a batch with embd != NULL (embedding tokens
    rather than integer token IDs), we feed raw float vectors directly into
    the model's first transformer layer, bypassing the token embedding lookup.

    This is the mechanism described in Prefix-Tuning (Li & Liang, 2021):
    prepending learned continuous vectors to the model's context to steer
    generation without modifying weights.

VRAM note:
    The HF model used for extraction is unloaded BEFORE the GGUF model is
    loaded (see extract_midlayer.py). Injection operates on already-extracted,
    already-projected tensors — no model overlap in VRAM.

Usage:
    from rosetta.determinex_inference import RosettaInferenceBridge

    bridge = RosettaInferenceBridge(
        model_path="models/engineer.gguf",
        rosetta_path="outputs/rosetta/best",
        target_family="qwen",
    )
    output = bridge.generate_with_prefix(
        prompt="Implement a thread-safe counter in Rust.",
        prefix_state=projected_tensor,   # [target_family_dim] float32
        max_tokens=512,
    )
"""

import sys
from pathlib import Path

import numpy as np
import torch

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


# ---------------------------------------------------------------------------
# IMPORTS — fail gracefully if llama-cpp-python not installed
# ---------------------------------------------------------------------------

try:
    from llama_cpp import Llama, llama_cpp

    _LLAMA_AVAILABLE = True
except ImportError:
    _LLAMA_AVAILABLE = False
    print(
        "[RosettaBridge] WARNING: llama-cpp-python not installed. "
        "Soft-prefix injection unavailable. Install with: pip install llama-cpp-python",
        flush=True,
    )

try:
    from train_rosetta import RosettaStone
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from train_rosetta import RosettaStone


# ---------------------------------------------------------------------------
# BRIDGE
# ---------------------------------------------------------------------------


class RosettaInferenceBridge:
    """
    Loads a GGUF model and injects Rosetta-projected latent states as soft
    prefixes before generation.

    The injection uses llama-cpp-python's low-level batch API:
        llama_batch.embd != NULL  →  embeddings mode (float vectors)
        llama_batch.token != NULL →  token mode (integer IDs)

    By prepending K float vectors (one per prefix token) before the real
    token embeddings, the model's attention mechanism attends to the
    projected latent context from the first layer onward.

    Limitations at Tier 0 (6GB VRAM):
        - One GGUF model at a time. The extractor HF model must be unloaded
          before this bridge is instantiated.
        - Prefix vectors must match the GGUF model's hidden_size exactly.
          The RosettaStone decoder handles the projection.
        - Soft-prefix injection via embedding batch requires llama.cpp
          compiled with LLAMA_EMBEDDING=ON (default in llama-cpp-python >= 0.2.57).
    """

    def __init__(
        self,
        model_path: str | Path,
        rosetta_path: str | Path,
        target_family: str,
        n_ctx: int = 4096,
        n_gpu_layers: int = -1,  # -1 = all layers on GPU
        verbose: bool = False,
    ):
        """
        Args:
            model_path    : path to the target GGUF model file
            rosetta_path  : path to trained RosettaStone weights directory
            target_family : model family key (e.g. "qwen", "mistral")
            n_ctx         : context window size
            n_gpu_layers  : GPU offload layers (-1 = full GPU)
            verbose       : enable llama.cpp verbose logging
        """
        if not _LLAMA_AVAILABLE:
            raise RuntimeError(
                "llama-cpp-python is required for soft-prefix injection. "
                "Install: pip install llama-cpp-python"
            )

        self.target_family = target_family
        self.model_path = Path(model_path)

        # Load RosettaStone (CPU only — tiny <10M params)
        print(f"[RosettaBridge] Loading RosettaStone from {rosetta_path}...", flush=True)
        self.stone = RosettaStone.load(Path(rosetta_path))
        self.stone.eval()

        # Validate target family exists in stone
        if target_family not in self.stone.families:
            raise ValueError(
                f"Family '{target_family}' not found in RosettaStone. "
                f"Available: {list(self.stone.families.keys())}"
            )

        self.target_dim = self.stone.families[target_family]

        # Load GGUF model
        print(
            f"[RosettaBridge] Loading GGUF: {self.model_path.name} "
            f"(family={target_family}, dim={self.target_dim})...",
            flush=True,
        )
        self._llm = Llama(
            model_path=str(self.model_path),
            n_ctx=n_ctx,
            n_gpu_layers=n_gpu_layers,
            embedding=True,  # required to enable embedding batch mode
            verbose=verbose,
        )

        # Verify embedding dimension matches target family — HARD FAIL on mismatch.
        # The historical silent-warning path produced fake-good results because
        # projection through a wrong-sized stone is meaningless. The registry +
        # RosettaDimensionMismatch enforce this at the load boundary.
        n_embd = self._llm._model.n_embd()
        if n_embd != self.target_dim:
            try:
                from rosetta.model_registry import RosettaDimensionMismatch

                raise RosettaDimensionMismatch(
                    source_model="(unspecified-source)",
                    source_arch=target_family,
                    expected_dim=self.target_dim,
                    actual_dim=n_embd,
                    target_model=str(self.model_path),
                    target_arch=target_family,
                )
            except ImportError:
                # Registry not on path — fall back to RuntimeError so we still fail loud
                raise RuntimeError(
                    f"GGUF embedding dim ({n_embd}) != RosettaStone target dim ({self.target_dim}) "
                    f"for family {target_family!r}. Refusing to project through wrong-sized stone."
                )
        self.n_embd = n_embd

        print(
            f"[RosettaBridge] Ready. n_embd={n_embd}, n_ctx={n_ctx}",
            flush=True,
        )

    def project(
        self,
        source_hidden: torch.Tensor,
        source_family: str,
    ) -> torch.Tensor:
        """
        Project a source model's pooled hidden state into the target model's
        embedding space via the RosettaStone.

        Args:
            source_hidden : [source_family_dim] float32 tensor
            source_family : family key of the source model

        Returns:
            [target_dim] float32 tensor in the target model's embedding space
        """
        if source_hidden.dim() != 1:
            raise ValueError(
                f"Expected 1D pooled state, got shape {source_hidden.shape}. "
                "Mean-pool before calling project()."
            )

        # Validate the source tensor's dim matches the source arch's registered
        # hidden_dim BEFORE projection. Catches the historical bug
        # (qwen2 expects 3584, got 1536) at the registry boundary, with structured
        # context. Never silently downgrades to self-injection — that decision
        # belongs to the caller, not project().
        try:
            from rosetta.model_registry import (
                RosettaArchUnknown,
                RosettaDimensionMismatch,
                get_arch,
                resolve_model,
                validate_hidden_dim,
            )

            spec = resolve_model(source_family)
            if spec is not None:
                validate_hidden_dim(spec, source_hidden, target_model=self.target_family)
            else:
                # source_family may be a bare arch label (e.g. "qwen2_1b5"); try arch
                try:
                    arch = get_arch(source_family)
                    if source_hidden.shape[0] != arch.hidden_dim:
                        raise RosettaDimensionMismatch(
                            source_model=f"arch:{source_family}",
                            source_arch=arch.key,
                            expected_dim=arch.hidden_dim,
                            actual_dim=source_hidden.shape[0],
                            target_model=self.target_family,
                            target_arch=self.target_family,
                        )
                except RosettaArchUnknown:
                    # Unknown to the registry — let stone.translate raise its own error
                    pass
        except ImportError:
            pass  # registry unavailable; legacy path

        with torch.no_grad():
            projected = self.stone.translate(
                src_family=source_family,
                tgt_family=self.target_family,
                hidden=source_hidden.unsqueeze(0).float(),
            )
        out = projected.squeeze(0).float()
        # L8-B: L2-normalise so deployed vectors stay on the unit hypersphere even
        # when the loaded rosetta_v1.pt was trained before the decoder norm was added.
        return torch.nn.functional.normalize(out, dim=0)

    def generate_with_prefix(
        self,
        prompt: str,
        prefix_vectors: list[torch.Tensor],
        max_tokens: int = 512,
        temperature: float = 0.2,
        top_p: float = 0.95,
        repeat_penalty: float = 1.1,
    ) -> str:
        """
        Generate text with soft-prefix injection.

        The prefix_vectors are injected as continuous float vectors into the
        model's first layer via the embedding batch API, followed by the
        tokenized prompt. The model attends to the prefix context from the
        first transformer layer onward.

        Args:
            prompt         : the user's text prompt
            prefix_vectors : list of [n_embd] float32 tensors to prepend
                             (typically 1–3 projected Rosetta states)
            max_tokens     : maximum new tokens to generate
            temperature    : sampling temperature
            top_p          : nucleus sampling threshold
            repeat_penalty : repetition penalty

        Returns:
            Generated text string (without the prompt)
        """
        # Tokenize prompt
        prompt_tokens = self._llm.tokenize(
            prompt.encode("utf-8"),
            add_bos=True,
            special=True,
        )

        # Build embedding prefix: stack prefix vectors into [n_prefix, n_embd]
        if prefix_vectors:
            prefix_np = np.stack(
                [v.detach().cpu().numpy().astype(np.float32) for v in prefix_vectors],
                axis=0,
            )  # [n_prefix, n_embd]
        else:
            prefix_np = np.empty((0, self.n_embd), dtype=np.float32)

        n_prefix = prefix_np.shape[0]

        # --- Inject prefix via llama_batch in embedding mode ---
        # We evaluate the prefix embeddings first, building KV cache entries
        # for those positions before evaluating the prompt tokens.
        if n_prefix > 0:
            self._eval_embeddings(prefix_np)

        # Then evaluate the real prompt tokens (continuing from KV cache)
        self._llm.eval(prompt_tokens)

        # Sample tokens
        output_tokens = []
        while len(output_tokens) < max_tokens:
            token_id = self._llm.sample(
                top_p=top_p,
                temp=temperature,
                repeat_penalty=repeat_penalty,
                mirostat_mode=0,
            )
            if token_id == self._llm.token_eos():
                break
            output_tokens.append(token_id)
            self._llm.eval([token_id])

        # Reset KV cache for next call
        self._llm.reset()

        return self._llm.detokenize(output_tokens).decode("utf-8", errors="replace")

    def _eval_embeddings(self, embeddings: np.ndarray):
        """
        Evaluate raw float embeddings through the model using the llama_batch
        embedding API (embd != NULL mode).

        This writes KV cache entries for the prefix positions without treating
        the embeddings as token IDs.

        Args:
            embeddings : float32 array [n_prefix, n_embd]
        """
        n_prefix = embeddings.shape[0]
        ctx = self._llm._ctx

        # Build a llama_batch with embeddings mode
        batch = llama_cpp.llama_batch_init(n_prefix, self.n_embd, 1)
        try:
            batch.n_tokens = n_prefix
            flat = embeddings.flatten()
            for i, val in enumerate(flat):
                batch.embd[i] = val
            for i in range(n_prefix):
                batch.pos[i] = i
                batch.n_seq_id[i] = 1
                batch.seq_id[i][0] = 0
                batch.logits[i] = False  # don't sample prefix positions

            ret = llama_cpp.llama_decode(ctx, batch)
            if ret != 0:
                raise RuntimeError(
                    f"llama_decode returned {ret} during soft-prefix injection; "
                    "refusing to continue as if Rosetta ran."
                )
        finally:
            llama_cpp.llama_batch_free(batch)

    def generate(
        self,
        prompt: str,
        source_hidden: torch.Tensor | None = None,
        source_family: str | None = None,
        max_tokens: int = 512,
        temperature: float = 0.2,
    ) -> str:
        """
        High-level convenience method:
            1. Project source hidden state through RosettaStone (if provided)
            2. Inject as soft prefix
            3. Generate and return text

        If source_hidden is None, generates without any prefix (standard mode).
        """
        prefix_vectors = []
        if source_hidden is not None and source_family is not None:
            projected = self.project(source_hidden, source_family)
            prefix_vectors = [projected]
            print(
                f"[RosettaBridge] Prefix injected: "
                f"{source_family}→{self.target_family}  "
                f"dim={projected.shape[0]}",
                flush=True,
            )

        return self.generate_with_prefix(
            prompt=prompt,
            prefix_vectors=prefix_vectors,
            max_tokens=max_tokens,
            temperature=temperature,
        )

    def unload(self):
        """Free GGUF model from VRAM."""
        if self._llm is not None:
            del self._llm
            self._llm = None
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            print("[RosettaBridge] GGUF unloaded. VRAM cleared.", flush=True)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.unload()


# ---------------------------------------------------------------------------
# A/B EVALUATOR — validates Rosetta prefix vs. no-prefix compile rate
# ---------------------------------------------------------------------------


class RosettaABEvaluator:
    """
    Runs a paired A/B evaluation comparing:
        A: standard generation (no soft prefix)
        B: Rosetta-prefix generation (with projected latent state)

    Measures compile-pass rate delta to validate the Rosetta Stone improves
    generation quality for code tasks.

    Used by rosetta_vs_text_eval.py for benchmark reporting.
    """

    def __init__(
        self,
        bridge: RosettaInferenceBridge,
        compiler: callable,  # fn(code: str) -> bool
    ):
        self.bridge = bridge
        self.compiler = compiler

    def run(
        self,
        prompts: list[str],
        source_hiddens: list[torch.Tensor],
        source_family: str,
        max_tokens: int = 512,
    ) -> dict:
        """
        Run A/B evaluation on a list of prompts.

        Returns:
            {
                "n_prompts": int,
                "baseline_pass": int,
                "rosetta_pass": int,
                "baseline_rate": float,
                "rosetta_rate": float,
                "delta": float,
            }
        """
        baseline_pass = 0
        rosetta_pass = 0

        for i, (prompt, hidden) in enumerate(zip(prompts, source_hiddens)):
            # A: no prefix
            output_a = self.bridge.generate(prompt, max_tokens=max_tokens)
            if self.compiler(output_a):
                baseline_pass += 1

            # B: with Rosetta prefix
            output_b = self.bridge.generate(
                prompt,
                source_hidden=hidden,
                source_family=source_family,
                max_tokens=max_tokens,
            )
            if self.compiler(output_b):
                rosetta_pass += 1

            print(
                f"[A/B] {i + 1}/{len(prompts)}  "
                f"baseline={'PASS' if self.compiler(output_a) else 'FAIL'}  "
                f"rosetta={'PASS' if self.compiler(output_b) else 'FAIL'}",
                flush=True,
            )

        n = len(prompts)
        return {
            "n_prompts": n,
            "baseline_pass": baseline_pass,
            "rosetta_pass": rosetta_pass,
            "baseline_rate": baseline_pass / n if n > 0 else 0.0,
            "rosetta_rate": rosetta_pass / n if n > 0 else 0.0,
            "delta": (rosetta_pass - baseline_pass) / n if n > 0 else 0.0,
        }


# ---------------------------------------------------------------------------
# SELF-TEST (no GGUF required — validates projection math)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("[RosettaBridge] Running projection self-test (no GGUF required)...", flush=True)

    import tempfile
    from pathlib import Path as P

    # Create a minimal RosettaStone and save it
    stone = RosettaStone()
    with tempfile.TemporaryDirectory() as tmpdir:
        stone.save(P(tmpdir) / "test")
        loaded = RosettaStone.load(P(tmpdir) / "test")

    # Test projection: mistral (4096) → qwen (2048)
    source_hidden = torch.randn(4096)
    with torch.no_grad():
        projected = loaded.translate("mistral", "qwen", source_hidden.unsqueeze(0))
    projected = projected.squeeze(0)

    assert projected.shape == (2048,), f"Expected (2048,), got {projected.shape}"

    # Verify it's not NaN/Inf
    assert not torch.isnan(projected).any(), "Projection contains NaN"
    assert not torch.isinf(projected).any(), "Projection contains Inf"

    cos_sim = torch.nn.functional.cosine_similarity(
        source_hidden[:2048].unsqueeze(0),
        projected.unsqueeze(0),
    ).item()

    print(
        f"  mistral(4096) → qwen(2048): shape={tuple(projected.shape)}  cos_sim_check={cos_sim:.4f}"
    )
    print(f"  norm: {projected.norm().item():.4f}")

    # Test multi-prefix stacking
    prefix_tensors = [torch.randn(2048), torch.randn(2048)]
    prefix_np = np.stack([v.numpy().astype(np.float32) for v in prefix_tensors], axis=0)
    assert prefix_np.shape == (2, 2048), f"Unexpected prefix shape: {prefix_np.shape}"
    print(f"  Prefix stack: {prefix_np.shape}  ✓")

    print("[RosettaBridge] Projection self-test passed.", flush=True)
