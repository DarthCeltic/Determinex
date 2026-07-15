/// model_puller.rs — Automated Ollama model downloader with progress tracking
///
/// Ensures all base models required by the Determinex Hive Mind are pulled into
/// the local Ollama registry before the bootstrap factory runs.
///
/// The current Determinex architecture requires these base models:
///   - qwen2.5-coder:1.5b-instruct  -> Engineer fallback (Tier 0, Builder role)
///   - qwen2.5-coder:3b-instruct    -> local/fast fallback (Oracle/Architect)
///   - qwen2.5-coder:7b-instruct    -> larger local reasoning fallback
///   - qwen2.5-coder:14b-instruct   -> Leviathan (CPU fallback, optional)
///
/// For custom fine-tuned GGUFs (v1.1 models from RunPod), those are handled
/// separately via GitHub Releases download and `ollama create -f Modelfile`.
///
/// Progress is reported via Tauri events so the frontend SetupWizard can
/// render per-model progress bars.
use serde::{Deserialize, Serialize};
use tokio::process::Command;

use crate::hardware;

#[cfg(target_os = "windows")]
fn no_window(cmd: &mut Command) -> &mut Command {
    const CREATE_NO_WINDOW: u32 = 0x0800_0000;
    cmd.creation_flags(CREATE_NO_WINDOW)
}
#[cfg(not(target_os = "windows"))]
fn no_window(cmd: &mut Command) -> &mut Command {
    cmd
}

// ─────────────────────────────────────────────────────────────────────────────
// TYPES
// ─────────────────────────────────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize)]
#[allow(dead_code)]
pub struct ModelPullStatus {
    pub model: String,
    pub status: String, // "already_exists", "pulling", "complete", "failed"
    pub progress: f32,  // 0.0 to 1.0
}

#[derive(Debug, Clone, Serialize)]
pub struct PullSummary {
    pub models_pulled: Vec<String>,
    pub models_existing: Vec<String>,
    pub models_failed: Vec<String>,
    pub tier_resolved: String,
    pub vram_budget_mb: u64,
}

// ─────────────────────────────────────────────────────────────────────────────
// MODEL RESOLUTION
// ─────────────────────────────────────────────────────────────────────────────

/// Determine which base models need to be present for the detected hardware tier.
///
/// The tier system from hardware.rs determines the Engineer model size.
/// We always need the small models (1.5b for Builder, 3b for Observer).
/// The tier determines whether we also pull the 7b and/or 14b.
fn required_models_for_budget(budget_mb: u64) -> Vec<&'static str> {
    let mut models = vec![
        "qwen2.5-coder:1.5b-instruct", // Builder fallback - always needed
        "qwen2.5-coder:3b-instruct",   // local/fast - always needed
    ];

    if budget_mb >= 7000 {
        models.push("qwen2.5-coder:7b-instruct"); // larger reasoning fallback
    }

    // The 14b Leviathan runs on CPU, so it's optional but useful.
    // Only pull if the system has 16GB+ RAM (not VRAM).
    // For now, skip it to save download time. Users can add it later.

    models
}

// ─────────────────────────────────────────────────────────────────────────────
// OLLAMA INTERACTION
// ─────────────────────────────────────────────────────────────────────────────

/// Parse `ollama list` output to get currently installed model tags.
async fn get_installed_models() -> Result<Vec<String>, String> {
    let output = no_window(Command::new("ollama").arg("list"))
        .output()
        .await
        .map_err(|e| format!("Failed to run `ollama list`: {}", e))?;

    if !output.status.success() {
        // If Ollama is running but has no models, it might still return success
        // with an empty list. A non-zero exit is a real error.
        let stderr = String::from_utf8_lossy(&output.stderr);
        return Err(format!("`ollama list` failed: {}", stderr.trim()));
    }

    let stdout = String::from_utf8_lossy(&output.stdout);
    let tags: Vec<String> = stdout
        .lines()
        .skip(1) // Header line: "NAME   ID   SIZE   MODIFIED"
        .filter_map(|line| {
            let tag = line.split_whitespace().next()?;
            if tag.is_empty() {
                None
            } else {
                Some(tag.to_string())
            }
        })
        .collect();

    log::info!("[MODEL-PULLER] Installed models: {:?}", tags);

    Ok(tags)
}

/// Check if a model tag (e.g. "qwen2.5-coder:7b-instruct") is already installed.
/// Allows Ollama quantization suffixes while avoiding bare-tag/instruct drift.
fn model_is_installed(tag: &str, installed: &[String]) -> bool {
    installed.iter().any(|installed_tag| {
        installed_tag == tag
            || installed_tag.starts_with(&format!("{}:", tag))
    })
}

