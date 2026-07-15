use crate::hardware::DeterminexConfig;
/// bootstrap.rs — First-run Determinex model factory
///
/// Programmatically constructs and registers the three Ollama models required by the
/// MoA pipeline. Each model is built by writing a temporary Modelfile to the OS temp
/// directory, calling `ollama create`, then cleaning up the temp file.
///
/// If a GGUF isn't present locally (the common case for anyone who isn't the
/// original author's own dev box), it's streamed down from the published
/// HuggingFace repos first. This is the actual first-run path for a real user --
/// without it, these three models can never be registered on any machine that
/// doesn't already have T:/determinex-models populated from a private training run.
///
/// Execution is sequential: Sentinel → Engineer → Observer. Each `ollama create` call
/// blocks until the model is fully built and registered in the local Ollama registry.
/// On a typical machine this takes 10–30 seconds per model (GGUF quantisation + indexing),
/// plus however long the download takes for a fresh install (models are 1.5-7 GB).
///
/// Uses `tokio::process::Command` throughout so the async Tauri command handler is not
/// stalled on the blocking `std::process::Command` API.
use futures_util::StreamExt;
use tokio::io::AsyncWriteExt;
use tokio::process::Command;

/// See ollama_installer.rs's `no_window` -- same rationale, duplicated here to
/// avoid a cross-module dependency for one helper. Windows allocates a visible
/// console for any spawned console-subsystem process unless told not to.
#[cfg(target_os = "windows")]
fn no_window(cmd: &mut Command) -> &mut Command {
    const CREATE_NO_WINDOW: u32 = 0x0800_0000;
    cmd.creation_flags(CREATE_NO_WINDOW)
}
#[cfg(not(target_os = "windows"))]
fn no_window(cmd: &mut Command) -> &mut Command {
    cmd
}

/// Target model names that the Hive Mind Orchestrator (litellm_config.yaml) expects.
/// These MUST match the model_name values under determinex.roles in litellm_config.yaml.
const ENGINEER_TAG: &str = "determinex-engineer-v11-dsl"; // Builder:   Qwen2.5-Coder-1.5B DSL v11
const OBSERVER_TAG: &str = "determinex-observer-v6-dsl"; // Monitor:   Llama-3.2-3B DSL v6
const SENTINEL_TAG: &str = "determinex-sentinel-v5-dsl"; // Architect: Mistral-7B DSL v5

/// One entry per model: Ollama tag, relative GGUF path under DETERMINEX_MODELS_DIR,
/// context window, and where to fetch the GGUF from if it isn't there yet.
struct ModelSpec {
    tag: &'static str,
    relative_gguf_path: &'static str,
    num_ctx: &'static str,
    download_url: &'static str,
}

const MODEL_SPECS: &[ModelSpec] = &[
    ModelSpec {
        tag: ENGINEER_TAG,
        relative_gguf_path: "versions/engineer/v11-dsl/determinex-engineer-v11-dsl.gguf",
        num_ctx: "4096",
        download_url: "https://huggingface.co/darthceltic85/determinex-engineer/resolve/main/determinex-engineer-v11-dsl.gguf",
    },
    ModelSpec {
        tag: OBSERVER_TAG,
        relative_gguf_path: "versions/observer/v6-dsl/determinex-observer-v6-dsl.gguf",
        num_ctx: "4096",
        download_url: "https://huggingface.co/darthceltic85/determinex-observer-llama-3.2/resolve/main/determinex-observer-v6-dsl.gguf",
    },
    ModelSpec {
        tag: SENTINEL_TAG,
        relative_gguf_path: "versions/sentinel/v5-dsl/determinex-sentinel-v5-dsl.gguf",
        num_ctx: "4096",
        download_url: "https://huggingface.co/darthceltic85/determinex-sentinel/resolve/main/determinex-sentinel-v5-dsl.gguf",
    },
];

