#!/usr/bin/env python3
"""
determinex_calibrate.py — per-rig concurrency calibration for verified search
=============================================================================
Determinex's correctness knob is K: sample K candidates, verify each against a real
oracle, and `P = 1 - (1 - p)^K`. K is therefore not a performance setting -- it is the
rate at which correctness accrues. The right K is a property of the MACHINE, and until
now it was a constant (`k: int = 8`) or an env var, identical on every rig.

Measured, that constant is wrong in both directions:

  AMD Radeon Cloud, vLLM 0.16.1, Qwen2.5-Coder-7B (captured evidence):
      K=1  28.7 tok/s @ 8.92s      K=32 739.9 tok/s @ 10.75s
      K=48 849.7 tok/s @ 13.62s    K=64 512.6 tok/s @ 29.59s   <- collapse
  Consumer box, Ollama, Qwen2.5-Coder-1.5B (measured 2026-08-02, warm):
      K=1  17.6 tok/s @ 2.73s      K=6  53.3 tok/s @ 4.62s
      K=8  60.4 tok/s @ 5.66s

The default K=6 leaves ~5x of the Radeon's throughput unused, and is already past the
efficient region on the consumer box. One number cannot serve both.

WHY THIS MEASURES RATHER THAN READS A CONFIG
--------------------------------------------
The first version of this read the backend's declared capacity -- vLLM publishes
`vllm:cache_config_info{num_gpu_blocks, block_size}`, and 31504*16/8192 = 61, which does
predict the Radeon collapse at 64. That looked sufficient until the same approach was tried
on Ollama, where `OLLAMA_NUM_PARALLEL=1` predicted full serialisation and the machine
delivered 3.4x speedup at K=8 instead. The env var was read from the client shell, not from
the environment the server was launched with, and a client-side config value is not the
authority that enforces the limit.

So: declared capacity is a HINT that seeds the sweep. The measurement is the answer.

OBJECTIVE: CANDIDATES PER SECOND
--------------------------------
Aggregate tok/s alone would pick a K that is still "gaining" while wall clock doubles --
useless for verified search, which needs K candidates *and* needs them soon. `K / wall_s` is
the rate at which independent attempts arrive, which is exactly what drives P upward. It
also finds the collapse for free: past the backend's real limit, requests preempt instead of
batching, wall clock explodes, and the ratio falls.

Applied to the captured Radeon numbers this picks K=48 (3.52 cand/s vs 2.98 at K=32 and
2.16 at K=64) -- i.e. it independently reproduces the knee that was found by hand.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import platform
import statistics
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable

_ROOT = Path(__file__).resolve().parent.parent

# Per-rig, NOT in the repo: a calibration is a fact about one machine and must never be
# committed or published as if it were a property of Determinex.
PROFILE_PATH = Path(
    os.environ.get("DETERMINEX_CALIBRATION")
    or (Path.home() / ".determinex" / "calibration.json")
)

# Conservative fallback when nothing is calibrated. Deliberately small: an uncalibrated rig
# should under-use the hardware, never fall off a cliff it has not measured.
UNCALIBRATED_K = 4

_PROBE_PROMPT = "Write a Rust function that returns the sum of a slice of i32. Code only."


@dataclass
class KPoint:
    k: int
    wall_s: float
    tokens: int
    agg_tok_s: float
    cand_per_s: float


@dataclass
class Calibration:
    backend: str
    model: str
    host: str
    optimal_k: int
    cand_per_s: float
    collapsed_at: int | None
    declared_hint: int | None
    points: list[dict]
    measured_at: str

    def summary(self) -> str:
        c = f", collapse at K={self.collapsed_at}" if self.collapsed_at else ""
        return (
            f"{self.backend}/{self.model} on {self.host}: optimal K={self.optimal_k} "
            f"({self.cand_per_s:.2f} candidates/s{c})"
        )


def host_fingerprint() -> str:
    """Coarse, non-identifying machine key. No usernames, no paths -- this file may be
    shared when a user opts into corpus sharing, so it carries no personal data."""
    return f"{platform.system()}-{platform.machine()}-{os.cpu_count()}cpu"


# ── declared-capacity hints (a starting point for the sweep, never the answer) ──────────


def _vllm_declared_k(base_url: str, max_model_len: int = 8192) -> int | None:
    """floor(KV cache tokens / max_model_len), read from vLLM's own /metrics.

    This is the number that correctly predicted the Radeon collapse (31504 blocks * 16
    tokens / 8192 = 61, and K=64 broke). It is used to bound the sweep so calibration does
    not spend minutes discovering a cliff the server already declared.
    """
    import re
    import urllib.request

    try:
        url = base_url.rstrip("/")
        for suffix in ("/v1", "/v1/"):
            if url.endswith(suffix):
                url = url[: -len(suffix)]
        with urllib.request.urlopen(url + "/metrics", timeout=6) as r:
            body = r.read().decode("utf-8", "replace")
    except Exception:
        return None
    m = re.search(r'vllm:cache_config_info\{([^}]*)\}', body)
    if not m:
        return None
    fields = dict(re.findall(r'(\w+)="([^"]*)"', m.group(1)))
    try:
        blocks = int(fields["num_gpu_blocks"])
        block_size = int(fields["block_size"])
    except (KeyError, ValueError):
        return None
    if max_model_len <= 0:
        return None
    return max(1, (blocks * block_size) // max_model_len)


# ── the sweep ───────────────────────────────────────────────────────────────────────────


def sweep(
    generate: Callable[[], int],
    ks: list[int],
    repeats: int = 3,
    warmup: int = 2,
) -> list[KPoint]:
    """Measure candidates/second at each K. Warms first, medians over `repeats`.

    The warm-up is not politeness: without it K=1 pays the model load and reports ~7 tok/s
    for a 1.5B model, which made the first run of this probe produce a conclusion that was
    simply wrong.
    """
    for _ in range(max(0, warmup)):
        generate()

    out: list[KPoint] = []
    for k in ks:
        walls, toks = [], []
        for _ in range(repeats):
            t0 = time.time()
            with cf.ThreadPoolExecutor(max_workers=k) as ex:
                got = sum(ex.map(lambda _i: generate(), range(k)))
            walls.append(time.time() - t0)
            toks.append(got)
        w = statistics.median(walls)
        t = int(statistics.median(toks))
        out.append(KPoint(k, round(w, 3), t, round(t / w, 1) if w else 0.0,
                          round(k / w, 3) if w else 0.0))
    return out


def pick_optimal(points: list[KPoint], tolerance: float = 0.97) -> tuple[int, int | None]:
    """(optimal_k, collapsed_at) by candidates/second.

    `collapsed_at` is the first K whose candidate rate fell below `tolerance` of the best
    seen so far -- the signature of a backend that started preempting instead of batching.
    Reported separately from the optimum because it is the interesting number: it is where
    the hardware says stop, and a rig that never collapses within the swept range simply
    has not been pushed far enough.
    """
    if not points:
        return UNCALIBRATED_K, None
    best = max(points, key=lambda p: p.cand_per_s)
    collapsed = None
    peak = 0.0
    for p in points:
        if p.cand_per_s > peak:
            peak = p.cand_per_s
        elif peak and p.cand_per_s < peak * tolerance:
            collapsed = p.k
            break
    return best.k, collapsed


# ── profile I/O ─────────────────────────────────────────────────────────────────────────


def load_profile() -> dict:
    if not PROFILE_PATH.is_file():
        return {}
    try:
        return json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def save_calibration(cal: Calibration) -> None:
    prof = load_profile()
    prof[f"{cal.backend}::{cal.model}::{cal.host}"] = asdict(cal)
    PROFILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    PROFILE_PATH.write_text(json.dumps(prof, indent=2) + "\n", encoding="utf-8")


def optimal_k(backend: str, model: str, default: int = UNCALIBRATED_K) -> tuple[int, str]:
    """(K, provenance). Never silently guesses.

    Mirrors the doctrine `determinex_oracle` already enforces -- a stub raises rather than
    quietly passing. Here an uncalibrated rig gets a conservative K and a string saying so,
    which the caller is expected to LOG, so a run at the fallback K is never mistaken for a
    run at a measured one.
    """
    key = f"{backend}::{model}::{host_fingerprint()}"
    entry = load_profile().get(key)
    if entry and entry.get("optimal_k"):
        return int(entry["optimal_k"]), f"calibrated {entry.get('measured_at', '?')}"
    return default, (
        f"UNCALIBRATED (no profile for {key}); using conservative K={default}. "
        f"Run: python scripts/determinex_calibrate.py --backend {backend} --model {model}"
    )


# ── CLI ─────────────────────────────────────────────────────────────────────────────────


def _ollama_generator(model: str, base_url: str, num_predict: int) -> Callable[[], int]:
    import urllib.request

    def gen() -> int:
        body = json.dumps({
            "model": model, "prompt": _PROBE_PROMPT, "stream": False,
            "options": {"num_predict": num_predict, "temperature": 0.4, "num_ctx": 4096},
        }).encode()
        req = urllib.request.Request(
            base_url.rstrip("/") + "/api/generate",
            data=body, headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=300) as r:
            return int(json.loads(r.read()).get("eval_count", 0))

    return gen


def _openai_generator(model: str, base_url: str, num_predict: int) -> Callable[[], int]:
    import urllib.request

    def gen() -> int:
        body = json.dumps({
            "model": model,
            "messages": [{"role": "user", "content": _PROBE_PROMPT}],
            "max_tokens": num_predict, "temperature": 0.4,
        }).encode()
        req = urllib.request.Request(
            base_url.rstrip("/") + "/chat/completions",
            data=body,
            headers={"Content-Type": "application/json",
                     "Authorization": "Bearer " + os.environ.get("OPENAI_API_KEY", "none")},
        )
        with urllib.request.urlopen(req, timeout=300) as r:
            d = json.loads(r.read())
        return int((d.get("usage") or {}).get("completion_tokens", 0))

    return gen


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--backend", choices=["ollama", "vllm", "openai"], default="ollama")
    ap.add_argument("--model", default="qwen2.5-coder:1.5b-instruct")
    ap.add_argument("--base-url", default=None)
    ap.add_argument("--ks", default=None, help="comma list, e.g. 1,2,4,8,16")
    ap.add_argument("--max-model-len", type=int, default=8192)
    ap.add_argument("--num-predict", type=int, default=48)
    ap.add_argument("--repeats", type=int, default=3)
    ap.add_argument("--show", action="store_true", help="print the stored profile and exit")
    args = ap.parse_args()

    if args.show:
        prof = load_profile()
        if not prof:
            print(f"no calibration profile at {PROFILE_PATH}")
            return 0
        print(f"{PROFILE_PATH}:")
        for k, v in prof.items():
            print(f"  {k}")
            print(f"      optimal K={v['optimal_k']}  ({v['cand_per_s']} cand/s)"
                  f"  collapse={v.get('collapsed_at')}  measured {v.get('measured_at')}")
        return 0

    base = args.base_url or (
        "http://localhost:11434" if args.backend == "ollama" else "http://localhost:8000/v1"
    )

    hint = None
    if args.backend == "vllm":
        hint = _vllm_declared_k(base, args.max_model_len)
        if hint:
            print(f"  backend declares capacity for ~{hint} concurrent requests "
                  f"(a hint that bounds the sweep; the measurement decides)")

    if args.ks:
        ks = [int(x) for x in args.ks.split(",") if x.strip()]
    else:
        ks = [1, 2, 4, 8, 16, 32, 48, 64]
        if hint:
            ks = [k for k in ks if k <= hint * 1.2] or [1, 2, 4]
        elif args.backend == "ollama":
            ks = [1, 2, 4, 6, 8, 12]

    gen = (_ollama_generator if args.backend == "ollama" else _openai_generator)(
        args.model, base, args.num_predict
    )

    print(f"  calibrating {args.backend}/{args.model} on {host_fingerprint()}")
    print(f"  sweeping K={ks}, {args.repeats} repeats, warm-up first\n")
    print(f"  {'K':<5}{'wall_s':<10}{'tokens':<9}{'agg tok/s':<12}{'cand/s':<9}")
    pts = sweep(gen, ks, repeats=args.repeats)
    for p in pts:
        print(f"  {p.k:<5}{p.wall_s:<10}{p.tokens:<9}{p.agg_tok_s:<12}{p.cand_per_s:<9}")

    best, collapsed = pick_optimal(pts)
    cal = Calibration(
        backend=args.backend, model=args.model, host=host_fingerprint(),
        optimal_k=best,
        cand_per_s=max(p.cand_per_s for p in pts),
        collapsed_at=collapsed, declared_hint=hint,
        points=[asdict(p) for p in pts],
        measured_at=time.strftime("%Y-%m-%dT%H:%M:%S"),
    )
    save_calibration(cal)
    print(f"\n  {cal.summary()}")
    if collapsed:
        print(f"  throughput fell past K={collapsed} -- the hardware's real ceiling.")
    else:
        print(f"  no collapse within K<={max(ks)}; this rig has more headroom than the sweep used.")
    print(f"  written to {PROFILE_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
