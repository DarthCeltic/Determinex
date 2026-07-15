"""
bundler/setup_sidecar.py — Determinex Embedded Python Sidecar Setup

Creates a self-contained Python runtime in bundler/sidecar/python/ that:
  - Does NOT require Python to be installed on the target system
  - Contains only the packages needed for GGUF inference (llama-cpp-python + numpy)
  - Is spawnable by the Tauri Rust backend via std::process::Command
  - Is small enough to ship alongside the Tauri installer (~250-400MB with CUDA wheels)

This is the "zero-dependency execution model" — a vibe coder who has never
touched a terminal can run Determinex by clicking the .exe installer.

Architecture:
  bundler/
    sidecar/
      python/               ← python-3.11.x-embed-amd64 (the embedded distribution)
        python.exe          ← the interpreter Tauri spawns
        python311._pth      ← patched to enable site-packages
        Lib/
          site-packages/    ← llama-cpp-python, numpy installed here
      determinex_sidecar.py    ← the NDJSON server (copied here at setup time)

Tauri spawn call (from orchestrator.rs / sidecar.rs):
  std::process::Command::new("bundler/sidecar/python/python.exe")
      .arg("bundler/sidecar/determinex_sidecar.py")
      .stdin(Stdio::piped())
      .stdout(Stdio::piped())

Requirements for this setup script:
  - Windows x64 (target: user's machine)
  - Internet connection for one-time download (~10MB Python + ~200MB wheel)
  - The hardware_profiler must have already written determinex_hardware_profile.json
    (so we know which CUDA wheel to install — run 'python scripts/hardware_profiler.py' first)

Usage:
  python bundler/setup_sidecar.py
  python bundler/setup_sidecar.py --force     # re-create even if sidecar exists
  python bundler/setup_sidecar.py --verify    # only verify existing sidecar
  python bundler/setup_sidecar.py --dry-run   # print what would happen, don't do it
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------

PYTHON_VERSION      = "3.11.9"
PYTHON_VERSION_NODOT = "311"
PYTHON_EMBED_URL    = (
    f"https://www.python.org/ftp/python/{PYTHON_VERSION}/"
    f"python-{PYTHON_VERSION}-embed-amd64.zip"
)
GET_PIP_URL         = "https://bootstrap.pypa.io/get-pip.py"

SIDECAR_DIR         = Path(__file__).parent / "sidecar"
PYTHON_DIR          = SIDECAR_DIR / "python"
SIDECAR_SCRIPT_SRC  = Path(__file__).parent / "determinex_sidecar.py"
SIDECAR_SCRIPT_DEST = SIDECAR_DIR / "determinex_sidecar.py"

PROFILE_CACHE       = Path(__file__).parent.parent / "determinex_hardware_profile.json"

# Minimum packages for the inference sidecar (NOT the training stack)
_SIDECAR_BASE_PACKAGES = ["numpy"]
_LLAMA_CPP_VERSION     = "0.3.4"

# Wheel index map (from hardware_profiler.py)
_CUDA_WHEEL_INDEX = {
    "12.5": "https://abetlen.github.io/llama-cpp-python/whl/cu125",
    "12.4": "https://abetlen.github.io/llama-cpp-python/whl/cu124",
    "12.3": "https://abetlen.github.io/llama-cpp-python/whl/cu123",
    "12.2": "https://abetlen.github.io/llama-cpp-python/whl/cu122",
    "12.1": "https://abetlen.github.io/llama-cpp-python/whl/cu121",
    "11.8": "https://abetlen.github.io/llama-cpp-python/whl/cu118",
    "11.7": "https://abetlen.github.io/llama-cpp-python/whl/cu117",
}
_METAL_INDEX  = "https://abetlen.github.io/llama-cpp-python/whl/metal"
_CPU_INDEX    = "https://abetlen.github.io/llama-cpp-python/whl/cpu"


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def _log(msg: str, indent: int = 0):
    prefix = "  " * indent
    print(f"[Bundler] {prefix}{msg}", flush=True)


def _download(url: str, dest: Path, label: str = "", dry_run: bool = False) -> Path:
    """Download url → dest with progress logging."""
    if dry_run:
        _log(f"DRY-RUN: would download {url} → {dest}")
        return dest

    dest.parent.mkdir(parents=True, exist_ok=True)
    _log(f"Downloading {label or url} ...")

    req = Request(url, headers={"User-Agent": "Determinex-Bundler/1.0"})
    with tempfile.NamedTemporaryFile(dir=dest.parent, suffix=".tmp", delete=False) as tmp:
        tmp_path = Path(tmp.name)
        try:
            with urlopen(req, timeout=120) as resp:
                total = int(resp.headers.get("Content-Length", 0))
                downloaded = 0
                while True:
                    chunk = resp.read(65536)
                    if not chunk:
                        break
                    tmp.write(chunk)
                    downloaded += len(chunk)
                    if total:
                        pct = downloaded * 100 // total
                        print(f"\r  {pct:3d}%  {downloaded//1024//1024} MB / {total//1024//1024} MB", end="", flush=True)
            print()
        except Exception:
            tmp_path.unlink(missing_ok=True)
            raise

    tmp_path.rename(dest)
    size_mb = dest.stat().st_size / 1024 / 1024
    _log(f"  → {dest} ({size_mb:.1f} MB)", indent=1)
    return dest


def _run_sidecar_python(args: list[str], dry_run: bool = False, **kwargs) -> int:
    """Run a command using the sidecar's python.exe."""
    python_exe = PYTHON_DIR / "python.exe"
    cmd = [str(python_exe)] + args
    _log(f"  $ {' '.join(str(a) for a in cmd)}", indent=1)
    if dry_run:
        return 0
    result = subprocess.run(cmd, **kwargs)
    return result.returncode


