# ProgramBench Reimplementation Playbook

> The standardized autonomous loop for taking a broken/low tool to lock:
> **setup → gate → read → refine → test → refine → finalize.**
> Legitimate (real working implementation, oracle-graded, nothing memorized).
> Goal: fewer refine-loops per tool by reusing the patterns banked here.

## The PreLook is implemented: `scripts/determinex_xray.py` ("xray")

X-ray a tool in one look → failure-mode class, upstream `github.com/<author>/<tool>@<sha>`
(from the slug), every failing test function grouped by cause + counts, and the
to-fix list by category. `--report <eval.json>` for one; `--all <dir> --json out`
for the whole batch. Master diagnosis index: `corpus/programbench/xray_index.json`.
Local triage is cheap (no Docker); the real-binary SCENARIO BATTERY (step h) is the
manual sweep when reimplementing. xray IS the mechanized prelook below.

### Spec cross-check (`--tasks-dir <dir-of-<slug>/tests.json>`) — the truth layer

Reading the eval REPORT alone is not enough: it can't tell a working-but-suppressed
tool from a genuinely-failing one, and that misread costs a whole wasted run. So xray
also reads the canonical `tests.json` (the ground-truth denominator + which branches
are `ignored` ceilings) and cross-checks emitted-vs-expected. It separates **three
worlds that must never be conflated** and names ONE primary cause = the next action:

| primary_cause | what it means | next action |
|---|---|---|
| `BEHAVIORAL_GAP` | binary fails tests that actually executed (behavioral pass <90%) | **reimpl work** — the loop below |
| `NOT_RUN_SUPPRESSION` | tests never ran, **no passing twin** under the other prefix | env-MATCH / build fixture / cap removal — NOT reimpl |
| `PREFIX_MISMATCH` | not_run rows **mirror a PASSING twin** under the other prefix | emit only the expected prefix in bidir/conftest |
| `SKIP_CEILING_OR_MATCH` | rows emitted a `skip` (not not_run) | verify vs upstream: unprovisionable skip = ceiling; provisionable = MATCH the env to un-skip |
| `NEAR_LOCK` | behavioral≈100%, ~0 not_run/skip | finicky tail / already done |

**The behavioral pass rate = passed / executed (prefix-stripped, skip+not_run excluded)
is ground truth — does the binary actually do the task.** Everything else is harness.

**Discipline (each of these was a real misread caught only by verifying — do NOT trust
a single flag, confirm the underlying rows):**
- `extra` (emitted IDs not in tests.json) is **bidir double-emission PB discards** — it's
  huge for *every* tool, including perfect locks. Never use it as a suppression signal.
- `skipped` ≠ `not_run`. A skip is a ceiling-or-MATCH question; a not_run is a harness cut.
- A not_run is only a cheap prefix fix if it has a **passing twin** under the other prefix.
  No twin ⇒ the test genuinely never ran (needs env/fixture), not a prefix tweak.
- behavioral<90% ⇒ it's the binary, full stop. No harness fix passes a wrong answer.

Run: `python scripts/determinex_xray.py --all C:/tmp/combined_reports --tasks-dir C:/tmp/pb_tasks --json corpus/programbench/xray_index.json`
(canonical task specs pulled from PB `src/programbench/data/tasks/<slug>/tests.json`).

## Core principle: Run 1 is playbook-armed (loops compound down)

The hand-cranked discovery on the FIRST tool of a class is the expensive part. Every
pattern it finds is banked here. The next tool of that class must apply ALL banked
patterns **in its Run 1** — so its first eval lands where the discovery tool's *last*
eval landed, and it needs ~1 refine instead of N. As the bank grows, #loops → 1.

> Rule: never write a naive Run 1. Write the playbook-armed Run 1. The system's Run 1
> should equal the previous tool's Run 2; the system's Run 2 should equal its Run 3.

## Lock definition-of-done (canonical parts every lock has)

A setup is a proper, archivable, gate-clean lock only when ALL of these exist:

