use regex::Regex;
use reqwest::Client;
use serde::{Deserialize, Serialize};
/// ollama_probe.rs — Ollama Engine Connectivity Detector
///
/// Provides a fast, timeout-bounded health-check against the Ollama API server.
/// The frontend polls this command every few seconds to gate the dashboard UI —
/// if Ollama is not running, the user sees the "Awaiting Engine" lockout overlay.
///
/// Design:
///   - 2-second total timeout (connect + read). Chosen because:
///       • Ollama on localhost typically responds in < 50ms when running.
///       • A 2s wait is imperceptible to a polling loop but avoids hanging
///         when Ollama is absent (TCP RST is instant; DNS/firewall timeouts are not).
///   - Returns `true` on any HTTP 2xx response from `/api/tags`.
///   - Returns `false` on connection error, timeout, or any non-2xx status.
///   - Never propagates an error to the frontend — the caller only cares
///     about reachable/not-reachable, not why it failed.
use std::collections::{HashMap, HashSet};
use std::time::Duration;

const OLLAMA_DEFAULT_BASE: &str = "http://localhost:11434";
const PROBE_TIMEOUT_SECS: u64 = 2;

/// Build the /api/tags URL from an optional user-configured base (see
/// api_keys::get_ollama_base_url), falling back to the localhost default.
fn ollama_tags_url(base_url: Option<&str>) -> String {
    let base = base_url
        .map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .unwrap_or(OLLAMA_DEFAULT_BASE);
    format!("{}/api/tags", base.trim_end_matches('/'))
}

// ─────────────────────────────────────────────────────────────────────────────
// INSTALLED MODEL DISCOVERY
// ─────────────────────────────────────────────────────────────────────────────

#[derive(Debug, Deserialize)]
struct OllamaTagsResponse {
    models: Vec<OllamaModelEntry>,
}

#[derive(Debug, Deserialize)]
struct OllamaModelEntry {
    name: String,
    size: Option<u64>,
    details: Option<OllamaModelDetails>,
}

#[derive(Debug, Deserialize)]
struct OllamaModelDetails {
    parameter_size: Option<String>,
    quantization_level: Option<String>,
}

#[derive(Debug, Serialize)]
pub struct InstalledModel {
    pub id: String,   // ollama model name, e.g. "determinex-engineer-v10-dsl:latest"
    pub name: String, // display name
    pub size_gb: f32,
    pub param_size: String, // e.g. "3B"
    pub quantization: String,
    pub is_determinex: bool, // true if name starts with "determinex-"
}

#[derive(Debug, Serialize)]
struct RoleModelReadiness {
    role: String,
    assignment: String,
    target_model: Option<String>,
    status: String,
    message: String,
}

/// Return the list of models currently installed in Ollama on this rig.
/// Called at startup to populate the model selector dynamically.
#[tauri::command]
pub async fn get_ollama_models(base_url: Option<String>) -> Result<Vec<InstalledModel>, String> {
    let client = Client::builder()
        .timeout(Duration::from_secs(5))
        .pool_max_idle_per_host(0)
        .build()
        .map_err(|e| format!("[OLLAMA-PROBE] client build: {}", e))?;

    let resp = client
        .get(ollama_tags_url(base_url.as_deref()))
        .send()
        .await
        .map_err(|e| format!("[OLLAMA-PROBE] get_ollama_models: {}", e))?;

    let tags: OllamaTagsResponse = resp
        .json()
        .await
        .map_err(|e| format!("[OLLAMA-PROBE] parse tags: {}", e))?;

    let models = tags
        .models
        .into_iter()
        .map(|m| {
            let size_gb = m.size.map(|b| b as f32 / 1_073_741_824.0).unwrap_or(0.0);
            let param_size = m
                .details
                .as_ref()
                .and_then(|d| d.parameter_size.clone())
                .unwrap_or_default();
            let quantization = m
                .details
                .as_ref()
                .and_then(|d| d.quantization_level.clone())
                .unwrap_or_default();
            let bare_name = m.name.split(':').next().unwrap_or(&m.name).to_string();
            let is_determinex = bare_name.starts_with("determinex-");
            let display = if is_determinex {
                // determinex-engineer-v10-dsl → Determinex Engineer v10-dsl
                // determinex-sentinel-v3     → Determinex Sentinel v3
                let without_prefix = bare_name.trim_start_matches("determinex-");
                // Capitalize first char of each dash-separated segment, rejoin with space
                let parts: Vec<String> = without_prefix
                    .split('-')
                    .map(|s| {
                        let mut c = s.chars();
                        match c.next() {
                            None => String::new(),
                            Some(f) => f.to_uppercase().collect::<String>() + c.as_str(),
                        }
                    })
                    .collect();
                format!("Determinex {}", parts.join(" "))
            } else {
                bare_name.clone()
            };
            InstalledModel {
                id: m.name.clone(),
                name: display,
                size_gb,
                param_size,
                quantization,
                is_determinex,
            }
        })
        .collect();

    Ok(models)
}

