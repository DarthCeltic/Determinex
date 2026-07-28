// Bridges scripts/determinex_agents.py -- the registry of external coding-agent
// CLIs (Claude Code, Codex, Gemini CLI, aider, cursor-agent) that Determinex can
// host as sub-agents. Listing is read-only (just `shutil.which` probes). Running
// one shells out to the real installed CLI against the given workspace, then
// verifies its edits through Determinex's own oracle (repair_workspace) before
// reporting success -- an agent's own claim of "done" is never trusted alone.
//
// Ryan, live: "i want this ide addon to be available (claude for vsc)... as well
// as codex and gemini and all of that." The Python registry already existed with
// zero frontend surface; this is the missing bridge + a real addon panel.

use serde::{Deserialize, Serialize};
use std::io::{Read, Write};
use std::path::PathBuf;
use std::process::{Command, Stdio};
use std::sync::{Arc, Mutex};
use std::time::{Duration, Instant};
use tauri::{AppHandle, Emitter};

use crate::project_audit::run_with_timeout;
use crate::win_process::HideConsoleExt;

const AGENTS_SCRIPT: &str = "scripts/determinex_agents.py";

// The Python side (determinex_agents.py) emits plain snake_case JSON --
// Python convention, not negotiable there. These structs are deserialized
// FROM that JSON first, then re-serialized TO the frontend as camelCase --
// asymmetric rename so each direction matches its own side's convention.
// A single `rename_all = "camelCase"` here made deserialization expect
// "installHint" from Python's actual "install_hint", failing every call
// with "malformed agent list JSON: missing field `installHint`" -- found
// live the first time this panel was opened.
#[derive(Debug, Serialize, Deserialize, Clone)]
#[serde(rename_all(serialize = "camelCase", deserialize = "snake_case"))]
pub struct CodingAgentInfo {
    pub name: String,
    pub probe: String,
    pub installed: bool,
    pub install_hint: String,
    pub aliases: Vec<String>,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
#[serde(rename_all(serialize = "camelCase", deserialize = "snake_case"))]
pub struct CodingAgentRunResult {
    pub agent: String,
    pub verified: bool,
    pub ran: bool,
    pub raw: String,
    pub oracle: String,
    pub n_failures: u32,
    pub note: String,
    pub next_moves: Vec<String>,
}

fn locate_repo_root() -> Option<PathBuf> {
    let cwd = std::env::current_dir().ok()?;
    let mut cur: Option<&std::path::Path> = Some(cwd.as_path());
    while let Some(c) = cur {
        if c.join(AGENTS_SCRIPT).is_file() {
            return Some(c.to_path_buf());
        }
        cur = c.parent();
    }
    None
}

#[tauri::command]
pub async fn list_coding_agents() -> Result<Vec<CodingAgentInfo>, String> {
    let root = locate_repo_root()
        .ok_or_else(|| format!("could not locate repo root ({AGENTS_SCRIPT} missing)"))?;

    let mut cmd = Command::new("python");

    cmd.hide_console();
    cmd.arg(root.join(AGENTS_SCRIPT));
    cmd.arg("list");
    cmd.arg("--json");
    cmd.current_dir(&root);

    let output = run_with_timeout(cmd, Duration::from_secs(15))
        .map_err(|e| format!("could not run agent registry: {e}"))?;
    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        return Err(format!("agent registry exited non-zero: {stderr}"));
    }
    let stdout = String::from_utf8_lossy(&output.stdout);
    crate::python_json::parse_python_json(&stdout, "agent registry")
}

