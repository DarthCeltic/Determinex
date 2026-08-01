---
name: anchor-curlie
description: Anchor 5 — curlie. HTTPie-syntax curl wrapper. Smallest test surface (741) and easy difficulty — the cluster's fast entry. Mostly argument translation + delegating to libcurl-equivalent.
type: anchor-pack
---

# Anchor 5 — curlie

| Field | Value |
|-------|-------|
| Repo | `rs/curlie` |
| Commit | `5dfcbb17ea673b66a3faab66d2ff5f24145f45a8` |
| Instance ID | `rs__curlie.5dfcbb1` |
| Reference language | Go |
| Recommended impl language | **Go** with `os/exec` to invoke `curl` — fastest path; **Python** is second-best |
| ProgramBench rank | #86 |
| Test count | **741** across 10 branches |
| Difficulty | **easy** (only easy in the anchor set) |

## Cluster (unlocks at 100% native)

| # | Tool | Tests | Ceiling | Transfer kind |
|---|------|-------|---------|---------------|
| #43 | oha       | 899   | 72.5% | partial (HTTP load tester; argument shape transfers; load-loop is new) |
| #94 | muffet    | 293   | 88.1% | partial (link checker; HTTP fetch + parse links) |
| #56 | miniserve | 304   | 78.6% | partial (tiny HTTP server; SERVER side; protocol semantics transfer) |
| #61 | dog       | 1,300 | 84.2% | partial (DNS-over-HTTPS; protocol layering transfers; DNS is novel) |
| #35 | gping     | 339   | 78.5% | minimal (ping plotter; CLI conventions only) |
| #101 | pingu    | 383   | 96.6% | minimal (similar to gping) |
| #55 | xh        | 1,171 | 50.0% | direct (HTTPie clone; near-identical to curlie) |

**Cluster total**: 7 tools, ~4,689 tests downstream.

## Why this anchor is the easiest entry

- 741 tests is the smallest of any anchor.
- "easy" difficulty rating reflects that curlie is fundamentally an *argument translator* — no novel algorithms, no novel data structures.
- The Go ecosystem and curl's command-line are well-documented; no domain mystery.
- A working solution can be a 200-line Go program that shells out to `curl`. Tests then verify the translation logic.

## Sections

1. [01_architecture.md](01_architecture.md)
2. [02_fuzzing_surface.md](02_fuzzing_surface.md)
3. [03_implementation_sequence.md](03_implementation_sequence.md)
4. [04_transfer_map.md](04_transfer_map.md)
5. [05_corpus_impact.md](05_corpus_impact.md)
6. **[06_behavioral_spec.md](06_behavioral_spec.md)** — empirical behavioral surface from 270 CATCHES + 74 goldens; inject into builder prompt
