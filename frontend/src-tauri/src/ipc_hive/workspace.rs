use std::process::Command;
use crate::windows_process::no_window;

use serde::Deserialize;
use tauri::State;

use super::{hive_script, project_root, resolve_python_exe, HiveProcessMap};

// ─────────────────────────────────────────────────────────────────────────────
// ENTERPRISE CODEBASE EXPLORER IPC
// ─────────────────────────────────────────────────────────────────────────────

#[derive(Deserialize)]
pub struct ExploreWorkspacePayload {
    pub workspace_path: String,
}

#[derive(Deserialize)]
pub struct DiagnoseWorkspacePayload {
    pub workspace_path: String,
    pub issue: String,
}

#[derive(Deserialize)]
pub struct FixWorkspacePayload {
    pub workspace_path: String,
    pub issue: String,
    #[serde(default)]
    pub out_path: Option<String>,
}

/// Explore an existing codebase: scan files, detect build system, run
/// shadow compilation, and return a diagnostic report.
///
/// This is the enterprise "load workspace" entry point. The frontend calls
/// this when the user opens an existing project (vs creating one from spec).
///
/// Spawns `determinex_hive.py explore --workspace PATH --json` as a subprocess.
/// Returns the full workspace report as JSON.
#[tauri::command]
pub async fn explore_workspace(
    payload: ExploreWorkspacePayload,
    _process_map: State<'_, HiveProcessMap>,
) -> Result<serde_json::Value, String> {
    log::info!("[IPC] explore_workspace: {}", payload.workspace_path);

    let root = project_root();
    let script = hive_script();

    if !script.exists() {
        return Ok(serde_json::json!({
            "ok": false,
            "error": format!("determinex_hive.py not found at {:?}", script)
        }));
    }

    let python = resolve_python_exe().map_err(|e| format!("Python not found: {}", e))?;
    let output = no_window(
        Command::new(&python)
            .args([
                script.to_str().unwrap(),
                "explore",
                "--workspace",
                &payload.workspace_path,
                "--json",
            ])
            .current_dir(&root),
    )
    .output()
    .map_err(|e| format!("Failed to spawn explore: {}", e))?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        return Ok(serde_json::json!({
            "ok": false,
            "error": format!("explore failed: {}", stderr)
        }));
    }

    let stdout = String::from_utf8_lossy(&output.stdout);
    match serde_json::from_str::<serde_json::Value>(&stdout) {
        Ok(data) => Ok(serde_json::json!({ "ok": true, "data": data })),
        Err(_) => Ok(serde_json::json!({
            "ok": true,
            "data": { "raw": stdout.trim().to_string() }
        })),
    }
}

/// Diagnose: given a bug description, locate the most relevant files in
/// an existing codebase and return targets + traceback context.
///
/// Spawns `determinex_hive.py diagnose --workspace PATH --issue TEXT`.
#[tauri::command]
pub async fn diagnose_workspace(
    payload: DiagnoseWorkspacePayload,
    _process_map: State<'_, HiveProcessMap>,
) -> Result<serde_json::Value, String> {
    log::info!(
        "[IPC] diagnose_workspace: {} issue_len={}",
        payload.workspace_path,
        payload.issue.len()
    );

    let root = project_root();
    let script = hive_script();

    if !script.exists() {
        return Ok(serde_json::json!({
            "ok": false,
            "error": format!("determinex_hive.py not found at {:?}", script)
        }));
    }

    let python = resolve_python_exe().map_err(|e| format!("Python not found: {}", e))?;
    let output = no_window(
        Command::new(&python)
            .args([
                script.to_str().unwrap(),
                "diagnose",
                "--workspace",
                &payload.workspace_path,
                "--issue",
                &payload.issue,
            ])
            .current_dir(&root),
    )
    .output()
    .map_err(|e| format!("Failed to spawn diagnose: {}", e))?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        return Ok(serde_json::json!({
            "ok": false,
            "error": format!("diagnose failed: {}", stderr)
        }));
    }

    let stdout = String::from_utf8_lossy(&output.stdout);
    match serde_json::from_str::<serde_json::Value>(&stdout) {
        Ok(data) => Ok(serde_json::json!({ "ok": true, "data": data })),
        Err(_) => Ok(serde_json::json!({
            "ok": true,
            "data": { "raw": stdout.trim().to_string() }
        })),
    }
}

/// Fix: locate a bug and generate a compiler-verified patch.
///
/// Spawns `determinex_hive.py fix --workspace PATH --issue TEXT [--out PATH]`
/// as a background subprocess. This can take minutes for large repos.
#[tauri::command]
pub async fn fix_workspace(
    payload: FixWorkspacePayload,
    _process_map: State<'_, HiveProcessMap>,
) -> Result<serde_json::Value, String> {
    log::info!(
        "[IPC] fix_workspace: {} issue_len={}",
        payload.workspace_path,
        payload.issue.len()
    );

    let root = project_root();
    let script = hive_script();

    if !script.exists() {
        return Ok(serde_json::json!({
            "ok": false,
            "error": format!("determinex_hive.py not found at {:?}", script)
        }));
    }

    let mut args = vec![
        script.to_str().unwrap().to_string(),
        "fix".to_string(),
        "--workspace".to_string(),
        payload.workspace_path.clone(),
        "--issue".to_string(),
        payload.issue.clone(),
    ];
    if let Some(ref out) = payload.out_path {
        args.push("--out".to_string());
        args.push(out.clone());
    }

    let python = resolve_python_exe().map_err(|e| format!("Python not found: {}", e))?;
    let output = no_window(Command::new(&python).args(&args).current_dir(&root))
        .output()
        .map_err(|e| format!("Failed to spawn fix: {}", e))?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        let stdout_text = String::from_utf8_lossy(&output.stdout);
        return Ok(serde_json::json!({
            "ok": false,
            "error": format!("fix failed: {}{}", stderr, stdout_text)
        }));
    }

    let stdout = String::from_utf8_lossy(&output.stdout);
    match serde_json::from_str::<serde_json::Value>(&stdout) {
        Ok(data) => Ok(serde_json::json!({ "ok": true, "data": data })),
        Err(_) => Ok(serde_json::json!({
            "ok": true,
            "data": { "raw": stdout.trim().to_string() }
        })),
    }
}