/// Runs a real, installed coding-agent CLI against the given workspace with the
/// given task, then verifies the result through Determinex's oracle -- same
/// trust model as every other execution path in this app: the agent's own
/// "done" is advisory, the compiler/test run is the source of truth. Bounded to
/// 5 minutes so a hung agent CLI can't block the UI indefinitely.
#[tauri::command]
pub async fn run_coding_agent(
    agent: String,
    task: String,
    workspace: String,
) -> Result<CodingAgentRunResult, String> {
    let root = locate_repo_root()
        .ok_or_else(|| format!("could not locate repo root ({AGENTS_SCRIPT} missing)"))?;

    let mut cmd = Command::new("python");

    cmd.hide_console();
    cmd.arg(root.join(AGENTS_SCRIPT));
    cmd.arg("run");
    cmd.arg(&agent);
    cmd.arg(&task);
    cmd.arg("--workspace");
    cmd.arg(&workspace);
    cmd.current_dir(&root);

    let output = run_with_timeout(cmd, Duration::from_secs(310))
        .map_err(|e| format!("could not run agent: {e}"))?;
    let stdout = String::from_utf8_lossy(&output.stdout);
    crate::python_json::parse_python_json(&stdout, "agent run").map_err(|e| {
        let stderr = String::from_utf8_lossy(&output.stderr);
        format!("{e} (stderr: {stderr})")
    })
}

// ── Roster status (Ryan: "I want to see everything who's online, what their
// credits are at") ───────────────────────────────────────────────────────
// Two tiers, deliberately kept separate:
//   1. Cheap status (below): each CLI's own auth-status subcommand
//      (claude/codex) or, for gemini-cli which ships no such command, a
//      local credential-file presence check. Free, fast, no model call --
//      safe to poll on an interval.
//   2. Live probe (agent_probe_test): a REAL minimal prompt, actually
//      spawned and streamed. This is the only way to learn things a status
//      file can't contain -- proven live: gemini-cli's stored OAuth creds
//      parse fine, but a real call surfaces "Your prepayment credits are
//      depleted." Manual-trigger only (costs real quota), never auto-polled.
#[derive(Debug, Serialize, Deserialize, Clone)]
#[serde(rename_all(serialize = "camelCase", deserialize = "snake_case"))]
pub struct AgentStatusEntry {
    pub name: String,
    pub installed: bool,
    pub auth_known: bool,
    pub logged_in: bool,
    pub plan: String,
    pub detail: String,
    pub install_hint: String,
}

#[tauri::command]
pub async fn agent_status_roster() -> Result<Vec<AgentStatusEntry>, String> {
    let root = locate_repo_root()
        .ok_or_else(|| format!("could not locate repo root ({AGENTS_SCRIPT} missing)"))?;

    let mut cmd = Command::new("python");
    cmd.hide_console();
    cmd.arg(root.join(AGENTS_SCRIPT));
    cmd.arg("status");
    cmd.arg("--json");
    cmd.current_dir(&root);

    let output = run_with_timeout(cmd, Duration::from_secs(20))
        .map_err(|e| format!("could not run agent status: {e}"))?;
    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        return Err(format!("agent status exited non-zero: {stderr}"));
    }
    let stdout = String::from_utf8_lossy(&output.stdout);
    crate::python_json::parse_python_json(&stdout, "agent status")
}

const PROBE_PROMPT: &str = "Reply with exactly the single word: OK";
const PROBE_TIMEOUT: Duration = Duration::from_secs(45);

#[derive(Debug, Serialize, Clone)]
#[serde(rename_all = "camelCase")]
struct AgentProbeOutputEvent {
    agent: String,
    stream: String,
    chunk: String,
}

#[derive(Debug, Serialize, Clone)]
#[serde(rename_all = "camelCase")]
struct AgentProbeCompleteEvent {
    agent: String,
    status: String, // "ok" | "quota_exhausted" | "auth_error" | "timeout" | "error"
    detail: String,
    raw_tail: String,
}

