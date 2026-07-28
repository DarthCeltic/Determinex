#!/usr/bin/env python3
"""
determinex_providers.py -- the universal provider registry (bring in any AI)
=========================================================================
Determinex's amplifier defined ONE contract: generate(prompt, temperature) -> str.
This registry exposes EVERY model -- Claude, Codex/GPT, Gemini, DeepSeek, local
Ollama, and anything added later -- behind that single contract, so any of them
plugs straight into verified search / build-from-idea / repair / the router.
Bringing in a new AI is one entry; that is what makes Determinex a host, not a
wrapper.

The whole point: correctness is bounded by the ORACLE, not the model, so it does
not matter which provider you bolt on -- weak or frontier, local or cloud,
present or not-yet-invented. Use one, or ensemble several (the router escalates
tiny->frontier and the amplifier samples them for diversity).

    from determinex_providers import get_generator, available, register_provider
    gen = get_generator("claude")            # generate(prompt, temp) -> str
    build_from_idea(idea, gen)               # ...feeds straight into the engine

    # an addon registers itself:
    register_provider("myllm", lambda model: my_generate_fn, tier=2, models=["myllm/x"])

CLI
---
    python scripts/determinex_providers.py            # show what's available here
"""
from __future__ import annotations

import json
import os
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse


class NetworkPolicyViolation(Exception):
    """Raised when an external network request is blocked by the active DETERMINEX_NETWORK_POLICY."""
    pass

GenerateFn = Callable[[str, float], str]
VALID_NETWORK_POLICIES = {"offline", "cloaked", "online"}


def _load_env_once() -> None:
    """Load repo .env into os.environ so provider keys are detected (idempotent)."""
    if os.environ.get("_DETERMINEX_ENV_LOADED"):
        return
    env = Path(__file__).resolve().parent.parent / ".env"
    if env.exists():
        for line in env.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and v and not os.environ.get(k):
                os.environ[k] = v
    os.environ["_DETERMINEX_ENV_LOADED"] = "1"
    _apply_env_aliases()


# The same credential goes by different names in different places, and a
# mismatch is silent: the provider simply reports itself unavailable and the
# model is skipped, with nothing saying why.
#
# Found live 2026-07-28: `.env` carried HF_TOKEN (the name HuggingFace's own CLI
# and docs use), this module's huggingface provider checked
# HUGGINGFACE_API_KEY, and passport.rs stores its row as HUGGINGFACE_TOKEN.
# Three names, one token, and the configured token reached nothing.
#
# Canonical name first, accepted aliases after. Aliasing is one-directional and
# never overwrites a value that is already set, so an explicit
# HUGGINGFACE_API_KEY always wins over an inferred one.
_ENV_ALIASES: dict[str, tuple[str, ...]] = {
    "HUGGINGFACE_API_KEY": ("HF_TOKEN", "HUGGINGFACE_TOKEN", "HUGGING_FACE_HUB_TOKEN"),
    "OPENAI_API_KEY": ("OPENAI_KEY",),
    "ANTHROPIC_API_KEY": ("CLAUDE_API_KEY",),
    "GEMINI_API_KEY": ("GOOGLE_API_KEY", "GOOGLE_GENAI_API_KEY"),
    "GITHUB_TOKEN": ("GH_TOKEN",),
}


def _apply_env_aliases() -> None:
    """Fill a canonical key from any accepted alias. Idempotent."""
    for canonical, aliases in _ENV_ALIASES.items():
        if os.environ.get(canonical):
            continue
        for alias in aliases:
            value = os.environ.get(alias)
            if value:
                os.environ[canonical] = value
                break


_load_env_once()


@dataclass
class Provider:
    name: str
    tier: int                       # 1 tiny/local ... 4 frontier
    env_key: str                    # required API key env var ("" = local/none)
    default_model: str              # litellm-style model string
    aliases: tuple[str, ...] = ()
    factory: Callable[[str], GenerateFn] | None = None   # custom (addons); else litellm
    models: list[str] = field(default_factory=list)

    def available(self) -> bool:
        if self.factory is not None and not self.env_key:
            return True
        if not self.env_key:                       # local
            return _ollama_up() if "ollama" in self.default_model else True
        return bool(os.environ.get(self.env_key))


