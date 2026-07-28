# DUAL AGENT CAMPAIGN BOARD
<!-- AUTO-RENDERED from eval_index.json + campaign_assignments.json + parked.json -->
<!-- DO NOT HAND-EDIT. Update source JSONs, re-render with: python scripts/render_campaign_board.py -->
<!-- Last render: 2026-06-11 by claude (v4 cycle: reconcile clean, CODEX-001/OVERRIDE-001 reconciled with bounce routing, CODEX-002 Hetzner running) -->

## Summary (2026-06-11)

| Metric | Value | Label |
|--------|-------|-------|
| **Strict locks** | **47 / 200** | passed==total, 0 not_run, 0 skipped, 0 failed |
| **Parity candidates** | **11** (unpublished) | upstream_skips only; Tier A/B classification pending |
| **Published parity** | **0** | No parity candidate has archived reference-diff artifact yet |
| Ceiling confirmed | 18 | Structural blockers; reference-diff evidence required per new protocol |
| Factory accepted | 10 | Board improvements; not at lock criteria |
| Pending unlock | 1 | argc (Hetzner eval running — CODEX-002) |
| Parked | 2 | igrep (harness-gap), jplot (best-only:park) |
| Board cache only | 113 | No eval artifacts |

> **NON-PUBLISHABLE (internal only):** Aggregate runnable-test % across all tools is a subset metric.
> Published numbers are TOOL COUNTS only: 47 strict · parity TBD.

> **RECONCILE NOTE 2026-06-10**: bartib demoted strict_lock→factory_accepted. Section 5 check:
> eval_report.json shows 886/929 (41 failures). Canonical count corrected 48→47.

> **RECONCILE NOTE 2026-06-11 (v4 cycle)**: Hardened reconcile: 47/47 strict_lock eval_reports clean (0 phantoms).
> CODEX-001 + CODEX-OVERRIDE-001 all reconciled — 7 tools bounced total with routed bounce records.
> Bounce classes: behavioral (fzf branch 3cde1a7d975e bidir, bartib date-substitution);
> harness-class (fasttext prefix inversion, age /workspace/executable systematic);
> mixed (bat 138+212, ast-grep 376+536); collection (ov JUnit XML gaps).
> Cross-tool Pattern 001 confirmed: age/bat/ast-grep/monolith all share /workspace/executable error.
> DRIVER_HOLD on Pattern 001 group pending compile.sh investigation.
> CODEX-002 Hetzner re-dispatched (PID 2913622). Corpus flywheel: 7 verdict rows + cross_tool_patterns.md.
> Cloak rerun: queued for next Hetzner overnight window after CODEX-002 completes.

---

## Strict Locks — 47/200 (23.5%)

`jq` (6874) · `yq` (2046) · `shellharden` (1292) · `angle-grinder` (1143) · `pastel` (1256) · `ripsecrets` (937) · `zoxide` (577) · `cmatrix` (769) · `hyperfine` (298) · `go-mod-outdated` (342) · `gron` (233) · `ascii-image-converter` (488) · `scc` (476) · `ditaa` (681) · `genact` (237) · `grex` (3036) · `bore` (900) · `clog-cli` (1556) · `code-minimap` (738) · `curlie` (1482) · `deadnix` (1418) · `diffr` (1524) · `dupl` (900) · `eva` (963) · `fblog` (2254) · `git-trim` (1422) · `hex` (1754) · `i3-style` (1500) · `loop` (1556) · `miniserve` (880) · `muffet` (864) · `nomino` (676) · `rnr` (1480) · `seqtk` (880) · `tex-fmt` (990) · `tparse` (1112) · `yj` (1457) · `entr` (1482) · `hck` (1768) · `ngrrram` (664) · `pier` (1556) · `rhit` (2176) · `tailspin` (1570) · `trdsql` (2806) · `xsv` (2634) · `flamelens` (510) · `thokr` (507)

---

## Parity Candidates — 11 tools (parity-pending-reference-diff)

> Published parity = 0 until each has an archived reference-diff artifact (same container, same tests).
> NON-PUBLISHABLE until verified.

| Tool | Score | Gap |
|------|-------|-----|
| htmlq | 2057/2058 | 1 upstream skip |
| ripgrep | 2536/2538 | 2 upstream skips |
| xq | 876/879 | 3 upstream skips |
| csview | 347/348 | 1 upstream skip |
| quickjs | 3038/3044 | 6 upstream skips |
| chroma | 524/531 | 7 upstream skips |
| sd | 1728/1738 | 10 upstream skips |
| dsq | 1660/1666 | 6 upstream skips |
| tuc | 2490/2498 | 8 upstream skips |
| elfcat | 1288/1291 | 3 upstream skips |
| zip-password-finder | 1582/1584 | 2 upstream skips |

---

## Ceiling Confirmed — 18 tools

> New protocol (2026-06-10): ceiling requires archived reference-diff artifact.
> Tools below are ceiling_confirmed per eval_index; most pre-date the reference-diff requirement.
> **Needs reference-diff verification:** all except amber, hexyl, fd, html-to-markdown, doxygen (5 documented with structural-blocker analysis).

