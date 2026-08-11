#!/usr/bin/env python3
"""Who started watching, starring, forking, or following? Diff against last run.

GitHub notifies you about issues and PRs. It does not notify you when someone starts
WATCHING a repository, stars it, forks it, or follows you -- and during a competition
those are the signals that matter, because they tell you who is paying attention before
they do anything visible.

There is no event API for this either: GitHub stopped emitting FollowEvent to public
timelines, so a follow cannot be timestamped after the fact. The only reliable method is
to snapshot the lists and diff them, which means the FIRST run establishes a baseline and
sees nothing. That is stated rather than hidden, because a monitoring tool that reports
"no changes" on its first run is indistinguishable from one that is broken.

    python scripts/dev/watch_alert.py                    # diff against the last snapshot
    python scripts/dev/watch_alert.py --json             # machine-readable, for a scheduler
    python scripts/dev/watch_alert.py --repos a/b c/d    # override the watched set
"""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import UTC, datetime, timedelta
from pathlib import Path

STATE = Path(__file__).resolve().parent.parent.parent / ".determinex" / "watch_alert.json"
USER = "DarthCeltic"
REPOS = ["DarthCeltic/Determinex"]


def gh(path: str) -> list:
    """One paged GitHub API call. Returns [] on any failure -- a monitor must not crash."""
    try:
        r = subprocess.run(
            ["gh", "api", f"{path}?per_page=100", "--jq", ".[].login"],
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
        return [x for x in r.stdout.split() if x]
    except Exception:
        return []


def collect(repos: list[str]) -> dict[str, list[str]]:
    snap = {"followers": gh(f"users/{USER}/followers")}
    for repo in repos:
        snap[f"{repo}::stars"] = gh(f"repos/{repo}/stargazers")
        snap[f"{repo}::watchers"] = gh(f"repos/{repo}/subscribers")
        snap[f"{repo}::forks"] = [
            x
            for x in subprocess.run(
                ["gh", "api", f"repos/{repo}/forks?per_page=100", "--jq", ".[].owner.login"],
                capture_output=True,
                text=True,
                timeout=60,
                check=False,
            ).stdout.split()
            if x
        ]
    return snap


#: Append-only observation log. Never rewritten -- an hourly series whose history can be edited
#: by the next run is not a series.
PULSE = Path(__file__).resolve().parent.parent.parent / ".determinex" / "repo_pulse.jsonl"


def _gh_json(path: str):
    """One GitHub API call returning parsed JSON, or None. A monitor must not crash."""
    try:
        r = subprocess.run(
            ["gh", "api", path],
            capture_output=True,
            text=True,
            timeout=90,
            check=False,
        )
        if r.returncode != 0 or not r.stdout.strip():
            return None
        return json.loads(r.stdout)
    except Exception:
        return None


def traffic(repo: str) -> dict:
    """Clones, views, referrers and paths as GitHub currently reports them.

    Values are per-DAY buckets; the day in progress is a running total, which is what makes
    hourly differencing possible. A missing section is recorded as None rather than {} so that
    "the API did not answer" stays distinguishable from "the answer was zero" -- collapsing
    those two is how a monitor reports calm during an outage.
    """
    out: dict = {"repo": repo}

    clones = _gh_json(f"repos/{repo}/traffic/clones")
    out["clones"] = (
        {
            c["timestamp"][:10]: {"count": c["count"], "uniques": c["uniques"]}
            for c in clones["clones"]
        }
        if isinstance(clones, dict) and "clones" in clones
        else None
    )
    views = _gh_json(f"repos/{repo}/traffic/views")
    out["views"] = (
        {
            v["timestamp"][:10]: {"count": v["count"], "uniques": v["uniques"]}
            for v in views["views"]
        }
        if isinstance(views, dict) and "views" in views
        else None
    )
    refs = _gh_json(f"repos/{repo}/traffic/popular/referrers")
    out["referrers"] = (
        {x["referrer"]: {"count": x["count"], "uniques": x["uniques"]} for x in refs}
        if isinstance(refs, list)
        else None
    )
    paths = _gh_json(f"repos/{repo}/traffic/popular/paths")
    out["paths"] = (
        {x["path"]: {"count": x["count"], "uniques": x["uniques"]} for x in paths[:15]}
        if isinstance(paths, list)
        else None
    )
    meta = _gh_json(f"repos/{repo}")
    out["stars"] = meta.get("stargazers_count") if isinstance(meta, dict) else None
    out["forks"] = meta.get("forks_count") if isinstance(meta, dict) else None
    return out


def record_pulse(repos: list[str]) -> dict:
    """Append one observation per repo. Returns the observation written."""
    obs = {
        "observed_at": datetime.now(UTC).isoformat(),
        "repos": [traffic(r) for r in repos],
    }
    PULSE.parent.mkdir(parents=True, exist_ok=True)
    with PULSE.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(obs) + "\n")
    return obs


