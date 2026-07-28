use serde::Serialize;
use std::fs;
use std::path::{Path, PathBuf};
use tauri::command;
use crate::win_process::HideConsoleExt;

/// Cross-platform filesystem boundary for all IPC file access commands.
/// Resolved at startup to the platform home directory via `app.path().home_dir()`.
/// Every `read_file_content` and `get_file_system_tree` call is validated against
/// this root — prevents path traversal from a compromised WebView or malicious IPC payload.
pub struct WorkspaceRoot(pub PathBuf);

/// Resolve symlinks and verify the target lives inside `root`.
/// Returns the canonicalized path on success, or an access-denied error string.
/// The root is also canonicalized so that symlinked home dirs (e.g. macOS /Users -> /private/var)
/// don't produce false negatives on the `starts_with` check.
fn safe_canonicalize(root: &Path, target_path: &str) -> Result<PathBuf, String> {
    let canonical = fs::canonicalize(target_path)
        .map_err(|_| format!("Invalid or non-existent path: {}", target_path))?;
    let canonical_root = fs::canonicalize(root).unwrap_or_else(|_| root.to_path_buf());
    if !canonical.starts_with(&canonical_root) {
        return Err(format!(
            "Access denied: path '{}' is outside workspace boundary '{}'",
            canonical.display(),
            canonical_root.display()
        ));
    }
    Ok(canonical)
}

fn resolve_write_target(raw_path: &str) -> PathBuf {
    let target = PathBuf::from(raw_path);
    if target.is_absolute() {
        return target;
    }

    let mut bases = Vec::new();
    if let Ok(root) = std::env::var("DETERMINEX_ROOT") {
        bases.push(PathBuf::from(root));
    }
    if let Ok(cwd) = std::env::current_dir() {
        for ancestor in cwd.ancestors() {
            bases.push(ancestor.to_path_buf());
        }
    }
    bases.push(PathBuf::from(env!("CARGO_MANIFEST_DIR")));

    for base in bases {
        let candidate = base.join(&target);
        if candidate.exists() || candidate.parent().is_some_and(Path::exists) {
            return candidate;
        }
    }

    std::env::current_dir()
        .unwrap_or_else(|_| PathBuf::from("."))
        .join(target)
}

// ─────────────────────────────────────────────────────────────────────────────
// AEGIS FS JAIL — Path Traversal Lockdown
// ─────────────────────────────────────────────────────────────────────────────

/// Verify that `target_path` is strictly inside `workspace_root` after
/// canonicalization. Designed for AI-directed file writes — prevents an
/// adversarial model from escaping the sandbox via `../../etc/passwd` tricks.
///
/// Handles both existing and not-yet-existing target paths:
///   • If `target_path` exists on disk → `fs::canonicalize` resolves symlinks
///     and returns the real absolute path. `starts_with` check is exact.
///   • If `target_path` does not yet exist (a new file) → we walk up the
///     ancestry until we find an existing prefix, canonicalize that, then
///     re-append the remaining suffix. This gives the same traversal
///     resistance without requiring the file to pre-exist.
///
/// # Returns
/// `true`  — the path is inside the workspace; the write is safe to proceed.  
/// `false` — the path escapes the workspace; the caller **must** abort.
///
/// # Usage in Orchestrator
/// ```rust
/// if !crate::fs::is_safe_path(&workspace.0, &candidate) {
///     return Err(OrchestratorError::security_panic("Path Traversal Blocked"));
/// }
/// ```
pub fn is_safe_path(workspace_root: &Path, target_path: &Path) -> bool {
    let canonical_root = match fs::canonicalize(workspace_root) {
        Ok(r) => r,
        Err(_) => workspace_root.to_path_buf(), // root doesn't exist yet — conservative
    };

    // Fast path: target already exists — full canonicalization available.
    if target_path.exists() {
        return fs::canonicalize(target_path)
            .map(|c| c.starts_with(&canonical_root))
            .unwrap_or(false);
    }

    // Slow path: target doesn't exist yet (new file being staged).
    // Walk up the path until we find an ancestor that exists, canonicalize it,
    // then re-attach the non-existing suffix and check the boundary.
    let mut existing_prefix = target_path.to_path_buf();
    let mut non_existing_suffix = Vec::<std::ffi::OsString>::new();

    loop {
        if existing_prefix.exists() {
            break;
        }
        match existing_prefix.file_name() {
            Some(name) => {
                non_existing_suffix.push(name.to_os_string());
                existing_prefix = match existing_prefix.parent() {
                    Some(p) => p.to_path_buf(),
                    None => return false, // hit filesystem root — definitely outside
                };
            }
            None => return false,
        }
    }

    let Ok(canonical_prefix) = fs::canonicalize(&existing_prefix) else {
        return false;
    };

    // Re-attach the non-existing suffix (reversed because we pushed ancestors last)
    let mut resolved = canonical_prefix;
    for component in non_existing_suffix.iter().rev() {
        resolved.push(component);
    }

    resolved.starts_with(&canonical_root)
}

