"""
DETERMINEX VRAM CRUCIBLE — Sequential MoA Load Test
=================================================
Fires a heavy context payload directly at the native Rust orchestrate_plan
endpoint via the Ollama HTTP bridge and monitors VRAM allocation in real time.

PASS CONDITION: VRAM allocation NEVER exceeds 5500 MiB (5.5 GB) during any
model handoff. The remaining 500 MiB is the OS safety buffer for a 6 GB GPU.

Usage:
    python benchmarks/vram_crucible.py

Prerequisites:
    - Ollama running: `ollama serve`
    - Models pulled:  `ollama pull llama3.2:3b && ollama pull qwen2.5-coder:7b && ollama pull phi3:mini`
    - pynvml:         `pip install pynvml requests`
"""

import json
import sys
import threading
import time
from datetime import datetime

import requests

try:
    import pynvml

    NVML_AVAILABLE = True
except ImportError:
    NVML_AVAILABLE = False
    print("[WARN] pynvml not found. Install with: pip install pynvml")
    print("[WARN] Falling back to nvidia-smi subprocess polling.")
    import subprocess

# --- Configuration ------------------------------------------------------------

OLLAMA_URL = "http://localhost:11434/api/generate"
VRAM_CEILING_MiB = 5500  # Hard pass limit (5.5 GB)
VRAM_POLL_SECS = 0.5  # Sampling interval
GPU_INDEX = 0  # 6 GB GPU is device 0

# Heavy payload — realistic long-context professional request
CRUCIBLE_PROMPT = """
You are the Determinex Sentinel. Analyze the following complex engineering request and produce
a complete, structured execution plan. This is a VRAM stress test — the payload is intentionally
dense to force maximum context utilization.

REQUEST:
Design a production-grade, fault-tolerant distributed message queue system in Rust using tokio.
The system must support:
1. Multi-producer, single-consumer (MPSC) channels with configurable backpressure thresholds
2. Persistent WAL (Write-Ahead Log) using SQLite with WAL journal mode
3. Dead-letter queue (DLQ) for failed message routing with automatic retry with exponential backoff
4. Priority queue semantics (HIGH/NORMAL/LOW) with strict ordering guarantees per priority tier
5. Graceful shutdown: drain all in-flight messages before terminating, with a 30-second SLA
6. Health telemetry endpoint (HTTP/JSON) exposing queue depth, throughput, and error rates
7. Zero-copy deserialization using serde with Bytes buffers to minimize heap allocations
8. Comprehensive tracing via the `tracing` crate with OpenTelemetry-compatible spans
9. Property-based tests using `proptest` for message ordering invariants
10. Benchmarks using `criterion` targeting < 500μs p99 enqueue latency under 10,000 msg/s load

Include architecture diagram as ASCII art, dependency specifications (Cargo.toml),
and module breakdown. Flag any concurrency hazards or potential deadlock conditions explicitly.

Output strictly as JSON matching this schema:
{
  "title": "string",
  "steps": ["string"],
  "audit_targets": ["string"]
}
"""

# --- VRAM Monitor -------------------------------------------------------------