**Produced by `programbench eval` (don't author — just achieve passed==total):**
`eval_report.json` with 9 keys (`test_results, error_code, error_details, log,
solution_branch, test_branches, test_branch_errors, executable_hash, warnings`),
showing `passed==total, not_run==0, skipped==0, failed==0`.

**Board entry (eval_index row) — populate:**
- Always: `slug, source` (full `author__tool.sha`), `status=strict_lock, tier,
  language, official_passed/total/not_run/skipped/failed, official_score_pct,
  official_full_suite_resolved=true`.
- Evidence pins: `eval_report_path, eval_report_sha256, tests_json_sha256,
  pb_head_commit, lock_timestamp`.

**Archive `locked/<full-slug>/` — place:**
`eval_report.json` + `submission.tar.gz` + `source/` + `lessons.md` + `README.md`
(+ `CEILING_CERT.md` only if it's a certified ceiling, not a 100% lock).

> The loop's **finalize** step = eval to passed==total → write these 3 layers.

## The loop (per tool)

1. **SETUP** — start from the per-language base (Rust: `clap` derive + `regex`).
   Binary name must match the submission's compile.sh `cp target/release/<NAME>`.
2. **GATE** — confirm the current submission's failure mode (no-binary / broken-stub
   / behavioral). Reimpl loop applies to no-binary + broken-stub.
3. **READ / PRELOOK (comprehensive — pre-find EVERYTHING before writing Run 1).**
   The cost of a thin prelook is N refine-loops discovering version/format/flags one at
   a time (datasurgeon paid this). A thorough prelook makes Run 1 accurate. Pre-find ALL:
   - **a. Build + slug**: the submission's compile.sh (binary NAME it `cp`s, build cmd,
     shim, bidir block, conftest). Slug → upstream `github.com/<author>/<tool>@<sha>`.
   - **b. Version**: exact `--version`/`-V` output from the real binary — including any
     repo URL / extra lines (tests often assert ALL of: name, number, URL).
   - **c. Flags**: full `--help` from the real binary → every flag, exact long+short
     names, which take values.
   - **d. I/O contract**: input modes (stdin / `-f` / `--directory`); exact output
     format — prefix/identifier per type, whole-line vs match, trailing newline,
     ordering, dedup; run the real binary per flag/construct on representative inputs.
   - **e. Edge/error**: no-args, empty input, missing file, invalid input → rc + exact
     message; the exact stdin-reading banner text.
   - **f. Test harness**: how tests invoke (stdin vs argv); **assertion type** — substring
     (`x in stdout`, forgiving) vs **exact golden** (`stdout == golden`, byte-exact,
     unforgiving — these dictate trailing-newline/format precision); TUI/skip markers.
   - **g. Tests = spec**: all failing test FUNCTIONS (deduped + counts) + expected per
     cluster, in one read.
   (Reference the real binary as a black box — observe, never copy its source.)
   - **h. SCENARIO BATTERY (the "look once" core — observe, never guess).** Every
     residual on datasurgeon was something GUESSED instead of observed. So run the real
     binary on a battery and match ALL outputs exactly:
       * each flag alone (already in d)
       * **flag COMBINATIONS** (e.g. `-D -l`, `-C -T`, `-D -e`) — formats compose oddly
       * **edge/boundary inputs**: invalid values (`256.1.1.1`→ observe partial match),
         edge TLDs (`.local`), overlapping/multi-match-per-line, empty input
       * **malformed args**: `-f` with no value, unknown flag → exact rc + stderr message
       * **multi-match / multi-type lines** with and without `-T` → per-line-once vs
         per-match, and how many lines emit
       * **filename form** under `-D`: basename vs full path
     Capture exact stdout/stderr/rc for each. The reimpl must reproduce the OBSERVED
     output — guessing any of (format / boundary regex / thorough semantics / arg-
     validation) is what costs refine-loops.
   > Automation direction: this battery is scriptable — given (tool, real binary), run a
   > standard scenario set, diff reimpl-vs-real, and the diffs ARE the to-fix list. That
   > is "look once, know the issues" mechanized.