/// Deterministic pattern match over the CLI's own real output -- never an
/// LLM judgement (this repo's whole thesis: a compiler/parser is the
/// oracle, not a model's opinion). Only recognizes patterns actually
/// observed live from these three CLIs; unrecognized non-zero exits fall
/// through to a generic "error" with the last non-empty line as detail
/// rather than guessing a category.
fn classify_probe(raw: &str, returncode: Option<i32>, timed_out: bool) -> (&'static str, String) {
    let lower = raw.to_lowercase();
    if lower.contains("resource_exhausted")
        || lower.contains("credits are depleted")
        || lower.contains("prepayment")
        || (lower.contains("quota") && (lower.contains("exceed") || lower.contains("exhaust")))
    {
        let detail = raw
            .lines()
            .find(|l| l.to_lowercase().contains("message"))
            .unwrap_or("quota/billing exhausted")
            .trim()
            .to_string();
        return ("quota_exhausted", detail);
    }
    if lower.contains("429") && lower.contains("rate") {
        return ("quota_exhausted", "rate limited (429)".to_string());
    }
    if lower.contains("not logged in")
        || lower.contains("unauthorized")
        || lower.contains("401")
        || lower.contains("invalid api key")
        || lower.contains("authentication_error")
    {
        let detail = raw
            .lines()
            .rev()
            .find(|l| !l.trim().is_empty())
            .unwrap_or("authentication error")
            .trim()
            .to_string();
        return ("auth_error", detail);
    }
    if timed_out {
        return (
            "timeout",
            format!("no terminal response within {}s", PROBE_TIMEOUT.as_secs()),
        );
    }
    if returncode == Some(0) {
        return ("ok", "responded".to_string());
    }
    if returncode.is_none() {
        // Still running, no recognized pattern yet -- not a verdict.
        return ("pending", String::new());
    }
    let detail = raw
        .lines()
        .rev()
        .find(|l| !l.trim().is_empty())
        .unwrap_or("unknown error")
        .trim()
        .to_string();
    ("error", detail)
}

fn spawn_probe_stream_reader(
    app: AppHandle,
    agent: String,
    stream: String,
    pipe: Option<impl Read + Send + 'static>,
    accumulated: Arc<Mutex<String>>,
) -> std::thread::JoinHandle<()> {
    std::thread::spawn(move || {
        let Some(mut pipe) = pipe else { return };
        let mut buf = [0u8; 4096];
        loop {
            match pipe.read(&mut buf) {
                Ok(0) => break,
                Ok(n) => {
                    let chunk = String::from_utf8_lossy(&buf[..n]).to_string();
                    if let Ok(mut acc) = accumulated.lock() {
                        acc.push_str(&chunk);
                    }
                    let _ = app.emit(
                        "agent-probe-output",
                        AgentProbeOutputEvent { agent: agent.clone(), stream: stream.clone(), chunk },
                    );
                }
                Err(_) => break,
            }
        }
    })
}

