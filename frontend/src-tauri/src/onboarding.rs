use serde::{Deserialize, Serialize};
use std::path::Path;

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct WorkspaceAnalysis {
    pub has_package_json: bool,
    pub has_cargo_toml: bool,
    pub has_requirements_txt: bool,
    pub inferred_stack: Vec<String>,
    pub recommended_action: String,
    pub build_command: Option<String>,
    /// The exact command "Execute Action" runs -- always kept consistent
    /// with `recommended_action` (e.g. "npm install" when the recommendation
    /// is to install dependencies, not the build command).
    pub action_command: Option<String>,
}

#[tauri::command]
pub async fn analyze_workspace(workspace: String) -> Result<WorkspaceAnalysis, String> {
    // Basic heuristics
    let root = Path::new(&workspace);
    let mut inferred_stack = Vec::new();
    let mut recommended_action = "Run Audit".to_string();
    let mut build_command = None;
    let mut action_command = None;

    let has_package_json = root.join("frontend/package.json").exists() || root.join("package.json").exists();
    let has_cargo_toml = root.join("frontend/src-tauri/Cargo.toml").exists() || root.join("Cargo.toml").exists();
    let has_requirements_txt = root.join("requirements.txt").exists() || root.join("pyproject.toml").exists();

    if has_package_json {
        inferred_stack.push("Node.js".to_string());
        build_command = Some("npm run build".to_string());
    }
    if has_cargo_toml {
        inferred_stack.push("Rust (Tauri)".to_string());
        if build_command.is_none() {
            build_command = Some("cargo build".to_string());
        }
    }
    if has_requirements_txt {
        inferred_stack.push("Python".to_string());
    }

    if inferred_stack.is_empty() {
        inferred_stack.push("Unknown".to_string());
        recommended_action = "Initialize Project".to_string();
    } else if has_package_json
        && !root.join("frontend/node_modules").exists()
        && !root.join("node_modules").exists()
    {
        recommended_action = "Install Dependencies (npm install)".to_string();
        action_command = Some("npm install".to_string());
    } else {
        action_command = build_command.clone();
    }

    Ok(WorkspaceAnalysis {
        has_package_json,
        has_cargo_toml,
        has_requirements_txt,
        inferred_stack,
        recommended_action,
        build_command,
        action_command,
    })
}
