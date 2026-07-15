use serde::{Deserialize, Serialize};
use std::process::Command;
use std::fs;
use std::path::Path;

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct LspDiagnostic {
    pub line: u32,
    pub column: u32,
    pub severity: String, // "error" | "warning" | "info"
    pub message: String,
}

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct LspSymbol {
    pub name: String,
    pub kind: String, // "class" | "method" | "function" | "variable"
    pub line: u32,
}

#[tauri::command]
pub fn get_lsp_diagnostics(file_name: String) -> Result<Vec<LspDiagnostic>, String> {
    let mut diagnostics = Vec::new();
    
    // For Rust files, we can shell out to cargo check --message-format=json
    if file_name.ends_with(".rs") {
        let output = Command::new("cargo")
            .args(["check", "--message-format=json"])
            .output();
            
        if let Ok(output) = output {
            let stdout = String::from_utf8_lossy(&output.stdout);
            for line in stdout.lines() {
                if let Ok(json) = serde_json::from_str::<serde_json::Value>(line) {
                    if json["reason"] == "compiler-message" {
                        let msg = &json["message"];
                        let severity_raw = msg["level"].as_str().unwrap_or("info");
                        let severity = match severity_raw {
                            "error" => "error",
                            "warning" => "warning",
                            _ => "info",
                        };
                        
                        let text = msg["message"].as_str().unwrap_or("").to_string();
                        
                        if let Some(spans) = msg["spans"].as_array() {
                            for span in spans {
                                if span["is_primary"].as_bool().unwrap_or(false) {
                                    let span_file = span["file_name"].as_str().unwrap_or("");
                                    if span_file.ends_with(&file_name) {
                                        diagnostics.push(LspDiagnostic {
                                            line: span["line_start"].as_u64().unwrap_or(1) as u32,
                                            column: span["column_start"].as_u64().unwrap_or(1) as u32,
                                            severity: severity.to_string(),
                                            message: text.clone(),
                                        });
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    } else if file_name.ends_with(".ts") || file_name.ends_with(".tsx") {
        // Fallback for JS/TS: we could run tsc or eslint, but that takes a while.
        // For now, return an empty array rather than failing.
    }
    
    Ok(diagnostics)
}

#[tauri::command]
pub fn get_lsp_symbols(file_name: String) -> Result<Vec<LspSymbol>, String> {
    let mut symbols = Vec::new();
    
    // Fallback: read file and do rudimentary regex matching
    let path = Path::new(&file_name);
    let abs_path = if path.is_absolute() {
        path.to_path_buf()
    } else {
        // Assume workspace root
        std::env::current_dir().unwrap_or_default().join(path)
    };
    
    if let Ok(content) = fs::read_to_string(&abs_path) {
        let mut line_num = 1;
        for line in content.lines() {
            let t = line.trim();
            // Very naive heuristics for demo purposes.
            // A real Language Server Protocol integration would use an LSP client.
            if t.starts_with("fn ") || t.starts_with("pub fn ") {
                if let Some(name) = t.split("fn ").nth(1).and_then(|s| s.split('(').next()) {
                    symbols.push(LspSymbol {
                        name: name.trim().to_string(),
                        kind: "function".to_string(),
                        line: line_num,
                    });
                }
            } else if t.starts_with("class ") || t.starts_with("export class ") {
                if let Some(name) = t.split("class ").nth(1).and_then(|s| s.split_whitespace().next()) {
                    symbols.push(LspSymbol {
                        name: name.trim().to_string(),
                        kind: "class".to_string(),
                        line: line_num,
                    });
                }
            } else if t.contains("struct ") {
                if let Some(name) = t.split("struct ").nth(1).and_then(|s| s.split_whitespace().next()) {
                    symbols.push(LspSymbol {
                        name: name.trim().to_string(),
                        kind: "class".to_string(), // map struct to class for the UI
                        line: line_num,
                    });
                }
            }
            line_num += 1;
        }
    }
    
    Ok(symbols)
}
