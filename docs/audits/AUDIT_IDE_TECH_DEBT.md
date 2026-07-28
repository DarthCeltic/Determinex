# Determinex IDE — Full Technical Debt Audit
**Date:** 2026-05-06  
**Audited by:** Claude Sonnet 4.6 (3-pass deep audit)  
**Scope:** frontend/src/ (React/Next.js), frontend/src-tauri/src/ (Rust/Tauri), scripts/ (Python pipeline)

---

## SEVERITY LEGEND
- 🔴 **CRITICAL** — Breaks correctness, crashes app, or silently corrupts data
- 🟠 **HIGH** — Silent failures, data loss, broken features users will hit
- 🟡 **MEDIUM** — Dead code, maintenance burden, confusing patterns
- 🟢 **LOW** — Polish, optimization, minor inconsistency

---

## 🔴 CRITICAL

### C1 — `getPipelineTopology()` always returns null
**File:** `frontend/src/lib/api.ts:142-145`  
`PipelineDashboard.tsx` calls this expecting real DAG data. It always gets null. The entire pipeline view shows hardcoded fake phases ("Phase 1: Architect Sentinel" etc.) that never reflect the actual running session. Dead feature disguised as a real one.

### C2 — `readHiveWorkspaceFile()` payload shape mismatch
**File:** `frontend/src/lib/api.ts:322-331`  
```typescript
invoke("read_hive_workspace_file", { payload: { session_id: sessionId }, relativePath })
```
`relativePath` is spread at the wrong level. Rust expects it inside `payload`. This function silently fails or crashes at runtime on every call.

### C3 — App hard-crashes on DB init failure
**File:** `frontend/src-tauri/src/lib.rs:133`  
`.expect()` on SQLite init. Corrupt or locked DB = full app panic, no recovery dialog, no user message.

### C4 — Orchestrator regex salvage forces confidence = 0.0
**File:** `frontend/src-tauri/src/orchestrator/mod.rs:250-266`  
When JSON parsing fails, salvage path sets `confidence: 0.0`. Confidence threshold for acceptance is 0.75. So salvaged verdicts are ALWAYS rejected downstream — the salvage is a no-op that wastes a cycle and discards what might have been a valid CLEAN verdict.

### C5 — Prompt truncated at arbitrary byte boundary, not token boundary
**File:** `frontend/src-tauri/src/orchestrator/transport.rs:48-56`  
Slices at 512KB byte offset. Can split a UTF-8 multi-byte character or mid-JSON token. Next parse call fails silently with empty response.

### C6 — Sidecar `try_lock()` on shutdown leaves zombie Python processes
**File:** `frontend/src-tauri/src/lib.rs:115-120`  
Non-blocking lock; silently skips quit signal if mutex is held. Python sidecar keeps running after app closes. Accumulates across app restarts.

### C7 — ServiceLoginModal mangles service name before sending to Rust
**File:** `frontend/src/components/modals/ServiceLoginModal.tsx:19-25`  
Strips `_`, `API_KEY`, `_TOKEN`, `_URL`, `_DSN`, `_ENABLED` from the key name. `"SLACK_WEBHOOK_URL"` becomes `"SLACKWEBHOOK"`. Rust `save_service_key()` won't match it. Keys silently not saved.

### C8 — `check_child_exit_for_oom()` is dead code — OOM events never fire
**File:** `frontend/src-tauri/src/orchestrator/mod.rs:543`  
Marked `#[allow(dead_code)]`, never called when processes exit. OOM kills are never surfaced to user. Jobs die silently with no explanation.

### C9 — Mutex unwrap panics in benchmark module
**File:** `frontend/src-tauri/src/ipc_benchmark.rs:146, 301`  
`.lock().unwrap()` — if mutex is poisoned by a thread panic, the next benchmark command panics the whole Tauri process.

### C10 — "Sync Context to Git" button has no onClick
**File:** `frontend/src/app/page.tsx:533`  
Dead UI control. Users click it expecting Git sync, nothing happens, no error. Remove or implement.

---

## 🟠 HIGH

### H1 — 8+ silent `.catch(() => {})` blocks across components
**Files:** `page.tsx:223, 259`, `PipelineDashboard.tsx:231`, and others  
Async IPC failures silently produce blank/default UI with zero user feedback. Users think the app is working when it's broken.

