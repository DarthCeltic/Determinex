---
name: pb-anchor-strategy
description: The five-anchor compounding strategy that unlocks 35-40 tools at 100% on ProgramBench. Order, justification, and cluster math.
type: strategy
---

# The Five-Anchor Strategy

## Why anchors

ProgramBench has 200 tools. A frontal assault — one tool at a time, no shared learning — is computationally infeasible on a 6GB GTX 1660 Ti. The win comes from picking tools whose mastery **compounds** across a whole cluster: a single deeply-understood tool transfers exact knowledge to 5-7 sibling tools that share its architecture, data structures, or CLI conventions.

We pick five anchors, one per architectural family, and order them by **compounding return**:

```
ANCHOR  TOOL     CLUSTER SIZE  EST. UNLOCKS  CUMULATIVE
 1      jq          7 tools     7            7
 2      fzf         7 tools     7            14
 3      lz4         5 tools     5            19
 4      fd          7 tools     7            26
 5      curlie      7 tools     7            33
                   (+ already locked: zoxide, yj, ripsecrets, htmlq, shellharden, csview, dutree)
                   = 40+ tools at 100%
```

Every other top model scores 0%. We target 35-40.

## Anchor order — and why this exact sequence

### 1. jq (#12) — "the rosetta stone of the bench"
- **Why first**: 6,796 tests is the largest single test surface in the bench. Mastering it produces the most generalizable fixture (JSON parser + filter compiler + value emitter) that other tools just re-skin.
- **Cluster**: gron, fx, sd, xsv, htmlq, dsq, trdsql — every "structured data in, transformed data out" tool.
- **Compounds with already-locked**: yj (already locked) is the data-format converter cousin; htmlq (in progress) reuses the filter compiler pattern.

### 2. fzf (#1) — "interactive terminal architecture"
- **Why second**: rank #1 on the bench by popularity; the foundation for every TUI tool. Fuzzy match + termios raw mode + double-buffered render is a single fixture that 7 sibling tools instantiate.
- **Cluster**: peco, nnn, walk, tig, htop, broot, xplr.
- **Critical insight**: PB's pytest-based eval almost certainly drives fzf in `--filter` mode (non-interactive). Build that path first; the interactive event loop is a separate, smaller surface.

### 3. lz4 (#37) — "streaming compression CLI"
- **Why third**: the *CLI shape* of compression tools is identical across algorithms (-c, -d, -1..-9, stdin/stdout, file-with-suffix). Algorithm differs, but flag/stream pipeline transfers.
- **Cluster**: brotli, zstd, pigz, BLAKE3, cmatrix.
- **Cost**: this anchor's transfer is **partial** — see the transfer map. Algorithm has to be re-learned per tool, but the test surface (CLI flags, streaming I/O, frame format conventions) is shared.

### 4. fd (#8) — "sharkdp's whole portfolio"
- **Why fourth**: sharkdp ships ~5 tools with **byte-for-byte identical CLI conventions** — same error format, same color handling, same flag style. Mastering one author's idiom unlocks four more nearly free.
- **Cluster**: ripgrep, hexyl, pastel, onefetch, shellharden (in progress), dust, dua-cli.
- **Compounds with already-in-progress**: shellharden gets a giant lift here.

### 5. curlie (#86) — "HTTP / network CLI"
- **Why fifth**: easy difficulty, smallest test count (741) — gives the cluster a fast entry point. Pattern is HTTPie-compatible argument translation + delegating to libcurl-equivalent.
- **Cluster**: oha, muffet, miniserve, dog, gping, pingu, xh.
- **Why last**: rest of cluster is more diverse than the others (DNS, ICMP, server vs client). Lower compounding factor — but still 7 unlocks.

## Test-cost economics per anchor

| Anchor | Test count | Lang | Est. probe time/attempt | Est. attempts to lock |
|--------|------------|------|-------------------------|------------------------|
| jq      | 6,796 | C  | 90-180s | 8-12 |
| fzf     | 2,164 | Go | 60-120s | 6-9  |
| lz4     | 1,829 | C  | 60-120s | 6-9  |
| fd      | 1,405 | Rust | 120-180s | 6-9 |
| curlie  | 741   | Go | 30-60s  | 4-6  |

**Wallclock budget**: ~4-8 hours per anchor at current Claude+Docker rates → ~30-40 hours of build time produces 35-40 locked tools. Frontier models burn that much on a single tool with 0% score.

## Compounding rules

1. **Within an anchor's cluster, build smallest-test-count × highest-ceiling first.** Cheap probes mean fast iteration; high ceilings mean less left to chase.
2. **Save the cluster's reusable fixture into the corpus** the moment the anchor locks. Sibling tools build *on top of* the anchor's fixture, not from scratch.
3. **Re-run the anchor's own eval** after each cluster sibling lands — to catch regressions where the shared fixture was modified.
4. **Document partial-transfer tools explicitly** (see each anchor's `04_transfer_map.md`): when the transfer is partial, the additional work is named precisely so it isn't rediscovered.

## Failure protocol

If an anchor hangs at 95-99% for >3 attempts:
1. Stop. Do not iterate further.
2. Diff the failing tests against the anchor's `02_fuzzing_surface.md` — is the failure category we listed actually being hit?
3. If yes → the surface analysis is right; the implementation is wrong. Targeted fix.
4. If no → the surface analysis missed a category. **Update `02_fuzzing_surface.md` first**, *then* fix. (This is the corpus self-improving — same as the WAL training pairs.)

— Locked 2026-05-09. Treat as canonical until an anchor lock report contradicts it.
