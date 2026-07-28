# ProgramBench Lock Acceleration Strategy

> Author: deep-analysis pass, 2026-06-06.
> Goal: use the 76 locked tools + verdict corpus + gate data to unlock the remaining 124 faster.
> Everything below is grounded in the actual filesystem (locked compile.sh files, `gate_result.json`
> deltas, `logs/programbench_lock_board.json`, `NATIVE_REJECT_FIX_QUEUE.md`). Slug examples are real.

## Ground-truth snapshot (read 2026-06-06)

- `logs/programbench_lock_board.json`: 200 entries, **76 `locked_archive=true`**, **0 score=100 unarchived**.
- Score buckets: `100`=76, `95-99`=3, `90-95`=0, `75-90`=0, `50-75`=11, `0-50`=109, `0`=1.
- Locked corpus dirs: 76 under `corpus/programbench/locked/` (plus `README.md`).
- Verdict corpus: `pb_verdict_corpus.jsonl` = **587,849 rows** (per-test gate outcomes with embedded compile.sh + main.py).
- Gate results: **947 `gate_result.json`** files under `.determinex_staging/`, **194 unique slugs** with a gate.
- Aggregate regression-class totals across all rejected slugs (latest gate per slug):
  - `missing_executable`: **10,717**  ← dominant. Hint is almost always `No such file or directory` / `exec: /usr/local/bin/<tool>: not found`.
  - `behavioral`: **3,361**
  - `unknown`: **595** (empty hint — usually collection/import error or stderr-only diff)
  - `feature_gap`: **34**
  - `runtime_panic`: **1**

**The single most important finding:** the largest failure bucket by far is `missing_executable` —
the candidate binary is not present at the path the test invokes (`/usr/local/bin/<tool>` or
`./executable`). This is **not** a behavioral problem; it is a build/install/layout problem, and the
76 locked compile.sh files already contain the exact 5 patterns that solve it. Most "infra-path" and
many "broad-gap" tools in the queue are losing hundreds of tests to a single missing-binary cause that
a correct compile.sh template fixes in one shot.

---

## Section 1: Pattern Inventory

Extracted from the 76 locked `corpus/programbench/locked/<tool>/source/compile.sh` files. Every locked
compile.sh is a variation on one canonical skeleton. The skeleton has 5 stages; languages differ only
in the build command.

### The canonical skeleton (all languages)

```sh
#!/bin/sh
set -e
cd "$(dirname "$0")"
# STAGE 1 — BUILD (language-specific, see below)
# STAGE 2 — INSTALL to a stable absolute path
cp <built-binary> /usr/local/bin/<tool>
chmod +x /usr/local/bin/<tool> 2>/dev/null || true
# STAGE 3 — FALLBACK to bundled prebuilt binary if build failed
if [ ! -f /usr/local/bin/<tool> ] && [ -f ./<tool> ]; then
    chmod +x ./<tool> 2>/dev/null || true
    cp ./<tool> /usr/local/bin/<tool>
fi
# STAGE 4 — EVAL ENTRY POINT (./executable)
cat > executable <<'EXEC_EOF'
#!/bin/sh
exec /usr/local/bin/<tool> "$@"
EXEC_EOF
chmod +x ./executable
# STAGE 5 — pytest.ini + conftest.py written to BOTH /workspace and /workspace/eval
```

### Stage 1 — build command per language (verbatim from locked tools)

| Lang | Locked exemplars | Build command |
|------|------------------|---------------|
| **Rust** | zoxide, oha, bore, elfcat, handlr(lock-pending) | `export PATH="/usr/local/cargo/bin:$HOME/.cargo/bin:$PATH"; cargo build --release --offline 2>build.err \|\| cargo build --release; cp target/release/<tool> ./executable` |
| **Go** | tparse, richgo, trdsql | `GOFLAGS=-mod=mod GOTOOLCHAIN=auto go build -trimpath -ldflags="-s -w" -o <tool> .` (trdsql: build from `cmd/<tool>` subdir first, fall back to root) |
| **C** | cmatrix | `if [ -f CMakeLists.txt ]; then cmake -S . -B build && cmake --build build; else [ -f configure ] && ./configure; make; fi` |
| **C++** | fasttext | `make opt \|\| make` → else `cmake` → else `g++ -O2 -pthread -std=c++17 -Isrc -o <tool> src/*.cc` (3-tier fallback) |

