# DETERMINEX Historical 10 / Current 13 Release-Cell Truth Closure 001

**Wave:** `DETERMINEX_100_PERCENT_COMPLETION_RELEASE_AND_PUBLIC_LAUNCH_PREP_WAVE_001`
**Lane:** C - Historical 10-cell vs current 13-cell migration
**Status:** `HISTORICAL_CURRENT_RELEASE_CELL_TRUTH_SEPARATED`
**Timestamp UTC:** `2026-06-02T22:17:45Z`
**Closure commit basis:** `847dfba96`
**Current HEAD during closure note:** `02cb01d8a`

## Closure

Historical artifacts may still report `10` release-supported exact cells.

Current registry truth reports `13` release-supported exact cells and `0` release-supported families.

Those statements are both true in their own time boundary:

- historical proof records produced before the three-cell promotion can remain `10`
- current source truth is `scripts/proof/release_cell_registry.py`
- current canonical release-supported exact cells are `13`
- current release-supported families remain `0`

No historical evidence was rewritten into fake current truth.

## Test Doctrine

Tests may assert historical `10` separately from current `13`.

The accepted pattern is:

- assert the historical record count exactly where the artifact is historical
- assert the current canonical registry count exactly where current authority is being tested
- permit bounded historical compatibility only when paired with an exact historical pin and an exact current registry pin
- keep release-supported families strict at `0`

The rejected pattern is:

- using `<= 13` as the only assertion for a current artifact
- converting old evidence to pretend it was generated under the 13-cell registry
- inferring family support from exact-cell promotion
- inferring public package readiness, clean-host readiness, or release readiness from exact-cell promotion

## Verified Boundary

Lane A committed the dirty-state reconciliation in `847dfba96`:

- 39 historical/current migration files
- one Codex dirty-state triage marker
- focused dirty-slice status tests passed
- stale invariant regression sweep passed
- anti-god, evidence index, evidence validate, append-only ledger, count drift guard, and day-one claim scanner passed

Lane B added the missing registry signoff marker in `02cb01d8a`:

- `assurance/evidence/release_registry_mutation_signoff_lock_001/run_20260602.RELEASE_REGISTRY_MUTATION_SIGNOFF_LOCK_001.json`
- `docs/handoffs/DETERMINEX_RELEASE_REGISTRY_MUTATION_SIGNOFF_LOCK_001_REPORT.md`
- `locks/sentinel/DETERMINEX_RELEASE_REGISTRY_MUTATION_SIGNOFF_LOCK_001.json`

## Non-Claims

This closure does not claim:

- full `tests/status` completion
- public release readiness
- beta readiness
- broad family support
- universal support
- signed/trusted installer proof
- clean-host install proof
- Proof Center installed-app smoke
- training eligibility
- source mutation authority

## Final Rule

Historical truth remains historical. Current truth remains registry-bound. Promotion requires exact proof, and blockers remain exact blockers.
