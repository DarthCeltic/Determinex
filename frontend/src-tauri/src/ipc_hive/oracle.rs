use std::process::{Command, Stdio};
use crate::win_process::HideConsoleExt;

use super::{
    project_root, resolve_python_exe, ConverseIdeaPayload, DiscoverIdeaPayload,
    GenerateSpecPayload, RefineSpecPayload,
};

fn user_safe_process_error(action: &str, stderr: &str) -> String {
    let cleaned = stderr.replace("\x1b", "");

    if let Some(line) = cleaned.lines().find(|line| line.contains("USER_ERROR:")) {
        return line
            .split_once("USER_ERROR:")
            .map(|(_, msg)| msg.trim().to_string())
            .filter(|msg| !msg.is_empty())
            .unwrap_or_else(|| {
                format!(
                    "{} could not continue because local model setup is incomplete.",
                    action
                )
            });
    }

    let lower = cleaned.to_lowercase();
    if lower.contains("ollama") && lower.contains("model") && lower.contains("not found") {
        return format!(
            "{} could not continue because the selected Ollama model is not installed. Open Settings -> Models to repair local models, or pull the missing model in Ollama.",
            action
        );
    }
    if lower.contains("ollama")
        && (lower.contains("connection")
            || lower.contains("refused")
            || lower.contains("unreachable"))
    {
        return format!(
            "{} could not continue because Ollama is not reachable. Start Ollama, then retry.",
            action
        );
    }
    if lower.contains("cloud model blocked") || lower.contains("determinex_allow_cloud_fallback") {
        return format!(
            "{} tried to use a cloud model, but cloud fallback is disabled. Choose a local model in Settings -> Models or explicitly enable cloud fallback.",
            action
        );
    }

    let detail = cleaned
        .lines()
        .rev()
        .find(|line| {
            let trimmed = line.trim();
            !trimmed.is_empty()
                && !trimmed.contains("LiteLLM")
                && !trimmed.contains("botocore")
                && !trimmed.contains("sagemaker")
                && !trimmed.contains("bedrock")
                && !trimmed.contains("[SAFETY]")
        })
        .map(str::trim)
        .unwrap_or("Check model setup and retry.");

    format!("{} failed. {}", action, detail)
}

fn simple_title(idea: &str) -> String {
    let words: Vec<&str> = idea
        .split_whitespace()
        .filter(|w| w.chars().any(|c| c.is_alphanumeric()))
        .take(6)
        .collect();
    if words.is_empty() {
        "New Project".to_string()
    } else {
        words
            .join(" ")
            .trim_matches(|c: char| !c.is_alphanumeric())
            .to_string()
    }
}

fn requested_surfaces(idea: &str) -> (bool, bool, bool, bool) {
    let text = idea.to_lowercase();
    let wants_web = [
        "website",
        "web app",
        "frontend",
        "dashboard",
        "portal",
        "saas",
        "browser",
    ]
    .iter()
    .any(|needle| text.contains(needle));
    let wants_mobile = [
        "mobile",
        "ios",
        "android",
        "phone app",
        "app store",
        "play store",
    ]
    .iter()
    .any(|needle| text.contains(needle));
    let wants_cli = ["cli", "command line", "terminal", "shell", "console"]
        .iter()
        .any(|needle| text.contains(needle));
    let wants_api = [
        "api", "backend", "server", "auth", "login", "account", "sync",
    ]
    .iter()
    .any(|needle| text.contains(needle));
    (wants_web, wants_mobile, wants_cli, wants_api)
}

