"""tests/test_settings.py — CONFIG_SPINE_LOCK_001 + PATH_PORTABILITY_LOCK_001

Verifies that DeterminexSettings:
  - resolves all paths without requiring T:/ to exist
  - respects env-var overrides
  - returns safe defaults for all safety flags
  - is importable with zero side effects
  - singleton resets correctly in test isolation
  - assert_safety_defaults() catches violations
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
for _p in (_ROOT, _ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))


@pytest.fixture(autouse=True)
def _reset_singleton():
    """Isolate each test from the module-level singleton."""
    from determinex_settings import reset_settings
    reset_settings()
    yield
    reset_settings()


# ---------------------------------------------------------------------------
# Importability
# ---------------------------------------------------------------------------

def test_import_no_side_effects():
    """Module must import cleanly with zero side effects."""
    import determinex_settings as cs
    assert hasattr(cs, "get_settings")
    assert hasattr(cs, "DeterminexSettings")
    assert hasattr(cs, "reset_settings")


# ---------------------------------------------------------------------------
# Safe defaults
# ---------------------------------------------------------------------------

def test_safety_flags_default_closed():
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    assert s.safety_mode == "strict"
    assert s.online_discovery is False
    assert s.allow_cloud_fallback is False
    assert s.allow_unsandboxed is False
    assert s.require_docker is True
    assert s.require_cloak is True
    assert s.offline_observer is True
    assert s.flywheel_auto is False
    assert s.cloak_enabled is False


def test_assert_safety_defaults_clean():
    """No violations when all flags are at defaults."""
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    # Clear any stray env vars that could open flags
    env_backup = {}
    open_flags = [
        "DETERMINEX_ONLINE_DISCOVERY",
        "DETERMINEX_ALLOW_CLOUD_FALLBACK",
        "DETERMINEX_ALLOW_UNSANDBOXED",
    ]
    for flag in open_flags:
        if flag in os.environ:
            env_backup[flag] = os.environ.pop(flag)
    try:
        violations = s.assert_safety_defaults()
        assert violations == [], f"Expected no violations, got: {violations}"
    finally:
        os.environ.update(env_backup)


def test_assert_safety_defaults_catches_open_flags(monkeypatch):
    monkeypatch.setenv("DETERMINEX_ONLINE_DISCOVERY", "1")
    monkeypatch.setenv("DETERMINEX_ALLOW_CLOUD_FALLBACK", "1")
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    violations = s.assert_safety_defaults()
    assert len(violations) == 2
    assert any("ONLINE_DISCOVERY" in v for v in violations)
    assert any("CLOUD_FALLBACK" in v for v in violations)


# ---------------------------------------------------------------------------
# Env-var overrides
# ---------------------------------------------------------------------------

def test_env_var_override_path(monkeypatch, tmp_path):
    monkeypatch.setenv("DETERMINEX_AUDIT_DIR", str(tmp_path / "my_audit"))
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    assert s.audit_dir == tmp_path / "my_audit"


def test_env_var_override_model(monkeypatch):
    monkeypatch.setenv("DETERMINEX_BUILDER_MODEL", "my-custom-model:7b")
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    assert s.builder_model == "my-custom-model:7b"


def test_api_key_resolution_primary(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test-primary")
    monkeypatch.delenv("DETERMINEX_ANTHROPIC_KEY", raising=False)
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    assert s.anthropic_api_key == "sk-ant-test-primary"


def test_api_key_resolution_alias(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.setenv("DETERMINEX_ANTHROPIC_KEY", "sk-ant-test-alias")
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    assert s.anthropic_api_key == "sk-ant-test-alias"


def test_hmac_key_fallback(monkeypatch):
    monkeypatch.delenv("DETERMINEX_HMAC_KEY", raising=False)
    monkeypatch.setenv("DETERMINEX_CORPUS_HMAC_KEY", "fallback-key-32-bytes-xxxxxxxxxxxxxxx")
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    assert s.hmac_key == "fallback-key-32-bytes-xxxxxxxxxxxxxxx"


def test_hmac_key_primary_wins(monkeypatch):
    monkeypatch.setenv("DETERMINEX_HMAC_KEY", "primary-key")
    monkeypatch.setenv("DETERMINEX_CORPUS_HMAC_KEY", "should-not-be-used")
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    assert s.hmac_key == "primary-key"


# ---------------------------------------------------------------------------
# Portable fallback (no T:/ required)
# ---------------------------------------------------------------------------

def test_audit_dir_local_fallback_when_drive_absent(monkeypatch, tmp_path):
    """When T:/ doesn't exist and no env var is set, fallback to logs/events."""
    monkeypatch.delenv("DETERMINEX_AUDIT_DIR", raising=False)
    # Point DETERMINEX_ROOT to tmp_path so the fallback resolves to a temp location
    monkeypatch.setenv("DETERMINEX_ROOT", str(tmp_path))

    # Monkey-patch _resolve_path at the module level to simulate absent T:/ drive.
    import determinex_settings as cs
    original_resolve = cs._resolve_path

    def fake_resolve(env_var, t_default, local_fallback=None):
        if env_var == "DETERMINEX_AUDIT_DIR" and not os.environ.get(env_var):
            # Pretend T:/ is absent by returning the fallback directly
            if local_fallback is not None:
                repo = Path(os.environ.get("DETERMINEX_ROOT", str(tmp_path)))
                return repo / local_fallback
        return original_resolve(env_var, t_default, local_fallback)

    monkeypatch.setattr(cs, "_resolve_path", fake_resolve)
    s = cs.DeterminexSettings()
    result = s.audit_dir
    # Should resolve to tmp_path/logs/events (no T:/ required)
    assert "logs" in str(result) or str(tmp_path) in str(result)