### H2 — `saveApiKeys()` closes modal even on failure
**File:** `frontend/src/components/modals/SettingsModal.tsx:112`  
`await saveApiKeys(keyInputs); onClose();` — `onClose()` runs regardless of whether save succeeded. User thinks keys are saved when they're not.

### H3 — Log ring buffer silently drops lines with no marker
**File:** `frontend/src-tauri/src/ipc_hive/mod.rs:67`  
At 10K lines capacity, oldest entries are silently discarded. Frontend has no way to know data was lost. Critical error messages can disappear from the log pane.

### H4 — RAG retrieval swallows all errors silently
**File:** `frontend/src-tauri/src/orchestrator/rag.rs:77-117`  
6 error paths all return `String::new()` with no logging. If vector engine crashes, pipeline continues with zero context and no indication anything is wrong.

### H5 — Cloud model fallback silent
**File:** `frontend/src-tauri/src/orchestrator/pipeline_models.rs:52`  
If litellm config assigns a cloud model but no API key is set, returns `None` and falls back to local model silently. User configures cloud inference, gets local inference, doesn't know why quality is different.

### H6 — `getKnowledgeSuggestions()` result parsing broken
**File:** `frontend/src/lib/api.ts:124-140`  
Assumes `result.data.plan.steps` exists. `orchestrate_plan` may return different structure. Silently produces empty suggestions array.

### H7 — 5 different Tauri runtime check patterns
**Files:** `page.tsx:271, 194`, `api.ts:9`, `ConceptLab.tsx:40`, `WorkspaceViewer.tsx:20`  
One of these is probably wrong. Zero-cost fix: one `isTauri()` function used everywhere.

### H8 — Training pair telemetry asymmetric
**File:** `frontend/src-tauri/src/orchestrator/mod.rs:587`  
Training pairs only logged on compiler failure, not on Observer rejection. If Observer rejects a compile-passing patch, no training data captured. Flywheel misses a valuable (error→fix) pair.

### H9 — `project_root()` falls back to `"."` silently
**File:** `frontend/src-tauri/src/ipc_hive/mod.rs:253-288`  
If all heuristics fail, uses current directory as project root. `./scripts/determinex_hive.py` silently doesn't exist. Session launch fails with cryptic "file not found."

### H10 — 22 `as any` casts with global ESLint disabled
**File:** `frontend/src/app/page.tsx:1`  
`/* eslint-disable @typescript-eslint/no-explicit-any */` at the top. Backend response shape changes will produce silent undefined values throughout the entire main component.

---

## 🟡 MEDIUM

### M1 — 9 Rust IPC commands exported but never called from frontend
```
orchestrate_codegen    — exported, never invoked
orchestrate_audit      — exported, never invoked  
converse_idea          — exported, never invoked
discover_idea          — exported, never invoked
refine_spec            — exported, never invoked
explore_workspace      — exported, never invoked
diagnose_workspace     — exported, never invoked
fix_workspace          — exported, never invoked
start_session          — exported, never invoked (generate_dag + run_session used instead)
```
Either remove from `generate_handler!` or implement frontend wrappers.

### M2 — 4 dead functions in api.ts
- `getTelemetry()` (line 58) — duplicate of `getHealthTelemetry()`, 0 callers
- `generateIdeationSteps()` (line 197) — 0 callers
- `createHiveSession()` (line 286) — frontend uses `invokeSafe("create_session")` directly
- `generateHiveDag()` (line 295) — frontend uses `invokeSafe("generate_dag")` directly

### M3 — `drain_all()` dead code in log ring buffer
**File:** `frontend/src-tauri/src/ipc_hive/mod.rs:73`  
`#[allow(dead_code)]` — expose as IPC command for log export or delete.

### M4 — LoadingThemes index.ts exports nothing
**File:** `frontend/src/components/LoadingThemes/index.ts`  
10 theme components defined but index doesn't re-export them. Each must be individually imported. Theme selection can fail if the import path isn't exact.

### M5 — Inconsistent Hive command abstraction
Some Hive commands have typed wrappers in `api.ts`, others are called via bare `invokeSafe()` inline. No consistent pattern. Makes it hard to add error handling or change signatures.

### M6 — `fine_tuning/` missing `__init__.py`
**File:** `scripts/fine_tuning/`  
Directory used as a package but not declared. Import behavior depends on working directory. Breaks in some environments.

