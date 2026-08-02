"""
rosetta/extract_midlayer.py — Mid-Layer Hidden State Extractor for Flow AI

Uses HuggingFace forward hooks to capture hidden states at layer N//2
of a transformer model. This is the "understanding" layer — where semantic
representations have formed but haven't been projected back to logit space.

Key design decisions:
    - Operates on HuggingFace models (NOT GGUF). llama-cpp-python does not
      expose mid-layer internals. The HF model is loaded, used for extraction,
      then deleted to free VRAM before the small GGUF model runs.
    - Mean-pools the [seq_len, hidden_dim] mid-layer output to [hidden_dim]
      matching the format used by collect_hidden_states.py and train_rosetta.py.
    - 4-bit NF4 quantization (same as collect_hidden_states.py) to minimize
      VRAM. A 7B model in 4-bit uses ~4-5GB VRAM.

Usage:
    extractor = MidLayerExtractor("mistralai/Mistral-7B-Instruct-v0.3")
    state = extractor.extract("The full context text goes here...")
    # state: torch.Tensor [hidden_dim], dtype=float32
    extractor.unload()  # free VRAM before loading GGUF
"""

import gc
import sys
from pathlib import Path

import torch

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

try:
    from kv_compress import mean_pool
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from kv_compress import mean_pool


# ---------------------------------------------------------------------------
# FAMILY CONFIGS
# Must match FAMILIES in collect_hidden_states.py and FAMILY_DIMS in train_rosetta.py
# ---------------------------------------------------------------------------

FAMILY_CONFIGS = {
    "llama": {
        "model_id": "meta-llama/Llama-3.2-3B-Instruct",
        "hidden_dim": 3072,
        "layer_attr": "model.layers",
    },
    "mistral": {
        "model_id": "mistralai/Mistral-7B-Instruct-v0.3",
        "hidden_dim": 4096,
        "layer_attr": "model.layers",
    },
    "qwen": {
        "model_id": "Qwen/Qwen2.5-Coder-3B-Instruct",
        "hidden_dim": 2048,
        "layer_attr": "model.layers",
    },
    "deepseek": {
        "model_id": "deepseek-ai/deepseek-coder-1.3b-instruct",
        "hidden_dim": 2048,
        "layer_attr": "model.layers",
    },
    "phi": {
        "model_id": "microsoft/Phi-3-mini-4k-instruct",
        "hidden_dim": 3072,
        "layer_attr": "model.layers",
    },
    "gemma": {
        "model_id": "google/gemma-2-2b-it",
        "hidden_dim": 2304,
        "layer_attr": "model.layers",
    },
}


def _get_layer_list(model, layer_attr: str):
    """Navigate dotted attribute path to the transformer layers list."""
    obj = model
    for part in layer_attr.split("."):
        obj = getattr(obj, part)
    return obj


# ---------------------------------------------------------------------------
# EXTRACTOR
# ---------------------------------------------------------------------------


