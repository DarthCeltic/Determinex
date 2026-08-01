# Morning review — overnight drive (2026-06-23)

## Integrity decision needed (affects headline count)
**9 verified_locks entries are UNVERIFIABLE** (empty sha, no local archive). Annotated
with `archive_status` in verified_locks.json. Hetzner factories checked — most DRIFTED/broke:
- `hooklift__gowsdl` factory 36/595 (build-broken) — was locked 846/846
- `eliukblau__pixterm` factory 6/530 (build-broken) — was locked 922/922
- `madler__pigz` factory 1614/1660 (near) — was locked 1876/1876
- `parqeye` 178/834 ; `crowdagger__crowbook` = dup of sha-pinned `crowbook`
- tier_2: `quickjs`/`jp2a`/`cheat`/`caesium-clt` (upstream-skip near-locks, archive lost)

These were verified at lock time but the artifact was never sha-pinned and the factory
has since rotted. Per the registry's own rule (empty sha = UNVERIFIED) they should NOT
count toward the verified total until re-established.
**DECISION:** demote to unverified (headline 65 -> ~60-61) and let autodrive re-build+
re-archive them (gowsdl/pixterm are build-fixable — autodrive's build.err loop locked
them before), OR re-eval+pin first then keep. Recommend: re-establish (they're recoverable).

## Near-lock reality (the drive)
Front near-locks need deep per-tool/model work, NOT simple autofix:
- bartib: 12 datetime fails, ALREADY has faketime — subtle date-anchor issue (per-tool).
- nsh: TUI cursor/history interaction tests.
- elfcat: semantic. jplot: TUI ("2157/2157 clean" is without-ignored, raw has TUI fails).
autodrive auto-closes only version/clock/locale/output residuals; the rest need
DETERMINEX_AMPLIFY (model) or manual MATCH. Realistic overnight lock yield is low.

## Confirmed safe
TUI-unlock deploy (138 tools) did NOT regress bartib (0 tmux fails, 12 pre-existing
datetime). At the official metric un-filter is neutral-or-gain.
