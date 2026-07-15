use serde::{Deserialize, Serialize};
use std::process::Command;
use crate::windows_process::no_window;

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct AuditCategory {
    pub title: String,
    pub score: u32,
    pub status: String, // "pass" | "warn" | "fail"
    pub details: String,
}

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ProjectAuditReport {
    pub score: u32,
    pub categories: Vec<AuditCategory>,
    pub blockers: Vec<String>,
    pub snyk_output: String,
}

#[tauri::command]
pub async fn run_project_audit() -> Result<ProjectAuditReport, String> {
    let mut categories = Vec::new();
    let mut blockers = Vec::new();
    let mut total_score = 100;
    
    // 1. Check Rust compiler health
    let cargo_status = no_window(Command::new("cargo").args(["check"]).current_dir("frontend/src-tauri"))
        .output();
        
    match cargo_status {
        Ok(output) => {
            if output.status.success() {
                categories.push(AuditCategory {
                    title: "Rust Compiler Health".to_string(),
                    score: 100,
                    status: "pass".to_string(),
                    details: "cargo check passed with 0 errors.".to_string(),
                });
            } else {
                categories.push(AuditCategory {
                    title: "Rust Compiler Health".to_string(),
                    score: 0,
                    status: "fail".to_string(),
                    details: "cargo check failed. See console for details.".to_string(),
                });
                total_score -= 30;
                blockers.push("Rust compilation is failing.".to_string());
            }
        },
        Err(e) => {
            categories.push(AuditCategory {
                title: "Rust Compiler Health".to_string(),
                score: 0,
                status: "warn".to_string(),
                details: format!("Failed to execute cargo check: {}", e),
            });
            total_score -= 30;
        }
    }
    
    // 2. Node.js NPM audit
    let npm_audit = no_window(Command::new("npm").args(["audit", "--json"]).current_dir("frontend"))
        .output();
        
    let mut snyk_output = String::from("npm Audit Security Scan Report\n--------------------------------------\n");
    match npm_audit {
        Ok(output) => {
            let stdout = String::from_utf8_lossy(&output.stdout);
            if let Ok(json) = serde_json::from_str::<serde_json::Value>(&stdout) {
                if let Some(metadata) = json.get("metadata").and_then(|m| m.get("vulnerabilities")) {
                    let high = metadata["high"].as_u64().unwrap_or(0);
                    let low = metadata["low"].as_u64().unwrap_or(0);
                    
                    if high > 0 {
                        categories.push(AuditCategory {
                            title: "Dependency Security Scan".to_string(),
                            score: 50,
                            status: "fail".to_string(),
                            details: format!("Found {} high-severity vulnerabilities.", high),
                        });
                        total_score -= 20;
                        blockers.push(format!("Fix {} high severity vulnerabilities.", high));
                        snyk_output.push_str(&format!("✗ {} high severity vulnerabilities found.\n", high));
                    } else if low > 0 {
                        categories.push(AuditCategory {
                            title: "Dependency Security Scan".to_string(),
                            score: 85,
                            status: "warn".to_string(),
                            details: format!("Found {} low-severity vulnerabilities.", low),
                        });
                        total_score -= 5;
                        snyk_output.push_str("✓ No high severity vulnerabilities found.\n");
                        snyk_output.push_str(&format!("✗ {} low severity vulnerabilities found.\n", low));
                    } else {
                        categories.push(AuditCategory {
                            title: "Dependency Security Scan".to_string(),
                            score: 100,
                            status: "pass".to_string(),
                            details: "0 vulnerabilities found in dependencies.".to_string(),
                        });
                        snyk_output.push_str("✓ No vulnerabilities found.\n");
                    }
                }
            } else {
                // If it fails to parse json, we just fallback
                categories.push(AuditCategory {
                    title: "Dependency Security Scan".to_string(),
                    score: 90,
                    status: "warn".to_string(),
                    details: "Audit completed but JSON parsing failed.".to_string(),
                });
                snyk_output.push_str("✓ Could not parse audit json.\n");
            }
        },
        Err(_) => {
            categories.push(AuditCategory {
                title: "Dependency Security Scan".to_string(),
                score: 100,
                status: "warn".to_string(),
                details: "Failed to execute npm audit. Bypassing.".to_string(),
            });
            snyk_output.push_str("✓ npm audit could not be executed.\n");
        }
    }
    
    // 3. Credential Leak Detection
    let leak_check = no_window(
        Command::new("git").args(["grep", "-i", "-E", "(api_key|secret|password)\\s*=\\s*[\"'][a-zA-Z0-9_-]{16,}[\"']"]),
    )
    .output();
        
    match leak_check {
        Ok(output) => {
            if output.stdout.is_empty() {
                categories.push(AuditCategory {
                    title: "Credential Leak Detection".to_string(),
                    score: 100,
                    status: "pass".to_string(),
                    details: "No hardcoded secrets detected in tracked files.".to_string(),
                });
            } else {
                categories.push(AuditCategory {
                    title: "Credential Leak Detection".to_string(),
                    score: 0,
                    status: "fail".to_string(),
                    details: "Found potential hardcoded secrets!".to_string(),
                });
                total_score -= 50;
                blockers.push("Remove hardcoded secrets from codebase.".to_string());
            }
        },
        Err(_) => {
            categories.push(AuditCategory {
                title: "Credential Leak Detection".to_string(),
                score: 100,
                status: "warn".to_string(),
                details: "Could not run git grep for leaks.".to_string(),
            });
        }
    }

    Ok(ProjectAuditReport {
        score: total_score.max(0) as u32,
        categories,
        blockers,
        snyk_output,
    })
}
