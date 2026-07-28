# Determinex — RunPod Retrain Handoff
**Date**: 2026-04-13  
**For**: Sonnet or Opus in Antigravity (or any Claude session with SSH access to RunPod)  
**Pod**: `root@<POD_IP>` port `<PORT>`, SSH key `~/.ssh/id_runpod`

---

## Context: What Determinex Is

Determinex is a local-first AI coding assistant — Tauri app, Ollama backend, three fine-tuned personas:
- **Engineer** (Qwen2.5-Coder-1.5B LoRA) — code generation
- **Observer** (Llama 3.2 3B LoRA) — hallucination detection + critique  
- **Sentinel** (Mistral 7B LoRA) — planning, decomposition, safety gating

All training uses compiler-verified ground truth (`rustc`, `go build`, `python`) — no LLM judges.

**Current system SWE score** (before this session's retrains):
- Engineer v10: 84% (38/45)
- Observer v4:  78% (35/45)
- Sentinel v3:  87% (39/45)
- **System combined: 83% (112/135)**

---

## Current Pod State (verified)

SSH into pod to confirm before starting:

```bash
ssh -p <PORT> -i ~/.ssh/id_runpod root@<POD_IP>
```

Files already on pod:
```
/workspace/fix_retrain_observer.py    — Observer v5 retrain script (Llama 3.2 3B)
/workspace/fix_retrain_sentinel.py    — Sentinel v4 retrain script (Mistral 7B)
/workspace/data/gap_v3_arc_mutex.jsonl        — 12 arc_mutex examples (all 3 models need this)
/workspace/data/gap_v3_go_panic.jsonl         — 12 go_panic_recover examples
/workspace/data/gap_v4_observer_specific.jsonl — 14 Observer-specific gap examples
/workspace/data/gap_v4_sentinel_specific.jsonl —  4 Sentinel-specific gap examples
/workspace/outputs/determinex-engineer-v9/determinex-engineer-v9.gguf — Engineer v10 GGUF (already done)
```

---

## Your Tasks (in order)

### TASK 1: Run Observer retrain

Observer gaps: arc_mutex 0%, refcell rename P5, first_even negatives P5, go_panic fmt GP2, fez P3/P4.

All gap data is already in `/workspace/data/` — the retrain script reads all `*.jsonl` there.

```bash
ssh -p <PORT> -i ~/.ssh/id_runpod root@<POD_IP> \
  "cd /workspace && python3 fix_retrain_observer.py 2>&1 | tee obs_retrain.log"
```

Watch for `STAGE[N/6]` markers. Should complete in 20–40 min.

On success, output GGUF is at: `/workspace/outputs/determinex-observer-v4/determinex-observer-v4.gguf`

### TASK 2: Download Observer GGUF

```bash
scp -P <PORT> -i ~/.ssh/id_runpod \
  root@<POD_IP>:/workspace/outputs/determinex-observer-v4/determinex-observer-v4.gguf \
  "${DETERMINEX_MODELS_DIR:-~/determinex-models}/determinex-observer-v4.gguf"
```

### TASK 2.5: Clean disk before Sentinel retrain

Root overlay is 50GB. Llama 3.2 (Observer base, ~6GB) will be in `~/.cache` after Observer retrain. Mistral 7B (Sentinel base, ~14GB) needs to download there too. Clear the Llama cache first:

```bash
ssh -p <PORT> -i ~/.ssh/id_runpod root@<POD_IP> \
  "rm -rf ~/.cache/huggingface/hub/models--meta-llama--Llama-3.2-3B-Instruct && df -h /"
```

Also clear any stale Qwen cache (Engineer is done, no longer needed):
```bash
ssh -p <PORT> -i ~/.ssh/id_runpod root@<POD_IP> \
  "rm -rf ~/.cache/huggingface/hub/models--Qwen* && df -h /"
```

After cleanup, root should have ~27GB+ free — plenty for Mistral's 14GB download.

The Sentinel retrain script writes adapter + merged model to `/workspace` (network fs, 276TB free) rather than `/tmp`, so the merge stage won't stress root disk.

### TASK 3: Run Sentinel retrain

Sentinel gaps: arc_mutex 0%, refcell rename P5. Smallest gap set of all three.

```bash
ssh -p <PORT> -i ~/.ssh/id_runpod root@<POD_IP> \
  "cd /workspace && python3 fix_retrain_sentinel.py 2>&1 | tee sen_retrain.log"
```

On success, output GGUF is at: `/workspace/outputs/determinex-sentinel-v3/determinex-sentinel-v3.gguf`

### TASK 4: Download Sentinel GGUF

```bash
scp -P <PORT> -i ~/.ssh/id_runpod \
  root@<POD_IP>:/workspace/outputs/determinex-sentinel-v3/determinex-sentinel-v3.gguf \
  "${DETERMINEX_MODELS_DIR:-~/determinex-models}/determinex-sentinel-v3.gguf"
```

### TASK 5: Reload all three models into Ollama

Engineer (GGUF already on T:/ — just reload it):
```bash
ollama rm determinex-engineer-v9 2>/dev/null; ollama create determinex-engineer-v9 -f ${DETERMINEX_MODELS_DIR:-~/determinex-models}/Modelfile.engineer
```

Observer (after download completes):
```bash
ollama rm determinex-observer-v4 2>/dev/null; ollama create determinex-observer-v4 -f ${DETERMINEX_MODELS_DIR:-~/determinex-models}/Modelfile.observer
```

Sentinel (after download completes):
```bash
ollama rm determinex-sentinel-v3 2>/dev/null; ollama create determinex-sentinel-v3 -f ${DETERMINEX_MODELS_DIR:-~/determinex-models}/Modelfile.sentinel
```

Verify all three are loaded:
```bash
ollama list
```

### TASK 6: Run full 3-model eval

Working directory: `C:\Dev\Determinex`

```bash
# Run sequentially — parallel kills Ollama VRAM
python scripts/micro_eval.py --model determinex-engineer-v9 --save-baseline 2>&1 | tee eval_engineer_v10.txt
python scripts/micro_eval.py --model determinex-observer-v4 2>&1 | tee eval_observer_v5.txt
python scripts/micro_eval.py --model determinex-sentinel-v3 2>&1 | tee eval_sentinel_v4.txt
```

> Note: `--model` flag takes the Ollama model name, not the file path.  
> IMPORTANT: Run sequentially — do NOT run in parallel. Ollama unloads one model to load another when two compete for 6GB VRAM.

### TASK 7: Update docs with real post-retrain numbers

After eval completes, update these three files in `C:\Dev\Determinex\`:

**`DETERMINEX_MASTER_PLAN.md`** — Update the "Empirical Benchmark History" table:
- Replace the "System (target post-retrain)" row with actual numbers
- Update "Current Model State" table with new versions (Engineer v10 → confirmed, Observer v5, Sentinel v4)

**`WHITE_PAPER_SECTION4_DRAFT.md`** — Update Section 4.5 benchmark tables with post-retrain scores

**`SPRINT.md`** (if it exists) — Mark retrain tasks complete, add new scores

Add a row to the benchmark history for each model:
```
| Engineer v10 | 2026-04-13 | [actual]% ([n]/45) | — | 672 | Post arc_mutex + go_panic gap curriculum |
| Observer v5  | 2026-04-14 | [actual]% ([n]/45) | — | ~[n] | Post arc_mutex + Observer-specific gaps |
| Sentinel v4  | 2026-04-14 | [actual]% ([n]/45) | — | ~[n] | Post arc_mutex + refcell rename gap |
| System combined | 2026-04-14 | [actual]% ([n]/135) | — | — | Post-retrain all 3 models |
```

---

## If Observer retrain OOMs (memory overflow)

The Llama 3.2 3B model is ~6GB fp16. If the pod's GPU can't fit it with LoRA overhead:

```python
# In fix_retrain_observer.py, replace the AutoModelForCausalLM.from_pretrained block with:
from transformers import BitsAndBytesConfig
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
)
model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
)
# And add prepare_model_for_kbit_training:
from peft import prepare_model_for_kbit_training
model = prepare_model_for_kbit_training(model)
```

Same fix applies to the Sentinel script if it OOMs on the 7B model.

---

## If Sentinel retrain OOMs (memory overflow)

Same BitsAndBytes 4bit swap as above, applied to `fix_retrain_sentinel.py`.

For the merge step with a 4bit model, you'll also need to run the merge on CPU:
```bash
# The merge script handles CPU merge automatically via device_map="cpu"
# This will be slow (~10 min) but works for 7B on CPU
```

---

## Licensing Context (for docs/README updates)

Determinex ships under **MIT License** — permissive, no copyleft, commercial-friendly.

When updating docs, note:
- MIT: anyone can use, modify, and distribute, including commercial products
- No AGPL copyleft — no forced open-sourcing of derivative works
- GitHub Sponsors: supports the project, gets priority issue response

---

## Key File Locations

```
${DETERMINEX_MODELS_DIR:-~/determinex-models}/
  Modelfile.engineer        — Ollama Modelfile for Engineer
  Modelfile.observer        — Ollama Modelfile for Observer  
  Modelfile.sentinel        — Ollama Modelfile for Sentinel
  determinex-engineer-v9.gguf  — Engineer v10 (already downloaded, 1.6 GB)
  determinex-observer-v4.gguf  — Observer (needs replacement after retrain)
  determinex-sentinel-v3.gguf  — Sentinel (needs replacement after retrain)

