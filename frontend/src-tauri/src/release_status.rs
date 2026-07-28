/// release_status.rs — reads the live release-gate evidence collector output.
///
/// `MissionControlPanel`/`SuccessorRoadmapPanel` used to import a hand-baked TS
/// snapshot of this file (`releaseGateStatus.ts`), which drifts stale within
/// days of a fresh `determinex_release_gates.py` run (see CLAUDE.md's "Board
/// staleness protocol"). This command reads the real, current evidence file at
/// runtime so the frontend can show live gate status with the baked-in
/// snapshot only as a browser-mode/read-failure fallback.
use serde_json::Value;
use std::fs;

#[tauri::command]
/// Returns the newest `release_gates_*.json` evidence file VERBATIM.
///
/// Deliberately untyped, and this is the one place where that is the honest
/// answer: the file is written by the release-gate collector and its shape is
/// whatever that run produced. Declaring a struct here would silently DROP fields
/// from an evidence artifact, which is worse than leaving it dynamic -- the whole
/// point of the artifact is that it is a faithful record.
pub fn get_release_gate_status() -> Result<Value, String> {
    let dir = crate::ipc_hive::project_root()
        .join("assurance")
        .join("evidence")
        .join("determinex_release_gate_status");

    let mut candidates: Vec<_> = fs::read_dir(&dir)
        .map_err(|e| format!("Cannot read {}: {e}", dir.display()))?
        .flatten()
        .filter(|entry| {
            let name = entry.file_name();
            let name = name.to_string_lossy();
            name.starts_with("release_gates_") && name.ends_with(".json")
        })
        .collect();

    // Sort by mtime so a future collector run that writes a differently-dated
    // filename is still picked up as "current" without a frontend code change.
    candidates.sort_by_key(|entry| entry.metadata().and_then(|m| m.modified()).ok());

    let newest = candidates
        .last()
        .ok_or_else(|| format!("No release_gates_*.json found in {}", dir.display()))?;

    let content = fs::read_to_string(newest.path()).map_err(|e| e.to_string())?;
    serde_json::from_str(&content).map_err(|e| e.to_string())
}
