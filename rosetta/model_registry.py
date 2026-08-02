"""rosetta/model_registry.py — local model/arch/dim/runtime registry.

The companion file `rosetta/determinex_registry.py` is the *remote weights package
manager* (fetches `family_*.pt` from the public Determinex registry). THIS file is
the *local model registry* — what we run on this machine, where its GGUF lives,
which Rosetta arch projects it, and what hidden dim its tensors carry.

Hard rule: every bridge path must call `require_model()` or `resolve_model()`
and `validate_hidden_dim()` BEFORE touching `RosettaStone.translate()`. The
specific failure the user has hit:

    source_arch='qwen2' expects hidden_dim=3584, but input tensor has shape [1, 1536]

is exactly the failure mode this registry exists to prevent. `qwen2` is too
coarse — the 1.5B/3B/7B/14B Qwen variants have different hidden_dims (1536 /
2048 / 3584 / 5120). Always use the SIZE-SPECIFIC rosetta_arch key.

Bridge results must declare which path executed using BridgeStatus. Anything
else is a silent fallback and must not be reported as Rosetta in eval output.
"""

from __future__ import annotations

import enum
import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------


class RosettaDimensionMismatch(Exception):
    """Hidden-state tensor dim does not match the source arch's registered dim.

    Carries enough structured context that callers can route around it instead
    of guessing. Never raised as a fallback — only when validation explicitly
    fails. Callers must NOT swallow this and pretend the projection worked.
    """

    def __init__(
        self,
        *,
        source_model: str,
        source_arch: str,
        expected_dim: int,
        actual_dim: int,
        target_model: str = "",
        target_arch: str = "",
    ):
        self.source_model = source_model
        self.source_arch = source_arch
        self.expected_dim = expected_dim
        self.actual_dim = actual_dim
        self.target_model = target_model
        self.target_arch = target_arch
        msg = (
            f"RosettaDimensionMismatch: "
            f"source_model={source_model!r} source_arch={source_arch!r} "
            f"expected_dim={expected_dim} actual_dim={actual_dim}"
        )
        if target_model or target_arch:
            msg += f" target_model={target_model!r} target_arch={target_arch!r}"
        super().__init__(msg)

    def to_dict(self) -> dict:
        return {
            "error": "RosettaDimensionMismatch",
            "source_model": self.source_model,
            "source_arch": self.source_arch,
            "expected_dim": self.expected_dim,
            "actual_dim": self.actual_dim,
            "target_model": self.target_model,
            "target_arch": self.target_arch,
        }


class RosettaArchUnknown(Exception):
    """An arch key was referenced that is not registered."""

    def __init__(self, arch: str, known: list[str]):
        self.arch = arch
        self.known = known
        super().__init__(f"unknown rosetta_arch {arch!r}; registered: {known}")


class RosettaModelUnknown(Exception):
    """A model name/alias was referenced that is not registered (require_model only)."""

    def __init__(self, name: str, known: list[str]):
        self.name = name
        self.known = known
        super().__init__(f"unknown model {name!r}; registered: {known}")


# ---------------------------------------------------------------------------
# Bridge result enum — eval reports MUST use these. No silent fallback.
# ---------------------------------------------------------------------------


class BridgeStatus(str, enum.Enum):
    """Result classifier for a Rosetta-mediated generation attempt.

    Eval reports MUST distinguish these. A run that fell back to text but
    reports as "rosetta_projected" is a fake-good number that pollutes A/B
    results — see the Rosetta acceptance line.
    """

    ROSETTA_PROJECTED = "rosetta_projected"
    DIRECT_SELF_INJECTION = "direct_self_injection"
    TEXT_FALLBACK = "text_fallback"
    FAILED_BRIDGE = "failed_bridge"


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

DETERMINEX_MODELS_DIR = Path(os.environ.get("DETERMINEX_MODELS_DIR", "T:/determinex-models"))


