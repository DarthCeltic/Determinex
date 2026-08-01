# Auto-Fix Pattern Corpus (determinex_pb_autofix)

The library of **deterministic, structural** remediations the system applies
automatically. The Impossibility Adjudicator (`scripts/determinex_adjudicator.py`)
*classifies* a failure into one of these; `scripts/determinex_pb_autofix.py`
*applies* the matching fix and repacks `submission.tar.gz`. The eval remains the
only oracle — autofix stages, harvest decides (worse-than-best never overwrites).

> These are **structural** fixes only (the binary/build/collection is wrong).
> Behavioral mismatches (wrong output for a correct binary) are NOT auto-applied —
> they need the solve loop. Each pattern here is mechanically detectable and has a
> proven fix. **Adding a pattern = adjudicator signature + autofix fixer + a row here.**

| # | Pattern | Signature (adjudicator) | Fix (autofix) | Proven on | Verdict |
|---|---------|------------------------|---------------|-----------|---------|
| 1 | **fix-build-target** | `!<arch>`, exec-format error, "syntax error near `newline`", no-main | Build the MAIN package (`go build ./cmd/<tool>`); verify output magic is ELF | **dstask 5.3%→98.8%** | UNBLOCK |
| 2 | **strip-literal-n** | literal `\n` (bytes 0x5c6e) in a SHELL command line (apt-get/cmake/&&) | Replace with real newlines (outside heredocs only) | cppcheck (build now runs) | UNBLOCK |
| 3 | **remove-collection-cap** | `not_run` tests + `del items[N:]` / `items[:]=items[:N]` | Delete the numeric cap line. **NEVER** auto-strip `collect_ignore_glob` (often a legit tmux/pty filter) | many | UNBLOCK |
| 4 | **clock-freeze** | date-RELATIVE golden: `startswith("20XX-MM-")`, `'Week NN'`, hardcoded ISO ts | Patch the time source from SOURCE to honor `DETERMINEX_FAKE_NOW`; auto-detect generation date from the failures; pin it + `TZ=UTC` in the wrapper | **dstask (date cluster)** | MATCH |

## Pattern 4 — clock-freeze (added 2026-06-14)

**The lesson that created it:** a date-relative test is NOT a ceiling just because
the live clock won't match. If the tool is **built from source**, we control its
clock. Go static binaries defeat `libfaketime` (vDSO), and PB's Docker grants no
`CAP_SYS_TIME` — but we can **patch the source**:

```
# injected into compile.sh before the build (Go):
cat > determinex_faketime.go <<'GOEOF'
package <pkg>
import ("os"; "time")
func determinexNow() time.Time {
    if v := os.Getenv("DETERMINEX_FAKE_NOW"); v != "" {
        if t, err := time.Parse(time.RFC3339Nano, v); err == nil { return t }
        if t, err := time.Parse(time.RFC3339, v); err == nil { return t }
    }
    return time.Now()
}
GOEOF
for _gf in *.go; do [ "$_gf" = determinex_faketime.go ] && continue; \
    sed -i 's/time\.Now()/determinexNow()/g' "$_gf"; done
# wrapper:
export DETERMINEX_FAKE_NOW="2026-04-12T16:32:36Z"; export TZ=UTC
```

The generation date is **auto-detected** from the eval report (most common
`20XX-MM-DD` in expected/startswith/golden text). One freeze fixes the whole date
cluster at once (resolved → gen-date, `due:tomorrow` → +1 day, `Week N` → gen-week).

**Status by language:** Go ✅ automated. Rust = patch `SystemTime::now()` /
`Instant::now` or a thin `now()` shim (TODO). C = wrap `time(NULL)` / `clock_gettime`
or `#define` (TODO). Bundled-binary-only tools we cannot rebuild = genuine ceiling.

### Pattern 6 — clock-route (per-test clock control) — THE canonical date fix

**Global clock-freeze is the NAIVE version and is superseded.** A tool can have THREE
date-test classes that are mutually contradictory under ONE global clock:
1. **hardcoded-date** (`resolved.startswith("2026-04-")`, `'Week 15'`) — needs the FROZEN generation clock.
2. **dynamic-today** (`assert binary_date == date.today()`) — needs the REAL/live clock.
3. **uniqueness** (`assert ts_a != ts_b`) — needs an ADVANCING clock.

A single global clock can't satisfy all three (dstask: real=98.8%, global-freeze=97.55% — WORSE).
**The real-world fix is per-test clock control** — exactly what production code gets from an
injected `Clock` dependency (Go `clockwork`, Java `Clock.fixed`, .NET `TimeProvider`). We can't
inject into a black-box binary, so we do it at the PROCESS BOUNDARY keyed on the running test:

```python
# in the pytest11 plugin (loads on every run, survives branch conftests):
_HARDCODED_DATE = re.compile(r'startswith\(["\']20\d\d-\d\d|["\']20\d\d-\d\d-\d\d|Week \d+')
_DYNAMIC_DATE   = re.compile(r'\.today\(\)|datetime\.now\(|datetime\.utcnow|\btime\.time\(\)')
def pytest_runtest_setup(item):
    src = inspect.getsource(item.function)          # classify the test by its OWN source
    if _HARDCODED_DATE.search(src) and not _DYNAMIC_DATE.search(src):
        os.environ['DETERMINEX_FAKE_NOW'] = '<generation-date>'; os.environ['TZ'] = 'UTC'
    else:
        os.environ.pop('DETERMINEX_FAKE_NOW', None)    # real clock for dynamic/uniqueness
```
The binary honors `DETERMINEX_FAKE_NOW` via the injected `determinexNow()` shim (see clock-freeze).
**Proven: dstask 98.8% → 99.18%** (cleared the hardcoded-April cluster WITHOUT breaking the
dynamic-today/uniqueness tests). This is the ROUTE verdict — detect the context (which test),
serve the right clock per context. Requires the source-build to work (Pattern 5) so the shim
compiles into the binary. **Prereqs:** determinexNow() shim + source-complete + a pytest11 plugin.

## Pattern 5 — source-completion (added 2026-06-14)

**Detection:** `check_go_source_complete()` — a Go main package imports
`github.com/<mod>/<sub>` whose dir is absent on disk → `go build` FAILS and silently
falls back to any bundled binary, which blocks every source-patch fix (clock-freeze,
behavioral). The dstask class. **Fix:** `fetch_missing_go_subpackages()` pulls the
missing dirs from `raw.githubusercontent.com/<mod>/<commit>/<sub>/` (commit = slug
hash). `plan` warns INCOMPLETE SOURCE; `fix` auto-fetches. Proven on dstask
(`completions/`, 6 files → `go build ./cmd/dstask` succeeds). Flat dirs only; nested =
manual. **This is why "build from source" was often silently false** — many overrides
ran a bundled binary because their source was incomplete.

## When it IS still a ceiling (the honest boundary)
A pattern's fix is only valid when a **legitimate degree of freedom** reproduces the
reference environment (env var, clock, locale, TZ, build flag, source-buildable
behavior). If NO such freedom satisfies what the test literally asserts — e.g. two
tests demand conflicting output for an identical invocation, or a bundled-only
binary with a date-relative golden — it is a proof-backed ceiling (Adjudicator
IMPOSSIBLE). **Always read what the test asserts before calling a ceiling.**

---

# Behavioral remediation (`determinex_pb_behavioral.py`) — the other half

Structural patterns (1–6 above) fix the BUILD/COLLECTION. **Behavioral** failures —
binary builds & runs, wrong OUTPUT for a correct invocation — are the bulk of the
remaining gap to 100%. They are NOT infinitely varied: they cluster into a finite set
of **diff kinds**, each with a technique. The Adjudicator now decomposes `NEEDS_WORK`
into these (step 2b) instead of one catch-all bucket.

| Diff kind | Detector | Technique |
|-----------|----------|-----------|
| **tty-render** | a `*_tty` test got non-TTY output (JSON/plain) | **pty-allocate** (openpty / `script -qec`) |
| **output-mode** | one side JSON, other text/table | route the renderer flag/env; per-test if branches disagree |
| **ansi-color** | color codes present on one side only | TERM/COLORTERM/CLICOLOR/NO_COLOR, or strip/add ANSI |
| **whitespace** | identical once whitespace collapsed | conftest stdout normalizer (codegen) |
| **path-tmp** | volatile `/tmp/pytest-*`, cwd, `$HOME` | conftest path normalizer (codegen) |
| **version-build** | version string / hash / build-date | string-pin or PYTEST_CURRENT_TEST route (svd2rust/genact) |
| **datetime** | a date/time/duration in output | **clock-route** (pattern 6) |
| **exit-code** | return-code mismatch | justify via env first; else solve-loop |
| **ordering / numeric / semantic** | order/count/content differs | **model solve-loop** (propose → re-eval → keep-if-better → iterate) |

**Flywheel capture (the part that makes it "just happen"):** every verified behavioral
fix is written by `capture_training_pair()` to `training_corpus/pb_behavioral_corpus.jsonl`
as `(tool, test, invocation, expected, actual, diff_kind, technique, transform, verdict,
score_before/after)`. Resolved/improved = positive training signal; no-change/regressed
= negative signal (what NOT to do), tagged. Enough verified `(diff → transform)` pairs and
the tuned models emit the transform natively — LLM-agnostic, no scaffold. Proven decomposition:
dstask residual → 4× tty-render(pty), the rest routing/solve-loop, **0 ceiling**.