#[derive(Serialize)]
pub struct FileNode {
    pub name: String,
    pub r#type: String, // 'file' or 'folder'
    pub path: String,
    pub children: Option<Vec<FileNode>>,
}

#[derive(Serialize)]
pub struct FsTreeResponse {
    pub tree: Vec<FileNode>,
}

#[derive(Serialize)]
pub struct WorkspaceFile {
    name: String,
    modified: String,
    r#type: String,
}

#[derive(Serialize)]
pub struct WorkspaceResponse {
    files: Vec<WorkspaceFile>,
}

#[derive(Serialize)]
pub struct FileContentResponse {
    status: String,
    content: String,
}

fn build_tree(path: &Path, depth: u32) -> Option<FileNode> {
    if !path.exists() {
        return None;
    }

    let name = path.file_name()?.to_string_lossy().to_string();
    let abs_path = path.to_string_lossy().to_string();

    if path.is_file() {
        Some(FileNode {
            name,
            r#type: "file".to_string(),
            path: abs_path,
            children: None,
        })
    } else if path.is_dir() {
        let mut children = Vec::new();
        if depth > 0 {
            if let Ok(entries) = fs::read_dir(path) {
                for entry in entries.flatten() {
                    let entry_path = entry.path();
                    let file_name = entry_path.file_name().unwrap_or_default().to_string_lossy();

                    if file_name.starts_with('.')
                        || file_name == "node_modules"
                        || file_name == "target"
                        || file_name == "__pycache__"
                        || file_name == "out"
                    {
                        continue;
                    }

                    if let Some(child_node) = build_tree(&entry_path, depth - 1) {
                        children.push(child_node);
                    }
                }
            }
        }

        // sort: folders first, then alphabetical
        children.sort_by(|a, b| {
            if a.r#type == b.r#type {
                a.name.cmp(&b.name)
            } else if a.r#type == "folder" {
                std::cmp::Ordering::Less
            } else {
                std::cmp::Ordering::Greater
            }
        });

        Some(FileNode {
            name,
            r#type: "folder".to_string(),
            path: abs_path,
            children: Some(children),
        })
    } else {
        None
    }
}

#[command]
pub fn get_file_system_tree(
    workspace: tauri::State<'_, WorkspaceRoot>,
    target_path: String,
) -> Result<FsTreeResponse, String> {
    let safe_path = safe_canonicalize(&workspace.0, &target_path)?;
    let mut tree = Vec::new();

    if let Ok(entries) = fs::read_dir(&safe_path) {
        for entry in entries.flatten() {
            let entry_path = entry.path();
            let file_name = entry_path.file_name().unwrap_or_default().to_string_lossy();

            if file_name.starts_with('.')
                || file_name == "node_modules"
                || file_name == "target"
                || file_name == "__pycache__"
                || file_name == "out"
            {
                continue;
            }

            if let Some(node) = build_tree(&entry_path, 2) {
                tree.push(node);
            }
        }
    }

    Ok(FsTreeResponse { tree })
}

