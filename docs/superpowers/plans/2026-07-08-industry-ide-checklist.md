# Industry IDE Checklist Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a repo-backed, app-visible audit checklist for the work needed to make Determinex a top-tier proof-governed IDE.

**Architecture:** Keep checklist truth in one typed frontend data module and render it inside the existing Successor Roadmap panel. The checklist is status-only and must not grant release readiness; each completed or partial item must cite evidence, blockers, or next actions.

**Tech Stack:** TypeScript, React, Vitest, Testing Library, Markdown release docs.

---

### Task 1: Add The Typed Checklist Data

**Files:**
- Create: `frontend/src/lib/industryIdeBacklog.ts`
- Test: `frontend/src/lib/__tests__/industryIdeBacklog.test.ts`

- [ ] **Step 1: Write the checklist module**

Create `frontend/src/lib/industryIdeBacklog.ts` with status types, category ids, checklist items, and summary helpers.

- [ ] **Step 2: Write data contract tests**

Create `frontend/src/lib/__tests__/industryIdeBacklog.test.ts` verifying all checked items have evidence, blocked items have blockers, and next-action ordering returns unfinished items first.

- [ ] **Step 3: Run focused tests**

Run: `npm.cmd test -- --run src/lib/__tests__/industryIdeBacklog.test.ts`
Expected: pass.

### Task 2: Render Checklist In The Existing Roadmap Panel

**Files:**
- Modify: `frontend/src/components/SuccessorRoadmapPanel.tsx`
- Test: `frontend/src/components/__tests__/SuccessorRoadmapPanel.test.tsx`

- [ ] **Step 1: Import checklist data**

Import checklist categories, items, summary counts, and label helpers from `industryIdeBacklog.ts`.

- [ ] **Step 2: Add a visible checklist section**

Render category summaries and the highest-priority unfinished checklist items below the existing successor locks.

- [ ] **Step 3: Extend UI tests**

Assert the panel renders the checklist heading, at least one blocked P0 item, and does not mark all items done.

- [ ] **Step 4: Run frontend tests and build**

Run: `npm.cmd test -- --run`
Expected: all tests pass.

Run: `npm.cmd run build`
Expected: production build passes.

### Task 3: Add A Durable Audit Document

**Files:**
- Create: `docs/release/DETERMINEX_INDUSTRY_IDE_AUDIT.md`

- [ ] **Step 1: Add the audit summary**

Create a release document that explains the checklist status boundary, checked-off items, and next execution order.

- [ ] **Step 2: Run claim scanner**

Run: `.venv\Scripts\python.exe scripts\claim_scanner\day_one_public_claim_scanner.py --print`
Expected: `DAY_ONE_PUBLIC_CLAIM_SCANNER_PASSED`.

### Task 4: Commit And Push

**Files:**
- Modified and created files from Tasks 1-3.

- [ ] **Step 1: Inspect diff**

Run: `git diff --stat`
Expected: only checklist data, roadmap panel/test, and release audit doc changed.

- [ ] **Step 2: Commit**

Run: `git add ...` then `git commit -m "Add industry IDE release checklist"`
Expected: commit succeeds.

- [ ] **Step 3: Push**

Run: `git push origin mojibake-and-count-fix`
Expected: branch pushes.

---

Self-review:
- Spec coverage: covers audit, check-off list, app-visible status, durable doc, and verification.
- Placeholder scan: no task uses TBD/TODO language.
- Type consistency: `IndustryIdeBacklogItem`, status labels, and summary helpers are defined before use.
