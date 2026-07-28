# Trajectory Memo — Campaign 002 (written 2026-06-12, post-2/26 A3 partial) (historical — all counts in this memo invalidated 2026-06-30, see docs/papers/PROGRAMBENCH.md)

## Current State (historical)
- Strict locks: **50/200** (historical, invalidated)
- A3 in flight: 2/26 done (dust=factory_accepted, dua-cli=factory_accepted_tui_cap)
- B2v2 + D1 queued on Hetzner, chain fires post-A3

---

## Branch Assumptions

### Conservative inputs (tool yield rates)
- A3 cap removal (26 tools): empirical yield estimate = 25–35% of tools hit strict lock
  - Basis: cap was a performance choice, many tools had ~90%+ scores under old metric
  - Known suppressions: broot (TUI ceiling), atlas (large multi-branch compile)
  - (historical) Best case if cap removal uncovers passing tests: ~8–9 locks from 26 tools
  - (historical) Realistic case (some tools had real behavioral failures behind the cap): ~5–6 locks
- B2v2 emission (10 tools, bidir fix): svgbob already 948/948; 9 others unknown
  - svgbob = 1 certified lock (pending Hetzner confirm)
  - Other 9: bidir fix targets namespace mismatch not_run; if primary failure mode, yield 3–5 more
  - (historical) Conservative: 2 locks from 9 (excluding svgbob)
- D1 parity (6 tools: htmlq/csview/zip/pingu/quickjs/tuc): all near-locks already
  - These are SEPARATE PARITY LINE — not summed into strict count
  - Count effect: 0

### Realistic branch (to 58)
```
Base:           50
A3 cap yields:   6  (from 26 tools — 23% hit rate)
B2v2 yields:     3  (svgbob + 2 others)
Codex F march:   2  (Codex F1-F10 when credits return; errcheck rc=2, blake3 --check)
-----------
Realistic:      61  (conservative side of realistic)
```

**Realistic range: 58–62**

Gating factor: A3 cap removal results not yet known. If cap was masking behavioral failures (not just collection gaps), yield will be on the low end. Yield data from A3 will set the branch in 4 hours.

### Optimistic branch (to 65)
```
Base:           50
A3 cap yields:   9  (from 26 tools — 35% hit rate; high cap count = pass was plausible)
B2v2 yields:     5  (svgbob + 4 others with bidir as primary blocker)
Codex F march:   4  (3-4 easy locks if F1-F10 addressed)
Leftover factory: 2  (direnv gets to 1946/1946 with 4 more fixes; some partial_eval_100 converts)
-----------
Optimistic:     70
```

**Optimistic range: 65–70**

Requires: A3 cap tools had passing tests behind the cap (evidence: many scored 90%+ under old metric = 360+ tests passed, cap was 400 limit = 10% of tests cut). Codex credits return before campaign closes.

### Pessimistic branch
```
A3 yield:   2–3  (cap removal exposes behavioral failures previously masked)
B2v2:       1    (svgbob only)
Codex:      0    (credits don't return)
-----------
Floor:     53–54
```

**Floor: 53–55** if A3 yields are low and Codex is offline.

---

## Which branch fires?

**A3 results are the discriminator.** Reading them in ~4h will tell us:
- If ≥7 tools hit strict lock → optimistic branch live
- If 4–6 tools hit strict lock → realistic branch live  
- If ≤3 tools → pessimistic, need new work (partial_eval_100 cap removal queue)

## Next highest-leverage moves after A3

1. **A3 strict locks** — certify immediately, archive to locked/
2. **B2v2 svgbob** — certify when Hetzner lands (should be ~1h after A3)
3. **B2v2 other 9** — certify any strict locks from emission batch
4. **errcheck rc=2** (Codex C4) — 100 failures, all rc=2 fatal; if Codex returns: 964→1064 possible
5. **partial_eval_100 queue** — 60 tools need cap removal + repack + Hetzner eval; ~15% yield = 9 more locks
6. **D1 parity publish** — htmlq/csview/pingu/quickjs at near-100%; publish parity line once confirmed

## Parity line (separate, not counted)
- htmlq: 2057/2058 (1 upstream skip)
- ripgrep: 2536/2538 (2 upstream skips)
- xq: 876/879 (3 upstream skips)
- csview: 347/348 (1 upstream skip)
- quickjs: 3038/3044 (6 upstream skips)
- chroma: 524/531 (7 upstream skips)
- cheat: 612/614 (2 upstream root-env skips)
- pingu: 416/419 (3 upstream "Too slow" skips — ceiling confirmed)

These are near-100% but not strict locks. Published as "≥N tools at 99%+ with only upstream skips."

---

*Written: 2026-06-12 | Source: eval_index.json, a3_run.log (2/26 partial), campaign_assignments.json*