fn fallback_discover(idea: &str) -> serde_json::Value {
    let (wants_web, wants_mobile, wants_cli, wants_api) = requested_surfaces(idea);
    let mut paths = Vec::new();
    if wants_web && wants_mobile {
        paths.push(serde_json::json!({
            "id": "web-mobile",
            "name": "Web + Mobile App",
            "description": "A shared product delivered as a website plus mobile applications.",
            "bestFor": "cross-platform products with accounts, sync, and shared workflows",
            "stack": "Next.js + API + React Native or Flutter",
            "complexity": "high",
            "buildTime": "3-6 weeks",
            "color": "#2dd4bf"
        }));
    }
    if wants_web {
        paths.push(serde_json::json!({
            "id": "web-app",
            "name": "Web App",
            "description": "A browser-based application with screens, workflows, and persistent state.",
            "bestFor": "dashboards, portals, SaaS workflows, and public product surfaces",
            "stack": "Next.js + TypeScript",
            "complexity": "medium",
            "buildTime": "1-2 weeks",
            "color": "#00e5ff"
        }));
    }
    if wants_mobile {
        paths.push(serde_json::json!({
            "id": "mobile-app",
            "name": "Mobile App",
            "description": "A phone-first application for iOS, Android, or both.",
            "bestFor": "native or cross-platform mobile experiences",
            "stack": "React Native, Flutter, Swift, or Kotlin",
            "complexity": "high",
            "buildTime": "2-4 weeks",
            "color": "#c084fc"
        }));
    }
    if wants_api || wants_web || wants_mobile {
        paths.push(serde_json::json!({
            "id": "api",
            "name": "Backend API",
            "description": "A service layer for app data, authentication, integrations, and business logic.",
            "bestFor": "web/mobile clients and integrations needing shared state",
            "stack": "FastAPI, Axum, Gin, or Express",
            "complexity": "medium",
            "buildTime": "1-2 weeks",
            "color": "#34d399"
        }));
    }
    if wants_cli || paths.is_empty() {
        paths.push(serde_json::json!({
            "id": "cli",
            "name": "CLI Tool",
            "description": "A command-line tool for scripted or terminal-driven workflows.",
            "bestFor": "developers and power users",
            "stack": "Rust, Go, Python, or Node",
            "complexity": "low",
            "buildTime": "1-3 days",
            "color": "#fb923c"
        }));
    }

    serde_json::json!({
        "paths": paths,
        "message": "I can still analyze this idea with the built-in advisor. Which product surface should we build first?",
        "questions": ["Who is the first user, and what should they be able to do on day one?"],
        "advisor_mode": "built_in_packaged_fallback"
    })
}

fn fallback_spec(idea: &str) -> String {
    let title = simple_title(idea);
    let (wants_web, wants_mobile, wants_cli, wants_api) = requested_surfaces(idea);
    let (language, project_type) = if wants_web || wants_mobile {
        (
            "typescript",
            if wants_web && wants_mobile {
                "fullstack-app"
            } else {
                "web-app"
            },
        )
    } else if wants_api {
        ("python", "api-service")
    } else if wants_cli {
        ("rust", "cli-tool")
    } else {
        ("typescript", "web-app")
    };
    format!(
        "# {title}\n\n## Goal\nBuild a working Determinex project from this idea: {idea}\n\n## Language\n{language}\n\n## Project Type\n{project_type}\n\n## Constraints\n- Keep the first version small enough to compile and test locally.\n- Use explicit error handling and deterministic tests for the core workflow.\n- Do not claim production readiness until installer, model, and proof gates pass.\n\n## Files\n- `README.md` - project overview and setup notes\n- `src/main` - primary application entry point\n- `tests/core.test` - smoke tests for the first user workflow\n\n## Dependencies\n- Standard project toolchain - selected after the first generated scaffold\n\n## Tests\nRun the language-native compiler or test runner and add at least one end-to-end smoke test for the core user path.\n\n## Notes\nThis spec was generated by the packaged built-in advisor because the optional Python Oracle scripts were not available in this install.\n"
    )
}

fn fallback_refine(spec: &str, request: &str) -> serde_json::Value {
    serde_json::json!({
        "response": format!("I recorded the requested refinement. The packaged fallback cannot call the full Oracle model yet, so I preserved the current spec and added the request as a note: {}", request),
        "spec": format!("{}\n\n## Refinement Request\n- {}\n", spec.trim(), request.trim())
    })
}

/// Generate a spec from free text by calling scripts/spec_generator.py.
/// Payload is sent via stdin as JSON to avoid Windows 32767-char CLI arg limit.
#[tauri::command]
pub async fn generate_spec(payload: GenerateSpecPayload) -> Result<serde_json::Value, String> {
    log::info!("[IPC] generate_spec: {} chars", payload.idea.len());
    let script = project_root().join("scripts").join("spec_generator.py");
    if !script.exists() {
        return Ok(serde_json::json!({
            "ok": true,
            "data": { "spec": fallback_spec(&payload.idea) },
            "advisor_mode": "built_in_packaged_fallback"
        }));
    }

    let python = match resolve_python_exe() {
        Ok(path) => path,
        Err(_) => {
            return Ok(serde_json::json!({
                "ok": true,
                "data": { "spec": fallback_spec(&payload.idea) },
                "advisor_mode": "built_in_packaged_fallback"
            }));
        }
    };

    let stdin_json = serde_json::to_string(&serde_json::json!({ "idea": payload.idea }))
        .map_err(|e| format!("Failed to serialize generate_spec payload: {}", e))?;

    let mut child = Command::new(&python).hide_console()
        .args([script.to_str().unwrap(), "--stdin"])
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .map_err(|e| format!("Failed to spawn spec_generator.py: {}", e))?;

    if let Some(mut stdin) = child.stdin.take() {
        use std::io::Write;
        stdin
            .write_all(stdin_json.as_bytes())
            .map_err(|e| format!("Failed to write generate_spec payload to stdin: {}", e))?;
    }

    let output = child
        .wait_with_output()
        .map_err(|e| format!("Failed to wait for spec_generator.py: {}", e))?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        return Ok(serde_json::json!({
            "ok": false,
            "error": user_safe_process_error("Spec generation", &stderr)
        }));
    }

    let stdout = String::from_utf8_lossy(&output.stdout);
    Ok(serde_json::json!({
        "ok": true,
        "data": {
            "spec": stdout.trim().to_string(),
        }
    }))
}

