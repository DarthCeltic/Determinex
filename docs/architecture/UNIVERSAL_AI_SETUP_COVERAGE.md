# Working across every AI setup — what is covered, and what is not

Additive to the release-readiness work; nothing here replaces it. Opened 2026-07-30 to track the
"conclusive and working across ALL AI setups" goal as a checklist with evidence, rather than as a
claim.

Status vocabulary matches `docs/audits/RELEASE_READINESS_SCOPE_20260730.md`: **DONE** = changed and
verified by running it. **SIMULATED** = logic verified, hardware not available here. **OPEN** = not
started. **OWNER** = needs a purchase, an account, or a decision only Ryan can make.

---

## 1. Accelerator / hardware backends

| Setup | Detection | Tier follows memory | torch device | Status |
| --- | --- | --- | --- | --- |
| NVIDIA (CUDA) | `nvidia-smi` | yes | `cuda` | **DONE** — verified on this host (6 GB, tier 0) |
| AMD (ROCm) | `amd-smi` → `rocm-smi` | yes | `cuda` ¹ | **SIMULATED** — parsing, unit scaling, tier arithmetic |
| Intel Arc / Data Center GPU | `xpu-smi discovery` | yes | `xpu` ³ | **SIMULATED** |
| Apple Silicon | `sysctl hw.memsize` × 0.75 ² | yes | `mps` | **SIMULATED** |
| Intel Mac | explicitly *not* matched | n/a | `cpu` | **DONE** — `mps` does not exist there |
| CPU-only (x86) | fallback; capacity from **system RAM** ⁴ | yes ⁴ | `cpu` | **DONE** |
| Windows on ARM / Qualcomm Snapdragon | named via `platform.machine()`/`processor()`; capacity from **system RAM** ⁴ ⁵ | yes ⁴ | `cpu` ⁵ | **DONE** — no NPU claim |

¹ A ROCm build of PyTorch deliberately keeps the `cuda` device name. Returning `"rocm"` would hand
callers a string torch rejects, which is why vendor and device are recorded separately.

³ Intel is NOT a CUDA alias the way ROCm is — it is a separate torch device. Handing `cuda` to a
caller on Arc would fail, which is why the device string is carried per-vendor rather than inferred
from the vendor name. A test asserts every entry declares a device torch actually accepts.

² Unified memory is not a separate pool. Reporting all of it would put an 8 GB Mac in tier 0 and start
swapping under a 3B model.

⁴ **Added 2026-07-31.** `tier` was derived from `vram_gb` alone, so every host without a discrete GPU
got tier -1 — `max_local_models() == 0`, `keep_hot == []` — and a 128 GB workstation scored identically
to an 8 GB laptop. `ram_gb` was already measured and then used for nothing. Wrong on its own terms:
Ollama and llama.cpp run models out of system RAM, which is exactly how a CPU-only install works. It
also made `keep_hot == []` backwards — a model reload costs *more* on a CPU host, so the machine that
most needed the builder resident was the one told to keep nothing.

Capacity now comes from `RAM − 8 GB` reserve (the OS, the app, and the cargo/Docker the same session
competes with), through the *same* threshold table as VRAM so the two cannot drift. Capped at **tier
1**: tier 2 means one branch per GPU, and keeping four models resident buys nothing when execution is
serialised on one CPU. `max_parallel_steps` returns 1 whenever `gpu_count == 0` regardless of tier —
having RAM does not make concurrent branches safe on one shared CPU. The pool used is recorded as
`capacity_basis` (`vram` / `system_ram` / `none`) and shown in the capability card, because "tier 1 on
16 GB of VRAM" and "tier 1 on 24 GB of system RAM" are different machines.

⁵ Snapdragon X has an Adreno GPU and a Hexagon NPU, and **Determinex uses neither**: there is no
PyTorch backend for them on Windows ARM64, and Ollama runs the ARM64 CPU path. So such a host is
precisely "no accelerator, plenty of RAM" and is handled by ⁴ rather than by a probe that would imply
an accelerator we never call. What was added is *identification* — the label reads
`CPU only (Qualcomm Snapdragon, ARM64) — 32.0 GB system RAM`, so a Snapdragon user can see the machine
was recognised instead of concluding detection failed. `platform_note` is display-only; a test asserts
it never becomes a vendor, a torch device, a device count, or a VRAM figure.

**Why this mattered.** Before 2026-07-30 detection was `nvidia-smi` only, so an AMD or Apple machine
fell to tier -1 "CPU-only" — `max_local_models() == 0`, `max_parallel_steps == 1`, nothing kept
resident. The strongest available hardware was driven as the weakest possible host.

**Fixed alongside it:** the tier thresholds were literal (`>= 24`), so every 24 GB card — an RTX 4090
included — was tier 1 rather than tier 2, because a 24 GB card reports 23.99 GiB. And RAM read as
0.0 GB on Windows 11 24H2+, because the probe shelled out to `wmic`, which that release removed.

