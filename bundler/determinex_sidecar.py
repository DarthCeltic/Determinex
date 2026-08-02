"""
bundler/determinex_sidecar.py — Determinex NDJSON Inference Server

This is the process that runs inside the embedded Python sidecar.
The Tauri Rust backend spawns it as a subprocess and communicates
via newline-delimited JSON (NDJSON) over stdin/stdout.

NO DEPENDENCIES except llama_cpp and the Python standard library.
This file must be self-contained — it runs inside the stripped-down
embedded Python distribution.

IPC Protocol:
    All messages are single-line JSON followed by a newline.
    Avoid print() for anything except protocol responses — stderr is used
    for logging (Tauri's Command captures stderr separately).

REQUEST FORMATS:
  Load a model:
    {"id": "1", "action": "load", "model_path": "/path/to/model.gguf",
     "n_gpu_layers": 20, "n_ctx": 4096}

  Run inference:
    {"id": "2", "action": "infer", "prompt": "...", "max_tokens": 512,
     "temperature": 0.1, "stop": ["\n\n"]}

  Get status:
    {"id": "3", "action": "status"}

  Graceful shutdown:
    {"id": "4", "action": "quit"}

RESPONSE FORMATS:
  Success:
    {"id": "1", "ok": true, "data": {...}}

  Token stream (infer):
    {"id": "2", "token": "Hello", "done": false}
    {"id": "2", "token": " world", "done": false}
    {"id": "2", "token": "", "done": true, "total_tokens": 42}

  Error:
    {"id": "1", "ok": false, "error": "Model not loaded"}

TAURI INTEGRATION (Rust):
    From sidecar.rs / orchestrator.rs:

    let mut child = std::process::Command::new("bundler/sidecar/python/python.exe")
        .arg("bundler/sidecar/determinex_sidecar.py")
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()?;

    // Write request:
    let req = serde_json::json!({"id": "1", "action": "load", "model_path": model_path});
    writeln!(child.stdin.as_mut().unwrap(), "{}", req.to_string())?;

    // Read response:
    let reader = BufReader::new(child.stdout.take().unwrap());
    for line in reader.lines() {
        let resp: serde_json::Value = serde_json::from_str(&line?)?;
        // handle response
    }
"""

import json
import os
import sys
import threading
import time


# Stderr for logs (Tauri captures this separately, never mixed with the NDJSON protocol)
def _log(msg: str):
    print(f"[Sidecar] {msg}", file=sys.stderr, flush=True)


# ---------------------------------------------------------------------------
# PROTOCOL HELPERS
# ---------------------------------------------------------------------------


def _send(payload: dict):
    """Write a single NDJSON line to stdout."""
    line = json.dumps(payload, ensure_ascii=False)
    sys.stdout.write(line + "\n")
    sys.stdout.flush()


def _send_ok(req_id: str, data: dict = None):
    _send({"id": req_id, "ok": True, "data": data or {}})


def _send_error(req_id: str, message: str):
    _send({"id": req_id, "ok": False, "error": message})


def _send_token(req_id: str, token: str, done: bool, total_tokens: int = 0):
    payload = {"id": req_id, "token": token, "done": done}
    if done:
        payload["total_tokens"] = total_tokens
    _send(payload)


# ---------------------------------------------------------------------------
# SIDECAR STATE
# ---------------------------------------------------------------------------


class SidecarState:
    def __init__(self):
        self.model = None  # llama_cpp.Llama instance
        self.model_path = ""
        self.n_gpu_layers = 0
        self.n_ctx = 2048
        self.loaded = False
        self.lock = threading.Lock()

    def status(self) -> dict:
        return {
            "loaded": self.loaded,
            "model_path": self.model_path,
            "n_gpu_layers": self.n_gpu_layers,
            "n_ctx": self.n_ctx,
        }


# ---------------------------------------------------------------------------
# HANDLERS
# ---------------------------------------------------------------------------


