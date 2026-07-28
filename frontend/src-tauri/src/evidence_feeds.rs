//! Real, file-backed readers for two flagship features that previously had
//! zero backend wiring: the flywheel training feed (FlywheelFeed.tsx) and the
//! Project Cloak privacy audit (PrivacyCockpit.tsx). Both were hardcoded
//! empty arrays with an honest "nothing loaded" empty state but no attempt to
//! read the real corpus/audit files that already exist elsewhere in the repo
//! (scripts/pb_verdict_corpus.py, scripts/verify_cloak.py). These commands
//! read those real files if present; if not, they return the same honest
//! empty result the frontend already renders -- no fabricated data either way.

use serde::Serialize;
use std::fs;
use std::io::{BufRead, BufReader};
use std::path::PathBuf;
use tauri::command;

fn project_root() -> PathBuf {
    if let Ok(root) = std::env::var("DETERMINEX_ROOT") {
        return PathBuf::from(root);
    }
    let mut found = std::env::current_dir().unwrap_or_else(|_| PathBuf::from("."));
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
}

fn truncate_chars(s: &str, n: usize) -> String {
    if s.chars().count() <= n {
        s.to_string()
    } else {
        s.chars().take(n).collect::<String>() + "…"
    }
}

// ── Flywheel training feed ─────────────────────────────────────────────────
// Reads corpus/programbench/training_corpus/pb_verdict_corpus.jsonl, the real
// append-only corpus written by scripts/pb_verdict_corpus.py::ingest_gate_result.

#[derive(Serialize)]
pub struct FlywheelPair {
    pub tool: String,
    pub lang: String,
    pub test_id: String,
    pub verdict: String, // "PASS" | "FAIL"
    pub captured_at: String,
    pub error_preview: Option<String>,
}

#[derive(Serialize)]
pub struct FlywheelSummary {
    pub total_pairs: u64,
    pub added_today: u64,
    pub pairs: Vec<FlywheelPair>,
}

#[command]
pub fn get_flywheel_feed(limit: Option<u64>) -> Result<FlywheelSummary, String> {
    let limit = limit.unwrap_or(30).max(1) as usize;
    let corpus_path = project_root()
        .join("corpus")
        .join("programbench")
        .join("training_corpus")
        .join("pb_verdict_corpus.jsonl");

    if !corpus_path.is_file() {
        return Ok(FlywheelSummary { total_pairs: 0, added_today: 0, pairs: vec![] });
    }

    let file = fs::File::open(&corpus_path).map_err(|e| e.to_string())?;
    let reader = BufReader::new(file);
    let lines: Vec<String> = reader.lines().filter_map(|l| l.ok()).collect();
    let total_pairs = lines.len() as u64;

    let today = chrono::Utc::now().format("%Y-%m-%d").to_string();
    let mut added_today = 0u64;
    let mut pairs: Vec<FlywheelPair> = Vec::new();

    for line in lines.iter().rev() {
        let Ok(val) = serde_json::from_str::<serde_json::Value>(line) else { continue };
        let meta = val.get("metadata").cloned().unwrap_or(serde_json::Value::Null);
        let captured_at = meta.get("captured_at").and_then(|v| v.as_str()).unwrap_or("").to_string();
        if captured_at.starts_with(&today) {
            added_today += 1;
        }
        if pairs.len() < limit {
            let verdict = meta
                .get("verdict")
                .and_then(|v| v.as_str())
                .unwrap_or("")
                .to_uppercase();
            let tool = meta.get("slug").and_then(|v| v.as_str()).unwrap_or("unknown").to_string();
            let lang = meta
                .get("implementation_language")
                .and_then(|v| v.as_str())
                .unwrap_or("unknown")
                .to_string();
            let test_id = meta.get("test_id").and_then(|v| v.as_str()).unwrap_or("").to_string();
            let error_preview = val
                .get("conversations")
                .and_then(|c| c.as_array())
                .and_then(|arr| arr.iter().find(|m| m.get("from").and_then(|f| f.as_str()) == Some("human")))
                .and_then(|m| m.get("value"))
                .and_then(|v| v.as_str())
                .map(|s| truncate_chars(s, 160));
            pairs.push(FlywheelPair { tool, lang, test_id, verdict, captured_at, error_preview });
        }
    }

    Ok(FlywheelSummary { total_pairs, added_today, pairs })
}