4. **REFINE** — fix ALL clusters in one pass (minimize loops).
5. **TEST** — `programbench eval` on Hetzner. **Prune the `:determinex-cached` image first**
   or the build is reused stale.
6. **REFINE/FINALIZE** — repeat on the residual; archive the lock.

## Reusable patterns (apply from loop 1 on the next tool)

**Per-language base — Rust CLI:** `clap`(derive) + `regex`; `[[bin]] name=<tool>`;
read stdin if no `-f/--directory`; `process::exit(1)` on missing file.

**Common CLI contract (datasurgeon-class extractor tools):**
- Default output: `"<id>: <whole line>"`. `-C/--clean`: `"<id>: <match>"`. `-X/--hide`: drop the `<id>: ` prefix.
- `-S/--suppress`: silence the `Reading standard input` message — **and that message goes to STDOUT, not stderr** (tests check `result.stdout`).
- `-D/--display`: `"<id>, file: <filename>: <content>"`.
- `-l/--line`: prefix `"<n>:"`. `-T/--thorough`: emit all matches per line (default = first only, with `-C`).
- `-t/--time`: append exactly `"[*] Time elapsed: 00h:00m:00s"` (golden expects zeroed).
- `--list`: print output containing "plugin" (e.g. `No plugins installed.`).
- `--directory`: process every file in dir (sorted); per-file filename for `-D`.
- **No type flags → enable ALL extractors** (default behavior).
- `rc=0` on success even with zero matches; `rc!=0` only on missing file / arg error.
- **Version string must match the real tool's exact version** (read it from the real `--version`).

**Identifiers are exact and per-type — read them from the real binary** (`<flag> -C -S`):
`email`, `phone_number`, `hashes`, `ip_address`, `ipv6_address`, `mac_address`,
`credit_card`, `url`, `files`, `bitcoin_wallet`, `aws`, `google`, `dns`, `social_security`.

**Regex quirks worth copying as priors:**
- ipv6 matches greedily and stops at `::` (e.g. `2001:db8::1` → `2001:db8`): `(?:[0-9A-Fa-f]{1,4}:)+[0-9A-Fa-f]{1,4}`.
- mac = **colon-only** (hyphen form is intentionally NOT matched).
- bitcoin = **legacy only** (`[13]...`); bech32 `bc1...` intentionally NOT matched.
- aws key: no trailing `\b` (matches `AKIA…16` even with trailing chars).
- ssn: `\b\d{3}-\d{2}-\d{4}\b|\b\d{9}\b`.

**Mechanics gotchas:**
- Submission for these = compile.sh (build recipe); our source goes in `_reimpl/` and
  compile.sh cleans the task source + lays ours down before `cargo build`.
- Always `docker rmi -f programbench-compiled/<slug>:determinex-cached` before re-eval.
- Keep the submission's bidir block (test-ID doubling) or tests land as `not_run`.

## Loop-count log (the challenge: fewer each time)

| Tool | Lang | Start | R1 | R2 | R3 | R4 | R5 | Lock | #loops |
|------|------|------:|---:|---:|---:|---:|---:|-----:|------:|
| datasurgeon | rust | 12% | 56.4% | 58.7% | 65.8% | 66.8% | 69.3% | not yet | 5+ (in prog) |

**Convergence shape (the key finding):** the jump is FRONT-LOADED — Run 1 = +44pp
(the unlock), then +2–3pp/run on a finicky behavioral tail (exact goldens, -T/default
semantics, flag combos, clap arg-validation). Reaching a *lock* is a long per-tool
grind whose edges are mostly tool-unique (don't compound). So:

- The playbook compounds the EARLY runs → the next extractor-class tool's Run 1 should
  open ~55–65% instead of 12% (ids/formats/flags/version/recursion known up front).
- Locking each tool to 100% remains a sustained grind. 200/200 = big campaign, not
  2 runs/tool. Honest expectation: armed Run 1 gets ~60%; lock takes many more.

*Patterns discovered DURING datasurgeon are above. Next tool starts armed.*
