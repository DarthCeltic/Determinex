//! Shared preflight for the Ollama-backed integration tests.
//!
//! WHY THIS EXISTS (2026-07-31). Four integration test binaries each gated themselves on a
//! reachability check of the shape:
//!
//! ```text
//! if !ollama_is_reachable(&client).await { println!("SKIPPED — run: ollama serve"); return; }
//! ```
//!
//! That guard answers "does the daemon respond". The tests need "is the model pulled". So on a box
//! with Ollama running but a given tag absent, the guard passed and the test then failed on its
//! first generate with `Ollama HTTP 404 Not Found` — reported as a test failure rather than a
//! skipped prerequisite.
//!
//! It was worse than an under-provisioning problem: the tags themselves were up to three
//! generations stale (`determinex-sentinel:v2`, `determinex-engineer:v2`, `determinex-observer:v3`
//! against the shipped `determinex-sentinel-v5-dsl`, `determinex-engineer-v11-dsl`,
//! `determinex-observer-v6-dsl`), so the 404 was guaranteed on EVERY machine. And because
//! `cargo test` stops at the first failing target, those failures masked the state of every target
//! after them — which is how "Rust 82/82" stayed believable while 8 targets were red. 82/82 was
//! true of the unit-test binary alone.
//!
//! A missing multi-gigabyte model is a missing prerequisite, not a defect, so these helpers skip.
//! A model that IS present is exercised for real.
//!
//! `tests/common/mod.rs` rather than a copy per file: `tests/*.rs` each compile to their own test
//! binary, but a subdirectory module does not, so this is the idiomatic shared place.

use std::collections::HashSet;
use std::time::Duration;

use reqwest::Client;

/// Environment-supplied prerequisites, or `None` after printing why the test is skipped.
///
/// The companion-RAG tests take a seeded database, a local fastembed model directory and an output
/// artifact path from the environment — inputs an external harness provides. Each read them with
/// `env::var(...).expect("... must point to ...")`, so running `cargo test` without that harness
/// did not report "prerequisite absent", it reported three test FAILURES. That is the same
/// distinction the Ollama guards above get wrong in the other direction, and it is what made the
/// Rust suite unrunnable by default: `cargo test` stops at the first failing target, so these
/// masked everything after them.
///
/// Returns the values in the order requested, so callers keep their positional reads.
pub fn required_env(test_name: &str, keys: &[&str]) -> Option<Vec<String>> {
    let mut values = Vec::with_capacity(keys.len());
    let mut missing = Vec::new();
    for key in keys {
        match std::env::var(key) {
            Ok(value) if !value.trim().is_empty() => values.push(value),
            _ => missing.push(*key),
        }
    }
    if missing.is_empty() {
        return Some(values);
    }
    println!();
    println!("── {test_name} — SKIPPED ─────────────────────────────────────────");
    println!("   This test is driven by an external harness that provisions its inputs.");
    println!("   Not set:");
    for key in &missing {
        println!("     {key}");
    }
    println!("   Absent prerequisites are not a defect; set them to run it for real.");
    println!();
    None
}

/// Ollama tag for a role, overridable so a rename cannot silently rot the defaults again.
pub fn model_for(env_key: &str, default: &str) -> String {
    std::env::var(env_key)
        .ok()
        .filter(|v| !v.trim().is_empty())
        .unwrap_or_else(|| default.to_string())
}

/// Every model tag Ollama currently has, or `None` when the daemon cannot be reached at all.
pub async fn installed_models(client: &Client, tags_url: &str) -> Option<HashSet<String>> {
    let response = client
        .get(tags_url)
        .timeout(Duration::from_secs(5))
        .send()
        .await
        .ok()?;
    if !response.status().is_success() {
        return None;
    }
    let body: serde_json::Value = response.json().await.ok()?;
    let mut names = HashSet::new();
    for entry in body.get("models")?.as_array()? {
        if let Some(name) = entry.get("name").and_then(|n| n.as_str()) {
            names.insert(name.to_string());
            // Ollama reports "foo:latest"; callers may ask for the bare "foo".
            if let Some(bare) = name.strip_suffix(":latest") {
                names.insert(bare.to_string());
            }
        }
    }
    Some(names)
}

/// Why a test cannot run, or `None` when every prerequisite is satisfied.
pub enum Unmet {
    OllamaUnreachable,
    ModelsMissing(Vec<String>),
    /// The models exist but this host cannot hold them all at once.
    InsufficientMemory { required: Vec<String>, resident: Vec<String> },
}