/// Ping the Ollama API server and return whether it is reachable.
///
/// Uses a dedicated one-shot `reqwest::Client` with a hard 2-second overall
/// timeout. This avoids reusing the orchestrator's persistent client, which
/// may be tied up mid-inference during the 8-second VRAM flush phases.
///
/// # Returns
/// - `Ok(true)`  — Ollama responded with HTTP 2xx on `/api/tags`
/// - `Ok(false)` — Ollama is unreachable, timed out, or returned an error status
#[tauri::command]
pub async fn check_ollama_status(base_url: Option<String>) -> Result<bool, String> {
    let client = Client::builder()
        .timeout(Duration::from_secs(PROBE_TIMEOUT_SECS))
        // Disable connection pooling — this is a one-shot probe, not a long-lived client.
        .pool_max_idle_per_host(0)
        .build()
        .map_err(|e| format!("[OLLAMA-PROBE] Failed to build reqwest client: {}", e))?;

    match client.get(ollama_tags_url(base_url.as_deref())).send().await {
        Ok(response) => {
            let reachable = response.status().is_success();
            if !reachable {
                log::warn!(
                    "[OLLAMA-PROBE] Ollama responded with non-success status: {}",
                    response.status()
                );
            }
            Ok(reachable)
        }
        Err(e) => {
            // Connection refused, timeout, DNS failure — all treated as "not running".
            // Log at debug level only — this fires every 3 seconds when Ollama is down,
            // so warn/error would saturate the log file immediately.
            log::debug!("[OLLAMA-PROBE] Unreachable: {}", e);
            Ok(false)
        }
    }
}

fn normalize_model_id(model_id: &str) -> String {
    model_id
        .trim()
        .strip_prefix("ollama/")
        .unwrap_or(model_id.trim())
        .strip_suffix(":latest")
        .unwrap_or_else(|| {
            model_id
                .trim()
                .strip_prefix("ollama/")
                .unwrap_or(model_id.trim())
        })
        .to_ascii_lowercase()
}

fn is_cloud_assignment(model_id: &str) -> bool {
    let lower = model_id.trim().to_ascii_lowercase();
    ["cloud/", "openai/", "anthropic/", "gemini/", "deepseek/"]
        .iter()
        .any(|prefix| lower.starts_with(prefix))
}

fn parse_model_aliases(config: &str) -> HashMap<String, String> {
    let mut aliases = HashMap::new();
    let entry_re = Regex::new(
        r"(?ms)^\s*-\s*model_name:\s*([^\s#]+)(.*?)(?=^\s*-\s*model_name:|^router_settings:|^determinex:|\z)"
    )
    .expect("valid model entry regex");
    let model_re = Regex::new(r"(?m)^\s*model:\s*([^\s#]+)").expect("valid model regex");
    for cap in entry_re.captures_iter(config) {
        if let (Some(alias), Some(block)) = (cap.get(1), cap.get(2)) {
            if let Some(model_cap) = model_re.captures(block.as_str()) {
                if let Some(model) = model_cap.get(1) {
                    aliases.insert(alias.as_str().to_string(), model.as_str().to_string());
                }
            }
        }
    }
    aliases
}

fn parse_role_assignments(config: &str) -> HashMap<String, String> {
    let mut roles = HashMap::from([
        ("oracle".to_string(), "local/fast".to_string()),
        ("architect".to_string(), "local/fast".to_string()),
        ("builder".to_string(), "determinex/engineer".to_string()),
        ("monitor".to_string(), "determinex/observer".to_string()),
    ]);
    for role in ["oracle", "architect", "builder", "monitor"] {
        let pattern = format!(r"(?m)^\s+{}:\s+([^\s#]+)", regex::escape(role));
        if let Ok(re) = Regex::new(&pattern) {
            if let Some(cap) = re.captures(config) {
                if let Some(value) = cap.get(1) {
                    roles.insert(role.to_string(), value.as_str().to_string());
                }
            }
        }
    }
    roles
}

fn installed_model_set(models: &[InstalledModel]) -> HashSet<String> {
    models
        .iter()
        .flat_map(|model| [model.id.as_str(), model.name.as_str()])
        .map(normalize_model_id)
        .collect()
}

