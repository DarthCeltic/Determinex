// CLAUDE LANE — IDE repair bridge.
//
// Locked under: locks/sentinel/TAURI_RUST_COMMAND_BRIDGE_LOCK_001.json
//
// Stable Tauri command surface that fronts the locked Python backend
// command surface (scripts/ide/backend_command_surface.py +
// tauri_backend_bridge.py). Every command here returns JSON-safe
// results and refuses to perform live model calls, source mutation,
// corpus writes, or training-eligibility changes.
//
// Wire-up: in src-tauri/src/lib.rs add `mod ide_repair_bridge;` near
// the other mod declarations, and append the command names below
// to the tauri::generate_handler! macro invocation. See
// docs/TAURI_RUST_COMMAND_BRIDGE.md for the integration recipe.
//
// All commands shell out to the project's Python interpreter via a
// short helper (`run_backend_command`), which is intentionally written
// against std::process::Command rather than the broader Tauri sidecar
// machinery so the Claude lane review surface is small.

use serde::{Deserialize, Serialize};
use std::path::PathBuf;
use std::process::Command;

const PYTHON_DRIVER: &str = "scripts/ide/_tauri_driver.py";

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct IdeRepairResponse {
    pub command: String,
    pub status: String,
    pub payload: serde_json::Value,
    pub source_mutation_authorized: bool,
    pub training_eligible: bool,
    pub notes: Vec<String>,
}

impl IdeRepairResponse {
    fn unknown(command: &str, reason: &str) -> Self {
        Self {
            command: command.to_string(),
            status: "TAURI_COMMAND_BLOCKED_UNKNOWN".to_string(),
            payload: serde_json::json!({}),
            source_mutation_authorized: false,
            training_eligible: false,
            notes: vec![reason.to_string()],
        }
    }

    fn backend_missing(command: &str, reason: &str) -> Self {
        Self {
            command: command.to_string(),
            status: "TAURI_RUST_COMMAND_BRIDGE_BLOCKED_BACKEND_MISSING".to_string(),
            payload: serde_json::json!({}),
            source_mutation_authorized: false,
            training_eligible: false,
            notes: vec![reason.to_string()],
        }
    }
}

/// Repo-root helper. Walks upward from the current working directory
/// looking for a `scripts/ide/_tauri_driver.py` marker. Returns None
/// if the marker is not found.
fn locate_repo_root() -> Option<PathBuf> {
    let cwd = std::env::current_dir().ok()?;
    let mut cur: Option<&std::path::Path> = Some(cwd.as_path());
    while let Some(c) = cur {
        if c.join(PYTHON_DRIVER).is_file() {
            return Some(c.to_path_buf());
        }
        cur = c.parent();
    }
    None
}

fn run_backend_command(command: &str, args_json: &str) -> IdeRepairResponse {
    let root = match locate_repo_root() {
        Some(r) => r,
        None => {
            return IdeRepairResponse::backend_missing(
                command,
                "could not locate repo root (scripts/ide/_tauri_driver.py missing)",
            )
        }
    };

    // Spawn `python scripts/ide/_tauri_driver.py <command> <args_json>`.
    // No shell. argv only.
    let mut cmd = Command::new("python");
    cmd.arg(root.join(PYTHON_DRIVER));
    cmd.arg(command);
    cmd.arg(args_json);
    cmd.current_dir(&root);
    crate::windows_process::no_window(&mut cmd);

    match cmd.output() {
        Ok(out) => {
            if !out.status.success() {
                let stderr = String::from_utf8_lossy(&out.stderr).to_string();
                return IdeRepairResponse::backend_missing(
                    command,
                    &format!("python driver exited {:?}: {stderr}", out.status.code()),
                );
            }
            let stdout = String::from_utf8_lossy(&out.stdout).to_string();
            match serde_json::from_str::<IdeRepairResponse>(&stdout) {
                Ok(r) => r,
                Err(e) => IdeRepairResponse::backend_missing(
                    command,
                    &format!("malformed JSON from driver: {e}"),
                ),
            }
        }
        Err(e) => IdeRepairResponse::backend_missing(
            command,
            &format!("could not spawn python driver: {e}"),
        ),
    }
}

// ---------------------------------------------------------------------------
// Tauri commands. Names match the locked TauriBridge.
// ---------------------------------------------------------------------------

