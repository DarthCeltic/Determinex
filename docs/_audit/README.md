# Determinex docs audit — 2026-05-29

Read-only audit artifacts. **No deletions, no moves, no consolidation has happened.**

## Artifacts

- [`reference_map_20260529.csv`](reference_map_20260529.csv) — every doc in `docs/` (260 rows) with bucket classification, reference counts across `locks/sentinel/*.json` / `scripts/` / `tests/` / root `README.md`+`CLAUDE.md`+`AGENTS.md`+`CHANGELOG.md` / `docs/README.md`, and recommended disposition.
- **Baseline tarball** (off-repo): `T:/ColdStorage/determinex-docs/bundles/determinex-docs-20260529-phase0-baseline.tar.gz` — 416 KB, sha256 `4a351003b09c4d1a1159ffe63265e528a8139c34e66eb5d1d129045ec23efb4a`, 261 entries. Captures the entire `docs/` directory before any cleanup. Restore individual file: `tar -xzf <bundle> docs/<NAME>.md`.

## Disposition summary

| Disposition | Count | Meaning |
|---|---:|---|
| `KEEP` | 37 | Foundation / Policy / Companion — keep at top level regardless of refs |
| `COLD_STORAGE_SAFE` | 186 | Zero references found from locks/scripts/tests/index — safe to move with no reference updates |
| `REVIEW` | 33 | Referenced (mostly 1–5 refs) — moving requires reference updates first |
| `CONSOLIDATE` | 4 | `*_FINAL_STATE` docs that should fold into a single rollup |

Of the 186 `COLD_STORAGE_SAFE`, 17 are foundation/policy/companion/recent-audit docs that should be **overridden to KEEP** despite zero references (humans use them via the index). Net safe-to-move: **~169**.

## Bucket breakdown

| Bucket | Count | Notes |
|---|---:|---|
| PER_PROGRAMBENCH_ADMIN | 46 | Most are per-run admin records; consolidate to ~5 canonical |
| PER_TRACE_FLOW | 37 | IDE/Frontend/Live/Real verification traces; consolidate to ~4 |
| MISC | 28 | Mixed; needs eyeballing |
| FOUNDATION | 20 | KEEP |
| PER_FINAL_STATE | 18 | Consolidate into a single rollup |
| PER_REACT | 16 | Five rooms × panel/binding; consolidate to 1 |
| POLICY | 13 | KEEP |
| PER_FRONTEND | 11 | Mostly trace docs; consolidate |
| PER_SOURCE_MUTATION | 9 | Approval/patch/rollback flows; consolidate |
| PER_PROOF_STATUS | 8 | Mixed; review |
| PER_CLAUDE_LANE | 8 | Claude-lane state docs |
| PER_MODEL_ADMISSION | 8 | Local/Live/Ollama routing |
| PER_EVIDENCE_GUARD | 7 | Ledger/drift/cross-lane |
| PER_AUDIT_DATED | 6 | Keep recent (2026-05), archive older |
| PER_ROOM_WORKFLOW | 4 | Idea Lab + Repo Clinic + Maintenance Bay + Learning Studio |
| PER_TAURI | 4 | Tauri bridge docs |
| PER_HANDOFF | 4 | Session handoffs — cold storage |
| COMPANION | 4 | KEEP (skill-load files) |
| PER_RECONCILE | 3 | Snapshots — cold storage |
| PER_UNIFIED_PRODUCT | 3 | Mixed |
| PER_BOARD_SNAPSHOT | 3 | Keep latest 1–2 |

## How to read the CSV

Columns:
- `doc`, `name`, `size_bytes`, `bucket`
- `ref_total` = sum of all references
- `ref_locks` / `ref_locks_count` — lock JSON files that cite this doc
- `ref_scripts` / `ref_scripts_count` — Python scripts that cite this doc
- `ref_tests` / `ref_tests_count` — test files that hardcode this doc path
- `ref_top` / `ref_top_count` — citations from root README/CLAUDE/AGENTS/CHANGELOG and `docs/README.md`
- `disposition` — recommended action

## Helper script

[`c:/tmp/build_doc_reference_csv.py`](c:/tmp/build_doc_reference_csv.py) — re-runnable; regenerates the CSV from current state. Not in repo (ephemeral).