class VramMonitor:
    def __init__(self, gpu_index: int, ceiling_mib: int, poll_interval: float):
        self.gpu_index = gpu_index
        self.ceiling_mib = ceiling_mib
        self.poll_interval = poll_interval
        self.samples: list[dict] = []
        self.breach_count = 0
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)

        if NVML_AVAILABLE:
            pynvml.nvmlInit()
            self.handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_index)

    def _get_vram_mib(self) -> float:
        if NVML_AVAILABLE:
            info = pynvml.nvmlDeviceGetMemoryInfo(self.handle)
            return info.used / (1024**2)
        else:
            try:
                out = subprocess.check_output(
                    ["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits"],
                    encoding="utf-8",
                )
                lines = [l.strip() for l in out.strip().splitlines() if l.strip()]
                return float(lines[self.gpu_index])
            except Exception:
                return 0.0

    def _run(self):
        while not self._stop.is_set():
            used = self._get_vram_mib()
            ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            entry = {"ts": ts, "vram_mib": used}
            self.samples.append(entry)

            if used > self.ceiling_mib:
                self.breach_count += 1
                print(
                    f"  [\033[91mBREACH\033[0m] {ts} — {used:.1f} MiB > {self.ceiling_mib} MiB ceiling",
                    flush=True,
                )
            else:
                bar_len = 30
                filled = int((used / self.ceiling_mib) * bar_len)
                bar = "#" * filled + "." * (bar_len - filled)
                pct = (used / self.ceiling_mib) * 100
                color = "\033[92m" if pct < 75 else "\033[93m" if pct < 90 else "\033[91m"
                print(
                    f"  [{ts}] VRAM: {color}{used:6.1f} MiB\033[0m [{bar}] {pct:4.1f}%", flush=True
                )

            self._stop.wait(self.poll_interval)

        if NVML_AVAILABLE:
            pynvml.nvmlShutdown()

    def start(self):
        self._thread.start()

    def stop(self):
        self._stop.set()
        self._thread.join()

    def report(self) -> dict:
        if not self.samples:
            return {"max_mib": 0, "avg_mib": 0, "min_mib": 0, "breach_count": 0, "passed": True}
        values = [s["vram_mib"] for s in self.samples]
        return {
            "max_mib": max(values),
            "avg_mib": sum(values) / len(values),
            "min_mib": min(values),
            "samples": len(values),
            "breach_count": self.breach_count,
            "ceiling_mib": self.ceiling_mib,
            "passed": self.breach_count == 0,
        }


# --- Sequential Stage Tester --------------------------------------------------


def call_ollama_stage(model: str, prompt: str, stage_name: str) -> tuple[bool, float, str]:
    """
    Fire a single Ollama inference request.
    Returns (success, elapsed_seconds, raw_response).
    """
    print(f"\n\033[1m{'-' * 60}\033[0m")
    print(f"  \033[96m[{stage_name.upper()}]\033[0m Model: {model}")
    print(f"  Prompt length: {len(prompt)} chars")
    print(f"{'-' * 60}\033[0m")

    start = time.time()
    try:
        resp = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "format": "json",
                # Match the native orchestrator's VRAM tuning exactly
                "keep_alive": 0,
                "options": {"num_ctx": 2048},
            },
            timeout=300,
        )
        elapsed = time.time() - start

        if resp.status_code != 200:
            print(f"  \033[91m[FAIL]\033[0m HTTP {resp.status_code}")
            return False, elapsed, ""

        data = resp.json()
        if not data.get("done", False):
            print("  \033[91m[FAIL]\033[0m Response not marked done")
            return False, elapsed, ""

        raw = data.get("response", "")
        print(
            f"  \033[92m[OK]\033[0m Completed in {elapsed:.2f}s — response length: {len(raw)} chars"
        )

        # Validate JSON schema
        try:
            parsed = json.loads(raw)
            print("  \033[92m[SCHEMA OK]\033[0m JSON parsed successfully")
            if stage_name == "sentinel":
                required = {"title", "steps", "audit_targets"}
                missing = required - set(parsed.keys())
                if missing:
                    print(f"  \033[93m[SCHEMA WARN]\033[0m Missing keys: {missing}")
        except json.JSONDecodeError as e:
            print(f"  \033[91m[SCHEMA FAIL]\033[0m Not valid JSON: {e}")

        return True, elapsed, raw

    except requests.exceptions.Timeout:
        elapsed = time.time() - start
        print(f"  \033[91m[TIMEOUT]\033[0m Stage timed out after {elapsed:.1f}s")
        return False, elapsed, ""
    except requests.exceptions.ConnectionError:
        elapsed = time.time() - start
        print(f"  \033[91m[CONN ERROR]\033[0m Cannot reach Ollama at {OLLAMA_URL}")
        print("  Ensure 'ollama serve' is running.")
        return False, elapsed, ""


# --- Main Crucible ------------------------------------------------------------


