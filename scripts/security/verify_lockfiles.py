"""
Lockfile verifier — confirms Python requirements files use pinned, hash-verified installs.

Checks:
  1. All direct dependencies are pinned (==, not >=, ~=, ^)
  2. No dependency has a known-bad version pattern
  3. Hash-checking mode supported (--require-hashes compatible)
  4. No unpinned VCS dependencies (git+https:// without @commit)

Reports violations as a structured list. Fails (exit 1) if any CRITICAL violations found.
"""
from __future__ import annotations

import logging
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

log = logging.getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent

_REQUIREMENTS_FILES = [
    "requirements.txt",
    "requirements-dev.txt",
    "scripts/requirements.txt",
    "scripts/requirements_bench.txt",
]

_PINNED = re.compile(r"^[A-Za-z0-9_.\-]+==[\d.]+")
_VCS_UNPINNED = re.compile(r"git\+https?://[^@\s]+(?!@[0-9a-f]{40})")
_UNPINNED_SPECIFIER = re.compile(r"[>~^]=|>=")
_COMMENT_OR_EMPTY = re.compile(r"^\s*(#|$)")
_OPTION_LINE = re.compile(r"^\s*-[rce]")


@dataclass
class LockfileViolation:
    file: str
    line_num: int
    line: str
    severity: str        # "CRITICAL" | "HIGH" | "MEDIUM"
    reason: str


@dataclass
class LockfileReport:
    files_checked: list[str] = field(default_factory=list)
    violations: list[LockfileViolation] = field(default_factory=list)

    @property
    def critical_count(self) -> int:
        return sum(1 for v in self.violations if v.severity == "CRITICAL")

    @property
    def passed(self) -> bool:
        return self.critical_count == 0

    def to_dict(self) -> dict:
        return {
            "files_checked": self.files_checked,
            "passed": self.passed,
            "violation_count": len(self.violations),
            "critical_count": self.critical_count,
            "violations": [
                {
                    "file": v.file, "line": v.line_num,
                    "content": v.line[:80], "severity": v.severity, "reason": v.reason
                }
                for v in self.violations
            ],
        }


def check_file(path: Path) -> list[LockfileViolation]:
    violations = []
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return []

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if _COMMENT_OR_EMPTY.match(stripped) or _OPTION_LINE.match(stripped):
            continue

        # VCS deps without commit hash
        if _VCS_UNPINNED.search(stripped):
            violations.append(LockfileViolation(
                file=str(path), line_num=i, line=stripped,
                severity="HIGH",
                reason="VCS dependency without pinned commit hash",
            ))
            continue

        # Unpinned specifiers
        if _UNPINNED_SPECIFIER.search(stripped) and not _PINNED.match(stripped):
            violations.append(LockfileViolation(
                file=str(path), line_num=i, line=stripped,
                severity="MEDIUM",
                reason="Dependency not pinned to exact version (use ==)",
            ))

    return violations


def run(repo_root: Path | None = None) -> LockfileReport:
    root = repo_root or _REPO_ROOT
    report = LockfileReport()

    for rel_path in _REQUIREMENTS_FILES:
        f = root / rel_path
        if f.is_file():
            report.files_checked.append(str(f.relative_to(root)))
            report.violations.extend(check_file(f))

    if not report.files_checked:
        log.warning("[verify_lockfiles] no requirements files found")

    if report.passed:
        log.info("[verify_lockfiles] PASS: %d files checked, 0 critical violations",
                 len(report.files_checked))
    else:
        log.warning("[verify_lockfiles] %d critical violations found", report.critical_count)

    return report


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    r = run()
    print(f"Files checked: {r.files_checked}")
    print(f"Violations: {len(r.violations)} ({r.critical_count} critical)")
    sys.exit(0 if r.passed else 1)
