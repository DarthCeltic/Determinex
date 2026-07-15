# Determinex Internal Rename Migration

Status: migration contract defined, mechanical rename pending.

Determinex is the public product name. Legacy `determinex_*` and `DETERMINEX_*` identifiers still exist in script names, environment variables, model tags, evidence paths, and historical artifacts. This document defines the safe migration bar; it does not claim the rename is complete.

## Migration Rules

- Preserve historical evidence paths and lock archives as immutable records.
- Add compatibility aliases before removing legacy command names.
- Rename user-facing strings before internal identifiers when both cannot move in one commit.
- Keep environment variable aliases for at least one release cycle.
- Do not rename benchmark evidence, corpus rows, or signed artifacts in place.

## Required Passing Evidence

The `internal_rename` release gate may pass only when:

- Project contract no longer declares legacy `determinex_*`/`DETERMINEX_*` identifiers as active implementation names.
- Compatibility aliases exist for old command names that remain documented.
- Migration tests cover at least script entry points, environment variables, Tauri commands, frontend labels, and installer metadata.
- Generated release evidence references Determinex as the product name.

## Non-Claims

- A migration contract is not a completed rename.
- A completed public rename does not authorize deleting historical evidence.
- A completed internal rename does not grant release readiness without the other release gates.
