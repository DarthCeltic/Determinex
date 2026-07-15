"""scripts/determinex_settings.py — Determinex central configuration spine.

Single source of truth for every path, flag, and tunable that was previously
scattered across 80+ scripts as naked ``os.environ.get()`` calls.

Usage::

    from determinex_settings import get_settings
    s = get_settings()
    print(s.audit_dir)          # resolved Path, may be T:/ or local fallback
    print(s.safety_mode)        # "strict" by default
    print(s.resolved_summary()) # dict of all resolved values (for doctor output)

Environment variable rules
--------------------------
Every value is sourced **only** from environment variables (or a hard default).
No Windows drive letter is *required* for correctness — every T:/ default has a
portable local fallback used automatically when the drive is absent and the env
var is not set.

Safe defaults
-------------
All security and isolation flags fail **closed**:
  - online_discovery = False
  - allow_cloud_fallback = False
  - allow_unsandboxed = False
  - require_docker = True
  - require_cloak = True
  - offline_observer = True
  - safety_mode = "strict"

These can be opened only by explicit env-var assignment.
"""
from __future__ import annotations

import os
import sys
import threading
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_REPO_ROOT = Path(__file__).resolve().parents[1]


def _env(name: str, default: str = "") -> str:
    return os.environ.get(name, default)


def _env_bool(name: str, default: bool = False) -> bool:
    """Return True when env var is "1", "true", "yes", "on" (case-insensitive)."""
    val = os.environ.get(name, "").strip().lower()
    if val == "":
        return default
    return val in ("1", "true", "yes", "on")


def _env_int(name: str, default: int) -> int:
    try:
        return int(os.environ.get(name, ""))
    except (ValueError, TypeError):
        return default


def _env_float(name: str, default: float) -> float:
    try:
        return float(os.environ.get(name, ""))
    except (ValueError, TypeError):
        return default


def _resolve_path(
    env_var: str,
    t_default: str,
    local_fallback: Optional[str | Path] = None,
) -> Path:
    """Resolve a path with portability-safe fallback.

    Priority:
      1. Env var (authoritative)
      2. t_default — used as-is when its drive exists OR no local_fallback
      3. local_fallback — when the t_default drive is absent and fallback provided

    This ensures that no T:/ (or any other drive letter) is *required* for
    correctness when a local fallback is available.
    """
    raw = os.environ.get(env_var, "").strip()
    if raw:
        return Path(raw)

    t_path = Path(t_default)

    if local_fallback is not None:
        # Check whether the drive root for the T-path is accessible.
        drive = t_path.drive  # e.g. "T:" on Windows, "" on POSIX
        if drive:
            drive_root = Path(drive + "/")
            if not drive_root.exists():
                return _REPO_ROOT / local_fallback if not Path(str(local_fallback)).is_absolute() else Path(str(local_fallback))

    return t_path


# ---------------------------------------------------------------------------
# Settings class
# ---------------------------------------------------------------------------