#[derive(Serialize)]
pub struct ArtifactEntry {
    pub name: String,
    pub path: String,
    pub size_bytes: u64,
    pub file_count: u64,
    pub modified: Option<String>,
}

/// Known build-output directory names, relative to a project workspace root.
/// Fixed literals only -- no user input is joined here, so there is no
/// traversal surface even before the is_safe_path check below runs.
const ARTIFACT_CANDIDATE_DIRS: &[&str] = &[
    "target/debug",
    "target/release",
    "frontend/.next",
    "frontend/src-tauri/target/debug",
    "frontend/src-tauri/target/release",
    "dist",
    "dist-windows",
];

fn dir_size_and_count(path: &Path) -> (u64, u64) {
    let mut size = 0u64;
    let mut count = 0u64;
    if let Ok(entries) = fs::read_dir(path) {
        for entry in entries.flatten() {
            let entry_path = entry.path();
            if let Ok(meta) = entry.metadata() {
                if meta.is_dir() {
                    let (s, c) = dir_size_and_count(&entry_path);
                    size += s;
                    count += c;
                } else {
                    size += meta.len();
                    count += 1;
                }
            }
        }
    }
    (size, count)
}

/// Real (non-fake) build-artifact scan: reports actual size/file-count/mtime for
/// whichever known build-output directories exist under the given project root.
/// Read-only, bounded to a fixed candidate list -- never lists arbitrary directories.
#[command]
pub fn get_build_artifacts(
    workspace: tauri::State<'_, WorkspaceRoot>,
    workspace_path: String,
) -> Result<Vec<ArtifactEntry>, String> {
    let root = PathBuf::from(&workspace_path);
    if !is_safe_path(&workspace.0, &root) {
        return Err(format!(
            "Access denied: '{}' is outside the file-browser boundary",
            workspace_path
        ));
    }

    let mut out = Vec::new();
    for rel in ARTIFACT_CANDIDATE_DIRS {
        let candidate = root.join(rel);
        if !candidate.is_dir() {
            continue;
        }
        let (size_bytes, file_count) = dir_size_and_count(&candidate);
        let modified = fs::metadata(&candidate)
            .ok()
            .and_then(|m| m.modified().ok())
            .map(|t| {
                let datetime: chrono::DateTime<chrono::Local> = t.into();
                datetime.format("%Y-%m-%d %H:%M:%S").to_string()
            });
        out.push(ArtifactEntry {
            name: rel.to_string(),
            path: candidate.to_string_lossy().to_string(),
            size_bytes,
            file_count,
            modified,
        });
    }
    Ok(out)
}

#[command]
pub fn get_workspace_files(
    workspace: tauri::State<'_, WorkspaceRoot>,
) -> Result<WorkspaceResponse, String> {
    // Sandbox is a `sandbox/` subdirectory within the platform workspace root.
    let sandbox_dir = workspace.0.join("sandbox");
    let mut files = Vec::new();

    if let Ok(entries) = fs::read_dir(&sandbox_dir) {
        for entry in entries.flatten() {
            let path = entry.path();
            if path.is_file() {
                let metadata = fs::metadata(&path).map_err(|e| e.to_string())?;
                let modified = metadata.modified().map_err(|e| e.to_string())?;
                let datetime: chrono::DateTime<chrono::Local> = modified.into();

                files.push(WorkspaceFile {
                    name: path
                        .file_name()
                        .unwrap_or_default()
                        .to_string_lossy()
                        .to_string(),
                    modified: datetime.format("%Y-%m-%d %H:%M:%S").to_string(),
                    r#type: "file".to_string(),
                });
            }
        }
    }

    Ok(WorkspaceResponse { files })
}