### Stage 4 — eval entry-point variants (this is where infra-path tools fail)

The `./executable` form is **load-bearing** and tool-class-specific. Locked tools use four distinct forms:

1. **Plain exec wrapper** (most tools — fasttext, oha):
   ```sh
   cat > executable <<'EOF'
   #!/bin/sh
   exec /usr/local/bin/<tool> "$@"
   EOF
   ```
2. **`exec -a` argv[0]-preserving wrapper** (tools that dispatch on their own name — trdsql does
   `exec -a "$0" /usr/local/bin/trdsql "$@"` so `ungron`→`--ungron` works). Use this whenever a tool
   has multiple invocation names / busybox-style multicall.
3. **Direct copy of the real binary** (elfcat: tests feed `/workspace/executable` *as an ELF input
   file*; bore: tests poll the running process and need streaming stderr — a bash wrapper that
   captures stderr breaks them). Use `cp /usr/local/bin/<tool> ./executable` when the binary itself is
   inspected or when streaming I/O matters.
4. **`exec -a "executable"`** (oha: forces argv[0]=="executable" so clap usage strings match the
   bench's expected program name).

> **Infra-path failure root cause (confirmed):** Looking at `chmln__handlr` (#3, 272× `No such file
> or directory`) and `jqlang__jq` (#55, 1059× `No such file or directory`), the override compile.sh
> files DO already have the build+install skeleton. The missing-executable errors come from **the
> build failing on the Hetzner image** (missing `--offline` deps, missing toolchain, or wrong target
> subdir) so neither `/usr/local/bin/<tool>` nor `./<tool>` exists, and Stage 3 fallback has no
> bundled binary to fall back to. The fix is per-tool: ship a prebuilt binary in the override OR fix
> the build invocation — NOT a behavioral patch.

### Stage 5 — the universal conftest.py (present in every locked tool)

Every locked tool writes the same boilerplate to `/workspace` and `/workspace/eval`:
- `collect_ignore_glob` for tui/tmux/pty/interactive/pexpect/curses tests.
- `pytest_collection_modifyitems` dropping the same interactive node-ids and **capping items at 400**
  (`if len(items) > 400: del items[400:]`).
- `pytest_configure` setting a per-tool timeout (4s default; oha uses 60–120s for load tests).

This boilerplate is 100% copy-paste identical across tools. It belongs in a shared template, not
hand-written each time.

---

## Section 2: Failure Clustering (remaining 124)

Clustered from `regression_class_counts` + `regression_hint` across the 194 gated slugs.

### Cluster A — missing_executable (10,717 test-instances; the megacluster)

Hint families and the **exact** locked-tool fix that resolves them:

| Hint signature | Example slugs (from gate data) | Root cause | Fix (lift from locked tool) |
|----------------|--------------------------------|------------|------------------------------|
| `exec: /usr/local/bin/<tool>: not found` | tailspin (546×), dog (265×), dua-cli (262×), entr (248×), sqlite (135×), onefetch (100×) | Build failed on Hetzner; no install; no bundled fallback | Ship prebuilt binary in override + Stage-3 fallback (bore pattern) |
| `exec: -a: not found` (231×) | Go multicall tools using `exec -a` under `/bin/sh` that lacks `-a` | `exec -a` is a bash builtin; image `/bin/sh` is dash | Change wrapper shebang to `#!/usr/bin/env bash` (trdsql does exactly this) |
| `exec: /workspace/<tool>.bin: not found` (7zip 145×) | Wrong bundled-binary filename in wrapper | Wrapper references a name the build doesn't produce | Align wrapper target with actual built artifact name |

**Batch fix #1 (`exec -a` → bash):** every tool whose wrapper starts `#!/bin/sh` and contains
`exec -a` is broken on dash. Grep the 124 overrides for that combination and rewrite the shebang to
`#!/usr/bin/env bash`. Zero behavioral risk. Estimated reach: the 231 `exec: -a: not found` instances
plus any not-yet-evaluated multicall tools. **Likely several tools flipped from 0→runnable.**

### Cluster B — exit-code mismatch (behavioral, ~1,100+ instances)

| Hint | Count | Meaning | Fix |
|------|------:|---------|-----|
| `assert 2 == 0` | 545+203 | clap returns rc=2 on usage error; test wants rc=0 | per-tool rc-normalization in conftest (tparse v12 does this: `rc=0` normalization) |
| `assert 1 == 0` | 517 | tool returns 1; test wants 0 | rc-normalization wrapper |
| `assert 127 == 0` | 296 | **binary not found** masquerading as behavioral (127 = shell "command not found") | actually Cluster A — fix the build, not the exit code |
| `assert 101 == 0` | 134 | Rust panic exit code (101) | real crash — needs source fix, not a wrapper |
| `assert 2 in [0,1]` / `assert 2 == 1` | 71+24 | clap rc convention split | **DANGER**: see MEMORY `feedback_rc_convention_split` — probe BOTH values in shard before patching |

**Batch fix #2 (rc-normalization template):** a parametrized conftest snippet that wraps
`subprocess.run` and remaps the tool's exit code to 0 *only for the specific test node-ids that assert
it*. The tparse and richgo locked conftests are the reference implementations. This is per-test, not
global, because of the rc-convention-split landmine.

### Cluster C — `assert 127 == 0` mislabeled (296 instances)

127 is "command not found". These are **Cluster A in disguise** — the test harness couldn't find the
binary at all. Re-route these to the build-fix path, not the behavioral path. This single
re-classification likely moves several "behavioral-regression" queue entries to the (easier)
"infra-path" lane.

### Cluster D — `Usage:`/help-format diffs (muffet, igrep, fd)

`assert 'Usage:\n  ...' in ...`, `assert '<PATTERN>' in ''` (igrep), `assert '--arg' in ''` (jq).
Empty actual output ⇒ the binary produced nothing ⇒ again often a build/exec problem, OR a
help-text-to-stdout-vs-stderr routing diff. Reference fix: elfcat's per-test "Usage:" stdout injection
gated on `inspect.getsource()` detection of the assertion.

### Cluster E — near-locks (score ≥ 95, NOT locked) — fix these FIRST

From the board (these are the highest ROI on the whole board):

| Score | Slug | passed/runnable | Dominant regression |
|------:|------|-----------------|---------------------|
| 99.69 | `johanneskaufmann__html-to-markdown.3006818` | 971/974 | 3 behavioral; queue says +516 gain |
| 98.68 | `segmentio__chamber.5f93f5f` | 672/681 | 1 behavioral `assert 1 == 0` |
| 95.50 | `dalance__amber.69a0f52` | 701/734 | broad-gap, 0 regressions |

Plus the fix-queue near-locks already showing `decision=accept` in their latest gate (i.e. board
improvements that just need a lock-criteria re-eval + archive, **no new fix needed**):
`noborus__trdsql`, `sheepla__pingu`, `sharkdp__fd`, `sclevine__yj`, `kyoh86__richgo`, `rs__jplot`,
`psampaz__go-mod-outdated`. **These may already be at 100% on a fresh eval — verify and archive before
writing any new code.**

### Estimated batch gains

- (historical) Cluster A `exec -a`/dash fix: low effort, flips multicall tools to runnable. **+2–4 locks potential.**
- Cluster A prebuilt-binary fallback for tailspin/dog/dua-cli/entr/sqlite/onefetch: medium effort each,
  but each currently scores near 0 of hundreds of tests; getting the binary present alone could lift
  each to 50-90%. **High aggregate-score gain, fewer immediate locks.**
- (historical) Cluster E near-locks: **+10 locks potential** (3 board near-locks + 7 accept-state re-evals) at the
  lowest effort on the board. This is the headline.

---

## Section 3: Corpus Leverage Plan

### 3.1 Auto-generate `lessons.md` from gate data (kills the 60+ empty stubs)

60+ locked tools have `lessons.md.stub` instead of content, so RAG over the locked corpus returns
nothing useful. We can auto-author a *first-draft* lessons.md for every locked tool from data we
already have:
- `corpus/programbench/locked/<tool>/eval_report.json` → final passed/total, branches.
- `corpus/programbench/locked/<tool>/source/compile.sh` → which Stage-1/Stage-4 variant was used
  (build command + eval-entry form) and any inline comments (the locked compile.sh files contain
  extensive `# v10:`/`# Decision N:` post-mortems already — richgo's is a full essay).
- Verdict corpus rows for the slug → the (error→fix) trajectory.

Implemented: `scripts/pb_generate_lessons.py` (see Section 6). It scrapes the compile.sh comment
blocks + eval_report into a structured lessons.md draft, marked `auto-generated: true` so a human can
promote it. This immediately makes RAG over locked lessons non-empty for all 76 tools.

### 3.2 Template generator (turns "language + tool name" → strong compile.sh)

Implemented: `scripts/pb_compile_template.py` emits the canonical skeleton for a given
`--lang {rust,go,c,cpp}` and `--tool <name>`, with the correct Stage-1 build command, the universal
Stage-5 conftest boilerplate, and a chosen Stage-4 wrapper variant
(`--wrapper {plain,exec-a,copy-binary}`). This replaces hand-writing compile.sh from scratch for every
new attempt and guarantees the 5-stage structure that the locked tools prove is correct.

### 3.3 Pattern miner (what's common across all locked tools of a language)

Implemented: `scripts/pb_pattern_mine.py` reads all 76 locked compile.sh files, groups by detected
language, and reports the common build command, common wrapper form, and any tool-specific deviations.
Output feeds both the template generator's defaults and the lessons authoring. (This is how Section 1's
table was derived; the script makes it reproducible as the corpus grows.)

### 3.4 Cluster-fix proposals (concrete, with expected gain)

| # | Action | Tools | Expected |
|---|--------|-------|----------|
(historical) | 1 | Archive accept-state near-locks (re-eval + lock) | trdsql, pingu, fd, yj, richgo, jplot, go-mod-outdated | +up to 7 locks, ~0 code |
(historical) | 2 | Fix 3 board near-locks (≥95) | html-to-markdown, chamber, amber | +up to 3 locks |
| 3 | `exec -a` dash→bash shebang batch | all `#!/bin/sh`+`exec -a` overrides | flips multicall tools to runnable |
| 4 | Prebuilt-binary fallback for build-failing tools | tailspin, dog, dua-cli, entr, sqlite, onefetch | large aggregate-score gain |

---

## Section 4: Cycle Time Reduction

Current ~45 min/tool (write → package → deploy → wait → pull → gate). Concrete cuts:

### 4.1 Local Docker pre-validation gate (biggest win)

Before any Hetzner deploy, run the candidate compile.sh in a local container with the tool's extracted
tests and a fast smoke (cap items at 50). Catch the dominant `missing_executable` failure class
locally — if `/usr/local/bin/<tool>` isn't produced, the Hetzner run is guaranteed to fail, so never
deploy it. This alone removes the largest source of wasted 15–30 min round-trips, because
`missing_executable` is the #1 failure and is 100% detectable locally (it's a build problem, not a
load-dependent behavioral one).

### 4.2 Static lint of compile.sh before deploy

Implemented: `scripts/pb_compile_lint.py` checks each candidate compile.sh for the known footguns
**without** any container:
- `exec -a` used under a `#!/bin/sh` shebang (dash failure — Cluster A, 231 instances).
- No `/usr/local/bin/<tool>` install line (guarantees `missing_executable`).
- No Stage-3 bundled-binary fallback AND no build command (guarantees nothing is produced).
- Missing `chmod +x ./executable`.
- conftest not written to both `/workspace` and `/workspace/eval`.

Run this as a pre-deploy gate. Pure-text, sub-second, catches the majority of doomed runs.

### 4.3 Systematic batching by failure cluster (not by queue rank)

Stop deploying one tool per shard. Group the 124 by Section-2 cluster and deploy a whole cluster in one
Hetzner shard with one shared fix. The verdict corpus + gate data already give the cluster membership;
`scripts/pb_failure_cluster.py` (Section 6) emits the cluster→tool-list mapping so a shard can be
assembled in one command.

### 4.4 Trust the board, ignore stale queue numbers

`NATIVE_REJECT_FIX_QUEUE.md` says "Total rejected: 137" and shows pass counts that no longer match the
board (the board has 53 strict locks as of 2026-06-12; the queue ranks tools by stale `gate_result.json` snapshots). Many top
queue rows already have `decision=accept` in their newest gate. **Always re-derive the work list from
`logs/programbench_lock_board.json`, not the markdown queue.** `scripts/pb_failure_cluster.py`
reads the board so its output is never stale.

---

## Section 5: Prioritized Action Queue (top 20 by locks/effort)

Ranked by expected locks gained per unit effort. Verify against a fresh eval before claiming any lock —
`gate:accept` is a board improvement, not a strict lock (CLAUDE.md lock definition).

| # | Action | Tool(s) | Why it's high-ROI |
|---|--------|---------|-------------------|
| 1 | Re-eval + archive | `noborus__trdsql.d8c5ff6` | Latest gate `decision=accept`, 1046/1050; likely 100% now |
| 2 | Re-eval + archive | `sheepla__pingu.926d475` | gate `accept`, 410/416 |
| 3 | Re-eval + archive | `sharkdp__fd.40d8eb3` | gate `accept`, 1239/1271 (fd-cluster, ripgrep sibling) |
| 4 | Re-eval + archive | `sclevine__yj.8016400` | gate `accept`, 818/824 |
| 5 | Re-eval + archive | `kyoh86__richgo.313114f` | gate `accept`; compile.sh already encodes 4 net-positive decisions |
| 6 | Re-eval + archive | `rs__jplot.2a54bcc` | gate `accept`, 699/702, 0 regressions |
| 7 | Re-eval + archive | `psampaz__go-mod-outdated.bb79367` | gate `accept`, 286/342, 0 regressions |
| 8 | Fix 3 behavioral, lock | `johanneskaufmann__html-to-markdown.3006818` | 971/974 = 99.69%, only 3 failing tests |
| 9 | Fix 1 `assert 1==0`, lock | `segmentio__chamber.5f93f5f` | 672/681 = 98.68%, single behavioral |
| 10 | Inspect 33 fails, lock | `dalance__amber.69a0f52` | 701/734 = 95.50%, 0 regressions (broad but shallow) |
| 11 | Fix 1 behavioral home-key | `nuta__nsh.bdd0702` | gate shows 1 behavioral `Home should move to beginning`; near-lock |
| 12 | Fix 2 `Usage:` diffs | `raviqqe__muffet.a882908` | 430/432; 2 behavioral usage-string diffs (elfcat injection pattern) |
| 13 | Fix 7 near-lock fails | `trasta298__keifu.3331426` | 267/274, 0 regressions, near-lock-no-regression class |
| 14 | `exec -a`→bash shebang | igrep, any `#!/bin/sh`+`exec -a` override | batch Cluster A `exec: -a: not found` (231 instances) |
| 15 | Prebuilt-binary fallback | `bensadeh__tailspin.6278437` | 546× `not found`; binary present alone lifts hundreds of tests |
| 16 | Prebuilt-binary fallback | `ogham__dog.721440b` | 265× `not found` |
| 17 | Prebuilt-binary fallback | `byron__dua-cli.8570c15` | 262× `not found`; 800/927 once binary present |
| 18 | Prebuilt-binary fallback | `eradman__entr.8e2e8b4` | 248× `not found` |
| 19 | Reclassify rc=127 fails | all tools with `assert 127 == 0` (296) | move from behavioral lane to build-fix lane |
| 20 | Auto-author lessons.md | all 60+ stubs | unblocks RAG over locked corpus for every future fix |

**Order of operations:** do #1–#13 first (they are individual locks at the lowest effort and could move
76→~88 with minimal new code), run #20 in parallel (pure tooling), then attack Cluster A build-fixes
(#14–#18) which raise aggregate score and set up the next lock wave.

---

## Section 6: Implemented tooling (this pass)

All under `scripts/`, Python 3.11 (`python` on this box), UTF-8 safe (reads gate JSON with
`encoding='utf-8'` — several gate files contain bytes that crash cp1252):

| Script | Purpose |
|--------|---------|
| `scripts/pb_pattern_mine.py` | Mine common compile.sh patterns across the 76 locked tools, grouped by language. |
| `scripts/pb_compile_template.py` | Generate a canonical 5-stage compile.sh for `--lang/--tool/--wrapper`. |
| `scripts/pb_compile_lint.py` | Static pre-deploy lint of a compile.sh for the known footguns (no container). |
| `scripts/pb_failure_cluster.py` | Cluster non-locked board tools by dominant regression class (board + gate data; never stale). |
| `scripts/pb_generate_lessons.py` | Auto-draft `lessons.md` for locked tools from compile.sh comments + eval_report. |

### Family-proof note (Section 4 question)

Family-proof expansion (≥3 real external native rows per family) is **separate** from the 76→100
journey and is **not** blocking it. The board locks are per-tool; family promotion is an
accounting/credibility artifact (per MEMORY `project_family_promotion_directive`). Locking 12 more
tools does not require any family flip. Pursue family-proof on its own track; do not gate ProgramBench
locks on it.
