//! benchmark_ingestor.rs — Phase 18: SWE-Bench Ingestor (The Dyno)
//!
//! Loads a JSONL benchmark dataset (SWE-Bench compatible format), runs each task
//! through the full Determinex Sentinel→Engineer→Observer pipeline, executes the
//! generated code against the task's test harness using `rustc` or `tsc`, and
//! writes a Markdown scorecard to `.determinex_staging/evals/`.
//!
//! ARCHITECTURE:
//!   • No Tauri AppHandle — same established pattern as eval_harness.rs.
//!   • Each task runs in an isolated `tempfile::TempDir` — no cross-task pollution.
//!   • Compiler execution is synchronous via `std::process::Command` (zero-VRAM).
//!   • VRAM is sampled via `nvidia-smi` at task boundaries (mirrors crucible_flood_test.rs).
//!
//! DATASET FORMAT (one JSON object per line):
//! ```json
//! {
//!   "task_id": "determinex_001",
//!   "prompt": "Write a Rust fn ...",
//!   "canonical_solution": "fn answer() { ... }",
//!   "test_cases": ["fn test_foo() { assert_eq!(foo(), 42); }"]
//! }
//! ```
//!
//! OUTPUT:
//!   `.determinex_staging/evals/scorecard_<timestamp>.md`
//!
//! PRE-CONDITIONS:
//!   • Ollama running: `ollama serve`
//!   • `rustc` on PATH (for Rust tasks)
//!   • `tsc` on PATH (for TypeScript tasks, optional)
//!   • Dataset file at path defined by `BENCHMARK_DATASET_PATH` constant
//!     (or create the placeholder dataset this test ships with).
//!
//! Run: cargo test --test benchmark_ingestor -- --nocapture
//!      cargo test --test benchmark_ingestor swe_bench_dyno -- --nocapture

mod common;

use reqwest::Client;
use serde::{Deserialize, Serialize};
use std::fs::{self, OpenOptions};
use std::io::{BufRead, BufReader, Write};
use std::path::{Path, PathBuf};
use std::process::Command;
use std::sync::{Mutex, OnceLock};
use std::time::{Duration, Instant};
use tempfile::TempDir;

#[derive(Serialize)]
struct TelemetryEvent {
    timestamp: String,
    language: String,
    task_id: String,
    original_broken_code: String,
    raw_compiler_panic: String,
    observer_review_notes: String,
    final_status: String,
}

impl TelemetryEvent {
    fn commit_to_vault(&self, path: &str) -> std::io::Result<()> {
        let mut file = OpenOptions::new().create(true).append(true).open(path)?;
        let json = serde_json::to_string(self)?;
        writeln!(file, "{}", json)
    }
}

/// Captures cases where the Observer called HALLUCINATION on code that actually passed.
/// Used to distill Observer-specific training data.
#[derive(Serialize)]
struct ObserverMistakeEvent {
    timestamp: String,
    language: String,
    task_id: String,
    passing_code: String,
    compiler_test_output: String,
    wrong_observer_verdict: String,
    wrong_observer_confidence: f32,
    wrong_observer_notes: Option<String>,
}

impl ObserverMistakeEvent {
    fn commit_to_vault(&self, path: &str) -> std::io::Result<()> {
        let mut file = OpenOptions::new().create(true).append(true).open(path)?;
        let json = serde_json::to_string(self)?;
        writeln!(file, "{}", json)
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// CONFIGURATION
// ─────────────────────────────────────────────────────────────────────────────

fn ollama_host() -> String {
    std::env::var("OLLAMA_HOST").unwrap_or_else(|_| "http://localhost:11434".to_string())
}
fn ollama_generate_url() -> String {
    format!("{}/api/generate", ollama_host())
}
fn ollama_tags_url() -> String {
    format!("{}/api/tags", ollama_host())
}
fn ollama_ps_url() -> String {
    format!("{}/api/ps", ollama_host())
}

// Defaults corrected 2026-07-31 -- up to three generations stale, so the DETERMINEX_*_MODEL
// overrides below were the only way this ever reached a real model, and unset they 404'd.
const MODEL_SENTINEL: &str = "determinex-sentinel-v5-dsl";
const MODEL_ENGINEER: &str = "determinex-engineer-v11-dsl";
const MODEL_OBSERVER: &str = "determinex-observer-v6-dsl";

const INFERENCE_TIMEOUT_SECS: u64 = 60;
/// Sentinel only generates a short JSON plan — 2048 is plenty and allocates a smaller KV-cache.
const NUM_CTX_SENTINEL: u32 = 2048;
/// Engineer (code gen) and Observer (code review) need 4096 — prompts include full code + compiler output.
const NUM_CTX: u32 = 4096;
const CONFIDENCE_THRESHOLD: f32 = 0.75;
const MAX_RETRIES: u32 = 3;

/// RAM-resident Leviathan — CPU-inferred 14B model used as escalation path.
/// Kicks in when a task has failed LEVIATHAN_ESCALATION_ROUND consecutive rounds.
/// Pulled from DETERMINEX_LEVIATHAN_MODEL env var; defaults to qwen2.5-coder:14b.
const MODEL_LEVIATHAN: &str = "qwen2.5-coder:14b";
/// Larger context window for deep failure analysis (fits ~3000 tokens of code + errors).
const NUM_CTX_LEVIATHAN: u32 = 8192;
/// Keep Leviathan resident in RAM for 30 min — avoids 30s NVMe reload per task.
const LEVIATHAN_KEEP_ALIVE_SECS: i32 = 1800;
/// CPU inference timeout: 14B model at ~4 tok/s, 500-token response ≈ 125s. 5 min is safe.
const LEVIATHAN_TIMEOUT_SECS: u64 = 300;
/// Escalate to Leviathan after this many consecutive failing rounds.
const LEVIATHAN_ESCALATION_ROUND: u32 = 2;

/// Path to the JSONL benchmark dataset.
/// Override with a real SWE-Bench file or generate one from the HumanEval dataset.
/// If the file does not exist the test creates a self-contained 5-task demo dataset.
const BENCHMARK_DATASET_PATH: &str = "../../.determinex_staging/evals/swebench_tasks.jsonl";

/// Directory where scorecards are written (relative to src-tauri/).
const SCORECARD_DIR: &str = "../../.determinex_staging/evals";

/// Claude API — auto-distillation fires inline as each task completes.
/// Model is read from DETERMINEX_CLAUDE_MODEL env var at runtime so you can update
/// without recompiling. Falls back to the hardcoded default.
/// Set ANTHROPIC_API_KEY in your environment before running.
const CLAUDE_API_URL: &str = "https://api.anthropic.com/v1/messages";
const CLAUDE_MODEL_DEFAULT: &str = "claude-opus-4-6";
const CLAUDE_DISTIL_ENGINEER_PATH: &str = "determinex_v1_distilled_claude.jsonl";
const CLAUDE_DISTIL_OBSERVER_PATH: &str = "determinex_v1_distilled_observer.jsonl";

/// Gemini API — fires in parallel with Claude for dual-perspective training data.
/// Model is read from DETERMINEX_GEMINI_MODEL env var at runtime.
/// Set GEMINI_API_KEY in your environment (or .env) before running.
const GEMINI_API_BASE: &str = "https://generativelanguage.googleapis.com/v1beta/models";
const GEMINI_MODEL_DEFAULT: &str = "gemini-3-flash-preview";
const GEMINI_DISTIL_ENGINEER_PATH: &str = "determinex_v1_distilled_gemini.jsonl";

// ─────────────────────────────────────────────────────────────────────────────
// OUTPUT FILE LOCKS — prevent interleaved JSON from concurrent distillation
// ─────────────────────────────────────────────────────────────────────────────

static CLAUDE_JSONL_LOCK: OnceLock<Mutex<()>> = OnceLock::new();
static GEMINI_JSONL_LOCK: OnceLock<Mutex<()>> = OnceLock::new();
static OBSERVER_JSONL_LOCK: OnceLock<Mutex<()>> = OnceLock::new();

// ─────────────────────────────────────────────────────────────────────────────
// ENV-OVERRIDABLE MODEL NAMES
// The loop sets DETERMINEX_ENGINEER_MODEL (etc.) in .env after each training run.
// ignite_forge.ps1 loads .env before cargo test, so no recompile is needed.
// ─────────────────────────────────────────────────────────────────────────────
static RESOLVED_SENTINEL: OnceLock<String> = OnceLock::new();
static RESOLVED_ENGINEER: OnceLock<String> = OnceLock::new();
static RESOLVED_OBSERVER: OnceLock<String> = OnceLock::new();
static RESOLVED_LEVIATHAN: OnceLock<String> = OnceLock::new();

fn sentinel_model() -> &'static str {
    RESOLVED_SENTINEL.get_or_init(|| {
        std::env::var("DETERMINEX_SENTINEL_MODEL").unwrap_or_else(|_| MODEL_SENTINEL.to_string())
    })
}
fn engineer_model() -> &'static str {
    RESOLVED_ENGINEER.get_or_init(|| {
        std::env::var("DETERMINEX_ENGINEER_MODEL").unwrap_or_else(|_| MODEL_ENGINEER.to_string())
    })
}
fn observer_model() -> &'static str {
    RESOLVED_OBSERVER.get_or_init(|| {
        std::env::var("DETERMINEX_OBSERVER_MODEL").unwrap_or_else(|_| MODEL_OBSERVER.to_string())
    })
}
fn leviathan_model() -> &'static str {
    RESOLVED_LEVIATHAN.get_or_init(|| {
        std::env::var("DETERMINEX_LEVIATHAN_MODEL").unwrap_or_else(|_| MODEL_LEVIATHAN.to_string())
    })
}

// ─────────────────────────────────────────────────────────────────────────────
// DATASET TYPES
// ─────────────────────────────────────────────────────────────────────────────

/// A single task from the benchmark dataset.
/// Fields mirror the SWE-Bench Lite and HumanEval JSONL schema.
#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct BenchmarkTask {
    /// Unique identifier — used in the scorecard and for log correlation.
    pub task_id: String,
    /// Natural-language specification fed to the Sentinel as the user prompt.
    pub prompt: String,
    /// Reference solution (not shown to the pipeline; used for comparison only).
    #[serde(default)]
    pub canonical_solution: String,
    /// One or more test harness snippets injected below the generated code.
    /// Each entry is a Rust `#[test]` function or TypeScript `describe/it` block.
    #[serde(default)]
    pub test_cases: Vec<String>,
    #[serde(default)]
    pub language: Language,
}

#[derive(Debug, Clone, PartialEq, Deserialize, Serialize)]
#[serde(rename_all = "lowercase")]
pub enum Language {
    Rust,
    Python,
    #[serde(rename = "typescript")]
    TypeScript,
    Go,
    #[serde(rename = "c++")]
    Cpp,
    Kotlin,
    Sql,
    #[serde(other)]
    Unknown,
}

