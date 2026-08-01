# Morning Fix List — overnight drive findings (2026-06-18)

> Generated autonomously while the 37-tool Hetzner re-eval drive ran. **Honest headline:
> mechanical re-eval produced 0 NEW locks.** The tools that come back clean were already
> locked (e.g. code-minimap — its full-slug row is an alias dup of an already-official lock).
> Every genuinely-not-locked tool comes back as a NEAR-LOCK with an environment-class or
> source-level tail — none are version/format one-touch fixes. Those need real per-tool
> engineering and were deliberately NOT attempted blind overnight.

## Verified-fresh NEAR-LOCKS (not already locked under any slug) — by fix class

| tool | fresh % | gap | fix class | specific action |
|------|--------:|-----|-----------|-----------------|
| `ariga__atlas.6d81150` | 99.94% | 1 test | **CEILING CANDIDATE (strong, criterion-1)** | Built legitimately from Go source (261s). The 1 fail (`test_migrate_apply_revisions_schema`) needs `--revisions-schema` on SQLite; the real community build returns rc=1 with `"cannot store revisions-table in a separate schema with SQLite driver. You're running the community build... may differ from the official version."` = **official/closed-source-only feature absent from open-source code.** Meets the Legitimate-Ceiling-Standard criterion 1 (unprovisionable, real binary itself refuses with proof). Per the HARD PROCESS, before final cert: Opus-verify there's no legitimate sqlite-ATTACH workaround. Ceiling 3474/3476. Not chasing. |
| `rs__jplot.2a54bcc` | 99.9% | 3 TUI | likely ceiling | exact terminal escape-sequence asserts (`ClearScrollback`, ticker, ReportCellSize). Already flagged `submetric_claim`. Verify vs real jplot TUI output; probably genuine ceiling (2157/2160). |
| `quinn-rs__quinn.bb359cc` | 99.8% | 1 skip | verify ceiling | only skip = `test_client_connection_refused`. Check if upstream `@pytest.mark.skip` (→ certify 598/599 ceiling) or runtime-skip that's matchable (→ provide loopback refusal, un-skip, lock). Board said 7.8% — huge stale-board correction either way. |
| `hush-shell__hush.560c33a` | 99% | `results_read_failed` on branch 10c7b30aafc4 | **branch test-run crash** | UPDATED: NOT a binary hang — a clean from-source build runs `print.hsh` (`std.exit(0)`) and exits rc=0 immediately (verified in rust:slim, 22s build). Clean re-eval on idle box (CPUS=1, timeout=30) scored **99 with `results_read_failed` on branch 10c7b30aafc4**: that branch's pytest run dies before writing JUnit (one test crashes/OOMs the process, not a per-test hang). The overnight "rc-9 at 5s" was a *different, tight-timeout submission under load*. Needs: find which test in branch 10c7b30aafc4 kills the run. Not a clean lock yet. |
| `axodotdev__oranda.27d60c7` | 99.3% | 6 | env-MATCH | GitHub-API network tests + css env-override (`ORANDA_CSS`?) + 1 cmd timeout. Network tests need outbound or a recorded fixture; env-override is a real behavioral check. |
| `ducaale__xh.4a6e44f` | 98.7% | 15 | mixed (build+env) | (a) man-page tests (`test_generate_man_page`, `test_man_page_*`) — generate+embed the man page at build time. (b) `httpbin.org` status/redirect tests — live-network dependent (exit-code-per-status). Split: fix man-page in compile.sh; network tests need a stub server or are env. |
| `tarka__xcp.5e5b448` | 97.6% | 10 | ceiling/env | `--reflink=always` needs btrfs/xfs (Docker fs is ext4 → rc=1); `test_preserve_executable_permissions` 509 vs 493 = root-in-container makes files 0775 not 0755. fd-class ceilings — mostly genuine unless eval fs/uid is changed. |

## B_HARNESS_FIX lane (high not_run, behavioral already ~100% — env/fixture provisioning)

