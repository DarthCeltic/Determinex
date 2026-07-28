# ProgramBench Campaign: All 200 to Ceiling

> **Adopted 2026-06-09.** Operator decisions recorded this date:
> **(1) Target = dual ledger, every tool driven to its proven ceiling.**
> **(2) Self-contained — no upstream ProgramBench engagement; impossible tools get ceiling-proof docs.**
> **(3) Moderate compute cadence — one Hetzner wave at a time, DeepSeek/local for fix loops, Claude in-session.**
> **(4) Hybrid ops — autonomous for mechanical phases (waves, triage, board sync); interactive sessions for per-tool lock engineering.**

---

## The dual ledger (definition of done)

| Ledger | Definition | Current | Max achievable (2026-06-09 evidence) |
|---|---|---|---|
| **strict_lock** | passed==total, 0 skipped, 0 not_run, guard-clean, archived | **48** | **~178** (173 zero-skip tools + 5 env-fix recoveries) |
| **reference/upstream-skip parity** | failed==0, not_run==0; every miss is a hard upstream skip or equivalent reference/environment skip | **10 near-locks** | **~15–20** |
| **ceiling_confirmed** | structurally impossible; signed proof doc per tool | **10** | Current ceiling register / eval_index rows |

Campaign is DONE when every one of the 200 rows is in one of the three ledgers
with a fresh (<48h at time of archival) full-suite eval as evidence.
**"200 locks" = 200 rows at proven ceiling**, headline written as:
*N strict + M parity + 7 ceiling-proofs = 200/200 accounted.*

Machine-readable ledger: [`corpus/programbench/ceiling_register.json`](../../../corpus/programbench/ceiling_register.json)
(regenerate after every wave: `python scripts/pb_ceiling_register.py`).
Canonical per-tool state: [`corpus/programbench/eval_index.json`](../../../corpus/programbench/eval_index.json).

## Live state update (2026-06-13, historical — corrected 2026-06-30)