impl Default for Language {
    fn default() -> Self {
        Language::Rust
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// DATASET LOADER
// ─────────────────────────────────────────────────────────────────────────────

/// Parse a JSONL file into a `Vec<BenchmarkTask>`.
///
/// Each non-empty line in the file must be a complete, standalone JSON object
/// matching the `BenchmarkTask` schema. Blank lines and lines beginning with
/// `//` (informal comment syntax) are silently skipped.
///
/// # Errors
/// Returns `Err(String)` if the file cannot be opened or if any non-skipped line
/// fails JSON parsing. The error message includes the 1-indexed line number and
/// the first 120 chars of the offending line for easy diagnosis.
pub fn load_benchmark_dataset(path: &str) -> Result<Vec<BenchmarkTask>, String> {
    let file =
        fs::File::open(path).map_err(|e| format!("Cannot open dataset at '{}': {}", path, e))?;

    let reader = BufReader::new(file);
    let mut tasks = Vec::new();

    for (i, line) in reader.lines().enumerate() {
        let line = line.map_err(|e| format!("IO error reading line {}: {}", i + 1, e))?;
        let trimmed = line.trim();

        // Skip blanks and informal comments
        if trimmed.is_empty() || trimmed.starts_with("//") {
            continue;
        }

        let task: BenchmarkTask = serde_json::from_str(trimmed).map_err(|e| {
            format!(
                "JSON parse error on line {}: {}\n  → {}",
                i + 1,
                e,
                &trimmed[..trimmed.len().min(120)]
            )
        })?;

        tasks.push(task);
    }

    Ok(tasks)
}

// ─────────────────────────────────────────────────────────────────────────────
// BUILT-IN DEMO DATASET
// ─────────────────────────────────────────────────────────────────────────────

/// Creates a 5-task JSONL demo dataset at `path` if no dataset file is found.
/// Tasks are representative of real HumanEval / SWE-Bench problem classes.
fn create_demo_dataset(path: &Path) -> Result<(), String> {
    if let Some(parent) = path.parent() {
        fs::create_dir_all(parent)
            .map_err(|e| format!("Cannot create dataset directory: {}", e))?;
    }

    let tasks: &[(&str, &str, &str, &[&str], &str)] = &[
        (
            "determinex_dyno_001",
            "Write a Rust function `fn fibonacci(n: u64) -> u64` that returns the nth Fibonacci number. Handle n=0 returning 0, n=1 returning 1. Must be iterative (no recursion). Wrap in a complete, compilable Rust lib crate.",
            "fn fibonacci(n: u64) -> u64 { let (mut a, mut b) = (0u64, 1u64); for _ in 0..n { let t = a + b; a = b; b = t; } a }",
            &[
                "#[test] fn test_fib_zero() { assert_eq!(fibonacci(0), 0); }",
                "#[test] fn test_fib_one()  { assert_eq!(fibonacci(1), 1); }",
                "#[test] fn test_fib_ten()  { assert_eq!(fibonacci(10), 55); }",
            ],
            "rust",
        ),
        (
            "determinex_dyno_002",
            "Write a Rust function `fn sum_of_squares(n: u64) -> u64` that returns the sum of squares from 1 to n inclusive. E.g. sum_of_squares(3) == 1+4+9 == 14. Wrap in a complete Rust module.",
            "fn sum_of_squares(n: u64) -> u64 { (1..=n).map(|i| i * i).sum() }",
            &[
                "#[test] fn test_sos_zero()  { assert_eq!(sum_of_squares(0), 0); }",
                "#[test] fn test_sos_three() { assert_eq!(sum_of_squares(3), 14); }",
                "#[test] fn test_sos_five()  { assert_eq!(sum_of_squares(5), 55); }",
            ],
            "rust",
        ),
        (
            "acid_test_py_001",
            "Write a Python script that uses the `multiprocessing` module to increment a shared counter 10,000 times across 4 processes. You MUST deliberately introduce a race condition by failing to use a `multiprocessing.Lock`. Then, write a `unittest` that reliably fails by catching the race condition (asserting the counter is not 40,000).",
            "import multiprocessing\ndef worker(counter, iters):\n    for _ in range(iters): counter.value += 1\ndef run():\n    c = multiprocessing.Value('i', 0)\n    procs = [multiprocessing.Process(target=worker, args=(c, 10000)) for _ in range(4)]\n    for p in procs: p.start()\n    for p in procs: p.join()\n    return c.value",
            &[
                "import unittest\nfrom solution import run\nclass TestAcid(unittest.TestCase):\n    def test_race_condition(self):\n        self.assertNotEqual(run(), 40000)\nif __name__ == '__main__':\n    unittest.main()",
            ],
            "python",
        ),
        (
            "acid_test_ts_001",
            "Write a Node.js script that demonstrates Event Loop Starvation. Create a recursive `Promise.resolve().then()` loop (a microtask) that blocks a `setTimeout` (a macrotask) from ever executing. Write a `node:test` that fails if the setTimeout does not fire within 1 second, proving the V8 microtask queue starved the event loop.",
            "export function starveLoop() { function loop() { Promise.resolve().then(loop); }; loop(); }",
            &[
                "import test from 'node:test';\nimport assert from 'node:assert';\nimport { starveLoop } from './solution';\ntest('event_loop_starvation', async () => {\n  let fired = false;\n  setTimeout(() => { fired = true; }, 100);\n  starveLoop();\n  // Wait 1 second (which will never resolve because of starvation if synchronous blocking, but we use setTimeout)\n  await new Promise(r => setTimeout(r, 1000));\n  assert.strictEqual(fired, false);\n});"
            ],
            "typescript",
        ),
    ];

    let mut jsonl = String::new();
    for (id, prompt, canonical, tests, lang) in tasks {
        let task = BenchmarkTask {
            task_id: id.to_string(),
            prompt: prompt.to_string(),
            canonical_solution: canonical.to_string(),
            test_cases: tests.iter().map(|t| t.to_string()).collect(),
            language: serde_json::from_str(&format!("\"{}\"", lang)).unwrap(),
        };
        jsonl.push_str(&serde_json::to_string(&task).unwrap());
        jsonl.push('\n');
    }

    fs::write(path, jsonl).map_err(|e| format!("Cannot write demo dataset: {}", e))
}

// ─────────────────────────────────────────────────────────────────────────────
// INLINE AUTO-DISTILLATION
// ─────────────────────────────────────────────────────────────────────────────

/// Fires a Claude distillation call immediately after a failure is vaulted.
/// Runs in a background tokio::spawn so the next task starts immediately.
/// Appends a fine-tuning JSONL entry to `output_path`.
async fn distill_engineer_failure(ev: TelemetryEvent, api_key: String, model: String) {
    let system = "You are a Senior Principal Engineer and AI training data specialist. \
        Your task is to convert a real compiler failure into a high-quality fine-tuning example. \
        The 'assistant' field MUST follow this exact three-part structure — do not skip any part:\n\
        1. ROOT CAUSE (2-3 sentences): Explain exactly what is semantically wrong and why. \
           Reference the specific error and the flawed line. Do NOT just restate the compiler message — \
           explain the underlying concept the code got wrong (ownership, type system, async contract, etc.).\n\
        2. CORRECTED CODE: The complete, working implementation. No markdown fences. No placeholders.\n\
        3. WHY THIS FIX WORKS (1-2 sentences): Explain the semantic reason this version is correct — \
           what invariant it now satisfies that the broken version violated.\n\
        Output ONLY valid JSON with keys: system, user, assistant.";

    let user_msg = format!(
        "Language: {}\nTask: {}\nFailed Code:\n{}\nCompiler Output:\n{}\nObserver Notes:\n{}",
        ev.language,
        ev.task_id,
        ev.original_broken_code,
        ev.raw_compiler_panic,
        ev.observer_review_notes
    );

    let assistant_ideal = format!(
        "ROOT CAUSE: The code failed because {}. This violates the {} contract for this pattern.\n\n\
        CORRECTED CODE:\n[see corrected implementation above]\n\n\
        WHY THIS FIX WORKS: The corrected version satisfies the compiler by addressing the root cause directly.",
        ev.raw_compiler_panic.lines().last().unwrap_or("unknown error"),
        ev.language
    );

    let entry = serde_json::json!({
        "system": system,
        "user": user_msg,
        "assistant": assistant_ideal,
        "task_id": ev.task_id,
        "language": ev.language,
        "source": "auto_distill"
    });

    // Call Claude to refine the assistant response
    let client = reqwest::Client::new();
    let body = serde_json::json!({
        "model": model,
        "max_tokens": 1024,
        "system": system,
        "messages": [{"role": "user", "content": user_msg}]
    });

    let resp = client
        .post(CLAUDE_API_URL)
        .header("x-api-key", &api_key)
        .header("anthropic-version", "2023-06-01")
        .json(&body)
        .send()
        .await;

    let refined_entry = match resp {
        Ok(r) if r.status().is_success() => match r.json::<serde_json::Value>().await {
            Ok(j) => {
                let content = j["content"][0]["text"].as_str().unwrap_or("").to_string();
                serde_json::json!({
                    "system": system,
                    "user": user_msg,
                    "assistant": content,
                    "task_id": ev.task_id,
                    "language": ev.language,
                    "source": "claude_distilled"
                })
            }
            Err(_) => entry,
        },
        _ => entry, // fallback: write synthetic entry anyway
    };

    {
        let _guard = CLAUDE_JSONL_LOCK
            .get_or_init(|| Mutex::new(()))
            .lock()
            .unwrap();
        if let Ok(mut f) = OpenOptions::new()
            .create(true)
            .append(true)
            .open(CLAUDE_DISTIL_ENGINEER_PATH)
        {
            let line = serde_json::to_string(&refined_entry).unwrap_or_default() + "\n";
            let _ = f.write_all(line.as_bytes());
            println!(
                "  · [distil/claude] {} → {}",
                ev.task_id, CLAUDE_DISTIL_ENGINEER_PATH
            );
        }
    }
}

/// Fires inline when the Observer incorrectly flags passing code as HALLUCINATION.
async fn distill_observer_mistake(ev: ObserverMistakeEvent, api_key: String, model: String) {
    let system = "You are a Senior Code Review Instructor building AI training data. \
        The Observer model made a mistake: it said HALLUCINATION on code that compiled and passed tests. \
        Output ONLY valid JSON with keys: system, user, assistant.";

    let user_msg = format!(
        "Language: {}\nPassing Code:\n{}\nCompiler Test Output:\n{}\nWrong Observer Verdict: {} ({:.0}%)\nObserver Notes: {}",
        ev.language, ev.passing_code, ev.compiler_test_output,
        ev.wrong_observer_verdict, ev.wrong_observer_confidence * 100.0,
        ev.wrong_observer_notes.as_deref().unwrap_or("none")
    );

    let assistant_ideal = format!(
        "The Observer was wrong. The compiler output shows all tests passed. \
        The correct verdict is CLEAN with confidence >= 0.95. \
        Key signal: '{}'. \
        The code implements {} correctly.",
        ev.compiler_test_output
            .lines()
            .find(|l| l.contains("ok") || l.contains("passed") || l.contains("OK"))
            .unwrap_or("tests passed"),
        ev.language
    );

    let entry = serde_json::json!({
        "system": system,
        "user": user_msg,
        "assistant": assistant_ideal,
        "task_id": ev.task_id,
        "language": ev.language,
        "source": "observer_correction"
    });

    let client = reqwest::Client::new();
    let body = serde_json::json!({
        "model": model,
        "max_tokens": 512,
        "system": system,
        "messages": [{"role": "user", "content": user_msg}]
    });

    let resp = client
        .post(CLAUDE_API_URL)
        .header("x-api-key", &api_key)
        .header("anthropic-version", "2023-06-01")
        .json(&body)
        .send()
        .await;

    let refined_entry = match resp {
        Ok(r) if r.status().is_success() => match r.json::<serde_json::Value>().await {
            Ok(j) => {
                let content = j["content"][0]["text"].as_str().unwrap_or("").to_string();
                serde_json::json!({
                    "system": system,
                    "user": user_msg,
                    "assistant": content,
                    "task_id": ev.task_id,
                    "language": ev.language,
                    "source": "observer_claude_corrected"
                })
            }
            Err(_) => entry,
        },
        _ => entry,
    };

    {
        let _guard = OBSERVER_JSONL_LOCK
            .get_or_init(|| Mutex::new(()))
            .lock()
            .unwrap();
        if let Ok(mut f) = OpenOptions::new()
            .create(true)
            .append(true)
            .open(CLAUDE_DISTIL_OBSERVER_PATH)
        {
            let line = serde_json::to_string(&refined_entry).unwrap_or_default() + "\n";
            let _ = f.write_all(line.as_bytes());
            println!(
                "  · [distil/observer] {} → {}",
                ev.task_id, CLAUDE_DISTIL_OBSERVER_PATH
            );
        }
    }
}

/// Gemini expert perspective on Observer mistakes — fires in parallel with Claude.
/// Produces additional training rows in determinex_v1_distilled_gemini.jsonl tagged
/// source=observer_gemini_corrected so both files can be merged for training.
async fn distill_observer_mistake_gemini(ev: ObserverMistakeEvent, api_key: String, model: String) {
    if api_key.is_empty() {
        return;
    }

    let system = "You are a Principal Code Review Engineer building AI training data. \
        The Observer model incorrectly labelled passing code as HALLUCINATION. \
        Explain exactly why the Observer was wrong, and what the correct CLEAN verdict reasoning should be. \
        Output ONLY valid JSON with keys: system, user, assistant.";

    let user_msg = format!(
        "Language: {}\nPassing Code:\n{}\nCompiler Test Output:\n{}\nWrong Observer Verdict: {} ({:.0}%)\nObserver Notes: {}",
        ev.language, ev.passing_code, ev.compiler_test_output,
        ev.wrong_observer_verdict, ev.wrong_observer_confidence * 100.0,
        ev.wrong_observer_notes.as_deref().unwrap_or("none")
    );

    let fallback = serde_json::json!({
        "system": system, "user": user_msg,
        "assistant": format!(
            "The Observer was incorrect. The harness confirmed all tests passed — {} code is CLEAN. \
            Correct verdict: CLEAN (confidence >= 0.95).", ev.language
        ),
        "task_id": ev.task_id, "language": ev.language,
        "source": "observer_gemini_synthetic"
    });

    let url = format!(
        "{}/{}:generateContent?key={}",
        GEMINI_API_BASE, model, api_key
    );
    let body = serde_json::json!({
        "systemInstruction": { "parts": [{ "text": system }] },
        "contents": [{ "role": "user", "parts": [{ "text": user_msg }] }],
        "generationConfig": { "maxOutputTokens": 768 }
    });

    let client = reqwest::Client::new();
    let resp = client.post(&url).json(&body).send().await;

    let final_entry = match resp {
        Ok(r) if r.status().is_success() => match r.json::<serde_json::Value>().await {
            Ok(j) => {
                let text = j["candidates"][0]["content"]["parts"][0]["text"]
                    .as_str()
                    .unwrap_or("")
                    .to_string();
                if text.is_empty() {
                    fallback
                } else {
                    serde_json::json!({
                        "system": system, "user": user_msg, "assistant": text,
                        "task_id": ev.task_id, "language": ev.language,
                        "source": "observer_gemini_corrected"
                    })
                }
            }
            Err(_) => fallback,
        },
        Ok(r) => {
            eprintln!("[GEMINI/OBS] HTTP {} for {}", r.status(), ev.task_id);
            fallback
        }
        Err(e) => {
            eprintln!("[GEMINI/OBS] Request failed for {}: {}", ev.task_id, e);
            fallback
        }
    };

    {
        let _guard = GEMINI_JSONL_LOCK
            .get_or_init(|| Mutex::new(()))
            .lock()
            .unwrap();
        if let Ok(mut f) = OpenOptions::new()
            .create(true)
            .append(true)
            .open(GEMINI_DISTIL_ENGINEER_PATH)
        {
            let line = serde_json::to_string(&final_entry).unwrap_or_default() + "\n";
            let _ = f.write_all(line.as_bytes());
            println!(
                "  · [distil/gemini/obs] {} → {}",
                ev.task_id, GEMINI_DISTIL_ENGINEER_PATH
            );
        }
    }
}

///
/// Produces `determinex_v1_distilled_gemini.jsonl` — same schema as the Claude file so
/// both can be merged into a single training dataset for diverse signal coverage.
/// Gemini 3.1 Flash is used: fast enough to complete before the next round starts.
async fn distill_engineer_failure_gemini(ev: TelemetryEvent, api_key: String, model: String) {
    if api_key.is_empty() {
        return;
    }

    let system = "You are a Principal Engineer specialising in polyglot systems. \
        A junior AI wrote code that failed compilation or tests. \
        Your response MUST follow this exact three-part structure:\n\
        1. ROOT CAUSE (2-3 sentences): Identify the specific concept the code got wrong — \
           ownership, async semantics, type mismatch, API misuse, etc. Do NOT just echo the \
           error message; explain the underlying invariant that was violated.\n\
        2. CORRECTED CODE: The complete working implementation. No markdown fences. No placeholders.\n\
        3. WHY THIS FIX WORKS (1-2 sentences): State which contract or invariant the fix now satisfies.\n\
        Output ONLY valid JSON with keys: system, user, assistant.";

    let user_msg =
        format!(
        "Language: {}\nTask: {}\nFailed Code:\n{}\nCompiler/Test Output:\n{}\nObserver Notes:\n{}",
        ev.language, ev.task_id, ev.original_broken_code,
        ev.raw_compiler_panic, ev.observer_review_notes
    );

    // Synthetic fallback entry (written if API call fails)
    let fallback = serde_json::json!({
        "system": system, "user": user_msg,
        "assistant": format!(
            "ROOT CAUSE: The {} code violated a language contract: {}.\n\nCORRECTED CODE:\n[fix required]\n\nWHY THIS FIX WORKS: Addresses the root violation directly.",
            ev.language, ev.raw_compiler_panic.lines().last().unwrap_or("unknown")),
        "task_id": ev.task_id, "language": ev.language, "source": "gemini_synthetic"
    });

    let url = format!(
        "{}/{}:generateContent?key={}",
        GEMINI_API_BASE, model, api_key
    );

    let body = serde_json::json!({
        "systemInstruction": { "parts": [{ "text": system }] },
        "contents": [{ "role": "user", "parts": [{ "text": user_msg }] }],
        "generationConfig": { "maxOutputTokens": 1024 }
    });

    let client = reqwest::Client::new();
    let resp = client.post(&url).json(&body).send().await;

    let final_entry = match resp {
        Ok(r) if r.status().is_success() => match r.json::<serde_json::Value>().await {
            Ok(j) => {
                let text = j["candidates"][0]["content"]["parts"][0]["text"]
                    .as_str()
                    .unwrap_or("")
                    .to_string();
                if text.is_empty() {
                    fallback
                } else {
                    serde_json::json!({
                        "system": system, "user": user_msg, "assistant": text,
                        "task_id": ev.task_id, "language": ev.language,
                        "source": "gemini_distilled"
                    })
                }
            }
            Err(_) => fallback,
        },
        Ok(r) => {
            eprintln!("[GEMINI] HTTP {} for task {}", r.status(), ev.task_id);
            fallback
        }
        Err(e) => {
            eprintln!("[GEMINI] Request failed for {}: {}", ev.task_id, e);
            fallback
        }
    };

    {
        let _guard = GEMINI_JSONL_LOCK
            .get_or_init(|| Mutex::new(()))
            .lock()
            .unwrap();
        if let Ok(mut f) = OpenOptions::new()
            .create(true)
            .append(true)
            .open(GEMINI_DISTIL_ENGINEER_PATH)
        {
            let line = serde_json::to_string(&final_entry).unwrap_or_default() + "\n";
            let _ = f.write_all(line.as_bytes());
            println!(
                "  · [distil/gemini]  {} → {}",
                ev.task_id, GEMINI_DISTIL_ENGINEER_PATH
            );
        }
    }
}

#[derive(Serialize)]
struct OllamaOptions {
    num_ctx: u32,
}

#[derive(Serialize)]
struct OllamaRequest<'a> {
    model: &'a str,
    prompt: &'a str,
    stream: bool,
    format: &'a str,
    keep_alive: i32,
    options: OllamaOptions,
}

#[derive(Deserialize, Debug)]
struct OllamaResponse {
    response: String,
    done: bool,
}

// ─────────────────────────────────────────────────────────────────────────────
// PIPELINE DOMAIN TYPES
// ─────────────────────────────────────────────────────────────────────────────

fn deserialize_flexible_seq<'de, D>(de: D) -> Result<Vec<String>, D::Error>
where
    D: serde::Deserializer<'de>,
{
    use serde::de::{SeqAccess, Visitor};
    use std::fmt;
    struct FlexSeq;
    impl<'de> Visitor<'de> for FlexSeq {
        type Value = Vec<String>;
        fn expecting(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
            write!(f, "array of strings or numbers")
        }
        fn visit_seq<A: SeqAccess<'de>>(self, mut seq: A) -> Result<Vec<String>, A::Error> {
            let mut out = Vec::new();
            while let Some(v) = seq.next_element::<serde_json::Value>()? {
                out.push(match &v {
                    serde_json::Value::String(s) => s.clone(),
                    other => other.to_string(),
                });
            }
            Ok(out)
        }
    }
    de.deserialize_seq(FlexSeq)
}

