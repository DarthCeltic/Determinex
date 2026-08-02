#!/usr/bin/env python3
"""determinex_notify.py — webhook notifications (Discord/Slack/Telegram/Generic).

Reads webhook URL from env DETERMINEX_NOTIFY_URL. Posts JSON.
Supports auto-detect of platform via URL pattern.

Usage:
    determinex_notify.py "Pool drained — 75/87 done, 12 scored"
    determinex_notify.py --level=critical "Pool stalled — 0 progress in 30 min"
    determinex_notify.py --tool=cheat --score=14.98 "Tool result"
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.request


def detect_platform(url: str) -> str:
    if "discord.com" in url or "discordapp.com" in url:
        return "discord"
    if "hooks.slack.com" in url:
        return "slack"
    if "api.telegram.org" in url:
        return "telegram"
    return "generic"


def discord_payload(msg: str, level: str = "info", tool: str = None, score: float = None) -> dict:
    colors = {"info": 0x3498DB, "ok": 0x2ECC71, "warn": 0xF39C12, "critical": 0xE74C3C}
    embed = {
        "title": f"Determinex {level.upper()}",
        "description": msg,
        "color": colors.get(level, 0x95A5A6),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "fields": [],
    }
    if tool:
        embed["fields"].append({"name": "tool", "value": tool, "inline": True})
    if score is not None:
        embed["fields"].append({"name": "score", "value": f"{score:.2f}%", "inline": True})
    return {"embeds": [embed]}


def slack_payload(msg: str, level: str = "info", tool: str = None, score: float = None) -> dict:
    icons = {
        "info": ":information_source:",
        "ok": ":white_check_mark:",
        "warn": ":warning:",
        "critical": ":rotating_light:",
    }
    text = f"{icons.get(level, '')} *Determinex* — {msg}"
    if tool:
        text += f"  `{tool}`"
    if score is not None:
        text += f"  `{score:.2f}%`"
    return {"text": text}


def post(url: str, payload: dict) -> bool:
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url, data=data, headers={"Content-Type": "application/json"}, method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status < 300
    except Exception as e:
        sys.stderr.write(f"webhook post failed: {e}\n")
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("message", nargs="+")
    ap.add_argument("--level", default="info", choices=["info", "ok", "warn", "critical"])
    ap.add_argument("--tool")
    ap.add_argument("--score", type=float)
    ap.add_argument("--url", default=os.environ.get("DETERMINEX_NOTIFY_URL"))
    args = ap.parse_args()
    msg = " ".join(args.message)

    if not args.url:
        sys.stderr.write("no webhook URL (set DETERMINEX_NOTIFY_URL or pass --url)\n")
        return 1

    platform = detect_platform(args.url)
    if platform == "discord":
        payload = discord_payload(msg, args.level, args.tool, args.score)
    elif platform == "slack":
        payload = slack_payload(msg, args.level, args.tool, args.score)
    else:
        payload = {"message": msg, "level": args.level, "tool": args.tool, "score": args.score}

    ok = post(args.url, payload)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