/// Read a file at `relative_path` inside the workspace root and return its contents as a string.
/// The path is joined with the workspace root before the boundary check — callers pass a
/// relative path (e.g. `"sandbox/main.rs"`), never an absolute one.
#[command]
pub async fn read_workspace_file(
    workspace: tauri::State<'_, WorkspaceRoot>,
    relative_path: String,
) -> Result<String, String> {
    let candidate = workspace.0.join(&relative_path);
    let safe_path = safe_canonicalize(&workspace.0, &candidate.to_string_lossy())?;
    if !safe_path.is_file() {
        return Err(format!("'{}' is not a regular file", relative_path));
    }
    fs::read_to_string(&safe_path).map_err(|e| e.to_string())
}

#[command]
pub fn read_file_content(
    workspace: tauri::State<'_, WorkspaceRoot>,
    target_path: String,
) -> Result<FileContentResponse, String> {
    // Canonicalize + workspace boundary check — prevents arbitrary file reads
    // via path traversal from a compromised WebView or malicious IPC payload.
    let safe_path = safe_canonicalize(&workspace.0, &target_path)?;

    if !safe_path.is_file() {
        return Err("Target is not a file or does not exist".to_string());
    }

    let content = fs::read_to_string(&safe_path).map_err(|e| e.to_string())?;
    Ok(FileContentResponse {
        status: "success".to_string(),
        content,
    })
}

#[command]
pub fn write_file_content(
    workspace: tauri::State<'_, WorkspaceRoot>,
    path: String,
    content: String,
) -> Result<FileContentResponse, String> {
    let target = resolve_write_target(&path);
    if !is_safe_path(&workspace.0, &target) {
        return Err(format!(
            "Access denied: path '{}' is outside workspace boundary '{}'",
            target.display(),
            workspace.0.display()
        ));
    }
    if let Some(parent) = target.parent() {
        fs::create_dir_all(parent).map_err(|e| e.to_string())?;
    }
    fs::write(&target, content.as_bytes()).map_err(|e| e.to_string())?;
    Ok(FileContentResponse {
        status: "success".to_string(),
        content,
    })
}

// ─────────────────────────────────────────────────────────────────────────────
// TRANSACTIONAL STAGING LAYER (For MoA BLAST RADIUS PROTECTION)
// ─────────────────────────────────────────────────────────────────────────────

/// Stage files to a hidden `.determinex_staging` directory inside `sandbox/`.
pub fn stage_files(
    workspace: &WorkspaceRoot,
    files_to_write: &[(String, String)],
) -> Result<PathBuf, String> {
    let staging_dir = workspace.0.join("sandbox").join(".determinex_staging");
    if staging_dir.exists() {
        fs::remove_dir_all(&staging_dir).map_err(|e| e.to_string())?;
    }
    fs::create_dir_all(&staging_dir).map_err(|e| e.to_string())?;

    for (file_name, content) in files_to_write {
        // Only allow bare filenames to be staged for safety currently to prevent traversal
        let safe_name = std::path::Path::new(file_name)
            .file_name()
            .unwrap_or_else(|| std::ffi::OsStr::new("output.txt"))
            .to_string_lossy()
            .to_string();

        let file_path = staging_dir.join(safe_name);
        fs::write(file_path, content).map_err(|e| e.to_string())?;
    }

    Ok(staging_dir)
}

/// Commits the staged files by moving them to `sandbox/` (Atomic rename where possible).
pub fn commit_staged_files(workspace: &WorkspaceRoot, staging_dir: &Path) -> Result<(), String> {
    let sandbox_dir = workspace.0.join("sandbox");

    if !staging_dir.exists() {
        return Ok(());
    }

    if let Ok(entries) = fs::read_dir(staging_dir) {
        for entry in entries.flatten() {
            let path = entry.path();
            if path.is_file() {
                let file_name = path.file_name().unwrap();
                let target_path = sandbox_dir.join(file_name);
                fs::rename(&path, &target_path).map_err(|e| e.to_string())?;
            }
        }
    }

    // Clear staging area after successful commit
    let _ = fs::remove_dir_all(staging_dir);
    Ok(())
}

