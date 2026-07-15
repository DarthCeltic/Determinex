# Installer Proof

**Status:** `PROOF_CENTER_ROUTE_MOUNTED_AND_VERIFIED` (corrected 2026-06-30 -- see below)
**Last checked UTC:** `2026-06-30` (superseding the 2026-06-02 blocker below)

This page records what the current Determinex installer evidence proves and what remains blocked.

## Correction (2026-06-30)

The "exact blocker" below (route not mounted) is stale and no longer accurate:

1. `frontend/src/app/page.tsx` currently links directly to `/proof-center/`, and
   `frontend/src/app/proof-center/page.tsx` exists, builds, and statically generates
   cleanly (`npm run build`: all 4 routes including `/proof-center` compile and
   prerender, verified 2026-06-30).
2. Pre-existing evidence already on disk from the *same day* this blocker was
   recorded shows a real installed-app session successfully navigating to
   `/proof-center` and rendering its content:
   `assurance/evidence/proof_center_installed_app_gui_smoke_001/proof_center_installed_app_rebuilt_transcript_20260602.json`
   -- a real `tauri.localhost` origin, `webSocketDebuggerUrl`, and captured page
   body starting `"Proof / Operator Center\nRefresh\nEvidence ledger..."`.

The `proof-center` page itself was separately found today to have hardcoded a
previously-claimed, now-invalidated ProgramBench figure (64/200 locks) directly
in its UI source -- fixed in the same session, see `docs/papers/PROGRAMBENCH.md`'s correction
banner and the commit correcting `frontend/src/app/proof-center/page.tsx`.
Route mounting and content correctness are two different claims; this page
now only speaks to route mounting.

## Exact Blocker (historical, resolved -- kept for record)

The installed-app Proof Center smoke was blocked because `frontend/src/app/page.tsx` did not mount the Proof / Operator Center route, as of the 2026-06-02 pre-rebuild evidence capture.

Existing route-binding evidence:

- `assurance/evidence/release_cell_mutation_proof_center_full_status_distribution_preflight_wave_001/proof_center_installed_app_route_binding_20260602.json`
- exact blocker (historical): `installed_app_proof_center_route_not_mounted_in_app_page`

## Required Before A Pass

To pass this lane, the app must show the Proof / Operator Center from the installed app and visibly surface:

- installer proof status
- GUI smoke status
- SBOM status
- clean-runner status
- release-cell status
- queue/spend status
- known-world detector status
- claim scanner status
- public distribution go/no-go status

No fake screenshot or UI-only status is accepted.

## Non-Claims

This page does not claim:

- public release readiness
- beta readiness
- signed/trusted installer proof
- clean-host install proof
- Proof Center installed-app smoke pass
- full `tests/status` completion
- universal support
- broad family support
