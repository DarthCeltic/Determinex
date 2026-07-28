# Determinex ProgramBench Campaign Log

---

## Cycle 2026-06-11 (overnight → morning)

**Count before cycle**: 53/200 (26.5%)
**Count after cycle**: 56/200 (28.0%) — strict locks only, official metric

### Locks gained (verified via Section 5, parse of raw eval_report)

| Tool | Tests | Commit | Root cause fixed |
|------|-------|--------|-----------------|
| `stathissideris__ditaa.f2286c4` | 681/681 | 71aad15b8 | SyntaxError (leading comma) in conftest prevented patching → ClassNotFoundException |
| `oppiliappan__eva.41ae245` | 1926/1926 | 71aad15b8 | Factory tarball pre-guard: del items[400:] cap + TUI filter → bidir undercounted |
| `sitkevij__hex.61ae69b` | 1754/1754 | 71aad15b8 | Same factory tarball pattern as eva |

*Note: hyperfine.327d5f4 (596/596), aic.d05a757 (976/976), code-minimap.0ddeea5 (738/738) were archived in the immediately preceding commit (3832e7b1d, "53/200").*

### Phantom-catch re-parse (Section 5 re-verify all 64 eval_index strict locks)

- Scanned: 64 eval_index entries with `official_full_suite_resolved=True`
- **Clean**: 63
- **Demotions**: 1

**jplot** — demoted from `strict_lock` to `submetric_claim`
- eval_report shows: `{'passed': 2157, 'failure': 3}`, total=2160
- Lock was claimed via `without_ignored` submetric (3 gold_fail + 4 dummy_pass filtered)
- Phantom-catch correctly flagged this as non-standard metric
- Official count **unaffected** (jplot was never in the canonical 47 list)
- Demoted in eval_index, added to verdict corpus

### Three-way reconcile (eval_index ↔ filesystem ↔ campaign_assignments)

- eval_index → filesystem: 2 drift entries (`ekzhang__bore.8e059cd.eval`, `pemistahl__grex.fa3e8ed`) point to canonical lock dirs (`locked/bore/`, `locked/grex/`) which exist. Benign — hash variants without dedicated locked dirs. Slug typo in bore entry (`.eval` suffix).
- filesystem → eval_index: 44 locked/ dirs without `official_full_suite_resolved=True` — these are near-lock archives, factory bounces, and old evals. Not strict locks, no action needed.
- campaign_assignments: added ROLLING-003/004/005/006 batch records; `_last_reconcile` = 2026-06-11.

### Section 12 flywheel

- `lessons.md` written for: ditaa.f2286c4, eva.41ae245, hex.61ae69b
- `cross_tool_patterns.md` updated: Pattern 004 (factory tarball rebuild), Pattern 005 (conftest SyntaxError)
- (historical) Verdict corpus: 4 entries added (3 locks + jplot demotion)
- RAG reseed: deferred (requires `python scripts/seed_knowledge_base.py --programbench-only`; queue after fasttext v4 resolves)

### Fasttext oversight (PROTOCOL Section 1)

- **v3 verdict**: BOUNCE. `_xdist_groups` in conftest.py was overwritten by branch conftests before `pytest_collection_finish` could populate it → `_xg` empty → no xdist suffix injection → 2 `not_run` entries (`test_analogies_basic@analogies_serial`, `test_analogies_default_k@analogies_serial`).
- **v4 fix**: Moved `pytest_collection_finish` + `_xg` dict + xdist injection entirely into the pip plugin (`determinex_bidir.py`). Plugin is immune to conftest overwrites (entry_points loaded first). Added sidecar file `/workspace/determinex_xdist_groups.txt` for post-run verification. Generates BOTH `eval.tests.*` and `tests.*` variants of @suffix entries.
- **v4 status**: Running on Hetzner via queue watcher (starts once current 4-slot capacity clears). 
- **Verification gate (before accepting any fasttext v4 result)**:
  - (a) `/workspace/determinex_xdist_groups.txt` must be non-empty (≥2 entries: analogies_basic, analogies_default_k)
  - (b) `results.xml.orig` must exist; pass/fail/error/skip counts must match between orig and injected
  - (c) Section 5: passed==total, 0 not_run, 0 skipped, 0 failed

### Overnight queue manifest (Hetzner)

**Currently running** (4 slots at max capacity, ~14:45 UTC):
| Eval | Status |
|------|--------|
| solar (`paradigmxyz__solar.5190d0e`) | Running |
| walk (`antonmedv__walk.bf802ef`) | Running |
| typst (`typst__typst.88356d0`) | Running |
| ctags (`universal-ctags__ctags.243595e`) from ROLLING-002 | Running ~45 min |

**Queue watcher** (`/tmp/rolling004_queue.sh`, PID 1051884) — starts each as slots open:
1. lz4 (`lz4__lz4.1519f46`) — cap removal
2. cppcheck (`danmar__cppcheck.0a5b103`) — cap removal
3. chafa (`hpjansson__chafa.dd4d4c1`) — cap removal
4. fx (`antonmedv__fx.86d0d34`) — cap removal
5. zstd (`facebook__zstd.1168da0`) — cap removal
6. fasttext v4 (`facebookresearch__fasttext.1142dc4`) — xdist fix

**ROLLING-001/002 evals** (fselect, lightningcss, luajit, jsonschema, gomplate, ctags, masscan, chamber) — masscan finished, ctags still running. Results pending reconciliation.

### Hetzner allocation

- `PROGRAMBENCH_DOCKER_CPUS=8` set on all new launches (box has 8 CPUs; default 10 caused Fatal CPU range error)
- Load at cycle time: 0.41 (healthy). 94 GB free disk.
- Cloak SWE-bench rerun: NOT started this cycle (priority: lock evals win). Scheduled for after current queue drains.

### RELEASE_CHECKLIST delta

- Official count: 56/200 (28.0%)
- doc-guard: deferred (needs `just doc-guard` run after count updates propagate to docs)
- REPRODUCTION.md: not yet created (blocking doc-guard green)
- Patents: HUMAN-OWNED, not tracked by driver

---
