use std::process::Command;
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct GitFile {
    pub path: String,
    pub status: String,
    /// The raw two-character porcelain status code (e.g. "M ", "??", "AM"),
    /// trimmed for display -- so the UI can show the real status letter
    /// instead of a hardcoded one.
    pub code: String,
    pub original_content: Option<String>,
    pub current_content: Option<String>,
}

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct GitStatusResult {
    pub branch: String,
    /// The upstream remote/branch this branch tracks (e.g. "origin/main"),
    /// if any -- None when there is no upstream configured.
    pub upstream: Option<String>,
    pub files: Vec<GitFile>,
    pub ahead: u32,
    pub behind: u32,
}

#[tauri::command]
pub fn git_status(cwd: String) -> Result<GitStatusResult, String> {
    let output = Command::new("git")
        .args(["status", "--porcelain", "-b"])
        .current_dir(&cwd)
        .output()
        .map_err(|e| e.to_string())?;

    if !output.status.success() {
        return Err(String::from_utf8_lossy(&output.stderr).to_string());
    }

    let stdout = String::from_utf8_lossy(&output.stdout);
    let mut files = Vec::new();
    let mut branch = String::from("unknown");
    let mut upstream: Option<String> = None;
    let mut ahead = 0;
    let mut behind = 0;

    for line in stdout.lines() {
        if line.starts_with("##") {
            // e.g. ## main...origin/main [ahead 1, behind 2]
            let parts: Vec<&str> = line.split_whitespace().collect();
            if parts.len() > 1 {
                let branch_info = parts[1];
                let mut segments = branch_info.split("...");
                branch = segments.next().unwrap_or("unknown").to_string();
                if let Some(remote) = segments.next() {
                    upstream = Some(remote.to_string());
                }
            }
            if line.contains("ahead") {
                if let Some(a) = line.split("ahead ").nth(1).and_then(|s| s.split(|c: char| !c.is_numeric()).next()) {
                    ahead = a.parse().unwrap_or(0);
                }
            }
            if line.contains("behind") {
                if let Some(b) = line.split("behind ").nth(1).and_then(|s| s.split(|c: char| !c.is_numeric()).next()) {
                    behind = b.parse().unwrap_or(0);
                }
            }
        } else if line.len() > 3 {
            let status_code = &line[0..2];
            let path = &line[3..];
            let index_char = status_code.chars().next().unwrap_or(' ');
            let status = if status_code == "??" {
                "untracked"
            } else if matches!(status_code, "UU" | "AA" | "DD" | "AU" | "UA" | "UD" | "DU") {
                "conflicted"
            } else if index_char != ' ' {
                // Any non-space index column means it's staged, regardless of
                // whether the worktree column also has a further unstaged
                // change (e.g. "MM") -- matches real git semantics instead of
                // only recognizing "A " as staged.
                "staged"
            } else {
                "modified"
            };
            let mut original_content = None;
            let mut current_content = None;

            if status != "untracked" {
                if let Ok(show_out) = Command::new("git")
                    .args(["show", &format!("HEAD:{}", path)])
                    .current_dir(&cwd)
                    .output()
                {
                    if show_out.status.success() {
                        original_content = Some(String::from_utf8_lossy(&show_out.stdout).to_string());
                    }
                }
            }

            if let Ok(content) = std::fs::read_to_string(std::path::Path::new(&cwd).join(path)) {
                current_content = Some(content);
            }

            files.push(GitFile {
                path: path.to_string(),
                status: status.to_string(),
                code: status_code.trim().to_string(),
                original_content,
                current_content,
            });
        }
    }

    Ok(GitStatusResult {
        branch,
        upstream,
        files,
        ahead,
        behind,
    })
}

#[tauri::command]
pub fn git_stage(cwd: String, path: String) -> Result<(), String> {
    let output = Command::new("git")
        .args(["add", &path])
        .current_dir(&cwd)
        .output()
        .map_err(|e| e.to_string())?;

    if !output.status.success() {
        return Err(String::from_utf8_lossy(&output.stderr).to_string());
    }
    Ok(())
}

#[tauri::command]
pub fn git_unstage(cwd: String, path: String) -> Result<(), String> {
    let output = Command::new("git")
        .args(["restore", "--staged", &path])
        .current_dir(&cwd)
        .output()
        .map_err(|e| e.to_string())?;

    if !output.status.success() {
        return Err(String::from_utf8_lossy(&output.stderr).to_string());
    }
    Ok(())
}

#[tauri::command]
pub fn git_stage_all(cwd: String) -> Result<(), String> {
    let output = Command::new("git")
        .args(["add", "."])
        .current_dir(&cwd)
        .output()
        .map_err(|e| e.to_string())?;

    if !output.status.success() {
        return Err(String::from_utf8_lossy(&output.stderr).to_string());
    }
    Ok(())
}

#[tauri::command]
pub fn git_commit(cwd: String, message: String) -> Result<(), String> {
    let output = Command::new("git")
        .args(["commit", "-m", &message])
        .current_dir(&cwd)
        .output()
        .map_err(|e| e.to_string())?;

    if !output.status.success() {
        return Err(String::from_utf8_lossy(&output.stderr).to_string());
    }
    Ok(())
}

#[tauri::command]
pub fn git_list_branches(cwd: String) -> Result<Vec<String>, String> {
    let output = Command::new("git")
        .args(["branch", "--format=%(refname:short)"])
        .current_dir(&cwd)
        .output()
        .map_err(|e| e.to_string())?;

    if !output.status.success() {
        return Err(String::from_utf8_lossy(&output.stderr).to_string());
    }

    let stdout = String::from_utf8_lossy(&output.stdout);
    let branches: Vec<String> = stdout
        .lines()
        .map(|s| s.trim().to_string())
        .filter(|s| !s.is_empty())
        .collect();

    Ok(branches)
}

#[tauri::command]
pub fn git_create_branch(cwd: String, name: String) -> Result<(), String> {
    let output = Command::new("git")
        .args(["checkout", "-b", &name])
        .current_dir(&cwd)
        .output()
        .map_err(|e| e.to_string())?;

    if !output.status.success() {
        return Err(String::from_utf8_lossy(&output.stderr).to_string());
    }
    Ok(())
}

#[tauri::command]
pub fn git_checkout_branch(cwd: String, name: String) -> Result<(), String> {
    let output = Command::new("git")
        .args(["checkout", &name])
        .current_dir(&cwd)
        .output()
        .map_err(|e| e.to_string())?;

    if !output.status.success() {
        return Err(String::from_utf8_lossy(&output.stderr).to_string());
    }
    Ok(())
}

#[tauri::command]
pub fn git_push(cwd: String) -> Result<(), String> {
    let output = Command::new("git")
        .args(["push"])
        .current_dir(&cwd)
        .output()
        .map_err(|e| e.to_string())?;

    if !output.status.success() {
        return Err(String::from_utf8_lossy(&output.stderr).to_string());
    }
    Ok(())
}

#[tauri::command]
pub fn git_pull(cwd: String) -> Result<(), String> {
    let output = Command::new("git")
        .args(["pull"])
        .current_dir(&cwd)
        .output()
        .map_err(|e| e.to_string())?;

    if !output.status.success() {
        return Err(String::from_utf8_lossy(&output.stderr).to_string());
    }
    Ok(())
}
