//! observer_sabotage.rs — Phase 6 Observer Determinism Stress Test
//!
//! Fires a deliberately broken Rust payload directly at the Observer (phi3:mini via
//! determinex-observer:v2) using the exact hardened system prompt and OllamaRequest struct
//! from orchestrator.rs. Bypasses Sentinel and Engineer entirely.
//!
//! PASS criteria: phi3:mini returns 100% raw JSON with zero markdown, zero padding,
//! and the output round-trips through serde_json::from_str without error.
//! We do NOT care about the verdict value — only that the tollbooth holds.

use reqwest::Client;
use serde::{Deserialize, Serialize};
use std::time::Duration;

// ─── Mirror of the private orchestrator transport types ────────────────────────
// Replicated here so the test is self-contained and exercises the exact same
// wire format without requiring pub access to orchestrator internals.

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

#[derive(Deserialize)]
struct OllamaResponse {
    response: String,
    done: bool,
}

// ─── Mirror of ObserverVerdict ─────────────────────────────────────────────────

#[derive(Debug, Deserialize)]
struct ObserverVerdict {
    verdict: String,
    issues: Vec<String>,
    confidence: f32,
}

// ─── Sabotage payload ──────────────────────────────────────────────────────────
// Deliberately broken Rust: type mismatch, null-pointer UB, out-of-bounds panic,
// wrong return type. This is maximally broken code — the Observer must flag it.

const SABOTAGE_CODE: &str = r#"
fn calculate_total() {
    let mut x = "5" + 5;                        // type error: cannot add &str to integer
    unsafe { *std::ptr::null_mut::<i32>() = 42; } // null pointer dereference — UB
    let v: Vec<i32> = Vec::new();
    let _oob = v[999];                           // panic: index out of bounds on empty vec
    return x                                     // missing semicolon + wrong return type
}
"#;

// ─── Test ──────────────────────────────────────────────────────────────────────