/// Fires one real, minimal prompt at an installed agent CLI and streams the
/// genuine result live -- the only trustworthy way to know an agent is
/// actually WORKING right now (not just "has stored credentials"). Manual
/// trigger only: this is a real model call and, for a quota-exhausted
/// account, will genuinely fail -- which is the point.
#[tauri::command]
pub async fn agent_probe_test(agent: String, workspace: String, app: AppHandle) -> Result<(), String> {
    let root = locate_repo_root()
        .ok_or_else(|| format!("could not locate repo root ({AGENTS_SCRIPT} missing)"))?;

    // Same single-source-of-truth `resolve` subcommand the chat pipeline
    // uses, with a short diagnostic prompt standing in for a real task.
    let mut resolve_cmd = Command::new("python");
    resolve_cmd.hide_console();
    resolve_cmd.arg(root.join(AGENTS_SCRIPT));
    resolve_cmd.arg("resolve");
    resolve_cmd.arg(&agent);
    resolve_cmd.arg(PROBE_PROMPT);
    resolve_cmd.arg("--workspace");
    resolve_cmd.arg(&workspace);
    resolve_cmd.current_dir(&root);
    let resolve_out = run_with_timeout(resolve_cmd, Duration::from_secs(15))
        .map_err(|e| format!("could not resolve probe argv: {e}"))?;
    let resolved: serde_json::Value = serde_json::from_slice(&resolve_out.stdout)
        .map_err(|e| format!("malformed resolve JSON: {e}"))?;
    if let Some(err) = resolved.get("error").and_then(|e| e.as_str()) {
        return Err(err.to_string());
    }
    let argv: Vec<String> = resolved
        .get("argv")
        .and_then(|a| a.as_array())
        .map(|arr| arr.iter().filter_map(|x| x.as_str().map(String::from)).collect())
        .unwrap_or_default();
    if argv.is_empty() {
        return Err("resolved probe argv was empty".to_string());
    }
    let installed = resolved.get("available").and_then(|a| a.as_bool()).unwrap_or(false);
    if !installed {
        let hint = resolved.get("install_hint").and_then(|h| h.as_str()).unwrap_or("");
        return Err(format!("agent '{agent}' is not installed ({hint})"));
    }
    let stdin_prompt = resolved.get("stdin_prompt").and_then(|b| b.as_bool()).unwrap_or(false);

    let mut cmd = Command::new(&argv[0]);
    cmd.hide_console();
    cmd.args(&argv[1..]);
    cmd.current_dir(&workspace);
    if stdin_prompt {
        cmd.stdin(Stdio::piped());
    }
    cmd.stdout(Stdio::piped());
    cmd.stderr(Stdio::piped());

    let mut child = cmd.spawn().map_err(|e| format!("failed to spawn agent CLI: {e}"))?;

    if stdin_prompt {
        if let Some(mut stdin) = child.stdin.take() {
            std::thread::spawn(move || {
                let _ = stdin.write_all(PROBE_PROMPT.as_bytes());
            });
        }
    }

    let accumulated = Arc::new(Mutex::new(String::new()));
    let out_handle = spawn_probe_stream_reader(
        app.clone(), agent.clone(), "stdout".to_string(), child.stdout.take(), accumulated.clone(),
    );
    let err_handle = spawn_probe_stream_reader(
        app.clone(), agent.clone(), "stderr".to_string(), child.stderr.take(), accumulated.clone(),
    );

    let start = Instant::now();
    let mut timed_out = false;
    loop {
        // Early-exit the moment the accumulated text already contains a
        // recognizable FAILURE pattern -- gemini-cli's own 3x
        // exponential-backoff retry loop otherwise burns 60-90s per probe
        // even though attempt 1 already said everything (proven live:
        // "prepayment credits are depleted" on the first try). Success can
        // only be confirmed by a real clean exit, so this never fires early
        // on "ok".
        let early = accumulated.lock().ok().map(|acc| classify_probe(&acc, None, false).0 != "pending");
        if early == Some(true) {
            break;
        }
        match child.try_wait() {
            Ok(Some(_)) => break,
            Ok(None) => {
                if start.elapsed() > PROBE_TIMEOUT {
                    timed_out = true;
                    break;
                }
                std::thread::sleep(Duration::from_millis(150));
            }
            Err(_) => break,
        }
    }
    let _ = child.kill();
    let returncode = child.wait().ok().and_then(|s| s.code());
    let _ = out_handle.join();
    let _ = err_handle.join();

    let raw = accumulated.lock().map(|g| g.clone()).unwrap_or_default();
    let (status, detail) = classify_probe(&raw, returncode, timed_out);
    let status = if status == "pending" { "error" } else { status };
    // Char-based (not byte-index) slicing -- raw came from
    // String::from_utf8_lossy chunks, but an arbitrary byte offset can still
    // land mid-character and panic a direct &raw[n..] slice.
    let raw_tail: String = {
        let chars: Vec<char> = raw.chars().collect();
        let start = chars.len().saturating_sub(2000);
        chars[start..].iter().collect()
    };

    let _ = app.emit(
        "agent-probe-complete",
        AgentProbeCompleteEvent { agent, status: status.to_string(), detail, raw_tail },
    );
    Ok(())
}
