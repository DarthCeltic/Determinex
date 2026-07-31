# hf-hackathon Model-Port Campaign — Technical Findings (2026-07-25)

Real, verified technical discoveries from a live session porting models to
`aifoundry-org/hf-hackathon`'s `llama.cpp-et` framework and filing
`most_models_ported` track claims. Captured for reuse in future porting or
CI-debugging sessions — every item below was confirmed against real source,
not inferred.

## 1. The `most_models_ported` claim validator (`model_port_claim.py`)

- Each claim JSON must declare `benchmark_config`, and this field is checked
  **verbatim** against the model's entry in `.github/ci/benchmark_config.json`:
  if that entry has a `"config"` key (a pointer to another JSON file, the
  standard pattern for every `llama_cpp_et` model), the claim's
  `benchmark_config` field must **exactly equal that pointer path** — not the
  top-level `.github/ci/benchmark_config.json` path. Setting it to the
  top-level file is only correct for models with a fully inline config entry
  (no `"config"` key). Mixing this up produces
  `"claim benchmark_config does not match the configured model include"` and
  silently fails every claim using the wrong convention — found this wrong on
  33 of our own already-filed claims, all from the same copy-paste mistake.
- A claim's `identity_id` must **already exist** in
  `data/model-port-identities.json` marked `eligible: true`, with matching
  `canonical_source`, `benchmark_config_sha256`, `validation_contract`, and
  `approved_runner`. This is a maintainer-owned, two-stage process — no
  claim can pass eligibility for an architecture the maintainers haven't
  pre-registered, regardless of claim quality. Check the registry's current
  eligible count before assuming any claim can succeed.
- The harness (`run_llama_server_benchmark.py`) only supports `api: "chat"`
  or `api: "completion"` — **no embedding, rerank, or classification scoring
  mode exists**. Any claim for a BERT-family/embedding/classification model
  (jina-bert, nomic-bert, distilbert, modernbert, etc.) cannot pass right now
  regardless of correctness; this needs harness code added to a CI-protected
  path, not something an individual claim PR can fix.
- `protected_track_change()` flags a PR as violating trust boundaries if it
  touches `.github/workflows/`, `.github/ci/scripts/`, `.github/ci/reference/`,
  or specific `data/*.json` files — but this check only runs if the PR is
  also "targeted" (has files under `claim_root`). A pure docs/proposal PR
  with zero claim files never triggers it, even if it touches
  `.github/ci/reference/` for something unrelated (e.g. proposing draft
  validation contracts).

## 2. GGUF architecture ground truth

Don't infer a model's registered arch string from the C++ enum name
(`LLM_ARCH_OPENAI_MOE`) — pull the literal string from the
`LLM_ARCH_NAMES` table in `llama-arch.cpp` (e.g. `LLM_ARCH_OPENAI_MOE` maps
to the string `"gpt-oss"`, not `"openai-moe"`). Naming a new identity from
the enum name alone risks silently duplicating an architecture already
claimed under its true GGUF string.

## 3. Building the ET Platform SDK for local verification

- `docs/ET_SOC1_QUICKSTART.md` + `.github/ci/scripts/install_et_sdk.sh` are
  real and public-source-buildable (clones `aifoundry-org/et-platform`,
  genuinely open). This gets you the **host-side runtime** (`libetrt.so`,
  `sys_emu` executable, `server`) — confirmed working end to end.
- The sysemu firmware ELFs (`BootromTrampolineToBL2`, `MachineMinion`, etc.)
  are checked into the repo itself at `.github/ci/firmware/esperanto-fw/` —
  no download needed, just copy into `${ET_INSTALL}/lib/esperanto-fw/`.
- The runtime env var the compiled `ggml-et` backend actually reads at
  **runtime** to find the SDK is `ET_TOOLCHAIN` (or `TOOLCHAIN_ROOT`) — not
  `ET_PLATFORM`, which is a build-time/CI-deploy variable used elsewhere.
  Setting the wrong one silently no-ops.
- Building `llama.cpp-et` itself with `-DGGML_ET=ON` requires cmake modules
  that have drifted between the fork's pinned reference and current
  `et-platform` master: `aifoundry-utils/ProjectFunctions` (needs a
  same-named subdirectory symlink; the source file itself lives flat at
  `et-platform/cmake/ProjectFunctions.cmake` today) and `Findlibcap.cmake`
  (also in `et-platform/cmake/`, just needs `CMAKE_MODULE_PATH`).
- **Hard wall found**: past that point, `ggml-et/et-kernels/CMakeLists.txt`
  needs `riscv64-ec-toolchain.cmake`, `DeviceUtils`, `et-common-libs`, and
  `esperantoTrace` — all expected under `${ET_PLATFORM_PATH}/lib/cmake/`.
  These do **not** exist anywhere in the public `et-platform` source (grepped
  the whole repo, confirmed absent). They're part of a separate,
  board-access-gated device-kernel-build SDK distribution, not publicly
  buildable. Don't chase this further without real AIFoundry board
  credentials (`docs/BOARD_ACCESS.md`).
- A **prebuilt** ET-enabled `llama-server` binary (compiled in an earlier
  session, before firmware got cleaned up) does exist and loads with the
  firmware restored — but it tries to `mmap` a real PCIe BAR0 register
  (`0x1000000000`) and hangs indefinitely with no physical ET-SoC1 card
  present. This confirms that specific binary was built for real-hardware
  mode, not software sysemu — the folder name (`build-sysemu`) is misleading.
- **Practical conclusion**: CPU-only builds (`-DGGML_ET=OFF`) are the
  pragmatic verification tier for filing a model-port claim. This still
  gives a real compute-graph build, real architecture identification, and a
  real PPL number via `llama-perplexity` — matching exactly the rigor this
  campaign already used for its honest negative-result disclosures
  (`hunyuan_0_5b`, `exaone4_1_2b`). The actual ET-SoC1 board benchmark run
  happens later in the maintainer's own trusted CI, not something an
  individual contributor needs to reproduce locally to file a valid claim.

## 4. Unrelated but same-session: GGUF/numpy 2.x compat

A separate repo's (`roco_ai`) GGUF→SafeTensors converter did
`int(parts[-1])` on a shape-`(1,)` numpy array, relying on implicit
scalar conversion numpy silently dropped as of 2.x (hard `TypeError` now,
not a warning). Fix: `int(parts[-1].reshape(-1)[0])`. Worth checking for
in any GGUF-metadata-reading script that predates numpy 2.
