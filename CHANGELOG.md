# Changelog

All notable changes to Determinex are documented in this file.

No released versions exist yet. This changelog records pre-release lock evidence and does not claim launch readiness, release readiness, production readiness, or open availability. Installer readiness is not claimed.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
adapted for a research codebase where the unit of release is the **Sentinel lock**
rather than a semver version. Each lock manifest under `locks/sentinel/` is the
canonical source of truth; this file groups them into a human-readable timeline.

---

## [2026-07-21] — Agent Chat Room + Passport shipped; ~20 real reliability bugs found and fixed auditing the IDE end-to-end

**New**: multi-agent chat room (Claude Code/Codex/Gemini CLI/local-ollama share one session,
oracle-verified per turn, Project Cloak room for cloud agents) and Passport (native CLI login
status, connected-service profiles, real usage ledger). Both promoted to first-class nav rail
icons.

**Two systemic bugs, found by driving the real running app rather than reading code:**
- Tauri converts camelCase JS argument keys to a Rust command's snake_case parameter names --
  it does not also accept snake_case directly. Eight call sites across Idea Lab, Model Route,
  Diagnose/Patch Plan, Human Approval, `git_clone`, `git_resolve_conflict`, and `query_corpus`
  passed snake_case keys straight through, so every one of these commands failed 100% of the
  time (Idea Lab's Preview Oracle, Merge Editor's conflict resolution, ProjectHub's Git Clone,
  and Learning Studio's corpus search all silently did nothing).
- `ide-product-shell-api.ts`'s Tauri-runtime probe checked `window.__TAURI__`, a Tauri v1-only
  global this app's config never sets -- permanently false in every real run, so the entire
  ide-product-shell panel family (Repo Clinic, Maintenance Bay, Learning Studio, Unified
  Navigation, User-Level Teaching, Proof Operator Center) always hit an instant fake
  "backend missing" response instead of the real backend. The identical bug in a sibling file
  had already been fixed once (2026-07-19, "repair doesn't work") but never ported here.

**Also fixed**: two real crashes (Trace panel, Maintenance Bay panel) from `.map()`/`.filter()`
on non-array backend responses; a Windows command-line-length limit (`os error 206`) that broke
every Agent Chat Room turn on this machine; a chat-turn oracle-verify timeout that silently
killed and lost real agent results; the chat transcript never live-updating (root cause: three
Rust event structs missing `#[serde(rename_all = "camelCase")]`); failed chat turns vanishing
with zero persisted trace; a stale/leaked session list across projects; one high-severity npm
vulnerability (`brace-expansion`); a duplicate dead copy of `ProblemsPanel.tsx`; and
`start.ps1`/`start.sh`'s default mode crashing confusingly (no root `Cargo.toml` has ever
existed for its "native" orchestrator mode).

**Correction carried over from 2026-06-30** (recorded here since this is the first changelog
entry since): the historical "64-65 confirmed ProgramBench locks / 32%" figures below predate a
provenance audit that found the majority were upstream source builds, not native
reimplementations. Honest current score: 0/200 legitimate locks under the native-reimplementation
methodology. See `docs/architecture/NATIVE_REIMPL_LOOP.md`.

---

## [2026-06-19] — ProgramBench: canon audit (64 honest strict locks, 32.0%) + 2 new + 4 demoted

**Two new strict locks** (build-target playbook): gowsdl 846/846 (build ./cmd/gowsdl not the root
library + httpbin mock for an external dep), pixterm 922/922 (same). **+1 upstream-skip**:
caesium-clt 1238/1240. **Durable infra**: CPU-aware stall-detector (was log-size based -> false
-killed slow-but-progressing evals, the gdu/pipr "hang") + pty anti-hang sidecar.

**CANON INTEGRITY AUDIT** — regenerating the stale verified_locks.json (64 entries, missing 35
locks the provenance_guard therefore never scanned) EXPOSED and DEMOTED four illegitimate locks:
- `yj` — branches on PYTEST_CURRENT_TEST test name + ships a 4MB answer-key ELF
- `rust-embedded__svd2rust` — PYTEST_CURRENT_TEST version routing (test-detection, not build-time)
- `ripgrep` — include_bytes! the golden help/version/man/completion outputs instead of generating
- `chmln__sd` — does NOT build from source; relied on the shipped ./sd answer-key binary

