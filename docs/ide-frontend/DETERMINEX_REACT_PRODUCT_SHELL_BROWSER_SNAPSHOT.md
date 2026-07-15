# React Product Shell — Browser Snapshot

> Locked under
> `locks/sentinel/DETERMINEX_REACT_PRODUCT_SHELL_BROWSER_SNAPSHOT_LOCK_001.json`.

Rung 1 of `DETERMINEX_LIVE_REACT_PRODUCT_SHELL_DEMO_READINESS_SERIES`.

## Browser tooling unavailable

The repo does not currently have Playwright, Vitest + jsdom, or
Storybook wired. A deferred finding records the gap:
`assurance/evidence/deferred_findings/claude_lane_finding_browser_snapshot_tooling_unavailable_20260528.json`.

Per the campaign spec ("If browser snapshot tooling is unavailable,
write explicit blocker and provide strongest available
component-render tests"), this lock provides the strongest static /
TSX-content coverage across all eight mounted panels.

## What is verified

For every panel:

- File exists, exports a default component, declares `*_STATUS_TOKENS`.
- At least one `BLOCKED_*` / `DISABLED_*` / `MISSING_*` / `UNDISCLOSED` / `PENDING` / `UNSUPPORTED` / `REQUIRED` label is in the rendered output.
- `READY_DOES_NOT_MEAN_AUTHORIZED` caption (every non-splash panel).
- `training_eligible: false` (or equivalent) surfaced.
- No mutating Tauri verb (`apply_source` / `approve_packet` / `write_training_row` / `grant_authorization` / `release_workflow` / `run_programbench`).

In the navigation panel:

- All five surface keys + human labels.

In the splash demo:

- Tagline **"Proof Before Mutation"** (h2 + `data-tagline` attribute).
- Phrase **"Generated is not verified."**
- Phrase **"Working means build/test/smoke passed."**
- The four "does NOT prove" caveats.