**Still not covered:** using an NPU (Qualcomm Hexagon, Intel AI Boost, Apple Neural Engine) as an
inference device. That needs an ONNX Runtime / QNN execution-provider path, which is a different
backend from the `torch`/Ollama one Determinex drives today — not an `_ACCELERATORS` entry. Those hosts
run correctly on the CPU path with RAM-derived capacity (⁴, ⁵); what is missing is speed, not
function, and the surface says so rather than implying an NPU is in use.

**Honest limit:** AMD and Apple are verified by simulating the vendor tools' documented CSV output. No
such hardware was available. That proves the parsing and the arithmetic; it is not a claim that
`amd-smi` on a real MI300 prints what the tests simulate. First run on real AMD hardware should be
treated as the actual verification.

## 2. Model providers / routing

Locality is decided in ONE place, `budget.is_local_model`, which knows `ollama/`, `ollama_chat/`,
`hosted_vllm/`, `text-completion-openai/`, `determinex/`, `local/` and the bare `determinex-` family.
That consolidation exists because the same question was answered by hand in three places and was wrong
in two — **DONE**, and guarded:

* the **pricer** billed local sessions at the cloud fallback rate until 2026-07-29, tripping
  `budget_exhausted` on runs that never left the machine;
* the **api_client timeout guard** never fired for an alias, so a local call had no timeout and a build
  step hung indefinitely (observed: 30+ minutes at 0% CPU on an open Ollama socket);
* the **safety gate** classified `determinex/engineer` as cloud, so on a fresh install
  (`DETERMINEX_REQUIRE_CLOAK=1` by default, `.env` not shipped) every local call was **blocked** as a
  "Cloud API call".

**OPEN:** no test asserts that a *newly added* provider prefix reaches all three consumers. The
guard currently pins the known set.

**The alias map itself was not shipped — FIXED.** `litellm_config.yaml` turns `determinex/engineer`
into `ollama/determinex-engineer-v11-dsl`. It was absent from `bundle.resources` AND from the sidecar's
PyInstaller data, and `_ROOT` in a sidecar is a temp extraction directory, so the single location the
loader checked could never hold it in a shipped build. Measured with `_ROOT` pointed at an empty dir:
**0 alias entries, every role alias unusable** — the hive loop could not call any model. Now the loader
searches `_ROOT`, `sys._MEIPASS`, beside the executable, and the `_up_/_up_/` layout Tauri preserves;
and the sidecar build ships the file. It is safe to ship because every `api_key` is an `os.environ/`
reference, which a test now enforces — a literal credential there would ship to every user.

This is the **third** defect of one shape found on 2026-07-30: works on the dev box because a file is
in the checkout, fails on every install. The other two were the agent-chat default model and the safety
gate blocking local calls, both dependent on `.env`. Worth naming as a class: **anything read from the
checkout root is absent in a shipped build unless something explicitly bundles it.**

## Routing out of the box

**DONE 2026-07-31 — the default is derived, not flipped.** The ladder lives in
`litellm_config.yaml` (`determinex.builder_ladder`): `determinex/engineer` (1.5B) then
`determinex/qwen7b` (7B), both LOCAL, paid rung commented out.

`DETERMINEX_ROUTE` still wins when set, and now in **both** directions — `=0` previously was
indistinguishable from unset, so there was no way to say "not this run". Unset, `route_decision`
answers from two checkable conditions:

| Condition | Why it is not just caution |
| --- | --- |
| **Every rung is local** | A user who uncomments `cloud/deepseek-chat` would otherwise begin escalating to a paid model without ever enabling routing. One paid rung → routing waits to be asked. `is_local_model` is the canonical locality decision and resolves the `determinex/*` aliases, so this is not a prefix guess. |
| **Tier ≥ 1** | The ladder is a 1.5B held resident (`keep_alive=-1`) plus a ~4.7 GB 7B: ~6.3 GB live on a card advertising 6 GB. Tier 0 offloads to CPU and prefill hits the 400–500 s that `api_client._ollama_extra` already documents as the cause of builder timeouts. Escalation that reliably times out is worse than none. |

Anything unreadable fails toward **off** — the prior behaviour — rather than toward spending money
or thrashing VRAM. Every session logs which way it went and why, because a derived default that
stays silent cannot be told apart from a broken feature.

Two things this change broke that had to be fixed with it: `determinex_route_ab.py`'s baseline arm
relied on *absence* to mean off, which on a tier-1 host would have compared routing against itself —
it now sets `DETERMINEX_ROUTE=0` explicitly, and `run_arm` refuses any arm that does not state its
intent. A test also asserts the shipped ladder is still all-local, so adding a paid rung to the
config fails the suite rather than quietly arming a spending default.

## 3. Oracle / language backends