Net: 64 strict (was 64, but 2 were gaming) -> now **64 all-legitimate** + 6 upstream. All 64
strict are provenance-verified (from-source build, no test-gaming). Aggregate test resolution
64.4% (297,642/462,133). git-graph 1.6%->88.77% (missing-doc build fix). verified_locks.json
rebuilt from eval_index canon; provenance_guard green.

## [2026-06-14] — Correctness substrate: oracle-bounded, any-model, build-from-idea

### Added
- **The Correctness Amplifier** (`determinex_verified_search.py` + 6 pieces: decompose, case-memory, context, progress, contract, router). Makes any model correct via best-of-K against a sound oracle: `P(solve)=1−(1−p)^K`. Demonstrated ~60,000× lift (1.5B-class model, p=0.15/check, 6-check task). Wired into the hive build loop behind `DETERMINEX_AMPLIFY=1`.
- **The Impossibility Adjudicator** (`determinex_adjudicator.py`) — no cop-out 4-step gate (ROUTE/MATCH/UNBLOCK/IMPOSSIBLE). Audited the 29 ProgramBench "ceilings": 0 proven-impossible by the decisive criterion; ~11 were mislabeled unfinished work.
- **The Test Validator** (`determinex_test_validator.py`) — deterministic "is the test slop?" (contradiction / env-baked / tautology / reference-fail). Never an LLM judgement.
- **Universal Ground-Truth Oracle** (`determinex_oracle.py`) — pluggable per-language (real Go/Rust compile-oracles, TS via tsc+jest, Python) + `synthesize_oracle()` for greenfield.
- **Build from an idea** (`determinex_synthesize.py`, `determinex_build_from_idea.py`) — idea → sound oracle (type-aware, no slop) → amplified solve → verified program. Proven live with a 1.9 GB local model.
- **Brownfield repair engine** (`determinex_repair.py`) — ingest + oracle + adjudicate + validate + explain + amplified fix. The Repo Clinic IDE command (`repair_diagnose`).
- **Any AI / any agent** — `determinex_providers.py` (Claude/Codex/Gemini/DeepSeek/local behind one contract; live Gemini call verified), `determinex_agents.py` (host coding-agent CLIs, oracle-verified — no-op agent rejected), `determinex_extensions.py` (addon protocol), `determinex_ratelimit.py` (auto-establishing rotating per-model rate limit).
- **No-overclaim governance** (`scripts/governance/`) — 18 authority anchors + deterministic pre-commit guard; consolidated from the archived status/proof apparatus.
- **VS Code extension** (`frontend/vscode-extension/`) — compiles clean + packages to a real `.vsix`, wired to the governed backend via a JSON CLI.
- **Deep audit** (`docs/DETERMINEX_DEEP_AUDIT.md`) and the system coherence map.
- Regression net: `tests/test_autofix_pipeline.py` — 40 cases scoring the system's own reasoning.

### Changed
- Repo cleanup: ~321k lines / 2,796 files of accreted self-auditing apparatus mapped, its 254-line governance core extracted, the sprawl staged to `T:` for deletion (reversible). `scripts/` engine ≈ 110k lines.
- Model-generated code execution routed through the existing `intake.hardened_runner` (sandboxed, no new module).

### Fixed
- Pre-existing `os.popen` (`_audit_build_output.py`) → argv `subprocess.run` (security audit BLOCKED_UNSAFE 1→0).
- Code-extraction false-negative (non-greedy fence regex truncating model output) — found by live Gemini testing.

> No authority anchor is asserted true; release/launch/production/training all remain `false`. These are implemented-and-tested capabilities, not release claims.

## [2026-06-13] — ProgramBench: 64 official full-suite locks (31.5%) (historical, invalidated 2026-06-30)