| tool | fresh % | gap | fix class | specific action |
|------|--------:|-----|-----------|-----------------|
| `stranger6667__jsonschema.d52e881` | 77.5% | 1101 not_run | **env-MATCH (data)** | 1059 `test_conformance` + 42 `test_cli` not_run. Behavioral 3806/3806 = 100% of what ran. The JSON-Schema-Test-Suite conformance corpus isn't provisioned in the build → those tests never collect. Provision the test-suite data dir in compile.sh → 1059 conformance tests run. Highest not_run-recovery on the board. |
| `stacked-git__stgit.430027d` | TIMEOUT | whole eval hangs | **source/harness** | stgit eval hangs >40min (load idle, frozen at 0%) → killed by per-tool timeout. Likely a blocking git op or interactive prompt during a test. Needs attended diagnosis (which test blocks); not safe to fix blind. |
| `jesseduffield__lazygit.1d0db51` | TIMEOUT | whole eval hangs | **TUI/harness** | same pattern as stgit — eval hangs >40min → timeout. lazygit is a TUI; a test likely waits on a pty/interactive frame. Needs a pty harness or per-test timeout; attended. (TUI tools as a class hang here — pipr/xplr/peco likely similar.) |

## D_FINICKY_TAIL lane (binary works, residual output-format mismatches)

| tool | fresh % | gap | fix class | specific action |
|------|--------:|-----|-----------|-----------------|
| `dandavison__delta.acd758f` | 98.2% | 42f | output-format (ANSI) | 35/42 are `test_grep`/`test_grep_gaps`: git-grep colorized output asserts exact ANSI codes (`48;5;28`, `32m1`, `\x1b[36m`). delta's grep colorization differs slightly. Match the exact ANSI sequences the real delta emits for git-grep. |
| `byron__dua-cli.8570c15` | 96.9% | 27f | output-format (size) | `test_harvest`/`test_aggregate`: byte-size formatting + dir aggregation (`4.00 KiB` vs `12.00 KiB`, empty-dir 0). Size-calc/format + apparent-vs-real block accounting. |
| `pls-rs__pls.4e1ae50` | 97.2% | 19f | output-format (align) | `test_symlinks`/`test_window_name`/`test_presentation`: unicode filename cell width, column alignment, sparse-file blocks. Terminal column-width math. |
| `elkowar__pipr.fae0b17` | TIMEOUT | hang | TUI/harness | TUI input previewer — eval hangs to 40min timeout (same TUI class as stgit/lazygit). |

> D-lane TUI tools `sayanarijit__xplr` and `peco__peco` were NOT completed — same TUI-hang
> class; deferred (re-eval needs a pty harness with per-test timeouts, not a full-eval timeout).

## Recipe-tools triage plan (the 71 NOT driven tonight)
Do NOT blind-eval them — most are D_FINICKY/E_REIMPL with the same tail class, and builds
can fail/waste compute. Instead, morning: `python scripts/determinex_xray.py --all <reports>
--tasks-dir C:/tmp/pb_tasks` then read `harness_flag` — only pursue rows that are
PREFIX_MISMATCH (rare, cheap) or NOT_RUN_SUPPRESSION with behavioral≈100% (env/data
provisioning). Skip BEHAVIORAL_GAP rows (those are reimpl projects, not quick locks).

## Broken pilot shims (IGNORE — real locks live in `corpus/programbench/locked/`)
- `oppiliappan__eva.41ae245` — pilot eval 42% (557 fails); eva is an archived lock. The `/root` pilot is a stale/experimental copy.
- `thezoraiz__ascii-image-converter.d05a757` — pilot eval 0/488 (all not_run); also an archived lock.
> Lesson banked: never source a re-eval submission from a random `/root` pilot dir — use the locked archive.

## Recommended morning order (highest expected value first)
1. **hush** — one source fix (EOF/non-tty handling) plausibly clears 16 results → full lock from a board-6.6% tool.
2. **quinn** — verify the single skip; likely a clean 598/599 ceiling certification (board 7.8% → certified near-lock) or a quick un-skip.
3. **atlas / jplot** — verify whether their 1–3 fails are genuine ceilings (build real binary, compare). If ceiling, certify; don't chase.
4. **xh man-page** — build-time man-page generation is a real compile.sh fix (the network tests are separate, env-gated).
5. **oranda / xcp** — env-MATCH (network fixture / fs+uid); larger lift, do last.

## What NOT to do
- Do not re-eval pilot shims expecting new locks — proven 0-yield.
- Do not auto-launch the 71 recipe tools blind — they're mostly D_FINICKY/E_REIMPL with the same tail class; build failures would waste compute. Triage them through xray first.
