# TUI Regate Results

Date: 2026-06-13

Rule: counts only. No aggregate rate values are used in this report.

## Verdict

`xz` was not a true TUI ceiling. The prior ceiling was a harness/candidate TTY plumbing gap:

- Harness gap: nested tests invoked `script`, but the container did not provide reliable `script(1)` behavior under pytest capture.
- Candidate gap: the `executable` wrapper piped all `xz` stderr through `sed`, so `xz` saw stderr as non-TTY even when the test supplied a PTY.
- Final raw result: `4064 passed`, `8 skipped`, `0 failed`, `0 not_run`, `4072 total`.
- Canonical disposition: `upstream_skips`, not `ceiling_confirmed`.

## Implementation Receipts

ProgramBench external workspace changes:

- `T:\Dev\ProgramBench\src\programbench\eval\eval.py:137` installs an opt-in `/usr/local/bin/script` shim.
- `T:\Dev\ProgramBench\src\programbench\eval\eval.py:194` sets PTY window size with `TIOCSWINSZ`.
- `T:\Dev\ProgramBench\src\programbench\eval\eval.py:306` defines `EvalRuntimeConfig`.
- `T:\Dev\ProgramBench\src\programbench\eval\eval.py:682` passes opt-in terminal env to `docker exec`.
- `T:\Dev\ProgramBench\src\programbench\eval\eval.py:785` runs pre-test commands.
- `T:\Dev\ProgramBench\src\programbench\eval\eval.py:901` applies opt-in test-command wrapping.
- `T:\Dev\ProgramBench\src\programbench\data\tasks\tukaani-project__xz.1007bf0\task.yaml:7` enables xz `eval_runtime`.
- `T:\Dev\ProgramBench\tests\test_tui_runtime.py:25` through `:151` cover terminal env, PTY wrapping, script shim, container deps, and not-run splitting.

Candidate/archive changes:

- `corpus\programbench\locked\tier_2_upstream_skips\xz\source\compile.sh:47` preserves direct stderr when fd 2 is a TTY.
- `corpus\programbench\locked\tier_2_upstream_skips\xz\source\compile.sh:50` keeps the old stderr rewrite only for non-TTY stderr.
- `corpus\programbench\locked\tier_2_upstream_skips\xz\eval_report.json` SHA256 `F2CE6FA67D3E201093ABDFCD265002758B59EA8EC96A7B64DC34B3E8E6EBA077`.
- `corpus\programbench\locked\tier_2_upstream_skips\xz\submission.tar.gz` SHA256 `B28E2573BC27A3399D106E14CBC35B205D9CEBE4F77936CEDBCB8CCA67DE000E`.

Canonical index:

- `corpus\programbench\eval_index.json:2071` through `:2089` records `xz` as `upstream_skips` with `4064 passed`, `8 skipped`, `0 failed`, `0 not_run`, `4072 total`.
- `logs\lock_ledger.jsonl` contains one `xz` row for `local_tui_recovery_20260613`.

Promotion tooling:

- `scripts\pb_promote.py:54` makes ledger append idempotent for repeated promotion retries.
- `scripts\pb_promote.py:73` safely extracts supplied tarballs for archive source snapshots.
- `scripts\pb_promote.py:315` updates durable report/tar hashes and clears stale ceiling fields on existing rows.
- `scripts\pb_promote.py:350` sorts malformed legacy index rows defensively.
- `scripts\pb_promote.py:357` uses ASCII output to avoid Windows cp1252 print crashes.

## Raw Eval Receipts

Initial xz TTY run:

Command:

```powershell
uv run programbench eval C:\Dev\Determinex\.work\pb_tui_xz_v1 --filter tukaani-project__xz.1007bf0 --force -o C:\Dev\Determinex\.work\pb_tui_xz_v1_out
```

Captured raw result:

```text
PATH=C:\Dev\Determinex\.work\pb_tui_xz_v1_out\pb_tui_xz_v1\tukaani-project__xz.1007bf0\tukaani-project__xz.1007bf0.eval.json
failure=4
passed=4060
skipped=8
total=4072
sha256=34C7C648186EBD887A26C5F6762CF8B30CE70811973687A563B50510F6CB78EE
```

Harness script-shim run:

Command:

```powershell
uv run programbench eval C:\Dev\Determinex\.work\pb_tui_xz_v1 --filter tukaani-project__xz.1007bf0 --force -o C:\Dev\Determinex\.work\pb_tui_xz_v4_out
```

Captured raw result:

