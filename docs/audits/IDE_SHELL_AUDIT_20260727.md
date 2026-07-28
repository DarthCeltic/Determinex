# Determinex IDE — Shell & Wiring Audit (2026-07-27)

Single authoritative list. Supersedes the ad-hoc lists in chat. Nothing here is
dropped until it is done or explicitly killed — including items carried over
from earlier in the session that are **not** regressions and still need an
owner decision.

Status key: **OPEN** · **DONE** · **NEEDS RYAN** (blocked on a decision or a
credential only Ryan can supply).

---

## Issue 1 — `invokeSafe` is safe for reads and dangerous for writes

**Status: rule established, 6 call sites fixed, NOT yet mechanically enforced.**

`invokeSafe` returns `null` on failure and never throws. Every Tauri command
that returns `Result<(), String>` *also* resolves to `null` on success. So for
any write, **success and failure are the same value**, and `try/catch` around it
is dead code.

This single mistake produced every one of these, all found live today:

| Where | Consequence |
|---|---|
| `EditorPanel.handleSave` | Failed save cleared `dirty` → **silent data loss** |
| `SettingsContext.setNetworkPolicy` | UI claimed "Offline" while egress was open → **false privacy assurance** |
| `gitService` (10 writes) | Failed commit/push/stage looked identical to success |
| `GitPanel` catch blocks | `setError("Commit failed")` was **unreachable** |
| `DiffReviewPanel` apply/reject | Refused apply looked inert, invited re-clicking |
| `VerifiedSearch` stage | Reported "refused" for a stage that **had** succeeded (null == ok) |
| `cloneRepo`, `resolveConflict` | Silently no-op'd for their entire lifetime (pre-existing, documented in-file) |

**The rule:** reads may use `invokeSafe`. **Writes must use raw `invoke`** so a
rejection propagates, and the caller must surface it.

**Remaining work (OPEN):** make it mechanical, not cultural. Two options, both
cheap:
1. A custom ESLint rule banning `invokeSafe("<cmd>")` where `<cmd>` is in a
   generated list of void/mutating commands.
2. Better — `tauri-specta` (see OSS §A1) generates typed wrappers from the Rust
   command signatures, so a void command's TS type makes the mistake
   unrepresentable *and* catches nonexistent commands at compile time.

Until then this rule lives here and in the code comments at each fixed site.

---

## Fixed today (regression-guarded)

