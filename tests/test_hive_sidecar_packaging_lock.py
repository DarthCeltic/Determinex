from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_hive_sidecar_builder_bundles_litellm_and_tiktoken_runtime_data():
    source = (ROOT / "bundler" / "build_hive_sidecar.py").read_text(encoding="utf-8")

    assert '"--collect-data", "litellm"' in source
    assert '"--hidden-import", "tiktoken_ext"' in source
    assert '"--hidden-import", "tiktoken_ext.openai_public"' in source


def test_hive_sidecar_runtime_modules_honor_determinex_root_env():
    modules = [
        ROOT / "scripts" / "hive" / "api_client.py",
        ROOT / "scripts" / "hive" / "budget.py",
        ROOT / "scripts" / "hive" / "compiler.py",
        ROOT / "scripts" / "hive" / "executor.py",
        ROOT / "scripts" / "hive" / "forge_daemon.py",
        ROOT / "scripts" / "hive" / "offline_observer.py",
    ]

    for module in modules:
        source = module.read_text(encoding="utf-8")
        assert "DETERMINEX_ROOT" in source, module
