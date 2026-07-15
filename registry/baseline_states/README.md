# registry/baseline_states/

This directory contains pre-committed hidden state tensors for the Determinex
Rosetta Stone core architectures. These are the training targets that allow
community contributors to add new model families **without downloading or
running the existing six base models.**

## Structure

```
baseline_states/
  llama/
    prompt_0000.pt  ... prompt_0029.pt   (30 tensors, dim=3072)
  qwen/
    prompt_0000.pt  ... prompt_0029.pt   (30 tensors, dim=2048)
  deepseek/
    prompt_0000.pt  ... prompt_0029.pt   (30 tensors, dim=2048)
  mistral/
    prompt_0000.pt  ... prompt_0029.pt   (30 tensors, dim=4096)
  phi/
    prompt_0000.pt  ... prompt_0029.pt   (30 tensors, dim=3072)
  gemma/
    prompt_0000.pt  ... prompt_0029.pt   (30 tensors, dim=2304)
```

## What These Are

Each `.pt` file is a mean-pooled, last-layer hidden state tensor from the
corresponding base model running the shared benchmark prompt set defined in
`rosetta/collect_hidden_states.py:SHARED_PROMPTS`.

They were extracted using:
```
python rosetta/collect_hidden_states.py --layer last --output_dir <this_dir>
```

## Size

~600 KB total. Small enough to version-control directly.

## For Contributors

Copy this directory into your extraction output before training:
```bash
cp -r registry/baseline_states/* outputs/hidden_states/
```

Then run `train_rosetta.py`. The training script will discover all family
subdirectories automatically and build cross-architecture alignment pairs.

> **Note:** The actual `.pt` files are populated on the first RunPod training
> run and committed to this directory. If you are setting up this repo from
> scratch, run `collect_hidden_states.py --layer last` to generate them.
