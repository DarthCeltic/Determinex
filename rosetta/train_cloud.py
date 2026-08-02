"""
train_cloud.py — Determinex Cloud Fine-Tuning (RTX 4090 optimized)

Fine-tunes all three Determinex personas sequentially in one RunPod session:
    1. Engineer  — Qwen2.5-Coder-3B-Instruct  (code generation)
    2. Observer  — Llama-3.2-3B-Instruct       (hallucination detection)
    3. Sentinel  — Mistral-7B-Instruct-v0.3    (planning + decomposition)

RTX 4090 advantages over local 6 GB GPU (Tier 0):
    - 24GB VRAM vs 6GB  → batch_size=4 (4x larger effective batch)
    - ~15x faster per step
    - No Windows display compositor throttle needed
    - All three models train in ~3 hours total vs 54 hours local

Usage:
    python rosetta/train_cloud.py --model engineer
    python rosetta/train_cloud.py --model observer
    python rosetta/train_cloud.py --model sentinel
    python rosetta/train_cloud.py --model all
"""

import argparse
import gc
import sys
import time
from pathlib import Path

import torch
from datasets import concatenate_datasets, load_dataset
from peft import LoraConfig, TaskType, get_peft_model
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from trl import SFTTrainer

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# HuggingFace auth — reads HF_TOKEN env var, works without CLI login
_hf_token = os.environ.get("HF_TOKEN", "")
if _hf_token:
    from huggingface_hub import login as _hf_login

    _hf_login(token=_hf_token, add_to_git_credential=False)
    print("[CLOUD] HuggingFace login OK", flush=True)
else:
    print("[CLOUD] WARNING: HF_TOKEN not set — gated models will fail", flush=True)

# ---------------------------------------------------------------------------
# PERSONA CONFIGS
# ---------------------------------------------------------------------------

PERSONAS = {
    "engineer": {
        "base_model": "Qwen/Qwen2.5-Coder-3B-Instruct",
        "output_name": "determinex-engineer-v9",
        "lora_r": 32,
        "lora_alpha": 64,
        "epochs": 3,
        "batch_size": 4,
        "grad_accum": 4,
        "system_prompt": (
            "You are Engineer, Determinex's code generation specialist. "
            "You write correct, idiomatic, compiler-verified code. "
            "Output ONLY the requested function or code block. "
            "No explanations. No prose. No markdown fences unless asked. "
            "The compiler is your judge — if it doesn't compile, it's wrong."
        ),
    },
    "observer": {
        "base_model": "meta-llama/Llama-3.2-3B-Instruct",
        "output_name": "determinex-observer-v4",
        "lora_r": 16,
        "lora_alpha": 32,
        "epochs": 3,
        "batch_size": 4,
        "grad_accum": 4,
        "system_prompt": (
            "You are Observer, Determinex's hallucination detection specialist. "
            "You review code and responses for correctness, logical errors, and hallucinations. "
            "Output ONLY valid JSON in this exact format: "
            '{"verdict": "CLEAN"|"HALLUCINATION", "issues": [...], "confidence": 0.0-1.0}'
        ),
    },
    "sentinel": {
        "base_model": "mistralai/Mistral-7B-Instruct-v0.3",
        "output_name": "determinex-sentinel-v3",
        "lora_r": 16,
        "lora_alpha": 32,
        "epochs": 3,
        "batch_size": 2,
        "grad_accum": 8,
        "system_prompt": (
            "You are Sentinel, Determinex's planning and decomposition specialist. "
            "You take user requests and produce structured execution plans. "
            "Output ONLY valid JSON: "
            '{"tasks": [...], "language": "...", "complexity": "low|medium|high", "safe": true|false}'
        ),
    },
}

# ---------------------------------------------------------------------------
# DATA PATHS — clean corpus only (no tainted v8 gap curriculum)
# ---------------------------------------------------------------------------