/// Stream a (potentially multi-gigabyte) file from `url` to `dest`, writing chunks
/// as they arrive rather than buffering the whole response in memory -- the
/// Sentinel GGUF alone is 7+ GB, which a buffer-then-write approach would hold
/// entirely in RAM before touching disk.
pub(crate) async fn stream_download(url: &str, dest: &std::path::Path) -> Result<(), String> {
    if let Some(parent) = dest.parent() {
        tokio::fs::create_dir_all(parent)
            .await
            .map_err(|e| format!("Failed to create directory {:?}: {}", parent, e))?;
    }

    let tmp_dest = dest.with_extension("gguf.partial");

    let client = reqwest::Client::builder()
        .timeout(std::time::Duration::from_secs(3600)) // large model, slow connections
        .build()
        .map_err(|e| format!("Failed to create HTTP client: {}", e))?;

    let response = client
        .get(url)
        .send()
        .await
        .map_err(|e| format!("Download request failed: {}", e))?;

    if !response.status().is_success() {
        return Err(format!(
            "Download failed with HTTP {}: {}",
            response.status(),
            url
        ));
    }

    let total_size = response.content_length().unwrap_or(0);
    let mut file = tokio::fs::File::create(&tmp_dest)
        .await
        .map_err(|e| format!("Failed to create {:?}: {}", tmp_dest, e))?;

    let mut stream = response.bytes_stream();
    let mut downloaded: u64 = 0;
    let mut last_logged_pct = 0u64;

    while let Some(chunk) = stream.next().await {
        let chunk = chunk.map_err(|e| format!("Download stream error: {}", e))?;
        file.write_all(&chunk)
            .await
            .map_err(|e| format!("Failed to write {:?}: {}", tmp_dest, e))?;
        downloaded += chunk.len() as u64;

        if total_size > 0 {
            let pct = downloaded * 100 / total_size;
            if pct >= last_logged_pct + 10 {
                last_logged_pct = pct;
                log::info!(
                    "[BOOTSTRAP] Downloading {:?}: {}% ({} / {} MB)",
                    dest.file_name().unwrap_or_default(),
                    pct,
                    downloaded / (1024 * 1024),
                    total_size / (1024 * 1024)
                );
            }
        }
    }

    file.flush()
        .await
        .map_err(|e| format!("Failed to flush {:?}: {}", tmp_dest, e))?;
    drop(file);

    tokio::fs::rename(&tmp_dest, dest)
        .await
        .map_err(|e| format!("Failed to finalize download to {:?}: {}", dest, e))?;

    Ok(())
}

