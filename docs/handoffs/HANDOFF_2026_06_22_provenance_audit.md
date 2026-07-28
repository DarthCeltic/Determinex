# HANDOFF — ProgramBench Lock Audit & Provenance Repair (2026-06-22)

## TL;DR — the honest state
The "65 ProgramBench locks" are **real PB resolutions but source-assisted + hidden-test-tuned (NOT cleanroom)**, count-inflated 2× by a candidate-side bidir injection. They are **not leaderboard-comparable**. The tools genuinely build and pass; the *claim* and *counting* need correcting. Nothing fabricated, but the headline was wrong.

---

## CRITICAL AUDIT FINDINGS (verified, not theory)

1. **ProgramBench is CLEANROOM** — README: *"Given only a compiled binary and its documentation, AI agents must architect and implement a complete codebase."* No source, no internet, hidden tests. Determinex locks **build from upstream source** (provenance gate *requires* it) and were **developed by reading the hidden tests** (the "classname mismatch" fix in CAMPAIGN_200_CEILING.md). → **source-assisted + contaminated, not cleanroom.**

2. **64/65 locks ship a candidate conftest that injects testcases into the scored `eval/results.xml`** (the bidir `_cb_run`/`_cb_mirror`). PB reads ONLY `eval/results.xml` and the submission writes to it — structurally unsound. PB's *official* scorer mostly ignores it (warns "N tests not in tests.json"), BUT:
   - **clog-cli is INJECTION-DEPENDENT**: with injection = 100 (reproduces 1556/1556), **without injection = 73**. So SOME locks need the crutch. Verified empirically.
   - Spot-verified REAL (hold 100 without injection): **gron, direnv, hostctl, handlr, hyperfine, ascii-image-converter** (6/6 of clean tests).

3. **Provenance IS partly wired**: `corpus/programbench/verified_locks.json` → `locks` dict (98 entries, keyed by short tool name) pins `submission_sha256` (92/98). BUT the pinned shas are **repack-drifted** — neither local nor Hetzner current submissions match (clog-cli pinned `f8b34bee`, local+hetzner both `2ffe8215`). The exact scored-100 bytes were repacked by continuous campaign ops. **Content likely intact (reproduces score with injection); exact sha lost.**

4. **Archive was a mess**: 175 dirs for 65 locks (short-name + full-slug + _native/_model duplicates). Cleaned to 104, **88 quarantined to `corpus/programbench/locked/_superseded/`** (retrievable). **37/65 local lock tarballs sha-mismatched.**

5. **corpus_loop has PLATEAUED**: deploys 0/cycle. autofix `fix()` SKIPS the "auto-fixable" tools because the fix-directive is already present — it checks if the text exists, not if it WORKS. Triage MISCLASSIFIES (go-critic flagged "go-toolchain" but actually builds fine; its 74 failures are `--help`/flag-text behavioral mismatches needing version-match). **"Jump all to 100" is NOT automatic — the rest is per-tool engineering, and some are genuine ceilings.**

---

## sha-HUNT RESULT (the canonical submissions ARE recoverable)
`C:/tmp/find_pinned_result.json`: **FOUND 83/86** canonical sha-pinned submissions.
- locations: `_superseded`=43 (cleanup quarantined the winners), `locked`=39, `full_evals_20260608`=1
- **MISSING 3**: `bellard__quickjs.d7ae12a`, `cheat__cheat.b8098dc`, `cslarsen__jp2a.61d205f`

---

## WHAT'S RUNNING (autonomous)
- **Hetzner belt** = all-200 eval engine: `ssh root@5.78.192.163`, `pb_parallel.py heavy.list --slots 2` (heavy.list = 113-tool lockable-first queue, mega-whales last). Guards: `diskguard.sh` (prune images at 80%), `memguard2.sh` (kill heaviest at <1.2GB free). `/tmp/grind/`.
- **corpus_loop** (local, plateaued): `C:/tmp/corpus_loop.py`, log `C:/tmp/corpus_loop.log`, report `logs/programbench_factory/CORPUS_NEEDS_REPORT.md`.
- **Local verification** (suspect — ran on some WRONG tarballs): `C:/tmp/verify2.sh`, results `C:/tmp/verify2.log`. **REDO against sha-matched submissions.**

## KEY FILES
- `corpus/programbench/verified_locks.json` — **source of truth** (sha-pinned registry, `locks` dict)
- `corpus/programbench/eval_index.json` — tier classification (downstream)
- `C:/tmp/find_pinned_result.json` — canonical submission locations (83 found)
- `C:/tmp/sha_mismatch.txt` — the 37 mismatched local tarballs
- `scripts/determinex_pb_autofix.py` — triage + fix (the `fix()` skip-when-present bug is here)
- `scripts/determinex_pb_lock_registry.py` — the sha-provenance code (`--guard`)

---

## NEXT STEPS (in order)
1. **Restore canonical submissions**: copy the 83 found (from `find_pinned_result.json`) into their canonical locked dirs. Recover the 3 missing from Hetzner or accept the repack-equivalent (reproduces score w/ injection).
2. **Re-verify ALL 65 against CORRECT (sha-matched) tarballs**, dual-eval per tool:
   - WITH injection → reproduces registered score? (content correct)
   - WITHOUT injection → holds 100 (clean lock) or drops (injection-dependent, like clog-cli)
3. **Classify** each: clean-sound-lock / injection-dependent / not-lock / build-fail. → the TRUE lock count.
4. **Correct counts** (drop bidir 2×) + **relabel** all "source-assisted / hidden-test-tuned" in eval_index. Wire injection-soundness into the lock gate (not just ad-hoc scripts).
5. **Per-tool engineering** for non-locked toward 100 (local bench → real failure → real fix → push to Hetzner). Bounded by genuine ceilings. NOT automatic.
6. **Later — the real claim**: cleanroom path = wire the amplifier (`determinex_verified_search`) onto a **differential oracle built from the provided binary** (legal dev oracle), free open-source model generates, certify against SEALED PB tests (never shown to solver). Measure generalization on **held-out** tools the corpus never touched.

## THE ONE LINE
Tools are real; locks are source-assisted + hidden-test-tuned + count-inflated + 1-known injection-dependent; archive is cleaned and canonical submissions found (83/86); the loop plateaued so the rest is per-tool work; cleanroom is the separate honest claim, not yet built.
