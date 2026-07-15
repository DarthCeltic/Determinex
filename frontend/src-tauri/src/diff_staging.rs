use serde::{Deserialize, Serialize};
use std::sync::Mutex;
use tauri::State;

#[derive(Debug, Serialize, Deserialize, Clone)]
#[serde(rename_all = "camelCase")]
pub struct StagedDiff {
    pub id: String,
    pub path: String,
    pub original_content: String,
    pub proposed_content: String,
}

pub struct DiffStagingStore {
    pub diffs: Mutex<Vec<StagedDiff>>,
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
        // In a real implementation we would write to disk
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

#[tauri::command]
pub async fn stage_diff_for_review(diff: StagedDiff, store: State<'_, DiffStagingStore>) -> Result<(), String> {
    let mut diffs = store.diffs.lock().map_err(|_| "Mutex poisoned")?;
    diffs.push(diff);
    Ok(())
}
