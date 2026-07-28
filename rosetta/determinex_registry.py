"""
rosetta/determinex_registry.py — Dynamic Rosetta Stone Registry Client

On Determinex startup, this module pings the remote registry.json manifest,
compares remote family versions against locally cached versions, and
transparently downloads + installs any new or updated family weight files.

This is the "package manager" mechanism for the Rosetta Stone protocol.
New community-contributed architectures (e.g., Llama-4, Qwen-3) appear in
registry.json after PR merge and are pulled automatically by all Determinex clients
without requiring users to retrain or reinstall.

Design invariants:
    - FAIL SAFE: if the registry ping fails for any reason (no internet,
      timeout, bad JSON), local weights are used unchanged. No crash.
    - ATOMIC: weight files are downloaded to a temp path, sha256-verified,
      then renamed into place. Partial downloads never corrupt local state.
    - NON-BLOCKING: registry check has a 5-second timeout. Runs on startup
      in a background thread so it never delays the user's first interaction.
    - AIR-GAP SAFE: DETERMINEX_OFFLINE=1 env var disables all network calls.
      Enterprise / air-gapped deployments set this and never phone home.

Usage:
    from rosetta.determinex_registry import RegistryClient

    client = RegistryClient(local_dir="registry/weights")
    updated = client.sync(stone)   # stone: RosettaStone instance
    # updated: list of family names that were downloaded and merged
"""

import hashlib
import json
import os
import sys
import tempfile
import time
from pathlib import Path
from typing import Optional
from urllib.request import urlopen, Request
from urllib.error import URLError

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------

REGISTRY_URL = os.environ.get(
    "DETERMINEX_REGISTRY_URL",
    "https://raw.githubusercontent.com/determinex-ai/determinex/main/registry/registry.json",
)

LOCAL_VERSIONS_FILE = "registry_local_versions.json"
TIMEOUT_SECONDS     = 5
_OFFLINE            = os.environ.get("DETERMINEX_OFFLINE", "").strip().lower() in ("1", "true", "yes")


# ---------------------------------------------------------------------------
# REGISTRY CLIENT
# ---------------------------------------------------------------------------