`corpus/programbench/eval_index.json` is the active source of truth. **Corrected
headline: 0/200 official full-suite locks** (the historical "64/200 = 32.0%" below
counted upstream source builds, invalidated by provenance audit — see
`docs/papers/PROGRAMBENCH.md`'s correction banner). The guard stack below describes
state as of 2026-06-13, pre-correction:

- `scripts/pb_doc_count_check.py`: OK, all scanned doc counts match eval_index.
- `scripts/pb_board_guard.py --guard`: 0 eval_index invariant violations.
- `scripts/pb_override_scan.py --guard`: 0 official-lock override violations.
- `scripts/claim_scanner/day_one_public_claim_scanner.py --root .`:
  `DAY_ONE_PUBLIC_CLAIM_SCANNER_PASSED`.

The June 9 counts below are retained as campaign history and should not be used
for current planning if they conflict with eval_index.

## Current state (eval_index, official metric, 2026-06-09)

**Session update (2026-06-09, Sonnet):** +64 strict locks (historical baseline) via two root-cause fixes applied to ALL 200+ per_tool_overrides:
1. **Dangling `if len(items) > 400:` SyntaxError**: 119 tools had broken conftest → all not_run. Fixed.
2. **nodeid-prepend**: rootdir=/workspace/ generates `tests.*` classnames but `eval.tests.*` expected. Fixed for 211 tools (entr excluded — has custom atexit).
New strict locks: tparse (556), code-minimap (369), rnr (740), dupl (450), tex-fmt (495). Evals in progress for git-trim, muffet, grex, nsh, entr, eva, run.

- **20 strict_lock** · 6 upstream_skips (parity) · 7 ceiling_confirmed · 1 reference_parity (pingu) · 49 pending_unlock · 117 board_cache_only (stale)
- **Structural fact that shapes everything:** The gap is `not_run` — whole branches/modules absent from JUnit XML. Root cause now confirmed: classname namespace mismatch (`tests.*` vs `eval.tests.*`). The nodeid-prepend fix is corpus-wide.
- board_cache_only tools need Hetzner (no local source tarballs available; factory dirs contain Python wrappers only).

## Skip-class discoveries (2026-06-09 census)

Five tools previously assumed parity-capped are **strict-eligible after container/env fixes**:

| Tool | Skips | Cause | Recovery |
|---|---|---|---|
| run | 79 | "rust/c/go/cpp/js/ruby is not available" | provision toolchains in compile.sh |
| fzf | 3 | man command non-functional in container | install man-db/groff or ship raw-groff fallback |
| keifu | 4 | pytest-dependency cascade (parent TUI tests) | fix parents; skips self-clear |
| hck | 1 | zstd not available | install zstd / build with zstd feature |
| elfcat | 1 | 32-bit compilation unavailable | gcc-multilib in compile.sh |

Five need probes (reasons unverifiable from archived reports): ripgrep, quickjs, xq, chroma, oha.
Ten are confirmed parity ceilings (hard `@pytest.mark.skip` / root-container): htmlq, csview,
entr, pingu, rustowl, sd, tuc, parqeye, zip-password-finder, rumdl.

---

## Phase order

### Phase 0 — Truth consolidation (now; autonomous)
1. ✅ Ceiling register generator + first run (this commit).
2. Ingest Hetzner Wave 2 (12 tools) on completion; stamp eval_index provenance.
3. **Single source of truth:** eval_index.json generates `POOL_STATUS.md`, the corpus README
   board, and paper stats. Fix/retire whatever regenerates `logs/programbench_lock_board.json` —
   it currently **drops the audit's `official_*` fields** (0/200 rows carry them today) and
   still reports the dead subset metric ("locked: 80"). Until fixed, lock_board.json is
   non-authoritative.
4. Pool hygiene: exclusion list for `.vscode` / `tier_*` phantom rows (board shows 203 rows).
5. Doc truth-sync: paper status block corrected (done this commit); CLAUDE.md counts on next
   operator pass.

### Phase 1 — Re-baseline the 117 unknowns (autonomous; 2–3 Hetzner waves)
- Their numbers predate cap removal; Wave 1 proved drift runs in BOTH directions
  (hexyl/fd drifted up 61 points). Ranking the 117 before re-evaling them is fiction.
- Per wave: rebuild uncapped tarballs with the **simple locked/-style conftest**
  (the ast.parse semantic-TUI-filter conftest caused `results_read_failed` on 9 of 56 Wave-1
  tools — retired), `pb_override_scan.py` clean, ship via
  `pb_export_hetzner_shard.py → pb_hetzner_eval_shard.sh → pb_import_hetzner_shard.py`.
- Expect surprise near-100s; archive anything that lands strict on arrival.

### Phase 2 — not_run triage automation (autonomous build, one-time)
- New `scripts/pb_notrun_classifier.py`: per tool × branch, diff tests.json vs JUnit XML;
  type every gap: `branch_build_fail` | `module_collect_error` | `phantom_id` |
  `upstream_skip` | `infra`. Emit typed fix-packets to
  `logs/programbench_factory/fix_packets/`.
- Queue rank key = **tests-recovered per branch fixed** (descending), not raw gap.

### Phase 3 — Lock-Factory drain (interactive sprints, queue-ordered)
1. **Env-fix strict recoveries** (cheap, big optics): run(+79), fzf-skips, keifu, hck, elfcat.
2. **priority_1_under100** (10 tools, proven sprint-sized): entr 35 · code-minimap 55 ·
   dupl 57 · rnr 58 · nomino 65 · git-trim 66 · elfcat 70 · muffet 74 · tex-fmt 94 · tparse 99.
3. **101–300 band** (25 tools, ~5.1K tests): ngrrram 121 · flamelens 125 · xplr 138 ·
   keifu 141 · miniserve 146 · seqtk 161 · oha 165 · igrep 174 · rustowl 188 · i3-style 211 ·
   xsv 217 · rhit 232 · clog-cli 234 · deadnix 242 · thokr 252 · hck 255 · cheat 261 ·
   bore 266 · jplot 267 · eureka 272 · tailspin 288 · pier 298 (+ post-rebaseline entries).
4. **301+ tail** (141 tools) ordered by branch-concentration from Phase 2 packets;
   feature-campaign tools (fzf 963-test gap, run 892 post-env-fix, dsq/trdsql 363…) last.
5. Probes for the 5 unverified-skip tools fold into their sprint.

### Phase 4 — Edges
- pandoc: one bounded Haskell build-deps sprint; if still blocked → ceiling_register entry
  with proof, ledger `ceiling_confirmed`.
- kiro-editor: first-ever eval in next wave; classify from zero.
- Ceiling-proof docs for the 7 impossible tools (evidence packets exist in CLAUDE.md notes;
  formalize under `corpus/programbench/ceiling_confirmed/<tool>/PROOF.md`). Self-contained —
  no upstream filings per operator decision.

---

## Factory tweaks (standing rules)

1. **eval_index.json is the only board.** Everything else derives. Any script that writes
   lock_board.json must preserve `official_*` fields or be retired.
2. **Auto-ingestion:** import + eval_index update on a poll loop after every wave launch —
   Wave 1 results sat unread for 2 days. Provenance stamps (`last_eval_date`, `source`)
   mandatory per board-staleness protocol (never plan on numbers >48h old).
3. **Conftest standard:** locked/-style simple conftest only. No collection caps, no
   semantic filters. `pb_override_scan.py --guard` runs on **every rebuild**, not just
   lock archival.
4. **Lock archival gate (unchanged):** official full-suite eval, passed==total, 0 not_run,
   0 skipped, guard-clean, archive to `corpus/programbench/locked/<tool>/`, eval_index
   updated same commit.
5. **Parity archival (new):** same gate except misses must be 100% hard-skip-classified in
   ceiling_register; archive to `corpus/programbench/locked/<tool>/` with
   `ledger: reference_parity` in eval_index.
6. **Hard rules carry over:** never edit eval fixtures unless provably broken (verify against
   upstream binary); one tool at a time in sprints; eval after every meaningful change.

## Throughput expectation (moderate cadence)

- Phase 0+1: ~1 week wall-clock, mostly machine time.
- Phase 3 band 1–2: days–2 weeks (sprint-sized, proven pattern).
- Band 3: ~2–6 sprints/tool → several weeks.
- Tail: multi-month grind; pace governed by branch-concentration ranking and one-wave-at-a-time
  eval cadence. Re-rank after every wave; the register is the dashboard.
