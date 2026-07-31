"""
bundler/build_hive_sidecar.py — Compile determinex_hive.py → native sidecar binary

This is the "VS Code pattern": bundle your internal tooling as a pre-compiled
native executable inside the app installer. The user never needs Python installed.

Output: frontend/src-tauri/bin/determinex-hive-<target-triple>[.exe]

Tauri sidecar naming convention (REQUIRED):
  The binary MUST be named <name>-<rustc-target-triple>[.exe]
  Tauri resolves the correct binary at runtime based on the build target.

  Windows x64:  determinex-hive-x86_64-pc-windows-msvc.exe
  macOS ARM:    determinex-hive-aarch64-apple-darwin
  macOS Intel:  determinex-hive-x86_64-apple-darwin
  Linux x64:    determinex-hive-x86_64-unknown-linux-gnu

Usage:
  python bundler/build_hive_sidecar.py              # build for current platform
  python bundler/build_hive_sidecar.py --dry-run    # print plan, don't execute
  python bundler/build_hive_sidecar.py --verify     # check existing binary is valid
"""

import argparse
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------------
# PATHS
# ---------------------------------------------------------------------------

ROOT        = Path(__file__).parent.parent          # repo root
SCRIPTS_DIR = ROOT / "scripts"
HIVE_SCRIPT = SCRIPTS_DIR / "determinex_hive.py"
BIN_OUT_DIR = ROOT / "frontend" / "src-tauri" / "bin"
BUILD_TEMP  = ROOT / "bundler" / "_pyinstaller_work"
SIDECAR_BASENAME = "determinex-hive"


def _log(msg: str):
    print(f"[HiveSidecar] {msg}", flush=True)


# ---------------------------------------------------------------------------
# TARGET TRIPLE DETECTION
# ---------------------------------------------------------------------------

def current_target_triple() -> str:
    """Return the Rust target triple for the current machine."""
    system  = platform.system()
    machine = platform.machine().lower()

    if system == "Windows":
        return "x86_64-pc-windows-msvc"
    elif system == "Darwin":
        if machine in ("arm64", "aarch64"):
            return "aarch64-apple-darwin"
        return "x86_64-apple-darwin"
    elif system == "Linux":
        if machine in ("arm64", "aarch64"):
            return "aarch64-unknown-linux-gnu"
        return "x86_64-unknown-linux-gnu"
    else:
        raise RuntimeError(f"Unsupported platform: {system}/{machine}")


def sidecar_binary_name(triple: str) -> str:
    """Return the full sidecar filename Tauri expects."""
    if "windows" in triple:
        return f"{SIDECAR_BASENAME}-{triple}.exe"
    return f"{SIDECAR_BASENAME}-{triple}"


# ---------------------------------------------------------------------------
# BUILD
# ---------------------------------------------------------------------------

def check_pyinstaller() -> bool:
    """Return True if PyInstaller is importable."""
    try:
        import PyInstaller  # noqa: F401
        return True
    except ImportError:
        return False


def install_pyinstaller(dry_run: bool = False):
    _log("PyInstaller not found. Installing...")
    cmd = [sys.executable, "-m", "pip", "install", "pyinstaller", "-q"]
    _log(f"  $ {' '.join(cmd)}")
    if not dry_run:
        subprocess.check_call(cmd)
    _log("  PyInstaller installed.")