| # | Item | Guard |
|---|---|---|
| 2 | Verified Search called `verified_search`, a command that never existed | 5 tests |
| 3 | Rail silently clipped Learn/Surfaces/Tools (`overflow-y-auto` + `no-scrollbar`) | live-verified |
| 4 | Addon dropdown hid 6 entries incl. Review; Quick Attach hid its tail | — |
| 5 | Advisor pill: permanent `z-50` box over content, no dismiss, duplicated rail GUIDE | — |
| 6 | Multichat portaled to `document.body` at `z-[999]` over every screen — now renders inside Work; the 6-condition suppress prop and 400ms position poll deleted with it | — |
| 7 | Router alias (`auto`) sent as an Ollama model tag → **every** verified build refused by default | 4 tests |
| 8 | `[vs]` progress lines on stdout corrupted the driver's JSON channel | 7 tests |
| 9 | 11 Rust bridges parsed Python stdout with zero tolerance | `python_json` + 7 tests |
| 10 | `git.rs` had **zero** tests despite shelling to real git | 9 real-git tests |
| 11 | Boot splash could hang forever (fake progress bar + unreachable `.catch`) | 4 tests |
| 12 | Editor save data loss / privacy false assurance / apply-inert | 7 tests |
| 13 | Source Control had no rail entry at all | — |
| 14 | Review queue had no producer (staging store's only writer was uncalled) | 5 tests |

Tests: **128 vitest** (from 86) · **43 Rust** (from 27).

### Two tests were protecting the bugs they appeared to cover
- `gitService.test.ts` simulated git in memory; its `vi.fn()` **threw** where the
  real `invokeSafe` **swallowed**, so it passed while production did the opposite.
- `SettingsContext.test.tsx` asserted "syncs through invokeSafe" — literally
  pinning the swallow in place.

Both rewritten. **Lesson: a mock that behaves better than production is worse
than no test.**

---

## OPEN — shell / UX (the current ask)

### 15. Sidebar clutter — 34 surfaces, no real organization
**Status: DONE.** 18-icon rail → 9 groups + `SurfaceDrawer`. Every surface has
exactly one home, enforced by `surfaceGroups.test.ts` (which parses the real
type unions out of `page.tsx`, so a new panel with no group fails the build).
That test immediately found and killed `ideation` — a 345-line surface nothing
could activate. Verified live.

There are **10 sidebars + 24 addon panels = 34 surfaces**, exposed through four
overlapping, inconsistent lists: an 18-item rail, a 20-item dropdown, a 17-item
Quick Attach, and the Tools hub. Same panel reachable 3 ways; some reachable 0
ways without scrolling a hidden-scrollbar menu.

**Target: 9 rail groups → expandable drawer.** Every one of the 34 surfaces maps
to exactly one group, so nothing is orphaned and nothing is listed twice:

| # | Group | Contains |
|---|---|---|
| 1 | **Work** | Work cockpit, Idea Lab, Project Hub |
| 2 | **Code** | Editor, Space/Explorer, Find in Files, Search |
| 3 | **Source** | Git, Review, Merge |
| 4 | **Run** | Terminal, Build, Runtime, Pipeline |
| 5 | **Prove** | Proof Center, Trace, Problems, Health |
| 6 | **Agents** | Repair, Coding Agents, Agent Chat, Passport |
| 7 | **Trust** | Audit, Repo Clinic, Maintenance Bay, Privacy Cockpit |
| 8 | **Learn** | Learning Studio, Product Surfaces, Brain/corpus, Guide |
| 9 | **System** | Tools/Extensions, Skin, Settings, Flywheel *(+ internal: Mission Control, Roadmap)* |

Drawer behaviour (per Ryan): clicking a group icon expands a panel listing its
members with **name + what it is + what it does**; the drawer is also a place to
show things that would not otherwise appear on the main screen; each entry can
be **sent to either main box** rather than having one hard-coded destination.

### 16. Layout is locked — panels cannot be moved, resized, or closed
**Status: DONE for Zone 1.** Drag handle on the right edge, width remembered
per surface (`usePanelWidth`), close already existed. Not
react-resizable-panels: Zone 1 is a framer-motion element whose inline
transform is rewritten every frame, and PanelGroup wants to own the same
element's sizing — so this follows the dock's proven drag+commit idiom instead.
Defaults unchanged, so nothing moves until the user drags.

**Zone 2 needs nothing** — correcting an earlier note here that called it "not
independently resizable". Zone 2 is `flex-1`, so it takes whatever Zone 1
leaves: dragging Zone 1's handle *is* the split control. It also already has
its own close button. Adding a second handle to a flex-1 element would be
inventing work, not unlocking anything. Both boxes are now
resize/close-capable.

Main regions use hard-coded widths (`w-[460px]`, `w-[760px]`, `w-[380px]`).
`react-resizable-panels` is **already a dependency and already imported in
`page.tsx` — and unused** (eslint flags `Panel`, `PanelGroup`,
`PanelResizeHandle` as unused vars). The unlock needs **no new dependency**.

The floating addon dock *is* already drag/resize/persist-capable
(`addonDockLiveRef` + `commitAddonLayout`) — that mechanism is the model to
extend to the two main boxes.

---

## OPEN — carried forward (explicitly not dropped)

### 17. Repair approval pipeline — **DONE.**
**Status: DONE.** Real patch generation (propose-only, snapshot+restore), real
oracle verdict, proposals staged into the Review queue so there is one
human-approved write path. The account below is kept because the failure mode
matters more than the fix.

I previously recorded this as a deliberate governance boundary awaiting
sign-off. That was wrong, and it was wrong in the most misleading possible
direction. Ryan: "so unblock it. i dont understand why its gated?" — the answer
is that there is nothing behind the gate to unblock.

What the "gated" commands actually return, in
`scripts/ide/backend_command_surface.py`:

```python
def _generate_patch_plan(...):   payload={"mode": "quarantine_only"}   # no patch
def _verify_temp_patch(self):    payload={"mode": "temp_only"}         # no verdict
def _source_apply_dry_run(...):  payload={"source_mutation": "BLOCKED_PENDING_REAL_HUMAN_APPROVAL"}
```

No patch is generated. No verification is performed. The apply step reports a
gate record for a patch that was never produced. The panels then describe this
as `BLOCKED_PENDING_HUMAN_APPROVAL` and
`REAL_APPROVAL_APPLY_POST_VERIFY_TRACE_LOCK_001`, which reads as "a working
capability held back for safety" when the accurate description is "not built".

**This is the exact failure mode the product exists to prevent.** Determinex's
whole claim is that a verdict must be earned. Safety-shaped language in front of
an unimplemented feature is an unearned claim about the system's own behaviour,
and it is worse than an empty panel because it actively discourages anyone from
looking closer. It is also self-inflicted: a reader (me, this morning) took the
gate at face value and filed it as governance rather than as missing work.

**A real patch engine already exists and is unused.**
`scripts/codebase_explorer.py` has `PatchPipeline.fix()` / `CodebaseExplorer.fix()`
which genuinely locate a bug, generate a patch, validate it, and revert on
failure. `repair_diagnose` is real too — verified live producing correct
CODE-blame. Only the middle of the flow is hollow.

**The unblock (scoped, not speculative):**
1. `_generate_patch_plan` calls the real `PatchPipeline` instead of returning
   `quarantine_only`, and returns the actual diff plus per-file
   original/proposed content.
2. `_verify_temp_patch` returns the real oracle verdict for that patch.
3. The approved patch is staged into the **existing** Review queue via
   `stage_diff_for_review`, so the human approval step and the workspace
   boundary check are the ones already built and tested today — no second
   source-mutation path.

Until step 1 lands, the honest fix is to stop calling it a gate.

### 18. OutputPanel / CICDPanel — **NEEDS RYAN** (product decision)
Both honestly labelled and permanently empty. OutputPanel needs a session
picker (`stream_session_log` emits per-session `hive-log-<id>`); CICD needs a
provider choice. Neither is a bug; both are unbuilt features.

### 19. EnvManager — **DONE.** Masked listing, one-key reveal, read-only.
Original entry kept below for the reasoning; the hedge in it was wrong.

#### (original) EnvManager — secrets call
No backend, local-only, non-persistent. Wiring it means reading/writing `.env`.
Repo policy forbids printing/committing secrets and the auto-mode classifier
hard-blocks `.env` writes. Safe version = read-only, masked, reveal-on-click.
**Ryan decides whether it exists at all.**

### 20. OAuth — **DONE.** GitHub Device Flow, real client id, token stored
server-side in the existing GITHUB_TOKEN row.

#### (original) OAuth — credential
No OAuth anywhere; GitHub/HuggingFace are PAT paste-in. GitHub Device Flow is
the right pattern (no client secret) but needs Ryan to register an OAuth App
(~5 min, one-time). HuggingFace desktop OAuth support is **unconfirmed** —
verify before assuming.

### 21. Sidecar — **DONE.** Provisioned and verified (llama_cpp OK, numpy OK).
Root cause was a pin to llama-cpp-python 0.3.4, which was never published, so
pip fell back to a source build. Now 0.3.34.

#### (original) Sidecar — provisioning
`bundler/sidecar/` is not provisioned, so all 5 sidecar commands are unreachable.
Paths are correct by design; `python bundler/setup_sidecar.py` creates it. The
error message is already honest.

### 22. Nothing pushed to any remote
Every commit this session is **local only**. Dev repo is ~9.7 GiB and must never
be force-pushed; `DarthCeltic/Determinex` is a curated ~30 MB mirror. Pushing is
Ryan's call.

---

## OSS / tooling gaps

`docs/architecture/OSS_TOOLING_QUEUE.md` already tracks 9 candidates (tree-sitter
and SQLite FTS5 **done**; mutation testing, constrained decoding, ast-grep, DSPy,
property testing, cargo-fuzz, difftastic outstanding). Those stand. Below are
**additions specific to the IDE shell**, which that queue does not cover.

### A1. `tauri-specta` + `specta` — **highest leverage item in this document**
Generates TypeScript types and typed `invoke` wrappers directly from the Rust
`#[tauri::command]` signatures. It would have made **four separate classes of
today's bugs impossible at compile time**:
- `verified_search` (command doesn't exist) → compile error, not a runtime null
- camelCase/snake_case arg mismatches (`remote_url`, `resolvedContent` — both
  shipped broken and silently no-op'd for their whole lifetime)
- void-vs-value return confusion → Issue 1 becomes unrepresentable in the types
- struct field shape drift (`StagedDiff`'s `rename_all = "camelCase"`)

Nothing else on any list prevents as much recurrence per hour spent.

### A2. Playwright E2E in CI
`@playwright/test` is already a dependency with **no suite**. Every UI
verification today was manual screenshot-driven. Even a handful of smoke specs
(boot completes, each of the 9 groups opens, save surfaces an error) would have
caught the clipped rail and the hung splash automatically.

### A3. `knip` (or `ts-prune`) — dead surface detection
Directly targets Ryan's "a whole list of things that do nothing." Finds unused
exports, unreachable components, orphaned panels. The 74 archived
ide-product-shell panels were found by hand; this finds the next batch for free.

### A4. Custom ESLint rule for Issue 1
Ban `invokeSafe` for known-mutating commands. Small, repo-specific, and it makes
today's most expensive rule self-enforcing. Pairs with A1 (or is redundant if A1
lands).

### A5. `dependency-cruiser` / `madge`
Import-graph rules — e.g. forbid components importing `@tauri-apps/api/core`
directly outside `lib/`, keeping the transport policy in one place.

### A6. `axe-core` / `eslint-plugin-jsx-a11y`
No accessibility checking exists. The rail is icon-only with 7px labels; several
controls are `<div onClick>` rather than `<button>` (not keyboard reachable).

**Suggested order: A1 → A2 → A3.** A1 prevents recurrence, A2 catches regressions
without a human driving screenshots, A3 shrinks the surface that needs either.

---

## Method note

Everything in the "Fixed today" table was found by **running the app**, not by
reading it. The wiring cross-check (125 frontend call targets vs 163 registered
handlers) found exactly one dead invoke; the other twelve were only visible in a
live session. Two of them were being actively concealed by passing tests.

Corollary for whoever picks this up: **a green suite here is weak evidence.**
Prefer A1/A2 over more unit tests against mocks.