# ---------------------------------------------------------------------------
# The universal LiteLLM-backed generator (handles claude/gpt/gemini/deepseek/ollama)
# ---------------------------------------------------------------------------
def _network_policy() -> str:
    policy = os.environ.get("DETERMINEX_NETWORK_POLICY", "cloaked").strip().lower()
    if policy not in VALID_NETWORK_POLICIES:
        raise NetworkPolicyViolation(
            f"Invalid DETERMINEX_NETWORK_POLICY={policy!r}; expected one of {sorted(VALID_NETWORK_POLICIES)}."
        )
    return policy


def _is_local_litellm_model(model: str) -> bool:
    normalized = model.strip().lower()
    return (
        normalized.startswith("ollama/")
        or normalized.startswith("ollama_chat/")
        or normalized.startswith("hosted_vllm/")
        or normalized.startswith("text-completion-openai/")
    )


def _litellm_generator(model: str) -> GenerateFn:
    def _gen(prompt: str, temperature: float) -> str:
        policy = _network_policy()
        if policy == "offline" and not _is_local_litellm_model(model):
            raise NetworkPolicyViolation(
                f"Cannot use cloud model '{model}' because DETERMINEX_NETWORK_POLICY is set to 'offline'."
            )

        import litellm
        resp = litellm.completion(
            # 8192: a full corrected compile.sh (the amplifier's task) runs 200-400 lines
            # >> 1024 tokens -> 1024 TRUNCATED every candidate to a malformed script that
            # fast-failed the eval (~0s). Code generation needs the headroom.
            model=model, temperature=float(temperature),
            messages=[{"role": "user", "content": prompt}], max_tokens=8192)
        _ledger_append(model, resp)
        return resp.choices[0].message.content or ""
    return _gen


# USD per 1M tokens (in, out) for cloud lanes without a BudgetGuard PRICING row.
# Conservative overestimates — the ledger exists to catch runaway spend early.
_LEDGER_PRICING_DEFAULT = (1.0, 1.0)
_LEDGER_PRICING = {
    "huggingface/qwen/qwen2.5-coder-32b-instruct": (0.9, 0.9),
}


def _ledger_append(model: str, resp) -> None:
    """Append real token usage to logs/api_ledger/providers.jsonl. NEVER raises —
    accounting must not break generation. Every cloud call through the litellm
    lane lands here so credit burn is observable (was previously untracked)."""
    try:
        import datetime as _dt
        import json as _json
        usage = getattr(resp, "usage", None)
        tin = int(getattr(usage, "prompt_tokens", 0) or 0)
        tout = int(getattr(usage, "completion_tokens", 0) or 0)
        pin, pout = _LEDGER_PRICING.get(model.lower(), _LEDGER_PRICING_DEFAULT)
        ledger_dir = Path(__file__).resolve().parent.parent / "logs" / "api_ledger"
        ledger_dir.mkdir(parents=True, exist_ok=True)
        with open(ledger_dir / "providers.jsonl", "a", encoding="utf-8") as f:
            f.write(_json.dumps({
                "ts": _dt.datetime.now(_dt.UTC).isoformat(timespec="seconds"),
                "model": model, "tokens_in": tin, "tokens_out": tout,
                "est_usd": round(tin / 1e6 * pin + tout / 1e6 * pout, 6),
            }) + "\n")
    except Exception:
        pass


def _ollama_up(host: str = "http://localhost:11434") -> bool:
    import urllib.request
    try:
        urllib.request.urlopen(host + "/api/tags", timeout=2)
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Registry -- the built-in providers + the extension point
# ---------------------------------------------------------------------------
_PROVIDERS: dict[str, Provider] = {}