fn model_is_installed(installed: &HashSet<String>, target: &str) -> bool {
    let normalized = normalize_model_id(target);
    installed.contains(&normalized) || installed.contains(&format!("{}:latest", normalized))
}

/// Return end-to-end model readiness for the Work/Hive path.
///
/// This command is intentionally authoritative: it reads the current
/// `litellm_config.yaml`, resolves role aliases through `model_list`, and
/// compares those resolved Ollama tags with the live `/api/tags` response.
#[tauri::command]
pub async fn get_work_readiness() -> Result<serde_json::Value, String> {
    let config_path = crate::ipc_hive::project_root().join("litellm_config.yaml");
    let config = std::fs::read_to_string(&config_path)
        .map_err(|e| format!("read {}: {}", config_path.display(), e))?;

    let aliases = parse_model_aliases(&config);
    let roles = parse_role_assignments(&config);
    let ollama_ok = check_ollama_status(None).await.unwrap_or(false);
    if !ollama_ok {
        return Ok(serde_json::json!({
            "status": "offline",
            "ready": false,
            "label": "Ollama Offline",
            "summary": "Ollama is not reachable. Start Ollama before generating specs.",
            "details": [],
            "missingRoles": roles.keys().cloned().collect::<Vec<_>>(),
            "checkedAt": chrono::Utc::now().timestamp_millis()
        }));
    }

    let models = get_ollama_models(None).await.unwrap_or_default();
    let installed = installed_model_set(&models);
    let mut checks: Vec<RoleModelReadiness> = Vec::new();
    let mut details: Vec<String> = Vec::new();
    let mut missing_roles: Vec<String> = Vec::new();
    let mut cloud_roles: Vec<String> = Vec::new();

    for role in ["oracle", "architect", "builder", "monitor"] {
        let assignment = roles
            .get(role)
            .cloned()
            .unwrap_or_else(|| "local/fast".to_string());
        let resolved = aliases.get(&assignment).cloned().or_else(|| {
            if assignment.starts_with("ollama/") || !assignment.contains('/') {
                Some(assignment.clone())
            } else {
                None
            }
        });

        if is_cloud_assignment(&assignment) {
            let message = format!("{} uses {}", role, assignment);
            cloud_roles.push(message.clone());
            checks.push(RoleModelReadiness {
                role: role.to_string(),
                assignment,
                target_model: resolved,
                status: "cloud".to_string(),
                message,
            });
            continue;
        }

        match resolved {
            Some(target) if model_is_installed(&installed, &target) => {
                let message = format!("{} -> {}", role, target);
                checks.push(RoleModelReadiness {
                    role: role.to_string(),
                    assignment,
                    target_model: Some(target),
                    status: "ready".to_string(),
                    message: message.clone(),
                });
                details.push(message);
            }
            Some(target) => {
                let message = format!("{} needs {}", role, target.trim_start_matches("ollama/"));
                missing_roles.push(message.clone());
                checks.push(RoleModelReadiness {
                    role: role.to_string(),
                    assignment,
                    target_model: Some(target),
                    status: "missing".to_string(),
                    message,
                });
            }
            None => {
                let message = format!("{} has unresolved assignment {}", role, assignment);
                missing_roles.push(message.clone());
                checks.push(RoleModelReadiness {
                    role: role.to_string(),
                    assignment,
                    target_model: None,
                    status: "unknown".to_string(),
                    message,
                });
            }
        }
    }

    if !missing_roles.is_empty() {
        return Ok(serde_json::json!({
            "status": "attention",
            "ready": false,
            "label": "Attention",
            "summary": format!("Missing local model coverage for {} role{}.", missing_roles.len(), if missing_roles.len() == 1 { "" } else { "s" }),
            "details": missing_roles,
            "missingRoles": missing_roles,
            "checks": checks,
            "checkedAt": chrono::Utc::now().timestamp_millis()
        }));
    }

    if !cloud_roles.is_empty() {
        return Ok(serde_json::json!({
            "status": "attention",
            "ready": false,
            "label": "Cloud Selected",
            "summary": "One or more Hive roles use cloud models. Confirm API keys or switch to local roles before generating.",
            "details": cloud_roles,
            "missingRoles": cloud_roles,
            "checks": checks,
            "checkedAt": chrono::Utc::now().timestamp_millis()
        }));
    }

    Ok(serde_json::json!({
        "status": "ready",
        "ready": true,
        "label": "Model Ready",
        "summary": "All local Hive roles resolve to installed Ollama models.",
        "details": details,
        "missingRoles": [],
        "checks": checks,
        "checkedAt": chrono::Utc::now().timestamp_millis()
    }))
}