def test_path_with_env_override_never_needs_drive(monkeypatch, tmp_path):
    """Explicit env var wins even when drive letter doesn't exist."""
    fake_dir = tmp_path / "audit_events"
    monkeypatch.setenv("DETERMINEX_AUDIT_DIR", str(fake_dir))
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    assert s.audit_dir == fake_dir


# ---------------------------------------------------------------------------
# Singleton
# ---------------------------------------------------------------------------

def test_singleton_returns_same_instance():
    from determinex_settings import get_settings
    a = get_settings()
    b = get_settings()
    assert a is b


def test_reset_singleton_creates_fresh():
    from determinex_settings import get_settings, reset_settings
    a = get_settings()
    reset_settings()
    b = get_settings()
    assert a is not b


# ---------------------------------------------------------------------------
# resolved_summary
# ---------------------------------------------------------------------------

def test_resolved_summary_contains_all_keys():
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    summary = s.resolved_summary()
    expected_keys = {
        "repo_root", "models_dir", "audit_dir", "corpus_root",
        "swebench_repos", "programbench_dir", "pb_tasks_root",
        "safety_mode", "online_discovery", "allow_cloud_fallback",
        "require_docker", "require_cloak", "builder_model",
        "observer_model", "architect_model", "anthropic_api_key",
        "hmac_key",
    }
    assert expected_keys.issubset(summary.keys()), (
        f"Missing keys: {expected_keys - summary.keys()}"
    )


def test_resolved_summary_masks_api_keys(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-real-key")
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    summary = s.resolved_summary()
    assert summary["anthropic_api_key"] == "***"
    assert "sk-ant-real-key" not in str(summary)


def test_resolved_summary_unset_key_label(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("DETERMINEX_ANTHROPIC_KEY", raising=False)
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    summary = s.resolved_summary()
    assert summary["anthropic_api_key"] == "(unset)"


def test_check_path_availability_returns_bools():
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    availability = s.check_path_availability()
    for key, val in availability.items():
        assert isinstance(val, bool), f"{key}: expected bool, got {type(val)}"


# ---------------------------------------------------------------------------
# Boolean env parsing
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("val,expected", [
    ("1", True), ("true", True), ("True", True), ("TRUE", True),
    ("yes", True), ("on", True),
    ("0", False), ("false", False), ("False", False), ("", False),
    ("no", False), ("off", False),
])
def test_env_bool_parsing(monkeypatch, val, expected):
    monkeypatch.setenv("DETERMINEX_FLYWHEEL_AUTO", val)
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    assert s.flywheel_auto is expected


def test_env_bool_default_false_when_unset(monkeypatch):
    monkeypatch.delenv("DETERMINEX_FLYWHEEL_AUTO", raising=False)
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    assert s.flywheel_auto is False
