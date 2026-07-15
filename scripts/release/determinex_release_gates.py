"""Determinex release gate status collector.

This collector turns scattered release evidence into one conservative status
model. It never grants release authority; it only reports what the current
checkout can prove from local files.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "determinex-release-gate-status-v1"
CLEAN_HOST_TRANSCRIPT_SCHEMA_VERSION = "determinex-clean-host-install-transcript-v1"
SWEBENCH_FRESH_PUBLICATION_SCHEMA_VERSION = "determinex-swebench-fresh-publication-evidence-v1"
WINDOWS_TRUST_SCHEMA_VERSION = "determinex-windows-trust-evidence-v1"
LEGAL_PUBLIC_DISTRIBUTION_SCHEMA_VERSION = "determinex-legal-public-distribution-evidence-v1"
WINDOWS_MSI_SCHEMA_VERSION = "determinex-windows-msi-evidence-v1"
EXTENSION_COMPAT_SCHEMA_VERSION = "determinex-extension-compat-runtime-evidence-v1"
PROGRAMBENCH_DENOMINATOR = 200
SWEBENCH_REQUIRED_PRIVACY_MODES = frozenset({"B-Uncloaked", "RegionControl", "Cloaked"})
LINUX_PACKAGE_TYPES = frozenset({"linux_appimage", "linux_deb", "linux_rpm"})
REQUIRED_LINUX_PACKAGE_TYPES = ("linux_appimage", "linux_deb", "linux_rpm")


@dataclass(frozen=True)
class ReleaseGate:
    gate_id: str
    title: str
    status: str
    release_ready: bool
    evidence: tuple[str, ...]
    exact_blocker: str
    next_action: str
    runbook_commands: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["evidence"] = list(self.evidence)
        payload["runbook_commands"] = list(self.runbook_commands)
        return payload


@dataclass(frozen=True)
class ReleaseGateReport:
    schema_version: str
    generated_at_utc: str
    product_name: str
    release_ready: bool
    authority_granted: bool
    gates: tuple[ReleaseGate, ...]
    notes: tuple[str, ...] = field(default_factory=tuple)

    @property
    def blocked_gate_ids(self) -> tuple[str, ...]:
        return tuple(g.gate_id for g in self.gates if g.status == "blocked")

    @property
    def partial_gate_ids(self) -> tuple[str, ...]:
        return tuple(g.gate_id for g in self.gates if g.status == "partial")

    @property
    def deferred_gate_ids(self) -> tuple[str, ...]:
        return tuple(g.gate_id for g in self.gates if g.status == "deferred")

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "generated_at_utc": self.generated_at_utc,
            "product_name": self.product_name,
            "release_ready": self.release_ready,
            "authority_granted": self.authority_granted,
            "blocked_gate_ids": list(self.blocked_gate_ids),
            "partial_gate_ids": list(self.partial_gate_ids),
            "deferred_gate_ids": list(self.deferred_gate_ids),
            "gates": [g.to_dict() for g in self.gates],
            "notes": list(self.notes),
        }


def _rel(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def _read_json(path: Path) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _is_sha256(value: str) -> bool:
    if len(value) != 64:
        return False
    return all(ch in "0123456789abcdefABCDEF" for ch in value)


def _download_artifacts(download: dict[str, Any] | None, artifact_type: str) -> list[dict[str, Any]]:
    if not isinstance(download, dict):
        return []
    return [
        artifact
        for artifact in (download.get("artifacts") or [])
        if isinstance(artifact, dict) and artifact.get("artifact_type") == artifact_type
    ]


def _download_artifact_errors(root: Path, artifact: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    source_path = str(artifact.get("source_path") or "").strip()
    sha256 = str(artifact.get("sha256") or "").strip()
    size_bytes = artifact.get("size_bytes")

    if not source_path:
        errors.append("missing source_path")
        path = None
    elif "mocked" in source_path.lower():
        errors.append("mocked source_path")
        path = None
    else:
        path = root / source_path
        if not path.is_file():
            errors.append("missing source file")

    if not sha256:
        errors.append("missing sha256")
    elif "mocked" in sha256.lower():
        errors.append("mocked sha256")
    elif not _is_sha256(sha256):
        errors.append("invalid sha256")
    elif path is not None and path.is_file() and _hash_file(path).lower() != sha256.lower():
        errors.append("sha256 mismatch")

    if path is not None and path.is_file() and size_bytes is not None:
        try:
            expected_size = int(size_bytes)
        except (TypeError, ValueError):
            errors.append("invalid size_bytes")
        else:
            if expected_size != path.stat().st_size:
                errors.append("size_bytes mismatch")
    return errors


def _valid_download_artifact_types(root: Path, download: dict[str, Any] | None) -> set[str]:
    if not isinstance(download, dict):
        return set()
    valid: set[str] = set()
    for artifact in download.get("artifacts") or []:
        if not isinstance(artifact, dict):
            continue
        artifact_type = str(artifact.get("artifact_type") or "")
        if artifact_type and not _download_artifact_errors(root, artifact):
            valid.add(artifact_type)
    return valid


def _download_artifact_type_blockers(
    root: Path,
    download: dict[str, Any] | None,
    required_types: tuple[str, ...],
) -> list[str]:
    blockers: list[str] = []
    for artifact_type in required_types:
        artifacts = _download_artifacts(download, artifact_type)
        if not artifacts:
            blockers.append(f"{artifact_type}_not_bundled")
            continue
        artifact_errors = [_download_artifact_errors(root, artifact) for artifact in artifacts]
        if not any(not errors for errors in artifact_errors):
            merged = sorted({error for errors in artifact_errors for error in errors})
            blockers.append(f"{artifact_type} ({', '.join(merged)})")
    return blockers


def _download_artifact_hashes(root: Path, download: dict[str, Any] | None) -> set[str]:
    if not isinstance(download, dict):
        return set()
    hashes: set[str] = set()
    for artifact in download.get("artifacts") or []:
        if isinstance(artifact, dict) and not _download_artifact_errors(root, artifact):
            hashes.add(str(artifact["sha256"]).lower())
    return hashes


def _clean_host_transcript_candidates(root: Path) -> list[Path]:
    return sorted(
        [
            *(root / "assurance/evidence/full_release_closure").glob("clean_host_install_transcript_*.json"),
            *(root / "assurance/evidence/clean_host_fresh_install_runner_execution").glob(
                "clean_host_install_transcript_*.json"
            ),
        ],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )


def _clean_host_transcript_errors(data: Any) -> list[str]:
    if not isinstance(data, dict):
        return ["transcript JSON must be an object"]
    errors: list[str] = []
    expected_true = (
        "clean_host_fresh_install",
        "installer_execution_performed",
        "launch_performed",
        "proof_center_smoke_performed",
        "workspace_command_smoke_performed",
        "uninstall_performed",
    )
    for field in expected_true:
        if data.get(field) is not True:
            errors.append(f"{field} must be true")
    expected_false = (
        "dry_run",
        "release_ready",
        "authority_granted",
    )
    for field in expected_false:
        if data.get(field) is not False:
            errors.append(f"{field} must be false")
    if data.get("schema_version") != CLEAN_HOST_TRANSCRIPT_SCHEMA_VERSION:
        errors.append(f"schema_version must be {CLEAN_HOST_TRANSCRIPT_SCHEMA_VERSION}")
    if data.get("product_name") != "Determinex":
        errors.append("product_name must be Determinex")

    runner = data.get("runner")
    if not isinstance(runner, dict):
        errors.append("runner must be an object")
    else:
        if runner.get("is_clean_host") is not True:
            errors.append("runner.is_clean_host must be true")
        if runner.get("host_reused_from_developer_machine") is not False:
            errors.append("runner.host_reused_from_developer_machine must be false")
        if not str(runner.get("os") or "").lower().startswith("windows"):
            errors.append("runner.os must identify a Windows clean host")
        runner_id = str(runner.get("runner_id") or "")
        if not runner_id or "mocked" in runner_id.lower():
            errors.append("runner.runner_id must not be a mocked runner")

    bundle = data.get("bundle")
    if not isinstance(bundle, dict):
        errors.append("bundle must be an object")
    else:
        if not str(bundle.get("source_commit") or "").strip():
            errors.append("bundle.source_commit must be recorded")
        if bundle.get("installer_sha256_verified") is not True:
            errors.append("bundle.installer_sha256_verified must be true")
        sha256 = str(bundle.get("installer_sha256") or "")
        if not sha256 or "mocked" in sha256.lower():
            errors.append("bundle.installer_sha256 must not be mocked")
    return errors


def _latest_clean_host_transcript(root: Path) -> tuple[Path | None, dict[str, Any] | None, list[str]]:
    download_manifests = sorted((root / "assurance/evidence").glob("determinex_download_bundle_*/download_manifest.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    manifest = _read_json(download_manifests[0]) if download_manifests and download_manifests[0].is_file() else None
    valid_hashes = _download_artifact_hashes(root, manifest)

    first_invalid: tuple[Path, list[str]] | None = None
    for candidate in _clean_host_transcript_candidates(root):
        data = _read_json(candidate)
        errors = _clean_host_transcript_errors(data)
        if not errors and isinstance(data, dict):
            bundle_hash = str((data.get("bundle") or {}).get("installer_sha256") or "").lower()
            if bundle_hash not in valid_hashes:
                errors.append("bundle.installer_sha256 does not match any known artifact in the current download bundle manifest")
        if not errors and isinstance(data, dict):
            return candidate, data, []
        if first_invalid is None:
            first_invalid = (candidate, errors)
    if first_invalid is not None:
        path, errors = first_invalid
        return path, None, errors
    return None, None, []


def _gate(
    gate_id: str,
    title: str,
    status: str,
    evidence: list[str],
    exact_blocker: str,
    next_action: str,
    runbook_commands: list[str] | None = None,
) -> ReleaseGate:
    return ReleaseGate(
        gate_id=gate_id,
        title=title,
        status=status,
        release_ready=False,
        evidence=tuple(evidence),
        exact_blocker=exact_blocker,
        next_action=next_action,
        runbook_commands=tuple(runbook_commands or []),
    )


def _packet_field_errors(
    data: Any,
    *,
    schema_version: str,
    expected_true: tuple[str, ...] = (),
    expected_false: tuple[str, ...] = ("authority_granted",),
) -> list[str]:
    if not isinstance(data, dict):
        return ["packet JSON must be an object"]
    errors: list[str] = []
    if data.get("schema_version") != schema_version:
        errors.append(f"schema_version must be {schema_version}")
    for field_name in expected_true:
        if data.get(field_name) is not True:
            errors.append(f"{field_name} must be true")
    for field_name in expected_false:
        if data.get(field_name) is not False:
            errors.append(f"{field_name} must be false")
    return errors


def _latest_packet(
    root: Path,
    folder: str,
    pattern: str,
    errors_fn,
) -> tuple[Path | None, dict[str, Any] | None, list[str]]:
    candidates = sorted(
        (root / folder).glob(pattern),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    first_invalid: tuple[Path, list[str]] | None = None
    for candidate in candidates:
        data = _read_json(candidate)
        errors = errors_fn(data)
        if not errors and isinstance(data, dict):
            return candidate, data, []
        if first_invalid is None:
            first_invalid = (candidate, errors)
    if first_invalid is not None:
        path, errors = first_invalid
        return path, None, errors
    return None, None, []


def _sbom_gate(root: Path) -> ReleaseGate:
    required = [
        root / "assurance/sbom/determinex-python.spdx.json",
        root / "assurance/sbom/determinex-python.cyclonedx.json",
        root / "assurance/sbom/determinex-npm.cyclonedx.json",
    ]
    missing = [p for p in required if not p.is_file()]
    evidence = [_rel(root, p) for p in required if p.is_file()]
    if missing:
        return _gate(
            "sbom",
            "SBOM coverage",
            "blocked",
            evidence,
            "Missing SBOM artifact(s): " + ", ".join(_rel(root, p) for p in missing),
            "Regenerate Python and npm SBOM artifacts and rerun this collector.",
            [
                r".venv\Scripts\python.exe scripts\security\generate_sbom.py",
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )

    parsed = [_read_json(p) for p in required]
    if any(p is None for p in parsed):
        return _gate(
            "sbom",
            "SBOM coverage",
            "blocked",
            evidence,
            "At least one SBOM artifact is not valid JSON.",
            "Regenerate malformed SBOM artifacts.",
            [
                r".venv\Scripts\python.exe scripts\security\generate_sbom.py",
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )

    spdx, python_cdx, npm_cdx = parsed
    python_spdx_name = str(spdx.get("name", "")) if isinstance(spdx, dict) else ""
    python_cdx_name = ""
    if isinstance(python_cdx, dict):
        metadata = python_cdx.get("metadata") or {}
        component = metadata.get("component") if isinstance(metadata, dict) else {}
        python_cdx_name = str((component or {}).get("name", ""))
    npm_bom_format = str(npm_cdx.get("bomFormat", "")) if isinstance(npm_cdx, dict) else ""
    if not python_spdx_name.startswith("determinex-python") or python_cdx_name != "determinex-python":
        return _gate(
            "sbom",
            "SBOM coverage",
            "blocked",
            evidence,
            "Python SBOM artifacts are not Determinex branded.",
            "Regenerate SBOMs with scripts/security/generate_sbom.py.",
            [
                r".venv\Scripts\python.exe scripts\security\generate_sbom.py",
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    if npm_bom_format != "CycloneDX":
        return _gate(
            "sbom",
            "SBOM coverage",
            "blocked",
            evidence,
            "NPM SBOM is not a CycloneDX JSON artifact.",
            "Regenerate frontend SBOM with the npm SBOM script.",
            [
                r"cd frontend; npm.cmd run sbom",
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    return _gate(
        "sbom",
        "SBOM coverage",
        "passed",
        evidence + [f"sha256:{_hash_file(p)}" for p in required],
        "",
        "Keep SBOMs regenerated for release artifacts and clean-host packets.",
        [
            r".venv\Scripts\python.exe scripts\security\generate_sbom.py",
            r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
        ],
    )


def _clean_host_gate(root: Path) -> ReleaseGate:
    path = root / (
        "assurance/evidence/clean_host_fresh_install_runner_execution/"
        "run_20260531.CLEAN_HOST_FRESH_INSTALL_RUNNER_EXECUTION_BLOCKED_RUNNER_NOT_EXECUTED.json"
    )
    transcript_path, transcript_data, transcript_errors = _latest_clean_host_transcript(root)
    preflights = sorted(
        [
            *(root / "assurance/evidence/clean_host_fresh_install_runner_execution").glob("runner_preflight_*.json"),
            *(root / "assurance/evidence/full_release_closure").glob("clean_host_runner_preflight_*.json"),
        ],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    preflight = preflights[0] if preflights else None
    evidence = [_rel(root, p) for p in (transcript_path, path, preflight) if p is not None and p.is_file()]
    data = _read_json(path) if path.is_file() else None
    preflight_data = _read_json(preflight) if preflight and preflight.is_file() else None
    if transcript_data is not None:
        return _gate(
            "clean_host",
            "Clean-host install proof",
            "passed",
            evidence,
            "",
            "Keep the clean-host transcript tied to the final release commit.",
            [
                r".venv\Scripts\python.exe scripts\release\clean_host_install_transcript.py --validate "
                + _rel(root, transcript_path),
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    if transcript_path is not None:
        return _gate(
            "clean_host",
            "Clean-host install proof",
            "blocked",
            evidence,
            "Invalid clean-host install transcript: " + "; ".join(transcript_errors),
            "Rerun the clean-host installer transcript on a clean Windows runner and validate it before collecting release gates.",
            [
                r".venv\Scripts\python.exe scripts\release\clean_host_install_transcript.py --template-output assurance\evidence\full_release_closure\clean_host_install_transcript_YYYYMMDD.json",
                r".venv\Scripts\python.exe scripts\release\clean_host_install_transcript.py --validate "
                + _rel(root, transcript_path),
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    if not isinstance(data, dict):
        return _gate(
            "clean_host",
            "Clean-host install proof",
            "blocked",
            evidence,
            "No clean-host install execution record found.",
            "Run a clean-host install/launch/smoke/uninstall transcript and record the output.",
            [
                "docker info",
                r".venv\Scripts\python.exe scripts\release\clean_host_install_transcript.py --template-output assurance\evidence\full_release_closure\clean_host_install_transcript_YYYYMMDD.json",
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    if isinstance(preflight_data, dict) and preflight_data.get("docker_info_available") is True:
        return _gate(
            "clean_host",
            "Clean-host install proof",
            "blocked",
            evidence,
            "Clean runner is available, but clean-host installer install/launch/uninstall proof has not been executed.",
            "Run the installer in a clean Windows runner, capture install/launch/uninstall transcript, and replace the blocked clean-host record with passing proof.",
            [
                "docker info",
                r".venv\Scripts\python.exe scripts\release\clean_host_install_transcript.py --template-output assurance\evidence\full_release_closure\clean_host_install_transcript_YYYYMMDD.json",
                r".venv\Scripts\python.exe scripts\release\full_release_closure.py --output assurance\evidence\full_release_closure\run_20260707.json",
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    preflight_blocker = (
        str(preflight_data.get("exact_blocker"))
        if isinstance(preflight_data, dict) and preflight_data.get("exact_blocker")
        else ""
    )
    blocker = (
        preflight_blocker
        or ((data.get("artifact_payloads") or {}).get("clean_run_transcript_or_blocker") or {}).get("blocker")
        or data.get("status")
        or "Clean-host proof did not pass."
    )
    next_action = (
        "Rerun the clean-host probe outside the sandbox, then execute the install/launch/uninstall transcript."
        if isinstance(preflight_data, dict) and preflight_data.get("docker_probe_blocked_by_sandbox") is True
        else "Provision or repair a clean runner, then rerun install/build/smoke proof."
    )
    return _gate(
        "clean_host",
        "Clean-host install proof",
        "blocked",
        evidence,
        str(blocker),
        next_action,
        [
            "docker info",
            r".venv\Scripts\python.exe scripts\release\clean_host_install_transcript.py --template-output assurance\evidence\full_release_closure\clean_host_install_transcript_YYYYMMDD.json",
            r".venv\Scripts\python.exe scripts\release\full_release_closure.py --output assurance\evidence\full_release_closure\run_20260707.json",
            r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
        ],
    )


def _first_e2e_gate(root: Path) -> ReleaseGate:
    path = root / "assurance/evidence/first_end_to_end_user_workflow/result.json"
    probe = root / "assurance/evidence/first_end_to_end_user_workflow/builder_health_probe_latest.json"
    rerun = root / "assurance/evidence/first_end_to_end_user_workflow/rerun_after_builder_health_latest.json"
    evidence = [_rel(root, p) for p in (path, probe, rerun) if p.is_file()]
    data = _read_json(path) if path.is_file() else None
    probe_data = _read_json(probe) if probe.is_file() else None
    rerun_data = _read_json(rerun) if rerun.is_file() else None
    rerun_session_id = (
        str(rerun_data.get("session_id"))
        if isinstance(rerun_data, dict) and rerun_data.get("session_id")
        else "99d31f71-a25a-4849-8b12-44131c586699"
    )
    if not isinstance(data, dict):
        return _gate(
            "first_e2e",
            "First end-to-end user workflow",
            "blocked",
            evidence,
            "No first E2E workflow result found.",
            "Run and capture a full user workflow transcript.",
            [
                r".venv\Scripts\python.exe scripts\hive\builder_health_probe.py --model determinex/engineer --output assurance\evidence\first_end_to_end_user_workflow\builder_health_probe_latest.json",
            ],
        )
    status = str(data.get("status", ""))
    rerun_status = str(rerun_data.get("status", "")) if isinstance(rerun_data, dict) else ""
    rerun_observed = rerun_data.get("observed_result") if isinstance(rerun_data, dict) else {}
    rerun_steps_complete = int(rerun_observed.get("steps_complete", -1)) if isinstance(rerun_observed, dict) else -1
    rerun_steps_total = int(rerun_observed.get("steps_total", -2)) if isinstance(rerun_observed, dict) else -2
    rerun_steps_failed = int(rerun_observed.get("steps_failed", 1)) if isinstance(rerun_observed, dict) else 1
    if (
        isinstance(rerun_data, dict)
        and (rerun_status.endswith("PASSED") or rerun_status.endswith("SUCCESS"))
        and rerun_steps_total > 0
        and rerun_steps_complete == rerun_steps_total
        and rerun_steps_failed == 0
    ):
        return _gate(
            "first_e2e",
            "First end-to-end user workflow",
            "passed",
            evidence,
            "",
            "Keep the passing first-E2E transcript current with the release commit.",
            [
                r".venv\Scripts\python.exe scripts\hive\builder_health_probe.py --model determinex/engineer --output assurance\evidence\first_end_to_end_user_workflow\builder_health_probe_latest.json",
                rf".venv\Scripts\python.exe scripts\determinex_hive.py run-session --session {rerun_session_id}",
            ],
        )
    if status.endswith("PASSED") or status.endswith("SUCCESS"):
        return _gate(
            "first_e2e",
            "First end-to-end user workflow",
            "passed",
            evidence,
            "",
            "Keep the transcript current with the release commit.",
            [
                r".venv\Scripts\python.exe scripts\hive\builder_health_probe.py --model determinex/engineer --output assurance\evidence\first_end_to_end_user_workflow\builder_health_probe_latest.json",
            ],
        )
    return _gate(
        "first_e2e",
        "First end-to-end user workflow",
        "blocked",
        evidence,
        (
            str(rerun_data.get("exact_blocker"))
            if isinstance(rerun_data, dict) and rerun_data.get("exact_blocker")
            else
            "First E2E transcript has not been rerun after Builder health passed."
            if isinstance(probe_data, dict) and probe_data.get("status") == "passed"
            else status or "First E2E did not pass."
        ),
        (
            str(rerun_data.get("next_required_action"))
            if isinstance(rerun_data, dict) and rerun_data.get("next_required_action")
            else
            "Rerun session 99d31f71-a25a-4849-8b12-44131c586699 with the existing correctness harness."
            if isinstance(probe_data, dict) and probe_data.get("status") == "passed"
            else str(data.get("next_required_action") or "Restore workflow health and rerun the transcript.")
        ),
        [
            r".venv\Scripts\python.exe scripts\hive\builder_health_probe.py --model determinex/engineer --output assurance\evidence\first_end_to_end_user_workflow\builder_health_probe_latest.json",
            r'$env:DETERMINEX_BUILDER_FALLBACK_MODEL="<stable admitted model>"; .venv\Scripts\python.exe scripts\hive\builder_health_probe.py --model determinex/engineer --fallback-model "<stable admitted model>"',
            rf".venv\Scripts\python.exe scripts\determinex_hive.py run-session --session {rerun_session_id}",
        ],
    )


def _download_artifact_types(download: dict[str, Any] | None) -> set[str]:
    if not isinstance(download, dict):
        return set()
    artifact_types = {
        str(artifact.get("artifact_type"))
        for artifact in (download.get("artifacts") or [])
        if isinstance(artifact, dict) and artifact.get("artifact_type")
    }
    matrix = download.get("package_matrix")
    if isinstance(matrix, dict):
        artifact_types.update(str(name) for name, present in matrix.items() if present is True)
    return artifact_types


def _installer_gate(root: Path) -> ReleaseGate:
    go_no_go = root / (
        "assurance/evidence/installer_install_launch_uninstall_release_signoff_wave_001/"
        "public_distribution_go_no_go_20260602.json"
    )
    hardening = root / (
        "assurance/evidence/installer_release_packet_hardening/"
        "run_20260629.INSTALLER_RELEASE_PACKET_HARDENED_UNSIGNED.json"
    )
    download_manifests = sorted(
        (root / "assurance/evidence").glob("determinex_download_bundle_*/download_manifest.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    download_manifest = download_manifests[0] if download_manifests else None
    evidence_paths = [p for p in (go_no_go, hardening, download_manifest) if p is not None and p.is_file()]
    evidence = [_rel(root, p) for p in evidence_paths]
    go = _read_json(go_no_go) if go_no_go.is_file() else None
    hard = _read_json(hardening) if hardening.is_file() else None
    download = _read_json(download_manifest) if download_manifest and download_manifest.is_file() else None
    if not isinstance(go, dict) and not isinstance(hard, dict) and not isinstance(download, dict):
        return _gate(
            "installer",
            "Installer/signing/public distribution",
            "blocked",
            evidence,
            "No installer release gate evidence found.",
            "Build an installer packet and capture install/launch/uninstall proof.",
            [
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    if isinstance(go, dict) and go.get("release_ready") is True and go.get("go_no_go") == "GO_PUBLIC_DISTRIBUTION":
        return _gate(
            "installer",
            "Installer/signing/public distribution",
            "passed",
            evidence,
            "",
            "Keep installer proof tied to the final release artifact.",
            [
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    blockers: list[str] = []
    if isinstance(go, dict):
        blockers.extend(str(b) for b in go.get("exact_blockers") or [])
    if isinstance(hard, dict) and hard.get("status"):
        blockers.append(str(hard["status"]))
    artifact_types = _download_artifact_types(download)
    setup_ready = isinstance(download, dict) and download.get("setup_ready_for_local_operator_testing") is True
    package_blockers: list[str] = []
    if setup_ready:
        if "windows_nsis_setup" not in artifact_types:
            package_blockers.append("windows_nsis_setup_not_bundled")
        if "windows_msi" not in artifact_types:
            package_blockers.append("windows_msi_not_bundled")
        missing_linux = [package_type for package_type in REQUIRED_LINUX_PACKAGE_TYPES if package_type not in artifact_types]
        if missing_linux:
            package_blockers.append("linux_packages_not_bundled")
            package_blockers.extend(f"{package_type}_not_bundled" for package_type in missing_linux)
    elif isinstance(download, dict):
        package_blockers.append("download_bundle_not_setup_ready")
    blockers = list(dict.fromkeys(blockers))
    if setup_ready:
        artifact_blockers = _download_artifact_type_blockers(
            root,
            download,
            ("windows_nsis_setup", "windows_msi", *REQUIRED_LINUX_PACKAGE_TYPES),
        )
        package_blockers.extend(artifact_blockers)
    package_blockers = list(dict.fromkeys(package_blockers))
    if setup_ready and not package_blockers:
        return _gate(
            "installer",
            "Installer/package artifact matrix",
            "passed",
            evidence,
            "",
            "Keep the cross-platform download bundle current with the final release commit.",
            [
                r"powershell -ExecutionPolicy Bypass -File scripts\release\build_release_package.ps1 -SkipDependencyRestore -SkipSbom -SkipSidecar -CargoTargetDir .tmp\determinex-cargo-target -PackageDownloadBundle -TauriBundleTarget all -DownloadBundleOutputDir .tmp\determinex-download-bundles",
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    return _gate(
        "installer",
        "Installer/package artifact matrix",
        "partial",
        evidence,
        "; ".join(package_blockers or blockers) or "Installer packet exists but final package artifact matrix is incomplete.",
        "Build the full package matrix: Windows NSIS, Windows MSI, and Linux package artifact(s), then refresh the download bundle.",
        [
            r"powershell -ExecutionPolicy Bypass -File scripts\release\build_release_package.ps1 -SkipDependencyRestore -SkipSbom -SkipSidecar -CargoTargetDir .tmp\determinex-cargo-target -PackageDownloadBundle -TauriBundleTarget all -DownloadBundleOutputDir .tmp\determinex-download-bundles",
            r"cd frontend; npm run tauri -- build --bundles appimage,deb,rpm",
            r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
        ],
    )


def _windows_trust_errors(data: Any) -> list[str]:
    errors = _packet_field_errors(
        data,
        schema_version=WINDOWS_TRUST_SCHEMA_VERSION,
        expected_true=(
            "code_signing_verified",
            "timestamp_verified",
            "smartscreen_verification_performed",
        ),
    )
    if not isinstance(data, dict):
        return errors
    if data.get("artifact_authenticode_status") != "Valid":
        errors.append("artifact_authenticode_status must be Valid")
    if str(data.get("smartscreen_result") or "").lower() not in {"pass", "no_warning", "trusted"}:
        errors.append("smartscreen_result must be pass, no_warning, or trusted")
    if not str(data.get("certificate_subject") or "").strip():
        errors.append("certificate_subject must be recorded")
    return errors


def _windows_trust_gate(root: Path) -> ReleaseGate:
    path, data, errors = _latest_packet(
        root,
        "assurance/evidence/windows_trust",
        "windows_trust_*.json",
        _windows_trust_errors,
    )
    evidence = [_rel(root, path)] if path else []
    if data is not None:
        return _gate(
            "windows_trust",
            "Windows signing and SmartScreen trust",
            "passed",
            evidence,
            "",
            "Keep Authenticode and SmartScreen evidence current for the final installer artifacts.",
            [
                r"powershell Get-AuthenticodeSignature <installer.exe>",
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    return _gate(
        "windows_trust",
        "Windows signing and SmartScreen trust",
        "deferred",
        evidence,
        (
            "Invalid Windows signing and SmartScreen trust packet: " + "; ".join(errors)
            if path
            else "No Windows signing and SmartScreen trust packet was found."
        ),
        "Sign the Windows installer, verify Authenticode and timestamp status, then run SmartScreen trust verification on the final artifact.",
        [
            r"powershell Get-AuthenticodeSignature <installer.exe>",
            r"powershell -ExecutionPolicy Bypass -File scripts\release\build_release_package.ps1 -PackageDownloadBundle",
            r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
        ],
    )


def _legal_public_distribution_errors(data: Any) -> list[str]:
    return _packet_field_errors(
        data,
        schema_version=LEGAL_PUBLIC_DISTRIBUTION_SCHEMA_VERSION,
        expected_true=(
            "legal_review_completed",
            "license_inventory_reviewed",
            "model_notice_reviewed",
            "public_repo_secret_scan_passed",
            "public_repo_scrub_completed",
            "third_party_notices_present",
        ),
    )


def _agpl_source_license_evidence(root: Path) -> tuple[list[str], list[str]]:
    required = [
        root / "LICENSE",
        root / "pyproject.toml",
        root / "frontend/package.json",
        root / "frontend/src-tauri/Cargo.toml",
        root / "frontend/vscode-extension/package.json",
    ]
    evidence: list[str] = []
    errors: list[str] = []
    for path in required:
        if not path.is_file():
            errors.append(f"{_rel(root, path)} missing")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        evidence.append(_rel(root, path))
        if path.name == "LICENSE":
            if "GNU AFFERO GENERAL PUBLIC LICENSE" not in text or "Version 3" not in text:
                errors.append("LICENSE is not AGPLv3 text")
        elif "AGPL-3.0" not in text:
            errors.append(f"{_rel(root, path)} does not declare AGPL-3.0")
    return evidence, errors


def _legal_public_distribution_gate(root: Path) -> ReleaseGate:
    path, data, errors = _latest_packet(
        root,
        "assurance/evidence/public_distribution",
        "legal_public_distribution_*.json",
        _legal_public_distribution_errors,
    )
    evidence = [_rel(root, path)] if path else []
    if data is not None:
        return _gate(
            "legal_public_distribution",
            "Legal/IP public distribution packet",
            "passed",
            evidence,
            "",
            "Keep legal, license, model notice, and public-repo scrub packets current with release artifacts.",
            [
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    agpl_evidence, agpl_errors = _agpl_source_license_evidence(root)
    if not agpl_errors:
        return _gate(
            "legal_public_distribution",
            "Legal/IP public distribution packet",
            "partial",
            evidence + agpl_evidence,
            (
                "AGPLv3 source license evidence is present, but public repo secret scan, "
                "repo scrub, model notices, and third-party notices have not been recorded "
                "in the legal public distribution packet."
            ),
            "Complete the public distribution packet after source license, notices, model inventory, secret scan, and repo scrub review.",
            [
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
                r"powershell # write assurance\evidence\public_distribution\legal_public_distribution_YYYYMMDD.json after review",
            ],
        )
    return _gate(
        "legal_public_distribution",
        "Legal/IP public distribution packet",
        "blocked",
        evidence + agpl_evidence,
        (
            "Invalid legal/IP public distribution packet: " + "; ".join(errors)
            if path
            else "No legal/IP public distribution packet was found; AGPL source license evidence incomplete: "
            + "; ".join(agpl_errors)
        ),
        "Complete legal/IP review, license inventory, model notices, secret scan, and public repo scrub before public distribution.",
        [
            r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            r"powershell # write assurance\evidence\public_distribution\legal_public_distribution_YYYYMMDD.json after review",
        ],
    )


def _windows_msi_errors(data: Any) -> list[str]:
    return _packet_field_errors(
        data,
        schema_version=WINDOWS_MSI_SCHEMA_VERSION,
        expected_true=(
            "wix_toolset_used",
            "msi_built",
            "msi_sha256_verified",
            "msi_installer_smoke_performed",
        ),
    )


def _windows_msi_gate(root: Path) -> ReleaseGate:
    path, data, errors = _latest_packet(
        root,
        "assurance/evidence/windows_msi",
        "windows_msi_*.json",
        _windows_msi_errors,
    )
    evidence = [_rel(root, path)] if path else []
    if data is not None:
        return _gate(
            "windows_msi",
            "Windows MSI/WiX distribution",
            "passed",
            evidence,
            "",
            "Keep MSI/WiX evidence current with the final release bundle.",
            [
                r"powershell -ExecutionPolicy Bypass -File scripts\release\build_release_package.ps1 -TauriBundleTarget msi",
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    return _gate(
        "windows_msi",
        "Windows MSI/WiX distribution",
        "blocked",
        evidence,
        (
            "Invalid Windows MSI/WiX evidence packet: " + "; ".join(errors)
            if path
            else "No Windows MSI/WiX evidence packet was found."
        ),
        "Build an MSI with WiX, verify the MSI hash, run an installer smoke, and record the MSI evidence packet.",
        [
            r"powershell -ExecutionPolicy Bypass -File scripts\release\build_release_package.ps1 -TauriBundleTarget msi",
            r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
        ],
    )


def _linux_packages_gate(root: Path) -> ReleaseGate:
    download_manifests = sorted(
        (root / "assurance/evidence").glob("determinex_download_bundle_*/download_manifest.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    download_manifest = download_manifests[0] if download_manifests else None
    download = _read_json(download_manifest) if download_manifest and download_manifest.is_file() else None
    evidence = [_rel(root, download_manifest)] if download_manifest else []
    artifact_types = _valid_download_artifact_types(root, download)
    missing_linux = [package_type for package_type in REQUIRED_LINUX_PACKAGE_TYPES if package_type not in artifact_types]
    linux_blockers = _download_artifact_type_blockers(root, download, REQUIRED_LINUX_PACKAGE_TYPES)

    if not missing_linux and not linux_blockers:
        return _gate(
            "linux_packages",
            "Linux package distribution",
            "passed",
            evidence,
            "",
            "Keep Linux package artifacts current with the final release commit.",
            [
                r"cd frontend; npm run tauri -- build --bundles appimage,deb,rpm",
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    return _gate(
        "linux_packages",
        "Linux package distribution",
        "blocked",
        evidence,
        (
            "Missing or invalid Linux package artifacts: " + ", ".join(linux_blockers)
            if linux_blockers
            else "No Linux package artifact was found in the latest download bundle manifest."
            if len(missing_linux) == len(REQUIRED_LINUX_PACKAGE_TYPES)
            else "Missing or invalid Linux package artifacts: " + ", ".join(missing_linux)
        ),
        "Build Linux AppImage, deb, and rpm package artifacts on a Linux host and refresh the download bundle manifest.",
        [
            r"cd frontend; npm run tauri -- build --bundles appimage,deb,rpm",
            r".venv\Scripts\python.exe scripts\release\package_download_bundle.py --installer-dir frontend/src-tauri/target/release/bundle --output-dir .tmp/determinex-download-bundles --evidence-dir assurance/evidence/determinex_download_bundle_20260707",
            r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
        ],
    )


def _extension_compat_errors(data: Any) -> list[str]:
    return _packet_field_errors(
        data,
        schema_version=EXTENSION_COMPAT_SCHEMA_VERSION,
        expected_true=(
            "extension_api_contract_defined",
            "vsix_import_smoke_passed",
            "open_vsx_metadata_parsed",
            "sandbox_permissions_enforced",
            "activation_event_smoke_passed",
        ),
    )


def _extension_gate(root: Path) -> ReleaseGate:
    bridge = root / "frontend/vscode-extension"
    contract = root / "docs/release/DETERMINEX_EXTENSION_COMPATIBILITY_CONTRACT.md"
    packet, data, errors = _latest_packet(
        root,
        "assurance/evidence/extension_compat",
        "extension_compat_*.json",
        _extension_compat_errors,
    )
    evidence = [_rel(root, p) for p in (bridge, contract, packet) if p is not None and p.exists()]
    if data is not None:
        return _gate(
            "extension_compat",
            "VS Code/Open VSX compatibility",
            "passed",
            evidence,
            "",
            "Keep extension import, metadata, activation, and sandbox smokes current.",
            [
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    if contract.is_file():
        return _gate(
            "extension_compat",
            "VS Code/Open VSX compatibility",
            "deferred",
            evidence,
            (
                "Invalid extension runtime compatibility packet: " + "; ".join(errors)
                if packet
                else "Extension compatibility contract exists, but runtime compatibility packet has not passed."
            ),
            "Run VSIX import, Open VSX metadata, activation-event, and sandbox permission smokes against the contract.",
            [
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    return _gate(
        "extension_compat",
        "VS Code/Open VSX compatibility",
        "deferred",
        evidence,
        "Standalone IDE does not yet import or run VS Code/Open VSX extensions.",
        "Define and implement extension compatibility/import contract.",
        [
            r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
        ],
    )


def _internal_rename_gate(root: Path) -> ReleaseGate:
    project = root / "PROJECT.md"
    migration = root / "docs/release/DETERMINEX_INTERNAL_RENAME_MIGRATION.md"
    evidence = [_rel(root, p) for p in (project, migration) if p.is_file()]
    text = project.read_text(encoding="utf-8", errors="replace") if project.is_file() else ""
    if "Literal `determinex_*`/`DETERMINEX_*`" in text:
        return _gate(
            "internal_rename",
            "Internal Determinex rename",
            "deferred",
            evidence,
            "Legacy determinex_* and DETERMINEX_* implementation identifiers remain by project contract.",
            "Execute the internal rename migration with compatibility aliases and migration tests.",
            [
                "rg \"determinex_|DETERMINEX_\"",
                r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
            ],
        )
    return _gate(
        "internal_rename",
        "Internal Determinex rename",
        "passed",
        evidence,
        "",
        "Keep compatibility aliases for older scripts and evidence.",
        [
            r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
        ],
    )


def _programbench_rows(root: Path) -> list[dict[str, Any]]:
    path = root / "corpus/programbench/eval_index.json"
    data = _read_json(path)
    if isinstance(data, list):
        rows = data
    elif isinstance(data, dict):
        rows = list(data.values())
    else:
        return []
    return [row for row in rows if isinstance(row, dict)]


def _programbench_200_gate(root: Path) -> ReleaseGate:
    path = root / "corpus/programbench/eval_index.json"
    evidence = [_rel(root, path)] if path.is_file() else []
    rows = _programbench_rows(root)
    if not rows:
        return _gate(
            "programbench_200",
            "ProgramBench 200/200 strict locks",
            "deferred",
            evidence,
            "No readable ProgramBench eval_index.json was found.",
            "Deferred for this open-source launch profile; restore ProgramBench evidence before making benchmark claims.",
            [
                r".venv\Scripts\python.exe scripts\pb_doc_count_check.py --verbose",
                r".venv\Scripts\python.exe scripts\pb_board_guard.py --guard",
                r".venv\Scripts\python.exe scripts\pb_override_scan.py --guard",
            ],
        )
    canonical = [row for row in rows if not row.get("alias_of") and not row.get("canonical_slug")]
    strict_count = sum(1 for row in canonical if row.get("official_full_suite_resolved") is True)
    status_counts = Counter(str(row.get("status")) for row in canonical)
    status_summary = ", ".join(f"{status}={count}" for status, count in status_counts.most_common(6))
    if len(canonical) == PROGRAMBENCH_DENOMINATOR and strict_count == PROGRAMBENCH_DENOMINATOR:
        return _gate(
            "programbench_200",
            "ProgramBench 200/200 strict locks",
            "passed",
            evidence,
            "",
            "Keep ProgramBench guards green and archive only official full-suite locks.",
            [
                r".venv\Scripts\python.exe scripts\pb_doc_count_check.py --verbose",
                r".venv\Scripts\python.exe scripts\pb_board_guard.py --guard",
                r".venv\Scripts\python.exe scripts\pb_override_scan.py --guard",
            ],
        )
    denominator_note = (
        ""
        if len(canonical) == PROGRAMBENCH_DENOMINATOR
        else f"; canonical non-alias rows={len(canonical)}, expected={PROGRAMBENCH_DENOMINATOR}"
    )
    return _gate(
        "programbench_200",
        "ProgramBench 200/200 strict locks",
        "deferred",
        evidence,
        (
            f"ProgramBench strict official locks are {strict_count}/{PROGRAMBENCH_DENOMINATOR}"
            f"{denominator_note}; current non-authorizing status mix: {status_summary or 'none'}."
        ),
        "Deferred for this open-source launch profile; continue the official lock campaign before making ProgramBench claims.",
        [
            r".venv\Scripts\python.exe scripts\pb_doc_count_check.py --verbose",
            r".venv\Scripts\python.exe scripts\pb_board_guard.py --guard",
            r".venv\Scripts\python.exe scripts\pb_override_scan.py --guard",
        ],
    )


def _swebench_packet_errors(data: Any) -> list[str]:
    if not isinstance(data, dict):
        return ["packet JSON must be an object"]
    errors: list[str] = []
    if data.get("schema_version") != SWEBENCH_FRESH_PUBLICATION_SCHEMA_VERSION:
        errors.append(f"schema_version must be {SWEBENCH_FRESH_PUBLICATION_SCHEMA_VERSION}")
    if data.get("benchmark") != "SWE-bench_Lite":
        errors.append("benchmark must be SWE-bench_Lite")
    expected_true = ("fresh_rerun_completed", "official_harness_used", "publication_claim_ready")
    for field_name in expected_true:
        if data.get(field_name) is not True:
            errors.append(f"{field_name} must be true")
    if data.get("authority_granted") is not False:
        errors.append("authority_granted must be false")
    modes = data.get("privacy_modes_completed")
    if not isinstance(modes, list) or not SWEBENCH_REQUIRED_PRIVACY_MODES.issubset({str(m) for m in modes}):
        errors.append("privacy_modes_completed must include B-Uncloaked, RegionControl, and Cloaked")
    reports = data.get("reports")
    if not isinstance(reports, list) or not reports:
        errors.append("reports must list the official rerun report paths")
    return errors


def _swebench_fresh_gate(root: Path) -> ReleaseGate:
    candidates = sorted(
        (root / "assurance/evidence/swebench_fresh_publication").glob("swebench_fresh_publication_*.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    first_invalid: tuple[Path, list[str]] | None = None
    for candidate in candidates:
        data = _read_json(candidate)
        errors = _swebench_packet_errors(data)
        if not errors:
            return _gate(
                "swebench_fresh",
                "Fresh SWE-bench publication reruns",
                "passed",
                [_rel(root, candidate)],
                "",
                "Keep the official SWE-bench rerun packet current with the release claim snapshot.",
                [
                    "python -m swebench.harness.run_evaluation --dataset_name princeton-nlp/SWE-bench_Lite --split test",
                    r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
                ],
            )
        if first_invalid is None:
            first_invalid = (candidate, errors)
    evidence = [_rel(root, first_invalid[0])] if first_invalid else []
    blocker = (
        "Invalid fresh SWE-bench publication packet: " + "; ".join(first_invalid[1])
        if first_invalid
        else "No fresh official SWE-bench privacy-mode rerun packet was found."
    )
    return _gate(
        "swebench_fresh",
        "Fresh SWE-bench publication reruns",
        "deferred",
        evidence,
        blocker,
        "Deferred for this open-source launch profile; run fresh official SWE-bench Lite reruns before making SWE-bench claims.",
        [
            "python -m swebench.harness.run_evaluation --dataset_name princeton-nlp/SWE-bench_Lite --split test",
            r".venv\Scripts\python.exe scripts\verified_task\swebench_result_ingest.py --report <report.json> --predictions <predictions.jsonl>",
            r".venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json",
        ],
    )


def collect(root: Path | str | None = None) -> ReleaseGateReport:
    repo_root = Path(root) if root is not None else Path(__file__).resolve().parents[2]
    gates = (
        _sbom_gate(repo_root),
        _installer_gate(repo_root),
        _windows_trust_gate(repo_root),
        _legal_public_distribution_gate(repo_root),
        _windows_msi_gate(repo_root),
        _linux_packages_gate(repo_root),
        _clean_host_gate(repo_root),
        _first_e2e_gate(repo_root),
        _programbench_200_gate(repo_root),
        _swebench_fresh_gate(repo_root),
        _extension_gate(repo_root),
        _internal_rename_gate(repo_root),
    )
    release_ready = all(g.status in {"passed", "deferred"} for g in gates)
    return ReleaseGateReport(
        schema_version=SCHEMA_VERSION,
        generated_at_utc=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        product_name="Determinex",
        release_ready=release_ready,
        authority_granted=False,
        gates=gates,
        notes=(
            "This report is a local evidence classifier, not a release approval.",
            "A passed individual gate does not override claim boundaries or protected action packets.",
            "ProgramBench, SWE-bench Lite, and SWE-bench Pro are deferred proof tracks for this open-source launch profile.",
        ),
    )


def write_report(output_path: Path, root: Path | str | None = None) -> ReleaseGateReport:
    report = collect(root)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report.to_dict(), indent=2), encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    report = collect(args.root)
    payload = json.dumps(report.to_dict(), indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