@dataclass(frozen=True)
class ArchSpec:
    """A Rosetta-registered architecture. Arch keys are SIZE-SPECIFIC."""

    key: str  # "qwen2_1b5", "qwen2_7b", "mistral_7b" — never bare "qwen2"
    family: str  # "qwen2" / "mistral" / "llama3" — upstream family label
    parameters_label: str  # "1.5B" / "3B" / "7B" / "14B"
    hidden_dim: int  # transformer hidden_size — load-bearing for Rosetta
    notes: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class ModelSpec:
    """A locally-runnable Determinex model. Single resolution point for the bridges.

    Field set matches the API contract the user steered toward:
        name, role, provider, gguf_path, rosetta_arch, hidden_dim
    plus an aliases tuple for ollama-tag / role-name lookups.
    """

    name: str  # canonical name, e.g. "engineer"
    role: str  # engineer | observer | sentinel | architect | oracle
    provider: str  # "ollama" | "gguf" | "hybrid"
    gguf_path: Path | None  # absolute path on disk if available
    rosetta_arch: str  # arch key — must exist in ARCHES
    hidden_dim: int  # denormalized from ARCHES for fast validation
    ollama_tag: str | None = None
    description: str = ""
    aliases: tuple = ()  # additional handles (e.g. tag, role name)

    def to_dict(self) -> dict:
        d = asdict(self)
        d["gguf_path"] = str(self.gguf_path) if self.gguf_path else None
        d["aliases"] = list(self.aliases)
        return d


# ---------------------------------------------------------------------------
# Registry data
# ---------------------------------------------------------------------------

ARCHES: dict[str, ArchSpec] = {
    "qwen2_1b5": ArchSpec(
        "qwen2_1b5", "qwen2", "1.5B", 1536, "Qwen2.5-Coder-1.5B-Instruct — C1 Engineer base"
    ),
    "qwen2_3b": ArchSpec("qwen2_3b", "qwen2", "3B", 2048, "Qwen2.5-3B-Instruct — C3 Observer base"),
    "qwen2_7b": ArchSpec(
        "qwen2_7b", "qwen2", "7B", 3584, "Qwen2.5-Coder-7B-Instruct — architect/oracle role"
    ),
    "qwen2_14b": ArchSpec(
        "qwen2_14b", "qwen2", "14B", 5120, "Qwen2.5-Coder-14B-Instruct — heavyweight local builder"
    ),
    "mistral_7b": ArchSpec(
        "mistral_7b", "mistral", "7B", 4096, "Mistral-7B-Instruct-v0.2 — C7 Sentinel base"
    ),
    "llama3_8b": ArchSpec(
        "llama3_8b", "llama3", "8B", 4096, "Llama-3-8B-Instruct — optional alternate sentinel"
    ),
}


def _maybe_gguf(*candidates: str) -> Path | None:
    """Return the first candidate filename that exists under DETERMINEX_MODELS_DIR.

    Variadic so each ModelSpec can list its current name AND legacy file names
    that map to the same logical role. Returns None when none exist — the
    healthcheck then reports UNAVAILABLE WITH REASON for that role's GGUF.
    """
    for name in candidates:
        p = DETERMINEX_MODELS_DIR / name
        if p.is_file():
            return p
    return None


