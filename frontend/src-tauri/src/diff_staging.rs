use serde::{Deserialize, Serialize};
use std::sync::Mutex;
use tauri::State;

use crate::compiler;

#[derive(Debug, Serialize, Deserialize, Clone)]
#[serde(rename_all = "camelCase")]
pub struct StagedDiff {
    pub id: String,
    pub path: String,
    pub original_content: String,
    pub proposed_content: String,
    /// Oracle verdict for `proposed_content`, computed once at staging time --
    /// None means "no oracle available for this file type", never "not yet
    /// checked" (there is no such state; verification happens synchronously
    /// in stage_diff_for_review, before the diff is ever visible to review).
    #[serde(default)]
    pub verified: Option<bool>,
    #[serde(default)]
    pub verification_tool: Option<String>,
    #[serde(default)]
    pub verification_output: Option<String>,
}

pub struct DiffStagingStore {
    pub diffs: Mutex<Vec<StagedDiff>>,
}

/// Infer a compiler.rs language tag from a file path's extension. Returns
/// None for anything compiler.rs has no oracle for yet -- an honest "can't
/// verify this one" rather than guessing.
fn infer_language(path: &str) -> Option<&'static str> {
    let ext = std::path::Path::new(path)
        .extension()
        .and_then(|e| e.to_str())
        .unwrap_or("")
        .to_lowercase();
    match ext.as_str() {
        "rs" => Some("rust"),
        "ts" | "tsx" => Some("typescript"),
        _ => None,
    }
}

#[tauri::command]
pub async fn get_staged_diffs(store: State<'_, DiffStagingStore>) -> Result<Vec<StagedDiff>, String> {
    let diffs = store.diffs.lock().map_err(|_| "Mutex poisoned")?.clone();
    Ok(diffs)
}

#[tauri::command]
pub async fn apply_staged_diff(id: String, store: State<'_, DiffStagingStore>) -> Result<(), String> {
    let mut diffs = store.diffs.lock().map_err(|_| "Mutex poisoned")?;
    if let Some(pos) = diffs.iter().position(|d| d.id == id) {
        let diff = diffs.remove(pos);
        std::fs::write(&diff.path, &diff.proposed_content).map_err(|e| e.to_string())?;
        Ok(())
    } else {
        Err("Diff not found".to_string())
    }
}

#[tauri::command]
pub async fn reject_staged_diff(id: String, store: State<'_, DiffStagingStore>) -> Result<(), String> {
    let mut diffs = store.diffs.lock().map_err(|_| "Mutex poisoned")?;
    if let Some(pos) = diffs.iter().position(|d| d.id == id) {
        diffs.remove(pos);
        Ok(())
    } else {
        Err("Diff not found".to_string())
    }
}

/// Stage a diff for review. This is also where verification actually happens --
/// by the time this returns, the diff either has a real compiler verdict
/// attached or an honest "no oracle for this file type" (None), never a
/// claim of correctness that wasn't actually checked.
#[tauri::command]
pub async fn stage_diff_for_review(diff: StagedDiff, store: State<'_, DiffStagingStore>) -> Result<(), String> {
    let mut diff = diff;

    if let Some(lang) = infer_language(&diff.path) {
        let filename = std::path::Path::new(&diff.path)
            .file_name()
            .and_then(|f| f.to_str())
            .unwrap_or("proposed")
            .to_string();
        let proposed = diff.proposed_content.clone();
        let feedback = tokio::task::spawn_blocking(move || compiler::check(lang, &filename, &proposed))
            .await
            .map_err(|e| format!("Verification task panicked: {}", e))?;

        if let Some(fb) = feedback {
            diff.verified = Some(fb.success);
            diff.verification_tool = Some(fb.tool);
            diff.verification_output = Some(fb.output);
        }
    }

    let mut diffs = store.diffs.lock().map_err(|_| "Mutex poisoned")?;
    diffs.push(diff);
    Ok(())
}
