"""
bundler/ensure_vc_redist.py — Fetch the Microsoft VC++ Redistributable for Windows Tauri builds

tauri-build checks for frontend/src-tauri/resources/vc_redist.x64.exe at build time on
Windows targets, regardless of whether tauri.conf.json's `resources` list mentions it.
It's a ~25MB third-party Microsoft installer -- never committed to git (see .gitignore) --
so a fresh clone is missing it and `cargo build`/`tauri dev` fails immediately with:
    resource path `resources\vc_redist.x64.exe` doesn't exist

No-op on non-Windows targets (the file is Windows-specific; other platforms don't need it).

Usage:
  python bundler/ensure_vc_redist.py              # fetch only if missing
  python bundler/ensure_vc_redist.py --verify      # check only, don't fetch
"""
import argparse
import platform
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
DST = ROOT / "frontend" / "src-tauri" / "resources" / "vc_redist.x64.exe"
URL = "https://aka.ms/vs/17/release/vc_redist.x64.exe"
MIN_SIZE_BYTES = 5_000_000  # the real installer is ~25MB; guard against a truncated/error fetch


def _log(msg: str) -> None:
    print(f"[VCRedist] {msg}", flush=True)


def _looks_valid(path: Path) -> bool:
    return path.is_file() and path.stat().st_size > MIN_SIZE_BYTES


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="Check only, don't fetch")
    args = parser.parse_args()

    if platform.system() != "Windows":
        _log("non-Windows platform, nothing to do")
        return 0

    if _looks_valid(DST):
        _log(f"OK: {DST} already present ({DST.stat().st_size:,} bytes)")
        return 0

    if args.verify:
        _log(f"FAIL: {DST} missing or too small")
        return 1

    _log(f"Fetching {URL} -> {DST}")
    DST.parent.mkdir(parents=True, exist_ok=True)
    try:
        urllib.request.urlretrieve(URL, DST)
    except Exception as e:
        _log(f"FAIL: download error: {e}")
        return 1

    if not _looks_valid(DST):
        _log(f"FAIL: downloaded file looks truncated/invalid ({DST.stat().st_size if DST.exists() else 0} bytes)")
        return 1

    _log(f"OK: fetched {DST.stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