/// Load each model, then check they are all resident AT THE SAME TIME.
///
/// MEASURED on the dev box (GTX 1660 Ti, 6 GB): a cold `determinex-sentinel-v5-dsl` generate takes
/// **102 s**; the same call warm takes **1 s**. These benchmarks use a 60 s inference timeout
/// described in their own source as "same as the production orchestrator", and that is a fair
/// number — production keeps models resident (`keep_alive: -1` for the builder role, see
/// `hive/api_client._ollama_extra`) and therefore only ever pays the warm cost. A cold load inside
/// a production-shaped timeout is an artefact of the test, not a property of the product.
///
/// So warming happens outside the measured window. But warming alone is not enough: the three
/// models this pipeline needs total ~12.6 GB against 6 GB of VRAM, so they evict each other and
/// every role switch pays 102 s again. Residency is therefore checked via `/api/ps` rather than
/// assumed — if the host cannot hold them together, the benchmark cannot run here, and that is a
/// hardware statement to report rather than a failure to record.
pub async fn residency_shortfall(
    client: &Client,
    generate_url: &str,
    ps_url: &str,
    wanted: &[&str],
) -> Option<Unmet> {
    for model in wanted {
        let body = serde_json::json!({
            "model": model,
            "prompt": "Reply with the single word OK.",
            "stream": false,
            "options": { "num_predict": 1 },
        });
        // Generous on purpose: this is the cold load, and 102 s was measured on a card two sizes
        // below the model. Failing here means the model cannot run at all on this host.
        let ok = client
            .post(generate_url)
            .json(&body)
            .timeout(Duration::from_secs(300))
            .send()
            .await
            .map(|r| r.status().is_success())
            .unwrap_or(false);
        if !ok {
            return Some(Unmet::InsufficientMemory {
                required: wanted.iter().map(|m| (*m).to_string()).collect(),
                resident: Vec::new(),
            });
        }
    }

    let resident = loaded_models(client, ps_url).await.unwrap_or_default();
    let missing: Vec<String> = wanted
        .iter()
        .filter(|m| !resident.iter().any(|r| r == *m || r == &format!("{m}:latest")))
        .map(|m| (*m).to_string())
        .collect();
    if missing.is_empty() {
        None
    } else {
        Some(Unmet::InsufficientMemory {
            required: wanted.iter().map(|m| (*m).to_string()).collect(),
            resident,
        })
    }
}

/// Models Ollama currently has LOADED (`/api/ps`), as opposed to merely pulled (`/api/tags`).
pub async fn loaded_models(client: &Client, ps_url: &str) -> Option<Vec<String>> {
    let response = client
        .get(ps_url)
        .timeout(Duration::from_secs(10))
        .send()
        .await
        .ok()?;
    if !response.status().is_success() {
        return None;
    }
    let body: serde_json::Value = response.json().await.ok()?;
    Some(
        body.get("models")?
            .as_array()?
            .iter()
            .filter_map(|m| m.get("name").and_then(|n| n.as_str()).map(str::to_string))
            .collect(),
    )
}

/// The preflight the old reachability check should have been.
pub async fn unmet_prerequisites(
    client: &Client,
    tags_url: &str,
    wanted: &[&str],
) -> Option<Unmet> {
    let installed = match installed_models(client, tags_url).await {
        Some(names) => names,
        None => return Some(Unmet::OllamaUnreachable),
    };
    let missing: Vec<String> = wanted
        .iter()
        .filter(|m| !installed.contains(**m) && !installed.contains(&format!("{m}:latest")))
        .map(|m| (*m).to_string())
        .collect();
    if missing.is_empty() {
        None
    } else {
        Some(Unmet::ModelsMissing(missing))
    }
}

/// Print a skip banner naming the exact unmet prerequisite and how to satisfy it.
///
/// Returns true when the caller should `return` (skip). The message distinguishes "no daemon" from
/// "daemon up, model absent" because the fixes are different commands, and the old banner always
/// said `ollama serve` even when Ollama was already running.
pub fn should_skip(test_name: &str, unmet: Option<Unmet>) -> bool {
    match unmet {
        None => false,
        Some(Unmet::OllamaUnreachable) => {
            println!();
            println!("── {test_name} — SKIPPED ─────────────────────────────────────────");
            println!("   Ollama is not reachable. Start it with:  ollama serve");
            println!();
            true
        }
        Some(Unmet::ModelsMissing(missing)) => {
            println!();
            println!("── {test_name} — SKIPPED ─────────────────────────────────────────");
            println!("   Ollama is running, but these models are not pulled:");
            for model in &missing {
                println!("     ollama pull {model}");
            }
            println!("   (override a tag with DETERMINEX_<ROLE>_MODEL if yours differs)");
            println!();
            true
        }
        Some(Unmet::InsufficientMemory { required, resident }) => {
            println!();
            println!("── {test_name} — SKIPPED ─────────────────────────────────────────");
            println!("   This host cannot hold the models this benchmark needs at once, so every");
            println!("   role switch would pay a cold load (measured: 102 s cold vs 1 s warm) and");
            println!("   blow the production-shaped 60 s inference timeout.");
            println!("   required: {}", required.join(", "));
            println!(
                "   resident after warm-up: {}",
                if resident.is_empty() { "none".to_string() } else { resident.join(", ") }
            );
            println!("   This is a hardware limit, not a defect. Run it on a host with enough VRAM");
            println!("   to hold them together.");
            println!();
            true
        }
    }
}
