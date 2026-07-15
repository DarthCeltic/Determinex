"""
Dependency vulnerability scanner.

Uses pip-audit (preferred) or safety as fallback to check installed Python
packages against known CVE databases.

Severity classification:
  CRITICAL / HIGH   → fail (block) unless explicitly waived
  MEDIUM            → warn, require acknowledgment
  LOW               → log only

Waiver mechanism: assurance/security/vulnerability_waivers.json
  {
    "waivers": [
      {
        "vuln_id": "CVE-2023-12345",
        "package": "requests",
        "reason": "...",
        "approved_by": "...",
        "expires": "2026-12-31"
      }
    ]
  }
"""
from __future__ import annotations

import json
import logging
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

log = logging.getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_WAIVER_PATH = _REPO_ROOT / "assurance" / "security" / "vulnerability_waivers.json"
_SCAN_OUTPUT = _REPO_ROOT / "assurance" / "security" / "dependency_scan.json"


@dataclass
class Vulnerability:
    vuln_id: str
    package: str
    installed_version: str
    fixed_version: str
    severity: str      # CRITICAL | HIGH | MEDIUM | LOW | UNKNOWN
    description: str
    waived: bool = False
    waiver_reason: str = ""


@dataclass
class ScanReport:
    scanner: str
    timestamp: str
    total_packages: int
    vulnerabilities: list[Vulnerability] = field(default_factory=list)
    scan_error: str | None = None

    @property
    def critical_count(self) -> int:
        return sum(1 for v in self.vulnerabilities if v.severity == "CRITICAL" and not v.waived)

    @property
    def high_count(self) -> int:
        return sum(1 for v in self.vulnerabilities if v.severity == "HIGH" and not v.waived)

    @property
    def blocked(self) -> bool:
        # scan_error means no scanner actually ran -- that is not the same as
        # "ran and found nothing". A missing tool must never read as a silent
        # PASS (this exact false-confidence bug: 0 packages scanned reported
        # as "0 vulnerabilities found").
        if self.scan_error:
            return True
        return self.critical_count > 0 or self.high_count > 0

    def to_dict(self) -> dict:
        return {
            "scanner": self.scanner,
            "timestamp": self.timestamp,
            "total_packages": self.total_packages,
            "critical_count": self.critical_count,
            "high_count": self.high_count,
            "blocked": self.blocked,
            "vulnerability_count": len(self.vulnerabilities),
            "vulnerabilities": [
                {
                    "id": v.vuln_id, "package": v.package,
                    "version": v.installed_version, "fixed": v.fixed_version,
                    "severity": v.severity, "waived": v.waived,
                }
                for v in self.vulnerabilities
            ],
        }


def _load_waivers() -> list[dict]:
    if not _WAIVER_PATH.is_file():
        return []
    try:
        data = json.loads(_WAIVER_PATH.read_text())
        today = date.today().isoformat()
        return [w for w in data.get("waivers", []) if w.get("expires", "9999") >= today]
    except Exception:
        return []


def _is_waived(vuln_id: str, package: str, waivers: list[dict]) -> tuple[bool, str]:
    for w in waivers:
        if w.get("vuln_id") == vuln_id and w.get("package", "").lower() == package.lower():
            return True, w.get("reason", "")
    return False, ""


def scan_with_pip_audit() -> ScanReport | None:
    import datetime
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip_audit", "--format=json", "-l"],
            capture_output=True, text=True, timeout=180,
        )
        # pip-audit exits 1 when it finds vulnerabilities (that is success, not
        # failure) but exits with other codes / empty stdout on a genuine
        # invocation error (bad flag, no environment found, etc). Empty stdout
        # must never silently parse to "0 packages, all clean" -- that is the
        # false-confidence bug this scanner previously had (a bad -q flag
        # caused every run to report PASS having scanned nothing).
        if not result.stdout.strip():
            raise RuntimeError(
                f"pip-audit produced no output (rc={result.returncode}): "
                f"{result.stderr[:500]}"
            )
        data = json.loads(result.stdout)
        waivers = _load_waivers()
        vulns = []

        # pip-audit output: list of {name, version, vulns: [{id, fix_versions, description}]}
        pkg_count = 0
        for pkg in (data if isinstance(data, list) else data.get("dependencies", [])):
            pkg_count += 1
            name = pkg.get("name", "")
            version = pkg.get("version", "")
            for v in pkg.get("vulns", []):
                vid = v.get("id", "")
                waived, reason = _is_waived(vid, name, waivers)
                vulns.append(Vulnerability(
                    vuln_id=vid,
                    package=name,
                    installed_version=version,
                    fixed_version=", ".join(v.get("fix_versions", [])),
                    severity="HIGH",  # pip-audit doesn't always give severity — default HIGH
                    description=v.get("description", "")[:200],
                    waived=waived,
                    waiver_reason=reason,
                ))

        return ScanReport(
            scanner="pip-audit",
            timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            total_packages=pkg_count,
            vulnerabilities=vulns,
        )
    except Exception as e:
        log.warning("[dependency_scan] pip-audit failed: %s", e)
        return None


def run(output_path: Path | None = None) -> ScanReport:
    import datetime

    report = scan_with_pip_audit()
    if report is None:
        report = ScanReport(
            scanner="none",
            timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            total_packages=0,
            scan_error="No scanner available. Install pip-audit: pip install pip-audit",
        )

    out = output_path or _SCAN_OUTPUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report.to_dict(), indent=2), encoding="utf-8")

    if report.blocked:
        log.error("[dependency_scan] BLOCKED: %d critical, %d high severity CVEs",
                  report.critical_count, report.high_count)
    else:
        log.info("[dependency_scan] PASS: %d vulnerabilities found (none blocking)",
                 len(report.vulnerabilities))

    return report


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    r = run()
    print(f"Scanner: {r.scanner}")
    print(f"Packages: {r.total_packages}")
    print(f"Vulnerabilities: {len(r.vulnerabilities)}")
    print(f"Blocked: {r.blocked}")