class MidLayerExtractor:
    """
    Loads a HuggingFace model and extracts mid-layer hidden states via
    forward hooks, without modifying the model's forward pass.

    The hook is registered on layer[N//2] of the transformer stack.
    It captures the primary hidden state output (output[0]) which is the
    residual stream at that layer — the same tensor that each subsequent
    attention block will read and write.
    """

    def __init__(
        self,
        family: str,
        model_id: str | None = None,
        load_in_4bit: bool = True,
        device: str | None = None,
    ):
        """
        Args:
            family      : model family key (e.g. "mistral", "llama")
            model_id    : HuggingFace model ID. Defaults to FAMILY_CONFIGS[family].
            load_in_4bit: use bitsandbytes 4-bit quantization to save VRAM.
            device      : "cuda" or "cpu". Auto-detected if None.
        """
        if family not in FAMILY_CONFIGS:
            raise ValueError(f"Unknown family '{family}'. Available: {list(FAMILY_CONFIGS)}")

        cfg = FAMILY_CONFIGS[family]
        self.family = family
        self.model_id = model_id or cfg["model_id"]
        self.hidden_dim = cfg["hidden_dim"]
        self.layer_attr = cfg["layer_attr"]
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self._model = None
        self._tok = None
        self._hook = None
        self._captured = {}

        self._load(load_in_4bit)

    def _load(self, load_in_4bit: bool):
        from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

        print(f"[Extractor] Loading {self.family} ({self.model_id})...", flush=True)

        tok = AutoTokenizer.from_pretrained(self.model_id, trust_remote_code=True)
        if tok.pad_token is None:
            tok.pad_token = tok.eos_token

        bnb = None
        if load_in_4bit and self.device == "cuda":
            bnb = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_quant_type="nf4",
            )

        model = AutoModelForCausalLM.from_pretrained(
            self.model_id,
            quantization_config=bnb,
            device_map="auto" if self.device == "cuda" else None,
            output_hidden_states=True,
            trust_remote_code=True,
            torch_dtype=torch.float16 if (not bnb and self.device == "cuda") else None,
        )
        if self.device == "cpu":
            model = model.to("cpu")
        model.eval()

        # Determine mid-layer index and register hook
        layers = _get_layer_list(model, self.layer_attr)
        n_layers = len(layers)
        mid_idx = n_layers // 2
        self._mid_idx = mid_idx

        captured = self._captured

        def _hook_fn(module, input, output):
            # output[0] is the hidden state tensor [batch, seq_len, hidden_dim]
            h = output[0] if isinstance(output, (tuple, list)) else output
            # Store on CPU immediately to avoid holding GPU memory
            captured["mid"] = h.detach().float().cpu()

        self._hook = layers[mid_idx].register_forward_hook(_hook_fn)

        self._model = model
        self._tok = tok

        n_params = sum(p.numel() for p in model.parameters())
        print(
            f"[Extractor] Ready. Layers={n_layers}, mid_layer={mid_idx}, "
            f"hidden_dim={self.hidden_dim}, params={n_params:,}",
            flush=True,
        )

    def extract(
        self,
        context_text: str,
        max_length: int = 2048,
    ) -> torch.Tensor:
        """
        Run context through the model and return the mid-layer hidden state.

        Args:
            context_text : the full context to compress (e.g. a code file,
                           a conversation history, a project description)
            max_length   : token limit. Long contexts are truncated.

        Returns:
            float32 tensor [hidden_dim] — mean-pooled mid-layer representation.
            This is the "semantic understanding" of the context.
        """
        if self._model is None:
            raise RuntimeError("Model has been unloaded. Create a new MidLayerExtractor.")

        self._captured.clear()

        inputs = self._tok(
            context_text,
            return_tensors="pt",
            truncation=True,
            max_length=max_length,
        )
        # Move to model device
        device = next(self._model.parameters()).device
        inputs = {k: v.to(device) for k, v in inputs.items()}

        seq_len = inputs["input_ids"].shape[1]

        with torch.no_grad():
            _ = self._model(**inputs)

        if "mid" not in self._captured:
            raise RuntimeError(
                f"Forward hook did not fire. Check layer_attr='{self.layer_attr}' "
                f"and mid_idx={self._mid_idx}."
            )

        mid_hidden = self._captured["mid"]  # [1, seq_len, hidden_dim] on CPU
        pooled = mean_pool(mid_hidden)  # [hidden_dim]

        self._captured.clear()

        print(
            f"[Extractor] Extracted: seq_len={seq_len}, "
            f"state_shape={pooled.shape}, family={self.family}",
            flush=True,
        )
        return pooled

    def extract_batch(
        self,
        texts: list[str],
        max_length: int = 512,
    ) -> list[torch.Tensor]:
        """
        Extract mid-layer states for a list of texts (sequential, not batched).
        Batching would require padding and complicate pooling — sequential is fine.
        """
        results = []
        for i, text in enumerate(texts):
            state = self.extract(text, max_length=max_length)
            results.append(state)
            if (i + 1) % 5 == 0:
                print(f"[Extractor] {i + 1}/{len(texts)} extracted", flush=True)
        return results

    def get_layer_info(self) -> dict:
        """Return metadata about extraction configuration."""
        return {
            "family": self.family,
            "model_id": self.model_id,
            "hidden_dim": self.hidden_dim,
            "mid_idx": self._mid_idx,
            "device": str(self.device),
        }

    def unload(self):
        """
        Remove the forward hook and delete the model to free VRAM.
        Call this before loading the GGUF inference model.
        """
        if self._hook is not None:
            self._hook.remove()
            self._hook = None
        if self._model is not None:
            del self._model
            self._model = None
        if self._tok is not None:
            del self._tok
            self._tok = None
        self._captured.clear()
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
        print(f"[Extractor] {self.family} unloaded. VRAM cleared.", flush=True)

    def __del__(self):
        try:
            self.unload()
        except Exception:
            pass

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.unload()


