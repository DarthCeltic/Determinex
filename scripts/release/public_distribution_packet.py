"""Build the legal/public distribution evidence packet for source opening."""
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = "determinex-legal-public-distribution-evidence-v1"

AGPL_FILES = (
    "LICENSE",
    "pyproject.toml",
    "frontend/package.json",
    "frontend/src-tauri/Cargo.toml",
    "frontend/vscode-extension/package.json",
)

NOTICE_FILES = (
    "docs/release/MODEL_NOTICES.md",
    "docs/release/THIRD_PARTY_NOTICES.md",
)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _agpl_license_ok(root: Path) -> tuple[bool, list[str]]:
    evidence: list[str] = []
    for rel in AGPL_FILES:
        path = root / rel
        if not path.is_file():
            return False, evidence
        text = _read_text(path)
        evidence.append(rel)
        if rel == "LICENSE":
            if "GNU AFFERO GENERAL PUBLIC LICENSE" not in text or "Version 3" not in text:
                return False, evidence
        elif "AGPL-3.0" not in text:
            return False, evidence
    return True, evidence


def _notices_present(root: Path) -> tuple[bool, list[str]]:
    evidence: list[str] = []
    for rel in NOTICE_FILES:
        path = root / rel
        if not path.is_file() or not _read_text(path).strip():
            return False, evidence
        evidence.append(rel)
    return True, evidence


def _secret_scan_clean(pushed: bool) -> tuple[bool, str]:
    args = ["python", "scripts/security/secret_scan.py"]
    if pushed:
        args.append("--pushed")
    try:
        completed = subprocess.run(
            args,
            cwd=Path.cwd(),
            text=True,
            capture_output=True,
            check=False,
            timeout=240,
        )
    except subprocess.TimeoutExpired as exc:
        return False, f"{' '.join(args)} timed out after {exc.timeout} seconds"
    transcript = "\n".join(part for part in (completed.stdout, completed.stderr) if part).strip()
    return completed.returncode == 0, transcript[-8000:]


def build_packet(root: Path, *, operator_reviewed: bool, pushed_secret_scan: bool = True) -> dict:
    agpl_ok, license_evidence = _agpl_license_ok(root)
    notices_ok, notice_evidence = _notices_present(root)
    secret_clean, secret_scan_transcript = _secret_scan_clean(pushed_secret_scan)
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "legal_review_completed": bool(operator_reviewed and agpl_ok and notices_ok and secret_clean),
        "license_inventory_reviewed": agpl_ok,
        "model_notice_reviewed": notices_ok,
        "public_repo_secret_scan_passed": secret_clean,
        "public_repo_scrub_completed": bool(operator_reviewed and secret_clean),
        "third_party_notices_present": notices_ok,
        "authority_granted": False,
        "operator_reviewed": bool(operator_reviewed),
        "pushed_secret_scan": bool(pushed_secret_scan),
        "evidence": {
            "license_files": license_evidence,
            "notice_files": notice_evidence,
            "secret_scan_command": "python scripts/security/secret_scan.py --pushed"
            if pushed_secret_scan
            else "python scripts/security/secret_scan.py",
            "secret_scan_transcript_tail": secret_scan_transcript,
        },
        "claim_boundary": (
            "This packet records public-distribution hygiene checks and operator review. "
            "It does not grant release authority and is not a substitute for external legal counsel."
        ),
    }


def write_packet(root: Path, output: Path, *, operator_reviewed: bool, pushed_secret_scan: bool = True) -> dict:
    packet = build_packet(root, operator_reviewed=operator_reviewed, pushed_secret_scan=pushed_secret_scan)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    return packet


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--operator-reviewed", action="store_true")
    parser.add_argument("--tracked-only-secret-scan", action="store_true")
    args = parser.parse_args()

    root = Path.cwd()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output = args.output or root / "assurance/evidence/public_distribution" / f"legal_public_distribution_{stamp}.json"
    output = output if output.is_absolute() else root / output
    packet = write_packet(
        root,
        output,
        operator_reviewed=args.operator_reviewed,
        pushed_secret_scan=not args.tracked_only_secret_scan,
    )
    print(json.dumps({"output": str(output), "legal_review_completed": packet["legal_review_completed"]}, indent=2))
    return 0 if all(
        packet[field] is True
        for field in (
            "legal_review_completed",
            "license_inventory_reviewed",
            "model_notice_reviewed",
            "public_repo_secret_scan_passed",
            "public_repo_scrub_completed",
            "third_party_notices_present",
        )
    ) else 2


if __name__ == "__main__":
    raise SystemExit(main())