def _detect_wheel_index() -> str:
    """Read hardware profile and select the correct wheel index URL."""
    if PROFILE_CACHE.exists():
        try:
            profile = json.loads(PROFILE_CACHE.read_text())
            vendor  = profile.get("gpu", {}).get("vendor", "")
            cuda_v  = profile.get("gpu", {}).get("cuda_version", "")
            metal   = profile.get("gpu", {}).get("metal_supported", False)

            if vendor == "nvidia" and cuda_v:
                major_minor = ".".join(cuda_v.split(".")[:2])
                url = _CUDA_WHEEL_INDEX.get(major_minor)
                if url is None:
                    # Round down to the closest known version
                    for v in sorted(_CUDA_WHEEL_INDEX.keys(), reverse=True):
                        if float(v) <= float(major_minor):
                            url = _CUDA_WHEEL_INDEX[v]
                            _log(f"CUDA {major_minor} not in index — using {v} wheel", indent=1)
                            break
                if url:
                    _log(f"Detected CUDA {major_minor} → wheel index: {url}", indent=1)
                    return url

            if metal:
                _log("Detected Apple Metal → Metal wheel index", indent=1)
                return _METAL_INDEX

        except Exception as e:
            _log(f"Could not parse hardware profile: {e} — falling back to CPU wheel", indent=1)

    _log("No GPU profile found — CPU wheel (run hardware_profiler.py first for GPU acceleration)", indent=1)
    return _CPU_INDEX


# ---------------------------------------------------------------------------
# SETUP STEPS
# ---------------------------------------------------------------------------

def step_download_embed(dry_run: bool = False):
    """Step 1: Download and extract python-embed-amd64.zip."""
    _log("Step 1: Downloading Python embeddable distribution...")
    zip_path = SIDECAR_DIR / f"python-{PYTHON_VERSION}-embed-amd64.zip"

    if zip_path.exists():
        _log(f"  Already downloaded: {zip_path}", indent=1)
    else:
        _download(PYTHON_EMBED_URL, zip_path, f"Python {PYTHON_VERSION} embed", dry_run)

    if not dry_run:
        _log(f"  Extracting to {PYTHON_DIR}...", indent=1)
        PYTHON_DIR.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(PYTHON_DIR)
        _log(f"  Extracted: {len(list(PYTHON_DIR.iterdir()))} files", indent=1)
    else:
        _log(f"  DRY-RUN: would extract to {PYTHON_DIR}", indent=1)


def step_patch_pth(dry_run: bool = False):
    """
    Step 2: Patch python311._pth to enable site-packages.

    By default, the embedded distribution has:
        python311.zip
        .
        #import site    ← commented out

    pip and third-party packages won't work until `import site` is active
    and the Lib/site-packages directory is in sys.path.
    """
    _log("Step 2: Patching python._pth to enable site-packages...")
    pth_file = PYTHON_DIR / f"python{PYTHON_VERSION_NODOT}._pth"

    if not pth_file.exists() and not dry_run:
        raise FileNotFoundError(f"Expected {pth_file} — is the embed zip corrupted?")

    new_content = (
        f"python{PYTHON_VERSION_NODOT}.zip\n"
        ".\n"
        "Lib\\site-packages\n"
        "\n"
        "# Uncommented by Determinex bundler setup — required for pip and third-party packages\n"
        "import site\n"
    )

    if dry_run:
        _log(f"  DRY-RUN: would write {pth_file}:", indent=1)
        print(new_content)
        return

    pth_file.write_text(new_content)
    _log(f"  Patched: {pth_file}", indent=1)


def step_bootstrap_pip(dry_run: bool = False):
    """Step 3: Bootstrap pip into the embedded distribution via get-pip.py."""
    _log("Step 3: Bootstrapping pip...")

    get_pip = SIDECAR_DIR / "get-pip.py"
    if not get_pip.exists():
        _download(GET_PIP_URL, get_pip, "get-pip.py", dry_run)

    # Create Lib/site-packages so pip has somewhere to install
    if not dry_run:
        (PYTHON_DIR / "Lib" / "site-packages").mkdir(parents=True, exist_ok=True)

    rc = _run_sidecar_python(
        [str(get_pip), "--no-warn-script-location"],
        dry_run=dry_run,
        cwd=str(PYTHON_DIR),
    )
    if rc != 0 and not dry_run:
        raise RuntimeError(f"pip bootstrap failed (exit {rc})")
    _log("  pip bootstrapped OK", indent=1)


