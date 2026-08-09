"""scripts/corpus/corpus_feedback.py — does the corpus earn its place, and what is it missing?

TWO QUESTIONS THE CORPUS COULD NOT ANSWER ABOUT ITSELF.

1. WHAT DID IT FAIL TO ANSWER? `ask()` returns hits and forgets. A query that came back empty or
   weak is the single highest-value signal for what to absorb next -- it is the corpus telling
   you precisely where its edge is -- and it was thrown away every time. `note_gap()` records it.

2. DID GROUNDING HELP? Compacted packets are now injected into every builder prompt, and matched
   fixes into every retry, on the argument that they should help. That is an assumption, not a
   measurement, and this project has spent months finding claims of exactly that shape inside its
   own documents. `effect()` measures it.

WHY THERE IS NO NEW WRITE PATH FOR (2). The WAL already stores each attempt's full system_prompt
alongside its outcome. The injected knowledge is therefore already on disk, next to the result it
produced -- so the honest measurement is a READ over data that exists, not new instrumentation.
Adding a parallel telemetry write would have created a second source of truth that can disagree
with the WAL, to measure something the WAL already recorded.

HONESTY GATE. A difference measured over a handful of attempts is noise, and "grounded prompts
pass 8% more often" from n=12 is the kind of number that ends up in a README and never leaves.
`effect()` reports a Wilson confidence interval and refuses to call a winner when the intervals
overlap. No result is a result.

    python scripts/corpus/corpus_feedback.py gaps       # what the corpus could not answer
    python scripts/corpus/corpus_feedback.py effect     # did grounding change outcomes
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

#: Local only, and deliberately not under corpus/. These are the operator's own queries -- what
#: they were stuck on and when -- which is more revealing than anything in the corpus proper.
#: Keeping it out of the published tree means it cannot be swept into a dataset export by a
#: future glob that was written without this file in mind.
GAP_LOG = REPO_ROOT / ".determinex" / "corpus_gaps.jsonl"

#: The markers the prompt builder writes when it grounds a prompt. Matching on the prompt text
#: rather than a flag means the measurement reads what the model ACTUALLY received -- a flag can
#: be set on a path where the injection later failed, and then the flag measures our intent
#: instead of the model's input.
GROUNDING_MARKERS = {
    "packets": "KNOWN FAILURE CLASSES",
    "matched_fix": "WE HAVE SEEN THIS BEFORE",
}

#: Below this many attempts in either arm, no comparison is reported at all. Chosen so a single
#: unlucky session cannot manufacture a headline.
MIN_ARM = 20


# ── 1. what the corpus could not answer ──────────────────────────────────────


def note_gap(query: str, n_hits: int, source: str = "ask", top_score: float = 0.0) -> None:
    """Record a query the corpus answered poorly. Best-effort and silent on failure.

    Called from the query path, so it must never be able to break a query. A telemetry write that
    can raise turns 'the corpus was unhelpful' into 'the corpus crashed', which is strictly worse.
    """
    try:
        GAP_LOG.parent.mkdir(parents=True, exist_ok=True)
        line = json.dumps(
            {
                "ts": time.time(),
                "query": query[:300],
                "n_hits": n_hits,
                "top_score": top_score,
                "source": source,
            }
        )
        fd = os.open(str(GAP_LOG), os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
        try:
            os.write(fd, (line + "\n").encode("utf-8", errors="replace"))
        finally:
            os.close(fd)
    except Exception:
        pass


def gaps(limit: int = 20) -> list[dict[str, Any]]:
    """The questions asked most often that the corpus answered worst.

    Ranked by frequency, because a gap hit once is curiosity and a gap hit nine times is a hole in
    the corpus with a queue of people falling into it.
    """
    try:
        raw = GAP_LOG.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []
    seen: Counter[str] = Counter()
    latest: dict[str, dict] = {}
    for line in raw:
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        # Normalised so "how do I fix X" and "How do I fix X?" are one gap, not two.
        key = " ".join(str(rec.get("query", "")).lower().split())
        if not key:
            continue
        seen[key] += 1
        latest[key] = rec
    return [
        {
            "query": q,
            "times_asked": n,
            "last": latest[q].get("ts"),
            "n_hits": latest[q].get("n_hits"),
        }
        for q, n in seen.most_common(limit)
    ]


# ── 2. did grounding change anything ─────────────────────────────────────────


def _wilson(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score interval. Used rather than a bare proportion because the whole point is to
    know whether a difference is real, and a bare 0.62 carries no information about how hard it
    would be to get 0.62 by luck."""
    if total == 0:
        return (0.0, 1.0)
    p = successes / total
    d = 1 + z * z / total
    centre = (p + z * z / (2 * total)) / d
    half = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / d
    return (max(0.0, centre - half), min(1.0, centre + half))