/// Pull a single model via `ollama pull <tag>`.
///
/// This blocks until the pull is complete. Ollama handles the download
/// internally with its own progress reporting to stderr.
async fn pull_model(tag: &str) -> Result<(), String> {
    log::info!("[MODEL-PULLER] Pulling model: {}", tag);

    let output = no_window(Command::new("ollama").args(["pull", tag]))
        .output()
        .await
        .map_err(|e| format!("Failed to run `ollama pull {}`: {}", tag, e))?;

    if output.status.success() {
        log::info!("[MODEL-PULLER] Successfully pulled: {}", tag);
        Ok(())
    } else {
        let stderr = String::from_utf8_lossy(&output.stderr);
        let stdout = String::from_utf8_lossy(&output.stdout);
        Err(format!(
            "`ollama pull {}` failed (exit {:?}).\nstdout: {}\nstderr: {}",
            tag,
            output.status.code(),
            stdout.trim(),
            stderr.trim()
        ))
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// PUBLIC API
// ─────────────────────────────────────────────────────────────────────────────

/// Master entry point: given a pre-resolved hardware config, pull any missing base models.
///
/// Takes the already-probed budget and config from ipc_bootstrap to avoid a redundant
/// second nvidia-smi call (the double-logging problem when called after initialize_system
/// already probed hardware at steps 2-3).
pub async fn ensure_models_ready_with_config(
    budget_mb: u64,
    config: &hardware::DeterminexConfig,
) -> Result<PullSummary, String> {
    log::info!(
        "[MODEL-PULLER] VRAM budget: {}MB → tier engineer={} num_ctx={}",
        budget_mb,
        config.engineer_model,
        config.num_ctx
    );

    // 1. Determine required models
    let required = required_models_for_budget(budget_mb);

    // 3. Check what's already installed
    let installed = get_installed_models().await.unwrap_or_default();

    let mut models_pulled = Vec::new();
    let mut models_existing = Vec::new();
    let mut models_failed = Vec::new();

    // 4. Pull each missing model
    for tag in &required {
        if model_is_installed(tag, &installed) {
            log::info!("[MODEL-PULLER] Already installed: {}", tag);
            models_existing.push(tag.to_string());
            continue;
        }

        match pull_model(tag).await {
            Ok(()) => models_pulled.push(tag.to_string()),
            Err(e) => {
                log::error!("[MODEL-PULLER] Failed to pull {}: {}", tag, e);
                models_failed.push(tag.to_string());
            }
        }
    }

    let tier_desc = format!(
        "engineer={} ctx={} vram={}MB",
        config.engineer_model, config.num_ctx, budget_mb
    );

    Ok(PullSummary {
        models_pulled,
        models_existing,
        models_failed,
        tier_resolved: tier_desc,
        vram_budget_mb: budget_mb,
    })
}

/// Tauri IPC command — exposed to the frontend Setup Wizard.
/// Probes hardware itself for standalone use (outside of initialize_system).
#[tauri::command]
pub async fn pull_required_models() -> Result<PullSummary, String> {
    let budget_mb = hardware::poll_vram_budget()?;
    let config = hardware::calculate_tier(budget_mb)?;
    ensure_models_ready_with_config(budget_mb, &config).await
}

// ─────────────────────────────────────────────────────────────────────────────
// ADVANCED / CUSTOM MODEL SELECTION
// ─────────────────────────────────────────────────────────────────────────────
//
// The tier system above (and hardware::available_tiers_for_budget) covers the
// "just works" path. These two commands are the escape hatch for everyone
// else: someone with 100GB of VRAM who wants to load up on much bigger
// experts, someone who already has a favorite fine-tune, or someone who wants
// whatever's new on HuggingFace this week that isn't in any hardcoded list.
// Both are deliberately generic -- neither one knows or cares what model it's
// fetching, unlike the DSL fine-tunes in bootstrap.rs which are specific,
// named, versioned entities.

/// Pull any Ollama-hosted model tag the user asks for, verbatim -- e.g.
/// "llama3.3:70b", "deepseek-coder-v2:236b", or literally anything on
/// ollama.com/library. No allowlist: if Ollama's registry has it, this can
/// fetch it. Errors surface Ollama's own message (e.g. "model not found").
#[tauri::command]
pub async fn pull_custom_model(tag: String) -> Result<PullSummary, String> {
    let trimmed = tag.trim();
    if trimmed.is_empty() {
        return Err("Model tag cannot be empty.".to_string());
    }

    let installed = get_installed_models().await.unwrap_or_default();
    if model_is_installed(trimmed, &installed) {
        return Ok(PullSummary {
            models_pulled: vec![],
            models_existing: vec![trimmed.to_string()],
            models_failed: vec![],
            tier_resolved: "custom".to_string(),
            vram_budget_mb: hardware::poll_vram_budget().unwrap_or(0),
        });
    }

    match pull_model(trimmed).await {
        Ok(()) => Ok(PullSummary {
            models_pulled: vec![trimmed.to_string()],
            models_existing: vec![],
            models_failed: vec![],
            tier_resolved: "custom".to_string(),
            vram_budget_mb: hardware::poll_vram_budget().unwrap_or(0),
        }),
        Err(e) => Ok(PullSummary {
            models_pulled: vec![],
            models_existing: vec![],
            models_failed: vec![format!("{}: {}", trimmed, e)],
            tier_resolved: "custom".to_string(),
            vram_budget_mb: hardware::poll_vram_budget().unwrap_or(0),
        }),
    }
}

/// Download an arbitrary GGUF (HuggingFace or any other direct URL) and
/// register it in Ollama under `tag`. This is how someone brings a model
/// that was never going to make it into any hardcoded list -- their own
/// fine-tune, something new from HF, a quantization variant, whatever.
///
/// The GGUF is cached under DETERMINEX_MODELS_DIR/custom/<safe-tag>.gguf so a
/// second registration (or a re-run after `ollama rm`) doesn't re-download.
#[tauri::command]
pub async fn register_custom_gguf(url: String, tag: String, num_ctx: u32) -> Result<String, String> {
    let tag = tag.trim();
    let url = url.trim();
    if tag.is_empty() || url.is_empty() {
        return Err("Both a model tag and a GGUF URL are required.".to_string());
    }

    let models_dir = std::env::var("DETERMINEX_MODELS_DIR").unwrap_or_else(|_| {
        let home = std::env::var("USERPROFILE")
            .or_else(|_| std::env::var("HOME"))
            .unwrap_or_else(|_| ".".to_string());
        format!("{}/determinex-models", home)
    });
    let safe_name = tag.replace([':', '/'], "_");
    let gguf_path = std::path::PathBuf::from(models_dir)
        .join("custom")
        .join(format!("{}.gguf", safe_name));

    if !gguf_path.exists() {
        log::info!("[MODEL-PULLER] Downloading custom GGUF for {} from {}", tag, url);
        crate::bootstrap::stream_download(url, &gguf_path).await?;
    } else {
        log::info!("[MODEL-PULLER] Custom GGUF for {} already cached at {:?}", tag, gguf_path);
    }

    let modelfile_content = format!(
        "FROM {}\nPARAMETER num_ctx {}\nPARAMETER temperature 0\n",
        gguf_path.to_string_lossy(),
        num_ctx.max(512)
    );
    let temp_path = std::env::temp_dir().join(format!("determinex_custom_modelfile_{}.txt", safe_name));
    std::fs::write(&temp_path, &modelfile_content)
        .map_err(|e| format!("Failed to write Modelfile for {}: {}", tag, e))?;

    let out = crate::windows_process::no_window_tokio(
        Command::new("ollama").args(["create", tag, "-f", temp_path.to_str().unwrap_or("")]),
    )
    .output()
    .await;

    let _ = std::fs::remove_file(&temp_path);
    let out = out.map_err(|e| format!("Failed to spawn `ollama create {}`: {}", tag, e))?;

    if out.status.success() {
        Ok(format!("Registered {} from {}", tag, gguf_path.display()))
    } else {
        let stderr = String::from_utf8_lossy(&out.stderr);
        Err(format!("`ollama create {}` failed: {}", tag, stderr.trim()))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn required_models_use_configured_instruct_tags() {
        assert_eq!(
            required_models_for_budget(4000),
            vec!["qwen2.5-coder:1.5b-instruct", "qwen2.5-coder:3b-instruct"]
        );
        assert_eq!(
            required_models_for_budget(8000),
            vec![
                "qwen2.5-coder:1.5b-instruct",
                "qwen2.5-coder:3b-instruct",
                "qwen2.5-coder:7b-instruct",
            ]
        );
    }

    #[test]
    fn model_install_detection_does_not_treat_bare_tag_as_instruct() {
        let installed = vec!["qwen2.5-coder:1.5b-instruct".to_string()];

        assert!(model_is_installed("qwen2.5-coder:1.5b-instruct", &installed));
        assert!(!model_is_installed("qwen2.5-coder:1.5b", &installed));
    }
}