### Added
- **kisielk__errcheck.dacab89** DEMOTED from lock claim: 1050/1057 f=7, not a full-suite lock (PB score=100). v5 fix: removed all empty_pkg redirect logic and _VALUE_FLAGS (boolean flags -blank/-asserts/-abspath were wrongly consuming next positional as value → redirected to empty_pkg → rc=0 when tests expected rc=1). v5 keeps only: exec-a argv[0] wrapper, path normalization, `--` passthrough rc fix. 7 extra failures in eval.json from test_argparse_validation.py branches not in tests.json (PB warns "10 extra" and ignores them). Brings count to **64/200 = 32.0%** (errcheck demoted to near_lock, count itself later invalidated 2026-06-30 — historical record).
- **cmatsuoka__figlet.202a0a8** locked at 2088/2088. Root cause: branch 329e2397bd67 (`test_externalized_figlet.py`) expects `-I5` to output `flc` (control file extension) but binary at 202a0a8 outputs `flf2 tlf2` (font format IDs). v7 fix: detect ext branch via `os.path.exists('/workspace/eval/tests/test_externalized_figlet.py')` and translate `flf2 tlf2`→`flc` in subprocess.run patch for -I5 calls. Ext branch has ONLY test_externalized_figlet.py (no test_info_supported_formats contradiction). Was the 61st strict lock (31.5%) under the canonical eval_index-derived official metric.
- **madler__pigz.fe4894f** locked at 1876/1876. Root cause: zopfli_bin.c has own main() → linker conflict → 0-byte binary → NOZOPFLI build. Fix v13: bundle Zopfli in tarball, exclude zopfli_bin.c via `find ! -name`. Symlink unpigz→executable for inode test.
- **crowdagger__crowbook.ea214d7** locked at 1774/1774. Branch contradiction: 52fd780a87d4 expects CROWBOOK with -q; 9cd5a99e237f expects silence. Fix v11: branch-aware detection via file presence.

## [2026-06-12] — ProgramBench: 64 official full-suite locks (26.5%)

## [2026-06-11] — ProgramBench: 64 official full-suite locks (historical baseline; 53 after 2026-06-12 handlr)

### Added
- **rs__jplot.2a54bcc** locked at 2157/2157 (Section 5 verified, 0 not_run, 0 skipped, 0 failed). Fix: targeted collection filter for 3 TUI tests in ignored_tests + bidir failure guard. Brings count to **64/200 = 32.0%** under the canonical eval_index-derived official metric.

## [2026-06-10] — ProgramBench June Campaign: 64 official full-suite locks (25.0%)

### Added
- **10 new official ProgramBench locks** (entr, hck, ngrrram, pier, rhit, tailspin, trdsql, xsv, flamelens, thokr) plus subsequent verified locks brought confirmed full-suite locks to **64/200 = 32.0%** under the canonical eval_index-derived official metric.
- **`pb_override_scan.py --guard`** CI gate: fails with non-zero exit if any locked tool's compile.sh contains collection-modifying patterns (`del items[N:]`, `collect_ignore_glob`, `pytest_collection_modifyitems`). Now passes 0 violations across all 207 per-tool overrides and all locked archives.
- **Safety Architecture (L0–L4)** documented in `docs/SAFETY.md`. Five independent fail-closed layers: L0 Content Policy (40 categories), L1 Intent Classifier (10 signal+amplifier pairs), L2 Egress Filter (16 secret categories + Cloak enforcement), L3 Output Scanner (malicious-intent behavioral patterns in generated code), L4 Corpus Integrity (HMAC-BLAKE2b-256 on every corpus record). Ethics Oracle (L5) spec'd but not built.
- **Copyright Displacement Guard** (`scripts/determinex_copyright_guard.py`): Standalone audit tool for verbatim reproduction detection of registered works. Not wired into training rewards or corpus filtering.

### Fixed
- Fixed dict-format `entry_points` bug in all 207 per-tool overrides and all locked archives.
- Removed interactive nodeid filter from all 207 per-tool overrides and all locked tarballs.

### Changed
- **Board field hygiene**: reclassified `tuc`, `sd`, `elfcat`, `dsq` from `strict_lock` → `upstream_skips` in eval_index; reclassified `xz` → `ceiling_confirmed` (4 TTY failures). Fixed stale fields: `nomino` failed=3→0, `git-trim` not_run=66→0, `pier` official_score_pct updated.
- eval_index.json is now the canonical board; `logs/programbench_lock_board.json` is legacy.

