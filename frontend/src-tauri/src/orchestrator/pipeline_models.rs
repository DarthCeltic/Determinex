/// orchestrator/pipeline_models.rs — Reads litellm_config.yaml and resolves Ollama and Cloud model tags.
use std::fmt;

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum ModelRoute {
    Ollama { model: String },
    OpenRouter { model: String },
    OpenAI { model: String },
    Anthropic { model: String },
    Gemini { model: String },
    DeepSeek { model: String },
    Mistral { model: String },
    Groq { model: String },
}

impl fmt::Display for ModelRoute {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            ModelRoute::Ollama { model } => write!(f, "Ollama({})", model),
            ModelRoute::OpenRouter { model } => write!(f, "OpenRouter({})", model),
            ModelRoute::OpenAI { model } => write!(f, "OpenAI({})", model),
            ModelRoute::Anthropic { model } => write!(f, "Anthropic({})", model),
            ModelRoute::Gemini { model } => write!(f, "Gemini({})", model),
            ModelRoute::DeepSeek { model } => write!(f, "DeepSeek({})", model),
            ModelRoute::Mistral { model } => write!(f, "Mistral({})", model),
            ModelRoute::Groq { model } => write!(f, "Groq({})", model),
        }
    }
}

pub struct PipelineModels {
    pub sentinel: ModelRoute,
    pub engineer: ModelRoute,
    pub observer: ModelRoute,
}

impl PipelineModels {
    const DEFAULT_SENTINEL: &'static str = "determinex-sentinel-v3";
    const DEFAULT_ENGINEER: &'static str = "determinex-engineer-v10-dsl";
    const DEFAULT_OBSERVER: &'static str = "determinex-observer-v5-dsl";

    pub fn load() -> Self {
        let root = Self::project_root();
        let config = match std::fs::read_to_string(root.join("litellm_config.yaml")) {
            Ok(s) => s,
            Err(e) => {
                log::warn!(
                    "[ORCHESTRATOR] litellm_config.yaml not readable ({e}) — using defaults"
                );
                return Self::defaults();
            }
        };
        let sentinel = Self::resolve_role(&config, "architect").unwrap_or_else(|| {
            log::warn!(
                "[ORCHESTRATOR] 'architect' role unresolvable — falling back to {}",
                Self::DEFAULT_SENTINEL
            );
            ModelRoute::Ollama { model: Self::DEFAULT_SENTINEL.to_string() }
        });
        let engineer = Self::resolve_role(&config, "builder").unwrap_or_else(|| {
            log::warn!(
                "[ORCHESTRATOR] 'builder' role unresolvable — falling back to {}",
                Self::DEFAULT_ENGINEER
            );
            ModelRoute::Ollama { model: Self::DEFAULT_ENGINEER.to_string() }
        });
        let observer = Self::resolve_role(&config, "monitor").unwrap_or_else(|| {
            log::warn!(
                "[ORCHESTRATOR] 'monitor' role unresolvable — falling back to {}",
                Self::DEFAULT_OBSERVER
            );
            ModelRoute::Ollama { model: Self::DEFAULT_OBSERVER.to_string() }
        });
        log::info!("[ORCHESTRATOR] Role models: architect={}, builder={}, monitor={}", sentinel, engineer, observer);
        Self {
            sentinel,
            engineer,
            observer,
        }
    }

    pub fn defaults() -> Self {
        Self {
            sentinel: ModelRoute::Ollama { model: Self::DEFAULT_SENTINEL.to_string() },
            engineer: ModelRoute::Ollama { model: Self::DEFAULT_ENGINEER.to_string() },
            observer: ModelRoute::Ollama { model: Self::DEFAULT_OBSERVER.to_string() },
        }
    }

