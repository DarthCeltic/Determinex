# Determinex Mission Control Design

## Goal

Build a first interactive guide surface for Determinex that helps users choose a mission, understand the current blocker, find the exact evidence, and run the right verification command without implying release readiness.

## Scope

This slice adds a frontend Mission Control panel backed by existing release gate data. It does not execute shell commands from the browser. Command execution requires a separate permissioned Tauri command path and is intentionally outside this slice.

## Architecture

`frontend/src/lib/missionControl.ts` defines mission metadata and derives gate details from `DETERMINEX_RELEASE_GATES`. `frontend/src/components/MissionControlPanel.tsx` renders selectable missions, status counts, runbook commands, evidence paths, and proof-boundary text. The main IDE shell exposes Mission Control as an attachable runtime panel and command-palette command.

## Data Flow

The panel imports the static frontend release gate snapshot from `releaseGateStatus.ts`. Mission definitions reference gate ids and roadmap pillar ids. The renderer resolves gate ids into full gate records at runtime and displays current blocker, next action, evidence, and runbook commands directly from the collector-backed snapshot.

## Error Handling

If a mission references a missing gate id, the resolver drops it instead of rendering fabricated state. Tests assert that every current mission resolves at least one gate and that release readiness remains false.

## Testing

Vitest covers the mission resolver, claim boundary, default render, tab switching, runbook commands, and exact first E2E blocker text.
