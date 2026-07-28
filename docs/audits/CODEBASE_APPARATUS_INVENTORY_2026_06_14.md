# Codebase Apparatus Inventory & Safe-Cleanup Map (2026-06-14)

> Purpose: map the campaign "apparatus" (status/proof self-auditing scaffolding)
> vs. the real engine, **prove what is severable**, and stage a reversible
> cleanup. **Nothing is moved by this document.** Archive happens only after you
> confirm the map.

## 1. The whole-system shape (why this exists)

162,422 tracked files, but **138,396 are `corpus/`** (ProgramBench tool sources,
SWE-bench repos, training data) — not engine. Of the engine code in `scripts/`,
roughly two-thirds by line count is **self-auditing campaign apparatus** produced
by autonomous multi-lane / overnight-wave sprints (1,667 commits in 3 months).

## 2. The Apparatus Island (cleanup target)

| Path | Files | Lines | What it is |
|------|------:|------:|------------|
| `scripts/status/` | 1,461 | 127,592 | 966 pure-shim "lane" scripts (≤20 lines, call a shared `*_common.main("LANE")`) + ~495 slightly-longer review scripts |
| `scripts/proof/` | 149 | 93,666 | ~30 `wave_NNN_claude_common.py` / `gulp_wave_*` / `*_common.py` sprint brains (1,000–1,832 lines each) + dated one-offs |
| `tests/status/` | 1,175 | 99,695 | auto-generated guard tests (`*_anti_god_script_rule_passes`) for the above |
| `tests/proof/` | 10 | 516 | proof-campaign tests |
| `scripts/claim_scanner/` | 1 | — | day-one public claim scanner (apparatus) |
| **TOTAL** | **~2,796** | **~321,469** | self-contained governance/proof scaffolding |

**Duplication note:** `wave_012` vs `wave_013` common differ ~65% — these are
divergent point-in-time sprint forks, not clean duplicates. They are **historical
snapshots** (archive candidates), not merge-able duplicates (so "consolidate" the
wave-commons mostly means "keep the latest + archive the rest").

## 3. Severability proof (verified 2026-06-14)

The apparatus does **not** support the engine. Verified:

- **Core engine does not import it.** No file under `scripts/{hive,repair,models,
  ide,determinex_cloak,verified_task,validators,agents,providers}` imports the
  `status` or `proof` packages.
- **The IDE backend coupling was a FALSE POSITIVE.** `scripts/ide/
  backend_command_surface.py` imports `scripts/ide/proof_operator_center_*`
  siblings and uses a local `status` variable — **not** the apparatus packages.
- **CI does not run the apparatus scripts.** `.github/workflows/test.yml` runs:
  `pre-commit run --all-files`, `scripts/fix_mojibake.py --scan`,
  `scripts/pb_doc_count_check.py`, `pytest tests/`, `scripts/determinex_limits_test.py`.
  None invoke `scripts/status` or `scripts/proof` directly.
- **Coverage gate is `--cov-fail-under=2`** (2%). Archiving `tests/status` cannot
  breach it.
- **Only two cross-references exist**, both inside/adjacent to the apparatus:
  `scripts/claim_scanner/day_one_public_claim_scanner.py` (apparatus→apparatus)
  and `tests/ide_frontend/test_proof_center_installed_app_route_mount_001.py`
  (one IDE-frontend test that imports `proof`).

**Conclusion: the apparatus is a self-contained island.** Archiving it cannot
break the engine, the real IDE backend, or the CI guards.

## 4. KEEP — real guards that live OUTSIDE the apparatus (do not touch)

These are in `scripts/` root, used by CI/pre-commit, and are genuine:
`pb_doc_count_check.py`, `pb_override_scan.py`, `pb_board_guard.py`,
`fix_mojibake.py`, `determinex_limits_test.py`. They are **not** part of the island.

## 5. The real engine (untouched by any cleanup)

`scripts/hive` (11k), `scripts/determinex_cloak` (1.4k), `rosetta/`, `scripts/
validators`, `scripts/repair`, `scripts/models`, `scripts/verified_task`,
`scripts/ide` (22k), the swebench/programbench agents (~5.7k), and the new
Adjudicator + Correctness Amplifier stack. Core (non-status) tests: **1,043 pass
/ 4 fail** — engine is 99.6% green.

## 6. Staged, reversible plan (execute only on your go)

**Stage A — Map (this doc).** Done. No moves.

**Stage B — Consolidate the live governance (keep what you'll add to).**
Decide which ONE wave-common + the `proof_record` writer + the `_shared_*`
primitives represent the *current* governance you want to keep extending. Collapse
the 966 lane shims into a single parameterized runner that imports it. Net: keep
~2–4k lines of live tooling, mark the other ~30 wave forks + 966 shims as historical.

**Stage C — Archive (reversible).** `git mv` the historical apparatus into
`archive/apparatus_2026_06/` (preserves full git history; nothing deleted). Move
`tests/status/` + `tests/proof/` with it so CI stays green. Rewire the 1
IDE-frontend test reference.

**Stage D — Verify nothing broke.** Run:
`pytest tests/ -q` · `python scripts/pb_doc_count_check.py` ·
`python scripts/determinex_limits_test.py` · `pre-commit run --all-files` ·
`python -m pytest tests/test_autofix_pipeline.py -q`. All must pass.

**Stage E — Bury/delete** only what Stage D proves unneeded, on your explicit go.

## 7. Expected outcome

Repo `scripts/` drops from ~340k → ~110k lines; test count from 17k → ~3k; the
real engine becomes legible. Zero capability lost (history preserved, guards kept,
engine untouched). Reversible at every stage until you say delete.