def register_provider(name: str, *, tier: int = 3, env_key: str = "",
                      default_model: str = "", aliases: tuple[str, ...] = (),
                      factory: Callable[[str], GenerateFn] | None = None,
                      models: list[str] | None = None) -> None:
    """Register an AI provider/addon. With no factory it routes through LiteLLM
    (model string decides the backend). With a factory it can be anything that
    yields generate(prompt, temperature) -> str -- a local agent, a remote API,
    an ensemble, a future model."""
    p = Provider(name=name, tier=tier, env_key=env_key,
                 default_model=default_model or name, aliases=aliases,
                 factory=factory, models=models or [])
    for key in (name, *aliases):
        _PROVIDERS[key.lower()] = p


# Built-ins. Codex == OpenAI; "claude" == Anthropic; etc. All via LiteLLM.
register_provider("claude", tier=4, env_key="ANTHROPIC_API_KEY",
                  default_model="anthropic/claude-sonnet-4-6",
                  aliases=("anthropic", "claude-code"))
register_provider("codex", tier=4, env_key="OPENAI_API_KEY",
                  default_model="openai/gpt-5.5-pro",
                  aliases=("openai", "gpt"))
register_provider("gemini", tier=4, env_key="GEMINI_API_KEY",
                  default_model="gemini/gemini-3-flash-preview",
                  aliases=("google",))
register_provider("deepseek", tier=3, env_key="DEEPSEEK_API_KEY",
                  default_model="deepseek/deepseek-chat")
register_provider("groq", tier=3, env_key="GROQ_API_KEY",
                  default_model="groq/llama-3.3-70b-versatile")
register_provider("huggingface", tier=3, env_key="HUGGINGFACE_API_KEY",
                  default_model="huggingface/Qwen/Qwen2.5-Coder-32B-Instruct",
                  aliases=("hf",))
register_provider("local", tier=1, env_key="",
                  default_model="ollama/determinex-coder-base-tiny:latest",
                  aliases=("ollama", "tiny"))
register_provider("bonsai", tier=1, env_key="",
                  default_model="ollama/bonsai-27b",
                  aliases=("bonsai-27b", "prism-ml/bonsai"))

# ── vLLM provider (1C — audit 2026-07-19) ────────────────────────────────────
# vLLM serves an OpenAI-compatible API. For the PB churn loop the verified-search
# amplifier benefits from vLLM's continuous batching: K=8 requests served in
# parallel instead of sequentially, cutting per-tool wall-clock time ~6x.
#
# Setup (Linux + CUDA required):
#   pip install vllm>=0.5.0
#   vllm serve Qwen/Qwen2.5-Coder-32B-Instruct --port 8000 --dtype bfloat16
#
# Then set in .env:
#   DETERMINEX_VLLM_BASE_URL=http://localhost:8000
#   DETERMINEX_VLLM_MODEL=Qwen/Qwen2.5-Coder-32B-Instruct
#
# _is_local_litellm_model() already recognizes "hosted_vllm/" prefix as local.
_VLLM_BASE_URL = os.environ.get("DETERMINEX_VLLM_BASE_URL", "http://localhost:8000").rstrip("/")
_VLLM_DEFAULT_MODEL = os.environ.get(
    "DETERMINEX_VLLM_MODEL", "hosted_vllm/Qwen/Qwen2.5-Coder-32B-Instruct"
)
# Prefix with hosted_vllm/ if the user gave a plain HF model name
if not _VLLM_DEFAULT_MODEL.startswith("hosted_vllm/"):
    _VLLM_DEFAULT_MODEL = f"hosted_vllm/{_VLLM_DEFAULT_MODEL}"


def _vllm_factory(model: str) -> GenerateFn:
    """Factory for vLLM provider: routes through LiteLLM's hosted_vllm backend."""
    def _gen(prompt: str, temperature: float) -> str:
        import litellm
        resp = litellm.completion(
            model=model,
            temperature=float(temperature),
            messages=[{"role": "user", "content": prompt}],
            max_tokens=8192,
            api_base=_VLLM_BASE_URL,
        )
        _ledger_append(model, resp)
        return resp.choices[0].message.content or ""
    return _gen


def _vllm_available() -> bool:
    """vLLM is available if its API responds to /health."""
    import urllib.request
    try:
        urllib.request.urlopen(f"{_VLLM_BASE_URL}/health", timeout=2)
        return True
    except Exception:
        return False