### M7 — Overlapping benchmark/eval scripts
`determinex_benchmark.py` vs `determinex_benchmark_5run.py` vs `benchmark_runner.py` — unclear differentiation. Same for `micro_eval.py` vs `micro_eval_extra.py` and `rosetta_recall_eval.py` vs `rosetta_vs_text_eval.py`. Three different scripts doing similar things with no clear "use this one" guidance.

### M8 — Provider/validator abstractions defined but unused
`scripts/providers/` and `scripts/validators/` define clean PROVIDER_MAP/VALIDATOR_MAP that the main agent pipeline (`determinex_swebench_agent.py`, `determinex_hive.py`) never calls. Dead abstraction.

### M9 — `executor.py` is 1943 lines
**File:** `scripts/hive/executor.py`  
Same tech debt that motivated the `ipc_hive.rs` split. Needs splitting into logical modules.

### M10 — Environment variable naming chaos
`ANTHROPIC_API_KEY`, `DETERMINEX_ANTHROPIC_KEY`, `DEEPSEEK_API_KEY`, `DETERMINEX_DEEPSEEK_KEY` — 4+ prefix styles all read with fallback chains in `constants.py`. Confusing for users setting up `.env`. Standardize to `DETERMINEX_*` with clear migration notes.

### M11 — Health telemetry polls every 15s unconditionally
**File:** `frontend/src/app/page.tsx:256`  
Hammers backend even when window is hidden/minimized. Should pause on `document.visibilityState === 'hidden'`.

### M11b - Security telemetry should ride the health watcher
**File:** `frontend/src-tauri/src/ipc_health.rs`, `frontend/src/lib/api.ts`  
The health telemetry loop already polls local operational state. Add a companion `get_security_telemetry` IPC command for passive local security signals: exposed listeners, risky AI/ASGI package versions, Docker published ports, generated executable/script churn, blocked secret files, and suspicious generated file patterns. Roadmap: `docs/IDE_SECURITY_MONITOR_ROADMAP_2026-05-27.md`.

### M12 — `SetupWizard.tsx` uses `require()` not dynamic import
**File:** `frontend/src/components/SetupWizard.tsx:27-31`  
Synchronous `require()` bundled at build time instead of `await import()`. Pulls full Tauri dep into bundle unconditionally.

### M13 — Collection detection returns "general" even if collection doesn't exist in DB
**File:** `frontend/src-tauri/src/orchestrator/rag.rs:33-58`  
Fallback collection "general" may not be created if user hasn't harvested any docs. Query silently returns empty.

### M14 — `agents/` directory exists but contains only modelfiles, no Rust implementation
**File:** `frontend/src-tauri/src/agents/`  
Misleading directory name. Either implement agent abstractions here or rename to `modelfiles/`.

### M15 — OOM exit code list incomplete
**File:** `frontend/src-tauri/src/ipc_hive/mod.rs:93-97`  
Missing Windows `STATUS_NO_MEMORY` (0xC0000017 = -1073741811). Stack overflow conflated with OOM.

### M16 — PendingTrainingPair asymmetric telemetry
**File:** `frontend/src-tauri/src/orchestrator/mod.rs:587`  
Training pairs only captured on compiler fail path, not Observer reject path. Flywheel missing a class of valuable training examples.

---

## 🟢 LOW

### L1 — Hardcoded `C:` drive fallback
**File:** `frontend/src-tauri/src/lib.rs:151`  
Breaks on D: drive, network mount, or non-standard system configs.

### L2 — Modal has no ESC key or outside-click dismiss
**Files:** `frontend/src/components/modals/AddModelModal.tsx`, `ServiceLoginModal.tsx`  
Modals can get stuck open with no keyboard escape.

### L3 — DEFAULT_ROLES hardcoded to model names
**File:** `frontend/src/lib/api.ts:380`  
`"determinex/planner-7b"` etc. If models are renamed, UI breaks without code change.

### L4 — `vanguard_state.rs` uses `Ordering::SeqCst` where `Acquire/Release` would suffice
**File:** `frontend/src-tauri/src/vanguard_state.rs:33-34`  
Functionally correct but unnecessarily expensive memory ordering for a single boolean flag.

### L5 — `workspace_search.rs` secret file blocking is silent to user
**File:** `frontend/src-tauri/src/workspace_search.rs:106-115`  
`.env` and credential files blocked from indexing (correct), but user gets no feedback that their file was blocked. They think it was indexed.