def build_sidecar(triple: str, dry_run: bool = False) -> Path:
    """
    Run PyInstaller to produce a single-file executable from determinex_hive.py.

    PyInstaller flags used:
      --onefile       Single executable (no dist/ folder with DLLs)
      --name          Output binary name without the triple suffix (added after)
      --distpath      Where to put the final binary
      --workpath      Temp build files (separate from dist)
      --specpath      .spec file location (temp)
      --noconfirm     Never prompt
      --clean         Clean PyInstaller cache before build
    """
    if not HIVE_SCRIPT.exists():
        raise FileNotFoundError(
            f"determinex_hive.py not found at {HIVE_SCRIPT}. "
            "Ensure the repo is fully checked out."
        )

    BIN_OUT_DIR.mkdir(parents=True, exist_ok=True)
    BUILD_TEMP.mkdir(parents=True, exist_ok=True)

    # PyInstaller names the output after --name, then we rename to add the triple.
    pyinstaller_name = SIDECAR_BASENAME
    dist_dir = BUILD_TEMP / "dist"
    work_dir = BUILD_TEMP / "work"
    spec_dir = BUILD_TEMP / "spec"

    cmd = [
        sys.executable, "-m", "PyInstaller",
        str(HIVE_SCRIPT),
        "--onefile",
        "--name",          pyinstaller_name,
        "--distpath",      str(dist_dir),
        "--workpath",      str(work_dir),
        "--specpath",      str(spec_dir),
        "--noconfirm",
        "--clean",
        # Add the repo root and scripts dir to the Python path so determinex_hive.py
        # can import any local modules it depends on
        "--paths",         str(ROOT),
        "--paths",         str(SCRIPTS_DIR),
        # Hidden imports that PyInstaller's static analysis may miss
        # The helper-dispatch modules (determinex_hive.cmd_helper). These are reached
        # via importlib.import_module, which PyInstaller's static analysis cannot see,
        # so without these the sidecar would expose `helper` and then fail at import --
        # and the desktop backend would silently fall back to the repo scripts that do
        # not exist in an installed copy, which is the whole reason `helper` was added.
        "--hidden-import", "determinex_agents",
        "--hidden-import", "determinex_agent_chat",
        "--hidden-import", "determinex_local_model_bench",
        "--hidden-import", "determinex_usage_ledger",
        "--hidden-import", "determinex_toolchain_installer",
        "--hidden-import", "determinex_corpus_api",
        # The provider registry, behind list_ai_providers. Added 2026-07-31 in the same pass as the
        # command itself -- and only because tests/test_router_bridge.py's allowlist guard caught it.
        # Without this the packaged app would list its 17 AI providers in a dev checkout and show an
        # empty picker once installed, which is precisely the dev-only-panel failure the `helper`
        # subcommand exists to prevent.
        "--hidden-import", "determinex_providers",
        "--hidden-import", "ide._tauri_driver",
        # cmd_helper reaches this via importlib, which PyInstaller cannot trace. Without the
        # hidden import the packaged sidecar would advertise the model installer and then
        # fail at import -- which matters more than usual here, since this is the command a
        # fresh install needs to become usable at all.
        "--hidden-import", "setup.install_determinex_models",
        # determinex_agents spawns determinex_local_agent as a separate process, so it
        # is not an import of anything above -- but the sidecar must still be able to
        # reach it, and swe_agent.* is what it imports.
        "--hidden-import", "determinex_local_agent",
        "--hidden-import", "litellm",
        "--hidden-import", "rich",
        "--hidden-import", "dotenv",
        "--hidden-import", "tiktoken_ext",
        "--hidden-import", "tiktoken_ext.openai_public",
        "--collect-data", "litellm",
        # OUR litellm_config.yaml, which is a different thing from litellm's own package data above.
        # It is the alias map: without it `determinex/engineer` resolves to ITSELF, and `determinex/`
        # is not a provider litellm knows -- so on a shipped build the hive loop could not call any
        # model at all. It was bundled by neither path (absent from bundle.resources AND from here),
        # and `_ROOT` in a PyInstaller sidecar is a temp extraction dir, so the one location the
        # loader checked never held it. Measured 2026-07-30: 0 alias entries, every role alias
        # unusable. `hive.api_client._alias_config_candidates` now searches sys._MEIPASS too, which
        # is where this lands.
        "--add-data", f"{ROOT / 'litellm_config.yaml'}{os.pathsep}.",
        # Exclude the heavyweight ML stack — the sidecar calls Ollama via HTTP,
        # not torch directly. Excluding these reduces binary size by ~2GB.
        # determinex_rosetta / determinex_inference import torch but they are optional
        # (wrapped in try/except in determinex_hive.py lines 72-81).
        # llama_cpp is excluded for the same reason torch is: this sidecar drives
        # models over HTTP (Ollama / LiteLLM), never in-process. It was NOT
        # excluded before, so PyInstaller bundled the Python package without its
        # native lib/ directory and the binary crashed at import with
        # FileNotFoundError before printing a single line -- the shipped engine
        # could not start at all. Local GGUF inference is a separate concern,
        # served by the embedded sidecar in src-tauri/src/sidecar.rs.
        "--exclude-module", "llama_cpp",
        "--exclude-module", "torch",
        "--exclude-module", "torchvision",
        "--exclude-module", "torchaudio",
        "--exclude-module", "tensorflow",
        "--exclude-module", "bitsandbytes",
        "--exclude-module", "transformers",
        "--exclude-module", "fastembed",
        "--exclude-module", "onnxruntime",
        "--exclude-module", "scipy",
        "--exclude-module", "sklearn",
        "--exclude-module", "matplotlib",
        "--exclude-module", "PIL",
        "--exclude-module", "cv2",
        "--exclude-module", "pandas",
    ]

    _log(f"Building sidecar binary for {triple}...")
    _log(f"  Source:  {HIVE_SCRIPT}")
    _log(f"  Output:  {BIN_OUT_DIR / sidecar_binary_name(triple)}")
    _log(f"  $ {' '.join(cmd)}")

    if not dry_run:
        result = subprocess.run(cmd, cwd=str(ROOT))
        if result.returncode != 0:
            raise RuntimeError(
                f"PyInstaller failed with exit code {result.returncode}. "
                "See output above for details."
            )

    # The PyInstaller output is named just "determinex-hive[.exe]"
    # Rename it to include the target triple (Tauri requirement)
    suffix = ".exe" if "windows" in triple else ""
    src_bin = dist_dir / f"{SIDECAR_BASENAME}{suffix}"
    dst_bin = BIN_OUT_DIR / sidecar_binary_name(triple)

    _log(f"Renaming {src_bin.name} → {dst_bin.name}")
    if not dry_run:
        if not src_bin.exists():
            raise FileNotFoundError(
                f"PyInstaller output not found at {src_bin}. Build may have failed."
            )
        shutil.copy2(src_bin, dst_bin)
        _log(f"  Binary size: {dst_bin.stat().st_size / 1024 / 1024:.1f} MB")

    return dst_bin