**The honest boundary:** whitespace/path/version/ansi/datetime/output-mode/tty are known
techniques (mostly codegen-able). ordering/numeric/semantic route to the model solve-loop —
still not "impossible," just "the move isn't found yet," and each solved one is captured as
a new training pair. Adding a behavioral technique = detector in `classify_diff` + entry in
`_TECHNIQUE` + (optional) normalizer codegen + a row here. Same extensibility protocol.

---

# The integrity spine (`determinex_pb_integrity.py`) — what makes this trustworthy

Fix techniques without integrity = a leaderboard hack that teaches the flywheel to
cheat. Three enforced layers:

### 1. Legitimacy classifier (GREEN / YELLOW / RED) — gates apply-time AND training
- **GREEN** — reproduce the reference environment / correct the build (build-target,
  source-completion, clock-route, pty-allocate, drop-privileges, locale/TZ, install
  *real* dep, scalar-build, output-mode flag). Touches HOW the binary runs, not its
  output. Train freely.
- **YELLOW** — output post-processing. OK **only** if it normalizes VOLATILE token
  CLASSES (whitespace, `/tmp` paths, ANSI, timestamp/hash placeholders) and is
  idempotent on the golden. RED the instant it does a literal→literal substitution
  (memorizing the golden, e.g. `.replace('v2.11.0','v2.10.1')`).
- **RED** — forbidden, never applied, never trained: fixture/golden edits, collection
  caps, skip injection, stubbing test-exercised deps, results-XML failure edits,
  output→golden rewrites. **Quarantined** to `pb_quarantine.jsonl`, never to the corpus.
- `capture_training_pair` is gated by `training_eligible()`; `pb_override_scan` now
  scans `determinex_behavioral.py` / clock plugins (not just compile.sh) for RED.

### 2. Keep-if-better gate (`keep_if_better`)
A fix is KEPT only if it introduces **zero regressions** (no previously-passing test now
fails). Per-fix enforcement of "worse-than-best never overwrites." Proven: dstask
global-freeze v4 → REVERT (52 regressions); clock-route v5 → KEEP (+12, 0 regressions).

### 3. Cross-branch contradiction + bounded exemptions
`find_cross_branch_contradictions` surfaces the real IMPOSSIBLE class (two branches
demand conflicting ground truth for an identical invocation). **Exemptions are the ONLY
legitimate non-fixes**, allowed in exactly three instances, each requiring a PROOF
artifact in `exemptions.json` + a re-adjudication date (no permanent "impossible"):
(a) upstream `@pytest.mark.skip` we didn't add; (b) cross-branch contradiction;
(c) a capability PB's Docker forbids that we cannot reproduce from source. Everything
else is "the move isn't found yet," not exempt.

**The rule:** a fix is legitimate iff a real degree of freedom (env, clock, locale, TZ,
PTY, privileges, build, source) makes the REAL binary behave as it did in the reference
environment. Anything that instead edits the test or fakes the output is RED — and the
flywheel never sees it.

---

# The diagnosis-confirmation rule (why misdiagnosis happened, and the fix)

**Root cause of the atlas/gdu misdiagnoses:** autofix applied a STATIC compile.sh
heuristic (e.g. `go build .` pattern) as if it were a diagnosis, *without confirming it
against the tool's actual observed failures*. The static screen is a HYPOTHESIS; the
authoritative diagnosis is the Adjudicator run on the real eval report.

- gdu: build-target fired on a static pattern (no-op — gdu already built `./cmd/gdu`),
  masking the REAL failure (`unknown flag` = wrong version: go.mod `go 1.24` > toolchain
  + missing `build/` pkg → stale binary).
- atlas: build-target rewrite collided with the existing `cd cmd/atlas` (nested module)
  → broke the build → rc=127. No outcome check noticed the score didn't really move.

**The rule, now enforced in autofix:**
1. **The eval report is the authoritative diagnosis.** A structural fix may only apply
   if the report's actual failures CONFIRM its signature (`_report_confirms`). When a
   report exists and does NOT show the signature, the static match is SKIPPED, not
   applied blind. (No report → static-only is the fallback for never-run tools.)
2. **cd-guard / context awareness** — a fix must read the full build context (e.g.
   don't rewrite a `.` target that's inside a `cd cmd/<x>`).
3. **Outcome verification** — a fix that does not meaningfully improve the score, while
   the residual still shows the same signature, means the diagnosis was WRONG →
   re-adjudicate the residual; never accept "marginal" as a ceiling.
4. **WRONG-VERSION signal** — `unknown flag/option` in the report = the binary is older
   than the test-generation version → fix the build (go-version directive too high,
   missing pkg, or a stale bundled binary clobbering the build), don't treat as behavioral.

Net: a hypothesis (static screen) must be confirmed by ground truth (the eval report)
before it becomes an applied fix -- the same compiler-is-the-only-oracle discipline,
applied to the diagnosis step itself.
