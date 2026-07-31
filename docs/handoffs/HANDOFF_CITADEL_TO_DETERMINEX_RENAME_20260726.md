# Handoff: Citadel → Determinex rename finalization (2026-07-26)

Paste this whole document as your first message in the new session.

## The task
Ryan's final decision: **"Determinex" wins everywhere. "Citadel" is retired, completely** — prose,
code identifiers, env vars, model tags, paths, the working directory itself, and the GitHub remote.
Background: the project was originally "Citadel." A prose-only rename to "Determinex" landed
2026-07-02, but literal code identifiers (env vars, script names, comments) drifted the *opposite*
direction across several later, independent sessions — they renamed things back toward `CITADEL_*`.
Net result was a real split-brain (docs said Determinex, code said Citadel) that had already cost
wasted debugging time.

## Repo state right now
- Path: `c:\Dev\Citadel` (folder NOT yet renamed — see "Still to do" below)
- Branch: `mojibake-and-count-fix`
- HEAD as of this handoff: `0ded7509b0` ("fix: begin Citadel->Determinex rename finalization
  (directive docs + env vars)") — **first check `git log --oneline -5` and `git status --short`
  the moment you're back in; a background sweep agent (see below) may have already committed on
  top of this, or may still be mid-run.**
- Pre-existing unrelated uncommitted changes that are NOT part of this task, leave them alone:
  `corpus/programbench/build_knowledge.json`, `corpus/programbench/embeddings_cache.meta.json`,
  `corpus/programbench/embeddings_cache.npy`, untracked `docs/handoffs/HF_HACKATHON_PORT_CAMPAIGN_FINDINGS_20260725.md`.

## What's already done (commit `0ded7509b0`)
- `CLAUDE.md`/`AGENTS.md` header notes corrected (accurate rename history; Hetzner box confirmed
  DOWN per Ryan, not the stale "BOX IS UP" status the note previously had — box has been down
  about a week; if/when reprovisioned it should come back as `/root/Determinex` / key
  `id_determinex`, not the Citadel-named paths a prior session's "fix" left behind).
- Env vars fixed to `DETERMINEX_*`: `AMPLIFY`/`_K`/`_ROUNDS`, `ALLOW_UNSANDBOXED`, `REQUIRE_DOCKER`
  — across `scripts/hive/{amplifier_bridge,executor,compiler}.py`, `scripts/determinex_pb_drive.py`,
  `scripts/determinex_settings.py`, the Tauri IPC layer (`frontend/src-tauri/src/ipc_hive/{mod,session}.rs`,
  `frontend/src/components/HiveBuildLoop.tsx`), and 2 tests (`tests/test_settings.py`,
  `tests/test_determinex_cli.py`).
- Root `C:\Dev\CLAUDE.md` (the master multi-project directive, one level up from this repo)
  updated: project table row `Citadel` → `Determinex`, path `./Citadel/` → `./Determinex/` (this
  path doesn't exist yet — see folder rename below), `docs/CITADEL_DEEP_AUDIT.md` →
  `docs/DETERMINEX_DEEP_AUDIT.md` and `scripts/citadel_providers.py` → `scripts/determinex_providers.py`
  (confirmed both are the real on-disk filenames already).
- `origin` remote repointed: `git remote -v` should show
  `https://github.com/DarthCeltic/Determinex.git`. **IMPORTANT — read the "Origin / GitHub" section
  below before doing anything with `origin`.**
- Memory migrated: `C:\Users\ryang\.claude\projects\c--Dev-Citadel\memory\` (89+ files, MEMORY.md
  index) copied in full to `C:\Users\ryang\.claude\projects\c--Dev-Determinex\memory\` so a future
  session starting from `c:\Dev\Determinex` inherits this history. Re-sync that copy again after
  you finish the folder rename below, since new memory entries keep landing in the `c--Dev-Citadel`
  copy until the path actually changes.
- Checked `ollama list`: no functional risk here. Live models are already `determinex-sentinel-v5-dsl`,
  `determinex-observer-v6-dsl`, `determinex-engineer-v11-dsl` (updated recently); the `citadel-*`
  tagged ones are 3-month-stale superseded leftovers, safe to ignore.

## What's still open (do these, roughly in this order)

### 1. A background sweep agent may have already run or still be running
I dispatched a `general-purpose` agent (no worktree isolation — see the incident note below for
why) to do the full remaining mechanical sweep: rename every other `CITADEL_*` env var
(`CORPUS_HMAC_KEY`, `AUDIT_DIR`, `ENGINEER_MODEL`, `OBSERVER_MODEL`, `SENTINEL_MODEL`,
`LEVIATHAN_MODEL`, `ANTHROPIC_KEY`, `ANTHROPIC_MODEL`, `SWEBENCH_REPOS`, `MODELS_DIR`,
`HF_CACHE_DIR`, `N_PREFIX`, `DEEPSEEK_KEY`, `HIVE_CARGO_TARGET_DIR`, `GGUF_MAX_WAIT_S`,
`CLAUDE_MODEL`, `GEMINI_MODEL`, `ROOT`, `DIR`, `VLLM_URL`, `NO_ROSETTA`, `CLOAK_AUDIT`,
`PB_STAGING_ROOT`, and any more it found) plus prose "Citadel" mentions across `frontend/`
(~20 files), `.github/workflows/*.yml`, `k3s/manifests/*.yaml`,
`integrations/openenv/determinex_oracle_env/**`, `dataset_generation/*.py`, `tools/*.py`,
`bundler/setup_sidecar.py`, and anything else a fresh scan turns up. True scope is roughly
150-250+ files.

**Deliberately excluded from the sweep (don't touch these — same precedent an earlier rename
commit already set, don't rewrite history):** `assurance/evidence/**`, `assurance/demo_workspaces/**`
(includes `Cargo.lock` fixtures like `citadel_rust_repair_probe`), `CHANGELOG.md`, dated historical
entries in `docs/papers/**` describing the name as it was at a past point in time,
`assurance/licenses/license_inventory.json` (auto-generated).

As of this handoff, that background agent had **not yet committed** (HEAD was still `0ded7509b0`)
and its last live status was "still running / holding for pytest results." A brand-new session
likely can't resume that exact background agent (it's tied to the conversation that spawned it).
**First move: check `git log --oneline -5` and `git status --short`.**
- If a new commit is already there with a rename-sweep message: read it, verify it looks complete
  and sane (check `git show --stat` for the file list), then proceed to step 2.
- If nothing landed (still at `0ded7509b0`, working tree clean apart from the pre-existing
  unrelated files listed above): the sweep never finished. Re-dispatch it (same prompt shape as
  described above, working directly in this checkout, no worktree isolation) or do it yourself.

### 2. Run the full test suite to confirm nothing broke
`pytest -q` from repo root (or the canonical test command per `CLAUDE.md`), plus `cargo check` in
`frontend/src-tauri` if Rust files changed, plus frontend build/lint if `frontend/` changed.

### 3. Rename the folder: `c:\Dev\Citadel` → `c:\Dev\Determinex`
Ryan confirmed the other Claude Code windows that were running the hf-hackathon campaign all week
are now closed, so this is safe to do. After renaming:
- Re-sync the memory copy one final time (it may already be current, but check).
- Update `C:\Dev\CLAUDE.md`'s path references if the earlier `./Determinex/` link needs anything
  else adjusted now that the folder actually exists there.
- Sanity-check nothing else on the box hardcodes the old `c:\Dev\Citadel` path (VS Code workspace
  settings, shortcuts, etc.) — not audited this session.

### 4. Origin / GitHub — force-push once everything above is verified
`origin` is repointed to `https://github.com/DarthCeltic/Determinex.git`. **This repo has
completely unrelated git history from this dev checkout** (confirmed via `git ls-remote` +
`git cat-file` — zero shared commits; it's a curated public release mirror, not a fork/clone of
this repo). Ryan explicitly approved, when asked: **force-push this full local history to
`DarthCeltic/Determinex`, making it authoritative and overwriting the curated mirror's current
history.** Do this as the *last* step, after the rename is fully complete and tests pass — don't
push a half-finished rename to the public-facing repo. `DarthCeltic` is Ryan's designated
open-source/developer-donation GitHub account — it's the intended final home, not
`DarthCeltic` (whose `citadel` repo the old `origin` pointed to doesn't even exist).

## Incident to know about (already resolved, but don't repeat it)
Earlier this session I dispatched the sweep agent with `isolation: "worktree"`. Its worktree came
up already checked out against completely unrelated history (matching the `DarthCeltic/Determinex`
curated mirror) **before the agent ran any command** — because `origin` had already been repointed
to that unrelated repo moments earlier, and the worktree-creation mechanism apparently defaults to
something `origin`-relative. Nothing was lost (the real `mojibake-and-count-fix` branch was
verified untouched via `git reflog` the whole time; the corrupted worktree was discarded, never
merged). Lesson: **don't use worktree isolation for agents in this repo while `origin` points to
an unrelated-history remote** — that's exactly why the re-dispatched sweep agent was told to work
directly in the main checkout instead.

## Memory
Full context is also in the auto-memory system at
`C:\Users\ryang\.claude\projects\c--Dev-Citadel\memory\` (and mirrored at
`c--Dev-Determinex\memory\`) — see `MEMORY.md`, especially
`project_citadel_to_determinex_rename_finalized_20260726.md` and
`user_darthceltic_oss_account.md`. Also relevant from the same session: hf-hackathon status
(`project_hf_hackathon_model_ports_track_20260726.md` — PR#111/#115/#155 merged 2026-07-21,
SmolVLM2 kernel win landed; new post-deadline "model_ports" track, 35 open PRs, 0 merged as of
last check) and corpus/Determinex gap notes discussed earlier in the original conversation
(1,300 quarantined learned_classes pending reabsorption, TUI/PTY unlock gap across 172 tools,
oracle-faithfulness buildout still open, IO-extractor OR-semantics fix not yet built).