#[tauri::command]
pub fn open_workspace(workspace: String) -> IdeRepairResponse {
    let args = serde_json::json!({ "workspace": workspace }).to_string();
    run_backend_command("open_workspace", &args)
}

#[tauri::command]
pub fn get_workspace_status(workspace: String) -> IdeRepairResponse {
    let args = serde_json::json!({ "workspace": workspace }).to_string();
    run_backend_command("get_workspace_status", &args)
}

#[tauri::command]
pub fn get_model_route_status(task_class: String) -> IdeRepairResponse {
    let args = serde_json::json!({ "task_class": task_class }).to_string();
    run_backend_command("get_model_route_status", &args)
}

#[tauri::command]
pub fn diagnose_dry_run(workspace: String, task_class: String) -> IdeRepairResponse {
    let args = serde_json::json!({
        "workspace": workspace, "task_class": task_class,
    })
    .to_string();
    run_backend_command("diagnose_dry_run", &args)
}

#[tauri::command]
pub fn diagnose_live_opt_in(
    workspace: String,
    task_class: String,
    opt_in: bool,
) -> IdeRepairResponse {
    let args = serde_json::json!({
        "workspace": workspace, "task_class": task_class, "opt_in": opt_in,
    })
    .to_string();
    run_backend_command("diagnose_live_opt_in", &args)
}

#[tauri::command]
pub fn generate_patch_plan(workspace: String, opt_in: bool) -> IdeRepairResponse {
    let args = serde_json::json!({
        "workspace": workspace, "opt_in": opt_in,
    })
    .to_string();
    run_backend_command("generate_patch_plan", &args)
}

#[tauri::command]
pub fn verify_temp_patch(workspace: String) -> IdeRepairResponse {
    let args = serde_json::json!({ "workspace": workspace }).to_string();
    run_backend_command("verify_temp_patch", &args)
}

#[tauri::command]
pub fn get_human_approval_packet(workspace: String, unified_diff: String) -> IdeRepairResponse {
    let args = serde_json::json!({
        "workspace": workspace, "unified_diff": unified_diff,
    })
    .to_string();
    run_backend_command("get_human_approval_packet", &args)
}

#[tauri::command]
pub fn source_apply_dry_run(workspace: String) -> IdeRepairResponse {
    let args = serde_json::json!({ "workspace": workspace }).to_string();
    run_backend_command("source_apply_dry_run", &args)
}

#[tauri::command]
pub fn get_repair_flow_state(workspace: String) -> IdeRepairResponse {
    let args = serde_json::json!({ "workspace": workspace }).to_string();
    run_backend_command("get_repair_flow_state", &args)
}

#[tauri::command]
pub fn generate_llm_program_advisory(workspace: String, user_request: String) -> IdeRepairResponse {
    let args = serde_json::json!({
        "workspace": workspace, "user_request": user_request,
    })
    .to_string();
    run_backend_command("generate_llm_program_advisory", &args)
}

#[tauri::command]
pub fn preview_idea_oracle(idea_text: String) -> IdeRepairResponse {
    let args = serde_json::json!({ "idea_text": idea_text }).to_string();
    run_backend_command("preview_idea_oracle", &args)
}

#[tauri::command]
pub fn build_idea(idea_text: String, opt_in: bool, model_id: Option<String>) -> IdeRepairResponse {
    let args = serde_json::json!({
        "idea_text": idea_text,
        "opt_in": opt_in,
        "model_id": model_id.unwrap_or_default(),
    })
    .to_string();
    run_backend_command("build_idea", &args)
}

#[tauri::command]
pub fn repair_diagnose(workspace: String) -> IdeRepairResponse {
    let args = serde_json::json!({ "workspace": workspace }).to_string();
    run_backend_command("repair_diagnose", &args)
}

#[tauri::command]
pub fn get_governance_status() -> IdeRepairResponse {
    run_backend_command("get_governance_status", "{}")
}

// ---------------------------------------------------------------------------
// Unified product shell commands. These are read-only view-model snapshots that
// already route through scripts/ide/_tauri_driver.py and IDEBackendCommandSurface.
// They do not mutate source, grant approval, execute ProgramBench, or open
// training eligibility.
// ---------------------------------------------------------------------------