DATA_FILES = [
    "data/determinex_v1_distilled_claude.jsonl",
    "data/determinex_v1_distilled_gemini.jsonl",
    "data/determinex_v1_distilled_observer.jsonl",
    "data/determinex_v1_targeted_gaps.jsonl",
]

MAX_SEQ_LENGTH = 2048


# ---------------------------------------------------------------------------
# FORMAT
# ---------------------------------------------------------------------------


def format_sample(sample: dict, system_prompt: str) -> str:
    sys_p = sample.get("system", system_prompt)
    user_p = sample.get("user", sample.get("instruction", ""))
    asst_p = sample.get("assistant", sample.get("output", ""))
    return (
        f"<|begin_of_text|>"
        f"<|start_header_id|>system<|end_header_id|>\n\n{sys_p}<|eot_id|>"
        f"<|start_header_id|>user<|end_header_id|>\n\n{user_p}<|eot_id|>"
        f"<|start_header_id|>assistant<|end_header_id|>\n\n{asst_p}<|eot_id|>"
    )


# ---------------------------------------------------------------------------
# TRAIN ONE PERSONA
# ---------------------------------------------------------------------------


def train_persona(name: str, cfg: dict, output_root: Path):
    print(f"\n{'=' * 60}", flush=True)
    print(f"[CLOUD] Training {name.upper()} — {cfg['base_model']}", flush=True)
    print(f"{'=' * 60}\n", flush=True)

    output_dir = output_root / cfg["output_name"]
    output_dir.mkdir(parents=True, exist_ok=True)

    # ── Load data ──────────────────────────────────────────────────────────
    available = [Path(p) for p in DATA_FILES if Path(p).exists()]
    if not available:
        print("[CLOUD] ERROR: No data files found. Expected in ./data/", flush=True)
        return False
    print(f"[CLOUD] Data files: {[p.name for p in available]}", flush=True)

    raw_datasets = [load_dataset("json", data_files=str(p), split="train") for p in available]
    dataset = concatenate_datasets(raw_datasets) if len(raw_datasets) > 1 else raw_datasets[0]
    print(f"[CLOUD] Samples loaded: {len(dataset)}", flush=True)

    # Alpaca mix — 20% general to prevent catastrophic forgetting
    general_target = int(len(dataset) * 0.25)
    try:
        alpaca = load_dataset("yahma/alpaca-cleaned", split=f"train[:{general_target}]")

        def remap(ex):
            u = ex["instruction"] + ("\n\n" + ex["input"] if ex.get("input", "").strip() else "")
            return {
                "system": "You are a helpful AI assistant.",
                "user": u,
                "assistant": ex.get("output", ""),
            }

        alpaca = alpaca.map(remap).select_columns(["system", "user", "assistant"])
        dataset = concatenate_datasets([dataset, alpaca])
        print(f"[CLOUD] +{len(alpaca)} Alpaca samples. Total: {len(dataset)}", flush=True)
    except Exception as e:
        print(f"[CLOUD] Alpaca mix failed ({e}), continuing without.", flush=True)

    # ── Load model ─────────────────────────────────────────────────────────
    bnb = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
    )
    print("[CLOUD] Loading base model...", flush=True)
    tok = AutoTokenizer.from_pretrained(cfg["base_model"], trust_remote_code=True)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    tok.padding_side = "right"

    model = AutoModelForCausalLM.from_pretrained(
        cfg["base_model"],
        quantization_config=bnb,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=torch.float16,
    )
    model.gradient_checkpointing_enable()

    # ── LoRA ───────────────────────────────────────────────────────────────
    lora = LoraConfig(
        r=cfg["lora_r"],
        lora_alpha=cfg["lora_alpha"],
        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            "gate_proj",
            "up_proj",
            "down_proj",
        ],
        lora_dropout=0.05,
        bias="none",
        task_type=TaskType.CAUSAL_LM,
    )
    model = get_peft_model(model, lora)
    model.enable_input_require_grads()  # required for 4-bit + gradient checkpointing
    model.print_trainable_parameters()

    # ── Format dataset ─────────────────────────────────────────────────────
    system_prompt = cfg["system_prompt"]

    def fmt(batch):
        return {
            "text": [
                format_sample(s, system_prompt)
                for s in [{k: batch[k][i] for k in batch} for i in range(len(batch["user"]))]
            ]
        }

    dataset = dataset.map(fmt, batched=True, remove_columns=dataset.column_names)

    # ── Training args ──────────────────────────────────────────────────────
    training_args = TrainingArguments(
        output_dir=str(output_dir / "checkpoints"),
        num_train_epochs=cfg["epochs"],
        per_device_train_batch_size=cfg["batch_size"],
        gradient_accumulation_steps=cfg["grad_accum"],
        learning_rate=2e-4,
        lr_scheduler_type="cosine",
        warmup_ratio=0.05,
        fp16=True,
        logging_steps=10,
        save_strategy="epoch",
        optim="paged_adamw_32bit",
        report_to="none",
        dataloader_num_workers=4,
    )

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        tokenizer=tok,
        max_seq_length=MAX_SEQ_LENGTH,
        dataset_text_field="text",
    )

    print("[CLOUD] Beginning training...", flush=True)
    start = time.time()
    trainer.train()
    elapsed = (time.time() - start) / 60
    print(f"[CLOUD] Training complete in {elapsed:.1f} minutes.", flush=True)

    # ── Merge + export ─────────────────────────────────────────────────────
    print("[CLOUD] Merging LoRA adapter...", flush=True)
    merged_dir = output_dir / "merged"
    merged_dir.mkdir(exist_ok=True)
    merged = model.merge_and_unload()
    # Cast to float16 — bitsandbytes 4-bit merged weights must be dequantized
    # before llama.cpp can convert. save_pretrained with torch_dtype ensures
    # the safetensors file contains float16 tensors, not quantized bnb format.
    merged = merged.to(torch.float16)
    merged.save_pretrained(str(merged_dir), safe_serialization=True)
    tok.save_pretrained(str(merged_dir))
    print(f"[CLOUD] Merged model saved → {merged_dir}", flush=True)

    # ── GGUF conversion ────────────────────────────────────────────────────
    gguf_path = output_dir / f"{cfg['output_name']}.gguf"
    llama_cpp = Path("/workspace/llama.cpp")
    if llama_cpp.exists():
        print("[CLOUD] Converting to GGUF...", flush=True)
        import subprocess

        result = subprocess.run(
            [
                "python3",
                str(llama_cpp / "convert_hf_to_gguf.py"),
                str(merged_dir),
                "--outfile",
                str(gguf_path),
                "--outtype",
                "q8_0",
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            size_gb = gguf_path.stat().st_size / 1e9
            print(f"[CLOUD] GGUF exported: {gguf_path} ({size_gb:.1f}GB)", flush=True)
        else:
            print(f"[CLOUD] GGUF conversion failed: {result.stderr[-500:]}", flush=True)
    else:
        print(
            "[CLOUD] llama.cpp not found — merged HF model saved. Will convert locally.", flush=True
        )

    # Cleanup VRAM
    del model, merged, trainer
    gc.collect()
    torch.cuda.empty_cache()
    print("[CLOUD] VRAM cleared for next model.", flush=True)
    return True


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model", choices=["engineer", "observer", "sentinel", "all"], default="all"
    )
    parser.add_argument("--output_dir", type=str, default="/workspace/outputs")
    args = parser.parse_args()

    output_root = Path(args.output_dir)
    targets = list(PERSONAS.keys()) if args.model == "all" else [args.model]

    results = {}
    for name in targets:
        ok = train_persona(name, PERSONAS[name], output_root)
        results[name] = "OK" if ok else "FAILED"
        print(f"\n[CLOUD] {name}: {results[name]}\n", flush=True)

    print(f"\n[CLOUD] All done: {results}", flush=True)
    print(f"[CLOUD] Outputs in: {output_root}", flush=True)
