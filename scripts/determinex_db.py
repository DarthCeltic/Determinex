#!/usr/bin/env python3
"""determinex_db.py — SQLite single source of truth for Determinex state.

Replaces:
- logs/mass_run_v2/inspection_report.json
- logs/mass_run_v2/argv_miner.json
- logs/mass_run_v2/oracle_memos.json
- logs/mass_run_v2/fixture_bank.json
- logs/mass_run_v2/scaffold_plan.json
- logs/mass_run_v2/failure_analysis.json
- /root/queue/{pending,claimed,done}.txt on Hetzner
- ad-hoc grep + jq queries across eval.json files

Schema:
  tools(instance_id PK, family, version, last_eval_at, locked_pct)
  evals(id PK, instance_id, branch, ran_at, passed, total, pct, duration_s, rc, error)
  test_results(id PK, eval_id, test_name, status, message)
  queue(instance_id PK, tier, claimed_by, claimed_at, status)
  iterations(id PK, started_at, ended_at, scaffold_version, total_tools, scored, agg_weighted, agg_per_tool)

Usage:
  python scripts/determinex_db.py init
  python scripts/determinex_db.py import-evals
  python scripts/determinex_db.py top 20
  python scripts/determinex_db.py bottom 20
  python scripts/determinex_db.py compare iter21 iter22
  python scripts/determinex_db.py history burntsushi__ripgrep
"""
from __future__ import annotations
import argparse
import glob
import json
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "logs" / "determinex.db"


SCHEMA = """
CREATE TABLE IF NOT EXISTS tools (
    instance_id TEXT PRIMARY KEY,
    family TEXT,
    version TEXT,
    last_eval_at REAL,
    locked_pct REAL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS evals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    instance_id TEXT NOT NULL,
    branch TEXT,
    iteration_id INTEGER,
    ran_at REAL NOT NULL,
    passed INTEGER,
    total INTEGER,
    pct REAL,
    duration_s INTEGER,
    rc INTEGER,
    error TEXT,
    source_path TEXT,
    UNIQUE(instance_id, ran_at)
);
CREATE INDEX IF NOT EXISTS idx_evals_inst ON evals(instance_id);
CREATE INDEX IF NOT EXISTS idx_evals_iter ON evals(iteration_id);
CREATE INDEX IF NOT EXISTS idx_evals_pct ON evals(pct);

CREATE TABLE IF NOT EXISTS test_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    eval_id INTEGER NOT NULL,
    test_name TEXT NOT NULL,
    status TEXT NOT NULL,
    message TEXT,
    FOREIGN KEY(eval_id) REFERENCES evals(id)
);
CREATE INDEX IF NOT EXISTS idx_results_eval ON test_results(eval_id);

CREATE TABLE IF NOT EXISTS queue (
    instance_id TEXT PRIMARY KEY,
    tier TEXT NOT NULL,
    claimed_by TEXT,
    claimed_at REAL,
    status TEXT NOT NULL DEFAULT 'pending'
);
CREATE INDEX IF NOT EXISTS idx_queue_status ON queue(status);

CREATE TABLE IF NOT EXISTS iterations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    label TEXT,
    started_at REAL NOT NULL,
    ended_at REAL,
    scaffold_version TEXT,
    total_tools INTEGER,
    scored INTEGER,
    agg_weighted REAL,
    agg_per_tool REAL,
    notes TEXT
);
"""


def conn() -> sqlite3.Connection:
    DB.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB)
    _verify_integrity(c, DB)
    c.executescript(SCHEMA)
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("PRAGMA foreign_keys=ON")
    return c


def _verify_integrity(c: sqlite3.Connection, path: Path) -> None:
    rows = c.execute("PRAGMA integrity_check").fetchall()
    problems = [str(row[0]) for row in rows if row and row[0] != "ok"]
    if problems:
        preview = "; ".join(problems[:5])
        raise sqlite3.DatabaseError(
            f"SQLite integrity_check failed for {path}: {preview}"
        )


def cmd_init(args):
    c = conn()
    c.commit(); c.close()
    print(f"OK: db at {DB}")


