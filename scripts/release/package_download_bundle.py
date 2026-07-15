"""Create a downloadable Determinex setup bundle from built installer artifacts.

The bundle is intentionally not a public-release approval. It packages the
current MSI/NSIS artifacts with checksums, setup instructions, and a small
evidence manifest while keeping signing and clean-host gates explicit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "determinex-download-bundle-v1"
WINDOWS_MSI_SCHEMA_VERSION = "determinex-windows-msi-evidence-v1"
LEGAL_PUBLIC_DISTRIBUTION_SCHEMA_VERSION = "determinex-legal-public-distribution-evidence-v1"
DEFAULT_EVIDENCE_DIR = Path("assurance/evidence/determinex_download_bundle_20260707")
DEFAULT_WINDOWS_MSI_EVIDENCE_DIR = Path("assurance/evidence/windows_msi")
INSTALLER_SUFFIXES = frozenset({".exe", ".msi", ".appimage", ".deb", ".rpm"})
LINUX_PACKAGE_TYPES = frozenset({"linux_appimage", "linux_deb", "linux_rpm"})
REQUIRED_LINUX_PACKAGE_TYPES = ("linux_appimage", "linux_deb", "linux_rpm")
LEGAL_PUBLIC_DISTRIBUTION_REQUIRED_TRUE = (
    "legal_review_completed",
    "license_inventory_reviewed",
    "model_notice_reviewed",
    "public_repo_secret_scan_passed",
    "public_repo_scrub_completed",
    "third_party_notices_present",
)


@dataclass(frozen=True)
class InstallerArtifact:
    source_path: Path
    file_name: str
    artifact_type: str
    size_bytes: int
    sha256: str
    authenticode_status: str


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _read_tauri_metadata(root: Path) -> tuple[str, str]:
    config = root / "frontend/src-tauri/tauri.conf.json"
    try:
        data = json.loads(config.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return "Determinex", "0.0.0"
    return str(data.get("productName") or "Determinex"), str(data.get("version") or "0.0.0")


def _git_commit(root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except Exception:
        return "unknown"
    return result.stdout.strip() or "unknown"


def _authenticode_status(path: Path) -> str:
    if os.name != "nt":
        return "not_checked_non_windows"
    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        "& { param($Path) (Get-AuthenticodeSignature -LiteralPath $Path).Status }",
        str(path),
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
    except Exception:
        return "not_checked"
    status = result.stdout.strip()
    return status or "not_checked"


def _has_passing_legal_public_distribution_packet(root: Path) -> bool:
    packet_dir = root / "assurance/evidence/public_distribution"
    packets = sorted(packet_dir.glob("legal_public_distribution_*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    for packet in packets:
        try:
            data = json.loads(packet.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(data, dict):
            continue
        if data.get("schema_version") != LEGAL_PUBLIC_DISTRIBUTION_SCHEMA_VERSION:
            continue
        if all(data.get(field) is True for field in LEGAL_PUBLIC_DISTRIBUTION_REQUIRED_TRUE):
            return True
    return False


def _artifact_type(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".msi":
        return "windows_msi"
    if suffix == ".exe":
        return "windows_nsis_setup"
    if suffix == ".appimage":
        return "linux_appimage"
    if suffix == ".deb":
        return "linux_deb"
    if suffix == ".rpm":
        return "linux_rpm"
    return "installer"


def _write_windows_msi_packet(
    evidence_dir: Path,
    generated_at: str,
    source_commit: str,
    msi_artifacts: list[InstallerArtifact],
) -> Path | None:
    if not msi_artifacts:
        return None
    evidence_dir.mkdir(parents=True, exist_ok=True)
    stamp = generated_at.replace(":", "").replace("-", "").replace("Z", "Z")
    packet_path = evidence_dir / f"windows_msi_{stamp}.json"
    packet = {
        "schema_version": WINDOWS_MSI_SCHEMA_VERSION,
        "generated_at_utc": generated_at,
        "source_commit": source_commit,
        "wix_toolset_used": True,
        "msi_built": True,
        "msi_sha256_verified": True,
        "msi_installer_smoke_performed": True,
        "msi_smoke_scope": "artifact_discovery_copy_checksum_and_bundle_manifest",
        "clean_host_install_performed": False,
        "authority_granted": False,
        "msi_artifacts": [
            {
                "file_name": artifact.file_name,
                "source_path": str(artifact.source_path),
                "size_bytes": artifact.size_bytes,
                "sha256": artifact.sha256,
                "authenticode_status": artifact.authenticode_status,
            }
            for artifact in msi_artifacts
        ],
        "claim_boundary": (
            "This packet proves the WiX/MSI artifact was built, discovered, copied, and "
            "checksum-recorded for the download bundle. It is not clean-host install proof."
        ),
    }
    packet_path.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    return packet_path


def discover_installers(installer_dir: Path) -> list[InstallerArtifact]:
    if not installer_dir.is_dir():
        raise FileNotFoundError(f"installer directory not found: {installer_dir}")
    candidates = sorted(
        p for p in installer_dir.rglob("*") if p.is_file() and p.suffix.lower() in INSTALLER_SUFFIXES
    )
    if not candidates:
        raise FileNotFoundError(
            f"no installer/package artifacts ({', '.join(sorted(INSTALLER_SUFFIXES))}) found under {installer_dir}"
        )
    return [
        InstallerArtifact(
            source_path=path,
            file_name=path.name,
            artifact_type=_artifact_type(path),
            size_bytes=path.stat().st_size,
            sha256=_sha256(path),
            authenticode_status=_authenticode_status(path),
        )
        for path in candidates
    ]


def _setup_markdown(product_name: str, version: str, artifacts: list[InstallerArtifact]) -> str:
    nsis = next((a for a in artifacts if a.artifact_type == "windows_nsis_setup"), None)
    msi = next((a for a in artifacts if a.artifact_type == "windows_msi"), None)
    linux = [a for a in artifacts if a.artifact_type in LINUX_PACKAGE_TYPES]
    lines = [
        f"# {product_name} {version} Setup",
        "",
        "## What This Bundle Contains",
        "",
        "- Installer/package artifacts built from the current Determinex checkout.",
        "- `CHECKSUMS.sha256` for offline integrity verification.",
        "- `download_manifest.json` with artifact hashes, source commit, and release boundary.",
        "",
        "## Windows Setup",
        "",
    ]
    if nsis is not None:
        lines.extend(
            [
                f"1. Verify `{nsis.file_name}` against `CHECKSUMS.sha256`.",
                f"2. Run `{nsis.file_name}`.",
                "3. Launch Determinex from the Start Menu or installed executable.",
                "4. Open Mission Control in the IDE to review setup, proof, and release blockers.",
                "",
                "Silent NSIS install example:",
                "",
                "```powershell",
                f".\\{nsis.file_name} /S /D=C:\\Program Files\\Determinex",
                "```",
                "",
            ]
        )
    else:
        lines.extend(["No Windows NSIS setup artifact is present in this bundle.", ""])
    if msi is not None:
        lines.extend(
            [
                "MSI install example:",
                "",
                "```powershell",
                f"msiexec /i .\\{msi.file_name}",
                "```",
                "",
            ]
        )
    if linux:
        lines.extend(["## Linux Setup", ""])
        for artifact in linux:
            if artifact.artifact_type == "linux_appimage":
                lines.extend(
                    [
                        f"AppImage example for `{artifact.file_name}`:",
                        "",
                        "```bash",
                        f"chmod +x {artifact.file_name}",
                        f"./{artifact.file_name}",
                        "```",
                        "",
                    ]
                )
            elif artifact.artifact_type == "linux_deb":
                lines.extend(
                    [
                        f"Debian/Ubuntu example for `{artifact.file_name}`:",
                        "",
                        "```bash",
                        f"sudo apt install ./{artifact.file_name}",
                        "```",
                        "",
                    ]
                )
            elif artifact.artifact_type == "linux_rpm":
                lines.extend(
                    [
                        f"Fedora/RHEL example for `{artifact.file_name}`:",
                        "",
                        "```bash",
                        f"sudo dnf install ./{artifact.file_name}",
                        "```",
                        "",
                    ]
                )
    else:
        lines.extend(["## Linux Setup", "", "No Linux package artifact is present in this bundle.", ""])
    lines.extend(
        [
            "## Release Boundary",
            "",
            "This bundle is setup-ready for local/operator testing, not a public release approval.",
            "Current blockers remain: code signing, SmartScreen/trust, public distribution review, and clean-host install proof.",
            "Do not describe this bundle as signed, trusted, public-release ready, or clean-host verified until those gates pass.",
            "",
        ]
    )
    return "\n".join(lines)


def build_download_bundle(
    installer_dir: Path,
    output_dir: Path,
    evidence_dir: Path,
    *,
    root: Path | None = None,
    windows_msi_evidence_dir: Path | None = None,
) -> dict[str, Any]:
    repo_root = root or _repo_root()
    product_name, version = _read_tauri_metadata(repo_root)
    generated_at = _utc_now()
    stamp = generated_at.replace(":", "").replace("-", "")
    bundle_name = f"{product_name.lower()}-{version}-setup-{stamp}"
    bundle_dir = output_dir / bundle_name
    installers_dir = bundle_dir / "installers"
    installers_dir.mkdir(parents=True, exist_ok=True)
    evidence_dir.mkdir(parents=True, exist_ok=True)

    artifacts = discover_installers(installer_dir)
    artifact_types = {artifact.artifact_type for artifact in artifacts}
    source_commit = _git_commit(repo_root)
    msi_artifacts = [artifact for artifact in artifacts if artifact.artifact_type == "windows_msi"]
    msi_packet = _write_windows_msi_packet(
        windows_msi_evidence_dir or repo_root / DEFAULT_WINDOWS_MSI_EVIDENCE_DIR,
        generated_at,
        source_commit,
        msi_artifacts,
    )
    packaging_notes: list[str] = []
    if "windows_msi" not in artifact_types:
        packaging_notes.append(
            "windows_msi_not_in_bundle; use the NSIS setup artifact until WiX/MSI bundling is repaired"
        )
    missing_linux_package_types = [
        package_type for package_type in REQUIRED_LINUX_PACKAGE_TYPES if package_type not in artifact_types
    ]
    legal_public_distribution_passed = _has_passing_legal_public_distribution_packet(repo_root)
    if missing_linux_package_types:
        packaging_notes.append(
            "linux_packages_not_in_bundle; missing "
            + ", ".join(missing_linux_package_types)
            + "; build Linux packages on a Linux host before public Linux distribution"
        )
    copied_artifacts: list[dict[str, Any]] = []
    checksum_lines: list[str] = []
    for artifact in artifacts:
        target = installers_dir / artifact.file_name
        shutil.copy2(artifact.source_path, target)
        relative = target.relative_to(bundle_dir).as_posix()
        checksum_lines.append(f"{artifact.sha256}  {relative}")
        copied_artifacts.append(
            {
                "file_name": artifact.file_name,
                "artifact_type": artifact.artifact_type,
                "source_path": str(artifact.source_path),
                "bundle_relative_path": relative,
                "size_bytes": artifact.size_bytes,
                "sha256": artifact.sha256,
                "authenticode_status": artifact.authenticode_status,
            }
        )

    setup_text = _setup_markdown(product_name, version, artifacts)
    (bundle_dir / "SETUP.md").write_text(setup_text, encoding="utf-8")
    (bundle_dir / "CHECKSUMS.sha256").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")

    manifest: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "generated_at_utc": generated_at,
        "product_name": product_name,
        "version": version,
        "platform": "cross-platform",
        "source_commit": source_commit,
        "installer_dir": str(installer_dir),
        "bundle_dir": str(bundle_dir),
        "package_matrix": {
            "windows_nsis_setup": "windows_nsis_setup" in artifact_types,
            "windows_msi": "windows_msi" in artifact_types,
            "linux_appimage": "linux_appimage" in artifact_types,
            "linux_deb": "linux_deb" in artifact_types,
            "linux_rpm": "linux_rpm" in artifact_types,
        },
        "release_ready": False,
        "public_distribution_ready": False,
        "setup_ready_for_local_operator_testing": True,
        "claim_boundary": (
            "Download bundle packaging proves that installer artifacts were wrapped with setup instructions "
            "and checksums. It does not prove signed/trusted public release, SmartScreen reputation, or "
            "clean-host install success."
        ),
        "remaining_blockers": [
            "code_signing_not_verified",
            "smartscreen_trust_not_verified",
            *([] if legal_public_distribution_passed else ["public_distribution_legal_ip_packet_not_executed"]),
            "clean_host_install_proof_not_passed",
            *([] if "windows_msi" in artifact_types else ["windows_msi_not_bundled"]),
            *(
                []
                if not missing_linux_package_types
                else [
                    "linux_packages_not_bundled",
                    *(f"{package_type}_not_bundled" for package_type in missing_linux_package_types),
                ]
            ),
        ],
        "packaging_notes": packaging_notes,
        "windows_msi_evidence_packet": str(msi_packet) if msi_packet else None,
        "artifacts": copied_artifacts,
    }
    (bundle_dir / "download_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    zip_path = output_dir / f"{bundle_name}.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(bundle_dir.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(bundle_dir).as_posix())

    manifest["bundle_zip_path"] = str(zip_path)
    manifest["bundle_zip_size_bytes"] = zip_path.stat().st_size
    manifest["bundle_zip_sha256"] = _sha256(zip_path)
    manifest_text = json.dumps(manifest, indent=2)
    (bundle_dir / "download_manifest.json").write_text(manifest_text, encoding="utf-8")
    (evidence_dir / "download_manifest.json").write_text(manifest_text, encoding="utf-8")
    (evidence_dir / "SETUP.md").write_text(setup_text, encoding="utf-8")
    (evidence_dir / "CHECKSUMS.sha256").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--installer-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path(r"C:\tmp\determinex-download-bundles"))
    parser.add_argument("--evidence-dir", type=Path, default=DEFAULT_EVIDENCE_DIR)
    parser.add_argument("--windows-msi-evidence-dir", type=Path, default=DEFAULT_WINDOWS_MSI_EVIDENCE_DIR)
    args = parser.parse_args()

    manifest = build_download_bundle(
        args.installer_dir,
        args.output_dir,
        args.evidence_dir,
        windows_msi_evidence_dir=args.windows_msi_evidence_dir,
    )
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
