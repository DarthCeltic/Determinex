//! crucible_flood_test.rs — Phase 11: VRAM Flood Physics Test
//!
//! Empirically proves that the Determinex sequential MPSC tollbooth prevents
//! concurrent Ollama inference from spiking past the the 6 GB ceiling.
//!
//! Architecture under test (mirrors orchestrator.rs exactly):
//!   5 concurrent senders → mpsc::channel(16) → single actor loop → one Ollama call at a time
//!
//! The test is self-contained. It does NOT depend on the Tauri app runtime.
//! It mirrors the exact Ollama wire types and actor pattern from orchestrator.rs.
//!
//! PASS criteria:
//!   • All 5 requests complete without error
//!   • Peak VRAM observed by nvidia-smi stays below 5800 MB
//!
//! Run: cargo test --test crucible_flood_test -- --nocapture

use reqwest::Client;
use serde::{Deserialize, Serialize};
use std::sync::{Arc, Mutex};
use std::time::{Duration, Instant};
use tokio::sync::{mpsc, oneshot, watch};
use tokio::task::JoinSet;

// ─────────────────────────────────────────────────────────────────────────────
// CONSTANTS
// ─────────────────────────────────────────────────────────────────────────────

const OLLAMA_URL: &str = "http://localhost:11434/api/generate";
/// Sentinel model — smallest VRAM footprint (llama3.2:3b @ ~2 GB).
/// Using the real production model, not a stub.
const MODEL: &str = "determinex-sentinel:v2";
const VRAM_CEILING_MB: u64 = 5800;
const FLOOD_SIZE: usize = 5;
const CHANNEL_CAPACITY: usize = 16; // identical to orchestrator.rs lib.rs spawn call

// ─────────────────────────────────────────────────────────────────────────────
// OLLAMA WIRE TYPES  (mirrored from orchestrator.rs — stays private there)
// ─────────────────────────────────────────────────────────────────────────────

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
    #[allow(dead_code)]
    response: String,
    done: bool,
}

// ─────────────────────────────────────────────────────────────────────────────
// ACTOR MESSAGE  (mirrors MoAMessage — stripped to the minimum needed)
// ─────────────────────────────────────────────────────────────────────────────

struct InferenceTicket {
    id: usize,
    reply: oneshot::Sender<Result<Duration, String>>,
}

// ─────────────────────────────────────────────────────────────────────────────
// OLLAMA CALL  (mirrors call_ollama in orchestrator.rs)
// ─────────────────────────────────────────────────────────────────────────────

async fn call_ollama(client: &Client, id: usize) -> Result<Duration, String> {
    let t0 = Instant::now();

    // Minimal prompt — we want the model to do real work (load into VRAM,
    // execute a forward pass) without wasting time on complex reasoning.
    let prompt = format!(
        "You are a test assistant. Respond ONLY with this exact JSON, nothing else: \
         {{\"id\": {id}, \"status\": \"ok\"}}",
        id = id
    );

    let body = OllamaRequest {
        model: MODEL,
        prompt: &prompt,
        stream: false,
        format: "json",
        // Force immediate VRAM eviction — identical to the production setting.
        keep_alive: 0,
        // Cap KV-cache — same as production to keep memory behaviour identical.
        options: OllamaOptions { num_ctx: 2048 },
    };

    let resp = client
        .post(OLLAMA_URL)
        .json(&body)
        .timeout(Duration::from_secs(300))
        .send()
        .await
        .map_err(|e| format!("Transport: {}", e))?;

    if !resp.status().is_success() {
        return Err(format!("HTTP {}", resp.status()));
    }

    let parsed: OllamaResponse = resp.json().await.map_err(|e| format!("Parse: {}", e))?;

    if !parsed.done {
        return Err("Response not marked done=true".into());
    }

    Ok(t0.elapsed())
}

// ─────────────────────────────────────────────────────────────────────────────
// VRAM SAMPLER
// ─────────────────────────────────────────────────────────────────────────────

fn sample_vram_mb() -> Option<u64> {
    let out = std::process::Command::new("nvidia-smi")
        .args(["--query-gpu=memory.used", "--format=csv,noheader,nounits"])
        .output()
        .ok()?;
    String::from_utf8_lossy(&out.stdout).trim().parse().ok()
}

// ─────────────────────────────────────────────────────────────────────────────
// THE FLOOD TEST
// ─────────────────────────────────────────────────────────────────────────────

