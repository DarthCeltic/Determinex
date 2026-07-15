#!/usr/bin/env python3
"""PB senses guard — verifies no static-RE tool names appear in session WALs.

Usage:
    python scripts/pb_senses_guard.py              # scan sessions/, print violations
    python scripts/pb_senses_guard.py --guard       # exit 1 if any violations
    python scripts/pb_senses_guard.py --path <dir>  # scan a custom WAL directory
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_WAL_DIR = ROOT / "sessions"

# Mirrors _STATIC_RE_TOOLS in syscall_diff.py
_STATIC_RE_PATTERNS = re.compile(
    r"\b(objdump|readelf|r2\b|radare2|ghidra|ida64?\b|iaito|binaryninja|binary_ninja"
    r"|rizin|rz-bin|capstone|unicorn|angr|pwntool|pwndbg|peda|nm\b|strings\b)\b",
    re.IGNORECASE,
)


def scan_wal_file(path: Path) -> list[dict]:
    violations = []
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    # WAL files may be JSON or JSONL
    lines = content.splitlines()
    for lineno, line in enumerate(lines, 1):
        if not line.strip():
            continue
        m = _STATIC_RE_PATTERNS.search(line)
        if m:
            violations.append(
                {
                    "file": str(path),
                    "line": lineno,
                    "tool": m.group(0),
                    "context": line.strip()[:120],
                }
            )
    return violations


def scan_dir(wal_dir: Path) -> list[dict]:
    violations = []
    if not wal_dir.exists():
        return []
    for p in sorted(wal_dir.rglob("*.json")):
        violations.extend(scan_wal_file(p))
    for p in sorted(wal_dir.rglob("*.jsonl")):
        violations.extend(scan_wal_file(p))
    return violations


def main() -> None:
    guard_mode = "--guard" in sys.argv
    custom_path = None
    if "--path" in sys.argv:
        idx = sys.argv.index("--path")
        if idx + 1 < len(sys.argv):
            custom_path = Path(sys.argv[idx + 1])

    wal_dir = custom_path or DEFAULT_WAL_DIR
    print(f"Scanning WAL files in {wal_dir}...")
    violations = scan_dir(wal_dir)

    if violations:
        print(f"\nVIOLATION: {len(violations)} static-RE tool reference(s) found in WAL:")
        for v in violations:
            print(f"  [{v['tool']}] {v['file']}:{v['line']} — {v['context']}")
        if guard_mode:
            print("SENSES GUARD FAILED")
            sys.exit(1)
    else:
        print(f"OK: no static-RE tool references found in {wal_dir}.")


if __name__ == "__main__":
    main()
