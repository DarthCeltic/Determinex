---
name: anchor-fd
description: Anchor 4 — fd. sharkdp's flagship Rust file-finder. Mastering one author's portfolio idiom unlocks 4-7 sibling tools that share his exact CLI conventions, error format, and color scheme.
type: anchor-pack
---

# Anchor 4 — fd

| Field | Value |
|-------|-------|
| Repo | `sharkdp/fd` |
| Commit | `40d8eb30bcade65942308262a1f41a1b7847a1fe` |
| Instance ID | `sharkdp__fd.40d8eb3` |
| Reference language | Rust |
| Recommended impl language | **Rust** (matches reference; `clap` + `ignore` + `regex` are mandatory; reproducing in Python loses the gitignore-walk speed and color-scheme defaults) |
| ProgramBench rank | #8 |
| Test count | **1,405** across 10 branches |
| Difficulty | medium |

## Cluster (unlocks at 100% native)

| # | Tool | Tests | Ceiling | Transfer kind |
|---|------|-------|---------|---------------|
| #3  | ripgrep    | 1,994 | 79.7% | direct (BurntSushi+sharkdp ecosystem; same `ignore` crate; same regex; pivot from path-match to content-match) |
| #45 | hexyl      | 906   | 82.8% | partial (sharkdp; same CLI conventions, different domain — hex dump) |
| #64 | pastel     | 1,114 | 77.2% | partial (sharkdp; color tool; CLI conventions transfer) |
| #38 | onefetch   | 1,166 | 81.7% | partial (Git-aware repo info; CLI conventions transfer) |
| #78 | shellharden | 1,095 | 81.7% | partial (shell linter; conventions transfer) — *in progress* |
| #39 | dust       | 584   | 70.9% | partial (du-clone; tree walker shared with fd; aggregation new) |
| #68 | dua-cli    | 709   | 86.9% | partial (interactive du; tree walker shared) |

**Cluster total**: 7 tools, ~7,568 tests downstream.

## Why this anchor compounds

sharkdp ships consistent CLI conventions across his portfolio:
- **Identical color scheme** (`--color always|auto|never`)
- **Identical error format** (`[fd error]: ` prefix)
- **Identical exit codes** (0/1/2 standard meanings)
- **Identical `--help` style** (clap-derived)
- **Identical concurrency idioms** (rayon-based parallel iterators)
- **Identical I/O guards** (atty detection for `--color auto`)

Mastering one means mastering five (fd, hexyl, pastel, hyperfine, bat). PB tests favor consistency; getting the conventions right once pays out across the cluster.

## Sections

1. [01_architecture.md](01_architecture.md)
2. [02_fuzzing_surface.md](02_fuzzing_surface.md)
3. [03_implementation_sequence.md](03_implementation_sequence.md)
4. [04_transfer_map.md](04_transfer_map.md)
5. [05_corpus_impact.md](05_corpus_impact.md)
6. **[06_behavioral_spec.md](06_behavioral_spec.md)** — empirical behavioral surface from 519 CATCHES + 177 goldens; inject into builder prompt