// ── Project Cloak privacy audit ────────────────────────────────────────────
// Reads the newest logs/swebench/*/cloak_audit/verify_report.json (written by
// scripts/verify_cloak.py) plus its sibling cloak_map_*.json files for a
// bounded sample of real identifier->token pairs. Returns None if no Cloak
// run has ever produced audit evidence on this machine.

#[derive(Serialize)]
pub struct CloakIdentifier {
    pub real: String,
    pub token: String,
}

#[derive(Serialize)]
pub struct CloakAuditSummary {
    pub run_dir: String,
    pub verdict: String, // "clean" | "leaked" | "unverified"
    pub total_private_identifiers: u64,
    pub restoration_failures: u64,
    pub leaks_found: u64,
    pub api_audit_present: bool,
    pub keep_list_preserved: Vec<String>,
    pub identifiers: Vec<CloakIdentifier>,
}

fn newest_file_matching(root: &std::path::Path, name: &str) -> Option<PathBuf> {
    let swebench_dir = root.join("logs").join("swebench");
    let run_dirs = fs::read_dir(&swebench_dir).ok()?;
    let mut best: Option<(std::time::SystemTime, PathBuf)> = None;
    for run_entry in run_dirs.flatten() {
        let candidate = run_entry.path().join("cloak_audit").join(name);
        if let Ok(meta) = fs::metadata(&candidate) {
            if let Ok(modified) = meta.modified() {
                let is_newer = match &best {
                    Some((t, _)) => modified > *t,
                    None => true,
                };
                if is_newer {
                    best = Some((modified, candidate));
                }
            }
        }
    }
    best.map(|(_, p)| p)
}

#[command]
pub fn get_cloak_audit_summary() -> Result<Option<CloakAuditSummary>, String> {
    let root = project_root();
    let Some(report_path) = newest_file_matching(&root, "verify_report.json") else {
        return Ok(None);
    };
    let report_text = fs::read_to_string(&report_path).map_err(|e| e.to_string())?;
    let report: serde_json::Value = serde_json::from_str(&report_text).map_err(|e| e.to_string())?;

    let audit_dir = report_path.parent().map(|p| p.to_path_buf());
    let mut keep_list_preserved: Vec<String> = Vec::new();
    let mut identifiers: Vec<CloakIdentifier> = Vec::new();

    if let Some(dir) = audit_dir {
        if let Ok(entries) = fs::read_dir(&dir) {
            for entry in entries.flatten() {
                let path = entry.path();
                let is_map = path
                    .file_name()
                    .and_then(|n| n.to_str())
                    .is_some_and(|n| n.starts_with("cloak_map_") && n.ends_with(".json"));
                if !is_map {
                    continue;
                }
                let Ok(text) = fs::read_to_string(&path) else { continue };
                let Ok(val) = serde_json::from_str::<serde_json::Value>(&text) else { continue };
                if let Some(keep) = val.get("keep_list_preserved").and_then(|v| v.as_array()) {
                    for k in keep {
                        if let Some(s) = k.as_str() {
                            if !keep_list_preserved.iter().any(|x| x == s) {
                                keep_list_preserved.push(s.to_string());
                            }
                        }
                    }
                }
                if let Some(forward) = val
                    .get("symbol_map")
                    .and_then(|m| m.get("forward"))
                    .and_then(|f| f.as_object())
                {
                    for (real, token) in forward {
                        if identifiers.len() >= 200 {
                            break;
                        }
                        if let Some(token_str) = token.as_str() {
                            identifiers.push(CloakIdentifier {
                                real: real.clone(),
                                token: token_str.to_string(),
                            });
                        }
                    }
                }
            }
        }
    }

    Ok(Some(CloakAuditSummary {
        run_dir: report.get("run_dir").and_then(|v| v.as_str()).unwrap_or("").to_string(),
        verdict: report.get("verdict").and_then(|v| v.as_str()).unwrap_or("unverified").to_string(),
        total_private_identifiers: report
            .get("total_private_identifiers")
            .and_then(|v| v.as_u64())
            .unwrap_or(0),
        restoration_failures: report.get("restoration_failures").and_then(|v| v.as_u64()).unwrap_or(0),
        leaks_found: report.get("leaks_found").and_then(|v| v.as_u64()).unwrap_or(0),
        api_audit_present: report.get("api_audit_present").and_then(|v| v.as_bool()).unwrap_or(false),
        keep_list_preserved,
        identifiers,
    }))
}