/// Registers the three Determinex DSL model tags in Ollama.
///
/// Model tags MUST match litellm_config.yaml role assignments:
///   engineer → determinex-engineer-v11-dsl (Qwen2.5-Coder-1.5B, DSL v11)
///   observer → determinex-observer-v6-dsl  (Llama-3.2-3B, DSL v6)
///   sentinel → determinex-sentinel-v5-dsl  (Mistral-7B, DSL v5)
///
/// The Modelfiles live in <repo>/modelfiles/ and reference GGUFs from DETERMINEX_MODELS_DIR.
/// If a GGUF is not present locally, it's downloaded from HuggingFace first. Only if
/// that download itself fails does this step skip gracefully with a warning.
pub async fn run_first_setup(_config: &DeterminexConfig) -> Result<(), String> {
    // ── Step 0: Check if models are already registered (fast path) ────────────
    // Idempotent: if all three tags exist, return immediately — no Docker check,
    // no GGUF scan, nothing. This is the common case on subsequent boots.
    let output = no_window(&mut Command::new("ollama").arg("list"))
        .output()
        .await
        .map_err(|e| format!("ollama list failed: {}", e))?;
    let installed = String::from_utf8_lossy(&output.stdout).to_string();

    let has_all_tags = installed.contains(ENGINEER_TAG)
        && installed.contains(OBSERVER_TAG)
        && installed.contains(SENTINEL_TAG);

    if has_all_tags {
        log::info!(
            "[BOOTSTRAP] All DSL-versioned models already registered ({}, {}, {}) — skipping.",
            ENGINEER_TAG,
            OBSERVER_TAG,
            SENTINEL_TAG
        );
        return Ok(());
    }

    // ── Step 1: Docker daemon check (optional — sidecar uses local compiler) ──
    // Docker is no longer required for sidecar-mode Determinex. Log a warning if
    // it's absent but do not abort — the build loop uses local rustc/go/python.
    let docker_check = tokio::time::timeout(
        std::time::Duration::from_secs(5),
        no_window(Command::new("docker").args(["info", "--format", "{{.ServerVersion}}"])).output(),
    )
    .await;
    match docker_check {
        Ok(Ok(ref out)) if out.status.success() => {
            let ver = String::from_utf8_lossy(&out.stdout);
            log::info!("[BOOTSTRAP] Docker daemon OK (version {})", ver.trim());
        }
        _ => {
            log::warn!(
                "[BOOTSTRAP] Docker not available — sidecar mode uses local compiler, continuing."
            );
        }
    }

    // ── Step 2: Locate the DETERMINEX_MODELS_DIR ─────────────────────────────────
    // Reads DETERMINEX_MODELS_DIR from the environment (set in .env or system env).
    // Falls back to ~/determinex-models so the system degrades gracefully.
    let models_dir = std::env::var("DETERMINEX_MODELS_DIR").unwrap_or_else(|_| {
        let home = std::env::var("USERPROFILE")
            .or_else(|_| std::env::var("HOME"))
            .unwrap_or_else(|_| ".".to_string());
        format!("{}/determinex-models", home)
    });
    let models_path = std::path::PathBuf::from(&models_dir);

    log::info!("[BOOTSTRAP] DETERMINEX_MODELS_DIR = {:?}", models_path);

    // ── Step 3: Build each missing model from its versioned GGUF ──────────────
    for spec in MODEL_SPECS {
        if installed.contains(spec.tag) {
            log::info!("[BOOTSTRAP] {} already registered — skipping.", spec.tag);
            continue;
        }

        let gguf_path = models_path.join(spec.relative_gguf_path);

        if !gguf_path.exists() {
            log::info!(
                "[BOOTSTRAP] GGUF not found for {} at {:?} — downloading from {}",
                spec.tag,
                gguf_path,
                spec.download_url
            );
            if let Err(e) = stream_download(spec.download_url, &gguf_path).await {
                log::warn!(
                    "[BOOTSTRAP] Download failed for {}: {}. \
                     Skipping — you can retry from the Setup Wizard, or place the GGUF \
                     at {:?} manually.",
                    spec.tag,
                    e,
                    gguf_path
                );
                continue;
            }
            log::info!("[BOOTSTRAP] Downloaded {} to {:?}", spec.tag, gguf_path);
        }

        let gguf_str = gguf_path.to_string_lossy();
        let modelfile_content = format!(
            "FROM {}\nPARAMETER num_ctx {}\nPARAMETER temperature 0\n",
            gguf_str, spec.num_ctx
        );

        let safe_name = spec.tag.replace(':', "_").replace('/', "_");
        let temp_path = std::env::temp_dir().join(format!("determinex_modelfile_{}.txt", safe_name));

        std::fs::write(&temp_path, &modelfile_content)
            .map_err(|e| format!("Failed to write Modelfile for {}: {}", spec.tag, e))?;

        log::info!("[BOOTSTRAP] Registering {} FROM {:?}", spec.tag, gguf_path);

        let out = no_window(Command::new("ollama").args(["create", spec.tag, "-f", temp_path.to_str().unwrap_or("")]))
            .output()
            .await
            .map_err(|e| format!("Failed to spawn `ollama create {}`: {}", spec.tag, e));

        let _ = std::fs::remove_file(&temp_path);
        let out = out?;

        if out.status.success() {
            log::info!("[BOOTSTRAP] Successfully registered: {}", spec.tag);
        } else {
            let stderr = String::from_utf8_lossy(&out.stderr);
            log::warn!(
                "[BOOTSTRAP] `ollama create {}` failed: {} — continuing to next model.",
                spec.tag,
                stderr.trim()
            );
        }
    }

    Ok(())
}