fn run_unified_product_command(command: &str) -> IdeRepairResponse {
    run_backend_command(command, "{}")
}

#[tauri::command]
pub fn get_unified_product_navigation_model() -> IdeRepairResponse {
    run_unified_product_command("get_unified_product_navigation_model")
}

#[tauri::command]
pub fn get_idea_lab_workflow_state() -> IdeRepairResponse {
    run_unified_product_command("get_idea_lab_workflow_state")
}

#[tauri::command]
pub fn get_repo_clinic_workflow_state() -> IdeRepairResponse {
    run_unified_product_command("get_repo_clinic_workflow_state")
}

#[tauri::command]
pub fn get_maintenance_bay_workflow_state() -> IdeRepairResponse {
    run_unified_product_command("get_maintenance_bay_workflow_state")
}

#[tauri::command]
pub fn get_learning_studio_workflow_state() -> IdeRepairResponse {
    run_unified_product_command("get_learning_studio_workflow_state")
}

#[tauri::command]
pub fn get_proof_operator_center_state() -> IdeRepairResponse {
    run_unified_product_command("get_proof_operator_center_state")
}

#[tauri::command]
pub fn get_user_level_teaching_windows() -> IdeRepairResponse {
    run_unified_product_command("get_user_level_teaching_windows")
}

#[tauri::command]
pub fn get_unified_splash_demo_spec() -> IdeRepairResponse {
    run_unified_product_command("get_unified_splash_demo_spec")
}

#[tauri::command]
pub fn get_idea_lab_verified_demo_status() -> IdeRepairResponse {
    run_unified_product_command("get_idea_lab_verified_demo_status")
}

#[tauri::command]
pub fn get_repo_clinic_verified_demo_status() -> IdeRepairResponse {
    run_unified_product_command("get_repo_clinic_verified_demo_status")
}

#[tauri::command]
pub fn get_maintenance_bay_verified_demo_status() -> IdeRepairResponse {
    run_unified_product_command("get_maintenance_bay_verified_demo_status")
}

#[tauri::command]
pub fn get_learning_studio_verified_demo_status() -> IdeRepairResponse {
    run_unified_product_command("get_learning_studio_verified_demo_status")
}

#[tauri::command]
pub fn get_proof_operator_center_milestone_dashboard_status() -> IdeRepairResponse {
    run_unified_product_command("get_proof_operator_center_milestone_dashboard_status")
}

// The list of registered commands. Frontend tests pin this so the
// Tauri command surface cannot drift silently.
pub const IDE_REPAIR_COMMANDS: &[&str] = &[
    "open_workspace",
    "get_workspace_status",
    "get_model_route_status",
    "diagnose_dry_run",
    "diagnose_live_opt_in",
    "generate_patch_plan",
    "verify_temp_patch",
    "get_human_approval_packet",
    "source_apply_dry_run",
    "get_repair_flow_state",
    "generate_llm_program_advisory",
    "preview_idea_oracle",
    "build_idea",
    "repair_diagnose",
    "get_governance_status",
];

#[allow(dead_code)]
pub const UNIFIED_PRODUCT_READ_ONLY_COMMANDS: &[&str] = &[
    "get_unified_product_navigation_model",
    "get_idea_lab_workflow_state",
    "get_repo_clinic_workflow_state",
    "get_maintenance_bay_workflow_state",
    "get_learning_studio_workflow_state",
    "get_proof_operator_center_state",
    "get_user_level_teaching_windows",
    "get_unified_splash_demo_spec",
    "get_idea_lab_verified_demo_status",
    "get_repo_clinic_verified_demo_status",
    "get_maintenance_bay_verified_demo_status",
    "get_learning_studio_verified_demo_status",
    "get_proof_operator_center_milestone_dashboard_status",
];

#[cfg(test)]
mod tests {
    use super::IDE_REPAIR_COMMANDS;

    #[test]
    fn flagship_commands_are_exposed_to_tauri() {
        for command in [
            "preview_idea_oracle",
            "build_idea",
            "repair_diagnose",
            "get_governance_status",
        ] {
            assert!(
                IDE_REPAIR_COMMANDS.contains(&command),
                "missing flagship Tauri command: {command}"
            );
        }
    }
}
