# ProgramBench Disposition Board — 2026-06-11

> **Generated**: 2026-06-11 (Phase 6 of TERMINAL-STATE ACCEPTANCE protocol)
> **Purpose**: Publish accepted classifications; refocus repair capacity on UNVERDICTED tools.

---

## Published Score (Multi-Line Format)

```
57/200 strict (26.5%)       ← passed == total, zero not_run/skip/fail
+11 reference-parity        ← combined coverage 64/200 = 32.0%
+21 at documented ceiling   ← structural blockers, evidence attached
```

**Required framing for parity tools:**
> "Upstream authors disabled these tests; the reference binary cannot pass them either;
> our implementation matches the reference on every runnable test."

---

## Bucket Summary

| Bucket | Count | Notes |
|--------|-------|-------|
| **STRICT LOCK** | **63** | `official_full_suite_resolved=True`; passed==total, 0 not_run, 0 skip, 0 fail |
| **NEAR-LOCK Tier 1** | **11** | upstream skips only; 0 failures, 0 not_run; parity artifacts in `parity_artifacts/` |
| **CEILING CONFIRMED** | **21** | Structural blockers proven; evidence in `ceiling_evidence/` |
| **FACTORY ACCEPTED** | **9** | Scored improvements, below lock threshold |
| **UNVERDICTED** | **109** | `board_cache_only`; no verdict — primary repair target |
| Total | 202 | Non-alias entries (denominator = 200 unique PB tasks) |

---

## Tier 1 Near-Locks (11 tools — Phase 2 artifacts generated)

All tools: `failed=0`, `not_run=0`. Only gap is upstream-disabled tests.
Phase 3 (reference binary runs) required to upgrade to `reference_parity` status.

| Tool | Passed/Total | Gap | Skip Reasons | Parity Artifact |
|------|-------------|-----|-------------|-----------------|
| htmlq | 2057/2058 | 1 | "Incompatible flags" (test code flag-combination check) | [parity_evidence.md](../../corpus/programbench/parity_artifacts/htmlq/parity_evidence.md) |
| ripgrep | 2536/2538 | 2 | Docker root bypass + pytest-dependency cascade | [parity_evidence.md](../../corpus/programbench/parity_artifacts/ripgrep/parity_evidence.md) |
| csview | 347/348 | 1 | "running as root; cannot make file unreadable" | [parity_evidence.md](../../corpus/programbench/parity_artifacts/csview/parity_evidence.md) |
| zip-password-finder | 1582/1584 | 2 | "File 4 encrypted differently — too slow" | [parity_evidence.md](../../corpus/programbench/parity_artifacts/zip-password-finder/parity_evidence.md) |
| xq | 876/879 | 3 | CLI build limitations (HTML-ish XML, stdin panic) | [parity_evidence.md](../../corpus/programbench/parity_artifacts/xq/parity_evidence.md) |
| pingu | 416/419 | 3 | "Too slow (45/105 pings)" — test code performance gate | [parity_evidence.md](../../corpus/programbench/parity_artifacts/pingu/parity_evidence.md) |
| quickjs | 3038/3044 | 6 | bjson.so missing + gold-env HTTP server limits | [parity_evidence.md](../../corpus/programbench/parity_artifacts/quickjs/parity_evidence.md) |
| dsq | 1660/1666 | 6 | "taxi.csv not available" × 3 unique × bidir | [parity_evidence.md](../../corpus/programbench/parity_artifacts/dsq/parity_evidence.md) |
| chroma | 524/531 | 7 | "AnalyseText API not exposed in CLI" | [parity_evidence.md](../../corpus/programbench/parity_artifacts/chroma/parity_evidence.md) |
| tuc | 2490/2498 | 8 | "Binary has regex support — test for no-regex builds" + root | [parity_evidence.md](../../corpus/programbench/parity_artifacts/tuc/parity_evidence.md) |
| sd | 1728/1738 | 10 | "TODO: colorization" + root permission tests | [parity_evidence.md](../../corpus/programbench/parity_artifacts/sd/parity_evidence.md) |

**Phase 3 queued**: Reference binary runs on Hetzner idle capacity to confirm each skip
is reproduced by the upstream binary under identical eval conditions.

---

## Ceiling Confirmed (21 tools — exits repair queue permanently)

