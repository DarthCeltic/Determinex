"""
collect_hidden_states.py — Determinex Rosetta Stone: Hidden State Collector

Loads each base model family, runs a shared set of prompts through them,
and saves the last hidden state for each prompt. These paired states are
the training signal for the W projection matrices.

Same prompt → different model → different coordinate system → same meaning.
W learns the coordinate transform.

Models collected (95% of open source):
    meta-llama/Llama-3.2-3B-Instruct
    Qwen/Qwen2.5-Coder-3B-Instruct
    deepseek-ai/deepseek-coder-1.3b-instruct
    mistralai/Mistral-7B-Instruct-v0.3
    microsoft/Phi-3-mini-4k-instruct
    google/gemma-2-2b-it

Usage (on RunPod):
    python rosetta/collect_hidden_states.py --output_dir outputs/hidden_states
"""

import argparse
import gc
import json
import sys
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

_REPO_ROOT = str(Path(__file__).resolve().parents[1])
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
from rosetta.shared_prompts import SHARED_PROMPTS  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------------
# MODELS TO COLLECT FROM
# Each entry: (family_name, hf_model_id, hidden_dim)
# ---------------------------------------------------------------------------

FAMILIES = [
    ("llama",    "meta-llama/Llama-3.2-3B-Instruct",           3072),
    ("qwen",     "Qwen/Qwen2.5-Coder-3B-Instruct",             2048),
    ("deepseek", "deepseek-ai/deepseek-coder-1.3b-instruct",   2048),
    ("mistral",  "mistralai/Mistral-7B-Instruct-v0.3",         4096),
    ("phi",      "microsoft/Phi-3-mini-4k-instruct",           3072),
    ("gemma",    "google/gemma-2-2b-it",                       2304),
]

# SHARED_PROMPTS now lives in shared_prompts.py (zero dependencies) so the GGUF-based
# collector (collect_hidden_states_gguf.py) can import the exact same prompt set without
# pulling in torch/transformers/bitsandbytes.

# ---------------------------------------------------------------------------
# COLLECTION
# ---------------------------------------------------------------------------

def load_model(model_id: str, device: str):
    """Load a model in 4-bit NF4 for efficient hidden state extraction."""
    print(f"  Loading {model_id}...", flush=True)
    bnb = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
    )
    tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb,
        device_map="auto",
        output_hidden_states=True,
        trust_remote_code=True,
    )
    model.eval()
    print(f"  Loaded. Parameters: {sum(p.numel() for p in model.parameters()):,}", flush=True)
    return model, tok


def collect_states(model, tok, prompts: list[str], family: str, out_dir: Path):
    """Run prompts through model and save last hidden states."""
    out_dir.mkdir(parents=True, exist_ok=True)
    saved = 0
    with torch.no_grad():
        for i, prompt in enumerate(prompts):
            try:
                inputs = tok(
                    prompt,
                    return_tensors="pt",
                    truncation=True,
                    max_length=256,
                ).to(model.device)
                outputs = model(**inputs, output_hidden_states=True)
                # Last hidden state, mean-pooled across sequence length
                last_hidden = outputs.hidden_states[-1]          # (1, seq, dim)
                pooled      = last_hidden.mean(dim=1).squeeze(0) # (dim,)
                pooled_cpu  = pooled.float().cpu()
                torch.save(pooled_cpu, out_dir / f"prompt_{i:04d}.pt")
                saved += 1
                if (i + 1) % 10 == 0:
                    print(f"    [{family}] {i+1}/{len(prompts)} prompts collected", flush=True)
            except Exception as e:
                print(f"    [{family}] prompt {i} failed: {e}", flush=True)
    print(f"  [{family}] Saved {saved}/{len(prompts)} states → {out_dir}", flush=True)
    return saved


def run_collection(output_dir: Path, families: list = None):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[COLLECT] Device: {device}", flush=True)
    print(f"[COLLECT] Prompts: {len(SHARED_PROMPTS)}", flush=True)

    target_families = families or [f[0] for f in FAMILIES]
    results = {}

    for family, model_id, _ in FAMILIES:
        if family not in target_families:
            continue
        print(f"\n[COLLECT] ── {family.upper()} ({model_id}) ──", flush=True)
        fam_dir = output_dir / family
        if fam_dir.exists() and len(list(fam_dir.glob("*.pt"))) >= len(SHARED_PROMPTS) * 0.9:
            print(f"[COLLECT] {family}: already collected, skipping.", flush=True)
            results[family] = len(list(fam_dir.glob("*.pt")))
            continue
        try:
            model, tok = load_model(model_id, device)
            n = collect_states(model, tok, SHARED_PROMPTS, family, fam_dir)
            results[family] = n
            # Free VRAM before loading next model
            del model, tok
            gc.collect()
            torch.cuda.empty_cache()
            print(f"[COLLECT] {family}: VRAM cleared.", flush=True)
        except Exception as e:
            print(f"[COLLECT] ERROR {family}: {e}", flush=True)
            results[family] = 0

    print(f"\n[COLLECT] Complete: {results}", flush=True)
    (output_dir / "collection_summary.json").write_text(
        json.dumps({"prompts": len(SHARED_PROMPTS), "families": results}, indent=2)
    )
    return results


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", type=str, default="outputs/hidden_states")
    parser.add_argument("--families",   type=str, default=None,
                        help="Comma-separated family names to collect (default: all)")
    args = parser.parse_args()

    families = args.families.split(",") if args.families else None
    run_collection(Path(args.output_dir), families)