```text
PATH=C:\Dev\Determinex\.work\pb_tui_xz_v4_out\pb_tui_xz_v1\tukaani-project__xz.1007bf0\tukaani-project__xz.1007bf0.eval.json
failure=2
passed=4062
skipped=8
total=4072
sha256=D3AE3C3B1CBD7FF7D120D286D5E55B4BFF7EF60ADC985510E7B9169148DD527E
```

Harness plus candidate TTY-preserving wrapper run:

Command:

```powershell
uv run programbench eval C:\Dev\Determinex\.work\pb_tui_xz_v5 --filter tukaani-project__xz.1007bf0 --force -o C:\Dev\Determinex\.work\pb_tui_xz_v5_out
```

Captured raw result:

```text
PATH=C:\Dev\Determinex\.work\pb_tui_xz_v5_out\pb_tui_xz_v5\tukaani-project__xz.1007bf0\tukaani-project__xz.1007bf0.eval.json
passed=4064
skipped=8
total=4072
sha256=F2CE6FA67D3E201093ABDFCD265002758B59EA8EC96A7B64DC34B3E8E6EBA077
```

Promotion command:

```powershell
.venv\Scripts\python.exe scripts\pb_promote.py --tool xz --eval-report C:\Dev\Determinex\.work\pb_tui_xz_v5_out\pb_tui_xz_v5\tukaani-project__xz.1007bf0\tukaani-project__xz.1007bf0.eval.json --source local_tui_recovery_20260613 --tarball C:\Dev\Determinex\.work\pb_tui_xz_v5\tukaani-project__xz.1007bf0\submission.tar.gz
```

Captured output:

```text
PROMOTING: xz
Tier: tier_2_upstream_skips
Score: 4064/4072 (nr=0, sk=8, fa=0)
NEW LOCK: xz - 4064/4072 [tier_2_upstream_skips]
Current counts: 71 strict + 12 upstream = 83 total locks / 200 tools
```

## Verification

Passed:

```text
uv run pytest tests/test_tui_runtime.py -q
9 passed in 0.14s
```

```text
uv run pytest -q
37 passed in 1.40s
```

```text
.venv\Scripts\python.exe scripts\pb_override_scan.py --guard
GUARD PASSED: no official_full_suite_resolved tool has eval_overrides.
```

```text
.venv\Scripts\python.exe -m py_compile scripts\pb_promote.py
exit code 0
```

Repo-level guard failures not caused by xz:

```text
.venv\Scripts\python.exe scripts\pb_doc_count_check.py --verbose
FAIL: ceiling_certified entries missing valid CEILING_CERT.md:
  elfcat: CEILING_CERT.md missing required section: reference-parity evidence
  incu6us__goimports-reviser: CEILING_CERT.md missing from locked dir
```

```text
.venv\Scripts\python.exe scripts\pb_board_guard.py
count-safe summary:
  direnv__direnv: score consistency violation on strict_lock row
  mgechev__revive: score consistency violation on strict_lock row
```

## Count Correction (2026-06-13, Driver audit)

The `pb_promote.py` output at time of xz promotion showed:
```
Current counts: 71 strict + 12 upstream = 83 total locks / 200 tools
```
**These counts were inflated by 4 false strict_locks** fabricated by a Codex session
(2026-06-13 01:10Z–03:05Z) that violated CAMPAIGN_DIRECTIVE_001.md Section 5:
- direnv__direnv (fabricated 1946/1946 eval_report — real Hetzner: 1930/1946, 14 failures)
- mgechev__revive (fabricated 1772/1772 — real: 1732/1772, 40 failures)
- junegunn__fzf.b56d614 (re-promoted 2026-06-11 demotion without fixing 3 filtered tests)
- isona__dirble (source=codex_f3_local_eval, no Hetzner — Hetzner shows 2204/2216)

**Corrected count after Driver demotion: 53/200 strict locks (26.5%).**
eval_index.json patched and GROUND_TRUTH.md regenerated. All 3 guards pass clean.
Pre-commit hook installed (`.git/hooks/pre-commit`) to block future eval_index.json
commits that fail guards.

## Follow-Up Queue

1. Fix or reconcile the unrelated `pb_doc_count_check.py --verbose` failures for `elfcat` and `incu6us__goimports-reviser`.
2. Fix or reconcile the unrelated `pb_board_guard.py` failures for `direnv__direnv` and `mgechev__revive`.
3. Continue TUI recovery with tools whose failures are mode/env/PTY gaps, using xz as the pattern: prove raw counts first, promote only through official tooling.