Sandboxed and verified: **Rust, Go, Python, TypeScript**. Everything else fails closed with an
actionable message. Kotlin, Swift and C/C++ are marked `planned` in the Marketplace and cannot be
toggled to "Installed" — see `docs/audits/RELEASE_READINESS_SCOPE_20260730.md` S5.2.

The richer per-language oracles in `determinex_oracle.py` are deliberately **not** wired into the IDE
path: their `verify_fn`s run a direct host subprocess, and buying verification by executing
model-generated code outside the sandbox would trade a correctness gap for a security one.

## 4. Surfacing it

`get_runtime_capability_status` (Python backend surface + Tauri command, ACL permission 175) returns
the detected accelerator, tier, torch device, resident-model policy, parallel-step budget, and the
`determinex_usage_ledger` summary. Where a probe cannot answer it carries the reason rather than a
zero, because a zero reads as "measured, and it was nothing".

**DONE** — `RuntimeCapabilityCard` renders it in Settings → AI Engine & Diagnostics, above Setup
Repair, because "what is this machine" is the first question that tab exists to answer.

It has three visually distinct states and no fourth: loading, a real reading, and
unavailable-with-reason. A failed probe is never rendered as a measurement — an absent VRAM figure
says "Accelerator not detected: <reason>", and an unreadable RAM figure says "not readable" rather
than `0.0 GB`. `invokeSafe` resolves `null` instead of rejecting, so null is the failure signal and is
treated as such. 7 tests pin exactly those distinctions, including that `0.0 GB` never appears when
nothing was measured.

## 5. Still open

| Item | Status |
| --- | --- |
| Qualcomm / Windows-on-ARM hosts | **DONE** — named, and capacity comes from system RAM. See ⁴ ⁵ |
| NPU as an *inference device* (Hexagon / AI Boost / ANE) | **OPEN** — needs an ONNX Runtime QNN path, a different backend from torch/Ollama |
| Real-AMD-hardware verification | **OWNER** — needs a ROCm box |
| Hugging Face Space demo | **OPEN** |
| README hardware-support section | **DONE** — four vendors, with the simulated caveat stated in the public README rather than only in tests |
| Engine reachable from the installed CLI | **DONE 2026-07-31** — `determinex build --idea <file>`. Everything the console script exposed was diagnostic, so an installed Determinex could not reach verified search at all. See §6. |
| Code-signing certificate | **OWNER** — purchase |
| `legal_public_distribution` operator review | **OWNER** — attestation |

## 6. Reaching the engine without a source checkout

The installed `determinex` console script offered `doctor`, `status`, `config` and `evidence` —
all diagnostic. The correctness engine was reachable only as
`python scripts/determinex_build_from_idea.py`, which by definition means a source checkout, not
an install. `determinex build --idea <file> [--provider local] [--model M] [--lang L] [--k N]`
closes that; it dispatches to the same module rather than duplicating its argument parsing.

Two defects had to be fixed to make that command honest, and both are the house pattern — a
check reporting an outcome it had not established:

* **The engine reported a capability verdict for a model it never called.** Run exactly as
  documented with a bare Ollama tag, `build_from_idea` printed `not solved, samples=12` plus an
  Adjudicator next-move. LiteLLM had raised `BadRequestError: LLM Provider NOT provided` on all
  twelve calls. `VerifiedSearch` had been turning the exception into the *string*
  `"__generation_error__: ..."`, digesting it, deduping it and handing it to the **oracle** as if
  it were source — and because every error string hashed identically, round 2 concluded "model is
  looping". Generation errors are now counted, never verified; a wholly failed run reports
  `NOT ATTEMPTED` with the real exception and `next_moves == ["fix:generator"]`; a partial failure
  still solves but discloses that the effective sample count was lower than requested.
  `get_generator("local", …)` now qualifies a bare tag with `ollama/` — the third place this
  footgun has bitten, and *not* the locality-guessing `budget.is_local_model` refuses to do,
  because the caller has already declared the provider.

* **The CLI advertised a command it rejected.** The command set was written down twice — click
  registrations plus `_USAGE`, and again as a literal tuple in `main()`'s dispatch guard — so
  adding `build` produced a CLI that listed it in `--help` and answered
  `Unknown command: 'build'`. The guard is derived from the click group now, and a test pins
  help-vs-dispatch agreement rather than today's contents.

Verified end-to-end: `determinex build --idea clamp.md --provider local --k 4` → `SOLVED` on
sample 1 against a 4-check synthesized oracle, candidate executed in `intake.hardened_runner`
with the network denied.

**Local-environment caveat, not a shipped defect:** `.venv/Scripts/determinex.exe` in this
checkout fails with `uv trampoline failed to canonicalize script path`, because the editable
install still maps to `C:\Dev\Citadel\scripts` from before the rename. The packaging itself is
sound — `top_level.txt` lists `scripts`, and loading the entry point the way a console script
does (`importlib.metadata` → `ep.load()`) runs correctly. Fix locally with
`python -m pip install -e .`.
