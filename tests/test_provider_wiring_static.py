from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_setup_and_config_vault_expose_all_advertised_cloud_key_providers():
    setup = (ROOT / "frontend/src/components/SetupWizard.tsx").read_text(encoding="utf-8")
    settings_context = (ROOT / "frontend/src/contexts/SettingsContext.tsx").read_text(encoding="utf-8")
    settings_modal = (ROOT / "frontend/src/components/modals/SettingsModal.tsx").read_text(encoding="utf-8")
    api = (ROOT / "frontend/src/lib/api.ts").read_text(encoding="utf-8")
    api_keys = (ROOT / "frontend/src-tauri/src/api_keys.rs").read_text(encoding="utf-8")

    for key in [
        "openai_key",
        "anthropic_key",
        "gemini_key",
        "groq_key",
        "deepseek_key",
        "mistral_key",
    ]:
        assert key in setup
        assert key in settings_context
        assert key in api
        assert key in api_keys

    for provider in ["openai", "anthropic", "gemini", "groq", "deepseek", "mistral"]:
        assert provider in settings_modal
        assert provider in api_keys


def test_role_assignment_cloud_options_match_litellm_model_names():
    roles = (ROOT / "frontend/src/components/RoleAssignmentPanel.tsx").read_text(encoding="utf-8")
    config = (ROOT / "litellm_config.yaml").read_text(encoding="utf-8")

    for model_name in [
        "cloud/claude-best",
        "cloud/claude-fast",
        "cloud/deepseek-chat",
        "cloud/deepseek-coder",
        "cloud/gemini-flash",
        "cloud/gpt4o",
        "cloud/mistral-large",
        "cloud/groq-llama",
    ]:
        assert model_name in roles
        assert f"model_name: {model_name}" in config


def test_tauri_pipeline_resolves_cloud_routes_instead_of_falling_back_to_ollama():
    pipeline = (ROOT / "frontend/src-tauri/src/orchestrator/pipeline_models.rs").read_text(encoding="utf-8")
    transport = (ROOT / "frontend/src-tauri/src/orchestrator/transport.rs").read_text(encoding="utf-8")
    orchestrator = (ROOT / "frontend/src-tauri/src/orchestrator/mod.rs").read_text(encoding="utf-8")

    assert "pub enum ModelRoute" in pipeline
    assert "ModelRoute::DeepSeek" in pipeline
    assert "ModelRoute::Mistral" in pipeline
    assert "ModelRoute::Groq" in pipeline
    assert "pub async fn call_model" in transport
    assert "cloud_route_blocked_by_offline_policy" in transport
    assert "call_model(" in orchestrator
    assert "call_ollama(" not in orchestrator
