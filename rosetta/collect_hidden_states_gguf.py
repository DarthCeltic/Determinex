"""collect_hidden_states_gguf.py -- Rosetta Stone hidden-state collection from LOCAL GGUF
files, no HuggingFace download required.

collect_hidden_states.py's collection is HF-only: every FAMILIES entry is a hf_model_id loaded
via transformers.AutoModelForCausalLM.from_pretrained(). That has two real costs this module
removes: (1) it requires downloading a full-precision checkpoint per family even when a
perfectly good local GGUF already exists (e.g. Determinex's own already-quantized
determinex-engineer-v11-dsl, or a gated model like google/gemma-2-2b-it that needs a manual
HuggingFace license click before ANY download works at all -- confirmed live 2026-07-27:
GatedRepoError 403, darthceltic85 has not yet accepted the gate); (2) it is bounded to exactly
the 6 hardcoded FAMILIES, not "every model the user actually has."

Ryan, direct instruction 2026-07-27: build a GGUF-based collector "for all models, not just the
ones we have." This module:
  - discovers EVERY model already registered in the user's local Ollama (any family, not a
    hardcoded list), resolving each one's real GGUF blob path the same way a human would
    (`ollama show <name> --modelfile`'s `FROM <path>` line);
  - also accepts an arbitrary standalone .gguf path, so a model that was never `ollama create`d
    (e.g. a bare GGUF sitting in a downloads folder) still works;
  - extracts the model's own hidden representation via llama-cpp-python's embedding mode
    (llama.cpp's `llama_get_embeddings()`, mean-pooled across the prompt -- the GGUF-world
    equivalent of transformers' `output_hidden_states=True` final layer, not a retrieval-style
    embedding-model output);
  - writes to the IDENTICAL per-prompt `prompt_NNNN.pt` format collect_hidden_states.py
    produces, so train_rosetta.py and export_rosetta_families.py consume either collector's
    output identically -- this is a second COLLECTION mechanism into the same pipeline, not a
    parallel training path.

Dependency: llama-cpp-python. NOT installed in this environment as of 2026-07-27 (pip installs
are gated for the agent building this -- give the operator the exact command rather than retry).
This module fails loudly and immediately on import if it's missing, with that exact command,
rather than silently no-op -- same "never lie about availability" contract as determinex_oracle.py.

Usage:
    pip install llama-cpp-python
    python rosetta/collect_hidden_states_gguf.py --output_dir outputs/hidden_states_gguf --discover
    python rosetta/collect_hidden_states_gguf.py --output_dir outputs/hidden_states_gguf \
        --model determinex-sentinel-v5-dsl
    python rosetta/collect_hidden_states_gguf.py --output_dir outputs/hidden_states_gguf \
        --gguf-path "C:/models/gemma-2-2b-it-Q8_0.gguf" --family gemma
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

_REPO_ROOT = str(Path(__file__).resolve().parents[1])
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
from rosetta.shared_prompts import SHARED_PROMPTS  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


class LlamaCppUnavailable(RuntimeError):
    """llama-cpp-python is not installed. Raised instead of silently producing zero states --
    same contract determinex_oracle.py's OracleUnavailable uses: a missing dependency is a loud,
    actionable error, never a quiet no-op that could be mistaken for 'nothing to collect'."""

    def __init__(self) -> None:
        super().__init__(
            "llama-cpp-python is not installed. Install it, then re-run this script:\n"
            "    pip install llama-cpp-python\n"
            "(On a CUDA machine, install the GPU-accelerated build instead for far faster "
            "collection -- see https://github.com/abetlen/llama-cpp-python#installation.)"
        )


def _import_llama_cpp():
    try:
        import llama_cpp  # noqa: PLC0415
    except ImportError as e:
        raise LlamaCppUnavailable() from e
    return llama_cpp


_FROM_LINE_RE = re.compile(r"^FROM\s+(.+)$", re.MULTILINE)


def discover_ollama_models() -> dict[str, Path]:
    """Every model currently registered in the local Ollama, mapped to its real GGUF blob path
    on disk -- resolved the same way `ollama show <name> --modelfile` reports it (a `FROM
    <path>` line pointing directly at Ollama's content-addressed blob store), not assumed from
    the model's display name. Returns {} if `ollama` isn't on PATH or no models are registered --
    this is a best-effort discovery step, never a hard requirement (a caller can always pass
    --gguf-path directly instead)."""
    # encoding="utf-8", errors="replace" explicitly: subprocess.run's default text-mode
    # decoding falls back to the Windows console's active codepage (often cp1252), which
    # cannot decode arbitrary Unicode a Modelfile's SYSTEM prompt might contain (found live
    # 2026-07-27: UnicodeDecodeError on byte 0x9d from one real installed model's Modelfile).
    try:
        listing = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            timeout=15,
            encoding="utf-8",
            errors="replace",
        )
    except (OSError, subprocess.TimeoutExpired):
        return {}
    if listing.returncode != 0:
        return {}

    names = []
    for line in listing.stdout.splitlines()[1:]:  # skip header row
        parts = line.split()
        if parts:
            names.append(parts[0])

    out: dict[str, Path] = {}
    for name in names:
        try:
            shown = subprocess.run(
                ["ollama", "show", name, "--modelfile"],
                capture_output=True,
                text=True,
                timeout=15,
                encoding="utf-8",
                errors="replace",
            )
        except (OSError, subprocess.TimeoutExpired):
            continue
        if shown.returncode != 0:
            continue
        m = _FROM_LINE_RE.search(shown.stdout)
        if not m:
            continue
        blob_path = Path(m.group(1).strip())
        if blob_path.is_file():
            out[name] = blob_path
    return out


def collect_states_gguf(
    model_path: Path,
    prompts: list[str],
    family: str,
    out_dir: Path,
    n_ctx: int = 2048,
    n_gpu_layers: int = -1,
) -> int:
    """Run `prompts` through a local GGUF model and save one mean-pooled hidden-state tensor
    per prompt, in the exact `prompt_NNNN.pt` format collect_hidden_states.py's collect_states()
    produces. `n_gpu_layers=-1` offloads every layer to GPU when one is available (llama.cpp's
    own convention); falls back to CPU-only automatically if no GPU is present.
    """
    import torch  # local import: this module's only hard dependency for the SAVE step, and
    # torch is already a project-wide dependency (unlike llama-cpp-python).

    llama_cpp = _import_llama_cpp()
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"  Loading {model_path} (embedding mode)...", flush=True)
    llm = llama_cpp.Llama(
        model_path=str(model_path),
        embedding=True,
        n_ctx=n_ctx,
        n_gpu_layers=n_gpu_layers,
        verbose=False,
    )

    saved = 0
    for i, prompt in enumerate(prompts):
        try:
            # create_embedding() pools llama.cpp's own llama_get_embeddings() output across the
            # prompt's tokens (mean pooling is llama.cpp's default pooling_type for embedding
            # mode) -- the GGUF-world equivalent of collect_hidden_states.py's
            # `outputs.hidden_states[-1].mean(dim=1)`: one pooled vector representing the
            # model's final hidden layer for this prompt.
            result = llm.create_embedding(prompt)
            vec = result["data"][0]["embedding"]
            tensor = torch.tensor(vec, dtype=torch.float32)
            torch.save(tensor, out_dir / f"prompt_{i:04d}.pt")
            saved += 1
            if (i + 1) % 10 == 0:
                print(f"    [{family}] {i + 1}/{len(prompts)} prompts collected", flush=True)
        except Exception as e:
            print(f"    [{family}] prompt {i} failed: {e}", flush=True)

    print(f"  [{family}] Saved {saved}/{len(prompts)} states -> {out_dir}", flush=True)
    del llm
    return saved


def run_collection_gguf(
    output_dir: Path,
    models: dict[str, Path] | None = None,
    single: tuple[str, Path] | None = None,
) -> dict[str, int]:
    """Collect hidden states for every (family_name, gguf_path) pair. `models` is normally the
    output of discover_ollama_models() (or a caller-supplied subset); `single` lets a caller
    collect exactly one standalone .gguf that was never registered with Ollama at all."""
    targets: dict[str, Path] = dict(models or {})
    if single:
        targets[single[0]] = single[1]

    print(f"[COLLECT-GGUF] Prompts: {len(SHARED_PROMPTS)}", flush=True)
    print(f"[COLLECT-GGUF] Targets: {list(targets.keys())}", flush=True)

    results: dict[str, int] = {}
    for family, gguf_path in targets.items():
        print(f"\n[COLLECT-GGUF] -- {family.upper()} ({gguf_path}) --", flush=True)
        fam_dir = output_dir / family
        if fam_dir.exists() and len(list(fam_dir.glob("*.pt"))) >= len(SHARED_PROMPTS) * 0.9:
            print(f"[COLLECT-GGUF] {family}: already collected, skipping.", flush=True)
            results[family] = len(list(fam_dir.glob("*.pt")))
            continue
        try:
            n = collect_states_gguf(gguf_path, SHARED_PROMPTS, family, fam_dir)
            results[family] = n
        except LlamaCppUnavailable:
            raise  # loud and immediate -- do not silently record 0 and continue
        except Exception as e:
            print(f"[COLLECT-GGUF] ERROR {family}: {e}", flush=True)
            results[family] = 0

    print(f"\n[COLLECT-GGUF] Complete: {results}", flush=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "collection_summary.json").write_text(
        json.dumps(
            {"prompts": len(SHARED_PROMPTS), "families": results, "backend": "gguf"}, indent=2
        )
    )
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output_dir", type=str, default="outputs/hidden_states_gguf")
    parser.add_argument(
        "--discover",
        action="store_true",
        help="Collect from every model currently registered in local Ollama",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Collect from exactly one Ollama-registered model by name",
    )
    parser.add_argument(
        "--gguf-path",
        type=str,
        default=None,
        help="Collect from a standalone .gguf file not registered with Ollama",
    )
    parser.add_argument(
        "--family",
        type=str,
        default=None,
        help="Family name to save under (required with --gguf-path)",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)

    if args.gguf_path:
        if not args.family:
            parser.error("--gguf-path requires --family (what name to save the states under)")
        run_collection_gguf(output_dir, single=(args.family, Path(args.gguf_path)))
        return 0

    discovered = discover_ollama_models()
    if not discovered:
        print(
            "[COLLECT-GGUF] No Ollama models discovered (is `ollama list` empty, or "
            "`ollama` not on PATH?). Use --gguf-path for a standalone file instead.",
            file=sys.stderr,
        )
        return 1

    if args.model:
        if args.model not in discovered:
            print(
                f"[COLLECT-GGUF] '{args.model}' not found among Ollama models: "
                f"{list(discovered.keys())}",
                file=sys.stderr,
            )
            return 1
        run_collection_gguf(output_dir, models={args.model: discovered[args.model]})
        return 0

    # --discover (or no selector at all): every registered model.
    run_collection_gguf(output_dir, models=discovered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