#[tokio::test]
async fn observer_sabotage_json_clamp() {
    const OLLAMA_URL: &str = "http://localhost:11434/api/generate";
    const MODEL: &str = "determinex-observer:v3";

    let audit_targets =
        "type safety, memory safety, index bounds, undefined behavior, return type correctness";
    let lang = "rust";
    let steps = "- Implement calculate_total that adds a string and an integer\n- Use unsafe pointer arithmetic\n- Access a Vec element out of bounds";

    // ── Exact hardened prompt from run_observer — must stay in sync ────────────
    let prompt = format!(
        r#"SYSTEM: You are a JSON serialization machine. You produce exactly one raw JSON object and nothing else.

OUTPUT CONTRACT — ANY VIOLATION WILL CRASH THE DESERIALIZER:
RULE 1: Your response MUST start with `{{` and end with `}}`. No characters before or after.
RULE 2: NO markdown. NO backticks. NO triple-backticks. NO "```json". NO "Here is your result:". NO explanations.
RULE 3: Output MUST exactly match this schema — no extra keys, no missing keys, no reordering:

EXACT REQUIRED SCHEMA:
{{
  "verdict": "CLEAN",
  "issues": [],
  "confidence": 0.95
}}

FIELD CONSTRAINTS:
- "verdict": string — MUST be exactly one of: "CLEAN", "HALLUCINATION", or "PARTIAL"
- "issues": array of strings — MUST be [] when verdict is "CLEAN"; list specific issues otherwise
- "confidence": float — MUST be a number between 0.0 and 1.0 (e.g. 0.87)

AUDIT TASK: Review the code below against the plan. Audit specifically for: {audit_targets}

CODE TO AUDIT (language: {lang}):
{code}

ORIGINAL PLAN STEPS:
{steps}

RESPOND WITH THE JSON OBJECT ONLY. YOUR FIRST CHARACTER MUST BE `{{`. YOUR LAST CHARACTER MUST BE `}}`."#,
        audit_targets = audit_targets,
        lang = lang,
        code = SABOTAGE_CODE,
        steps = steps
    );

    let client = Client::builder()
        .timeout(Duration::from_secs(120))
        .build()
        .expect("Failed to build reqwest client");

    let body = OllamaRequest {
        model: MODEL,
        prompt: &prompt,
        stream: false,
        format: "json",
        keep_alive: 0,
        options: OllamaOptions { num_ctx: 2048 },
    };

    println!("\n");
    println!("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
    println!("  DETERMINEX — PHASE 6 OBSERVER SABOTAGE TEST");
    println!("  Model   : {}", MODEL);
    println!("  Payload : broken Rust — type error, null UB, OOB panic, bad return");
    println!("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n");
    println!("  Sending request to Ollama (may take 15-60s on 6 GB GPU)...\n");

    let http_resp = client
        .post(OLLAMA_URL)
        .json(&body)
        .send()
        .await
        .expect("Ollama unreachable — is it running on :11434?");

    assert!(
        http_resp.status().is_success(),
        "Ollama returned HTTP {}",
        http_resp.status()
    );

    let envelope: OllamaResponse = http_resp
        .json()
        .await
        .expect("Failed to parse Ollama response envelope");

    assert!(envelope.done, "Ollama response was not marked done=true");

    let raw = &envelope.response;

    // ── Print the full raw output, never truncated ─────────────────────────────
    println!(
        "┌─ RAW OBSERVER OUTPUT ({} bytes) ─────────────────────────────────",
        raw.len()
    );
    println!("{}", raw);
    println!("└──────────────────────────────────────────────────────────────────\n");

    // ── Structural checks (pre-serde) ──────────────────────────────────────────
    let trimmed = raw.trim();
    let first_char = trimmed.chars().next().unwrap_or('\0');
    let last_char = trimmed.chars().last().unwrap_or('\0');

    let check_first = first_char == '{';
    let check_last = last_char == '}';
    let check_backtick = !raw.contains('`');
    let check_fence = !raw.contains("```");
    let check_here_is = !raw.to_lowercase().contains("here is");
    let check_note = !raw.to_lowercase().starts_with("note");

    println!("┌─ STRUCTURAL CHECKS ──────────────────────────────────────────────");
    println!(
        "  First non-whitespace == '{{' : {}",
        pass_fail(check_first)
    );
    println!("  Last  non-whitespace == '}}' : {}", pass_fail(check_last));
    println!(
        "  No backtick chars           : {}",
        pass_fail(check_backtick)
    );
    println!("  No ``` code fences          : {}", pass_fail(check_fence));
    println!(
        "  No 'Here is' preamble       : {}",
        pass_fail(check_here_is)
    );
    println!("  No 'Note:' preamble         : {}", pass_fail(check_note));
    println!("└──────────────────────────────────────────────────────────────────\n");

    // ── serde_json deserialization ─────────────────────────────────────────────
    println!("┌─ SERDE_JSON DESERIALIZATION ─────────────────────────────────────");
    match serde_json::from_str::<ObserverVerdict>(raw) {
        Ok(verdict) => {
            println!("  STATUS     : PASS — deserialized without error");
            println!("  verdict    : {:?}", verdict.verdict);
            println!("  confidence : {:.2}", verdict.confidence);
            println!("  issues     : {} item(s)", verdict.issues.len());
            for (i, issue) in verdict.issues.iter().enumerate() {
                println!("    [{}] {}", i, issue);
            }
            println!("└──────────────────────────────────────────────────────────────────\n");

            // Verdict must be one of the three known values
            assert!(
                ["CLEAN", "HALLUCINATION", "PARTIAL"].contains(&verdict.verdict.as_str()),
                "verdict field contained unexpected value: {:?}",
                verdict.verdict
            );

            // Confidence must be in-bounds
            assert!(
                verdict.confidence >= 0.0 && verdict.confidence <= 1.0,
                "confidence out of range: {}",
                verdict.confidence
            );

            // Warn (don't fail) if it called broken code CLEAN
            if verdict.verdict == "CLEAN" {
                println!("  WARNING: Observer called deliberately broken code CLEAN");
                println!("           This is a logic failure but NOT a JSON format failure.");
                println!("           The tollbooth held — the audit logic did not.\n");
            } else {
                println!(
                    "  Verdict is '{}' — Observer correctly identified problems.\n",
                    verdict.verdict
                );
            }

            // All structural checks must pass
            assert!(
                check_first,
                "Output did not start with '{{' — markdown or preamble leak"
            );
            assert!(
                check_last,
                "Output did not end with '}}' — trailing garbage"
            );
            assert!(
                check_backtick,
                "Output contained backtick characters — markdown leak"
            );
            assert!(
                check_fence,
                "Output contained ``` code fence — markdown leak"
            );
            assert!(
                check_here_is,
                "Output contained 'here is' preamble — conversational leak"
            );
            assert!(
                check_note,
                "Output started with 'note' — conversational leak"
            );

            println!("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
            println!("  FINAL: TOLLBOOTH HOLDS — Observer output is 100% pure JSON");
            println!("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n");
        }
        Err(e) => {
            println!("  STATUS  : FAIL — serde_json rejected the output");
            println!("  ERROR   : {}", e);
            println!("└──────────────────────────────────────────────────────────────────\n");
            println!("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
            println!("  FINAL: TOLLBOOTH BREACHED — Observer hallucinated non-JSON output");
            println!("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n");
            panic!("Observer output failed deserialization: {}", e);
        }
    }
}

fn pass_fail(ok: bool) -> &'static str {
    if ok {
        "PASS"
    } else {
        "FAIL"
    }
}