class DeterminexSettings:
    """Centralized Determinex configuration resolved from environment variables.

    Instantiate via :func:`get_settings` to get the cached singleton.
    Direct instantiation is fine for tests (pass env overrides before calling).
    """

    # ------------------------------------------------------------------
    # Core paths
    # ------------------------------------------------------------------

    @property
    def repo_root(self) -> Path:
        return _resolve_path("DETERMINEX_ROOT", str(_REPO_ROOT))

    @property
    def models_dir(self) -> Path:
        return _resolve_path(
            "DETERMINEX_MODELS_DIR",
            "T:/determinex-models",
            local_fallback="data/models",
        )

    @property
    def audit_dir(self) -> Path:
        return _resolve_path(
            "DETERMINEX_AUDIT_DIR",
            "T:/determinex_audit/events",
            local_fallback="logs/events",
        )

    @property
    def corpus_root(self) -> Path:
        return _resolve_path(
            "DETERMINEX_CORPUS_ROOT",
            "T:/determinex_corpus",
            local_fallback="corpus",
        )

    @property
    def swebench_repos(self) -> Path:
        return _resolve_path(
            "DETERMINEX_SWEBENCH_REPOS",
            "T:/determinex-swebench",
        )

    @property
    def programbench_dir(self) -> Path:
        """The ProgramBench evaluation harness root (uv run programbench eval …)."""
        return _resolve_path(
            "PROGRAMBENCH_DIR",
            "T:/Dev/ProgramBench",
        )

    @property
    def pb_tasks_root(self) -> Path:
        """Determinex's per-tool ProgramBench build/eval output directory."""
        return _resolve_path(
            "DETERMINEX_PB_TASKS_ROOT",
            "T:/determinex-programbench",
        )

    @property
    def pb_staging_root(self) -> Path:
        return _resolve_path(
            "DETERMINEX_PB_STAGING_ROOT",
            "T:/determinex-staging",
            local_fallback="data/pb_staging",
        )

    @property
    def rosetta_pt_path(self) -> Path:
        return _resolve_path(
            "DETERMINEX_ROSETTA_PT_PATH",
            "T:/determinex-models/rosetta_v1.pt",
        )

    @property
    def hf_home(self) -> Path:
        return _resolve_path(
            "HF_HOME",
            "T:/huggingface_cache",
            local_fallback=str(Path.home() / ".cache" / "huggingface"),
        )

    @property
    def artifact_quarantine(self) -> Path:
        return _resolve_path(
            "DETERMINEX_QUARANTINE_DIR",
            "T:/determinex_artifacts/quarantine",
            local_fallback="data/quarantine",
        )

    @property
    def artifact_cache(self) -> Path:
        return _resolve_path(
            "DETERMINEX_ARTIFACT_CACHE",
            "T:/determinex_artifacts/cache",
            local_fallback="data/artifact_cache",
        )

    # ------------------------------------------------------------------
    # Safety flags — all fail CLOSED
    # ------------------------------------------------------------------

    @property
    def safety_mode(self) -> str:
        return _env("DETERMINEX_SAFETY_MODE", "strict")

    @property
    def online_discovery(self) -> bool:
        """Online artifact discovery — disabled by default."""
        return _env_bool("DETERMINEX_ONLINE_DISCOVERY", default=False)

    @property
    def allow_cloud_fallback(self) -> bool:
        return _env_bool("DETERMINEX_ALLOW_CLOUD_FALLBACK", default=False)

    @property
    def allow_unsandboxed(self) -> bool:
        return _env_bool("DETERMINEX_ALLOW_UNSANDBOXED", default=False)

    @property
    def require_docker(self) -> bool:
        return _env_bool("DETERMINEX_REQUIRE_DOCKER", default=True)

    @property
    def require_cloak(self) -> bool:
        return _env_bool("DETERMINEX_REQUIRE_CLOAK", default=True)

    @property
    def offline_observer(self) -> bool:
        return _env_bool("DETERMINEX_OFFLINE_OBSERVER", default=True)

    @property
    def flywheel_auto(self) -> bool:
        return _env_bool("DETERMINEX_FLYWHEEL_AUTO", default=False)

    @property
    def cloak_enabled(self) -> bool:
        return _env_bool("DETERMINEX_CLOAK", default=False)

    @property
    def cloak_audit(self) -> bool:
        return _env_bool("DETERMINEX_CLOAK_AUDIT", default=False)

    # ------------------------------------------------------------------
    # Model identifiers
    # ------------------------------------------------------------------

    @property
    def builder_model(self) -> str:
        return _env("DETERMINEX_BUILDER_MODEL", "determinex-engineer-v11-dsl")

    @property
    def observer_model(self) -> str:
        return _env("DETERMINEX_OBSERVER_MODEL", "determinex-observer-v6-dsl")

    @property
    def architect_model(self) -> str:
        return _env("DETERMINEX_ARCHITECT_MODEL", "determinex-sentinel-v5-dsl")

    @property
    def deepseek_model(self) -> str:
        return _env("DETERMINEX_DEEPSEEK_MODEL", "deepseek-chat")

    @property
    def anthropic_model(self) -> str:
        return _env("DETERMINEX_ANTHROPIC_MODEL", "claude-sonnet-4-6")

    @property
    def ollama_url(self) -> str:
        return _env("DETERMINEX_OLLAMA_URL", _env("OLLAMA_HOST", "http://localhost:11434"))

    @property
    def vllm_url(self) -> str:
        return _env("DETERMINEX_VLLM_URL", "http://localhost:8000/v1")

    @property
    def vllm_model(self) -> str:
        return _env("DETERMINEX_VLLM_MODEL", "Qwen/Qwen2.5-Coder-7B-Instruct")

    @property
    def inference_backend(self) -> str:
        return _env("DETERMINEX_INFERENCE_BACKEND", "ollama")

    # ------------------------------------------------------------------
    # API keys — no defaults; callers must handle empty string
    # ------------------------------------------------------------------

    @property
    def anthropic_api_key(self) -> str:
        return _env("ANTHROPIC_API_KEY", _env("DETERMINEX_ANTHROPIC_KEY", ""))

    @property
    def deepseek_api_key(self) -> str:
        return _env("DETERMINEX_DEEPSEEK_KEY", _env("DEEPSEEK_API_KEY", ""))

    @property
    def openrouter_api_key(self) -> str:
        return _env("OPENROUTER_API_KEY", "")

    @property
    def openai_api_key(self) -> str:
        return _env("DETERMINEX_OPENAI_KEY", _env("OPENAI_API_KEY", ""))

    @property
    def gemini_api_key(self) -> str:
        return _env("DETERMINEX_GEMINI_KEY", _env("GEMINI_API_KEY", ""))

    @property
    def hmac_key(self) -> str:
        """HMAC signing key for corpus rows. Prefer DETERMINEX_HMAC_KEY; also accepts DETERMINEX_CORPUS_HMAC_KEY."""
        return _env("DETERMINEX_HMAC_KEY", _env("DETERMINEX_CORPUS_HMAC_KEY", ""))

    # ------------------------------------------------------------------
    # Budget / rate limits
    # ------------------------------------------------------------------

    @property
    def budget_usd(self) -> float:
        return _env_float("DETERMINEX_BUDGET_USD", 2.50)

    @property
    def budget_calls(self) -> int:
        return _env_int("DETERMINEX_BUDGET_CALLS", 200)

    @property
    def budget_per_task(self) -> float:
        return _env_float("DETERMINEX_BUDGET_PER_TASK", 6.0)

    # ------------------------------------------------------------------
    # Context / inference tuning
    # ------------------------------------------------------------------

    @property
    def max_retries(self) -> int:
        return _env_int("DETERMINEX_MAX_RETRIES", 5)

    @property
    def observer_timeout(self) -> int:
        return _env_int("DETERMINEX_OBSERVER_TIMEOUT", 7200)

    @property
    def test_timeout(self) -> int:
        return _env_int("DETERMINEX_TEST_TIMEOUT", 60)

    @property
    def rosetta_layer2(self) -> bool:
        return _env_bool("DETERMINEX_ROSETTA_LAYER2", default=False)

    @property
    def no_rosetta(self) -> bool:
        return _env_bool("DETERMINEX_NO_ROSETTA", default=False)

    # ------------------------------------------------------------------
    # Introspection helpers
    # ------------------------------------------------------------------

    def resolved_summary(self) -> dict[str, object]:
        """Return a flat dict of all resolved values — used by determinex doctor."""
        return {
            # paths
            "repo_root":         str(self.repo_root),
            "models_dir":        str(self.models_dir),
            "audit_dir":         str(self.audit_dir),
            "corpus_root":       str(self.corpus_root),
            "swebench_repos":    str(self.swebench_repos),
            "programbench_dir":  str(self.programbench_dir),
            "pb_tasks_root":     str(self.pb_tasks_root),
            "pb_staging_root":   str(self.pb_staging_root),
            "rosetta_pt_path":   str(self.rosetta_pt_path),
            "hf_home":           str(self.hf_home),
            "artifact_quarantine": str(self.artifact_quarantine),
            "artifact_cache":    str(self.artifact_cache),
            # safety
            "safety_mode":          self.safety_mode,
            "online_discovery":     self.online_discovery,
            "allow_cloud_fallback": self.allow_cloud_fallback,
            "allow_unsandboxed":    self.allow_unsandboxed,
            "require_docker":       self.require_docker,
            "require_cloak":        self.require_cloak,
            "offline_observer":     self.offline_observer,
            "flywheel_auto":        self.flywheel_auto,
            "cloak_enabled":        self.cloak_enabled,
            # models
            "builder_model":    self.builder_model,
            "observer_model":   self.observer_model,
            "architect_model":  self.architect_model,
            "ollama_url":       self.ollama_url,
            "inference_backend": self.inference_backend,
            # api keys (masked)
            "anthropic_api_key":  "***" if self.anthropic_api_key else "(unset)",
            "deepseek_api_key":   "***" if self.deepseek_api_key else "(unset)",
            "openrouter_api_key": "***" if self.openrouter_api_key else "(unset)",
            "openai_api_key":     "***" if self.openai_api_key else "(unset)",
            "hmac_key":           f"***({len(self.hmac_key)} chars)" if self.hmac_key else "(unset)",
        }

    def check_path_availability(self) -> dict[str, bool]:
        """Return which paths currently exist on disk (for doctor pass/warn/fail)."""
        return {
            "repo_root":        self.repo_root.exists(),
            "models_dir":       self.models_dir.exists(),
            "audit_dir":        self.audit_dir.exists(),
            "corpus_root":      self.corpus_root.exists(),
            "swebench_repos":   self.swebench_repos.exists(),
            "programbench_dir": self.programbench_dir.exists(),
            "pb_tasks_root":    self.pb_tasks_root.exists(),
            "pb_staging_root":  self.pb_staging_root.exists(),
            "rosetta_pt_path":  self.rosetta_pt_path.exists(),
            "hf_home":          self.hf_home.exists(),
        }

    def assert_safety_defaults(self) -> list[str]:
        """Return a list of safety violation strings (empty = all closed).

        Call this in any script that should verify it is running in a safe
        configuration before touching corpus or evidence artifacts.
        """
        violations: list[str] = []
        if self.online_discovery:
            violations.append("DETERMINEX_ONLINE_DISCOVERY=1 (unsafe: online artifact discovery enabled)")
        if self.allow_cloud_fallback:
            violations.append("DETERMINEX_ALLOW_CLOUD_FALLBACK=1 (unsafe: cloud fallback enabled)")
        if self.allow_unsandboxed:
            violations.append("DETERMINEX_ALLOW_UNSANDBOXED=1 (unsafe: unsandboxed execution enabled)")
        return violations