def cmd_import_evals(args):
    """Walk T:/determinex-programbench/ for all *.eval.json and import."""
    c = conn()
    cur = c.cursor()
    imported = skipped = 0
    pattern = "T:/determinex-programbench/determinex_pb_*_v*/*/*.eval.json"
    for ej in glob.glob(pattern):
        try:
            mtime = Path(ej).stat().st_mtime
            j = json.loads(Path(ej).read_text(encoding="utf-8"))
        except Exception as e:
            skipped += 1
            continue
        inst = Path(ej).parent.name
        r = j.get("test_results") or []
        if not r:
            skipped += 1
            continue
        passed = sum(1 for x in r if x.get("status") == "passed")
        total = len(r)
        pct = round(100 * passed / total, 2)
        try:
            cur.execute("""
                INSERT OR IGNORE INTO evals(instance_id, ran_at, passed, total, pct, source_path)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (inst, mtime, passed, total, pct, ej))
            if cur.rowcount > 0:
                imported += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ERR  {inst}: {e}")
    # Update tools.last_eval_at + locked_pct
    cur.execute("""
        INSERT OR REPLACE INTO tools(instance_id, last_eval_at, locked_pct)
        SELECT instance_id, MAX(ran_at), MAX(pct)
        FROM evals
        GROUP BY instance_id
    """)
    c.commit()
    c.close()
    print(f"imported: {imported}, skipped: {skipped}")


def cmd_top(args):
    c = conn()
    rows = c.execute("""
        SELECT t.instance_id,
               (SELECT pct FROM evals e WHERE e.instance_id=t.instance_id ORDER BY ran_at DESC LIMIT 1) latest_pct,
               (SELECT passed FROM evals e WHERE e.instance_id=t.instance_id ORDER BY ran_at DESC LIMIT 1) passed,
               (SELECT total FROM evals e WHERE e.instance_id=t.instance_id ORDER BY ran_at DESC LIMIT 1) total
        FROM tools t
        ORDER BY latest_pct DESC NULLS LAST
        LIMIT ?
    """, (args.n,)).fetchall()
    print(f"=== TOP {args.n} ===")
    for inst, pct, p, t in rows:
        if pct is None: continue
        print(f"  {pct:6.2f}%  {p:>5}/{t:<5}  {inst}")
    c.close()


def cmd_bottom(args):
    c = conn()
    rows = c.execute("""
        SELECT t.instance_id,
               (SELECT pct FROM evals e WHERE e.instance_id=t.instance_id ORDER BY ran_at DESC LIMIT 1) latest_pct,
               (SELECT passed FROM evals e WHERE e.instance_id=t.instance_id ORDER BY ran_at DESC LIMIT 1) passed,
               (SELECT total FROM evals e WHERE e.instance_id=t.instance_id ORDER BY ran_at DESC LIMIT 1) total
        FROM tools t
        WHERE latest_pct IS NOT NULL
        ORDER BY latest_pct ASC
        LIMIT ?
    """, (args.n,)).fetchall()
    print(f"=== BOTTOM {args.n} ===")
    for inst, pct, p, t in rows:
        print(f"  {pct:6.2f}%  {p:>5}/{t:<5}  {inst}")
    c.close()


def cmd_history(args):
    c = conn()
    rows = c.execute("""
        SELECT ran_at, passed, total, pct, duration_s, rc
        FROM evals
        WHERE instance_id = ?
        ORDER BY ran_at DESC
        LIMIT 20
    """, (args.tool,)).fetchall()
    print(f"=== HISTORY {args.tool} ===")
    for ran_at, p, t, pct, d, rc in rows:
        ts = datetime.fromtimestamp(ran_at, tz=timezone.utc).strftime("%Y-%m-%d %H:%M")
        print(f"  {ts}  {pct:6.2f}%  {p}/{t}  ({d or '?'}s rc={rc or '?'})")
    c.close()


def cmd_stats(args):
    c = conn()
    cur = c.cursor()
    n_evals = cur.execute("SELECT COUNT(*) FROM evals").fetchone()[0]
    n_tools = cur.execute("SELECT COUNT(DISTINCT instance_id) FROM evals").fetchone()[0]
    # Latest per tool
    latest = cur.execute("""
        SELECT pct FROM evals e1
        WHERE ran_at = (SELECT MAX(ran_at) FROM evals e2 WHERE e2.instance_id = e1.instance_id)
        AND pct IS NOT NULL
    """).fetchall()
    pcts = [r[0] for r in latest]
    buckets = {"95-100": 0, "70-94": 0, "40-69": 0, "10-39": 0, "0-9": 0}
    for p in pcts:
        if p >= 95: buckets["95-100"] += 1
        elif p >= 70: buckets["70-94"] += 1
        elif p >= 40: buckets["40-69"] += 1
        elif p >= 10: buckets["10-39"] += 1
        else: buckets["0-9"] += 1
    print(f"total evals: {n_evals}  tools: {n_tools}  scored-latest: {len(pcts)}")
    print(f"weighted avg: {sum(pcts)/max(1,len(pcts)):.2f}%")
    print("buckets:")
    for k, v in buckets.items():
        print(f"  {k}%: {v}")
    c.close()


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init")
    sub.add_parser("import-evals")
    sp = sub.add_parser("top"); sp.add_argument("n", type=int, nargs="?", default=15)
    sp = sub.add_parser("bottom"); sp.add_argument("n", type=int, nargs="?", default=15)
    sp = sub.add_parser("history"); sp.add_argument("tool")
    sub.add_parser("stats")
    args = ap.parse_args()

    cmds = {"init": cmd_init, "import-evals": cmd_import_evals,
            "top": cmd_top, "bottom": cmd_bottom,
            "history": cmd_history, "stats": cmd_stats}
    cmds[args.cmd](args)


if __name__ == "__main__":
    main()