def step_install_packages(dry_run: bool = False):
    """Step 4: Install llama-cpp-python (correct wheel) + numpy into the sidecar."""
    _log("Step 4: Detecting GPU and installing packages...")
    wheel_index = _detect_wheel_index()

    # Install base packages first
    for pkg in _SIDECAR_BASE_PACKAGES:
        _log(f"  Installing {pkg}...", indent=1)
        _run_sidecar_python(
            ["-m", "pip", "install", pkg, "--no-warn-script-location", "-q"],
            dry_run=dry_run,
        )

    # Install llama-cpp-python from the correct prebuilt wheel
    llama_pkg = f"llama-cpp-python=={_LLAMA_CPP_VERSION}"
    _log(f"  Installing {llama_pkg} from {wheel_index}...", indent=1)
    rc = _run_sidecar_python(
        ["-m", "pip", "install", llama_pkg,
         "--extra-index-url", wheel_index,
         "--no-warn-script-location", "-q"],
        dry_run=dry_run,
    )
    if rc != 0 and not dry_run:
        _log("  WARNING: GPU wheel install failed — retrying with CPU wheel", indent=1)
        rc = _run_sidecar_python(
            ["-m", "pip", "install", llama_pkg,
             "--extra-index-url", _CPU_INDEX,
             "--no-warn-script-location", "-q"],
            dry_run=dry_run,
        )
        if rc != 0 and not dry_run:
            raise RuntimeError("llama-cpp-python install failed on both GPU and CPU paths")

    _log("  Packages installed OK", indent=1)


def step_copy_sidecar_script(dry_run: bool = False):
    """Step 5: Copy determinex_sidecar.py into the sidecar directory."""
    _log("Step 5: Installing Determinex sidecar server script...")
    if not SIDECAR_SCRIPT_SRC.exists():
        raise FileNotFoundError(
            f"determinex_sidecar.py not found at {SIDECAR_SCRIPT_SRC}. "
            "Build it first with: python bundler/setup_sidecar.py"
        )
    if not dry_run:
        shutil.copy2(SIDECAR_SCRIPT_SRC, SIDECAR_SCRIPT_DEST)
    _log(f"  Copied: {SIDECAR_SCRIPT_SRC} → {SIDECAR_SCRIPT_DEST}", indent=1)


def step_verify(dry_run: bool = False) -> bool:
    """Step 6: Verify the sidecar works."""
    _log("Step 6: Verifying sidecar...")
    verify_script = "from llama_cpp import Llama; print('llama_cpp OK')"
    rc = _run_sidecar_python(
        ["-c", verify_script],
        dry_run=dry_run,
        timeout=30,
    )
    if rc != 0 and not dry_run:
        _log("  FAIL: llama_cpp could not be imported", indent=1)
        return False

    numpy_script = "import numpy; print(f'numpy {numpy.__version__} OK')"
    _run_sidecar_python(["-c", numpy_script], dry_run=dry_run)

    _log("  Sidecar verified — ready for Tauri spawn", indent=1)
    return True


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def setup(force: bool = False, dry_run: bool = False):
    _log(f"=== Determinex Sidecar Setup (Python {PYTHON_VERSION}-embed-amd64) ===")
    _log(f"    Target dir: {SIDECAR_DIR}")
    if dry_run:
        _log("    MODE: DRY-RUN (nothing will be written)")

    if PYTHON_DIR.exists() and not force:
        _log(f"  Sidecar already exists at {PYTHON_DIR}. Use --force to rebuild.")
        return step_verify(dry_run)

    if PYTHON_DIR.exists() and force and not dry_run:
        _log(f"  --force: removing existing sidecar...")
        shutil.rmtree(PYTHON_DIR)

    SIDECAR_DIR.mkdir(parents=True, exist_ok=True)

    step_download_embed(dry_run)
    step_patch_pth(dry_run)
    step_bootstrap_pip(dry_run)
    step_install_packages(dry_run)
    step_copy_sidecar_script(dry_run)
    ok = step_verify(dry_run)

    if ok or dry_run:
        _log("\n=== Sidecar setup complete. ===")
        _log(f"  Spawn with: {PYTHON_DIR / 'python.exe'} {SIDECAR_SCRIPT_DEST}")
        _log(f"  Protocol:   NDJSON on stdin/stdout")
        _log(f"  Test:       python bundler/setup_sidecar.py --verify")
    else:
        _log("\n=== Sidecar setup FAILED. See errors above. ===")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Determinex embedded Python sidecar setup")
    parser.add_argument("--force",   action="store_true", help="Rebuild even if sidecar exists")
    parser.add_argument("--verify",  action="store_true", help="Only verify existing sidecar")
    parser.add_argument("--dry-run", action="store_true", help="Print plan, don't execute")
    args = parser.parse_args()

    if args.verify:
        ok = step_verify()
        sys.exit(0 if ok else 1)
    else:
        setup(force=args.force, dry_run=args.dry_run)