/// Clears the staging directory entirely (used on observer rejection/rollback).
pub fn clear_staged_files(workspace: &WorkspaceRoot) {
    let staging_dir = workspace.0.join("sandbox").join(".determinex_staging");
    let _ = fs::remove_dir_all(staging_dir);
}

// ─────────────────────────────────────────────────────────────────────────────
// EXPLORER CONTEXT MENU — new file/folder, rename, delete
// ─────────────────────────────────────────────────────────────────────────────

/// Create a new empty file or an empty directory at `path`. Errors if
/// something already exists there — callers should prompt for a different
/// name rather than silently overwriting.
#[command]
pub fn create_path(
    workspace: tauri::State<'_, WorkspaceRoot>,
    path: String,
    is_dir: bool,
) -> Result<(), String> {
    let target = resolve_write_target(&path);
    if target.exists() {
        return Err(format!("'{}' already exists", target.display()));
    }
    if !is_safe_path(&workspace.0, &target) {
        return Err(format!(
            "Access denied: path '{}' is outside workspace boundary '{}'",
            target.display(),
            workspace.0.display()
        ));
    }
    if is_dir {
        fs::create_dir_all(&target).map_err(|e| e.to_string())?;
    } else {
        if let Some(parent) = target.parent() {
            fs::create_dir_all(parent).map_err(|e| e.to_string())?;
        }
        fs::write(&target, b"").map_err(|e| e.to_string())?;
    }
    Ok(())
}

/// Rename/move a file or directory from `from` to `to`. Both paths must be
/// inside the workspace boundary; `to` must not already exist.
#[command]
pub fn rename_path(
    workspace: tauri::State<'_, WorkspaceRoot>,
    from: String,
    to: String,
) -> Result<(), String> {
    let from_target = resolve_write_target(&from);
    let to_target = resolve_write_target(&to);
    if !from_target.exists() {
        return Err(format!("'{}' does not exist", from_target.display()));
    }
    if to_target.exists() {
        return Err(format!("'{}' already exists", to_target.display()));
    }
    if !is_safe_path(&workspace.0, &from_target) || !is_safe_path(&workspace.0, &to_target) {
        return Err(format!(
            "Access denied: path is outside workspace boundary '{}'",
            workspace.0.display()
        ));
    }
    fs::rename(&from_target, &to_target).map_err(|e| e.to_string())
}