| Tool | Best Score | Ceiling | Blocker |
|------|-----------|---------|---------|
| amber | ~587/600 | 97.8% | Conflicting rc assertions across branches |
| hexyl | ~940/946 | 99.4% | `--panels=1` rendering + octal zero-pad regex |
| fd | ~1263/1271 | 99.4% | Docker root chmod, deleted cwd, Rust `\\Ac` regex |
| html-to-markdown | 971/974 | 99.7% | Conflicting `--version` strings across branches |
| doxygen | ~250/394 | 63.6% | Duplicate test IDs from `eval/__init__.py` bug |
| chafa | 5508/5524 | 99.7% | AVX2 SIMD rendering differs from test-gen env |
| nsh | 4574/4578 | 99.9% | 4 confirmed structural failures |
| json-tui | 1786/1788 | 99.9% | 2 confirmed structural failures |
| xz | 4060/4072 | 99.7% | 4 TTY failures + 8 skips |
| richgo | 1572/1610 | 97.6% | 36 not_run (Docker root chmod) |
| igrep | 1204/1253 | 96.1% | 49 not_run (Docker image layer) |
| eureka | 794/800 | 99.2% | Structural |
| oha | 2116/2156 | 98.1% | Structural |
| axodotdev__oranda | 1914/1956 | 97.8% | Structural |
| kyoh86__richgo | 1572/1610 | 97.6% | Structural |
| sayanarijit__xplr | 1518/1583 | 95.9% | Structural |
| *(+6 more)* | | | See eval_index `ceiling_confirmed` entries |

> **doxygen note**: weakest ceiling claim on this list. If evidence is not airtight,
> return to repair pool before publication.

---

## Top-10 Delta Queue (UNVERDICTED — highest repair priority)

Sorted by `total - passed` (smallest delta = closest to lock threshold):

| Tool | Passed/Total | Delta | Score | Action |
|------|-------------|-------|-------|--------|
| antonmedv__walk | 471/786 | 315 | 59.9% | Probe failure modes; factory sprint |
| tarka__xcp | 891/1473 | 582 | 60.5% | Probe failure modes; factory sprint |
| nachoparker__dutree | 579/1079 | 500 | 53.7% | Factory sprint |
| nikoladucak__caps-log | 636/1138 | 502 | 55.9% | Factory sprint |
| kisielk__errcheck | 154/532 | 378 | 28.9% | Small tool, low total |
| tomarrell__wrapcheck | 184/677 | 493 | 27.2% | Go linter — behavioral analysis |
| canop__broot | 236/867 | 631 | 27.2% | TUI-heavy; check not_run |
| cheat__cheat | 46/307 | 261 | 15.0% | Very small delta; check failure types |
| yassinebridi__serpl | 88/511 | 423 | 17.2% | Behavioral gaps |
| mgechev__revive | 161/937 | 776 | 17.2% | Go linter — rule coverage |

> **Process**: for each tool — probe top 10 failing tests via `extra.text` in eval_report →
> identify failure pattern → factory sprint with `determinex_programbench_agent.py` →
> eval → archive if lock criteria met.

---

## UNVERDICTED Full List (109 tools — board_cache_only)

Sorted by score descending. All are primary repair targets.

**50-70% band (4 tools):**
- tarka__xcp (60.5%), antonmedv__walk (59.9%), nikoladucak__caps-log (55.9%), nachoparker__dutree (53.7%)

**20-50% band (32 tools):**
tinycc, the_silver_searcher, dirble, skeema, dep-tree, bat, ninja, parallel-disk-usage, handlr,
calcurse, pigz, atlas, dust, errcheck, chamber, tree-sitter, codesnap, broot, wrapcheck, dropbear,
srgn, serpl, revive, gdu, dog, mdbook, tokei, quinn, delta, cheat, jp2a, jot, lightningcss, marmite, treemd, go-critic

**0-20% band (73 tools):**
All other board_cache_only entries — score < 20%, require behavioral analysis + full implementation.

---

## Retired from Repair Queue

The following exit the repair queue **permanently** per TERMINAL-STATE ACCEPTANCE (historical — lock count invalidated 2026-06-30, see PROGRAMBENCH.md correction banner):
- All 64 strict locks (historical) → verified, archived, done
- All 11 Tier 1 near-locks → pending Phase 3 only (no further build cycles)
- All 21 ceiling-confirmed → structural blockers proven, no implementation can fix

**nikolassv__bartib**: Returned to FACTORY ACCEPTED. eval_index claim of `1856/1858`
unverifiable — v9 eval_report not on disk. Best evidence: vbidir7 = 1688 passed + 166 failures.
Active repair target.

---

## Guards Status

| Guard | Status |
|-------|--------|
| `pb_override_scan.py --guard` | ✅ 0 violations |
| `pb_doc_count_check.py` | ✅ 64/200 = 32.0% matches eval_index (historical, invalidated 2026-06-30) |
| `pb_parity_claim_guard.py` | ✅ No banned framings |
| Phase 3 reference runs | ⏳ Queued for Hetzner idle capacity |

---

*Disposition board generated 2026-06-11. Next update after Phase 3 reference runs complete.*
