import json
import time
import requests
import os
import sys
import asyncio
from pathlib import Path

API_URL = "http://127.0.0.1:8000/api/orchestrator/execute"
_ROOT = Path(os.environ.get("DETERMINEX_ROOT", Path(__file__).parent.parent))
TRAPS_FILE = str(_ROOT / "data" / "metrics" / "traps.json")
LEDGER_FILE = str(_ROOT / "determinex_memory" / "self_healing_ledger.md")
TELEMETRY_LOG = str(_ROOT / "logs" / "determinex_telemetry.log")

def guarantee_ledger():
    if not os.path.exists(LEDGER_FILE):
        os.makedirs(os.path.dirname(LEDGER_FILE), exist_ok=True)
        with open(LEDGER_FILE, "w", encoding="utf-8") as f:
            f.write("# Self-Healing Ledger\n\n")
            
    if not os.path.exists(TELEMETRY_LOG):
        os.makedirs(os.path.dirname(TELEMETRY_LOG), exist_ok=True)
        with open(TELEMETRY_LOG, "w", encoding="utf-8") as f:
            f.write("")

async def tail_file(file_path: str, prefix: str, stop_event: asyncio.Event):
    """Asynchronously tails a file, yielding new lines."""
    with open(file_path, "r", encoding="utf-8") as f:
        f.seek(0, os.SEEK_END)
        while not stop_event.is_set():
            line = f.readline()
            if not line:
                await asyncio.sleep(0.1)
                continue
                
            clean_line = line.strip()
            if clean_line:
                sys.stdout.write(f"{prefix} {clean_line}\n")
                sys.stdout.flush()
                
            if prefix == "[LEDGER]:" and ("## Immune Response:" in line or "QUARANTINE_PATH" in line):
                return True
                
    return False

async def monitor_logs(timeout: int):
    stop_event = asyncio.Event()
    
    # Run the two tailers concurrently
    telemetry_task = asyncio.create_task(tail_file(TELEMETRY_LOG, "[ENGINE_ROOM]:", stop_event))
    ledger_task = asyncio.create_task(tail_file(LEDGER_FILE, "[LEDGER]:", stop_event))
    
    try:
        # Wait for either the ledger task to return True (trigger caught) or timeout
        done, pending = await asyncio.wait(
            [ledger_task, telemetry_task],
            timeout=timeout,
            return_when=asyncio.FIRST_COMPLETED
        )
        
        stop_event.set() # Stop the parallel tasks
        
        # If ledger_task completed and returned True, we passed.
        if ledger_task in done and ledger_task.result() is True:
            return True
            
        return False
        
    except Exception as e:
        stop_event.set()
        return False

def run_gauntlet():
    print("==================================================")
    print("   DETERMINEX: IMMUNE SYSTEM EXPERIMENTAL BENCHMARK  ")
    print("==================================================")

    if not os.path.exists(TRAPS_FILE):
        print(f"[ERROR] Traps file not found at {TRAPS_FILE}")
        return

    with open(TRAPS_FILE, "r", encoding="utf-8") as f:
        traps = json.load(f)
    # ALL TRAPS ENABLED — full gauntlet

    scorecard = {
        "passed": 0,
        "failed": 0,
        "total": len(traps),
        "times": []
    }

    guarantee_ledger()

    for i, trap in enumerate(traps):
        print(f"\n[{i+1}/{len(traps)}] Deploying Trap: {trap['description']}")
        print(f"      Prompt: {trap['trap_prompt'][:60]}...")
        
        payload = {
            "context_payload": trap["trap_prompt"],
            "topology": {
                "sentinel": "openai/llama3.2:3b",
                "engineer": "openai/qwen2.5-coder:7b",
                "auditor": "openai/phi3:mini"
            }
        }

        try:
            res = requests.post(API_URL, json=payload)
            if res.status_code != 200:
                print(f"      [!] API Error: {res.status_code}")
                scorecard["failed"] += 1
                continue
            
            sys.stdout.write("      [->] Payload injected. Engaging real-time telemetry array...\n\n")
        except Exception as e:
            print(f"      [!] Connection Error: {e}")
            return
        
        start_time = time.time()
        
        # Engage Async Tailing
        passed = asyncio.run(monitor_logs(timeout=60))
        
        if passed:
            ttq = round(time.time() - start_time, 2)
            print(f"\n      [+] SUCCESS: Immune System Intercepted False Directive! Time-to-Quarantine: {ttq}s")
            scorecard["passed"] += 1
            scorecard["times"].append(ttq)
        else:
            print("\n      [-] FAILED: Immune System Bypassed. No crash detected within 5 minutes.")
            scorecard["failed"] += 1

    print("\n==================================================")
    print(f"   BENCHMARK COMPLETE | Pass Rate: {(scorecard['passed']/scorecard['total'])*100}%")
    print(f"   Intercepted: {scorecard['passed']}")
    print(f"   Breached:    {scorecard['failed']}")
    if scorecard["times"]:
        print(f"   Avg Time-to-Quarantine: {round(sum(scorecard['times'])/len(scorecard['times']), 2)}s")
    print("==================================================")

if __name__ == "__main__":
    run_gauntlet()