C:\Dev\Determinex\scripts\
  micro_eval.py                   — Evaluation harness (45 probes, 3 compilers)
  fix_retrain_engineer.py         — Engineer retrain (Qwen2.5-Coder-1.5B)
  fix_retrain_observer.py         — Observer retrain (Llama 3.2 3B)
  fix_retrain_sentinel.py         — Sentinel retrain (Mistral 7B)
  gen_gap_observer_sentinel.py    — Gap curriculum generator for Observer+Sentinel
  gap_v4_observer_specific.jsonl  — 14 Observer gap examples
  gap_v4_sentinel_specific.jsonl  —  4 Sentinel gap examples

C:\Dev\Determinex\
  DETERMINEX_MASTER_PLAN.md     — Master tracker (update after eval)
  WHITE_PAPER_SECTION4_DRAFT.md — White paper Section 4 benchmarks
```

---

## Success Criteria

The session is complete when:
- [ ] Observer v5 GGUF downloaded to ${DETERMINEX_MODELS_DIR:-~/determinex-models}/
- [ ] Sentinel v4 GGUF downloaded to ${DETERMINEX_MODELS_DIR:-~/determinex-models}/
- [ ] All 3 models loaded in Ollama (`ollama list` shows all three)
- [ ] Full 3-model micro_eval completed (3 × 45 probes)
- [ ] Docs updated with post-retrain numbers
- [ ] System combined score documented (goal: ≥127/135, ~94%)
