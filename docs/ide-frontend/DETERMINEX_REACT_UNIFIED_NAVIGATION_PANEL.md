# React Unified Navigation Panel

> Locked under
> `locks/sentinel/DETERMINEX_REACT_UNIFIED_NAVIGATION_PANEL_LOCK_001.json`.

Rung 2. Live React shell for the five product surfaces at
`frontend/src/components/ide-product-shell/UnifiedNavigationPanel.tsx`.

## Five tabs

- Idea Lab
- Repo Clinic
- Maintenance Bay
- Learning Studio
- Proof / Operator Center

## Per-surface display

Each tab shows:

- `unified-navigation-purpose`
- `unified-navigation-blocked-states` (enumerated)
- `unified-navigation-what-is-allowed`
- `unified-navigation-what-is-not-authorized` (source_mutation_boundary + training_eligibility_boundary text)
- `unified-navigation-ready-does-not-mean-authorized` ("Ready does NOT mean authorized.")
- `unified-navigation-claim-caveats`

Bottom: `unified-navigation-authority-vocabulary` (shared 8-class set).

## Hard rules (test-enforced)

- All five surfaces render or `BLOCKED_MISSING_SURFACE` banner shows
- Negative-authority text rendered on every surface
- "Ready does NOT mean authorized." constant present
- No forbidden success phrases ("All set!", "Source mutation enabled", "Training enabled", "Ready means authorized")
- No mutating Tauri command invoked from this panel
- API lib refuses backend responses claiming `source_mutation_authorized=true` or `training_eligible=true`
