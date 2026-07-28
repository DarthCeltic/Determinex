# Full Release Closure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a deterministic release-closure runner that executes the remaining local release preflights, updates evidence, and refuses to mark Determinex public-release ready while protected gates remain blocked.

**Architecture:** Add a focused `scripts/release/full_release_closure.py` script that validates the current download bundle, probes clean-runner availability, writes fresh evidence, and wraps the existing `determinex_release_gates.py` collector. Keep gate authority centralized in `determinex_release_gates.py`, with a narrow update so clean-host status can distinguish stale Docker failure from missing clean-host install proof.

**Tech Stack:** Python standard library, pytest, existing release evidence JSON files.

---

### Task 1: Clean-Host Preflight Evidence

**Files:**
- Modify: `scripts/release/determinex_release_gates.py`
- Test: `tests/test_determinex_release_gates.py`

- [ ] **Step 1:** Add latest runner preflight discovery under `assurance/evidence/clean_host_fresh_install_runner_execution/runner_preflight_*.json`.
- [ ] **Step 2:** Keep `clean_host` blocked when Docker is available but no install transcript exists.
- [ ] **Step 3:** Add a pytest fixture proving the blocker changes from stale Docker-health failure to missing install/launch/uninstall proof.
- [ ] **Step 4:** Run `pytest tests/test_determinex_release_gates.py -q`.

### Task 2: Full Release Closure Runner

**Files:**
- Create: `scripts/release/full_release_closure.py`
- Create: `tests/test_full_release_closure.py`

- [ ] **Step 1:** Add a bundle verifier for the latest `determinex_download_bundle_*/download_manifest.json`.
- [ ] **Step 2:** Add a Docker clean-runner probe that writes `runner_preflight_<date>.json`.
- [ ] **Step 3:** Add a closure report with `release_ready: false`, `authority_granted: false`, blocked/partial gate IDs, protected external blockers, and next executable actions.
- [ ] **Step 4:** Add tests proving the runner validates ZIP checksums and does not grant authority.
- [ ] **Step 5:** Run `pytest tests/test_full_release_closure.py tests/test_determinex_release_gates.py -q`.

### Task 3: Fresh Evidence And Verification

**Files:**
- Create/Update: `assurance/evidence/clean_host_fresh_install_runner_execution/runner_preflight_20260707.json`
- Create/Update: `assurance/evidence/full_release_closure/run_20260707.json`
- Update: `assurance/evidence/determinex_release_gate_status/release_gates_20260707.json`

- [ ] **Step 1:** Run `.venv\Scripts\python.exe scripts\release\full_release_closure.py --output assurance\evidence\full_release_closure\run_20260707.json`.
- [ ] **Step 2:** Run `.venv\Scripts\python.exe scripts\release\determinex_release_gates.py --output assurance\evidence\determinex_release_gate_status\release_gates_20260707.json`.
- [ ] **Step 3:** Run focused pytest, claim scanner, evidence index, and overclaim guard before commit.
