use crate::bootstrap;
use crate::hardware;
use crate::model_puller;
use crate::ollama_installer;
/// ipc_bootstrap.rs — Tauri IPC command for first-run system initialization
///
/// Exposes `initialize_system` as a single async Tauri command that chains
/// through the entire zero-friction setup pipeline:
///
///   0. Check Docker daemon is running (required for compiler sandboxing)
///   1. Ensure Ollama is installed and running (auto-installs if missing)
///   2. Probe available VRAM via the hardware detection chain
///   3. Resolve the hardware tier to a concrete DeterminexConfig
///   4. Pull any missing base models from the Ollama registry
///   5. Build the three Determinex model tags via `ollama create`
///
/// Safe to invoke on subsequent runs — each step is idempotent.
///
/// The frontend Setup Wizard calls this as the master "do everything" command.
/// For granular progress, it can also call the individual IPC commands:
///   - `check_docker_status`    (step 0)
///   - `ensure_ollama_installed` (step 1)
///   - `pull_required_models`   (steps 2-4)
///   - `initialize_system`      (steps 0-5)
use serde::Serialize;
use tokio::process::Command;

#[derive(Debug, Serialize)]
pub struct BootstrapResult {
    pub ollama_status: String,
    pub ollama_version: String,
    pub total_vram_mb: Option<u64>,
    pub vram_budget_mb: u64,
    pub reserved_vram_mb: u64,
    pub hardware_source: String,
    pub hardware_fallback: bool,
    pub tier: String,
    pub models_pulled: Vec<String>,
    pub models_existing: Vec<String>,
    pub models_failed: Vec<String>,
    /// True if Docker daemon is reachable. False means builds will fail at compile time.
    pub docker_ok: bool,
    pub docker_version: String,
}

/// Check whether the Docker daemon is running and reachable.
///
/// Returns (is_running, version_string).
/// Called standalone by the frontend status bar and as step 0 of initialize_system.
#[tauri::command]
pub async fn check_docker_status() -> Result<serde_json::Value, String> {
    let out = Command::new("docker")
        .args(["info", "--format", "{{.ServerVersion}}"])
        .output()
        .await;

    match out {
        Ok(ref o) if o.status.success() => {
            let version = String::from_utf8_lossy(&o.stdout).trim().to_string();
            Ok(serde_json::json!({
                "running": true,
                "version": version,
                "message": format!("Docker daemon OK (v{})", version)
            }))
        }
        Ok(ref o) => {
            let stderr = String::from_utf8_lossy(&o.stderr);
            Ok(serde_json::json!({
                "running": false,
                "version": "",
                "message": format!(
                    "Docker is installed but not running. Start Docker Desktop, then retry.\nError: {}",
                    stderr.trim()
                )
            }))
        }
        Err(ref e) if e.kind() == std::io::ErrorKind::NotFound => Ok(serde_json::json!({
            "running": false,
            "version": "",
            "message": "Docker is not installed. Download Docker Desktop (free) from https://www.docker.com/products/docker-desktop"
        })),
        Err(e) => Ok(serde_json::json!({
            "running": false,
            "version": "",
            "message": format!("Docker check failed: {}", e)
        })),
    }
}

/// Full zero-friction bootstrap: check Docker → install Ollama → detect hardware → pull models → build tags.
///
/// This single command takes a machine from zero to fully operational Determinex.
/// Returns a structured result the Setup Wizard can display.
#[tauri::command]
pub async fn initialize_system() -> Result<BootstrapResult, String> {
    // ── Step 0: Check Docker daemon (optional — sidecar mode uses local compiler) ──
    // Docker is NOT required for sidecar-mode Determinex. The Compiler Oracle
    // invokes rustc/go/python directly from the determinex-hive sidecar binary.
    // We still probe it so the frontend can surface a status indicator, but
    // we no longer abort if it's absent or not running.
    let docker_result = tokio::time::timeout(
        std::time::Duration::from_secs(5),
        check_docker_status(),
    )
    .await
    .unwrap_or_else(|_| Ok(serde_json::json!({
        "running": false, "version": "", "message": "Docker check timed out (daemon not running)"
    })))
    .unwrap_or_else(|_| serde_json::json!({
        "running": false, "version": "", "message": "Docker check failed"
    }));
    let docker_ok = docker_result["running"].as_bool().unwrap_or(false);
    let docker_version = docker_result["version"].as_str().unwrap_or("").to_string();

    // ── Step 1: Ensure Ollama ────────────────────────────────────────────────
    let ollama = ollama_installer::ensure_ollama().await?;
    let ollama_status = format!("{:?}", ollama.status);

    // ── Step 2: Probe VRAM ──────────────────────────────────────────────────
    let hardware_probe = hardware::poll_hardware()?;
    let budget_mb = hardware_probe.vram_budget_mb;

    // ── Step 3: Resolve tier ────────────────────────────────────────────────
    let config = hardware::calculate_tier(budget_mb)?;

    // ── Step 4: Pull base models (pass already-probed config — no second nvidia-smi) ──
    let pull_summary = model_puller::ensure_models_ready_with_config(budget_mb, &config).await?;

    // ── Step 5: Build Determinex model tags ─────────────────────────────────────
    // bootstrap::run_first_setup now also checks Docker again internally as a
    // belt-and-suspenders guard for headless / CLI invocations.
    bootstrap::run_first_setup(&config).await?;

    let tier_desc = format!(
        "engineer={} | num_ctx={} | vram={}MB",
        config.engineer_model, config.num_ctx, budget_mb
    );

    Ok(BootstrapResult {
        ollama_status,
        ollama_version: ollama.version,
        total_vram_mb: hardware_probe.total_vram_mb,
        vram_budget_mb: budget_mb,
        reserved_vram_mb: hardware_probe.reserved_mb,
        hardware_source: hardware_probe.source,
        hardware_fallback: hardware_probe.fallback,
        tier: tier_desc,
        models_pulled: pull_summary.models_pulled,
        models_existing: pull_summary.models_existing,
        models_failed: pull_summary.models_failed,
        docker_ok,
        docker_version,
    })
}

/// Probes the system hardware and returns the VRAM budget and recommended tier without installing anything.
/// Used by the interactive Setup Wizard to display recommendations before proceeding.
#[tauri::command]
pub async fn probe_hardware() -> Result<serde_json::Value, String> {
    let hardware_probe = hardware::poll_hardware()?;
    let budget_mb = hardware_probe.vram_budget_mb;
    let config = hardware::calculate_tier(budget_mb)?;

    Ok(serde_json::json!({
        "total_vram_mb": hardware_probe.total_vram_mb,
        "vram_budget_mb": budget_mb,
        "reserved_vram_mb": hardware_probe.reserved_mb,
        "hardware_source": hardware_probe.source,
        "hardware_fallback": hardware_probe.fallback,
        "recommended_tier": format!("engineer={} | num_ctx={}", config.engineer_model, config.num_ctx)
    }))
}
