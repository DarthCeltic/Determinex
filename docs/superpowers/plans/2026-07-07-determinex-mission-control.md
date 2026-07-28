# Determinex Mission Control Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a release-gate-backed interactive guide panel to the Determinex IDE.

**Architecture:** Create a small mission data layer, render it in a React panel, attach the panel to the existing add-on dock, and test the guide behavior. The panel reads existing release gate data and does not create new readiness authority.

**Tech Stack:** Next.js, React, TypeScript, lucide-react, Vitest, Testing Library.

---

### Task 1: Mission Data Model

**Files:**
- Create: `frontend/src/lib/missionControl.ts`
- Test: `frontend/src/components/__tests__/MissionControlPanel.test.tsx`

- [x] Define mission types and mission records.
- [x] Resolve gate ids to current `DETERMINEX_RELEASE_GATES` records.
- [x] Derive mission status counts and completion totals.

### Task 2: Mission Control Panel

**Files:**
- Create: `frontend/src/components/MissionControlPanel.tsx`
- Test: `frontend/src/components/__tests__/MissionControlPanel.test.tsx`

- [x] Render mission tabs with status labels and selected-state styling.
- [x] Render selected mission objective, user outcome, proof boundary, current gates, runbook commands, evidence paths, and next actions.
- [x] Keep visible product naming as Determinex and use legacy implementation names only inside real command/path strings.

### Task 3: IDE Integration

**Files:**
- Modify: `frontend/src/app/page.tsx`
- Modify: `frontend/src/components/ToolsHub.tsx`

- [x] Add Mission Control to the attachable add-on union.
- [x] Add a command-palette entry for Mission Control.
- [x] Add a Tools Hub card for Mission Control.
- [x] Include the panel in the runtime toolbar.

### Task 4: Verification

**Files:**
- Test: `frontend/src/components/__tests__/MissionControlPanel.test.tsx`

- [x] Run focused Vitest coverage for Mission Control and the existing roadmap panel.
- [x] Run TypeScript check for frontend integration.
- [x] Run release proof guards that are cheap and relevant to claim boundaries.