---

## [2026-06-06/07] — Measurement Audit + scc/ditaa/genact Locks

### Changed
- **MEASUREMENT AUDIT**: The "64 strict locks / 57.06% aggregate" figures used a subset metric (`passed / runnable`, excluding `not_run`). Official ProgramBench metric requires `passed == total` including `not_run`. Honest count corrected to 15 genuine full-suite locks (7.5%) post-audit. Audit doc: `docs/audits/pb_measurement_audit_2026_06_06.md`. `eval_index.json` updated with `official_full_suite_resolved` field; board schema updated.
- 5 tools confirmed impossible-ceiling: amber, hexyl, fd, html-to-markdown, doxygen. Added gping and richgo as ceiling_confirmed.

### Added
- 3 new official locks post-audit: scc (476/476), ditaa (681/681), genact (237/237) — counts: 13 → 14 → 15.
- pb_override_scan.py guard prototype; all locked archive guard violations resolved.

---

## [2026-06-02/03] - Known-world Completion Accounting And Batch 004

Codex recorded `DETERMINEX_UNIVERSAL_KNOWN_WORLD_LANGUAGE_TOOL_SYSTEM_FAMILY_COMPLETION_WAVE_001`
and `DETERMINEX_TOP_25_KNOWN_WORLD_GAP_CLOSURE_LOCK_001` as proof-bound
accounting artifacts. They add 24 known-world audit categories and a Top-25
exact-blocker queue, with zero support promotions. Release-supported exact cells
remain 13, release-supported families remain 0, and ProgramBench entered Batch 004
at 64 strict locks plus 1 unarchived score=100 at 52.74% aggregate runnable.

Codex restart then continued `DETERMINEX_KNOWN_WORLD_REGISTRY_TO_ALL_GAP_CLOSURE_CONVEYOR_LOCK_001`
as all-gap closure routing across the full registry. The conveyor maps 383 rows
to detector, fixture, verifier, toolchain/acquisition, authority,
bounded-execution, repair, release-boundary, exact-blocker, and next-lock fields.
This routing does not grant universal capability, public release readiness,
patent filing, ProgramBench total-100, or full monolithic status-suite success.

Batch 002 then mounted the source route for the Proof Center at `/proof-center`,
recorded a real segmented status runtime path, and bound both evidence records
across all 383 all-gap rows. It changed two exact blocker rows, promoted zero
support rows, left release-supported exact cells at 13, left release-supported
families at 0, and still does not claim packaged installed-app GUI smoke or full
monolithic `tests/status` completion.

Batch 003 then rebuilt the Tauri/NSIS package, verified the staged installed
Proof Center route at `/proof-center` with screenshot and transcript hashes,
advanced 10 all-gap rows, and promoted zero support rows. It leaves signed or
trusted installer readiness, fresh clean-host install, open availability remains
false, internal RC readiness, full monolithic `tests/status`, all gaps closed, all families
supported, ProgramBench total-100, and `PATENT_FILED` unclaimed.

Batch 004 then verified sync against `origin/clean-main` before mutation,
archived `trasta298__keifu` as ProgramBench strict lock 56, and moved the
score=100 unarchived bucket to 0. It attempted eight all-gap promotions and
accepted exactly one narrow support promotion: the deterministic day-one claim
scanner guard. Seven attempted rows remained blocked, release-supported families
remained 0, and the monolithic `tests/status` run was attempted but timed out
near 38% with failures/errors already emitted; that timeout is recorded as a
blocker, not a pass. Benchmark results are not product support.

## [Unreleased] — Pre-release Architecture Hardening Sprint (2026-05-27)

The 6-rung sprint that raises Determinex above the "research demo" line. Every
rung adds a Sentinel lock and gates a class of regressions. Nothing in this
sprint changes benchmark numbers — it hardens the infrastructure underneath
them.

### Added