#[tokio::test(flavor = "multi_thread", worker_threads = 4)]
async fn crucible_vram_flood() {
    // ── Pre-flight: verify Ollama is up ──────────────────────────────────────
    let client = Arc::new(
        Client::builder()
            .timeout(Duration::from_secs(300))
            .build()
            .expect("HTTP client build failed"),
    );

    match client.get("http://localhost:11434").send().await {
        Err(_) => {
            println!();
            println!("╔══════════════════════════════════════════════════════════════════╗");
            println!("║  [CRUCIBLE] SKIPPED — Ollama not reachable at localhost:11434    ║");
            println!("║  Start Ollama and ensure '{:<34}' is pulled. ║", MODEL);
            println!("╚══════════════════════════════════════════════════════════════════╝");
            println!();
            return;
        }
        Ok(r) if !r.status().is_success() && r.status().as_u16() != 200 => {
            // Ollama root returns 200 for a simple GET; anything else is suspicious
            // but we'll proceed — the real request will surface errors.
        }
        _ => {}
    }

    println!();
    println!(
        "[CRUCIBLE] Ollama reachable. Initiating VRAM flood — {} concurrent senders.",
        FLOOD_SIZE
    );

    // ── VRAM monitor: polls every 500 ms ─────────────────────────────────────
    let peak_vram: Arc<Mutex<u64>> = Arc::new(Mutex::new(0));
    let vram_samples: Arc<Mutex<Vec<(u64, u64)>>> = Arc::new(Mutex::new(Vec::new())); // (elapsed_ms, mb)
    let (stop_tx, mut stop_rx) = watch::channel(false);

    {
        let peak_c = peak_vram.clone();
        let samples_c = vram_samples.clone();
        let wall = Instant::now();
        tokio::spawn(async move {
            loop {
                tokio::select! {
                    _ = stop_rx.changed() => {
                        if *stop_rx.borrow() { break; }
                    }
                    _ = tokio::time::sleep(Duration::from_millis(500)) => {
                        if let Some(mb) = sample_vram_mb() {
                            let elapsed = wall.elapsed().as_millis() as u64;
                            {
                                let mut p = peak_c.lock().unwrap();
                                if mb > *p { *p = mb; }
                            }
                            samples_c.lock().unwrap().push((elapsed, mb));
                        }
                    }
                }
            }
        });
    }

    // ── Sequential actor: one Ollama call at a time ──────────────────────────
    // This is the TOLLBOOTH. Identical architecture to the Orchestrator actor
    // in orchestrator.rs — the MPSC channel is the sequencing primitive.
    let (tx, mut rx) = mpsc::channel::<InferenceTicket>(CHANNEL_CAPACITY);

    {
        let actor_client = client.clone();
        tokio::spawn(async move {
            // recv().await will NOT return the next message until the previous
            // match arm completes. This is the sequential guarantee.
            while let Some(ticket) = rx.recv().await {
                let result = call_ollama(&actor_client, ticket.id).await;
                // reply send failure means the sender timed-out or was dropped —
                // not an actor-loop concern; we continue processing the queue.
                let _ = ticket.reply.send(result);
            }
        });
    }

    // ── Flood: all 5 senders enqueue simultaneously ───────────────────────────
    let wall_start = Instant::now();
    let mut set = JoinSet::new();

    for i in 0..FLOOD_SIZE {
        let tx_c = tx.clone();
        set.spawn(async move {
            let (reply_tx, reply_rx) = oneshot::channel();
            let enqueue_t = Instant::now();

            tx_c.send(InferenceTicket {
                id: i,
                reply: reply_tx,
            })
            .await
            .unwrap_or_else(|_| panic!("Actor channel closed before request {} could enqueue", i));

            let enqueue_ms = enqueue_t.elapsed().as_millis();

            // Block here until the actor finishes this specific request.
            match reply_rx.await {
                Ok(Ok(latency)) => {
                    println!(
                        "[CRUCIBLE] Request {:>2} complete  enqueue={:>5}ms  inference={:>7}ms",
                        i,
                        enqueue_ms,
                        latency.as_millis()
                    );
                    (i, enqueue_ms, latency, true)
                }
                Ok(Err(e)) => {
                    eprintln!("[CRUCIBLE] Request {:>2} FAILED: {}", i, e);
                    (i, enqueue_ms, Duration::ZERO, false)
                }
                Err(_) => {
                    eprintln!("[CRUCIBLE] Request {:>2} reply channel dropped", i);
                    (i, enqueue_ms, Duration::ZERO, false)
                }
            }
        });
    }

    // Drop the extra sender clone so the actor loop can detect EOF when all tasks finish.
    drop(tx);

    // Collect results in completion order, then sort by id for display.
    let mut results: Vec<(usize, u128, Duration, bool)> = Vec::new();
    while let Some(r) = set.join_next().await {
        results.push(r.expect("Flood task panicked"));
    }
    results.sort_by_key(|(i, _, _, _)| *i);

    let total_time = wall_start.elapsed();

    // ── Stop VRAM monitor ─────────────────────────────────────────────────────
    let _ = stop_tx.send(true);
    // Give the monitor one final poll window to record the post-run idle VRAM.
    tokio::time::sleep(Duration::from_millis(600)).await;

    // ── Crunch numbers ────────────────────────────────────────────────────────
    let peak = *peak_vram.lock().unwrap();
    let samples = vram_samples.lock().unwrap().clone();

    let completed = results.iter().filter(|(_, _, _, ok)| *ok).count();
    let avg_latency_ms: u128 = if completed > 0 {
        results
            .iter()
            .filter(|(_, _, _, ok)| *ok)
            .map(|(_, _, l, _)| l.as_millis())
            .sum::<u128>()
            / completed as u128
    } else {
        0
    };

    // ── Print empirical results ───────────────────────────────────────────────
    println!();
    println!("╔══════════════════════════════════════════════════════════════════╗");
    println!("║            DETERMINEX CRUCIBLE — VRAM FLOOD RESULTS                ║");
    println!("╠══════════════════════════════════════════════════════════════════╣");
    println!("║  Architecture   : Sequential MPSC tollbooth (actor pattern)     ║");
    println!(
        "║  Channel capacity         : {:>4}                               ║",
        CHANNEL_CAPACITY
    );
    println!(
        "║  Concurrent senders fired : {:>4}                               ║",
        FLOOD_SIZE
    );
    println!(
        "║  Requests completed       : {:>4} / {:<4}                          ║",
        completed, FLOOD_SIZE
    );
    println!("║  Model                    : {:<36} ║", MODEL);
    println!("║  keep_alive               : 0  (immediate VRAM eviction)        ║");
    println!("║  num_ctx                  : 2048  (capped KV-cache)             ║");
    println!("╠══════════════════════════════════════════════════════════════════╣");
    println!(
        "║  Total wall time          : {:>10} ms                         ║",
        total_time.as_millis()
    );
    println!(
        "║  Avg per-request latency  : {:>10} ms                         ║",
        avg_latency_ms
    );
    println!(
        "║  Peak VRAM observed       : {:>10} MB                         ║",
        peak
    );
    println!(
        "║  VRAM hard ceiling        : {:>10} MB                         ║",
        VRAM_CEILING_MB
    );
    println!(
        "║  VRAM headroom            : {:>10} MB                         ║",
        VRAM_CEILING_MB.saturating_sub(peak)
    );
    println!("╠══════════════════════════════════════════════════════════════════╣");
    println!("║  Per-request breakdown:                                          ║");
    for (i, enqueue_ms, latency, ok) in &results {
        println!(
            "║    [Req {:>2}]  enqueue {:>6}ms  inference {:>8}ms  [{}]    ║",
            i,
            enqueue_ms,
            latency.as_millis(),
            if *ok { "PASS" } else { "FAIL" }
        );
    }
    if !samples.is_empty() {
        println!("╠══════════════════════════════════════════════════════════════════╣");
        println!("║  VRAM timeline (nvidia-smi @ 500ms):                             ║");
        // Print every sample to give a shape of the VRAM curve
        for (t_ms, mb) in &samples {
            let bar_len = (*mb as usize / 200).min(30);
            let bar: String = "█".repeat(bar_len);
            println!(
                "║    t={:>6}ms  {:>5} MB  {}{}  ║",
                t_ms,
                mb,
                bar,
                " ".repeat(30 - bar_len)
            );
        }
    }
    println!("╠══════════════════════════════════════════════════════════════════╣");

    let verdict = if peak == 0 {
        "? WARN — nvidia-smi unavailable, VRAM not measured      "
    } else if peak < VRAM_CEILING_MB {
        "✓ PASS — Sequential tollbooth held. Ceiling not breached."
    } else {
        "✗ FAIL — VRAM CEILING BREACHED. Concurrent inference!   "
    };
    println!("║  VERDICT: {}  ║", verdict);
    println!("╚══════════════════════════════════════════════════════════════════╝");
    println!();

    // ── Hard assertions ───────────────────────────────────────────────────────
    assert!(
        completed > 0,
        "Every request failed. Ollama may have crashed or {} is not pulled.",
        MODEL
    );

    assert!(
        completed == FLOOD_SIZE,
        "{} / {} requests failed. Check Ollama logs.",
        FLOOD_SIZE - completed,
        FLOOD_SIZE
    );

    if peak > 0 {
        assert!(
            peak < VRAM_CEILING_MB,
            "VRAM CEILING BREACHED: {} MB >= {} MB. \
             The sequential tollbooth failed to prevent concurrent inference.",
            peak,
            VRAM_CEILING_MB
        );
    }
}
