"""Repository license scan wrapper for assurance artifacts."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from corpus.code_ingest.license_detector import detect


DEFAULT_OUT = ROOT / "assurance" / "licenses" / "license_inventory.json"


def scan(paths: list[Path]) -> dict:
    rows = []
    for path in paths:
        result = detect(path)
        rows.append({
            "path": str(path),
            "spdx_id": result.spdx_id,
            "bucket": result.bucket,
            "ingest_allowed": result.ingest_allowed,
            "source": result.source,
            "confidence": result.confidence,
        })
    return {
        "schema_version": "determinex-license-inventory-v1",
        "rows": rows,
        "blocked_count": sum(1 for row in rows if not row["ingest_allowed"]),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, default=[ROOT])
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    report = scan(args.paths)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.out)
    print(json.dumps({"blocked_count": report["blocked_count"], "rows": len(report["rows"])}, indent=2))
    return 0 if report["blocked_count"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