register_provider(
    "vllm",
    tier=1,
    env_key="",  # No API key — local endpoint
    default_model=_VLLM_DEFAULT_MODEL,
    aliases=("vllm-local",),
    factory=_vllm_factory,
)



# ---------------------------------------------------------------------------
# User-registered models -- "compatible with EVERYTHING"
# ---------------------------------------------------------------------------
# Ryan, live: "users should be able to add future llms that dont have access at
# the moment, we should make sure we are compatable with EVERYTHING."
#
# The IDE writes user-added models into `models_registry.json` in the Tauri app
# data directory (see frontend/src-tauri/src/registry.rs). Nothing read that file
# on this side, so a model added in the UI was registered into a catalogue the
# engine never consulted -- it appeared in a dropdown and could not be used.
#
# An entry carrying `base_url` is routed as `openai/<id>` with that api_base.
# That covers effectively every current and future provider without a code change,
# because vendors and local servers alike (vLLM, llama.cpp, LM Studio, Ollama,
# OpenRouter, Together, Fireworks, and whatever launches next month) all expose an
# OpenAI-compatible /v1 surface. An entry without one is assumed to name a model a
# built-in provider already understands and is routed by LiteLLM on its id alone.
#
# `api_key_env` holds the NAME of an environment variable, never a secret: this
# file is plain JSON on disk, and a key written into it would end up in every
# backup of the app data directory.

_CUSTOM_REGISTRY_ENV = "DETERMINEX_MODELS_REGISTRY"


def _app_data_registry_paths() -> list[Path]:
    """Where models_registry.json can live, most explicit first."""
    paths: list[Path] = []
    override = os.environ.get(_CUSTOM_REGISTRY_ENV, "").strip()
    if override:
        paths.append(Path(override))
    # Tauri's app data dir. The identifier is set in tauri.conf.json; on Windows
    # this is %APPDATA%\<identifier>, on macOS ~/Library/Application Support, and
    # on Linux ~/.local/share.
    ident = "com.determinex.ide"
    appdata = os.environ.get("APPDATA")
    if appdata:
        paths.append(Path(appdata) / ident / "models_registry.json")
    home = Path.home()
    paths.append(home / "Library" / "Application Support" / ident / "models_registry.json")
    paths.append(home / ".local" / "share" / ident / "models_registry.json")
    return paths


def _custom_model_entries() -> list[dict]:
    for path in _app_data_registry_paths():
        try:
            if not path.is_file():
                continue
            data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
        except (OSError, json.JSONDecodeError):
            # A malformed or unreadable registry must not take the engine down;
            # the built-in providers still work.
            continue
        out: list[dict] = []
        for tier in data.get("tiers") or []:
            for model in tier.get("models") or []:
                if isinstance(model, dict) and model.get("id"):
                    out.append(model)
        if out:
            return out
    return []


def _openai_compatible_factory(model_id: str, base_url: str, api_key_env: str) -> GenerateFn:
    """Generate against any OpenAI-compatible endpoint."""
    def _gen(prompt: str, temperature: float) -> str:
        policy = _network_policy()
        # A user-supplied endpoint may well be a local server, which offline mode
        # must still allow -- but anything not demonstrably loopback is treated as
        # network egress and refused, rather than assumed safe.
        if policy == "offline" and not _is_loopback(base_url):
            raise NetworkPolicyViolation(
                f"Cannot reach custom endpoint '{base_url}' because "
                f"DETERMINEX_NETWORK_POLICY is set to 'offline'."
            )
        import litellm
        kwargs = {
            "model": f"openai/{model_id}",
            "temperature": float(temperature),
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 8192,
            "api_base": base_url,
        }
        key = os.environ.get(api_key_env, "") if api_key_env else ""
        # Many local servers require no key but LiteLLM's openai backend still
        # wants the parameter present, so send a placeholder rather than failing.
        kwargs["api_key"] = key or "not-needed"
        resp = litellm.completion(**kwargs)
        _ledger_append(f"openai/{model_id}", resp)
        return resp.choices[0].message.content or ""
    return _gen