#[derive(Debug, Clone, Serialize, Deserialize)]
struct SentinelPlan {
    title: String,
    #[serde(deserialize_with = "deserialize_flexible_seq")]
    steps: Vec<String>,
    #[serde(default, deserialize_with = "deserialize_flexible_seq")]
    audit_targets: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
struct EngineerCode {
    language: String,
    code: String,
    #[serde(default)]
    files_affected: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
struct ObserverVerdict {
    verdict: String,
    issues: Vec<String>,
    confidence: f32,
    review_notes: Option<String>,
}

// ─────────────────────────────────────────────────────────────────────────────
// INFRASTRUCTURE
// ─────────────────────────────────────────────────────────────────────────────

const OLLAMA_TAGS: &str = "http://127.0.0.1:11434/api/tags";
const OLLAMA_GENERATE: &str = "http://127.0.0.1:11434/api/generate";


fn build_client() -> Client {
    Client::builder()
        .timeout(Duration::from_secs(INFERENCE_TIMEOUT_SECS))
        .build()
        .expect("reqwest client build failed")
}

async fn ollama_is_reachable(client: &Client) -> bool {
    client
        .get(OLLAMA_TAGS)
        .timeout(Duration::from_secs(2))
        .send()
        .await
        .map(|r| r.status().is_success())
        .unwrap_or(false)
}

async fn call_ollama(
    client: &Client,
    model: &str,
    prompt: &str,
    num_ctx: u32,
) -> Result<String, String> {
    let body = OllamaRequest {
        model,
        prompt,
        stream: false,
        format: "json",
        keep_alive: 0,
        options: OllamaOptions { num_ctx },
    };
    let resp = client
        .post(OLLAMA_GENERATE)
        .json(&body)
        .send()
        .await
        .map_err(|e| format!("Transport: {}", e))?;
    if !resp.status().is_success() {
        return Err(format!("Ollama HTTP {}", resp.status()));
    }
    let parsed: OllamaResponse = resp.json().await.map_err(|e| format!("Parse: {}", e))?;
    if !parsed.done {
        return Err("Response not done=true".to_string());
    }
    Ok(parsed.response)
}

/// Like call_ollama, but keeps the model in RAM (long keep_alive) and uses a
/// 5-minute timeout — necessary for CPU-inferred models like Leviathan 14B.
async fn call_ollama_ram(
    client: &Client,
    model: &str,
    prompt: &str,
    num_ctx: u32,
) -> Result<String, String> {
    let body = OllamaRequest {
        model,
        prompt,
        stream: false,
        format: "json",
        keep_alive: LEVIATHAN_KEEP_ALIVE_SECS, // stay resident in system RAM
        options: OllamaOptions { num_ctx },
    };
    let resp = client
        .post(OLLAMA_GENERATE)
        .timeout(Duration::from_secs(LEVIATHAN_TIMEOUT_SECS))
        .json(&body)
        .send()
        .await
        .map_err(|e| format!("Leviathan transport: {}", e))?;
    if !resp.status().is_success() {
        return Err(format!("Leviathan HTTP {}", resp.status()));
    }
    let parsed: OllamaResponse = resp
        .json()
        .await
        .map_err(|e| format!("Leviathan parse: {}", e))?;
    if !parsed.done {
        return Err("Leviathan response not done=true".to_string());
    }
    Ok(parsed.response)
}

fn extract_json(raw: &str) -> &str {
    let t = raw.trim();
    if let (Some(s), Some(e)) = (t.find('{'), t.rfind('}')) {
        &t[s..=e]
    } else {
        t
    }
}

/// Strip markdown code fences that the Engineer model sometimes wraps around code inside JSON.
/// Handles ```lang\n...\n``` and bare ```\n...\n```.
fn strip_code_fences(code: &str) -> String {
    let s = code.trim();
    if !s.starts_with("```") {
        return s.to_string();
    }
    // Skip the opening fence line (``` or ```rust etc.)
    let rest = &s[3..];
    let body = match rest.find('\n') {
        Some(nl) => &rest[nl + 1..],
        None => return s.to_string(), // no newline after fence — malformed, return as-is
    };
    // Strip trailing ```
    let body = body.trim_end();
    if body.ends_with("```") {
        body[..body.len() - 3].trim_end().to_string()
    } else {
        body.to_string()
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// VRAM SAMPLER
// ─────────────────────────────────────────────────────────────────────────────

fn sample_vram_mb() -> Option<u64> {
    Command::new("nvidia-smi")
        .args(["--query-gpu=memory.used", "--format=csv,noheader,nounits"])
        .output()
        .ok()
        .and_then(|o| String::from_utf8_lossy(&o.stdout).trim().parse().ok())
}

// ─────────────────────────────────────────────────────────────────────────────
// THREE-STAGE PIPELINE
// ─────────────────────────────────────────────────────────────────────────────

async fn run_sentinel(client: &Client, task: &BenchmarkTask) -> Result<SentinelPlan, String> {
    let prompt = format!(
        r#"You are the Determinex Sentinel. Analyze the following request and produce a structured execution plan.
You MUST output ONLY valid JSON matching this exact schema — no markdown, no explanation, no extra keys:
{{
  "title": "short descriptive title",
  "steps": ["step 1", "step 2", "..."],
  "audit_targets": ["specific thing to verify 1", "..."]
}}
HARD RULE: Output ONLY the JSON object. No other text.
USER REQUEST: {prompt}"#,
        prompt = task.prompt
    );
    let raw = call_ollama(client, sentinel_model(), &prompt, NUM_CTX_SENTINEL).await?;
    let json = extract_json(&raw);
    serde_json::from_str::<SentinelPlan>(json)
        .map_err(|e| format!("Sentinel parse: {e}\nRaw: {raw}"))
}

async fn run_engineer(
    client: &Client,
    task: &BenchmarkTask,
    plan: &SentinelPlan,
    retry_hint: &str,
) -> Result<EngineerCode, String> {
    let steps = plan.steps.join("\n  • ");
    let prompt = format!(
        r#"You are the Determinex Engineer. You write production-quality {lang} code.
ENVIRONMENT CONSTRAINTS: You are operating in a strict single-file sandbox. 
For Rust: You run in an air-gapped `rustc` compiler without a Cargo.toml. NO external crates (e.g., `tokio`, `serde`) are available. You MUST use standard library primitives like `std::thread` and `std::sync`. NEVER use `#[tokio::test]` — it will NOT compile. Write plain `#[test]` functions. NEVER use `.await` inside sync test functions.
For Python: Beware of mutable default arguments triggering data leaks across functional states.
For TypeScript: Beware of `Array.forEach` swallowing async Promises. Properly await synchronous events.
For SQL: Use ONLY standard SQLite syntax. NO PostgreSQL extensions (no SERIAL, no PL/pgSQL, no LANGUAGE plpgsql). Use INTEGER PRIMARY KEY AUTOINCREMENT instead of SERIAL. Use datetime('now') instead of NOW().
For Go: The test file uses Go's `testing` package with `func TestXxx(t *testing.T)`. Your solution code MUST use `package main`. Write the implementation only — do NOT write your own main() function unless the test requires it.
For C++: Do NOT use any external test frameworks. NO gtest, NO catch2, NO boost.test. Use ONLY `<cassert>` with `assert()` for all assertions, and `<iostream>` for output. The code must compile with `g++ -std=c++17` and no extra flags.
For C++: Track memory destruction ordering strictly to avoid use-after-free pointer captures.
For Kotlin: Use ONLY kotlin stdlib and java.util.concurrent. NO kotlinx.coroutines, NO JUnit, NO external libraries. Compiled with `kotlinc -include-runtime`. When the test provides `fun main()`, do NOT add your own main() — write the class/function only.

EXECUTION PLAN:
  Title : {title}
  Steps :
  • {steps}

ORIGINAL REQUEST: {task_prompt}
{retry}

You MUST output ONLY valid JSON matching this exact schema — no markdown, no explanation:
{{
  "language": "{lang}",
  "code": "<full rust code here>",
  "files_affected": ["src/lib.rs"]
}}"#,
        lang = format!("{:?}", task.language).to_lowercase(),
        title = plan.title,
        steps = steps,
        task_prompt = task.prompt,
        retry = retry_hint
    );
    let raw = call_ollama(client, engineer_model(), &prompt, NUM_CTX).await?;
    let json = extract_json(&raw);
    let mut parsed = serde_json::from_str::<EngineerCode>(json)
        .map_err(|e| format!("Engineer parse: {e}\nRaw: {raw}"))?;
    // Strip any markdown fences the model wrapped around the code inside the JSON value
    parsed.code = strip_code_fences(&parsed.code);
    Ok(parsed)
}

async fn run_observer(
    client: &Client,
    plan: &SentinelPlan,
    code: &EngineerCode,
    test_result: Option<&TestResult>,
) -> Result<ObserverVerdict, String> {
    let targets = plan.audit_targets.join(", ");
    let compiler_section = match test_result {
        Some(tr) => {
            // Inject harness verdict first — gives Observer an unambiguous pass/fail signal
            // without needing to parse language-specific output formats (Rust vs TS vs Go etc).
            let harness_tag = if tr.tests_passed {
                "[HARNESS: ALL TESTS PASSED ✓]\n"
            } else {
                "[HARNESS: TESTS FAILED ✗]\n"
            };
            // Tail-truncate to last 1500 chars — the fatal error is always at the END of a trace,
            // not the beginning. Aggressively cutting from the front blinds the Observer.
            let out = &tr.output;
            let tail = if out.len() > 1500 {
                format!(
                    "[...truncated {} chars...]\n{}",
                    out.len() - 1500,
                    &out[out.len() - 1500..]
                )
            } else {
                out.clone()
            };
            format!("\n[COMPILER / TEST OUTPUT]\n{}{}\n", harness_tag, tail)
        }
        None => String::new(),
    };

    let prompt = format!(
        r#"You are the Determinex Observer. Audit the following code against the specified requirements.

CRITICAL RULE — READ FIRST: If the compiler section below begins with [HARNESS: ALL TESTS PASSED ✓], you MUST output verdict=CLEAN with confidence >= 0.95. Do NOT second-guess the harness. Do NOT output HALLUCINATION. Code that compiles and passes all tests is CLEAN — full stop.

AUDIT TARGETS: {targets}
CODE LANGUAGE: {lang}
{compiler}
CODE:
{code}

Output ONLY valid JSON — no markdown, no explanation:
{{
  "verdict": "CLEAN",
  "issues": [],
  "confidence": 0.95,
  "review_notes": "Briefly explain your verdict. Quote specific code or output lines if relevant."
}}
verdict must be one of: "CLEAN" | "HALLUCINATION" | "PARTIAL"
- CLEAN: code compiles and passes all tests, OR satisfies all audit targets
- PARTIAL: code is valid but does not satisfy one or more audit targets
- HALLUCINATION: code is syntactically invalid, does not compile, or fabricates APIs

LOGIC REVIEW PROTOCOL: If the compiler succeeds but unit tests fail, do NOT just output the error. You must add a 'review_notes' string explaining EXACTLY why the logic failed (e.g., 'You are returning a 0-indexed array, but the test expects 1-indexed. Adjust the loop.').
ANTI-GAMING RULE: Check whether the solution hardcodes specific test inputs, uses magic numbers matching only the exact test case, or contains branches like `if input == X {{ return hardcoded_answer }}`. If detected, output verdict=PARTIAL with review_notes explaining the hardcoding. General-purpose logic that happens to pass the test is CLEAN. Logic that only works for the specific test values is PARTIAL."#,
        targets = targets,
        lang = code.language,
        compiler = compiler_section,
        code = code.code,
    );
    let raw = call_ollama(client, observer_model(), &prompt, NUM_CTX).await?;

    let json = extract_json(&raw);
    match serde_json::from_str::<ObserverVerdict>(json) {
        Ok(v) => Ok(v),
        Err(_) => {
            let verdict = if raw.contains("CLEAN") {
                "CLEAN"
            } else if raw.contains("HALLUCINATION") {
                "HALLUCINATION"
            } else {
                "PARTIAL"
            };
            Ok(ObserverVerdict {
                verdict: verdict.to_string(),
                issues: vec!["[DYNO] Observer truncated — verdict inferred".to_string()],
                confidence: 0.5,
                review_notes: None,
            })
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// LEVIATHAN ESCALATION — RAM-resident 14B fallback
// ─────────────────────────────────────────────────────────────────────────────
//
// Called when a task has failed LEVIATHAN_ESCALATION_ROUND consecutive rounds.
// Leviathan receives the full failure context (broken code + compiler output)
// and produces a complete replacement implementation.
//
// VRAM note: Leviathan uses keep_alive=1800 and runs on CPU (Ollama num_gpu 0
// in its Modelfile). VRAM stays free for Sentinel/Engineer/Observer hot-swap.
// System RAM: qwen2.5-coder:14b Q4_K_M ≈ 8.5 GB — fits in 19 GB pool.

async fn run_leviathan(
    client: &Client,
    task: &BenchmarkTask,
    plan: &SentinelPlan,
    failed_code: &str,
    compiler_output: &str,
    retry_hint: &str,
) -> Result<EngineerCode, String> {
    let steps = plan.steps.join("\n  • ");
    let lang = format!("{:?}", task.language).to_lowercase();

    let failure_section = if failed_code.is_empty() {
        String::from("No previous code was produced.")
    } else {
        // Tail-truncate to keep the prompt within 8192 ctx
        let code_preview = if failed_code.len() > 2000 {
            format!(
                "[...truncated...]\n{}",
                &failed_code[failed_code.len() - 2000..]
            )
        } else {
            failed_code.to_string()
        };
        let err_preview = if compiler_output.len() > 1500 {
            format!(
                "[...truncated...]\n{}",
                &compiler_output[compiler_output.len() - 1500..]
            )
        } else {
            compiler_output.to_string()
        };
        format!(
            "FAILED CODE (previous attempt):\n```\n{}\n```\n\nFAILURE OUTPUT:\n```\n{}\n```",
            code_preview, err_preview
        )
    };

    let prompt = format!(
        r#"You are Leviathan, a senior 14B code architect called in as a last resort.
A smaller model failed to solve this task after multiple attempts. You have full visibility of what went wrong.

STRICT ENVIRONMENT CONSTRAINTS (must be honoured exactly):
- Rust: air-gapped rustc, no Cargo.toml, no external crates. Use only std. No tokio::test, no .await in sync tests.
- Python: no mutable default argument leaks. No external packages beyond stdlib.
- TypeScript: properly await Promises inside forEach equivalents.
- SQL: SQLite ONLY. No PostgreSQL syntax (no SERIAL, use INTEGER PRIMARY KEY AUTOINCREMENT; use datetime('now') not NOW()).
- Go: package main, no external test frameworks. Use testing package only.
- C++: no gtest/catch2/boost. Use only <cassert> with assert() + <iostream>. Compile with g++ -std=c++17.
- Kotlin: stdlib + java.util.concurrent ONLY. No kotlinx.coroutines or JUnit. Compiled with kotlinc -include-runtime.

EXECUTION PLAN:
  Title : {title}
  Steps :
  • {steps}

ORIGINAL REQUEST: {task_prompt}

{failure_section}

{retry}

TASK: Analyse the failure. Identify the root cause. Write a complete, correct {lang} implementation that avoids all the previous mistakes.

You MUST output ONLY valid JSON with no markdown, no explanation outside the JSON:
{{
  "language": "{lang}",
  "code": "<complete working implementation here>",
  "files_affected": ["src/lib.rs"]
}}"#,
        title = plan.title,
        steps = steps,
        task_prompt = task.prompt,
        failure_section = failure_section,
        retry = retry_hint,
        lang = lang,
    );

    let raw = call_ollama_ram(client, leviathan_model(), &prompt, NUM_CTX_LEVIATHAN).await?;
    let json = extract_json(&raw);
    let mut parsed = serde_json::from_str::<EngineerCode>(json)
        .map_err(|e| format!("Leviathan parse: {e}\nRaw: {raw}"))?;
    parsed.code = strip_code_fences(&parsed.code);
    Ok(parsed)
}

// ─────────────────────────────────────────────────────────────────────────────
// COMPILER EXECUTOR
// ─────────────────────────────────────────────────────────────────────────────

/// Result of running the test harness against generated code.
#[derive(Debug, Clone)]
pub struct TestResult {
    /// Did the code compile without errors?
    pub compiled: bool,
    /// Did all test cases pass?
    pub tests_passed: bool,
    /// Full compiler + test output for the scorecard.
    pub output: String,
    /// How many individual test functions passed.
    pub passed_count: usize,
    /// Total test functions attempted.
    pub total_count: usize,
}

pub fn execute_task_tests(
    lang: &Language,
    tmp: &Path,
    code: &str,
    test_cases: &[String],
) -> TestResult {
    let mut tests = String::new();
    for tc in test_cases {
        tests.push_str(tc);
        tests.push('\n');
    }

    match lang {
        Language::Rust => {
            let src_path = tmp.join("solution.rs");
            let bin_path = tmp.join("solution_test");

            let mut source = String::new();
            source.push_str("// Determinex Dyno — generated\n");
            source.push_str("#![allow(dead_code, unused_variables, unused_imports)]\n\n");
            source.push_str(code);
            if !test_cases.is_empty() {
                source.push_str("\n\n#[cfg(test)]\nmod dyno_tests {\n    use super::*;\n");
                for tc in test_cases {
                    source.push_str("    ");
                    source.push_str(tc);
                    source.push('\n');
                }
                source.push_str("}\n");
            }

            if let Err(e) = fs::write(&src_path, &source) {
                return TestResult {
                    compiled: false,
                    tests_passed: false,
                    output: format!("Failed to write source: {}", e),
                    passed_count: 0,
                    total_count: test_cases.len(),
                };
            }

            let compile_out = Command::new("rustc")
                .args(["--test", "--edition=2021", "-o"])
                .arg(&bin_path)
                .arg(&src_path)
                .output();

            let compile_result = match compile_out {
                Err(e) => {
                    return TestResult {
                        compiled: false,
                        tests_passed: false,
                        output: format!("rustc error: {}", e),
                        passed_count: 0,
                        total_count: test_cases.len(),
                    }
                }
                Ok(r) => r,
            };

            if !compile_result.status.success() {
                return TestResult {
                    compiled: false,
                    tests_passed: false,
                    output: format!(
                        "COMPILE FAIL:\n{}",
                        String::from_utf8_lossy(&compile_result.stderr)
                    ),
                    passed_count: 0,
                    total_count: test_cases.len(),
                };
            }

            let run_out = Command::new(&bin_path)
                .args(["--test-threads=1", "--nocapture"])
                .current_dir(tmp)
                .output();

            match run_out {
                Err(e) => TestResult {
                    compiled: true,
                    tests_passed: false,
                    output: format!("Test exec failed: {}", e),
                    passed_count: 0,
                    total_count: test_cases.len(),
                },
                Ok(r) => {
                    let combined = format!(
                        "{}\n{}",
                        String::from_utf8_lossy(&r.stdout),
                        String::from_utf8_lossy(&r.stderr)
                    );
                    let passed_count = combined.matches(" ok").count();
                    let failed_count = combined.matches("FAILED").count();
                    let tests_passed = r.status.success();
                    TestResult {
                        compiled: true,
                        tests_passed,
                        output: combined,
                        passed_count,
                        total_count: (passed_count + failed_count).max(test_cases.len()),
                    }
                }
            }
        }

        Language::Python => {
            let src_path = tmp.join("solution.py");
            let test_path = tmp.join("test_solution.py");
            if fs::write(&src_path, code).is_err() || fs::write(&test_path, &tests).is_err() {
                return TestResult {
                    compiled: false,
                    tests_passed: false,
                    output: "Python IO Fail".to_string(),
                    passed_count: 0,
                    total_count: test_cases.len(),
                };
            }
            // Pass the module name (no .py extension) — `python -m unittest test_solution.py` is invalid
            let run_out = Command::new("python")
                .args(["-m", "unittest", "test_solution"])
                .current_dir(tmp)
                .output();
            match run_out {
                Err(e) => TestResult {
                    compiled: true,
                    tests_passed: false,
                    output: format!("Python execution error: {}", e),
                    passed_count: 0,
                    total_count: test_cases.len(),
                },
                Ok(r) => {
                    let combined = format!(
                        "{}\n{}",
                        String::from_utf8_lossy(&r.stdout),
                        String::from_utf8_lossy(&r.stderr)
                    );
                    let tests_passed = r.status.success();
                    TestResult {
                        compiled: true,
                        tests_passed,
                        output: combined,
                        passed_count: if tests_passed { test_cases.len() } else { 0 },
                        total_count: test_cases.len(),
                    }
                }
            }
        }
        Language::TypeScript => {
            let appdata = std::env::var("APPDATA").unwrap_or_else(|_| {
                dirs::data_dir()
                    .map(|p: std::path::PathBuf| p.to_string_lossy().to_string())
                    .unwrap_or_default()
            });
            let tsx_path = format!("{}\\npm\\tsx.ps1", appdata);

            // If the test imports from './solution', write separate files so the import resolves
            // correctly. Concatenating both into solution.ts causes duplicate symbol errors because
            // tsx resolves `import { X } from './solution'` back to the same file.
            let needs_split = test_cases
                .iter()
                .any(|tc| tc.contains("from './solution'") || tc.contains("from \"./solution\""));

            let run_file = if needs_split {
                let sol_path = tmp.join("solution.ts");
                let test_path = tmp.join("test_solution.ts");
                if fs::write(&sol_path, code).is_err() || fs::write(&test_path, &tests).is_err() {
                    return TestResult {
                        compiled: false,
                        tests_passed: false,
                        output: "TS IO Fail".to_string(),
                        passed_count: 0,
                        total_count: test_cases.len(),
                    };
                }
                "test_solution.ts"
            } else {
                // Single-file: test uses symbols defined directly in solution (no import needed)
                let src_path = tmp.join("solution.ts");
                let mut source = String::new();
                source.push_str(code);
                source.push_str("\n\n");
                source.push_str(&tests);
                if fs::write(&src_path, &source).is_err() {
                    return TestResult {
                        compiled: false,
                        tests_passed: false,
                        output: "TS IO Fail".to_string(),
                        passed_count: 0,
                        total_count: test_cases.len(),
                    };
                }
                "solution.ts"
            };

            let run_out = Command::new("powershell")
                .args([
                    "-NoProfile",
                    "-NonInteractive",
                    "-File",
                    &tsx_path,
                    "--test",
                    run_file,
                ])
                .current_dir(tmp)
                .output();
            match run_out {
                Err(e) => TestResult {
                    compiled: true,
                    tests_passed: false,
                    output: format!("TypeScript execution error: {}", e),
                    passed_count: 0,
                    total_count: test_cases.len(),
                },
                Ok(r) => {
                    let combined = format!(
                        "{}\n{}",
                        String::from_utf8_lossy(&r.stdout),
                        String::from_utf8_lossy(&r.stderr)
                    );
                    let tests_passed = r.status.success();
                    TestResult {
                        compiled: true,
                        tests_passed,
                        output: combined,
                        passed_count: if tests_passed { test_cases.len() } else { 0 },
                        total_count: test_cases.len(),
                    }
                }
            }
        }

        Language::Go => {
            // Write solution as solution.go and test cases as solution_test.go
            let sol_path = tmp.join("solution.go");
            let test_path = tmp.join("solution_test.go");
            // Ensure solution has package main declaration
            let sol_source = if code.contains("package ") {
                code.to_string()
            } else {
                format!("package main\n\n{}", code)
            };
            // Ensure test file has package main
            let test_source = if tests.contains("package ") {
                tests.clone()
            } else {
                format!("package main\n\n{}", tests)
            };
            fs::write(&sol_path, &sol_source).unwrap();
            fs::write(&test_path, &test_source).unwrap();
            // Initialize a go module so `go test` works in the temp dir
            let _ = Command::new("go")
                .args(["mod", "init", "determinex_sandbox"])
                .current_dir(tmp)
                .output();
            let out = Command::new("go")
                .args(["test", "-v", "-timeout", "10s", "./..."])
                .current_dir(tmp)
                .output();
            match out {
                Ok(r) => {
                    let combined = format!(
                        "{}{}",
                        String::from_utf8_lossy(&r.stdout),
                        String::from_utf8_lossy(&r.stderr)
                    );
                    let tests_passed = r.status.success();
                    TestResult {
                        compiled: true,
                        tests_passed,
                        output: combined,
                        passed_count: if tests_passed { test_cases.len() } else { 0 },
                        total_count: test_cases.len(),
                    }
                }
                Err(e) => TestResult {
                    compiled: false,
                    tests_passed: false,
                    output: format!("Go execution error: {}", e),
                    passed_count: 0,
                    total_count: test_cases.len(),
                },
            }
        }
        Language::Cpp => {
            let src_path = tmp.join("main.cpp");
            let bin_path = tmp.join("main.out");
            let mut source = code.to_string();
            source.push_str("\n\n");
            source.push_str(&tests);
            fs::write(&src_path, &source).unwrap();
            let compile = Command::new("g++")
                .args(["-std=c++17", "main.cpp", "-o", "main.out"])
                .current_dir(tmp)
                .output();
            if let Ok(c) = compile {
                if !c.status.success() {
                    return TestResult {
                        compiled: false,
                        tests_passed: false,
                        output: String::from_utf8_lossy(&c.stderr).to_string(),
                        passed_count: 0,
                        total_count: test_cases.len(),
                    };
                }
            }
            let out = Command::new(&bin_path).current_dir(tmp).output();
            match out {
                Ok(r) => TestResult {
                    compiled: true,
                    tests_passed: r.status.success(),
                    output: format!(
                        "{}{}",
                        String::from_utf8_lossy(&r.stdout),
                        String::from_utf8_lossy(&r.stderr)
                    ),
                    passed_count: 0,
                    total_count: test_cases.len(),
                },
                Err(e) => TestResult {
                    compiled: true,
                    tests_passed: false,
                    output: format!("C++ exec err: {}", e),
                    passed_count: 0,
                    total_count: test_cases.len(),
                },
            }
        }
        Language::Kotlin => {
            let src_path = tmp.join("Solution.kt");
            let jar_path = tmp.join("solution.jar");
            let mut source = code.to_string();
            source.push_str("\n\n");
            source.push_str(&tests);
            fs::write(&src_path, &source).unwrap();

            // Use absolute path since kotlinc is in %LOCALAPPDATA% which isn't on system PATH
            let kotlinc_path = format!(
                "{}\\kotlinc\\kotlinc\\bin\\kotlinc.bat",
                std::env::var("LOCALAPPDATA").unwrap_or_else(|_| dirs::cache_dir()
                    .map(|p: std::path::PathBuf| p.to_string_lossy().to_string())
                    .unwrap_or_default())
            );

            // Step 1: Compile to a self-contained JAR.
            // -include-runtime bundles the Kotlin stdlib so `java -jar` works without extra classpath.
            // `-script` mode only accepts .kts files; plain .kt files must be compiled first.
            let compile = Command::new(&kotlinc_path)
                .args(["-include-runtime", "-d", "solution.jar", "Solution.kt"])
                .current_dir(tmp)
                .output();

            let compile_result = match compile {
                Err(e) => {
                    return TestResult {
                        compiled: false,
                        tests_passed: false,
                        output: format!("kotlinc not found: {}", e),
                        passed_count: 0,
                        total_count: test_cases.len(),
                    }
                }
                Ok(r) => r,
            };

            if !compile_result.status.success() {
                let err = format!(
                    "COMPILE FAIL:\n{}{}",
                    String::from_utf8_lossy(&compile_result.stdout),
                    String::from_utf8_lossy(&compile_result.stderr)
                );
                return TestResult {
                    compiled: false,
                    tests_passed: false,
                    output: err,
                    passed_count: 0,
                    total_count: test_cases.len(),
                };
            }

            // Step 2: Run the compiled JAR.
            let run = Command::new("java")
                .args(["-jar", jar_path.to_str().unwrap()])
                .current_dir(tmp)
                .output();

            match run {
                Ok(r) => {
                    let combined = format!(
                        "{}{}",
                        String::from_utf8_lossy(&r.stdout),
                        String::from_utf8_lossy(&r.stderr)
                    );
                    TestResult {
                        compiled: true,
                        tests_passed: r.status.success(),
                        output: combined,
                        passed_count: 0,
                        total_count: test_cases.len(),
                    }
                }
                Err(e) => TestResult {
                    compiled: true,
                    tests_passed: false,
                    output: format!("java -jar failed: {}", e),
                    passed_count: 0,
                    total_count: test_cases.len(),
                },
            }
        }
        Language::Sql => {
            let src_path = tmp.join("schema.sql");
            let mut source = code.to_string();
            source.push_str("\n\n");
            source.push_str(&tests);
            fs::write(&src_path, &source).unwrap();
            // Pass full path via -ArgumentList — Start-Job spawns a new PS session that does NOT
            // inherit current_dir, so a bare '.read schema.sql' fails with "cannot open schema.sql".
            let schema_full = src_path.to_string_lossy().replace('\\', "/");
            let ps_cmd = format!(
                "& {{ $p = '{}'; $job = Start-Job -ScriptBlock {{ param($sp) sqlite3 :memory: \".read $sp\" }} -ArgumentList $p; \
                Wait-Job $job -Timeout 8 | Out-Null; \
                if ($job.State -eq 'Running') {{ Stop-Job $job; Write-Error 'SQL TIMEOUT: execution exceeded 8s limit' }} \
                else {{ Receive-Job $job }} }}",
                schema_full
            );
            let out = Command::new("powershell")
                .args(["-NoProfile", "-NonInteractive", "-Command", &ps_cmd])
                .current_dir(tmp)
                .output();
            match out {
                Ok(r) => {
                    let combined = format!(
                        "{}{}",
                        String::from_utf8_lossy(&r.stdout),
                        String::from_utf8_lossy(&r.stderr)
                    );
                    // PowerShell parent always exits 0 — check output for error keywords instead.
                    let tests_passed =
                        !combined.contains("Error:") && !combined.contains("TIMEOUT");
                    TestResult {
                        compiled: true,
                        tests_passed,
                        output: combined,
                        passed_count: 0,
                        total_count: test_cases.len(),
                    }
                }
                Err(e) => TestResult {
                    compiled: false,
                    tests_passed: false,
                    output: format!("SQL execution error: {}", e),
                    passed_count: 0,
                    total_count: test_cases.len(),
                },
            }
        }
        Language::Unknown => TestResult {
            compiled: false,
            tests_passed: false,
            output: "[DYNO] Unknown language".to_string(),
            passed_count: 0,
            total_count: test_cases.len(),
        },
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// SCORECARD WRITER
// ─────────────────────────────────────────────────────────────────────────────

/// Per-task entry aggregated into the final scorecard.
#[derive(Debug)]
struct TaskEntry {
    task_id: String,
    prompt_preview: String,
    pass_at_1: bool,     // solved on first Engineer attempt (0 retries)
    final_success: bool, // solved within retry budget
    retries: u32,
    compile_ok: bool,
    tests_ok: bool,
    observer_verdict: String,
    wall_ms: u128,
    code_len: usize,
    vram_mb: Option<u64>,
    compiler_output: String,
}

/// Write the full Markdown scorecard and return its path.
fn write_scorecard(entries: &[TaskEntry], peak_vram: Option<u64>, total_wall_ms: u128) -> PathBuf {
    let timestamp = chrono::Local::now().format("%Y%m%d_%H%M%S").to_string();
    let dir = PathBuf::from(SCORECARD_DIR);
    let _ = fs::create_dir_all(&dir);
    let path = dir.join(format!("scorecard_{}.md", timestamp));

    let total = entries.len();
    let pass_at_1 = entries.iter().filter(|e| e.pass_at_1).count();
    let final_successes = entries.iter().filter(|e| e.final_success).count();
    let avg_retries = if total > 0 {
        entries.iter().map(|e| e.retries as f64).sum::<f64>() / total as f64
    } else {
        0.0
    };
    let pass_at_1_rate = if total > 0 {
        pass_at_1 as f64 / total as f64 * 100.0
    } else {
        0.0
    };
    let final_success_rate = if total > 0 {
        final_successes as f64 / total as f64 * 100.0
    } else {
        0.0
    };

    let mut md = String::new();

    // ── Header ─────────────────────────────────────────────────────────────────
    md.push_str("# Determinex Dyno — SWE-Bench Scorecard\n\n");
    md.push_str(&format!(
        "> Generated: {}  \n",
        chrono::Local::now().format("%Y-%m-%d %H:%M:%S")
    ));
    md.push_str(&format!(
        "> Models: `{}` → `{}` → `{}`  \n\n",
        sentinel_model(),
        engineer_model(),
        observer_model()
    ));

    // ── Summary Table ──────────────────────────────────────────────────────────
    md.push_str("## Summary\n\n");
    md.push_str("| Metric | Value |\n");
    md.push_str("|---|---|\n");
    md.push_str(&format!("| Total Tasks | {} |\n", total));
    md.push_str(&format!(
        "| Pass@1 (first attempt) | **{}/{} ({:.1}%)** |\n",
        pass_at_1, total, pass_at_1_rate
    ));
    md.push_str(&format!(
        "| Final Success Rate | **{}/{} ({:.1}%)** |\n",
        final_successes, total, final_success_rate
    ));
    md.push_str(&format!(
        "| Average Retries per Task | **{:.2}** |\n",
        avg_retries
    ));
    md.push_str(&format!(
        "| Total Wall Time | **{:.1}s** |\n",
        total_wall_ms as f64 / 1000.0
    ));
    md.push_str(&format!(
        "| Peak VRAM | **{}** |\n",
        peak_vram
            .map(|v| format!("{} MB", v))
            .unwrap_or_else(|| "N/A (nvidia-smi absent)".to_string())
    ));
    md.push_str(&format!("| Max Retries Budget | {} |\n", MAX_RETRIES));
    md.push_str(&format!("| KV-Cache Cap (`num_ctx`) | {} |\n\n", NUM_CTX));

    // ── Grade ──────────────────────────────────────────────────────────────────
    let grade = if final_success_rate >= 80.0 {
        "🏆 A"
    } else if final_success_rate >= 60.0 {
        "🥈 B"
    } else if final_success_rate >= 40.0 {
        "🥉 C"
    } else {
        "❌ F"
    };
    md.push_str(&format!(
        "**Swarm Grade: {}** ({:.1}% final success rate)\n\n",
        grade, final_success_rate
    ));

    // ── Per-Task Results Table ─────────────────────────────────────────────────
    md.push_str("## Per-Task Results\n\n");
    md.push_str(
        "| Task ID | Prompt | Pass@1 | Final | Retries | Compile | Tests | Observer | Wall (s) |\n",
    );
    md.push_str("|---|---|:---:|:---:|:---:|:---:|:---:|---|---:|\n");

    for e in entries {
        let prompt_short = if e.prompt_preview.len() > 60 {
            format!("{}…", &e.prompt_preview[..60])
        } else {
            e.prompt_preview.clone()
        };
        md.push_str(&format!(
            "| `{}` | {} | {} | {} | {} | {} | {} | `{}` | {:.1} |\n",
            e.task_id,
            prompt_short,
            if e.pass_at_1 { "✅" } else { "❌" },
            if e.final_success { "✅" } else { "❌" },
            e.retries,
            if e.compile_ok { "✅" } else { "❌" },
            if e.tests_ok { "✅" } else { "❌" },
            e.observer_verdict,
            e.wall_ms as f64 / 1000.0,
        ));
    }
    md.push('\n');

    // ── Per-Task Detail ────────────────────────────────────────────────────────
    md.push_str("## Per-Task Detail\n\n");
    for e in entries {
        md.push_str(&format!("### `{}`\n\n", e.task_id));
        md.push_str(&format!(
            "**Status:** {}  \n",
            if e.final_success {
                "✅ PASSED"
            } else {
                "❌ FAILED"
            }
        ));
        md.push_str(&format!(
            "**Pass@1:** {}  \n",
            if e.pass_at_1 { "Yes" } else { "No" }
        ));
        md.push_str(&format!("**Retries:** {}  \n", e.retries));
        md.push_str(&format!(
            "**Observer Verdict:** `{}`  \n",
            e.observer_verdict
        ));
        md.push_str(&format!(
            "**Generated Code Length:** {} chars  \n",
            e.code_len
        ));
        if let Some(v) = e.vram_mb {
            md.push_str(&format!("**VRAM at task start:** {} MB  \n", v));
        }
        md.push_str(&format!(
            "**Wall Time:** {:.1}s  \n\n",
            e.wall_ms as f64 / 1000.0
        ));

        if !e.compiler_output.is_empty() {
            let snippet = &e.compiler_output[..e.compiler_output.len().min(600)];
            md.push_str("<details><summary>Compiler / Test Output</summary>\n\n");
            md.push_str("```\n");
            md.push_str(snippet);
            md.push_str("\n```\n\n</details>\n\n");
        }
        md.push_str("---\n\n");
    }

    let _ = fs::write(&path, &md);
    path
}

// ─────────────────────────────────────────────────────────────────────────────
// BATCH-BY-ROUND STATE
// ─────────────────────────────────────────────────────────────────────────────

/// Per-task mutable state for the batch-by-round Dyno loop.
///
/// All 14 tasks are initialised upfront. The loop then processes them in waves:
///   Round N → Engineer batch → parallel compile → Observer batch → partition.
/// Tasks that pass are drained to `entries`; tasks that fail advance with a
/// retry hint. This reduces model swaps from N_tasks×3 to 3 per round.
struct DynoTask<'a> {
    task: &'a BenchmarkTask,
    tmp: TempDir,
    plan: Option<SentinelPlan>,
    /// Code produced by the Engineer in the current round.
    /// None if Engineer failed to emit valid JSON this round.
    current_code: Option<EngineerCode>,
    retry_count: u32,
    /// How many rounds in a row this task has failed (compile/test/observer).
    /// Triggers Leviathan escalation when it reaches LEVIATHAN_ESCALATION_ROUND.
    consecutive_fails: u32,
    pass_at_1: bool,
    final_success: bool,
    retry_hint: String,
    /// Accumulated final snapshot for scorecard (updated each round).
    final_code: String,
    final_verdict: ObserverVerdict,
    last_test: Option<TestResult>,
    vram_mb: Option<u64>,
    wall_start: std::time::Instant,
}

/// Seconds to pause between batch phases so Ollama fully evicts the previous
/// model from VRAM before the next one starts loading.
/// keep_alive: 0 triggers eviction immediately on response, so 4s is safe on a 6 GB GPU for v3.
/// Reduce back to 2s after Engineer v4 (Phi-3, 2.3 GB) is promoted — eviction will be sub-second.
const DYNO_PHASE_FLUSH_SECS: u64 = 4;

// ─────────────────────────────────────────────────────────────────────────────
// THE DYNO TEST
// ─────────────────────────────────────────────────────────────────────────────

/// SWE-Bench Dyno: headless batch benchmark runner.
///
/// For each task in the dataset:
///   1. Spawn an isolated `TempDir` workspace.
///   2. Run Sentinel → Engineer (with retry) → Observer pipeline.
///   3. Compile generated code + test harness via `rustc --test`.
///   4. Execute test binary, capture PASS/FAIL per test case.
///   5. Aggregate results and write Markdown scorecard.
///
/// Ollama unreachable → self-skip (no panic).
/// Missing dataset    → auto-create 5-task demo and proceed.
#[tokio::test(flavor = "multi_thread", worker_threads = 2)]
async fn swe_bench_dyno() {
    let client = build_client();
    let wall = Instant::now();
    let dataset_path = Path::new(BENCHMARK_DATASET_PATH);

    // ── Pre-flight: Ollama ─────────────────────────────────────────────────────
    // Was `ollama_is_reachable`, whose banner then said "ensure the determinex models are pulled"
    // -- advice it did not itself act on. See tests/common/mod.rs.
    let wanted = [sentinel_model(), engineer_model(), observer_model()];
    if common::should_skip(
        "[DYNO] swe_bench_dyno",
        match common::unmet_prerequisites(&client, &ollama_tags_url(), &wanted).await {
            Some(unmet) => Some(unmet),
            None => {
                common::residency_shortfall(
                    &client,
                    &ollama_generate_url(),
                    &ollama_ps_url(),
                    &wanted,
                )
                .await
            }
        },
    ) {
        return;
    }

    // ── Dataset: load or create demo ───────────────────────────────────────────
    if !dataset_path.exists() {
        println!(
            "[DYNO] Dataset not found at '{}' — creating 5-task demo.",
            BENCHMARK_DATASET_PATH
        );
        if let Err(e) = create_demo_dataset(dataset_path) {
            panic!("[DYNO] Could not create demo dataset: {}", e);
        }
        println!("[DYNO] Demo dataset written.");
    }

    // A malformed dataset is treated exactly like a missing one: report loudly, regenerate the
    // demo, continue.
    //
    // This dataset lives under .determinex_staging/, which is GITIGNORED -- a local convenience
    // input, not an assertion target, and a clean clone has no such file (which is why the
    // create-demo path above exists at all). One stale local copy had a Windows path written into
    // a prompt with unescaped backslashes, whose \U is not a valid JSON escape, so line 12 failed
    // to parse and this panicked. Because `cargo test` stops at the first failing target, that one
    // corrupt local line hid the state of every target after it.
    let tasks = match load_benchmark_dataset(BENCHMARK_DATASET_PATH) {
        Ok(t) => t,
        Err(e) => {
            println!("[DYNO] Dataset at '{}' failed to load: {}", BENCHMARK_DATASET_PATH, e);
            println!("[DYNO] It is a gitignored local artifact -- regenerating the 5-task demo.");
            if let Err(e) = create_demo_dataset(dataset_path) {
                panic!("[DYNO] Could not regenerate demo dataset: {}", e);
            }
            match load_benchmark_dataset(BENCHMARK_DATASET_PATH) {
                Ok(t) => t,
                Err(e) => panic!("[DYNO] Regenerated demo dataset also failed to load: {}", e),
            }
        }
    };

    if tasks.is_empty() {
        panic!("[DYNO] Dataset is empty — nothing to benchmark.");
    }

    println!();
    println!("══════════════════════════════════════════════════════════════════════");
    println!("  DETERMINEX DYNO — SWE-BENCH BATCH RUNNER");
    println!("══════════════════════════════════════════════════════════════════════");
    println!("  Dataset : {}", BENCHMARK_DATASET_PATH);
    println!("  Tasks   : {}", tasks.len());
    println!(
        "  Models  : {} → {} → {}",
        sentinel_model(),
        engineer_model(),
        observer_model()
    );
    println!("  Max retries per task : {}", MAX_RETRIES);

    // ── Auto-distillation setup ────────────────────────────────────────────────
    //
    // Model names are resolved at runtime from env vars so you can update them
    // without recompiling. Set DETERMINEX_CLAUDE_MODEL or DETERMINEX_GEMINI_MODEL in
    // your .env to override (useful when new model versions drop).
    dotenvy::dotenv().ok();

    let api_key = std::env::var("ANTHROPIC_API_KEY").unwrap_or_default();
    let gemini_key = std::env::var("GEMINI_API_KEY").unwrap_or_default();
    let claude_model =
        std::env::var("DETERMINEX_CLAUDE_MODEL").unwrap_or_else(|_| CLAUDE_MODEL_DEFAULT.to_string());
    let gemini_model =
        std::env::var("DETERMINEX_GEMINI_MODEL").unwrap_or_else(|_| GEMINI_MODEL_DEFAULT.to_string());

    if api_key.is_empty() {
        println!("[AUTODISTIL] ⚠  ANTHROPIC_API_KEY not set — Claude distillation writes synthetic entries only.");
    } else {
        println!(
            "[AUTODISTIL] Claude ({}) ready — fires inline after each failure.",
            claude_model
        );
    }
    if gemini_key.is_empty() {
        println!("[AUTODISTIL] ⚠  GEMINI_API_KEY not set — Gemini distillation skipped.");
    } else {
        println!(
            "[AUTODISTIL] Gemini ({}) ready — fires in parallel with Claude.",
            gemini_model
        );
    }
    println!(
        "[AUTODISTIL] Override models anytime: DETERMINEX_CLAUDE_MODEL / DETERMINEX_GEMINI_MODEL in .env"
    );
    println!();

    // ── VRAM tracking ──────────────────────────────────────────────────────────
    let mut peak_vram: Option<u64> = None;
    let mut entries: Vec<TaskEntry> = Vec::with_capacity(tasks.len());

    // ── Phase 0: Build task states + batch Sentinel (1 model load total) ───────
    //
    // All 14 tasks run through Sentinel in sequence before ANY Engineer inference.
    // This reduces model swaps from N_tasks×3 to 3 per round:
    //
    //   Before:  [S→E→O] [S→E→O] ... × 14  =  42 model swaps
    //   After:   [S×14]  [E×14]  [O×14]     =   3 model swaps per round
    //
    // At 8s per swap on a 6 GB GPU: 42×8=336s → 3×8=24s saved on first round alone.

    println!("══════════════════════════════════════════════════════════════════════");
    println!(
        "  PHASE 0 — BATCH SENTINEL ({} tasks, 1 model load)",
        tasks.len()
    );
    println!("══════════════════════════════════════════════════════════════════════");
    println!();

    let mut task_states: Vec<DynoTask> = Vec::with_capacity(tasks.len());
    let total_tasks = tasks.len();

    for (task_idx, task) in tasks.iter().enumerate() {
        let vram_mb = sample_vram_mb();
        if let Some(mb) = vram_mb {
            peak_vram = Some(peak_vram.unwrap_or(0).max(mb));
        }

        let tmp = match TempDir::new() {
            Ok(d) => d,
            Err(e) => {
                eprintln!("[DYNO] TempDir failed for '{}': {}", task.task_id, e);
                entries.push(TaskEntry {
                    task_id: task.task_id.clone(),
                    prompt_preview: task.prompt[..task.prompt.len().min(80)].to_string(),
                    pass_at_1: false,
                    final_success: false,
                    retries: 0,
                    compile_ok: false,
                    tests_ok: false,
                    observer_verdict: "ERROR".to_string(),
                    wall_ms: 0,
                    code_len: 0,
                    vram_mb,
                    compiler_output: format!("TempDir failed: {}", e),
                });
                continue;
            }
        };

        print!(
            "  [SENTINEL {}/{}] {:25} ... ",
            task_idx + 1,
            total_tasks,
            task.task_id
        );
        let plan = match run_sentinel(&client, task).await {
            Ok(p) => {
                println!("✓ ({} steps)", p.steps.len());
                Some(p)
            }
            Err(e) => {
                println!("✗ {}", e);
                let _ = TelemetryEvent {
                    timestamp: chrono::Utc::now().to_rfc3339(),
                    language: format!("{:?}", task.language),
                    task_id: task.task_id.clone(),
                    original_broken_code: String::new(),
                    raw_compiler_panic: format!("Sentinel parse failed: {}", e),
                    observer_review_notes: String::new(),
                    final_status: "SENTINEL_FAIL".to_string(),
                }
                .commit_to_vault("determinex_v1_failures.jsonl");
                None
            }
        };

        task_states.push(DynoTask {
            task,
            tmp,
            plan,
            current_code: None,
            retry_count: 0,
            consecutive_fails: 0,
            pass_at_1: false,
            final_success: false,
            retry_hint: String::new(),
            final_code: String::new(),
            final_verdict: ObserverVerdict {
                verdict: "PENDING".to_string(),
                issues: vec![],
                confidence: 0.0,
                review_notes: None,
            },
            last_test: None,
            vram_mb,
            wall_start: Instant::now(),
        });
    }

    // Drain Sentinel failures into entries; keep the rest as active
    let mut pending: Vec<DynoTask> = Vec::new();
    for ts in task_states {
        if ts.plan.is_none() {
            entries.push(TaskEntry {
                task_id: ts.task.task_id.clone(),
                prompt_preview: ts.task.prompt[..ts.task.prompt.len().min(80)].to_string(),
                pass_at_1: false,
                final_success: false,
                retries: 0,
                compile_ok: false,
                tests_ok: false,
                observer_verdict: "SENTINEL_FAIL".to_string(),
                wall_ms: ts.wall_start.elapsed().as_millis(),
                code_len: 0,
                vram_mb: ts.vram_mb,
                compiler_output: "Sentinel failed — see determinex_v1_failures.jsonl".to_string(),
            });
        } else {
            pending.push(ts);
        }
    }

    println!();
    println!(
        "[DYNO] Sentinel phase complete — {} tasks advancing.",
        pending.len()
    );
    println!(
        "[DYNO] VRAM flush pause ({}s — evicting Sentinel)...",
        DYNO_PHASE_FLUSH_SECS
    );
    tokio::time::sleep(Duration::from_secs(DYNO_PHASE_FLUSH_SECS)).await;

    // ── Retry rounds: Engineer → parallel compile → Observer ───────────────────
    //
    // Each round processes ALL pending tasks through each phase before moving on:
    //
    //   Round N:
    //     Engineer phase : tasks[0..N] sequentially  (1 model load, 1 model evict)
    //     Compile phase  : tasks[0..N] in PARALLEL   (pure CPU — GPU is idle)
    //     Observer phase : tasks[0..N] sequentially  (1 model load, 1 model evict)
    //     Partition      : passed → entries, failed → next round with hint
    //
    // Parallel compilation is the free win: all 14 rustc/tsc/python/go builds run
    // simultaneously during the Engineer eviction window.

    for round in 0..=MAX_RETRIES {
        if pending.is_empty() {
            break;
        }

        println!();
        println!("══════════════════════════════════════════════════════════════════════");
        println!(
            "  ROUND {}/{} — {} tasks active",
            round + 1,
            MAX_RETRIES + 1,
            pending.len()
        );
        println!("══════════════════════════════════════════════════════════════════════");
        println!();

        // ── Engineer batch (sequential GPU, 1 model load) ─────────────────────
        // After LEVIATHAN_ESCALATION_ROUND consecutive failures, the task escalates
        // to Leviathan (CPU-resident 14B) which gets the full failure context.
        // Leviathan uses keep_alive=1800 so it stays in system RAM between calls;
        // the GPU is completely idle during Leviathan inference (no VRAM conflict).
        let batch_size = pending.len();
        println!(
            "  [ENGINEER BATCH] {}/{} tasks remaining",
            batch_size, total_tasks
        );
        for (i, ts) in pending.iter_mut().enumerate() {
            let escalating = ts.consecutive_fails >= LEVIATHAN_ESCALATION_ROUND;
            if escalating {
                print!(
                    "    [{}/{}] {:25} LEVIATHAN (round {}, {} consec fails) ... ",
                    i + 1,
                    batch_size,
                    ts.task.task_id,
                    round + 1,
                    ts.consecutive_fails
                );
                let failed_code = ts
                    .current_code
                    .as_ref()
                    .map(|c| c.code.as_str())
                    .unwrap_or("");
                let compiler_out = ts
                    .last_test
                    .as_ref()
                    .map(|t| t.output.as_str())
                    .unwrap_or("");
                match run_leviathan(
                    &client,
                    ts.task,
                    ts.plan.as_ref().unwrap(),
                    failed_code,
                    compiler_out,
                    &ts.retry_hint,
                )
                .await
                {
                    Ok(code) if code.code.trim().len() < 10 => {
                        println!("✗ Leviathan empty code ({} chars)", code.code.len());
                    }
                    Ok(code) => {
                        println!("✓ Leviathan ({} chars)", code.code.len());
                        ts.current_code = Some(code);
                    }
                    Err(e) => {
                        println!("✗ Leviathan error: {} — falling back to Engineer", e);
                        // Leviathan failed (model not pulled?) — fall through to Engineer below
                        match run_engineer(
                            &client,
                            ts.task,
                            ts.plan.as_ref().unwrap(),
                            &ts.retry_hint,
                        )
                        .await
                        {
                            Ok(code) => {
                                ts.current_code = Some(code);
                            }
                            Err(e2) => {
                                println!("  ✗ Engineer fallback also failed: {}", e2);
                            }
                        }
                    }
                }
            } else {
                print!(
                    "    [{}/{}] {:25} attempt {} ... ",
                    i + 1,
                    batch_size,
                    ts.task.task_id,
                    round + 1
                );
                match run_engineer(&client, ts.task, ts.plan.as_ref().unwrap(), &ts.retry_hint)
                    .await
                {
                    Ok(code) if code.code.trim().len() < 10 => {
                        // Guard: empty or trivially short code — skip compile, retry immediately
                        println!("✗ empty code ({} chars) — forcing retry", code.code.len());
                        ts.retry_hint = format!(
                            "CRITICAL: Your last response had an empty or near-empty 'code' field ({} chars). \
                            You MUST return complete, compilable {} code in the 'code' JSON field. \
                            Do not explain. Do not use markdown. Return the full implementation.",
                            code.code.len(),
                            format!("{:?}", ts.task.language).to_lowercase()
                        );
                    }
                    Ok(code) => {
                        println!("✓ ({} chars)", code.code.len());
                        ts.current_code = Some(code);
                    }
                    Err(e) => {
                        println!("✗ {}", e);
                        let _ = TelemetryEvent {
                            timestamp: chrono::Utc::now().to_rfc3339(),
                            language: format!("{:?}", ts.task.language),
                            task_id: ts.task.task_id.clone(),
                            original_broken_code: String::new(),
                            raw_compiler_panic: format!("Engineer parse failed: {}", e),
                            observer_review_notes: String::new(),
                            final_status: "ENGINEER_PARSE_FAIL".to_string(),
                        }
                        .commit_to_vault("determinex_v1_failures.jsonl");
                        ts.retry_hint =
                            format!("PREVIOUS ATTEMPT FAILED (your JSON was malformed): {}", e);
                    }
                }
            }
        }

        println!(
            "  [DYNO] VRAM flush pause ({}s — evicting Engineer)...",
            DYNO_PHASE_FLUSH_SECS
        );
        tokio::time::sleep(Duration::from_secs(DYNO_PHASE_FLUSH_SECS)).await;

        // ── Compile batch (parallel CPU — GPU completely idle) ────────────────
        println!("  [COMPILER BATCH] {} tasks in parallel...", pending.len());

        let compile_handles: Vec<_> = pending
            .iter()
            .map(|ts| {
                let code_str = ts
                    .current_code
                    .as_ref()
                    .map(|c| c.code.clone())
                    .unwrap_or_default();
                let test_cases = ts.task.test_cases.clone();
                let lang = ts.task.language.clone();
                let tmp_path = ts.tmp.path().to_path_buf();
                tokio::task::spawn_blocking(move || {
                    execute_task_tests(&lang, &tmp_path, &code_str, &test_cases)
                })
            })
            .collect();

        let mut test_results: Vec<TestResult> = Vec::with_capacity(compile_handles.len());
        for handle in compile_handles {
            test_results.push(handle.await.unwrap_or_else(|_| TestResult {
                compiled: false,
                tests_passed: false,
                output: "spawn_blocking panicked".to_string(),
                passed_count: 0,
                total_count: 0,
            }));
        }

        for (i, (ts, tr)) in pending.iter().zip(test_results.iter()).enumerate() {
            if tr.compiled {
                println!(
                    "    [{}/{}] {:25} ✓  tests {}/{}",
                    i + 1,
                    batch_size,
                    ts.task.task_id,
                    tr.passed_count,
                    tr.total_count
                );
            } else {
                println!(
                    "    [{}/{}] {:25} ✗  compile failed",
                    i + 1,
                    batch_size,
                    ts.task.task_id
                );
            }
        }
        println!();

        // ── Observer batch (sequential GPU, 1 model load) ─────────────────────
        println!(
            "  [OBSERVER BATCH] {}/{} tasks remaining",
            batch_size, total_tasks
        );

        let mut verdicts: Vec<ObserverVerdict> = Vec::with_capacity(pending.len());
        for (i, (ts, tr)) in pending.iter().zip(test_results.iter()).enumerate() {
            let plan = ts.plan.as_ref().unwrap();
            let code_struct = ts.current_code.clone().unwrap_or_else(|| EngineerCode {
                language: format!("{:?}", ts.task.language).to_lowercase(),
                code: String::new(),
                files_affected: vec![],
            });
            print!("    [{}/{}] {:25} ... ", i + 1, batch_size, ts.task.task_id);
            let verdict = match run_observer(&client, plan, &code_struct, Some(tr)).await {
                Ok(v) => {
                    println!("→ {} ({:.0}%)", v.verdict, v.confidence * 100.0);
                    v
                }
                Err(e) => {
                    println!("✗ Observer parse failed: {}", e);
                    ObserverVerdict {
                        verdict: "HALLUCINATION".to_string(),
                        issues: vec![format!("Observer parse failed: {}", e)],
                        confidence: 0.0,
                        review_notes: None,
                    }
                }
            };
            verdicts.push(verdict);
        }

        println!(
            "  [DYNO] VRAM flush pause ({}s — evicting Observer)...",
            DYNO_PHASE_FLUSH_SECS
        );
        tokio::time::sleep(Duration::from_secs(DYNO_PHASE_FLUSH_SECS)).await;

        // ── Partition: accepted → entries, retry → next round ─────────────────
        let mut next_pending: Vec<DynoTask> = Vec::new();
        // Collect per-task outcomes for the round summary printed after the loop
        let mut round_passed: Vec<String> = Vec::new();
        let mut round_retry: Vec<String> = Vec::new();
        let mut round_failed: Vec<String> = Vec::new();

        for (mut ts, (test_result, verdict)) in pending
            .into_iter()
            .zip(test_results.into_iter().zip(verdicts.into_iter()))
        {
            let compiler_won = test_result.tests_passed;
            let observer_accepted = (verdict.verdict == "CLEAN"
                && verdict.confidence >= CONFIDENCE_THRESHOLD)
                || compiler_won;

            // Capture Observer mistakes for training
            if compiler_won && verdict.verdict != "CLEAN" {
                println!(
                    "[DYNO] Compiler-wins override: {} — tests passed, Observer overruled.",
                    ts.task.task_id
                );
                let obs_mistake = ObserverMistakeEvent {
                    timestamp: chrono::Utc::now().to_rfc3339(),
                    language: format!("{:?}", ts.task.language),
                    task_id: ts.task.task_id.clone(),
                    passing_code: ts
                        .current_code
                        .as_ref()
                        .map(|c| c.code.clone())
                        .unwrap_or_default(),
                    compiler_test_output: test_result.output.clone(),
                    wrong_observer_verdict: verdict.verdict.clone(),
                    wrong_observer_confidence: verdict.confidence,
                    wrong_observer_notes: verdict.review_notes.clone(),
                };
                if let Ok(()) = obs_mistake.commit_to_vault("determinex_v1_observer_mistakes.jsonl") {
                    println!("[TELEMETRY] Observer mistake captured.");
                    let key = api_key.clone();
                    let model = claude_model.clone();
                    let ev = ObserverMistakeEvent {
                        timestamp: chrono::Utc::now().to_rfc3339(),
                        language: format!("{:?}", ts.task.language),
                        task_id: ts.task.task_id.clone(),
                        passing_code: ts
                            .current_code
                            .as_ref()
                            .map(|c| c.code.clone())
                            .unwrap_or_default(),
                        compiler_test_output: test_result.output.clone(),
                        wrong_observer_verdict: verdict.verdict.clone(),
                        wrong_observer_confidence: verdict.confidence,
                        wrong_observer_notes: verdict.review_notes.clone(),
                    };
                    tokio::spawn(async move {
                        distill_observer_mistake(ev, key, model).await;
                    });
                    // Gemini expert fires in parallel — second perspective on the same Observer mistake
                    if !gemini_key.is_empty() {
                        let ev_gem = ObserverMistakeEvent {
                            timestamp: chrono::Utc::now().to_rfc3339(),
                            language: format!("{:?}", ts.task.language),
                            task_id: ts.task.task_id.clone(),
                            passing_code: ts
                                .current_code
                                .as_ref()
                                .map(|c| c.code.clone())
                                .unwrap_or_default(),
                            compiler_test_output: test_result.output.clone(),
                            wrong_observer_verdict: verdict.verdict.clone(),
                            wrong_observer_confidence: verdict.confidence,
                            wrong_observer_notes: verdict.review_notes.clone(),
                        };
                        let gkey = gemini_key.clone();
                        let gmod = gemini_model.clone();
                        tokio::spawn(async move {
                            distill_observer_mistake_gemini(ev_gem, gkey, gmod).await;
                        });
                    }
                }
            }

            // Update task snapshot
            ts.final_code = ts
                .current_code
                .as_ref()
                .map(|c| c.code.clone())
                .unwrap_or_default();
            ts.final_verdict = verdict.clone();
            ts.last_test = Some(test_result.clone());

            if observer_accepted && test_result.tests_passed {
                if round == 0 {
                    ts.pass_at_1 = true;
                }
                ts.final_success = true;
                ts.consecutive_fails = 0; // reset escalation counter on success
                let p1_tag = if ts.pass_at_1 { " pass@1" } else { "" };
                round_passed.push(format!(
                    "  ✅ {:25} {:>5.0}%  {}{}",
                    ts.task.task_id,
                    verdict.confidence * 100.0,
                    verdict.verdict,
                    p1_tag
                ));
                entries.push(TaskEntry {
                    task_id: ts.task.task_id.clone(),
                    prompt_preview: ts.task.prompt[..ts.task.prompt.len().min(80)].to_string(),
                    pass_at_1: ts.pass_at_1,
                    final_success: true,
                    retries: ts.retry_count,
                    compile_ok: test_result.compiled,
                    tests_ok: test_result.tests_passed,
                    observer_verdict: verdict.verdict.clone(),
                    wall_ms: ts.wall_start.elapsed().as_millis(),
                    code_len: ts.final_code.len(),
                    vram_mb: ts.vram_mb,
                    compiler_output: test_result.output,
                });
            } else {
                // Distill the failure in background
                let code_str = ts.final_code.clone();
                let compiler_output = test_result.output.clone();
                if !code_str.is_empty() {
                    let telemetry = TelemetryEvent {
                        timestamp: chrono::Utc::now().to_rfc3339(),
                        language: format!("{:?}", ts.task.language),
                        task_id: ts.task.task_id.clone(),
                        original_broken_code: code_str.clone(),
                        raw_compiler_panic: compiler_output.clone(),
                        observer_review_notes: verdict.review_notes.clone().unwrap_or_default(),
                        final_status: verdict.verdict.clone(),
                    };
                    if let Ok(()) = telemetry.commit_to_vault("determinex_v1_failures.jsonl") {
                        // Fire Claude + Gemini distillation in parallel — both spawn immediately
                        // and the next compile round starts without waiting for either.
                        let claude_key = api_key.clone();
                        let claude_m = claude_model.clone();
                        let gemini_key_d = gemini_key.clone();
                        let gemini_m = gemini_model.clone();
                        let ev_claude = TelemetryEvent {
                            timestamp: chrono::Utc::now().to_rfc3339(),
                            language: format!("{:?}", ts.task.language),
                            task_id: ts.task.task_id.clone(),
                            original_broken_code: code_str.clone(),
                            raw_compiler_panic: compiler_output.clone(),
                            observer_review_notes: verdict.review_notes.clone().unwrap_or_default(),
                            final_status: verdict.verdict.clone(),
                        };
                        let ev_gemini = TelemetryEvent {
                            timestamp: chrono::Utc::now().to_rfc3339(),
                            language: format!("{:?}", ts.task.language),
                            task_id: ts.task.task_id.clone(),
                            original_broken_code: code_str,
                            raw_compiler_panic: compiler_output.clone(),
                            observer_review_notes: verdict.review_notes.clone().unwrap_or_default(),
                            final_status: verdict.verdict.clone(),
                        };
                        tokio::spawn(async move {
                            distill_engineer_failure(ev_claude, claude_key, claude_m).await;
                        });
                        tokio::spawn(async move {
                            distill_engineer_failure_gemini(ev_gemini, gemini_key_d, gemini_m)
                                .await;
                        });
                    }
                }

                if ts.retry_count >= MAX_RETRIES {
                    let reason = if !test_result.compiled {
                        "compile fail"
                    } else if !test_result.tests_passed {
                        "tests fail"
                    } else {
                        "observer reject"
                    };
                    round_failed.push(format!(
                        "  ❌ {:25} gave up after {} retries  ({})",
                        ts.task.task_id, ts.retry_count, reason
                    ));
                    entries.push(TaskEntry {
                        task_id: ts.task.task_id.clone(),
                        prompt_preview: ts.task.prompt[..ts.task.prompt.len().min(80)].to_string(),
                        pass_at_1: false,
                        final_success: false,
                        retries: ts.retry_count,
                        compile_ok: test_result.compiled,
                        tests_ok: test_result.tests_passed,
                        observer_verdict: verdict.verdict.clone(),
                        wall_ms: ts.wall_start.elapsed().as_millis(),
                        code_len: ts.final_code.len(),
                        vram_mb: ts.vram_mb,
                        compiler_output: test_result.output,
                    });
                } else {
                    // Build tail-biased retry hint (fatal error is at the end)
                    let truncate_tail = |s: &str, limit: usize| -> String {
                        if s.len() > limit {
                            format!(
                                "[...{} chars omitted...]\n{}",
                                s.len() - limit,
                                &s[s.len() - limit..]
                            )
                        } else {
                            s.to_string()
                        }
                    };
                    let reason = if !test_result.compiled {
                        "compile fail"
                    } else if !test_result.tests_passed {
                        "tests fail"
                    } else {
                        "observer reject"
                    };
                    round_retry.push(format!(
                        "  🔄 {:25} retry {}/{}  ({})",
                        ts.task.task_id,
                        ts.retry_count + 1,
                        MAX_RETRIES,
                        reason
                    ));
                    let compiler_hint = if !test_result.compiled {
                        format!(
                            "Code did not compile: {}",
                            truncate_tail(&compiler_output, 1000)
                        )
                    } else if !test_result.tests_passed {
                        format!("Tests failed: {}", truncate_tail(&compiler_output, 1000))
                    } else {
                        format!("Observer rejected: {}", verdict.issues.join("; "))
                    };
                    let observer_notes = match verdict.review_notes.clone() {
                        Some(n) if !n.is_empty() => format!("\nSenior Observer Notes: {}", n),
                        _ => String::new(),
                    };
                    ts.retry_hint = format!(
                        "PREVIOUS ATTEMPT REJECTED. {}.{}\nFix all issues. Return complete compilable code.",
                        compiler_hint, observer_notes
                    );
                    ts.retry_count += 1;
                    ts.consecutive_fails += 1;
                    next_pending.push(ts);
                }
            }
        }

        // ── Round summary ──────────────────────────────────────────────────────
        println!();
        println!("  ┌─────────────────────────────────────────────────────────────────┐");
        println!(
            "  │  ROUND {}/{} RESULTS  —  passed: {}  retry: {}  failed: {}{}",
            round + 1,
            MAX_RETRIES + 1,
            round_passed.len(),
            round_retry.len(),
            round_failed.len(),
            " ".repeat(
                23usize.saturating_sub(
                    format!(
                        "passed: {}  retry: {}  failed: {}",
                        round_passed.len(),
                        round_retry.len(),
                        round_failed.len()
                    )
                    .len()
                )
            )
        );
        println!("  ├─────────────────────────────────────────────────────────────────┤");
        for line in &round_passed {
            println!("{}", line);
        }
        for line in &round_retry {
            println!("{}", line);
        }
        for line in &round_failed {
            println!("{}", line);
        }
        let total_done = entries.len();
        println!("  ├─────────────────────────────────────────────────────────────────┤");
        println!(
            "  │  Overall: {}/{} resolved  ({} still pending next round)",
            total_done,
            total_tasks,
            next_pending.len()
        );
        println!("  └─────────────────────────────────────────────────────────────────┘");
        println!();

        pending = next_pending;
    }

    // Safety drain: tasks that somehow outlived the retry budget
    for ts in pending {
        let test_r = ts.last_test.unwrap_or(TestResult {
            compiled: false,
            tests_passed: false,
            output: "No result recorded".to_string(),
            passed_count: 0,
            total_count: ts.task.test_cases.len(),
        });
        entries.push(TaskEntry {
            task_id: ts.task.task_id.clone(),
            prompt_preview: ts.task.prompt[..ts.task.prompt.len().min(80)].to_string(),
            pass_at_1: false,
            final_success: false,
            retries: ts.retry_count,
            compile_ok: test_r.compiled,
            tests_ok: test_r.tests_passed,
            observer_verdict: ts.final_verdict.verdict.clone(),
            wall_ms: ts.wall_start.elapsed().as_millis(),
            code_len: ts.final_code.len(),
            vram_mb: ts.vram_mb,
            compiler_output: test_r.output,
        });
    }

    let total_wall = wall.elapsed().as_millis();

    // ── Scorecard ──────────────────────────────────────────────────────────────
    let scorecard_path = write_scorecard(&entries, peak_vram, total_wall);

    // ── Console summary ────────────────────────────────────────────────────────
    let total = entries.len();
    let pass_at_1_count = entries.iter().filter(|e| e.pass_at_1).count();
    let final_ok = entries.iter().filter(|e| e.final_success).count();
    let avg_retries = if total > 0 {
        entries.iter().map(|e| e.retries as f64).sum::<f64>() / total as f64
    } else {
        0.0
    };

    println!();
    println!("╔══════════════════════════════════════════════════════════════════╗");
    println!("║              DETERMINEX DYNO — FINAL SCORECARD                      ║");
    println!("╠══════════════════════════════════════════════════════════════════╣");
    println!(
        "║  Tasks evaluated     : {:>10}                              ║",
        total
    );
    println!(
        "║  Pass@1 (first try)  : {:>10} ({:.1}%)                    ║",
        pass_at_1_count,
        if total > 0 {
            pass_at_1_count as f64 / total as f64 * 100.0
        } else {
            0.0
        }
    );
    println!(
        "║  Final Success Rate  : {:>10} ({:.1}%)                    ║",
        final_ok,
        if total > 0 {
            final_ok as f64 / total as f64 * 100.0
        } else {
            0.0
        }
    );
    println!(
        "║  Avg retries / task  : {:>10.2}                              ║",
        avg_retries
    );
    println!(
        "║  Total wall time     : {:>10} ms                          ║",
        total_wall
    );
    println!(
        "║  Peak VRAM observed  : {:>10}                              ║",
        peak_vram
            .map(|v| format!("{} MB", v))
            .unwrap_or_else(|| "N/A".to_string())
    );
    println!("╠══════════════════════════════════════════════════════════════════╣");
    println!("║  Scorecard written to:                                           ║");
    println!("║  {:<64} ║", scorecard_path.display());
    println!("╚══════════════════════════════════════════════════════════════════╝");
    println!();

    // ── Snyk notice: no secrets written; temp dirs cleaned by Drop ─────────────
    // TempDir instances are dropped here (end of function scope) and their contents
    // are erased by the OS. No generated code persists beyond the test run.

    // ── Soft assertion: at least one task must have been evaluated ─────────────
    // We do NOT assert final_success > 0 because the Dataset may be adversarial
    // and a 0% pass rate is itself a valid (alarming) benchmark finding.
    assert!(
        total > 0,
        "[DYNO] No tasks were evaluated — something went wrong during dataset loading."
    );

    println!("[DYNO] Benchmark complete. {} task(s) evaluated.", total);
}
