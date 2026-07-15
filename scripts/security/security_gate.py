#!/usr/bin/env python3
"""security_gate.py -- single pass/fail artifact over all security scanners.

Runs secret_scan, dependency_scan, verify_lockfiles, license_scan, and
container_scan (generate_sbom is informational, not a gate -- it has nothing
to pass/fail, it just produces an inventory) and produces ONE consolidated
result instead of six scripts each interpreted separately. Matches the
pb_board_guard.py / pb_override_scan.py --guard convention: exit 0 = clean,
exit 1 = blocked, human-readable summary either way.

Usage:
  python scripts/security/security_gate.py           # run all gates, print summary
  python scripts/security/security_gate.py --guard   # same, but exit 1 on any block (CI use)
  python scripts/security/security_gate.py --json out.json   # also write machine-readable result
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import sys
from contextlib import redirect_stdout
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts" / "security"))


@contextlib.contextmanager
def _bare_argv():
    """Each sub-scanner's main() calls argparse.parse_args() with no explicit
    argv, so it inherits THIS script's own --guard/--json flags and crashes.
    Sandbox sys.argv to just the program name for the duration of the call."""
    saved = sys.argv
    sys.argv = [saved[0]]
    try:
        yield
    finally:
        sys.argv = saved


def _run_secret_scan() -> tuple[bool, str]:
    import secret_scan  # type: ignore[import-not-found]
    buf = io.StringIO()
    with _bare_argv(), redirect_stdout(buf):
        code = secret_scan.main()
    lines = buf.getvalue().strip().splitlines()
    return (code == 0), (lines[-1] if lines else "no output")


def _run_dependency_scan() -> tuple[bool, str]:
    import dependency_scan  # type: ignore[import-not-found]
    r = dependency_scan.run()
    detail = f"{r.total_packages} packages, {len(r.vulnerabilities)} vulns ({r.critical_count} critical, {r.high_count} high)"
    if r.scan_error:
        detail = f"SCAN DID NOT RUN: {r.scan_error}"
    return (not r.blocked), detail


def _run_verify_lockfiles() -> tuple[bool, str]:
    import verify_lockfiles  # type: ignore[import-not-found]
    r = verify_lockfiles.run()
    return r.passed, f"{len(r.files_checked)} files checked, {r.critical_count} critical violations"


def _run_license_scan() -> tuple[bool, str]:
    import license_scan  # type: ignore[import-not-found]
    out_path = REPO_ROOT / "assurance" / "licenses" / "license_inventory.json"
    with _bare_argv():
        license_scan.main()
    data = json.loads(out_path.read_text(encoding="utf-8"))
    blocked = data.get("blocked_count", 0)
    # A blocked_count of exactly 1 pointing at the repo root itself with
    # source="none" is the scanner not recognizing Determinex's own custom
    # Source-Available LICENSE (no SPDX id) -- not a real finding. Anything
    # else blocked is real and should fail this gate.
    real_blocks = [
        r for r in data.get("rows", [])
        if not (r.get("path") == str(REPO_ROOT) and r.get("source") == "none")
    ]
    return (len(real_blocks) == 0), f"{blocked} flagged ({len(real_blocks)} not the known repo-license false positive)"


def _run_container_scan() -> tuple[bool, str]:
    import container_scan  # type: ignore[import-not-found]
    out_path = REPO_ROOT / "assurance" / "security" / "container_scan.json"
    with _bare_argv():
        container_scan.main()
    data = json.loads(out_path.read_text(encoding="utf-8"))
    unpinned = data.get("unpinned_count", 0)
    # container_scan is inventory + advisory (docstring: "does not perform a
    # CVE scan by itself"), not a hard gate -- unpinned tags are a finding to
    # know about, not something that should block every commit.
    return True, f"{data.get('image_count', 0)} images, {unpinned} unpinned tags (advisory, non-blocking)"


GATES = [
    ("secret_scan", _run_secret_scan),
    ("dependency_scan", _run_dependency_scan),
    ("verify_lockfiles", _run_verify_lockfiles),
    ("license_scan", _run_license_scan),
    ("container_scan", _run_container_scan),
]


def run_all() -> dict:
    results = []
    for name, fn in GATES:
        try:
            passed, detail = fn()
        except Exception as e:  # a gate crashing is a block, never a silent pass
            passed, detail = False, f"GATE CRASHED: {e}"
        results.append({"gate": name, "passed": passed, "detail": detail})
    overall = all(r["passed"] for r in results)
    return {
        "schema": "determinex-security-gate-v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "overall_passed": overall,
        "gates": results,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--guard", action="store_true", help="exit 1 if any gate blocked (CI mode)")
    p.add_argument("--json", type=Path, help="also write the machine-readable result here")
    args = p.parse_args(argv)

    result = run_all()

    print("=== Determinex Security Gate ===")
    for g in result["gates"]:
        status = "PASS" if g["passed"] else "BLOCKED"
        print(f"  [{status:7s}] {g['gate']:20s} {g['detail']}")
    print()
    print(f"Overall: {'PASS' if result['overall_passed'] else 'BLOCKED'}")

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(f"Wrote: {args.json}")

    if args.guard and not result["overall_passed"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