# ---------------------------------------------------------------------------
# COLLECT MID-LAYER STATES (for training RosettaMidLayer)
# Mirrors the collection loop from collect_hidden_states.py but for mid-layer
# ---------------------------------------------------------------------------


def collect_midlayer_states(
    output_dir: Path,
    prompts: list[str],
    families: list[str] | None = None,
):
    """
    Run the shared prompt set through each model family and save mid-layer states.
    Output structure: output_dir/{family}/prompt_NNNN.pt

    This produces training data for train_rosetta.py --mode midlayer.
    """
    output_dir = Path(output_dir)
    target_families = families or list(FAMILY_CONFIGS.keys())
    results = {}

    for family in target_families:
        fam_dir = output_dir / family
        fam_dir.mkdir(parents=True, exist_ok=True)

        existing = sorted(fam_dir.glob("*.pt"))
        if len(existing) >= len(prompts) * 0.9:
            print(
                f"[Collect] {family}: already collected ({len(existing)} files), skipping.",
                flush=True,
            )
            results[family] = len(existing)
            continue

        print(f"\n[Collect] ── {family.upper()} ──", flush=True)
        try:
            with MidLayerExtractor(family) as extractor:
                saved = 0
                for i, prompt in enumerate(prompts):
                    try:
                        state = extractor.extract(prompt, max_length=256)
                        torch.save(state, fam_dir / f"prompt_{i:04d}.pt")
                        saved += 1
                    except Exception as e:
                        print(f"[Collect] {family} prompt {i} failed: {e}", flush=True)
                results[family] = saved
                print(
                    f"[Collect] {family}: saved {saved}/{len(prompts)} states → {fam_dir}",
                    flush=True,
                )
        except Exception as e:
            print(f"[Collect] ERROR loading {family}: {e}", flush=True)
            results[family] = 0

    summary = {"prompts": len(prompts), "families": results, "mode": "midlayer"}
    (output_dir / "midlayer_collection_summary.json").write_text(
        __import__("json").dumps(summary, indent=2)
    )
    print(f"\n[Collect] Complete: {results}", flush=True)
    return results


# ---------------------------------------------------------------------------
# SELF-TEST (no model load — just hook logic with a tiny synthetic model)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("[Extractor] Self-test: hook + mean_pool on synthetic model...", flush=True)

    import torch.nn as nn

    class TinyTransformerLayer(nn.Module):
        def __init__(self, dim):
            super().__init__()
            self.ff = nn.Linear(dim, dim)

        def forward(self, x):
            return (self.ff(x),)  # return tuple like real transformer

    class TinyModel(nn.Module):
        def __init__(self, dim=64, n_layers=4):
            super().__init__()
            self.layers = nn.ModuleList([TinyTransformerLayer(dim) for _ in range(n_layers)])

        def forward(self, x):
            for layer in self.layers:
                x = layer(x)[0]
            return x

    dim = 64
    n_layers = 4
    mid_idx = n_layers // 2

    model = TinyModel(dim, n_layers)
    captured = {}

    def hook_fn(module, input, output):
        h = output[0] if isinstance(output, (tuple, list)) else output
        captured["mid"] = h.detach().float().cpu()

    hook = model.layers[mid_idx].register_forward_hook(hook_fn)

    x = torch.randn(1, 10, dim)  # batch=1, seq=10, dim=64
    _ = model(x)

    assert "mid" in captured, "Hook did not fire"
    mid = captured["mid"]
    pooled = mean_pool(mid)
    assert pooled.shape == (dim,), f"Expected ({dim},), got {pooled.shape}"
    print(f"  Hook fired: mid.shape={mid.shape}, pooled.shape={pooled.shape}")

    hook.remove()
    print("[Extractor] Self-test passed.", flush=True)