/// Run the discovery phase: analyze raw idea + optional image attachments.
/// Full payload is sent via stdin so large image data doesn't get truncated in CLI args.
#[tauri::command]
pub async fn discover_idea(payload: DiscoverIdeaPayload) -> Result<serde_json::Value, String> {
    log::info!("[IPC] discover_idea: {}", payload.idea);
    let script = project_root().join("scripts").join("idea_oracle.py");
    if !script.exists() {
        return Ok(serde_json::json!({ "ok": true, "data": fallback_discover(&payload.idea) }));
    }
    let python = match resolve_python_exe() {
        Ok(path) => path,
        Err(_) => {
            return Ok(serde_json::json!({ "ok": true, "data": fallback_discover(&payload.idea) }))
        }
    };

    let payload_json = serde_json::to_string(&payload)
        .map_err(|e| format!("Failed to serialize discover payload: {}", e))?;

    let mut child = Command::new(&python).hide_console()
        .args([script.to_str().unwrap(), "--mode", "discover"])
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .map_err(|e| format!("Failed to spawn idea_oracle.py: {}", e))?;

    if let Some(mut stdin) = child.stdin.take() {
        use std::io::Write;
        stdin
            .write_all(payload_json.as_bytes())
            .map_err(|e| format!("Failed to write discover payload to stdin: {}", e))?;
    }

    let output = child
        .wait_with_output()
        .map_err(|e| format!("Failed to wait for idea_oracle.py: {}", e))?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        let safe_error = user_safe_process_error("Idea discovery", &stderr);
        let mut fallback = fallback_discover(&payload.idea);
        fallback["warning"] = serde_json::Value::String(safe_error);
        return Ok(serde_json::json!({ "ok": true, "data": fallback }));
    }

    let stdout = String::from_utf8_lossy(&output.stdout);
    let parsed: serde_json::Value = serde_json::from_str(stdout.trim()).map_err(|e| {
        format!(
            "Failed to parse discover output: {} — raw: {}",
            e,
            stdout.trim()
        )
    })?;

    if let Some(err) = parsed.get("error") {
        return Ok(serde_json::json!({ "ok": false, "error": err }));
    }

    Ok(serde_json::json!({ "ok": true, "data": parsed }))
}

/// Continue the discovery conversation. Full payload (history + current message + attachments)
/// is sent via stdin as JSON.
#[tauri::command]
pub async fn converse_idea(payload: ConverseIdeaPayload) -> Result<serde_json::Value, String> {
    log::info!("[IPC] converse_idea: {}", payload.user_message);
    let script = project_root().join("scripts").join("idea_oracle.py");
    if !script.exists() {
        return Ok(serde_json::json!({
            "ok": true,
            "data": {
                "response": "Got it. What should the first working version do for the user?",
                "ready_to_spec": false,
                "spec_summary": null,
                "advisor_mode": "built_in_packaged_fallback"
            }
        }));
    }
    let python = match resolve_python_exe() {
        Ok(path) => path,
        Err(_) => {
            return Ok(serde_json::json!({
                "ok": true,
                "data": {
                    "response": "Got it. What should the first working version do for the user?",
                    "ready_to_spec": false,
                    "spec_summary": null,
                    "advisor_mode": "built_in_packaged_fallback"
                }
            }));
        }
    };

    let payload_json = serde_json::to_string(&payload)
        .map_err(|e| format!("Failed to serialize converse payload: {}", e))?;

    let mut child = Command::new(&python).hide_console()
        .args([script.to_str().unwrap(), "--mode", "converse"])
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .map_err(|e| format!("Failed to spawn idea_oracle.py: {}", e))?;

    if let Some(mut stdin) = child.stdin.take() {
        use std::io::Write;
        stdin
            .write_all(payload_json.as_bytes())
            .map_err(|e| format!("Failed to write converse payload to stdin: {}", e))?;
    }

    let output = child
        .wait_with_output()
        .map_err(|e| format!("Failed to wait for idea_oracle.py: {}", e))?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        return Ok(serde_json::json!({
            "ok": true,
            "data": {
                "response": user_safe_process_error("Idea conversation", &stderr),
                "ready_to_spec": false,
                "spec_summary": null,
                "advisor_mode": "built_in_packaged_fallback"
            }
        }));
    }

    let stdout = String::from_utf8_lossy(&output.stdout);
    let parsed: serde_json::Value = serde_json::from_str(stdout.trim()).map_err(|e| {
        format!(
            "Failed to parse converse output: {} — raw: {}",
            e,
            stdout.trim()
        )
    })?;

    if let Some(err) = parsed.get("error") {
        return Ok(serde_json::json!({ "ok": false, "error": err }));
    }

    Ok(serde_json::json!({ "ok": true, "data": parsed }))
}

