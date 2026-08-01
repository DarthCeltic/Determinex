# locked/_superseded/ — quarantined duplicate archives

These are **redundant duplicate eval archives** for ProgramBench tasks that are
already represented by a kept, referenced canonical archive in `locked/`. They were
moved here on **2026-06-21** during the corpus reconciliation (the brotli incident).

**Nothing here is deleted.** Each dir is a real eval archive retained so we can still
inspect how a tool handled a given test set, or restore it if a better canonical is
ever questioned. They are simply not the active/canonical archive for their task.

## Why a dir landed here

A dir was quarantined only when **all** of these held (maximally conservative):

1. It is **not referenced** by any `eval_index.json` row's `eval_report_path`.
2. It is **not a key** in `verified_locks.json` (the sha-pinned provenance registry).
3. Its name appears in **no** corpus registry (`capability_map.json`,
   `provenance_proofs.json`, `provenance_justifications.json`, `proven_ceilings.json`,
   `ceiling_register.json`).
4. Its canonical task already has a kept archive in `locked/` (same short name).

So every task represented here is still fully covered by a live archive — these are
pure dead duplicates (short-name vs `owner__repo.hash` vs `_native`/`_model` variants).

## The law that made this necessary

`scripts/pb_tier_classify.py` now enforces the **archive-authoritative + provenance**
reconcile law on every run, and `--guard` fails CI if `eval_index.json` ever disagrees
with the locked archives / `verified_locks.json` again. That is what prevents another
"brotli was locked but shown as unsolved for days" drift. See the script header.

`MOVED.txt` lists the exact dirs moved in this pass.