class RegistryClient:
    """
    Manages the lifecycle of Rosetta Stone family weight files.

    Responsibilities:
        1. Fetch remote registry.json
        2. Compare remote family versions with local cache
        3. Download new/updated family weight files
        4. sha256-verify before installing
        5. Call stone.load_family_extension() to activate new families
        6. Update local version cache
    """

    def __init__(
        self,
        local_dir:    str | Path = "registry/weights",
        registry_url: str = REGISTRY_URL,
        timeout:      int = TIMEOUT_SECONDS,
    ):
        self.local_dir    = Path(local_dir)
        self.registry_url = registry_url
        self.timeout      = timeout
        self.local_dir.mkdir(parents=True, exist_ok=True)
        self._versions_path = self.local_dir / LOCAL_VERSIONS_FILE

    # ── Remote ───────────────────────────────────────────────────────────────

    def fetch_remote_manifest(self) -> Optional[dict]:
        """
        Fetch registry.json from the remote URL.
        Returns None on any network error (fail-safe).
        """
        if _OFFLINE:
            print("[Registry] DETERMINEX_OFFLINE=1 — skipping registry check.", flush=True)
            return None
        try:
            req = Request(
                self.registry_url,
                headers={"User-Agent": "Determinex/1.0 RegistryClient"},
            )
            with urlopen(req, timeout=self.timeout) as resp:
                raw = resp.read().decode("utf-8")
            manifest = json.loads(raw)
            print(
                f"[Registry] Fetched manifest v{manifest.get('registry_version', '?')} "
                f"({len(manifest.get('families', {}))} families)",
                flush=True
            )
            return manifest
        except URLError as e:
            print(f"[Registry] Network unreachable: {e}. Using local weights.", flush=True)
            return None
        except json.JSONDecodeError as e:
            print(f"[Registry] Bad manifest JSON: {e}. Using local weights.", flush=True)
            return None
        except Exception as e:
            print(f"[Registry] Unexpected error: {e}. Using local weights.", flush=True)
            return None

    # ── Local version cache ───────────────────────────────────────────────────

    def load_local_versions(self) -> dict:
        """Load the locally cached family → version mapping."""
        if self._versions_path.exists():
            try:
                return json.loads(self._versions_path.read_text())
            except Exception:
                pass
        return {}

    def save_local_versions(self, versions: dict):
        """Persist updated local version mapping."""
        self._versions_path.write_text(json.dumps(versions, indent=2))

    # ── Download + verify ─────────────────────────────────────────────────────

    def _sha256_file(self, path: Path) -> str:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()

    def download_family(self, family: str, entry: dict) -> Optional[Path]:
        """
        Download a family weight file with sha256 verification.

        Returns:
            Path to the downloaded file, or None on failure.
        """
        url    = entry.get("url", "")
        sha256 = entry.get("sha256", "")
        if not url:
            print(f"[Registry] No URL for family '{family}' — skipping.", flush=True)
            return None

        dest = self.local_dir / f"family_{family}.pt"

        # Download to temp file, verify, rename atomically
        try:
            print(f"[Registry] Downloading '{family}' from {url}...", flush=True)
            t0  = time.time()
            req = Request(url, headers={"User-Agent": "Determinex/1.0 RegistryClient"})
            with tempfile.NamedTemporaryFile(
                dir=self.local_dir, suffix=".tmp", delete=False
            ) as tmp:
                tmp_path = Path(tmp.name)
                with urlopen(req, timeout=60) as resp:
                    while True:
                        chunk = resp.read(65536)
                        if not chunk:
                            break
                        tmp.write(chunk)

            # Verify sha256 (skip if placeholder)
            if sha256 and not sha256.startswith("PLACEHOLDER"):
                actual = self._sha256_file(tmp_path)
                if actual != sha256:
                    tmp_path.unlink(missing_ok=True)
                    print(
                        f"[Registry] sha256 MISMATCH for '{family}': "
                        f"expected={sha256[:16]}… got={actual[:16]}…",
                        flush=True
                    )
                    return None
                print(f"[Registry] sha256 verified for '{family}'.", flush=True)
            else:
                print(
                    f"[Registry] WARNING: No sha256 in manifest for '{family}'. "
                    f"Skipping verification (unsafe for production).",
                    flush=True
                )

            tmp_path.rename(dest)
            elapsed = time.time() - t0
            size_kb = dest.stat().st_size / 1024
            print(
                f"[Registry] '{family}' downloaded: {size_kb:.1f} KB in {elapsed:.1f}s → {dest}",
                flush=True
            )
            return dest

        except Exception as e:
            print(f"[Registry] Download failed for '{family}': {e}", flush=True)
            if "tmp_path" in locals():
                tmp_path.unlink(missing_ok=True)
            return None

    # ── Main sync ─────────────────────────────────────────────────────────────

    def sync(self, stone=None) -> list[str]:
        """
        Check remote registry, download new/updated families, merge into stone.

        Args:
            stone: a RosettaStone instance (or None to skip loading).
                   If provided, new families are activated via load_family_extension().

        Returns:
            List of family names that were downloaded and activated this sync.
        """
        manifest = self.fetch_remote_manifest()
        if manifest is None:
            return []

        local_versions  = self.load_local_versions()
        remote_families = manifest.get("families", {})
        updated         = []

        for family, entry in remote_families.items():
            remote_ver = entry.get("version", 0)
            local_ver  = local_versions.get(family, {}).get("version", 0)

            if remote_ver <= local_ver:
                continue  # Already up to date

            weight_path = self.local_dir / f"family_{family}.pt"
            if weight_path.exists() and local_ver > 0:
                print(
                    f"[Registry] Update available: '{family}' v{local_ver} → v{remote_ver}",
                    flush=True
                )
            else:
                print(
                    f"[Registry] New family available: '{family}' v{remote_ver}",
                    flush=True
                )

            dl_path = self.download_family(family, entry)
            if dl_path is None:
                continue

            # Activate in stone if provided
            if stone is not None:
                try:
                    stone.load_family_extension(dl_path)
                    print(f"[Registry] '{family}' activated in RosettaStone.", flush=True)
                except Exception as e:
                    print(f"[Registry] Failed to activate '{family}': {e}", flush=True)
                    continue

            # Mark as updated locally
            local_versions[family] = {
                "version":    remote_ver,
                "sha256":     entry.get("sha256", ""),
                "family_dim": entry.get("family_dim", 0),
                "updated_at": time.time(),
            }
            self.save_local_versions(local_versions)
            updated.append(family)

        if updated:
            print(f"[Registry] Sync complete. Updated families: {updated}", flush=True)
        else:
            print("[Registry] All families up to date.", flush=True)

        return updated

    def list_local(self) -> dict:
        """Return the locally cached family version map."""
        return self.load_local_versions()

    def status(self) -> dict:
        """Return registry status dict for diagnostics/UI display."""
        local = self.load_local_versions()
        weight_files = list(self.local_dir.glob("family_*.pt"))
        return {
            "local_dir":      str(self.local_dir),
            "registry_url":   self.registry_url,
            "offline_mode":   _OFFLINE,
            "local_families": list(local.keys()),
            "local_versions": {k: v.get("version") for k, v in local.items()},
            "weight_files":   [f.name for f in weight_files],
        }


# ---------------------------------------------------------------------------
# STARTUP HELPER (call from determinex_hive.py or main entry point)
# ---------------------------------------------------------------------------

def startup_sync(
    stone,
    local_dir:    str | Path = "registry/weights",
    registry_url: str        = REGISTRY_URL,
    background:   bool       = True,
) -> list[str]:
    """
    Run a registry sync on Determinex startup.

    If background=True, runs in a daemon thread so it never delays the UI.
    Returns immediately (empty list); any updates are applied asynchronously.

    If background=False, runs synchronously and returns list of updated families.

    Usage in determinex_hive.py:
        from rosetta.determinex_registry import startup_sync
        startup_sync(rosetta_stone, background=True)
    """
    client = RegistryClient(local_dir=local_dir, registry_url=registry_url)

    if not background:
        return client.sync(stone)

    import threading
    def _run():
        try:
            client.sync(stone)
        except Exception as e:
            print(f"[Registry] Background sync error: {e}", flush=True)

    t = threading.Thread(target=_run, daemon=True, name="determinex-registry-sync")
    t.start()
    return []


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Determinex Rosetta Registry Client")
    parser.add_argument("--status",  action="store_true", help="Show local registry status")
    parser.add_argument("--sync",    action="store_true", help="Sync with remote registry (no stone load)")
    parser.add_argument("--offline", action="store_true", help="Force offline mode for this run")
    args = parser.parse_args()

    if args.offline:
        os.environ["DETERMINEX_OFFLINE"] = "1"

    client = RegistryClient()

    if args.status:
        print(json.dumps(client.status(), indent=2))
    elif args.sync:
        updated = client.sync(stone=None)
        print(f"Updated: {updated or 'none'}")
    else:
        parser.print_help()
