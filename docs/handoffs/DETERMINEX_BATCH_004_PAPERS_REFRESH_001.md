# DETERMINEX_BATCH_004_PAPERS_REFRESH_001

- Mission: `DETERMINEX_BATCH_004_SYNC_FIRST_PROMOTION_PROGRAMBENCH_AND_RELEASE_FAMILY_PATH`.
- Date: `2026-06-03`.
- Purpose: refresh public-facing and paper-facing docs after the sync-first Batch 004 promotion attempt and ProgramBench keifu strict-lock archival.

## Updated Surfaces

- `README.md`
- `CLAUDE.md`
- `CHANGELOG.md`
- `docs/README.md`
- `docs/papers/PROGRAMBENCH.md`
- `docs/papers/WHITE_PAPER.md`
- `docs/papers/ARCHITECTURE.md`
- `corpus/programbench/README.md`

## Current Truth

- ProgramBench strict locks: `56`.
- Score=100 unarchived rows: `0`.
- Factory-accepted nonlocked rows: `70`.
- Aggregate runnable score: `84,957 / 161,099 = 52.74%`.
- Release-supported cells: `13`.
- Release-supported families: `0`.
- All-gap Batch 004 promotions passed: `1`, limited to `determinex_surface_claim_scanner`.
- Monolithic `tests/status`: attempted, timed out near 38%, not a pass.

## Boundaries Preserved

- No ProgramBench total-100 claim.
- No all-gaps-closed claim.
- No family-support claim.
- No full monolithic status-suite claim.
- No signed/trusted installer or clean-host install claim.
- Open availability remains false.
- `PATENT_FILED` remains false.
