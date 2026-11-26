#!/usr/bin/env python3
"""pb_slop_retriage.py -- run the AUTOMATED reference-fail slop detector across the whole PB tail.

For every per_tool_overrides tool with failures: pre-filter to those whose tracebacks expose a
recoverable invocation (args= / Command '[...]'), then build a clean reference + run each failing
test's invocation against it (determinex_test_validator.auto_reference_check). SLOP only when a correct
binary fails too; a non-functional/unbuildable reference DEFERS (never false slop). Writes a per-tool
tally + a grand total. Runs where the source + toolchains are (the box).

    python3 scripts/pb_slop_retriage.py [--log /root/slop_tail.log]
"""

from __future__ import annotations

import glob
import json
import os
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import determinex_test_validator as V  # noqa: E402

BASE = "corpus/programbench/per_tool_overrides"


def _txt(x: dict) -> str:
    e = x.get("extra") or {}
    return e.get("text", "") if isinstance(e, dict) else ""


def main() -> int:
    log_path = "/root/slop_tail.log"
    if "--log" in sys.argv:
        log_path = sys.argv[sys.argv.index("--log") + 1]
    out = open(log_path, "w", encoding="utf-8")

    def log(s: str) -> None:
        out.write(s + "\n")
        out.flush()
        print(s, flush=True)

    dirs = sorted(
        d
        for d in glob.glob(BASE + "/*")
        if os.path.isdir(d) and os.path.exists(d + "/eval_report.json")
    )
    log(f"=== SLOP RE-TRIAGE (whole tail) -- scanning {len(dirs)} tools ===")
    tot: Counter = Counter()
    for d in dirs:
        try:
            r = json.load(open(d + "/eval_report.json", encoding="utf-8"))
        except Exception:
            continue
        tr = r.get("test_results") or []
        fails = [x for x in tr if x.get("status") in ("failure", "failed")]
        if not fails:
            continue
        name = os.path.basename(d)
        cc = Counter(x.get("status") for x in tr)
        pa, nr, total = cc.get("passed", 0), cc.get("not_run", 0), sum(cc.values())
        bs = (
            " BUILD-SUSPECT" if (total and nr > 0.25 * total) else ""
        )  # high not_run -> build likely broke
        if bs:
            tot["tools_build_suspect"] += 1
        rec = sum(1 for x in fails if "args=" in _txt(x) or "Command '[" in _txt(x))
        if rec == 0:
            log(
                f"{name[:38]:<38} p{pa:<5d} nr{nr:<5d} f{len(fails):<5d} DEFER(no-recoverable-invocation){bs}"
            )
            tot["tools_defer_norec"] += 1
            continue
        try:
            js = V.auto_reference_check(Path(d), Path(d + "/eval_report.json"))
        except Exception as e:
            log(f"{name[:42]:<42} f={len(fails):<4d} ERROR {str(e)[:40]}")
            tot["tools_error"] += 1
            continue
        if not js:
            log(
                f"{name[:38]:<38} p{pa:<5d} nr{nr:<5d} f{len(fails):<5d} DEFER(no-functional-ref/unparsed){bs}"
            )
            tot["tools_defer_build"] += 1
            continue
        c = Counter(j.verdict.value for j in js)
        slop, corr = c.get("SLOP", 0), c.get("CORRECT", 0)
        log(
            f"{name[:38]:<38} p{pa:<5d} nr{nr:<5d} f{len(fails):<5d} SLOP={slop:<3d} CORRECT={corr:<3d}{bs}"
        )
        tot["tools_checked"] += 1
        tot["slop"] += slop
        tot["correct"] += corr
        if slop and corr == 0:
            tot["tools_all_slop"] += 1
    log(f"=== DONE: {dict(tot)} ===")
    out.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