/// Refine an existing spec and return both the updated spec and an Oracle explanation.
/// Calls scripts/spec_refiner.py which returns JSON { response, spec }.
#[tauri::command]
pub async fn refine_spec(payload: RefineSpecPayload) -> Result<serde_json::Value, String> {
    log::info!(
        "[IPC] refine_spec: {} chars request, {} chars spec",
        payload.request.len(),
        payload.spec.len()
    );
    let script = project_root().join("scripts").join("spec_refiner.py");
    if !script.exists() {
        return Ok(serde_json::json!({
            "ok": true,
            "data": fallback_refine(&payload.spec, &payload.request),
            "advisor_mode": "built_in_packaged_fallback"
        }));
    }

    let python = match resolve_python_exe() {
        Ok(path) => path,
        Err(_) => {
            return Ok(serde_json::json!({
                "ok": true,
                "data": fallback_refine(&payload.spec, &payload.request),
                "advisor_mode": "built_in_packaged_fallback"
            }));
        }
    };

    // Send payload via stdin as JSON to avoid Windows 32767-char CLI arg limit.
    let stdin_json = serde_json::to_string(&serde_json::json!({
        "spec": payload.spec,
        "request": payload.request,
    }))
    .map_err(|e| format!("Failed to serialize refine_spec payload: {}", e))?;

    let mut child = Command::new(&python).hide_console()
        .args([script.to_str().unwrap(), "--stdin"])
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .map_err(|e| format!("Failed to spawn spec_refiner.py: {}", e))?;

    if let Some(mut stdin) = child.stdin.take() {
        use std::io::Write;
        stdin
            .write_all(stdin_json.as_bytes())
            .map_err(|e| format!("Failed to write refine_spec payload to stdin: {}", e))?;
    }

    let output = child
        .wait_with_output()
        .map_err(|e| format!("Failed to wait for spec_refiner.py: {}", e))?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        return Ok(serde_json::json!({
            "ok": true,
            "data": fallback_refine(&payload.spec, &user_safe_process_error("Spec refinement", &stderr)),
            "advisor_mode": "built_in_packaged_fallback"
        }));
    }

    let stdout = String::from_utf8_lossy(&output.stdout);
    let parsed: serde_json::Value = serde_json::from_str(stdout.trim()).map_err(|e| {
        format!(
            "Failed to parse spec_refiner output: {} — raw: {}",
            e,
            stdout.trim()
        )
    })?;

    if let Some(err) = parsed.get("error") {
        return Ok(serde_json::json!({ "ok": false, "error": err }));
    }

    Ok(serde_json::json!({
        "ok": true,
        "data": {
            "response": parsed["response"],
            "spec": parsed["spec"],
        }
    }))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn built_in_discover_fallback_respects_web_and_mobile_intent() {
        let result = fallback_discover("Build a website and mobile app for repair scheduling");
        let paths = result["paths"].as_array().expect("paths");
        let names: Vec<&str> = paths.iter().filter_map(|p| p["name"].as_str()).collect();
        assert!(names.contains(&"Web + Mobile App"));
        assert!(names.contains(&"Web App"));
        assert!(names.contains(&"Mobile App"));
    }

    #[test]
    fn built_in_spec_fallback_generates_markdown_contract() {
        let spec = fallback_spec("Build a dashboard for model setup");
        assert!(spec.starts_with("# Build a dashboard"));
        assert!(spec.contains("## Language"));
        assert!(spec.contains("typescript"));
        assert!(spec.contains("packaged built-in advisor"));
    }
}