| Tool | Score | Status |
|------|-------|--------|
| amber | 701/868 | structural blocker (conflicting rc assertions) |
| doxygen | 250/261 | structural blocker (duplicate test IDs) |
| html-to-markdown | 971/1307 | structural blocker (conflicting --version strings) |
| hexyl | 291/1270 | structural blocker (--panels=1 / zero-pad regex) |
| fd | 418/1822 | structural blocker (root perms / deleted cwd / regex) |
| gping | 628/735 | ceiling 649/655 (ENXIO irreconcilable + upstream skips) |
| richgo | 1572/1610 | @go_test phantom IDs |
| igrep | 1204/1253 | harness-gap (also PARKED) |
| oha | 2116/2156 | needs reference-diff |
| rumdl | 1311/4542 | needs reference-diff |
| nsh | 4574/4578 | needs reference-diff |
| json-tui | 1786/1788 | needs reference-diff |
| xz | 4060/4072 | needs reference-diff (4 TTY failures) |
| keifu | 548/625 | 8 upstream skips (max 617/625) |
| parqeye | 760/920 | 2 upstream skips (max 918/920) |
| eureka | 794/800 | needs reference-diff |
| rustowl | 1442/1524 | needs reference-diff |
| xplr | 1518/1583 | needs reference-diff |

---

## Factory Accepted — 9 tools

| Tool | Score | Notes |
|------|-------|-------|
| fzf | 3606/3852 | large test suite |
| ov | 3862/4195 | large test suite |
| jplot | 1424/1444 | PARKED — best is v2 at 1438/1444 (v3 regressed) |
| bartib | 886/929 | demoted 2026-06-10: eval_report shows 41 failures; claimed 722/722 unverified |
| run | 693/1585 | needs eval |
| ast-grep | 17/1232 | needs eval |
| bat | 30/1178 | needs eval |
| fasttext | 353/665 | needs eval |
| age | 137/1038 | needs eval |

---

## Pending Unlock — 1 tool

| Tool | Score | Action |
|------|-------|--------|
| argc | 400/1375 | Verify per Section 5 before archiving |

---

## Parked — 2 tools

| Tool | Verdict | Best Score | Root Cause |
|------|---------|-----------|------------|
| igrep | harness-gap:parked | 862/1408 | Docker image layering — /workspace/executable conflict |
| jplot | best-only:park | 1438/1444 v2 | v3 -cover flag regression; 2 irreconcilable failures |

---

## Active Batches

| Batch | Owner | Wave | Slugs | Status |
|-------|-------|------|-------|--------|
| CODEX-001 | Codex | T3 | fzf · ov · fasttext | **reconciled** — all 3 bounced |
| CODEX-002 | Codex | T1 | argc · run | **hetzner_eval_running** (PID 2913257) |
| CODEX-OVERRIDE-001 | Codex | T2 | bartib · age · bat · ast-grep | **active** (user-authorized) |

**CODEX-001 (reconciled)**: All 3 bounced. fzf: Section 5 FAIL (89 bidir failures, 3 skips). ov: Score 52, large JUnit XML gaps. fasttext: Score 17, bidir prefix inversion.

**CODEX-002 (Hetzner running)**: argc and run tarballs repacked. Dispatched to Hetzner sequential chain. Log: `/root/determinex-programbench/_logs/codex002_eval.log`. argc expects ~975 tests to unlock; run has 79 C-lang skips that need gcc for strict lock.

**CODEX-OVERRIDE-001 (active)**: User-authorized emergency claim while rolling_queue was unwritten. Codex working on bartib/age/bat/ast-grep from Hetzner factory dirs. Handbacks expected next cycle.

---

## Rolling Queue (live — Codex self-claims ≤4 by CLAIM entry in CODEX_HANDBACK.md)

See `campaign_assignments.json` → `rolling_queue.slugs` for full ordered list (122 candidates).

**Top of queue** (after current in-flight):
1. `nikolassv__bartib` — factory_accepted, 66 not_run
2. `jhspetersson__fselect` — board_cache_only, 2780 not_run
3. `parcel-bundler__lightningcss` — board_cache_only, 2768 not_run (Hetzner dir exists)
4. `luajit__luajit` — board_cache_only, 2552 not_run
5. `stranger6667__jsonschema` — board_cache_only, 2461 not_run (Hetzner dir exists)

---

## Dispatch Log

| Date | Action | Slugs | Worker | Status |
|------|--------|-------|--------|--------|
| 2026-06-10 | Campaign bootstrap | — | claude | Complete |
| 2026-06-11 | CODEX-001 handback verified (hashes matched) | fzf · ov · fasttext | claude | Complete |
| 2026-06-11 | Hetzner eval chain (CODEX-001) | fzf · ov · fasttext | hetzner | Complete — all bounced |
| 2026-06-11 | Assigned CODEX-002 (T1 cap removal) | argc · run | claude | Complete |
| 2026-06-11 | Hetzner eval chain (CODEX-002) | argc · run | hetzner | Running (PID 2913257) |
| 2026-06-11 | CODEX-OVERRIDE-001 ratified | bartib · age · bat · ast-grep | claude | Active |
| 2026-06-11 | Rolling queue written (122 slugs) | — | claude | Complete |
| 2026-06-11 | PROTOCOL.md amended (rolling queue + parity tiers + corpus flywheel) | — | claude | Complete |
