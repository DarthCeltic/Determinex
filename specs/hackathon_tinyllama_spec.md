# Goal: Port TinyLlama to ET-SoC1 Hardware

You are tasked with porting `TinyLlama/TinyLlama-1.1B-Chat-v1.0` to run on the ET-SoC1 board.

## Requirements
1. The source that will run on the board must be placed in `hf-hackathon/ported_models/tinyllama`.
2. Generate the necessary ET-SoC1 ELFs. Avoid CPU fallbacks for key ops.
3. Use hart 0 for matrix/tensor work, hart 1 for packing/pointer math.
4. Ensure 64-byte memory alignment to prevent segmentation faults during tile reads.
5. Create a `artifacts.json` pointing to local cache names.
6. Register the model in `.github/ci/benchmark_config.json`.
7. Write a script `build_tinyllama.sh` to compile it.

## Hardware Reference
* DRAM/main memory: large and slow. Avoid repeated streaming.
* L2/shire-local: cooperation zone. Tile into it.
* L1/minion-local: hot working set. Keep accumulators here.

**Do not attempt a huge loop.** First make a single boundary correct, measure variance, and then iterate.
