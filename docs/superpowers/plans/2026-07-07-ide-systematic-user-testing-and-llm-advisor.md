# IDE Systematic User Testing And LLM Advisor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a native, evidence-bounded test/audit lane for user-facing IDE workflows and a model-neutral advisory packet generator that can brief any LLM on creating, maintaining, or repairing a program.

**Architecture:** Keep advisory generation deterministic and local: inspect workspace signals, classify the user intent, emit a structured packet, and preserve proof boundaries. Add a separate systematic audit script that checks visible IDE surfaces, command wiring, release gates, and advisory boundaries, then writes a JSON evidence artifact.

**Tech Stack:** Python stdlib, existing `scripts/ide` command surface, React/TypeScript static Mission Control data, pytest, existing governance/evidence checks.

---

### Task 1: Native LLM Program Advisory Packet

**Files:**
- Create: `scripts/ide/llm_program_advisor.py`
- Modify: `scripts/ide/backend_command_surface.py`
- Test: `tests/ide/test_llm_program_advisor_lock.py`
- Test: `tests/ide/test_ide_backend_command_surface_lock.py`

- [ ] Add tests that the advisor emits `creation`, `upkeep`, and `repair` intents, includes verifier-first instructions, keeps `source_mutation_authorized` and `training_eligible` false, and avoids universal verified-support claims.
- [ ] Implement the advisor dataclass and packet builder.
- [ ] Wire backend command `generate_llm_program_advisory`.
- [ ] Run the focused pytest files and confirm passing output.

### Task 2: Systematic IDE User Audit Evidence

**Files:**
- Create: `scripts/ide/systematic_ide_user_audit.py`
- Create: `tests/ide/test_systematic_ide_user_audit_lock.py`
- Create during verification: `assurance/evidence/systematic_ide_user_audit/run_20260707.json`

- [ ] Add tests that the audit covers Mission Control, Tools Hub, release gates, backend command surface, repair panels, provider routing, and LLM advisory boundaries.
- [ ] Implement the audit collector with deterministic pass/fail checks and exact blockers.
- [ ] Generate the evidence JSON.
- [ ] Run evidence index and overclaim guards.

### Task 3: Mission Control Surface Binding

**Files:**
- Modify: `frontend/src/lib/missionControl.ts`
- Modify: `frontend/src/components/MissionControlPanel.tsx` if needed
- Test: `frontend/src/components/__tests__/MissionControlPanel.test.tsx`

- [ ] Add a mission for `llm-program-advisor` that tells users how to brief any model while preserving verifier and support boundaries.
- [ ] Assert the mission appears in Mission Control tests.
- [ ] Run frontend tests, TypeScript, and production build.

### Task 4: Commit And Push

**Files:**
- Commit only scoped files above plus generated evidence.

- [ ] Run final verification commands.
- [ ] Commit with a release-hardening message.
- [ ] Push branch.