def handle_load(state: SidecarState, req: dict) -> bool:
    req_id = req.get("id", "?")
    model_path = req.get("model_path", "")
    n_gpu = req.get("n_gpu_layers", state.n_gpu_layers)
    n_ctx = req.get("n_ctx", state.n_ctx)

    if not model_path:
        _send_error(req_id, "model_path is required for 'load' action")
        return True

    if not os.path.isfile(model_path):
        _send_error(req_id, f"Model file not found: {model_path}")
        return True

    try:
        from llama_cpp import Llama
    except ImportError as e:
        _send_error(req_id, f"llama_cpp not available in sidecar: {e}")
        return True

    with state.lock:
        _log(f"Loading model: {model_path} (n_gpu_layers={n_gpu}, n_ctx={n_ctx})")
        t0 = time.time()
        try:
            # Unload existing if any
            if state.model is not None:
                del state.model
                state.model = None

            state.model = Llama(
                model_path=model_path,
                n_gpu_layers=n_gpu,
                n_ctx=n_ctx,
                verbose=False,
            )
            state.model_path = model_path
            state.n_gpu_layers = n_gpu
            state.n_ctx = n_ctx
            state.loaded = True

            elapsed = time.time() - t0
            _log(f"Model loaded in {elapsed:.2f}s")
            _send_ok(
                req_id, {"loaded": True, "elapsed_sec": round(elapsed, 2), "model_path": model_path}
            )
        except Exception as e:
            state.loaded = False
            _send_error(req_id, f"Failed to load model: {e}")

    return True


def handle_infer(state: SidecarState, req: dict) -> bool:
    req_id = req.get("id", "?")
    prompt = req.get("prompt", "")
    max_tokens = req.get("max_tokens", 512)
    temperature = req.get("temperature", 0.1)
    stop = req.get("stop", [])
    top_p = req.get("top_p", 0.9)
    top_k = req.get("top_k", 40)

    if not state.loaded or state.model is None:
        _send_error(req_id, "No model loaded — send a 'load' request first")
        return True

    if not prompt:
        _send_error(req_id, "prompt is required for 'infer' action")
        return True

    _log(f"Inference: max_tokens={max_tokens} temp={temperature}")

    try:
        total_tokens = 0
        with state.lock:
            stream = state.model(
                prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                stop=stop if stop else None,
                stream=True,
                echo=False,
            )

            for chunk in stream:
                token_text = chunk["choices"][0]["text"]
                total_tokens += 1
                _send_token(req_id, token_text, done=False)

        _send_token(req_id, "", done=True, total_tokens=total_tokens)
        _log(f"Inference complete: {total_tokens} tokens")

    except Exception as e:
        _send_error(req_id, f"Inference error: {e}")

    return True


def handle_status(state: SidecarState, req: dict) -> bool:
    req_id = req.get("id", "?")
    _send_ok(req_id, state.status())
    return True


def handle_quit(state: SidecarState, req: dict) -> bool:
    req_id = req.get("id", "?")
    _send_ok(req_id, {"message": "Determinex sidecar shutting down."})
    _log("Quit requested — exiting.")
    return False  # Signal to stop the main loop


HANDLERS = {
    "load": handle_load,
    "infer": handle_infer,
    "status": handle_status,
    "quit": handle_quit,
}


# ---------------------------------------------------------------------------
# MAIN LOOP
# ---------------------------------------------------------------------------


def main():
    _log(f"Determinex sidecar started. Python {sys.version.split()[0]}")
    _log("Listening for NDJSON requests on stdin...")

    state = SidecarState()

    # Signal ready to Tauri (Rust side can wait for this line on stdout)
    _send({"event": "ready", "version": "1.0.0"})

    for raw_line in sys.stdin:
        raw_line = raw_line.strip()
        if not raw_line:
            continue

        try:
            req = json.loads(raw_line)
        except json.JSONDecodeError as e:
            _log(f"Invalid JSON received: {e}")
            _send({"id": "?", "ok": False, "error": f"Invalid JSON: {e}"})
            continue

        action = req.get("action", "").lower()
        req_id = req.get("id", "?")

        _log(f"Request: action={action} id={req_id}")

        handler = HANDLERS.get(action)
        if handler is None:
            _send_error(req_id, f"Unknown action: '{action}'. Valid: {list(HANDLERS)}")
            continue

        try:
            should_continue = handler(state, req)
        except Exception as e:
            _log(f"Handler exception: {e}")
            _send_error(req_id, f"Internal sidecar error: {e}")
            should_continue = True

        if not should_continue:
            break

    _log("Sidecar main loop exited.")


if __name__ == "__main__":
    main()
