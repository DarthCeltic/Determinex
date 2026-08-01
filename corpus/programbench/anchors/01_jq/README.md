---
name: anchor-jq
description: Anchor 1 — jq. Filter compiler + JSON value model + stream evaluator. Largest test surface in ProgramBench (6,796 tests). The rosetta stone for every structured-data tool on the bench.
type: anchor-pack
---

# Anchor 1 — jq

| Field | Value |
|-------|-------|
| Repo | `jqlang/jq` |
| Commit | `b33a7634ba34ffa7ce7368cc0ebf5ca40b54c7e6` |
| Instance ID | `jqlang__jq.b33a763` |
| Reference language | C |
| Recommended impl language | **Python** (fastest path to lock) — Go acceptable |
| ProgramBench rank | #12 |
| Test count | **6,796** across 12 branches |
| Difficulty | medium |

## Cluster (unlocks at 100% native)

| # | Tool | Tests | Ceiling | Transfer kind |
|---|------|-------|---------|---------------|
| #28  | gron      | 224   | 90.2% | direct (JSON walker → flat assignments) |
| #23  | fx        | 2,047 | 75.7% | direct (filter language over JSON) |
| #60  | sd        | 810   | 90.9% | partial (sed-style stream edit; reuses regex/replace) |
| #41  | xsv       | 1,182 | 82.7% | direct (CSV instead of JSON; same stream-row pipeline) |
| #57  | htmlq     | 1,455 | 93.9% | direct (CSS selector instead of jq filter; same emit model) — *in progress* |
| #84  | dsq       | 542   | 80.3% | direct (SQL over JSON/CSV — reuses the JSON parser) |
| #100 | trdsql    | 1,312 | 66.8% | direct (same as dsq) |

**Cluster total**: 7 tools, ~7,572 tests downstream.

## Sections

1. [01_architecture.md](01_architecture.md) — data structures, algorithms, modules, build script
2. [02_fuzzing_surface.md](02_fuzzing_surface.md) — flag combos and edge cases the harness will probe
3. [03_implementation_sequence.md](03_implementation_sequence.md) — what to build first, what's last, where 90→100% lives
4. [04_transfer_map.md](04_transfer_map.md) — exact knowledge that transfers per cluster tool
5. [05_corpus_impact.md](05_corpus_impact.md) — what completing this teaches the Oracle