# ---------------------------------------------------------------------------
# VERIFY
# ---------------------------------------------------------------------------

def verify_sidecar(triple: str) -> bool:
    """Smoke-test the sidecar binary by running it with --help."""
    dst_bin = BIN_OUT_DIR / sidecar_binary_name(triple)

    if not dst_bin.exists():
        _log(f"FAIL: binary not found at {dst_bin}")
        return False

    _log(f"Verifying {dst_bin.name}...")
    result = subprocess.run(
        [str(dst_bin), "--help"],
        capture_output=True,
        text=True,
        timeout=90,  # onefile mode extracts to %TEMP% on first run (~30-60s)
    )
    combined = result.stdout + result.stderr

    # This check used to accept a CRASH as success. On a non-zero exit it did:
    #
    #     if result.stdout or result.stderr:
    #         _log("  Sidecar binary OK (responded to --help)")
    #         return True
    #
    # A fatal traceback IS output, so a binary that died on import "responded"
    # and was declared OK. Measured 2026-07-28: the shipped
    # determinex-hive.exe crashed with FileNotFoundError before printing one
    # useful line, and this function reported "Sidecar binary OK". Worse,
    # frontend/package.json's `pretauri` runs `--verify || build`, so a green
    # verify SKIPS the rebuild -- the broken engine shipped BECAUSE this passed.
    #
    # A verifier that a crash satisfies is worse than no verifier: the clean run
    # gets read as proof.
    # Only genuinely FATAL markers. The first version of this list also included
    # "ModuleNotFoundError" / "ImportError" / "FileNotFoundError", which matched
    # the optional-component guard's own success message -- "Phase 2 Latent Bridge
    # components unavailable (ModuleNotFoundError: No module named 'torch') --
    # continuing" is the guard WORKING, and this rejected the binary for saying so.
    # An over-eager verifier is its own failure mode: it just fails in the safe
    # direction instead of the dangerous one.
    #
    # PyInstaller always emits both of these on an unhandled exception, so they are
    # sufficient to catch a real crash.
    fatal_markers = (
        "Traceback (most recent call last)",
        "Failed to execute script",
    )
    hit = next((m for m in fatal_markers if m in combined), None)
    if hit:
        _log(f"  FAIL: binary crashed on --help ({hit})")
        for line in combined.strip().splitlines()[-6:]:
            _log(f"    {line}")
        return False

    # determinex_hive.py uses argparse, so --help exits 0. Anything else is a
    # failure, full stop.
    if result.returncode != 0:
        _log(f"  FAIL: --help exited {result.returncode}")
        for line in combined.strip().splitlines()[-6:]:
            _log(f"    {line}")
        return False

    # And it has to look like THIS CLI's help, not merely be non-empty -- a
    # binary that prints anything at all should not pass a smoke test.
    if "usage:" not in combined.lower():
        _log("  FAIL: --help produced no usage text; this is not the hive CLI")
        return False

    _log("  Sidecar binary OK (--help exited 0 and printed usage)")
    return True


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Build the Determinex Hive sidecar binary")
    parser.add_argument("--dry-run", action="store_true", help="Print plan, don't build")
    parser.add_argument("--verify",  action="store_true", help="Verify existing binary only")
    parser.add_argument("--triple",  default=None,        help="Override target triple")
    args = parser.parse_args()

    triple = args.triple or current_target_triple()
    _log(f"Target triple: {triple}")

    if args.verify:
        ok = verify_sidecar(triple)
        sys.exit(0 if ok else 1)

    if not check_pyinstaller():
        install_pyinstaller(dry_run=args.dry_run)

    dst = build_sidecar(triple, dry_run=args.dry_run)

    if not args.dry_run:
        ok = verify_sidecar(triple)
        if ok:
            _log(f"\n✅ Sidecar ready: {dst}")
            _log("   Next step: npx tauri build")
        else:
            _log("\n❌ Sidecar build succeeded but verification failed.")
            sys.exit(1)
    else:
        _log("\n[DRY-RUN] No files written.")


if __name__ == "__main__":
    main()
