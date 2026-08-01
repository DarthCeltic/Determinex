---
name: anchor-lz4
description: Anchor 3 — lz4. Streaming LZ77 block + frame format. The rosetta stone for compression CLI conventions. Algorithm transfer is partial — the CLI shape is the universal piece.
type: anchor-pack
---

# Anchor 3 — lz4

| Field | Value |
|-------|-------|
| Repo | `lz4/lz4` |
| Commit | `1519f46a3a11f312be8f5796e8fa4779140277f0` |
| Instance ID | `lz4__lz4.1519f46` |
| Reference language | C |
| Recommended impl language | **Python** with `lz4` pip module — fastest path to lock; **C** if pip is blocked (PB containers DO allow pip) |
| ProgramBench rank | #37 |
| Test count | **1,829** across 12 branches |
| Difficulty | medium |

## Cluster (unlocks at 100% native)

| # | Tool | Tests | Ceiling | Transfer kind |
|---|------|-------|---------|---------------|
| #27 | brotli  | 441   | 90.7% | partial (CLI shape direct; algorithm differs) |
| #16 | zstd    | 2,038 | 68.8% | partial (CLI shape direct; algorithm differs; biggest test count) |
| #92 | pigz    | 831   | 83.2% | partial (gzip parallel; same CLI conventions) |
| #65 | BLAKE3  | 647   | 97.5% | partial (hash, not compress; only the stream-CLI pattern transfers) |
| #75 | cmatrix | 508   | 97.0% | minimal (terminal display; only stream-input pattern transfers) |

**Cluster total**: 5 tools, ~4,465 tests downstream.

> **Cluster cost**: this is the lowest-compounding anchor. The transferable piece is the **CLI shape and stream-I/O scaffold**, not the compression algorithm. Algorithm has to be re-learned per tool. We pick lz4 because (a) it's the simplest of the five algorithms, (b) the frame format is the most explicitly documented spec, and (c) Python's `lz4` pip module gives a free reference encoder/decoder for the round-trip-against-real-binary tests likely in PB.

## Sections

1. [01_architecture.md](01_architecture.md)
2. [02_fuzzing_surface.md](02_fuzzing_surface.md)
3. [03_implementation_sequence.md](03_implementation_sequence.md)
4. [04_transfer_map.md](04_transfer_map.md)
5. [05_corpus_impact.md](05_corpus_impact.md)
6. **[06_behavioral_spec.md](06_behavioral_spec.md)** — empirical behavioral surface from 621 CATCHES + 80 goldens; inject into builder prompt