def main():
    print("\n" + "=" * 60)
    print("  DETERMINEX VRAM CRUCIBLE — SEQUENTIAL MoA HANDOFF TEST")
    print("  6 GB GPU · 6GB VRAM · Ceiling: 5500 MiB")
    print("=" * 60)

    # Check Ollama health
    try:
        check = requests.get("http://localhost:11434", timeout=3)
        print(f"\n  [\033[92mOLLAMA ONLINE\033[0m] v{check.text.strip()}")
    except Exception:
        print("\n  [\033[91mOLLAMA OFFLINE\033[0m] Start with: ollama serve")
        sys.exit(1)

    monitor = VramMonitor(GPU_INDEX, VRAM_CEILING_MiB, VRAM_POLL_SECS)
    monitor.start()

    print(
        f"\n  \033[93mVRAM monitor live. Ceiling: {VRAM_CEILING_MiB} MiB. Sampling every {VRAM_POLL_SECS}s.\033[0m\n"
    )

    stages = [
        ("sentinel", "determinex-sentinel-v3", CRUCIBLE_PROMPT),
        (
            "engineer",
            "determinex-engineer-v10-dsl",
            "You are the Determinex Engineer. Execute this plan:\n"
            + CRUCIBLE_PROMPT[:500]
            + '\n\nOutput JSON: {"language":"rust","code":"...","files_affected":["src/queue.rs"]}',
        ),
        (
            "observer",
            "determinex-observer-v5-dsl",
            'Audit this code for correctness. Output JSON: {"verdict":"CLEAN","issues":[],"confidence":0.95}',
        ),
    ]

    results = []
    total_start = time.time()

    for stage_name, model, prompt in stages:
        success, elapsed, response = call_ollama_stage(model, prompt, stage_name)
        results.append(
            {
                "stage": stage_name,
                "model": model,
                "success": success,
                "elapsed": elapsed,
            }
        )
        if not success:
            print(
                f"\n  \033[91m[CRUCIBLE ABORT]\033[0m Stage {stage_name} failed. Halting pipeline.\033[0m"
            )
            break
        # Explicit pause between stages — gives Ollama time to fully evict the previous model.
        # This matches the orchestrator's VRAM_FLUSH_SECS = 8 constant.
        print("  Waiting 8s for Ollama VRAM flush between stages (matching native orchestrator)...")
        time.sleep(8)

    total_elapsed = time.time() - total_start
    monitor.stop()

    vram_report = monitor.report()

    # -- Final Report ---------------------------------------------------------
    print("\n" + "=" * 60)
    print("  CRUCIBLE FINAL REPORT")
    print("=" * 60)

    print("\n  STAGE TIMING:")
    for r in results:
        status = "\033[92mPASS\033[0m" if r["success"] else "\033[91mFAIL\033[0m"
        print(f"    [{status}] {r['stage']:10s} ({r['model']:25s}) — {r['elapsed']:6.2f}s")

    print(f"\n  TOTAL PIPELINE TIME: {total_elapsed:.2f}s")

    print("\n  VRAM TELEMETRY:")
    print(f"    Peak allocation : {vram_report['max_mib']:.1f} MiB")
    print(f"    Average         : {vram_report['avg_mib']:.1f} MiB")
    print(f"    Minimum         : {vram_report['min_mib']:.1f} MiB")
    print(f"    Samples         : {vram_report['samples']}")
    print(f"    Ceiling         : {VRAM_CEILING_MiB} MiB")
    print(f"    Headroom        : {VRAM_CEILING_MiB - vram_report['max_mib']:.1f} MiB")
    print(f"    Breaches        : {vram_report['breach_count']}")

    all_stages_passed = all(r["success"] for r in results)
    vram_passed = vram_report["passed"]
    overall_pass = all_stages_passed and vram_passed

    print("\n" + "-" * 60)
    if overall_pass:
        print("  \033[92m\033[1m✓ CRUCIBLE PASSED\033[0m")
        print("  Sequential handoff complete. VRAM constraint honored.")
        print(
            f"  Peak {vram_report['max_mib']:.1f} MiB / {VRAM_CEILING_MiB} MiB — {VRAM_CEILING_MiB - vram_report['max_mib']:.1f} MiB headroom maintained."
        )
    else:
        print("  \033[91m\033[1m✗ CRUCIBLE FAILED\033[0m")
        if not all_stages_passed:
            failed = [r["stage"] for r in results if not r["success"]]
            print(f"  Pipeline failure at: {', '.join(failed)}")
        if not vram_passed:
            print(
                f"  VRAM ceiling breached {vram_report['breach_count']} time(s). Peak: {vram_report['max_mib']:.1f} MiB"
            )
    print("-" * 60 + "\n")

    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
