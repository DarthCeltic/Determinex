# HANDOFF — Official-Metric Correction, bidir-mirror Strip & Near-Lock Re-eval Campaign (2026-06-24)

## TL;DR — the honest state
- **Official lock count is still 65/200 = 32.5%.** No new clean (gap=0) lock landed this session.
- **The big durable win is a MEASUREMENT correction**: we were scoring with raw `passed/total`, which **understated every tool**. The official metric is `programbench info` = `EvaluationResult.for_branches(get_active_branches).without_ignored(get_ignored_tests)` → `TRUE-LOCK = n_resolved == len`. Use this ALWAYS, never raw.
- **The local eval harness was lying** because of a **double-bidir bug** (conftest mirror + pip plugin) that fabricated failing tests → local scores diverged from Hetzner. Fixed corpus-wide (210 tools).
- **23 near-locks were re-eval'd accurately**: confirmed at 99.5–99.9% official, but **every one has a real structural/deep tail** (skips, output-mismatches, root-perm, PB branch-crashes, local divergence). None is a free lock.

---

## DURABLE WINS THIS SESSION (committed + pushed, branch `mojibake-and-count-fix`)

1. **Official-metric tooling** (`official_metric_vs_raw_2026_06_23` in build_knowledge). To score: stage `run_dir/<iid>/<iid>.eval.json`, then `cd T:/Dev/ProgramBench && uv run programbench info <run_dir>`. Programmatic: `EvaluationResult.model_validate_json(...).for_branches(get_active_branches(inst)).without_ignored(get_ignored_tests(inst))`, count `passed` vs `len`. **NOTE: requires the PB uv env — can't import programbench from plain python.**

2. **bidir-MIRROR strip (210 tools)** — `scripts/determinex_pb_strip_conftest_mirror.py`. The legacy conftest `_bidir_inject_classnames` + `_cb_mirror` blocks ran ALONGSIDE the `/opt/determinex_bidir` pip plugin = double bidir = fabricated failing testcases. melody proved it: local 2642/2771 (gap129) vs Hetzner factory_v1 2652/2653 (gap1), **same binary**. Strip removed the mirror, kept collect_ignore/modifyitems/pip-plugin. (`conftest_bidir_mirror_inflation_2026_06_23`.)

3. **PTY anti-hang (13 TUI tools)** — `determinex_pb_pty.inject_pty`. pytest `--timeout` (SIGALRM main-thread) CANNOT break a subprocess blocked on a C-level read. The plugin injects a `waitpid`-based hard timeout into `subprocess.run`/`Popen.communicate` → hanging TUI test → clean timeout-failure, eval COMPLETES. Applied to json-tui/walk/pipr/tui-journal/hush/pls/dstask/oha/delta/hashcards + **ov/felix/xq** (added when ov hung the campaign). Load-order-robust guard (`isinstance(_pt_orig_popen, type)`) prevents the Popen-subclass crash.

4. **Whale masteries (official)**: **tinycc 4035/4040 (100)**, **ctags 4769/4837 (99)**, **luajit 6054/6160 (98)**. Built via: tinycc=CRLF-strip+bash-configure+tcc→tinycc; ctags=autotools+libs+chmod-packcc/misc; luajit=argv0-preserve+make-install+bash (vmdef wall remains). All near-lock ceilings, not clean locks.

5. **Corpus deepened**: `buildfail_whale_taxonomy_2026_06_23`, `native_build_recipes_2026_06_23`, `crlf_configure_wall`, `exec_bit_stripped`, `binary_location_mismatch`, `not_run_taxonomy`, `eval_orphan_pipe_hang`, `probe_in_task_image_not_ubuntu`, `corpus_wide_sweep_state` + more.

---

## RE-EVAL CAMPAIGN — exact official results (the 23 near-locks)
`scripts/determinex_pb_reeval_campaign.py` (single-instance PID-guard + heartbeat + resumable done-markers). Targets `/c/tmp/reeval_targets.txt`, log `/c/tmp/reeval_campaign.log`.