def _load_pulse() -> list[dict]:
    if not PULSE.is_file():
        return []
    rows = []
    for line in PULSE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue  # a torn final line during a crash must not kill the report
    return rows


def pulse_report(hours: float) -> list[str]:
    """Per-interval deltas over the requested window, derived by differencing observations."""
    rows = _load_pulse()
    if len(rows) < 2:
        return [
            f"  only {len(rows)} observation(s) recorded -- a delta needs two.",
            "  Nothing is being claimed about activity yet; run again in an hour.",
        ]
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    out: list[str] = []
    for a, b in zip(rows, rows[1:]):
        t_b = datetime.fromisoformat(b["observed_at"])
        if t_b < cutoff:
            continue
        t_a = datetime.fromisoformat(a["observed_at"])
        gap = (t_b - t_a).total_seconds() / 3600
        for ra, rb in zip(a.get("repos", []), b.get("repos", [])):
            if ra.get("repo") != rb.get("repo"):
                continue
            bits = []
            for field in ("clones", "views"):
                da, db = ra.get(field), rb.get(field)
                if not isinstance(da, dict) or not isinstance(db, dict):
                    bits.append(f"{field}=n/a")
                    continue
                # Difference every day bucket, so a late-appearing day is not missed.
                d_count = sum(v["count"] - da.get(k, {}).get("count", 0) for k, v in db.items())
                d_uniq = sum(v["uniques"] - da.get(k, {}).get("uniques", 0) for k, v in db.items())
                bits.append(f"{field} +{d_count} (+{d_uniq}u)")
            ds = (rb.get("stars") or 0) - (ra.get("stars") or 0)
            df = (rb.get("forks") or 0) - (ra.get("forks") or 0)
            if ds:
                bits.append(f"STARS +{ds}")
            if df:
                bits.append(f"FORKS +{df}")
            out.append(f"  {t_b.strftime('%m-%d %H:%M')}Z  (+{gap:.1f}h)  " + "  ".join(bits))
    if not out:
        out = [f"  no observation pairs inside the last {hours:g}h."]
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true", help="emit JSON instead of prose")
    ap.add_argument("--repos", nargs="*", default=REPOS)
    ap.add_argument(
        "--pulse",
        action="store_true",
        help="also record a traffic observation (clones/views/referrers/paths)",
    )
    ap.add_argument(
        "--report",
        type=float,
        metavar="HOURS",
        default=None,
        help="print per-interval traffic deltas over the last N hours and exit",
    )
    args = ap.parse_args()

    if args.report is not None:
        print(f"\n  repo pulse -- last {args.report:g}h (deltas between observations)\n")
        for line in pulse_report(args.report):
            print(line)
        print(
            "\n  Note: GitHub reports traffic per DAY and lags behind live activity, so a delta"
            "\n  is attributed to when it was OBSERVED, not when the clone happened.\n"
        )
        return 0

    if args.pulse:
        record_pulse(args.repos)

    now = collect(args.repos)
    prev = {}
    first_run = not STATE.is_file()
    if not first_run:
        try:
            prev = json.loads(STATE.read_text(encoding="utf-8")).get("snapshot", {})
        except Exception:
            prev, first_run = {}, True

    new: dict[str, list[str]] = {}
    gone: dict[str, list[str]] = {}
    for key, names in now.items():
        before = set(prev.get(key, []))
        added = [n for n in names if n not in before]
        removed = [n for n in before if n not in names]
        if added:
            new[key] = added
        if removed:
            gone[key] = removed

    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(
        json.dumps({"checked_at": datetime.now(UTC).isoformat(), "snapshot": now}, indent=2),
        encoding="utf-8",
    )

    if args.json:
        print(
            json.dumps(
                {
                    "first_run": first_run,
                    "new": new,
                    "gone": gone,
                    "totals": {k: len(v) for k, v in now.items()},
                },
                indent=2,
            )
        )
        return 0

    if first_run:
        print("BASELINE ESTABLISHED (first run sees nothing by construction):")
        for k, v in now.items():
            print(f"  {k:<44} {len(v)}")
        print("\n  Run again later to see changes.")
        return 0

    if not new and not gone:
        print(
            "no change since last check.  "
            + "  ".join(f"{k.split('::')[-1]}={len(v)}" for k, v in now.items())
        )
        return 0

    for key, names in new.items():
        print(f"NEW {key}:")
        for n in names:
            print(f"  + {n}   https://github.com/{n}")
    for key, names in gone.items():
        print(f"LOST {key}:")
        for n in names:
            print(f"  - {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