def _is_loopback(url: str) -> bool:
    host = urlparse(url).hostname or ""
    return host in {"localhost", "127.0.0.1", "::1", "0.0.0.0"}


def register_custom_providers() -> list[str]:
    """Register every user-added model from the IDE's registry. Returns the names
    registered, so a caller (and the test suite) can assert it actually happened."""
    registered: list[str] = []
    for entry in _custom_model_entries():
        model_id = str(entry["id"]).strip()
        if not model_id:
            continue
        base_url = str(entry.get("base_url") or "").strip()
        api_key_env = str(entry.get("api_key_env") or "").strip()
        # Name it by id so a user picks the same string they typed in.
        name = model_id.lower()
        if base_url:
            register_provider(
                name,
                tier=int(entry.get("tier") or 3),
                env_key="",  # availability is the endpoint's, not a key's
                default_model=model_id,
                factory=lambda m, _u=base_url, _k=api_key_env: _openai_compatible_factory(m, _u, _k),
            )
        else:
            register_provider(name, tier=3, env_key=api_key_env, default_model=model_id)
        registered.append(name)
    return registered


# Registered at import so every entry point (hive, amplifier, autofix, the IDE
# bridge) sees user-added models without each having to remember to ask.
try:
    register_custom_providers()
except Exception as exc:  # pragma: no cover - defensive
    print(f"[providers] could not load user-added models: {exc}", file=sys.stderr)


def get_generator(provider: str, model: str | None = None) -> GenerateFn:
    """Return the universal generate(prompt, temperature) for a provider."""
    p = _PROVIDERS.get(provider.lower())
    if p is None:
        raise KeyError(f"unknown provider '{provider}'. Known: {sorted(set(_PROVIDERS))}")
    m = model or p.default_model
    if p.factory is not None:
        return p.factory(m)
    return _litellm_generator(m)


def available() -> dict[str, bool]:
    seen = {}
    for p in _PROVIDERS.values():
        seen[p.name] = p.available()
    return dict(sorted(seen.items()))


def get_rotating_generator(names: list[str] | None = None, persist: bool = True):
    """A generate(prompt, temperature) that auto-throttles per model and ROTATES
    across providers on a 429 -- so a rate limit on one AI transparently falls over
    to the next. Defaults to all available providers. Returns the universal contract."""
    from determinex_ratelimit import AdaptiveLimiter, RotatingGenerator
    names = names or [n for n, ok in available().items() if ok]
    if not names:
        raise RuntimeError("no providers available for a rotating generator")
    providers = [(n, get_generator(n)) for n in names]
    pp = (Path(__file__).resolve().parent.parent / ".determinex_ratelimits.json") if persist else None
    return RotatingGenerator(providers, limiter=AdaptiveLimiter(persist_path=pp)).generate


def to_router_entries(only_available: bool = True):
    """Build determinex_router.ModelEntry list from the registry -- so the router can
    escalate across providers (e.g. local tiny -> Claude -> a frontier fallback)."""
    sys.path.insert(0, os.path.dirname(__file__))
    from determinex_router import ModelEntry
    entries, seen = [], set()
    for p in _PROVIDERS.values():
        if p.name in seen:
            continue
        seen.add(p.name)
        if only_available and not p.available():
            continue
        entries.append(ModelEntry(name=p.name, tier=p.tier, cost=float(p.tier),
                                  generate=get_generator(p.name),
                                  capability_hint=p.default_model))
    return entries


def main() -> int:
    print("=== Determinex providers (universal generate contract) ===")
    for name, ok in available().items():
        p = _PROVIDERS[name]
        mark = "READY" if ok else "----"
        print(f"  {mark}  {name:10} tier {p.tier}  {p.default_model}"
              + ("" if ok else f"   (needs {p.env_key or 'ollama'})"))
    rdy = [n for n, ok in available().items() if ok]
    print(f"\n  {len(rdy)} provider(s) ready here: {rdy}")
    print("  Any of them plugs into build-from-idea / repair / router unchanged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