/// Delete a file, or a directory and everything inside it. Irreversible —
/// the caller (the explorer context menu) is expected to confirm with the
/// user before invoking this.
#[command]
pub fn delete_path(workspace: tauri::State<'_, WorkspaceRoot>, path: String) -> Result<(), String> {
    let target = resolve_write_target(&path);
    if !target.exists() {
        return Err(format!("'{}' does not exist", target.display()));
    }
    if !is_safe_path(&workspace.0, &target) {
        return Err(format!(
            "Access denied: path '{}' is outside workspace boundary '{}'",
            target.display(),
            workspace.0.display()
        ));
    }
    if target.is_dir() {
        fs::remove_dir_all(&target).map_err(|e| e.to_string())
    } else {
        fs::remove_file(&target).map_err(|e| e.to_string())
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// SPEC FILE WRITER — Hive Mind DAG Orchestrator
// ─────────────────────────────────────────────────────────────────────────────

/// Open the parent directory of a workspace-relative path in the platform
/// file explorer (Explorer on Windows, Finder on macOS, Files on Linux).
/// Accepts the same relative path format that FileCommitted emits
/// (e.g. `sessions/<id>/sandbox/output.rs`).
#[command]
pub fn reveal_in_explorer(
    workspace: tauri::State<'_, WorkspaceRoot>,
    relative_path: String,
) -> Result<(), String> {
    let candidate = workspace.0.join(&relative_path);
    // Resolve symlinks so the OS can find the exact inode.
    let abs_path = fs::canonicalize(&candidate).unwrap_or(candidate); // fall back to unresolved path if file doesn't exist yet

    #[cfg(target_os = "windows")]
    {
        // `/select,<path>` opens the parent folder with the file highlighted.
        std::process::Command::new("explorer").hide_console()
            .args(["/select,", &abs_path.to_string_lossy()])
            .spawn()
            .map_err(|e| format!("Failed to open Explorer: {}", e))?;
    }
    #[cfg(target_os = "macos")]
    {
        std::process::Command::new("open").hide_console()
            .args(["-R", &abs_path.to_string_lossy()])
            .spawn()
            .map_err(|e| format!("Failed to open Finder: {}", e))?;
    }
    #[cfg(not(any(target_os = "windows", target_os = "macos")))]
    {
        let parent = abs_path.parent().unwrap_or(&abs_path);
        std::process::Command::new("xdg-open").hide_console()
            .arg(parent)
            .spawn()
            .map_err(|e| format!("Failed to open file manager: {}", e))?;
    }
    Ok(())
}

/// Write a Concept Lab MD spec to sessions/specs/spec_{timestamp}.md.
///
/// The path is always internal to the Determinex project root — resolved via
/// CARGO_MANIFEST_DIR so it works regardless of the OS working directory.
/// Returns the absolute path string so the caller can pass it to create_session.
///
/// No WorkspaceRoot boundary check needed: the write destination is computed
/// internally, not from user-supplied path input.
#[command]
pub fn write_spec_file(content: String) -> Result<String, String> {
    // Resolve project root at runtime: DETERMINEX_ROOT env var takes precedence.
    // Falls back to walking up from current_exe() until scripts/determinex_hive.py is found.
    let project_root = if let Ok(root) = std::env::var("DETERMINEX_ROOT") {
        std::path::PathBuf::from(root)
    } else {
        let mut found = std::env::current_dir().unwrap_or_else(|_| std::path::PathBuf::from("."));
        if let Ok(exe) = std::env::current_exe() {
            let mut candidate = exe.parent().map(|p| p.to_path_buf()).unwrap_or_default();
            for _ in 0..8 {
                if candidate.join("scripts").join("determinex_hive.py").exists() {
                    found = candidate.clone();
                    break;
                }
                match candidate.parent() {
                    Some(p) => candidate = p.to_path_buf(),
                    None => break,
                }
            }
        }
        found
    };

    let specs_dir = project_root.join("sessions").join("specs");
    fs::create_dir_all(&specs_dir)
        .map_err(|e| format!("Cannot create sessions/specs/ dir: {}", e))?;

    let timestamp = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map(|d| d.as_secs())
        .unwrap_or(0);

    let file_path = specs_dir.join(format!("spec_{}.md", timestamp));
    fs::write(&file_path, content.as_bytes())
        .map_err(|e| format!("Cannot write spec file: {}", e))?;

    Ok(file_path.to_string_lossy().to_string())
}

#[cfg(test)]
mod tests {
    use super::{is_safe_path, resolve_write_target};

    #[test]
    fn safe_path_allows_new_file_inside_root() {
        let root = tempfile::tempdir().expect("temp root");
        let target = root.path().join("src").join("main.rs");
        assert!(is_safe_path(root.path(), &target));
    }

    #[test]
    fn safe_path_blocks_escape_for_new_file() {
        let root = tempfile::tempdir().expect("temp root");
        let outside = root.path().parent().unwrap().join("outside.rs");
        assert!(!is_safe_path(root.path(), &outside));
    }

    #[test]
    fn resolve_write_target_keeps_absolute_paths() {
        let root = tempfile::tempdir().expect("temp root");
        let target = root.path().join("file.txt");
        assert_eq!(resolve_write_target(&target.to_string_lossy()), target);
    }
}
