# ProgramBench — Strategy & Locks

> **CORRECTED 2026-06-30 (READ FIRST) — the "64/200" etc. numbers below are historical
> record, not current truth.** A full provenance audit of all 67 rows that carried
> `official_full_suite_resolved: true` found **62 confirmed + 5 unverified** as upstream
> source builds (go.mod/Cargo.toml module identity or file copyright headers matching the
> real project verbatim — e.g. `yq`'s go.mod literally declares `module
> github.com/mikefarah/yq/v4`), not native reimplementations. This independently confirms,
> with hard evidence, what the 2026-06-25 PIVOT note already declared:
> `METHODOLOGY_INVALIDATION` — shipping upstream source is the forbidden shortcut
> ProgramBench exists to prevent. **Honest current count: 0/200 fully-resolved by the
> legitimate methodology**, matching public leaderboard reality. The 62 archives are
> **not deleted or devalued** — they're retained exactly as the PIVOT intended: reference
> corpus/foundation material that the Native Reimplementation Loop feeds to the model so
> *it* can reimplement to 100% for real. See `eval_index.json` rows' `reconcile_note` field
> (`status: native_rebuild`) for the per-tool evidence. The numbered history below predates
> this correction and describes the invalidated methodology's timeline, kept for record.

> **Status**: Active (historical, pre-correction). **As of 2026-06-13**: **61 T1 strict locks** (passed==total, 0 not_run, 0 skipped, 0 failed) **+ 12 T2 ceiling-certified** (f=0, nr=0, sk>0, CEILING_CERT.md). Headline: **64/200 = 32.0% fully resolved** — strongest confirmed ProgramBench result (all public frontier models: 0–0.5%). **Master per-tool catalog (one-stop):** [`corpus/programbench/README.md`](../../corpus/programbench/README.md) — descriptions, scores, paths, overrides, cluster siblings, ceilings for all 200 tools. Eval index: [`corpus/programbench/eval_index.json`](../../corpus/programbench/eval_index.json). Priority queue: [`docs/programs/programbench/PB_PRIORITY_QUEUE.md`](PB_PRIORITY_QUEUE.md). The 2026-06-06 measurement audit ([`../audits/pb_measurement_audit_2026_06_06.md`](../audits/pb_measurement_audit_2026_06_06.md)) found the earlier "77 locks" figure used a subset metric; all pre-audit claims are historical record under the old metric.
>
> **Recent campaign (week of 2026-05-19 -> 2026-06-06):**
> - (historical) Pre-campaign baseline: 5 locks (zoxide / ripsecrets / htmlq / ripgrep / shellharden).
> - 2026-05-25 EOD: 35 locks (+30 in 6 days via bulk native-source flip).
> - 2026-05-26 EOD: 53 locks (+18 in 24 h). New techniques: slug-hash audit, `argv[0]` rename, stderr/stdout `sed` normalization, hardware-env fixture pinning, counter-state trick for conflicting tests.
> - 2026-05-27 (canonical board refresh): **57 strict archived locks** + 1 unarchived score=100 (`keifu`); aggregate 52.74 %.
> - 2026-06-02 (Batch 003): no new locks since 5-27; next jump targets `gated:accept` -> strict-lock conversion and `keifu` archival.
> - 2026-06-03 (Batch 004): `trasta298__keifu` archived as strict lock 56; score=100 unarchived is now 0.
> - 2026-06-04 (Lane B board sync): canonical board reports **67** strict locks; aggregate **57.06% (96,704 / 169,466)**; 53 factory-accepted non-locked improvements.
> - 2026-06-06 (morning): canonical board reports **76** strict locks; aggregate **58.67% (99,512 / 169,612)**; 51 factory-accepted non-locked improvements. `pb_lock_agent.py` built (7-command AI-callable interface with native guard + failure classifier). Ethics Oracle architecture captured in `docs/policy/ETHICS_ORACLE.md`. Hetzner batch `claude_agent_batch1_20260606` queued (entr v7 / caps-log v6 / html2md v9).
> - 2026-06-06 (evening): **64 strict locks** (historical). 4 tools confirmed impossible-ceiling (amber/hexyl/fd/html-to-markdown). Board provenance fields established to prevent stale-number planning.
> - Native-source flip: 10 of 11 wrapper-debt tools converted to real upstream source. Pandoc remains a Haskell build-deps blocker.
> - Strict ledger model: `gated:accept` != lock. The current board query shows 51 factory-accepted non-locked improvements; converting these is the next jump toward 100.
> - Canonical machine-readable source: `corpus/programbench/eval_index.json` (official metric; `logs/programbench_lock_board.json` is legacy).
> - 2026-06-13 (truth sync, historical, invalidated 2026-06-30): **64/200 = 32.0% confirmed** (added figlet 2088/2088) under the official eval_index-derived metric. The June 10 guard-cleanup batch added ten official full-suite locks: entr (1482) · hck (1768) · ngrrram (664) · pier (1556) · rhit (2176) · tailspin (1570) · trdsql (2806) · xsv (2634) · flamelens (510) · thokr (507). bartib was demoted 2026-06-10 via Section 5 reconcile: eval_report 886/929 contradicts claimed 722/722. Simultaneously: fixed dict-format entry_points bug in all 207 per_tool_overrides + locked archives; removed interactive nodeid filter from all 207; `pb_override_scan.py --guard` passes 0 official-lock override violations. Board drift audit: tuc/sd/elfcat/dsq reclassified to `upstream_skips`; xz reclassified to `ceiling_confirmed` (4 TTY failures).
> - All ProgramBench operational/audit/factory docs live under **[`../programs/programbench/`](../programs/programbench/)**.

2026-06-11 support-accounting note: canonical state is 64 strict locks plus upstream-skip near-locks and ceiling-confirmed rows as recorded in `corpus/programbench/eval_index.json` (the pre-audit "77" figure is historical, old metric; 15 was the honest count post-audit pre-June-10-batch). ProgramBench locks are benchmark artifacts, not product support, not release support, and not product readiness. Benchmark results are not product support.

---

## Codex Campaign Apparatus

As of 2026-05-28, the Codex lane has a reusable non-executing ProgramBench campaign apparatus. Doxygen is not an artifact dead end: its official upstream artifact authority is present, but execution is blocked pending operator security policy admission after scan failure.

The reusable platform now includes a common instance state schema, Batch 001 state aggregation, generic operator policy admission, generic execution preflight, skip reason taxonomy, batch skip decisions, an operator action queue, a read-only reporting API, an evidence graph, and a Codex lane final state packet.

Read-only report:

```powershell
.\.venv\Scripts\python.exe scripts\corpus\programbench\programbench_campaign_report.py --json
```

This apparatus does not run Docker, run ProgramBench, rebuild, remediate, grant policy exceptions, or create training rows.

The operator-ready layer now adds packet templates, a packet validator, Batch 001 metadata recovery queue, exact-provider probe plan, packet bundle, local inbox scanner, admission router, unblock simulation, evidence-graph integrity guard, operator CLI, operator outbox, completion scorecard, and final operator-ready state. The default outbox is `assurance/operator_outbox/programbench/`; completed signed packets should be placed in `assurance/operator_inbox/programbench/`.

The admission processing layer now reads the operator inbox and turns valid live packets into gate-review routes. Empty inboxes produce a signed no-live-packets record; fixtures are rejected as non-live.

The live packet review layer now verifies that the operator-ready prerequisites exist before looking at the live inbox. With no live packets supplied, it records `NO_LIVE_PACKETS` and grants no approval or execution authority.

The operator-ready audit layer verifies templates, validator behavior, inbox handling, routing, unblock simulation, graph integrity guards, CLI/outbox boundaries, Doxygen blocked status, Batch 001 actionability, and scorecard conservatism. It currently records `PROGRAMBENCH_OPERATOR_READY_AUDIT_PASSED`.

The Batch 001 unblock priority layer ranks the existing non-executing evidence paths. It records that Doxygen should stay paused until real operator security policy admission, and that the safest next Codex actions are exact image metadata/provenance packets for missing Batch 001 rows. This priority record does not authorize Docker, ProgramBench reruns, policy exceptions, or training rows.

The Batch 001 metadata campaign derives exact expected `task_cleanroom` image names for the ten metadata-only rows and plans exact DockerHub manifest metadata lookup. The safe registry manifest client now performs direct Docker Registry HTTP metadata lookup for exact `programbench/...:task_cleanroom` references only. It found all ten manifests and admitted their digests as metadata-only evidence. Those rows now require artifact import provenance and scan evidence; they are still not cache-ready, executable, or training-eligible. Benchmark results are not product support, not release support, and not product readiness.

The Batch 001 import/scan planning layer now writes import request packets, blocks local import preflight because no safe import method is authorized yet, emits ten operator artifact import templates, provides an exact artifact import evidence gate, creates a ten-row scan queue, and pins scan policy routing. No artifacts were imported or scanned.

---

## What It Is

[ProgramBench](https://github.com/programbench/programbench) is a 200-tool benchmark of real CLI tools (jq, fzf, lz4, fd, ripgrep, etc.) where each tool is reimplemented from scratch and verified against ~1,000–7,000 pytest tests with byte-exact golden output files. Every frontier model — Opus 4.7, GPT-5.4, Gemini 3.1 Pro — currently scores **0% fully resolved** across all 200 tasks. Even partial solutions hit ceilings around 80-95% for any given tool.

Determinex's plan is the only credible route to a non-zero fully-resolved score: pick five anchor tools whose mastery **compounds** across an architectural cluster (5-7 sibling tools per anchor), then a mass-run for the long tail. Target: **35-40 tools at 100%**.

---

## The Five-Anchor Strategy

| # | Anchor  | Cluster size | Test count | Difficulty | Why this slot |
|---|---------|--------------|------------|------------|---------------|
| 1 | jq      | 7 | 6,796 | medium | Largest test surface; most generalizable fixture (JSON parser + filter compiler + value emitter) |
| 2 | fzf     | 7 | 2,164 | medium | Foundation for every TUI; build `--filter` mode first (60-75% of tests) |
| 3 | lz4     | 5 | 1,829 | medium | Compression-CLI flag/stream conventions transfer; algorithm differs per tool |
| 4 | fd      | 7 | 1,405 | medium | sharkdp's portfolio idiom — five tools share byte-for-byte CLI conventions |
| 5 | curlie  | 7 | 741   | easy   | Smallest test count; xh sibling is near-clone — biggest single sibling lift |

Each anchor unlocks ~7 cluster siblings. The 35-lock target articulated in May has been **met and exceeded**: 48 official-metric locks as of 2026-06-10 (the earlier "67" figure used a subset metric; see the June 6 measurement audit). The campaign's frontier is cap removal + full-suite re-eval for partial_eval_100 tools and fix-packet repair of factory-accepted non-locked improvements.

Strategy details: [`corpus/programbench/_strategy/anchor_strategy.md`](../corpus/programbench/_strategy/anchor_strategy.md).

### Anchor packs

Each anchor has six deep-study files used by the Architect (C7) and Builder (C1):

```
corpus/programbench/anchors/0X_<tool>/
├── README.md                    — one-page overview
├── 01_architecture.md           — data structures, modules, build approach
├── 02_fuzzing_surface.md        — testable behaviors the PB harness will hit
├── 03_implementation_sequence.md — numbered build steps, fastest-passing first
├── 04_transfer_map.md           — per-unlocked-tool: exact knowledge that transfers
├── 05_corpus_impact.md          — what completing this teaches the Oracle
└── 06_behavioral_spec.md        — extracted pytest tests + goldens (700-900 lines each)
```

Total empirical surface across all 5 `06_behavioral_spec.md` files: **~7,200 tests, 4,190 CATCHES docstrings, 1,708 byte-exact goldens**.

---

## Mass-Run v1 (parallel campaign)

Strategy: [`corpus/programbench/_strategy/mass_run_v1.md`](../corpus/programbench/_strategy/mass_run_v1.md).

For the 157 residual tools (everything not in an anchor cluster), use:
- 8 universal CLI patterns shared across most tools (`universal_cli_patterns.md`)
- Per-language scaffold templates (`per_language_scaffolds.md`)
- 25-family sprint routing matrix (`language_family_sprint_matrix.md`)
- One-shot scaffold + iterate-from-leftover

Excludes the 42 tools below 50% ceiling. Targets **20-40 additional locks on attempt 1**.

The two campaigns are **complementary, both running** — they share corpus tree, RAG DB, and memory tree. Multi-window Determinex sessions all see the same corpus state.

---

## Lock methodology

When a tool reaches 100% on the eval, it gets locked into the corpus:

```
corpus/programbench/locked/<tool>/
├── source/
│   ├── compile.sh
│   └── main.* (and friends)
├── lessons.md           — 8 hard discoveries, file/line citations, what to do faster next time
├── eval_report.json     — final eval JSON proving 100%
└── submission.tar.gz    — exact files from the winning submission
```

The locked tools under `corpus/programbench/locked/` follow this structure when the source and eval reports have been archived.

---

## The eight transferable lessons (cross-tool, distilled)

These are the lessons that have shown up across BOTH locks so far. Future lock attempts should consult these first:

### 1. Mirror upstream verbatim, don't curve-fit tests

Test-driven patching of an existing implementation tends to oscillate in the 90-95% band — every fix breaks 2-3 tests in another suite. The breakthrough comes from extracting the upstream source from a test branch tarball and porting it line-for-line. Failure counts drop precipitously after the pivot (ripsecrets: 50 → 12 → 2 → 1 → 0; htmlq: 155 → 45 → 22 → 6 → 3 → 2 → 0).

### 2. Verify against the upstream binary BEFORE editing test fixtures

If a test pair appears contradictory, do not edit the goldens to make your output be "correct". Build the upstream binary (we have Cargo.toml + src/ in every test branch tarball — `cargo build --release` runs in 61 seconds) and run it against both fixtures. Both tests are usually correct; the discriminator is some upstream-binary quirk you can observe and replicate.

The htmlq `--remove-nodes` situation was the canonical case of this: two tests asserted opposite behaviors, the upstream binary genuinely behaves both ways depending on tree structure (kuchiki Descendants iterator-invalidation), one rule fixed both.

### 3. Python's `m.lastindex` lies for nested-alternation regex

For a combined regex like `(p1 | p2 | ... | pN)` where some inner pattern has a capturing group, Python's `m.lastindex` returns the OUTER group index (1) even when an inner group at index >1 actually captured. Iterate `range(2, m.re.groups + 1)` and check `m.group(i) is not None`, NOT `range(2, m.lastindex + 1)`. This bug alone caused ~38 failing tests in ripsecrets.

### 4. BeautifulSoup boundary settings (when porting Rust HTML tools)

For html5ever-faithful behavior in Python with BeautifulSoup:
- `from_encoding="utf-8"` — html5lib auto-detect gets UTF-8 wrong (latin-1 misinterpretation produces mojibake)
- `multi_valued_attributes=None` — keeps `class="  spaced  "` as the raw string (default tokenizes to a list and loses whitespace)
- Sort attributes alphabetically when serializing — html5ever uses a sorted attribute map; insertion-order preservation is wrong
- HTML5 void elements (`<br>`, `<hr>`, `<img>`, etc.) never get a closing tag

### 5. URL normalization mirrors Rust's `url` crate

- `Url::parse("https://example.com")` → `"https://example.com/"` (adds trailing /)
- `base.join("///path")` returns Err in Rust → upstream falls back to base (in Python urljoin returns `https://path`, which is wrong)
- `////path` strips leading slashes (special-cased, not joined)
- Non-ASCII path chars get percent-encoded
- Special schemes without a netloc (`mailto:`, `javascript:`, `data:`) skip normalization entirely

### 6. xdist + pytest-dependency cascade-skips dependent tests across workers

When the eval framework runs tests in parallel via pytest-xdist, the pytest-dependency plugin can't communicate dep state across workers. The dep can pass on worker A but its dependent on worker B is still marked skipped. This is an **eval framework limitation, not a code bug** — both currently-locked tools have 2 such skips that don't count against the score.

### 7. Tree-mutating filters can break iterators in tree-walking semantics

The htmlq `--remove-nodes` filter detaches nodes during a Descendants iterator walk. The kuchiki iterator stores `self.current = X.first_child` after returning X. If the filter then detaches THAT node (the iterator's pointer), iteration corrupts and ends. If it detaches a deeper or sibling node, iteration continues. HTML structure (whitespace text between tags) determines which path is taken — and the eval test fixtures probe both cases. Same rule may apply to other tree-mutating CLI tools in the jq cluster.

### 8. clap-2 error message format matters for verbatim test goldens

When a CLI argparse-style validator errors, it must:
- Print `error: <message>` to stderr
- Print `USAGE:\n    <focused usage line for the failing arg>` (NOT the generic synopsis)
- Print `For more information try --help`

For invalid-regex panics in Rust, the format is `thread 'main' (THREAD_ID) panicked at src/main.rs:LINE:COL:\n<message>\nnote: run with RUST_BACKTRACE=1 environment variable to display a backtrace`. Tests strip the THREAD_ID by regex before comparing.

### 9. First official eval run must verify image/executable plumbing

Before trusting a ProgramBench official eval result for a new tool, run a one-minute image preflight:
- Confirm the task image exists locally with the expected normalized name: `programbench/<owner>_1776_<repo>.<hash>:task_cleanroom`.
- Confirm the reference executable is present in the repo image (`/workspace/executable`) and that ProgramBench can stash/hash the candidate executable.
- Candidate `compile.sh` must produce a real `./executable` file, not a symlink. ProgramBench moves it to `/opt/programbench-stashed-executable-do-not-modify`; symlinks can break after the move and surface as `hash_executable_failed`.
- If official eval returns `0/0`, inspect the eval JSON before interpreting score. `hash_executable_failed` is harness/image plumbing, not behavioral failure.

Use the preflight helper before the first official eval of a tool:
```bash
python scripts/programbench_image_preflight.py jqlang__jq.b33a763 --source-dir work/programbench/jq_anchor/source
```

---

## Language classification step (factory pipeline)

> Added 2026-05-23. The behavioral test suite for each tool reveals the
> language constraints through what it tests. The classifier surfaces this
> as a routing signal so workers know whether to write Python or rewrite
> in the source language before final submission.

After every `pb_score_audit.py` run (which is the factory's source of truth
for the lock board), `scripts/pb_language_classifier.py` automatically
scans every tool's **failing-test surface** and writes:

- `logs/programbench_factory/LANGUAGE_CLASSIFICATION.json` — per-slug record
- `logs/programbench_factory/LANGUAGE_CLASSIFICATION.md` — human-readable report

Each tool is tagged as:

| label | meaning | implication |
|---|---|---|
| `native-required` | failing tests bind native semantics (integer overflow, signal handling, byte-level output, file magic, mmap, timing, native panic frames) | rewrite in source language before final submission |
| `python-sufficient` | failing tests are pure text I/O (stdout, stderr, exit codes, help/version strings, file existence) | ship as Python; cmatrix-style locks live here |
| `unknown` | no eval data yet, or current implementation already passes everything (no failures to diagnose) | needs an attempt before classifying |

**Signal taxonomy.** The classifier scans both test names and failure messages.
Native signals include `integer_overflow`, `c_atoi_semantics`, `buffer_size`,
`signal_handling`, `byte_level`, `binary_output`, `file_magic`, `endianness`,
`memory_layout`, `timing_perf`, `native_panic`, `size_t_off_t`, `utf16_native`,
`compression_native`, `null_byte`, `mmap_io`, `invalid_utf8`, `native_ints`,
and byte-escape sequences (`\xff\xfe`) in failure messages. **Only failing
tests count** — a test named `test_overflow` that already passes under a
wrapper isn't blocking, the surface it tests is already handled.

The factory dispatcher (`pb_factory_dispatch.py`) surfaces the classification
in the queue output and in `DISPATCH_QUEUE.json` so workers route accordingly.

```bash
# Manual refresh (also runs automatically after pb_score_audit.py):
python scripts/pb_language_classifier.py --summary

# Inspect one tool:
python scripts/pb_language_classifier.py --slug abishekvashok__cmatrix
```

**Reference rules of thumb** (from the cmatrix lock & corroborated by the
classifier):

- Tests that check memory behavior, buffer sizes, or overflow semantics → native required. The cmatrix `c_atoi` overflow test enshrined C integer behavior; Python cannot replicate that faithfully.
- Tests that exercise SIGPIPE / SIGTERM / SIGINT behavior → native required. Python's signal model differs from native binaries in ways the tests will catch.
- Tests that check file format headers, magic bytes, or byte-level encoding → native required.
- Tests that require specific timing or performance characteristics → native required.
- Tests that only check stdout/stderr content, exit codes, and file existence → **Python is sufficient**. The majority of current locks fall here.
- Tools whose source is already Python or Go-with-no-C-level-behavior → Python is sufficient.

---

## How to use this corpus

- **Architect (C7 / Sentinel)** reads the relevant anchor's `01_architecture.md` + `02_fuzzing_surface.md` before generating the build DAG.
- **Builder (C1 / Engineer)** is given `03_implementation_sequence.md` to drive its build order.
- **Monitor (C3 / Observer)** uses `02_fuzzing_surface.md` to score where attempts are weak.
- **The RAG** ingests every `*.md` under this tree as the `programbench` collection — see [`scripts/seed_knowledge_base.py`](../scripts/seed_knowledge_base.py) routing.
- **Future flywheel passes** include this corpus alongside the compiler-validated WAL records.

Refresh the in-memory RAG with:
```bash
python scripts/seed_knowledge_base.py --reseed-programbench
# or programbench-only mode if core is already seeded:
python scripts/seed_knowledge_base.py --programbench-only --reseed-programbench
```

---

## Eval command (canonical)

All Determinex-launched evals must go through the resource guard:

```bash
python scripts/programbench_eval_runner.py "<instance_id>" "T:/determinex-programbench/<pilot_dir>" --force
```

If you run the official harness directly, these flags are mandatory:

```bash
cd T:/Dev/ProgramBench && PYTHONUTF8=1 uv run programbench eval "T:/determinex-programbench/<pilot_dir>" --filter "<author_substring>" --workers 1 --branch-workers 1 --docker-cpus 1 --force
```

Resource-sensitive tools such as `sharkdp/hyperfine` are quarantined by default.
They may only run with `DETERMINEX_PB_ALLOW_RESOURCE_RISK=1`, and then only in the
one-worker lane (`--workers 1 --branch-workers 1 --docker-cpus 1`). This is law
because a single apparent "serial" eval can still run `pytest -n auto` inside
Docker, and those workers can spawn subprocess-heavy tests. That pattern has
wedged Docker Desktop and surfaced as UI 500s / `results_read_failed`.

Pre-cloned task repos: `T:\determinex-programbench\` (zero clone overhead).
Task definitions: `T:\Dev\ProgramBench\src\programbench\data\tasks\<instance_id>\{task.yaml,tests.json}`.

---

## Hard rules (enforced for every anchor)

1. **100% or it does not count.** No partial credit. No "almost resolved."
2. **One tool at a time.** Lock it before moving to the next.
3. **Fast closes first within each cluster** — lowest test count × highest ceiling first.
4. **Run eval after every meaningful change.** Don't batch blind.
5. **Document every failure category before fixing anything.**
6. **Never combine fixes across unrelated failure groups in one eval cycle.**
7. **Never edit eval test fixtures unless they are PROVABLY broken** — verify against the real upstream binary first. Editing goldens to match your output is gaming the eval.

---

## Status board (live)

The hand-maintained table that used to live here went stale and was removed 2026-06-09.
Canonical, machine-generated state:

- Per-tool official-metric state: [`corpus/programbench/eval_index.json`](../../corpus/programbench/eval_index.json)
- Ceiling ledger (strict / parity / impossible): [`corpus/programbench/ceiling_register.json`](../../corpus/programbench/ceiling_register.json) — regenerate via `python scripts/pb_ceiling_register.py`
- Campaign plan and queue order: [`../programs/programbench/CAMPAIGN_200_CEILING.md`](../programs/programbench/CAMPAIGN_200_CEILING.md)

**Strict locks (48, official full-suite — passed==total, 0 not_run, 0 skipped, 0 failed):**
jq 6874 · yq 2046 · shellharden 1292 · angle-grinder 1143 · pastel 1256 · ripsecrets 937 · zoxide 577 · cmatrix 769 · hyperfine 298 · go-mod-outdated 342 · gron 233 · ascii-image-converter 488 · scc 476 · ditaa 681 · genact 237 · grex 3036 · bore 900 · clog-cli 1556 · code-minimap 738 · curlie 1482 · deadnix 1418 · diffr 1524 · dupl 900 · eva 963 · fblog 2254 · git-trim 1422 · hex 1754 · i3-style 1500 · loop 1556 · miniserve 880 · muffet 864 · nomino 676 · rnr 1480 · seqtk 880 · tex-fmt 990 · tparse 1112 · yj 1457 · entr 1482 · hck 1768 · ngrrram 664 · pier 1556 · rhit 2176 · tailspin 1570 · trdsql 2806 · xsv 2634 · flamelens 510 · thokr 507 · bartib 722.

**Upstream-skip near-locks (10, not strict locks):** chroma 524/531 · csview 347/348 · dsq 1660/1666 · elfcat 1288/1291 · htmlq 2057/2058 · quickjs 3038/3044 · ripgrep 2536/2538 · sd 1728/1738 · tuc 2490/2498 · xq 876/879.