### L6 — Missing React.memo/useMemo on ModelSelectorDropdown model tier calculation
**File:** `frontend/src/components/ModelSelectorDropdown.tsx`  
`modelTiers.forEach()` runs on every render including keystrokes. With 100+ models this is noticeable.

### L7 — No loading state on ConceptLab and RoleAssignmentPanel async ops
Users can't tell if the app is frozen or waiting during generation.

### L8 — Inconsistent error handling strategy in api.ts
Some functions return `null` on `!isTauri()`, others return empty objects `{ threads: [] }`. Callers must null-check some but not others. No documented contract.

### L9 — Window-global `refreshRegistry` side effect
**File:** `frontend/src/app/page.tsx:235`  
`(window as any).refreshRegistry = refreshRegistry` — exposes internal state function to global scope. Race condition risk if called from devtools console.

### L10 — `diagnose_workspace` and `fix_workspace` Rust commands implemented but frontend never calls them
Users have no way to trigger workspace diagnosis/fix from the IDE. Feature exists in Rust, invisible in UI.

### L11 — Regex compilation with `.unwrap()` at startup
**File:** `frontend/src-tauri/src/ast_editor.rs` (multiple locations)  
`Regex::new(...).unwrap()` at module init time. Panics at startup if regex is malformed. Low risk since these are static strings, but should use `once_cell::sync::Lazy`.

### L12 — No `BenchmarkRunner` error type differentiation
Script missing vs process crash vs timeout all produce the same generic "error" state. No actionable guidance for user.

---

## IPC CONTRACT MISMATCH SUMMARY

### Frontend calls command with no Rust implementation
None found — all invoked commands exist in Rust.

### Rust commands never invoked from frontend (9 total)
`orchestrate_codegen`, `orchestrate_audit`, `converse_idea`, `discover_idea`, `refine_spec`, `explore_workspace`, `diagnose_workspace`, `fix_workspace`, `start_session`

### api.ts wrappers that frontend bypasses (uses invokeSafe directly instead)
`createHiveSession()`, `generateHiveDag()`

---

## SCRIPTS PYTHON AUDIT

### Orphaned scripts (defined, never called from pipeline)
- `scripts/fine_tuning/train_observer.py`
- `scripts/fine_tuning/forge_watcher.py`
- `scripts/archive/*.py` (7 files with underscore prefix)
- `scripts/rosetta_recall_eval.py` vs `rosetta_vs_text_eval.py` (duplicates)
- `scripts/micro_eval.py` vs `scripts/micro_eval_extra.py` (duplicates)

### Dead abstractions
- `scripts/providers/` — PROVIDER_MAP defined, main pipeline never calls it
- `scripts/validators/` — VALIDATOR_MAP defined, main pipeline never calls it

### Hardcoded paths
- `scripts/swe_agent/rag.py:26-28` — assumes monorepo structure
- `scripts/determinex_benchmark.py:40-41` — absolute `_MICRO_DIR` path
- `scripts/merge_adapter.py:7-8` — Windows path separators as strings

### Structural
- `scripts/hive/executor.py` — 1943 lines, needs splitting
- `scripts/fine_tuning/` — missing `__init__.py`
- `scripts/swe_agent/__init__.py` — exports nothing; should re-export key symbols

---

## QUICK WIN PRIORITY LIST (fix in order)

1. Fix `readHiveWorkspaceFile()` payload shape — **it's broken right now**
2. Fix ServiceLoginModal service name mangling — **keys not saving**
3. Replace 8 silent `.catch(() => {})` with error toast system
4. Fix regex salvage confidence → should not force 0.0
5. Fix prompt truncation to respect token/character boundaries, not raw bytes
6. Add `[LOG TRUNCATED]` marker when ring buffer overflows
7. Wire `check_child_exit_for_oom()` into session exit path or delete it
8. Single `isTauri()` utility replacing 5 patterns
9. Standardize all env vars to `DETERMINEX_*` prefix
10. Expose `drain_all()` as IPC command or delete it
11. Remove 4 dead api.ts functions
12. Remove or implement 9 unused Rust IPC commands
13. Pause health telemetry poll when window hidden
14. Fix DB init `.expect()` to graceful degrade
15. Add ESC key dismiss to all modals

---

*Audit complete. Return here to work through the list.*