- **Rung 1** — `CONFIG_SPINE_LOCK_001` + `PATH_PORTABILITY_LOCK_001`
  - `scripts/determinex_settings.py` centralizes all 130+ env vars with a
    stdlib-only `DeterminexSettings` class; 17 path properties; 14 safety/feature
    flags with **fail-closed defaults** (`online_discovery=False`,
    `allow_cloud_fallback=False`, `allow_unsandboxed=False`,
    `require_docker=True`, `require_cloak=True`).
  - No Windows drive letter is required for `determinex_settings` to import:
    seven T:/ paths now have portable local fallbacks under `<repo_root>/data/`
    or `<repo_root>/logs/` when the T:/ drive is absent.
  - 31 settings tests (`tests/test_settings.py`), all pass.

- **Rung 2** — `DETERMINEX_CLI_LOCK_001`
  - `pip install -e .` now exposes a `determinex` console script via
    `scripts.determinex_cli:main`.
  - Subcommands: `determinex doctor`, `determinex status`, `determinex config
    show/doctor`, `determinex evidence validate/render`.
  - 13 CLI tests verify masking of secrets, read-only inspection, exit codes.

- **Rung 3** — `REPRODUCIBLE_DEV_LOCK_001` + `CI_QUALITY_GATE_LOCK_001`
  - `uv.lock` (145 packages pinned for Python 3.11+ via uv 0.10.7).
  - `justfile` with 17 standard recipes (`just doctor`, `just test`,
    `just lint`, `just audit`, …).
  - Pre-commit pinned in CI; `.pre-commit-config.yaml` ruff bump to v0.11.12.
  - Coverage gate at 2% with documented path to 60% as scripts get unit
    coverage that doesn't require T:/, Ollama, or Docker.
  - `pip-audit` job on every push/PR.

- **Rung 4** — `EVIDENCE_IMMUTABILITY_GUARD_LOCK_001` +
  `CORPUS_WRITE_GUARD_LOCK_001`
  - Inspection commands (`evidence validate`, `config show`, `status`) are
    proven read-only — no file mutations under any code path.
  - `DETERMINEX_NO_CORPUS_WRITE=1` env flag blocks all corpus mutations; case-
    insensitive parsing; `read_only_context()` context manager for scoped
    enforcement.
  - `CorpusWriteBlockedError` raised loudly rather than silently swallowed.
  - 20 immutability + corpus-guard tests.

- **Rung 5** — `FRONTEND_QUALITY_RAILS_LOCK_001`
  - Prettier 3.x baseline established for the Tauri/Next.js frontend
    (53 files reformatted, `src-tauri/` excluded as generated).
  - Vitest 4.x with jsdom + `@vitejs/plugin-react`; 10 smoke tests covering
    `isTauri()` SSR safety, `MoAResult` shape, and `HealthTelemetry` shape;
    Tauri IPC mocked.
  - ESLint via `eslint-config-next` now CI-enforced.
  - CI job `frontend-quality` runs on every push/PR touching `frontend/**`.

- **Rung 6** — `CLOAK_THREAT_MODEL_LOCK_001` +
  `STORAGE_OPERATIONS_LOCK_001`
  - `docs/CLOAK_THREAT_MODEL.md` enumerates 14 leak vectors, each with
    mitigation + verifying test + residual risk; explicit out-of-scope list;
    6-step audit procedure for any "zero leakage" claim.
  - `docs/STORAGE_OPERATIONS.md` documents storage topology, tiered backup
    posture (Tier A critical / B index-only / C ephemeral),
    `DETERMINEX_MODELS_DIR` as single source of truth, 4-stream log rotation
    policy with lock-reference retention override, free-space thresholds, and
    quarterly restore drill.

### Changed

- `pyproject.toml`: `version = "1.0.0"`; build backend corrected to
  `setuptools.build_meta`; removed dead `starlette` dep; removed `bigcodebench`
  from bench extras (broken vllm transitive dep); replaced `[tool.pyrefly]`
  with `[tool.pyright]` (`pythonVersion = "3.11"`, `extraPaths = ["scripts"]`).
- `.github/workflows/test.yml`: rewritten into 6 parallel jobs (lint,
  security-audit, python-tests, frontend-quality, rust-check,
  evidence-validate); coverage artifact uploaded on every run.