def _wal_records(wal_root: Path | None = None) -> list[dict]:
    root = wal_root or (REPO_ROOT / "logs" / "wal")
    out: list[dict] = []
    if not root.exists():
        return out
    for p in root.rglob("*.jsonl"):
        try:
            for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        except OSError:
            continue
    return out


def effect(wal_root: Path | None = None) -> dict[str, Any]:
    """Compare outcomes for attempts whose prompt carried corpus knowledge against those without.

    Observational, not an experiment, and the difference between those matters here. Grounding is
    not randomly assigned: a matched fix appears precisely when an error resembles one we have
    already solved, which is not a random subset of errors. So a positive result is evidence
    worth acting on and never proof of causation, and this says so rather than leaving a reader
    to assume otherwise.
    """
    records = _wal_records(wal_root)
    arms: dict[str, dict[str, int]] = {
        name: {"n": 0, "ok": 0} for name in (*GROUNDING_MARKERS, "none")
    }
    for rec in records:
        prompt = str(rec.get("system_prompt") or "")
        outcome = rec.get("outcome") or {}
        if not isinstance(outcome, dict) or "compile_ok" not in outcome:
            continue
        ok = bool(outcome.get("compile_ok"))
        hit = False
        for name, marker in GROUNDING_MARKERS.items():
            if marker in prompt:
                arms[name]["n"] += 1
                arms[name]["ok"] += ok
                hit = True
        if not hit:
            arms["none"]["n"] += 1
            arms["none"]["ok"] += ok

    report: dict[str, Any] = {"records_scanned": len(records), "arms": {}}
    for name, a in arms.items():
        lo, hi = _wilson(a["ok"], a["n"])
        report["arms"][name] = {
            "attempts": a["n"],
            "compiled": a["ok"],
            "rate": round(a["ok"] / a["n"], 3) if a["n"] else None,
            "ci95": [round(lo, 3), round(hi, 3)],
        }

    base = arms["none"]
    verdict = "insufficient data"
    for name in GROUNDING_MARKERS:
        arm = arms[name]
        if arm["n"] < MIN_ARM or base["n"] < MIN_ARM:
            continue
        a_lo, _ = _wilson(arm["ok"], arm["n"])
        _, b_hi = _wilson(base["ok"], base["n"])
        verdict = (
            f"{name} grounding is ahead (CIs do not overlap)"
            if a_lo > b_hi
            else f"{name}: no separable difference yet"
        )
    report["verdict"] = verdict
    report["caveat"] = (
        "Observational. Grounding is not randomly assigned -- a matched fix appears exactly when "
        "an error resembles one already solved -- so this is evidence, never proof of causation."
    )
    report["min_arm"] = MIN_ARM
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("mode", choices=("gaps", "effect"))
    ap.add_argument("--limit", type=int, default=20)
    args = ap.parse_args()

    reconf = getattr(sys.stdout, "reconfigure", None)
    if reconf is not None:
        reconf(encoding="utf-8")

    if args.mode == "gaps":
        rows = gaps(args.limit)
        if not rows:
            print("  no recorded gaps yet -- nothing has queried the corpus and come away empty.")
            return 0
        print(f"  {len(rows)} distinct question(s) the corpus answered poorly:\n")
        for r in rows:
            print(f"   {r['times_asked']:>3}x  (hits={r['n_hits']})  {r['query'][:88]}")
        return 0

    rep = effect()
    print(f"  WAL records scanned: {rep['records_scanned']}")
    for name, a in rep["arms"].items():
        rate = "--" if a["rate"] is None else f"{a['rate']:.1%}"
        print(
            f"   {name:12} n={a['attempts']:>5}  compiled={rate:>7}  "
            f"95% CI [{a['ci95'][0]:.2f}, {a['ci95'][1]:.2f}]"
        )
    print(f"\n  verdict: {rep['verdict']}  (needs n>={rep['min_arm']} per arm)")
    print(f"  {rep['caveat']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
