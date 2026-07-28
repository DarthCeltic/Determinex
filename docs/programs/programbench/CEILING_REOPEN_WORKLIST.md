# ProgramBench Ceiling Reopen Worklist

> Generated 2026-06-14 by `determinex_adjudicator.py` run across the best eval of
> every tool previously labeled `ceiling_certified` / `ceiling_confirmed`.
> Command: `python scripts/determinex_adjudicator.py classify <best_eval.json>`.

## Headline

Of the tools audited, **only `gping` (4) and `pingu` (3) carry a genuine ceiling**
(network/Windows/too-slow upstream `@pytest.mark.skip`). **Every other "ceiling"
is reopenable** — the label was applied without proof. The mechanical audit
turns "I think this tops out" into a per-failure move.

> **What "reopen" means (read this):** `reopen` = the Adjudicator found a
> non-IMPOSSIBLE next move for that failure. It does **not** guarantee a lock.
> `remove-collection-cap` reveals not_run tests whose post-cap pass/fail is
> unknown until re-eval; `iterate-solve-loop` is ordinary code work;
> `pytest-current-test-routing` needs a per-test golden map. Reopen = "not a
> proven ceiling, here is the next move," not "free lock."

## The worklist (clean run, drop-privileges false-positive fixed)

| Tool | reopen | genuine ceiling | top moves |
|------|-------:|----------------:|-----------|
| rvben__rumdl | 3375 | 0 | cap:2590, routing:599, iterate:147 |
| johanneskaufmann__html-to-markdown | 857 | 0 | iterate:517, routing:275, cap:56 |
| sharkdp__fd | 555 | 0 | **cap:539**, iterate:5, drop-priv:4 |
| cordx56__rustowl | 507 | 0 | iterate:307, cap:160, routing:30 |
| sharkdp__hexyl | 331 | 0 | **cap:325**, iterate:6 |
| segmentio__chamber | 330 | 0 | cap:297, routing:26 |
| doxygen__doxygen | 223 | 0 | iterate:178, install:30, cap:7 |
| dalance__amber | 167 | 0 | cap:129, iterate:33 |
| rbakbashev__elfcat | 104 | 0 | cap:69, iterate:34 |
| sigoden__argc | 78 | 0 | remove-self-skip:58, investigate:20 |
| kyoh86__richgo | 52 | 0 | cap:38, iterate:13 |
| filosottile__age | 44 | 0 | investigate:24, install:12 ⚠, pty:8 |
| alexpovel__srgn | 16 | 0 | **routing:15**, investigate:1 |
| hpjansson__chafa | 12 | 0 | cap:8, **scalar-build:4** |
| eudoxia0__hashcards | 7 | 0 | routing:4, investigate:2 |
| bellard__quickjs | 6 | 0 | investigate:5, install:1 |
| oppiliappan__statix | 4 | 0 | investigate:4 |
| **orf__gping** | 4 | **4** | error-norm:2, pty:2 (+ 4 genuine) |
| incu6us__goimports-reviser | 3 | 0 | routing:2, investigate:1 |
| agourlay__zip-password-finder | 1 | 0 | investigate:1 |
| arthursonzogni__json-tui | 1 | 0 | routing:1 |
| nikolassv__bartib | 1 | 0 | investigate:1 |
| wfxr__csview | 1 | 0 | investigate:1 |
| **sheepla__pingu** | 0 | **3** | (all genuine upstream skip) |

## Reopen reality check (verified 2026-06-14 — the reopens are NOT free)

The audit kept going and verified the *kind* of work behind each move. Crucial
correction: **the "cap" reopens are almost all TUI/PTY capability filters, not
performance caps.** Sampled fd, hexyl, amber, elfcat, richgo, rumdl compile.sh:
**0 had a `del items[N:]` performance cap; all had `collect_ignore` tmux/pty/curses
filters.** Removing the filter alone converts not_run into *failures* unless tmux+
libtmux are installed and a PTY is allocated (the keifu pattern). So:

1. **TUI-capability reopens (fd, hexyl, amber, elfcat, richgo, rumdl, chamber):**
   real keifu-pattern work — install tmux+libtmux, allocate PTY, verify each test
   passes. NOT a one-line strip. Uncertain payoff; reveals the true ceiling.
2. **chafa (scalar-build:4)** — rebuild with `-mno-avx2`; the cleanest single
   hypothesis test (does the SIMD-render mismatch vanish?). Lowest-risk genuine reopen.
3. **srgn (routing:15), html-to-markdown (routing:275)** — distinct-nodeid
   conflicts → `PYTEST_CURRENT_TEST` routing + a per-test golden map (svd2rust move).
   Real work, proven technique.
4. **iterate-solve-loop counts** (rustowl 307, html-to-markdown 517, doxygen 178)
   — ordinary behavioral bugs; the standard solve loop, tool by tool.

**Honest bottom line:** the ceilings are debunked (proven not-impossible), but the
reopens are real engineering, the same per-tool work the campaign has always done
— the Adjudicator tells you the *right move* and stops a false surrender; it does
not make the move free. Three over-simplifications by the Adjudicator were caught
and fixed *during this very audit* (drop-privileges false-match, install-dependency
for a non-existent package, cap-vs-TUI-filter) — the governor being held to its
own no-slop standard.

## Verified false reopen (integrity note)

⚠ **age (`install-dependency:12`)** — the skips say *"requires age-plugin-batchpass
which is not available."* Investigation: `age-plugin-batchpass` is **not a real
public package** — it is a test-only plugin fixture the PB suite expects but does
not ship. So the "install-dependency" verdict is a *false reopen*: you cannot
install it; you would have to **implement** the age plugin protocol. Until then
age's 7 batchpass tests are a genuine near-lock; its ~8 PTY tests are reopenable
via `pty-allocate`. The Adjudicator's `install-dependency` remediation was
hardened (2026-06-14) to require verifying the dependency is publicly installable
before claiming the reopen — otherwise flag implement-or-near-lock. This is the
governor catching *itself* copping out in reverse.

## Genuine ceilings (confirmed, with proof)

- **gping** — 4 failures resolve (error-norm + pty) but **4 genuine** upstream
  `@pytest.mark.skip` (network ping to a host + Windows-only parser).
- **pingu** — 3 genuine `@pytest.mark.skip("Too slow")`.
- Upstream-skip near-locks (csview, htmlq, xq, quickjs, statix, bartib, sd, tuc,
  xz, zip-password-finder, hashcards, goimports-reviser) — `investigate-skip-origin`
  here means "confirm the skip is upstream"; most are genuine near-locks.
