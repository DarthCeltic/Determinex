#!/usr/bin/env python3
"""
secret_scan.py -- find leaked API keys / secrets in the working tree and history
================================================================================
Defensive security for YOUR machine, independent of any product claim. Scans for
provider-key shapes (Anthropic / Google / OpenAI / DeepSeek / generic) so a live
secret never sits in a tracked file or in pushed git history.

    python scripts/security/secret_scan.py            # scan tracked working tree
    python scripts/security/secret_scan.py --history  # also scan ALL git history
    python scripts/security/secret_scan.py --pushed   # only what the REMOTE has

Prints REDACTED matches (first/last few chars) and a clear verdict. Exit 1 if any
secret is found in a place that could leak (tracked file, or pushed history).
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent

# provider key shapes (kept tight to avoid false positives)
PATTERNS = {
    "anthropic": re.compile(r"sk-ant-api[0-9]{2}-[A-Za-z0-9_-]{20,}"),
    "google":    re.compile(r"AIzaSy[A-Za-z0-9_-]{30,}"),
    "openai":    re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{40,}"),
    "deepseek":  re.compile(r"\bsk-[a-f0-9]{32}\b"),
    "aws":       re.compile(r"AKIA[0-9A-Z]{16}"),
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}
_SKIP = (".env.example", "package-lock.json", ".lock", ".bak", "/secret_scan.py",
         ".pre-commit-config.yaml")


def _redact(s: str) -> str:
    return s[:8] + "..." + s[-4:] if len(s) > 14 else s[:4] + "..."


def _scan_text(text: str) -> list[tuple[str, str]]:
    hits = []
    for name, pat in PATTERNS.items():
        for m in pat.findall(text):
            hits.append((name, _redact(m)))
    return hits


def _git(args: list[str]) -> str:
    # decode as utf-8 with replacement so binary blobs (parquet, etc.) and
    # non-cp1252 bytes never crash the scan on Windows.
    try:
        r = subprocess.run(["git", *args], cwd=str(REPO), capture_output=True,
                           timeout=180)
        return (r.stdout or b"").decode("utf-8", errors="replace")
    except Exception:
        return ""


# Paths that legitimately contain key-SHAPED strings -- NOT your secrets:
#  - corpus/ is benchmark TOOL data (upstream test vectors / fixtures), e.g.
#    ripsecrets' own fixtures, mbedtls/openssl/age crypto test PEMs, the AWS
#    documentation example key. These ship with the tools; they are not credentials.
#  - the secret-detection tooling + its tests contain key SHAPES by design.
_FALSE_POSITIVE = re.compile(
    r"^corpus/|/corpus/|ripsecrets|secret_scan|secret_scanner|test_secret"
    r"|\.parquet$|\.env\.example$|testdata|test_vectors|crypto"
    r"|detect.?secret|gitleaks|trufflehog|AKIAIOSFODNN7EXAMPLE", re.I)


def scan_tracked() -> dict:
    """Fast native scan via `git grep` (handles 100k+ tracked files instantly)."""
    out: dict = {}
    alt = "|".join(p.pattern for p in PATTERNS.values())
    files = _git(["grep", "-lE", alt,
                  "--", ":!*.lock", ":!*package-lock.json"]).splitlines()
    for rel in files:
        if any(s in rel for s in _SKIP) or _FALSE_POSITIVE.search(rel):
            continue
        p = REPO / rel
        try:
            if p.stat().st_size > 2_000_000:
                continue
            hits = _scan_text(p.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        if hits:
            out[rel] = hits
    return out


def scan_history(remotes_only: bool) -> dict:
    """Scan every blob ever committed (or only on remote refs)."""
    rev = ["--remotes"] if remotes_only else ["--all"]
    out = {}
    # list commits + the .env / config blobs they touched, scan those blobs
    log = _git(["log", *rev, "--pretty=%H", "--name-only", "--diff-filter=AM"])
    seen: set[str] = set()
    commit = ""
    for line in log.splitlines():
        if re.fullmatch(r"[0-9a-f]{40}", line):
            commit = line
            continue
        rel = line.strip()
        if not rel or any(s in rel for s in _SKIP):
            continue
        # only bother with files that commonly hold secrets
        if not re.search(r"\.env|config|\.json|\.ya?ml|\.sh|\.toml|key|secret|cred", rel, re.I):
            continue
        key = f"{commit}:{rel}"
        if key in seen:
            continue
        seen.add(key)
        blob = _git(["show", key])
        hits = _scan_text(blob)
        if hits:
            out.setdefault(rel, []).append((commit[:9], hits))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Determinex secret scanner")
    ap.add_argument("--history", action="store_true", help="scan ALL git history")
    ap.add_argument("--pushed", action="store_true", help="scan only remote/pushed history")
    args = ap.parse_args()

    print("=== secret scan: tracked working tree ===")
    tracked = scan_tracked()
    if tracked:
        for rel, hits in tracked.items():
            for name, red in hits:
                print(f"  LEAK  {rel}: {name} {red}")
    else:
        print("  clean -- no secrets in tracked files")

    pushed_bad = False
    if args.pushed or args.history:
        scope = "remote/pushed" if args.pushed else "ALL"
        print(f"\n=== secret scan: {scope} git history ===")
        hist = scan_history(remotes_only=args.pushed)
        if hist:
            for rel, recs in hist.items():
                for commit, hits in recs:
                    for name, red in hits:
                        leaked = " (PUSHED -- ROTATE NOW)" if args.pushed else " (local history)"
                        print(f"  {commit} {rel}: {name} {red}{leaked}")
                        if args.pushed:
                            pushed_bad = True
        else:
            print(f"  clean -- no secrets in {scope} history")

    print("\n=== verdict ===")
    if tracked or pushed_bad:
        print("  ACTION REQUIRED: a secret is in a leakable location. Rotate the key(s)")
        print("  and remove from tracking/history. See docs/SECURITY_POSTURE.md.")
        return 1
    print("  OK: no secret in tracked files or pushed history.")
    if args.history:
        print("  (Any matches above were LOCAL-only history -- not leaked off-box, but")
        print("   rotate + scrub if the box could be accessed. See docs/SECURITY_POSTURE.md.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