# Determinex C-tier models. `aliases` lets ollama tags and role names resolve too.
_MODELS_LIST: list[ModelSpec] = [
    ModelSpec(
        name="engineer",
        role="engineer",
        provider="ollama",
        # v11-dsl is served via Ollama only; bare-GGUF fallbacks cover legacy
        # generations that share the same Qwen2.5-Coder-1.5B base.
        gguf_path=_maybe_gguf(
            "engineer-v11.gguf",
            "determinex-engineer-v9.gguf",
            "determinex-engineer-v1.1.gguf",
            "determinex-1-tiny-v1.1-repair.gguf",
        ),
        rosetta_arch="qwen2_1b5",
        hidden_dim=ARCHES["qwen2_1b5"].hidden_dim,
        ollama_tag="determinex-engineer-v11-dsl",
        description="C1 — Builder, fast code generation, DSL fine-tuned",
        aliases=("c1", "determinex-engineer-v11-dsl"),
    ),
    ModelSpec(
        name="observer",
        role="observer",
        provider="ollama",
        gguf_path=_maybe_gguf(
            "observer-v6.gguf",
            "determinex-observer-v4.gguf",
            "determinex-observer-v1.1.gguf",
            "determinex-3-medium-v1.1-repair.gguf",
        ),
        rosetta_arch="qwen2_3b",
        hidden_dim=ARCHES["qwen2_3b"].hidden_dim,
        ollama_tag="determinex-observer-v6-dsl",
        description="C3 — Monitor, error diagnosis, adjudication",
        aliases=("c3", "determinex-observer-v6-dsl"),
    ),
    ModelSpec(
        name="sentinel",
        role="sentinel",
        provider="ollama",
        gguf_path=_maybe_gguf(
            "sentinel-v5.gguf",
            "determinex-sentinel-v1.1.gguf",
            "determinex-sentinel-base-q8.gguf",
            "determinex-7-large-v1.1.gguf",
        ),
        rosetta_arch="mistral_7b",
        hidden_dim=ARCHES["mistral_7b"].hidden_dim,
        ollama_tag="determinex-sentinel-v5-dsl",
        description="C7 — Architect / Oracle base, DAG planning, escalation",
        aliases=("c7", "determinex-sentinel-v5-dsl"),
    ),
    # Architect/Oracle roles are bound to qwen7b per the role-assignment memory:
    # "architect+oracle = determinex/qwen7b. NEVER assign architect to determinex/sentinel"
    ModelSpec(
        name="architect",
        role="architect",
        provider="ollama",
        gguf_path=_maybe_gguf("qwen2.5-coder-7b-instruct.gguf"),
        rosetta_arch="qwen2_7b",
        hidden_dim=ARCHES["qwen2_7b"].hidden_dim,
        ollama_tag="determinex/qwen7b",
        description="DAG planner — Qwen2.5-Coder-7B (NOT sentinel; see role memory)",
        aliases=("architect-7b", "determinex/qwen7b"),
    ),
    ModelSpec(
        name="oracle",
        role="oracle",
        provider="ollama",
        gguf_path=_maybe_gguf("qwen2.5-coder-7b-instruct.gguf"),
        rosetta_arch="qwen2_7b",
        hidden_dim=ARCHES["qwen2_7b"].hidden_dim,
        ollama_tag="determinex/qwen7b",
        description="Compiler-output adjudication assist — same backing model as architect",
        aliases=("oracle-7b",),
    ),
]

MODELS: dict[str, ModelSpec] = {m.name: m for m in _MODELS_LIST}


# Build a flat lookup by every handle (name, ollama_tag, alias entries).
def _build_alias_index() -> dict[str, ModelSpec]:
    idx: dict[str, ModelSpec] = {}
    for m in _MODELS_LIST:
        for handle in {m.name, m.ollama_tag, *m.aliases}:
            if handle:
                # Last-write-wins is fine — collisions are intentional (same model,
                # multiple handles all pointing at it).
                idx[handle] = m
    return idx


_ALIAS_INDEX = _build_alias_index()


# ---------------------------------------------------------------------------
# Public API (matches the API contract the user specified)
# ---------------------------------------------------------------------------


def supported_arches() -> list[str]:
    """Return all registered Rosetta arch keys (sorted)."""
    return sorted(ARCHES.keys())


def supported_models() -> list[str]:
    """Return all registered model names (sorted, canonical names only)."""
    return sorted(MODELS.keys())


def get_arch(key: str) -> ArchSpec:
    """Resolve an arch key. Raises RosettaArchUnknown if missing."""
    if key not in ARCHES:
        raise RosettaArchUnknown(key, supported_arches())
    return ARCHES[key]


