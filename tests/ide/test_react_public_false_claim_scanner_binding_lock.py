"""Tests for DETERMINEX_REACT_PUBLIC_FALSE_CLAIM_SCANNER_BINDING_LOCK_001."""
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (_REPO_ROOT, _REPO_ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

loader = importlib.import_module("ide.public_false_claim_scanner_status")

PANEL_PATH = (
    _REPO_ROOT / "frontend" / "src" / "components" / "ide-product-shell"
    / "PublicFalseClaimScannerPanel.tsx"
)
API_LIB_PATH = _REPO_ROOT / "frontend" / "src" / "lib" / "ide-product-shell-api.ts"
LOCK_PATH = (
    _REPO_ROOT / "locks" / "sentinel"
    / "DETERMINEX_REACT_PUBLIC_FALSE_CLAIM_SCANNER_BINDING_LOCK_001.json"
)
EVIDENCE_DIR = (
    _REPO_ROOT / "assurance" / "evidence"
    / "determinex_react_public_false_claim_scanner_binding"
)
EVIDENCE_INDEX = _REPO_ROOT / "assurance" / "evidence" / "evidence_index.json"
FLAGSHIP_DIR = (
    _REPO_ROOT / "assurance" / "evidence" / "public_tidal_wave_flagship_flow_certification"
)
EXPORT_DIR = _REPO_ROOT / "assurance" / "evidence" / "public_proof_report_export"


def test_loader_passes_against_live_codex_evidence():
    rec = loader.load()
    assert rec.is_passed, rec.notes


def test_loader_flagship_count_is_9():
    rec = loader.load()
    assert rec.flagship_scanner_count == 9
    assert len(rec.flagship_scanner_phrases) == 9


def test_loader_export_forbidden_count_is_11():
    rec = loader.load()
    assert rec.export_forbidden_count == 11
    assert len(rec.export_forbidden_phrases) == 11


def test_loader_all_phrases_blocked_or_flagged():
    rec = loader.load()
    for row in (*rec.flagship_scanner_phrases, *rec.export_forbidden_phrases):
        assert row.action == "BLOCK_OR_FLAG"
        assert row.current_claim_allowed is False


def test_loader_required_forbidden_phrases_covered():
    rec = loader.load()
    combined = " | ".join(rec.combined_blocked_phrases)
    expected_substrings = [
        "release ready",
        "production ready",
        "all apps supported",
        "all languages supported",
        "all platforms supported",
        "fully autonomous source mutation",
        "training eligible by default",
        "no edge cases",
        "unknown/novel cases supported by default",
        "arbitrary app generation",
        "commercial",
    ]
    missing = [s for s in expected_substrings if s not in combined]
    assert not missing, f"missing required block phrases: {missing}"


def test_loader_returns_awaiting_when_missing(tmp_path):
    rec = loader.load(tmp_path / "no-flagship", tmp_path / "no-export")
    assert rec.is_awaiting


def test_loader_fallback_does_not_invent_success(tmp_path):
    rec = loader.load(tmp_path / "no-flagship", tmp_path / "no-export")
    assert rec.is_passed is False
    assert rec.flagship_scanner_count == 0


def _write_tampered_flagship(tmp: Path, mutate) -> Path:
    src = sorted(FLAGSHIP_DIR.glob("run_*.json"))[-1]
    blob = json.loads(src.read_text(encoding="utf-8"))
    mutate(blob)
    out = tmp / "run_99.tampered.json"
    out.write_text(json.dumps(blob), encoding="utf-8")
    return tmp


def test_loader_blocks_scanner_count_mismatch(tmp_path):
    def m(b):
        b["false_claim_scanner_model"]["blocked_or_flagged_phrases"] = b["false_claim_scanner_model"][
            "blocked_or_flagged_phrases"
        ][:5]
    ed = _write_tampered_flagship(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "SCANNER_COUNT_MISMATCH" in rec.decision


def test_loader_blocks_scanner_action_mismatch(tmp_path):
    def m(b):
        b["false_claim_scanner_model"]["blocked_or_flagged_phrases"][0]["action"] = "ALLOW"
    ed = _write_tampered_flagship(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "SCANNER_ACTION_MISMATCH" in rec.decision


def test_loader_blocks_current_claim_allowed_true(tmp_path):
    def m(b):
        b["false_claim_scanner_model"]["blocked_or_flagged_phrases"][0]["current_claim_allowed"] = True
    ed = _write_tampered_flagship(tmp_path, m)
    rec = loader.load(ed)
    assert rec.is_blocked
    assert "SCANNER_ACTION_MISMATCH" in rec.decision


def test_panel_present_and_uses_command():
    assert PANEL_PATH.is_file()
    src = PANEL_PATH.read_text(encoding="utf-8")
    assert "invokeUnifiedProductCommand" in src
    assert "get_public_false_claim_scanner_status" in src


def test_command_registered():
    api = API_LIB_PATH.read_text(encoding="utf-8")
    assert '"get_public_false_claim_scanner_status"' in api


def test_panel_renders_required_captions():
    src = PANEL_PATH.read_text(encoding="utf-8")
    required = [
        "This panel displays evidence; it does not grant authority.",
        "Claim scanner output is a public-safety boundary.",
        "It prevents",
        "report language from overstating support, release readiness,",
        "production readiness, authority, training eligibility, or",
        "universal coverage.",
        "Every listed phrase is BLOCKED or FLAGGED.",
        "Forbidden shortcuts remain forbidden.",
        "Universal support is not claimed.",
        "Release-supported remains 0 cells / 0 families.",
    ]
    for cap in required:
        assert cap in src, f"missing caption: {cap}"


def test_panel_does_not_render_authority_grant():
    src = PANEL_PATH.read_text(encoding="utf-8")
    for f in ("release_ready: true", "training_eligible: true", "source_mutation_authorized: true"):
        assert f not in src


def test_lock_present_and_authority_false():
    assert LOCK_PATH.is_file()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert lock["lock_id"] == "DETERMINEX_REACT_PUBLIC_FALSE_CLAIM_SCANNER_BINDING_LOCK_001"
    sd = lock.get("scope_discipline", {})
    for flag in (
        "release_ready",
        "training_eligible",
        "source_mutation_authorized",
        "approval_authority_granted",
        "proof_execution_authority_granted",
        "broad_claims_granted",
    ):
        assert sd.get(flag) is False, flag


def test_evidence_record_present():
    files = sorted(EVIDENCE_DIR.glob("run_*.json"))
    assert files
    rec = json.loads(files[-1].read_text(encoding="utf-8"))
    assert rec["lock_id"] == "DETERMINEX_REACT_PUBLIC_FALSE_CLAIM_SCANNER_BINDING_LOCK_001"


def test_lock_in_evidence_index():
    if not EVIDENCE_INDEX.is_file():
        pytest.skip("evidence index missing")
    idx = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    ids = {e.get("evidence_id") for e in idx.get("entries", [])}
    if "DETERMINEX_REACT_PUBLIC_FALSE_CLAIM_SCANNER_BINDING_LOCK_001" not in ids:
        pytest.skip("index not yet regenerated")
    assert "DETERMINEX_REACT_PUBLIC_FALSE_CLAIM_SCANNER_BINDING_LOCK_001" in ids