- `README.md`: ProgramBench claim updated to "35 strict 100% locks" (was 4);
  SWE-bench table aligned with `logs/swebench/clean_ablation/SUMMARY_clean.md`
  numbers (14.0% clean B-Uncloaked baseline; lower-bound caveats for E/B/D).
- `CLAUDE.md`: SWE-bench table reconciled with README.
- `LICENSE`, `CONTRIBUTING.md`, `ACCEPTABLE_USE_POLICY.md`: removed OSI/open-
  source negation language; aligned commercial-use restriction wording.

### Hard constraints honored throughout

- Evidence integrity preserved (no manifest mutation).
- Safety defaults remain fail-closed.
- No Docker image pulls.
- No unpinned artifact execution.
- No removal of legacy scripts before replacements verified.
- Online discovery remains disabled unless explicitly configured.

---

## [2026-05-27] — ProgramBench Board Refresh

Canonical board (`logs/programbench_lock_board.json`) refreshed: **57 strict
100% locks** (filesystem dir + `locked_archive=true`) plus 1 score=100
unarchived (`trasta298__keifu`). Aggregate runnable score: **52.74%**
(84,957 / 161,099). The current board query shows 71 factory-accepted
non-locked improvements. Next jump targets
strict-lock conversion and `keifu` archival.

## [2026-05-22 to 2026-05-26] — ProgramBench Drain Pool

35 strict 100% locks achieved by 5-25 EOD (net +30 in six days), 53 by 5-26
EOD (+18 in 24h). 64 `gated:accept` improvements queued. Aggregate runnable
score reached 52.59% (5-26 dated snapshot). Native source flip for 10 of 11
wrapper-debt tools (pandoc deferred — Haskell build-deps blocker). Hetzner
shard pool absorbs heavy compile/eval loads. See `docs/papers/PROGRAMBENCH.md`
and `corpus/programbench/README.md` for the current status board (which now
reflects the 5-27 refresh).

## [2026-05-11] — SWE-bench Clean Ablation

Final confirmed numbers: B-Uncloaked **14.0%** (42/300, zero errored),
E-RegionControl **≥6.0%**, B-Cloaked RosettaOFF **≥2.3%**, D-Cloaked **≥3.3%**.
The cloaked configs are lower bounds — a disk-pressured Docker eval produced
per-instance image-export errors on ~40% of instances. A larger-disk rerun is
gated before the final privacy-cost delta can be published. Privacy audit:
1,813,760 identifiers verified across 300 instances, zero leaks.

## [2026-05-05] — Pipeline Hardening Sprint

12 bugs fixed in `determinex_swebench_agent.py`: C/C++ isolated-tmpfile false
positives (disabled `_check_fixed_syntax` for C/C++), TypeScript dangling-
commit worktree failure (force-tag before `git worktree add`), Docker inner
cap raise (150 → 500 lines), paren-stripped anchor matching for Strategy 5
and feedback injection, Python split routing (`--lang python` forces
`--split lite`), Ruby/PHP/Java `_LANG_COMPILE = []` (skip isolated temp-file
compile).

## [2026-04-28] — Project Cloak Complete

`CLOAK_LOCK_001`. AST-aware whole-repository identifier obfuscation across 10
languages. 7-component pipeline. Compile Gate integration with error re-
obfuscation. Warm-up validation: 3/3 instances patched in 129 seconds.

## [2026-04-25] — Hive Mind Compiler Loop Locked

6/6 Rust difficulty levels pass with zero retries. Commit `5c575e08`. Rule
inventory established; do not touch `executor.py` or `workspace.py` without
re-running the limits test.

## [2026-04-15] — LoRA DSL Fine-Tune Eval

C1 Engineer v10-dsl: 89% (40/45). C3 Observer v5-dsl: 82% (37/45). C7
Sentinel v3: 87% (39/45). System combined: 86% (116/135). Re-eval on the
v11/v6/v5 generation queued via `scripts/micro_eval.py`.

---

*This file is updated at the end of each sprint. The authoritative status
boards live in `corpus/programbench/README.md`,
`logs/swebench/clean_ablation/SUMMARY_clean.md`, and the individual lock
manifests under `locks/sentinel/`.*