| tool | official | tail nature |
|---|---|---|
| elfcat | 1207/1210 (gap3) | 3 output-mismatch (ELF→HTML, huge diff) — **most fixable** |
| pipr | 1346/1351 (gap5) | 3 fail + 2 skip |
| tinycc | 4035/4040 (gap5) | root-perm ceiling (structural) |
| srgn | 3922/3928 (gap6) | 5 fail |
| xz | 3440/3446 (gap6) | 2 fail + 4 skip |
| oranda | 1735/1745 (gap10) | 9 fail |
| hashcards | 2433/2444 (gap11) | 8 fail + 3 skip |
| delta | 2085/2097 (gap12) | 12 fail |
| **hush** | 2564/~2581 (gap~17) | **15 results_read_failed (PB branch-crash) + 2 fail — STRUCTURAL** |
| mdbook | 3363/3386 (gap23) | 17 fail + 6 skip |
| oha | 1968/1994 (gap26) | 13 fail + 4 skip |
| dstask | 2823/2867 (gap44) | 40 fail + 4 skip |
| git-graph | 1190/1301 (gap111) | 109 fail |
| **lua / json-tui / walk / pls** | ~2% / 38% / 24% / 0% | **LOCAL-vs-Hetzner DIVERGENCE** (like melody — local eval ≠ Hetzner, same binary) |

**Bartib**: 1650/1651 (gap1, 1 upstream skip) — datetime clock-plugin fix worked, but the skip is structural.

---

## WHY NO CLEAN LOCK (the walls, per corpus)
- **results_read_failed / `nr_tests_json_eval_prefix`** (hush): a PB test-branch's `eval.tests.*` tests are in tests.json but the branch eval crashes (no results.xml) → not_run. Corpus status: **OPEN, complex per-branch diagnosis** (also miller 2207, rumdl 2437, grex 47). NOT a build/output fix.
- **Local-vs-Hetzner divergence** (lua/melody/json-tui/walk/pls): same binary scores far lower locally than on Hetzner. Root cause partially the bidir-mirror (now fixed) but residual divergence remains — env/build-flavor specific. **Needs per-tool reconciliation.**
- **Structural ceilings**: root-perm (tinycc), upstream skip (bartib), output-mismatch version diffs (elfcat).

---

## INFRA LEARNINGS (cost hours — DO NOT repeat)
1. **MSYS `kill -0` and `ps | grep` are UNRELIABLE** on Windows (Windows pid ≠ MSYS pid; ps cmdline truncated). Liveness checks gave false-DEAD → I relaunched → **18-process runaway campaign**.
2. **The fix**: run the campaign as a **single harness-tracked Bash background task**; NEVER blind-relaunch. The campaign now has a **PID-guard (os.kill in python)** + **heartbeat file** (`/c/tmp/campaign.heartbeat`, mtime < 900s = alive) — use the heartbeat + `docker ps -q | wc -l` (1–2 normal), not pid checks.
3. **Runaway signal** = containers > 4 OR all "Up 3-9 seconds". **Nuclear fix** = PowerShell `cmd /c "taskkill /F /IM python.exe"` then `docker rm -f` all. WARNING: `taskkill /IM uv.exe` when uv absent throws NativeCommandError → PowerShell exit 1 that **masks all output** (looks like failure but kills worked).
4. **eval_orphan_pipe_hang**: nohup whale_build evals die → orphan the eval → pipe-block hang. Use tracked tasks.

---

## NEXT STEPS (corpus-prioritized)
1. **elfcat** (gap3 output-mismatch) — the one truly build/version-type tail; harvest the 3 ELF→HTML diffs, check for a single root cause (version/flag). Most-tractable lock attempt, but NOT promised.
2. **Local-vs-Hetzner reconciliation** (lua/melody/json-tui/walk/pls): the bidir-mirror strip should have helped — re-verify; residual divergence is env/build-flavor. High leverage (unblocks a whole class) but deep.
3. **Buildfail whales** per `buildfail_whale_taxonomy_2026_06_23` (the 167k test-gain): (a) **stale-in-pull recovery** — re-eval tinycc/ctags/jq (already fixed, cheap aggregate recovery); (b) probed recipes lz4(make-include)/dog(source-gap mutagen crate)/tig(autoreconf); (c) **configure-step mega-whales** php-src(13k)/proj(5.7k)/duckdb(7k) — hardest, biggest gain, need configure-generated-headers engineering.
4. **results_read_failed class** (hush + miller/rumdl/grex) — OPEN; needs per-branch collection-failure diagnosis. Defer unless a pattern emerges.

## STATE / TRUST
- Test resolution NOW (official aggregate, pull best-run): ~280k/448k ≈ 62.6% (understated — stale-in-pull tinycc/ctags/jq would recover ~15k).
- Official lock count: **65** (committed set; verified_locks.json provenance-gated).
- Hetzner: **OFF** (user shut it down); full pull at `T:/determinex-hetzner-pull-20260623/` (521 results + 255 compile.sh).
- Campaign artifacts: `/c/tmp/reeval_targets.txt`, `/c/tmp/_camp_done/`, `/c/tmp/reeval_campaign.log`.

*Determinex · ProgramBench · 2026-06-24 · official-metric + bidir-mirror-strip + near-lock measurement session*