    /// Resolve one role from litellm_config.yaml to a ModelRoute.
    pub fn resolve_role(config: &str, role: &str) -> Option<ModelRoute> {
        use regex::Regex;

        let role_re =
            Regex::new(&format!(r"(?m)^\s+{}:\s+([^#\s\n]+)", regex::escape(role))).ok()?;
        let model_name = role_re.captures(config)?.get(1)?.as_str().to_string();

        if !model_name.contains('/') {
            return Some(ModelRoute::Ollama { model: model_name });
        }

        let search = format!("model_name: {model_name}");
        let start = config.find(&search)?;
        let rest = &config[start..];
        let block_end = rest[1..]
            .find("- model_name:")
            .map(|p| p + 1)
            .unwrap_or(rest.len());
        let block = &rest[..block_end];

        let model_re = Regex::new(r"(?m)model:\s+([^\s\n]+)").ok()?;
        let tag = model_re.captures(block)?.get(1)?.as_str().to_string();

        if tag.starts_with("ollama/") {
            Some(ModelRoute::Ollama { model: tag.replace("ollama/", "") })
        } else if tag.starts_with("openrouter/") {
            // openrouter/<provider>/<model-id>:free → keep full provider/model path after openrouter/
            Some(ModelRoute::OpenRouter { model: tag.replace("openrouter/", "") })
        } else if tag.starts_with("openai/") {
            Some(ModelRoute::OpenAI { model: tag.replace("openai/", "") })
        } else if tag.starts_with("anthropic/") {
            Some(ModelRoute::Anthropic { model: tag.replace("anthropic/", "") })
        } else if tag.starts_with("gemini/") {
            Some(ModelRoute::Gemini { model: tag.replace("gemini/", "") })
        } else if tag.starts_with("deepseek/") {
            Some(ModelRoute::DeepSeek { model: tag.replace("deepseek/", "") })
        } else if tag.starts_with("mistral/") {
            Some(ModelRoute::Mistral { model: tag.replace("mistral/", "") })
        } else if tag.starts_with("groq/") {
            Some(ModelRoute::Groq { model: tag.replace("groq/", "") })
        } else {
            // fallback
            if tag.contains("/") {
                Some(ModelRoute::Ollama { model: tag.split('/').last().unwrap().to_string() })
            } else {
                Some(ModelRoute::Ollama { model: tag })
            }
        }
    }

    /// Same root-finding logic as ipc_hive.rs::project_root().
    fn project_root() -> std::path::PathBuf {
        if let Ok(root) = std::env::var("DETERMINEX_ROOT") {
            return std::path::PathBuf::from(root);
        }
        if let Ok(exe) = std::env::current_exe() {
            let mut candidate = exe.parent().map(|p| p.to_path_buf()).unwrap_or_default();
            for _ in 0..8 {
                if candidate.join("scripts").join("determinex_hive.py").exists() {
                    return candidate;
                }
                match candidate.parent() {
                    Some(p) => candidate = p.to_path_buf(),
                    None => break,
                }
            }
        }
        let fallback = std::env::current_dir().unwrap_or_else(|_| std::path::PathBuf::from("."));
        log::warn!(
            "[ORCHESTRATOR] project_root() fell back to '{}' — set DETERMINEX_ROOT to suppress",
            fallback.display()
        );
        fallback
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn cloud_roles_resolve_to_provider_routes_instead_of_none() {
        let config = r#"
model_list:
  - model_name: cloud/deepseek-chat
    litellm_params:
      model: deepseek/deepseek-chat
      api_key: os.environ/DEEPSEEK_API_KEY
      api_base: https://api.deepseek.com
  - model_name: cloud/mistral-large
    litellm_params:
      model: mistral/mistral-large-latest
      api_key: os.environ/MISTRAL_API_KEY
  - model_name: cloud/groq-llama
    litellm_params:
      model: groq/llama-3.3-70b-versatile
      api_key: os.environ/GROQ_API_KEY
determinex:
  roles:
    architect: cloud/deepseek-chat
    builder: cloud/mistral-large
    monitor: cloud/groq-llama
"#;

        assert_eq!(
            PipelineModels::resolve_role(config, "architect"),
            Some(ModelRoute::DeepSeek {
                model: "deepseek-chat".to_string()
            })
        );
        assert_eq!(
            PipelineModels::resolve_role(config, "builder"),
            Some(ModelRoute::Mistral {
                model: "mistral-large-latest".to_string()
            })
        );
        assert_eq!(
            PipelineModels::resolve_role(config, "monitor"),
            Some(ModelRoute::Groq {
                model: "llama-3.3-70b-versatile".to_string()
            })
        );
    }

    #[test]
    fn openrouter_free_models_resolve_correctly() {
        let config = r#"
model_list:
  - model_name: free/qwen3-coder
    litellm_params:
      model: openrouter/qwen/qwen3-coder:free
      api_base: https://openrouter.ai/api/v1
      api_key: os.environ/OPENROUTER_API_KEY
  - model_name: free/llama-3.3-70b
    litellm_params:
      model: openrouter/meta-llama/llama-3.3-70b-instruct:free
      api_base: https://openrouter.ai/api/v1
      api_key: os.environ/OPENROUTER_API_KEY
determinex:
  roles:
    architect: free/qwen3-coder
    builder: free/qwen3-coder
    monitor: free/llama-3.3-70b
"#;

        assert_eq!(
            PipelineModels::resolve_role(config, "architect"),
            Some(ModelRoute::OpenRouter {
                model: "qwen/qwen3-coder:free".to_string()
            })
        );
        assert_eq!(
            PipelineModels::resolve_role(config, "builder"),
            Some(ModelRoute::OpenRouter {
                model: "qwen/qwen3-coder:free".to_string()
            })
        );
        assert_eq!(
            PipelineModels::resolve_role(config, "monitor"),
            Some(ModelRoute::OpenRouter {
                model: "meta-llama/llama-3.3-70b-instruct:free".to_string()
            })
        );
    }
}