def resolve_model(name_or_alias: str) -> ModelSpec | None:
    """Lookup a model by any handle (name, ollama_tag, alias). Returns None if not found."""
    if not name_or_alias:
        return None
    return _ALIAS_INDEX.get(name_or_alias)


def require_model(name_or_alias: str) -> ModelSpec:
    """Same as resolve_model but raises RosettaModelUnknown on miss."""
    m = resolve_model(name_or_alias)
    if m is None:
        raise RosettaModelUnknown(name_or_alias, supported_models())
    return m


def current_family() -> dict[str, ModelSpec]:
    """Return the canonical C1/C3/C7 (+ architect/oracle) family map.

    Keys are the role names: engineer / observer / sentinel / architect / oracle.
    """
    return {m.role: m for m in _MODELS_LIST}


def _tensor_dim(hidden: Any) -> int:
    """Best-effort dim extraction for tensors / arrays / ints / shapes."""
    if isinstance(hidden, int):
        return hidden
    if hasattr(hidden, "shape"):
        shape = tuple(hidden.shape)
        if not shape:
            raise ValueError("0-d tensor has no hidden dim")
        return int(shape[-1])
    if hasattr(hidden, "__len__"):
        return len(hidden)
    raise TypeError(f"cannot derive hidden_dim from {type(hidden).__name__}")


def validate_hidden_dim(
    spec: ModelSpec,
    hidden: Any,
    *,
    target_model: str = "",
) -> None:
    """Verify a tensor / array's last dim matches the model spec's hidden_dim.

    Accepts torch.Tensor, np.ndarray, plain int (already-extracted dim), or any
    object with `.shape` whose last axis is the hidden dim.

    Raises RosettaDimensionMismatch with structured fields on mismatch.
    Never silently downgrades. Never falls back to self-injection — that
    decision belongs to the caller, not validation.
    """
    actual = _tensor_dim(hidden)
    if actual == spec.hidden_dim:
        return

    tgt_arch = ""
    if target_model:
        tgt = resolve_model(target_model)
        if tgt is not None:
            tgt_arch = tgt.rosetta_arch

    raise RosettaDimensionMismatch(
        source_model=spec.name,
        source_arch=spec.rosetta_arch,
        expected_dim=spec.hidden_dim,
        actual_dim=actual,
        target_model=target_model,
        target_arch=tgt_arch,
    )


# ---------------------------------------------------------------------------
# Diagnostic helpers
# ---------------------------------------------------------------------------


def snapshot() -> dict:
    """JSON-serializable snapshot of the full registry — used by healthcheck."""
    return {
        "determinex_models_dir": str(DETERMINEX_MODELS_DIR),
        "arches": {k: v.to_dict() for k, v in ARCHES.items()},
        "models": {k: v.to_dict() for k, v in MODELS.items()},
        "family": {role: m.name for role, m in current_family().items()},
        "bridge_status_values": [s.value for s in BridgeStatus],
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _cli():
    import argparse
    import json

    ap = argparse.ArgumentParser(description="Determinex local model/arch registry")
    ap.add_argument("--list", action="store_true", help="list full registry as JSON")
    ap.add_argument("--model", help="resolve one model by any handle")
    ap.add_argument("--arch", help="resolve one rosetta_arch key")
    args = ap.parse_args()

    if args.model:
        m = resolve_model(args.model)
        if m is None:
            print(json.dumps({"error": "unknown model", "known": supported_models()}, indent=2))
            raise SystemExit(2)
        print(json.dumps(m.to_dict(), indent=2))
        return

    if args.arch:
        try:
            print(json.dumps(get_arch(args.arch).to_dict(), indent=2))
        except RosettaArchUnknown as e:
            print(json.dumps({"error": str(e), "known": e.known}, indent=2))
            raise SystemExit(2)
        return

    print(json.dumps(snapshot(), indent=2))


if __name__ == "__main__":
    _cli()