# ---------------------------------------------------------------------------
# Singleton
# ---------------------------------------------------------------------------

_singleton: Optional[DeterminexSettings] = None
_lock = threading.Lock()


def get_settings() -> DeterminexSettings:
    """Return the process-wide settings singleton (created on first call)."""
    global _singleton
    if _singleton is None:
        with _lock:
            if _singleton is None:
                _singleton = DeterminexSettings()
    return _singleton


def reset_settings() -> None:
    """Reset the singleton — intended for tests only."""
    global _singleton
    with _lock:
        _singleton = None


# Module-level convenience alias (import and use directly)
settings = DeterminexSettings()


# ---------------------------------------------------------------------------
# CLI: python -m scripts.determinex_settings  (or python scripts/determinex_settings.py)
# ---------------------------------------------------------------------------

def _main() -> int:
    import json
    s = get_settings()
    summary = s.resolved_summary()
    availability = s.check_path_availability()
    violations = s.assert_safety_defaults()

    print("Determinex Settings — resolved configuration\n")
    width = max(len(k) for k in summary) + 2
    for key, val in summary.items():
        exists = availability.get(key)
        tag = ""
        if exists is True:
            tag = "  [exists]"
        elif exists is False:
            tag = "  [missing]"
        print(f"  {key:<{width}} {val}{tag}")

    if violations:
        print("\nSafety violations:")
        for v in violations:
            print(f"  !! {v}")
    else:
        print("\n  Safety defaults: all closed (OK)")

    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(_main())
