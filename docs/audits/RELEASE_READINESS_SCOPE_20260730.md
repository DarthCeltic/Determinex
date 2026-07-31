# Release readiness — full scope, 2026-07-30

Consolidates every defect found in the 2026-07-29/30 sweep: my own hunting plus four
independent audits (release/installer security, guards-that-cannot-fail, frontend/IPC honesty,
oracle/engine soundness). Companion to
[`USER_FACING_AUDIT_20260729.md`](USER_FACING_AUDIT_20260729.md), which holds the narrative for
items 1–11 there.

**Status vocabulary.** `FIXED` = changed and verified by running it. `FIXED (untested path)` =
changed, correct by construction, but its runtime path was not exercised. `SCOPED` = confirmed
defect, not yet fixed, with the fix identified. `OWNER` = needs a decision or a purchase only
Ryan can make.

Every `CONFIRMED` item below was traced in code, and most were reproduced by execution. Where an
audit reported something as SUSPECTED it is marked as such rather than promoted.

---

## S10 — NEW, found 2026-07-30 21:00: both lock files installed CVE versions the remediation had fixed

Found by fixing `verify_lockfiles`' verdict line, which had been printing a bare `PASS` while omitting
60 MEDIUM findings. Reading what those 60 actually were led here.

They are `>=` **security floors**, most carrying the advisory they close (`aiohttp>=3.14.1  # 11 CVEs`,
`torch>=2.13.0  # CVE-2025-3000`, `pyasn1>=0.6.4  # PYSEC-2026-3455/6/7`). **Converting them to `==`
would have been the wrong fix** — it freezes each package at today's version so future CVE fixes never
arrive. The correct model is floors in `requirements.txt` plus pins in a lock file, which this repo
already has. So the question became: do the lock files honour the floors?

**They did not. 10 packages were pinned below their declared floor.**

| Lock | Package | Pinned | Floor | Why the floor exists |
| --- | --- | --- | --- | --- |
| `requirements-lock.txt` | cryptography | 43.0.3 | 48.0.1 | GHSA-537c-gmf6-5ccf |
| `requirements-lock.txt` | torch | 2.5.1 | 2.13.0 | CVE-2025-3000 memory corruption + PYSEC-2025-194 |
| `requirements-lock.txt` | litellm | 1.52.3 | 1.84.0 | — |
| `uv.lock` | aiohttp | 3.13.5 | 3.14.1 | 11 CVEs incl. CVE-2026-54273..80 |
| `uv.lock` | cryptography | 48.0.0 | 48.0.1 | GHSA-537c-gmf6-5ccf |
| `uv.lock` | torch | 2.12.0 | 2.13.0 | CVE-2025-3000 |
| `uv.lock` | pyasn1 | 0.6.3 | 0.6.4 | PYSEC-2026-3455/6/7 — its own comment says "pinned explicitly to stop drift" |
| `uv.lock` | pillow / setuptools / httplib2 | | | |

`requirements-lock.txt` is the worse of the two: its header said *"For production: pip install -r
requirements-lock.txt (pinned, bit-for-bit reproducible)"*, so **the documented production install
path installed known-vulnerable cryptography and torch.** Two sources of truth for the same versions,
nothing comparing them, and the security-relevant one silently losing. CI was safe only by accident —
it installs from `requirements.txt` — but `[tool.uv.workspace]` is configured, so `uv sync` resolves
from `uv.lock`.

**A second, separate defect in the same file:** it pins 19 of the 50 dependencies `requirements.txt`
declares. The 31 missing include `aiohttp`, `mcp`, `pillow`, `pyasn1`, `pygments`, `setuptools` and
`urllib3` — largely the CVE-remediation additions. So "reproducible" also meant "missing 31 packages".

**FIXED.**
* `requirements-lock.txt`: the three stale pins updated to versions verified installed and working
  here (cryptography 49.0.0, torch 2.13.0, litellm 1.86.2 — full suite passes against them). Its
  header no longer claims completeness or production-readiness it does not have, and states the exact
  regeneration command.
* `uv.lock`: fixed properly with `uv lock --upgrade-package` for exactly the 7, rather than a blanket
  `--upgrade` days before release. All 7 now at or above floor. The resolve also added six declared
  but never-locked `tree-sitter-*` packages, so the lock is more complete as well.
* `verify_lockfiles.check_lock_floor_conflicts` now reports any lock pinning below a declared floor as
  **HIGH**, which blocks (`passed` requires critical and high to be zero). Deliberately harsher than
  the unpinned-specifier findings, which stay advisory because a `>=` floor is a considered choice.
  Violations quote the floor's justifying comment, so they say which advisory regresses.

**Still open (owner, needs network):** closing the 19-of-50 coverage gap needs
`pip-compile requirements.txt`, because 16 of the declared dependencies are not installed locally and
inventing versions for them would be precisely the unverified claim this repo refuses.

Guarded by `tests/security/test_verify_lockfiles_fail_closed.py` (6 tests) — including that the
conflict check stays HIGH, since a MEDIUM would be recorded and ignored.

---

## S0 — Ship-blocking

| # | Defect | Status |
| --- | --- | --- |
| S0.1 | **The secret scanner had never scanned anything.** Its patterns are PCRE (`sk-(?:proj-)?…`, `\b`), but it invoked `git grep -lE`; POSIX ERE rejects `(?:`, so git exited 128 *every time*. `_git`'s `except Exception: return ""` swallowed that, so `scan_tracked()` returned `{}` and the tool printed `clean -- no secrets in tracked files` and exited 0. The failure path and the clean path were byte-identical. | **FIXED** — switched to `-lP` with a `git ls-files` + Python fallback; verified it now finds real matches |
| S0.2 | **A failed scan read as a clean scan.** Any git failure — missing git, bad `--root`, the 180 s timeout on this ~10 GB history — produced "clean", exit 0. | **FIXED** — `GitUnavailable` raised; verdict becomes `UNKNOWN`, exit 2. Verified from a non-git dir |
| S0.3 | **The last gate before a public push scanned the wrong tree.** `publish_mirror.secret_scan` passes `cwd=<staging dir>`, but `secret_scan.REPO` is derived from `__file__` and `_git` hardcoded `cwd=REPO`. Every publish so far scanned the developer checkout, never the staged mirror. | **FIXED** — `--root` plumbed through; `publish_mirror` now passes it and refuses to publish unless the scanner reports the mirror path |
| S0.4 | **The scanner claimed to check pushed history when it never did.** The verdict line `OK: no secret in tracked files or pushed history.` printed unconditionally, and that exact string is pasted into `legal_public_distribution_20260712T234913Z.json` as proof — whose own `pushed_secret_scan` field is `false`. | **FIXED** — verdict now states only what ran, and says plainly when history was not scanned |
| S0.5 | **`crypto` and `testdata` exempted 5,337 files.** Bare substrings matched anywhere in a path, `re.I`. | **FIXED** — anchored to whole path segments |
| S0.6 | **Content-level entries in the false-positive list were dead.** `AKIAIOSFODNN7EXAMPLE` was listed, but the regex is applied to the *path*, so it never suppressed anything. | **FIXED** — separate exact-value placeholder allowlist applied to matched text |
| S0.7 | **173 Tauri commands are exempt from the ACL.** No `src-tauri/permissions/` and no `__app-acl__` in `gen/schemas/acl-manifests.json`, so `has_app_acl_manifest` is false and Tauri ACL-checks nothing for app commands. The `windows: [...]` list governs only `core:*`/plugin commands, and `"ide-repair"`/`"proof-center"` are Next.js *routes*, not window labels. | **SCOPED** — add `src-tauri/permissions/` + per-window capability. Needs the app run to verify; not landing blind |
| S0.8 | **The workspace boundary is `C:\`.** `lib.rs` sets `WorkspaceRoot` to `SystemDrive`, so every `is_safe_path` check asserts only "somewhere on C:". `reveal_env_var(workspace, key)` therefore returns cleartext from **this repo's live `.env`**. `get_lsp_symbols` has no boundary check at all. | **SCOPED** — needs a separate, tighter secrets boundary; the browser root is a deliberate product choice and must not simply be narrowed |
| S0.9 | **Command injection, in the process holding the updater signing key.** `_authenticode_status` passes the path as a trailing argv element after `-Command`; PowerShell rejoins and re-parses. Proven: a path containing `; Write-Output X` **executed X**, rc=0. `build_release_package.ps1` sets `TAURI_SIGNING_PRIVATE_KEY` to the key content in the same process that later invokes this. | **FIXED** — env-var pattern; injection probe now returns `not_checked` and spaced paths resolve, both verified |
| S0.10 | **The updater signing key is handed to two mutable third-party refs.** `tauri-apps/tauri-action@v0` (floating tag) and `dtolnay/rust-toolchain@stable` (force-pushed branch) in the job that holds `TAURI_SIGNING_PRIVATE_KEY` with `contents: write`. Compromise signs archives every installed client accepts. | **FIXED** — all 13 references across 5 workflows pinned to commit SHAs, with the ref kept as a trailing comment; guarded by tests/test_workflow_hygiene.py |

## S1 — Gates that cannot fail

| # | Defect | Status |
| --- | --- | --- |
| S1.1 | `first_e2e` green on evidence 3 weeks older than the code; one transcript held it across the rename, the updater, and the period the app could not launch. | **FIXED** — freshness binding to the download manifest |
| S1.2 | `status.endswith("PASSED")` accepted `"NOT_PASSED"`. First fix was itself insufficient — it still accepted `BYPASSED` (the word contains "PASSED"), `UNVERIFIED_PASSED`, `PARTIALLY_PASSED`, `MOCK_SUCCESS`, `SIMULATED_SUCCESS`, `STUBBED_SUCCESS`. | **FIXED** — whole-token boundary + qualifier denylist; all forms verified rejected |
| S1.3 | SBOM gate never checked the SBOM describes what ships. npm SBOM was 2 weeks stale and omitted `plugin-dialog`, `plugin-process`, `plugin-updater`. | **FIXED** — direct-dependency coverage binding, with a scoped-package test so it cannot false-positive |
| S1.4 | **`verify_lockfiles` cannot fail.** `passed = critical_count == 0`, but no code path ever emits `CRITICAL` — only `HIGH` and `MEDIUM`. Measured: 60 violations, `critical_count: 0`, `passed: True`. Documented checks 2 and 3 are unimplemented. | **FIXED** — HIGH now blocks, and bare unversioned deps are detected (proven in both directions) |
| S1.5 | **`license_scan` examines exactly one path: the repo root.** `paths` defaults to `[ROOT]`; the single row is the repo's own AGPL LICENSE, which `security_gate` then explicitly exempts. **No dependency license has ever been checked** — on an AGPL release. | **FIXED** — now scans 174 real dependency surfaces (was 1); reads dist-info METADATA; PyInstaller's bootloader exception documented in the artifact, not silently applied |
| S1.6 | **`windows_msi` gate is satisfied by a file existing.** `package_download_bundle` writes `wix_toolset_used/msi_built/msi_sha256_verified/msi_installer_smoke_performed` as unconditional literals whenever any `.msi` is found, and the gate checks exactly those four. Its own sibling field says `msi_smoke_scope: "artifact_discovery_copy_checksum_and_bundle_manifest"`. | **FIXED** — the four literals are now derived; smoke attestation moved to the clean-host transcript, which actually installs |
| S1.7 | **`_latest_packet` lets an older *passing* packet outrank a newer *failing* one.** Returns the first *valid* candidate, continuing past an invalid newer one. Governs `windows_msi`, `windows_trust`, `legal_public_distribution`, `extension_compat`. | **FIXED** — the newest packet decides; an older passing one is history, not fallback |
| S1.8 | `legal_public_distribution` passes on a 17-day-old hand-written packet with no freshness or commit binding. | **FIXED** — freshness binding added; the stale packet's secret-scan attestation came from a scanner now known never to have scanned |
| S1.9 | **An unsigned installer does not block `release_ready`.** `windows_trust` returns `deferred` on failure *and* when absent, and `release_ready = all(status in {passed, deferred})`. | **OWNER** — needs a cert; the gate should arguably block rather than defer |
| S1.10 | `full_release_closure` decides its verdict with `not any("mismatch" in b for b in blockers)`, so a corrupt zip, a missing artifact, and an illegal `release_ready` claim all report `passed_with_release_blockers`. | **FIXED** — integrity blockers separated from inherited readiness blockers |
| S1.11 | **`pb_override_scan --guard` cannot fail.** Blocking set is built from `official_full_suite_resolved`, which is `false` for all 210 board entries post-retraction. Lists ~50 violations then prints `GUARD PASSED`. | **FIXED** — reports GUARD VACUOUS and discloses the 3 locked archives with overrides |
| S1.12 | **`container_scan` returns `True` unconditionally** and reports `0 images` as PASS when Docker is absent. Labelled advisory, so partially honest. | **FIXED** — a scan that could not run no longer renders as `0 images` PASS |
| S1.13 | **23 evidence-signature families fall back to a hardcoded key published in the source.** None of the 23 env vars is set or documented anywhere, so the literal is the live path, making `verify_*` `hmac(k,x) == hmac(k,x)`. `corpus_manager.py` has the correct fail-closed design to copy. | **BOUNDED + DISCLOSED; key migration still deferred.** The crypto is unchanged, deliberately — the correct pattern exists in `corpus_manager._load_hmac_key` (ephemeral `os.urandom(32)` + loud warning), but adopting it invalidates every record already written across all 23 families and `root_cause_packet_gate` REJECTS on signature mismatch, so it turns today's green evidence red. It needs a `signing_key_source` field plus a re-sign pass (`scripts/corpus/resign_corpus_records.py` is the existing tool of that shape) — a migration, not an edit, and not one to attempt unattended before a public flip. Note a field cannot simply be added to the record either: `_signature` hashes the whole payload minus `_sig`, so any new field is itself invalidating. **What did land:** the finding "none of the 23 env vars is documented anywhere" is closed — all 23 are now tabulated in `docs/SECURITY_POSTURE.md` with the threat model, the `secrets.token_hex(32)` mitigation, and why the fix is a migration. And `tests/test_evidence_signing_key_hygiene.py` (5 tests) bounds the set: a 24th family cannot join silently, a migrated family must be struck from the list in the same change, the fail-closed reference cannot regress to a literal, and the doc table cannot drift from the code. Threat model unchanged and narrow: these sign local evidence in the developer's own checkout, the literals are not credentials, so it is integrity theatre rather than a leak — but it is now disclosed rather than silent. |
| S1.14 | `clean_host_kit` picks its manifest with `key=lambda p: p.name`, where every candidate is named `download_manifest.json` — so the sort is a no-op and it ships the **wrong installer** (`…20260707`, MSI sha `5377…`) while every gate reads `…20260729`. The documented path to satisfy the last gate cannot succeed. | **FIXED** — sorts by mtime, so the kit and the gates read the same manifest |
| S1.15 | Clean-host smoke: `proof_center_smoke_performed` is an ASCII grep of the exe, computed outside any launch check — it was `true` on the host where the app died in 1.8 s. `workspace_command_smoke_performed` is three `Test-Path` calls. `installer_sha256_verified` is set `true` with nothing compared when `-InstallerPath` is given. | **SCOPED** (the `-or` → `-and` and registry-path fixes already landed) |

## S2 — Oracle and engine soundness

| # | Defect | Status |
| --- | --- | --- |
| S2.1 | **Zero-leaf `amplified_solve` claimed "SOLVED all 0 leaves (oracle-verified)"** without calling the model or the oracle. `0 == 0`. | **FIXED** — verified with generate/verify functions that raise if called |
| S2.2 | **`_verify_typescript` passed an empty workspace**, and passed a workspace containing a real type error that shipped no tsconfig. The Python `compileall` bug relocated into the universal registry. | **FIXED** — fails closed; an existing test that asserted the "vacuous pass" was corrected rather than deleted |
| S2.3 | **A vacuous synthesized oracle is published as "oracle-verified".** With no examples and no typeable invariant, the whole oracle is `assert callable(f)`; `build_from_idea` returns `solved=True` with proof "PASSES all 1 synthesized checks". The `caveat` fires only for `oracle_proposed`, so the *weakest* oracle ships with no warning. | **FIXED** — synthesizer emits a vacuous-oracle marker and build_from_idea refuses to claim verification on it; discrimination verified both ways |
| S2.4 | **`run_correctness_tests` reports skips as PASS.** Five skip signals return `(True, signal)`, so the caller's `elif skip` is unreachable; those steps enter the trainset as `compiler_result=PASS, score=1.0`. Triggers include a missing harness, a non-rust/go/python language, a test timeout, a missing runner. | **SCOPED** — memory flags `executor.py` as locked; needs the limits test re-run |
| S2.5 | **`_compile_gate` returns PASS without compiling or testing**, and that PASS is what writes `"verified": true` into `auto_curriculum.jsonl`. Baseline failure, no Python sources, missing toolchain, any exception, or an unsupported language all yield `""` = pass. | **SCOPED** |
| S2.6 | **The only proof-based IMPOSSIBLE verdict is dead code.** `same_ctx` compares `p.test_id == f.test_id` over a list built by excluding that id, so it is always false. The reachable IMPOSSIBLE is a regex over skip messages, and `pb_certify_ceiling` writes "ALL proven IMPOSSIBLE / maximum attainable score" on the count alone. | **PARTIALLY FIXED** — the ceiling certifier now requires a `PROOF:` rationale, so an upstream-skip classification can no longer self-certify. The dead `same_ctx` branch in the adjudicator remains, documented |
| S2.7 | Test Validator declares SLOP from a whole-**file** tautology scan (one `assert True` anywhere marks every failing test in that file) and from traceback regexes (`/home/\w+/`, `\b20\d\d-\d\d-\d\d\b`) that match ordinary Linux tracebacks and any date. Dismisses real failures rather than claiming passes. | **SCOPED** |
| S2.8 | Model-patched code runs on the **host** outside Docker/hardened_runner (`make`, `cmake`, `mvn`, `gradlew`, `npx --yes`), and the execution-layer audit classifies that path as `HIVE_SANDBOXED_PATH` by prefix — so the audit is clean partly by assertion. | **SCOPED** |
| S2.9 | `UNVERIFIED:` tags survive only in `compiler_output`; `compiler_result` becomes plain `pass` and **no consumer greps the prefix**, so a lenient step counts as a normal pass in training-quality classification. | **SCOPED** |

## S3 — Product honesty (what a user sees)

| # | Defect | Status |
| --- | --- | --- |
| S3.1 | **Proof Center never calls its live command** — it checks `window.__TAURI__`, which this app never sets (`withGlobalTauri` unset). Two sibling files document this exact bug as already found and fixed; Proof Center was never brought in line. Inside the desktop app it renders "live read unavailable… open the desktop app". | **FIXED** — uses the canonical `isTauri()`; guarded repo-wide by tests/test_product_honesty.py |
| S3.2 | Proof Center release gates are hardcoded `"passed"` literals, including "Full test suite passes — 5,326 passed" (8 weeks stale, and CLAUDE.md says the monolithic suite is unclaimed), and a 31/31 100% progress bar beside its own text "0 release-ready families". This is the page headed "the single authoritative record". | **FIXED** — stale 5,326 literal removed; the 31/31 bar that rendered 100% beside "0 release-ready families" is now 0/1 |
| S3.3 | Wizard tells a brand-new user **"OpenRouter Free Tier — Already Configured ✓ / Your OPENROUTER_API_KEY is already in .env"** with no key check. Same class as the "Registering… swarm" defect, one screen earlier. | **FIXED** — driven by `get_api_key_status`; the unconditional "Already Configured" claim is gone |
| S3.4 | **Offline setup swallows init failure and reports "System Ready"**, and never calls `check_determinex_models` — so the model-gap panel added today never renders for an offline install. | **FIXED** — offline init failure now surfaces as an error, and both paths probe model coverage |
| S3.5 | **The model-readiness gate is entirely unwired.** `page.tsx` never passes `workReadiness` to `ConceptLab`, `evaluateWorkReadiness` is called nowhere, `get_work_readiness` is never invoked. "Missing local model coverage for N roles" can never appear. Corrects the existing audit, which said this *blocks* spec generation — it does not. | **SCOPED** |
| S3.6 | Verified Search hardcodes `oracle_sound` to `true` when `build` exists (the payload has no such field), so it can print "Sound — every check is type-safe" directly above a proof reading "oracle not sound". | **SCOPED** |
| S3.7 | Problems panel prints **"No problems detected / Real cargo check results"** when cargo never ran (spawn failure or timeout falls through `if let Ok`), and `.ts`/`.tsx` return empty by design. | **FIXED** — states the analysis scope instead of asserting "Real cargo check results" |
| S3.8 | Landing screen shows a green **"Working tree clean"** when `git_status` *failed*. | **SCOPED** |
| S3.9 | Marketplace asserts `cpp-oracle` and `docker` are **"installed"** as static literals; `_ORACLE_IMAGES` is `{rust, go, python, typescript}` and C/C++ fails closed. Oracle descriptions overstate what runs (Rust "cargo test" → `cargo build`; Python "pytest + mypy" → `compileall`+import+`unittest`). Uninstall of any seeded addon does not persist. | **FIXED** — cpp-oracle demoted to "available"; all four oracle descriptions corrected against validate_project; uninstall now persists |
| S3.10 | Project Hub ships three seeded cards with the developer's own paths (`C:\Dev\Determinex`, `T:\…`) plus static "lastOpened: Today" and proof state. | **SCOPED** |
| S3.11 | Pipeline view renders a green check on step 1 and a pulsing "Active" on step 2 with no session running. Maintenance Bay states `UPDATE_PROPOSED_QUARANTINED` and "impact plan present" unconditionally; Repo Clinic reports "analyzed" with no workspace open. "Brain Online" is a static pill beside telemetry that honestly says "NOT WIRED". | **SCOPED** |
| S3.12 | BigCodeBench scores 500 launched tasks against a denominator of 1140 → a perfect run displays 43.9%. Flywheel renders `0` with tooltip "Exact line count." on a failed read. Benchmark Stop logs "⚠ Stopped" before the kill is attempted. | **SCOPED** |
| S3.13 | Neither distributable conveyed the AGPL license; installer and `.vsix` both shipped without it. Cargo `repository` pointed at a nonexistent org. | **FIXED** |

## S4 — Tests that pin the bug instead of guarding it

`test_release_package_matrix_workflow` asserts `-TauriBundleTarget all`, which `build_release_package.ps1` documents as **invalid on Windows** — so the Windows half of the release matrix cannot complete, and fixing the workflow now breaks a test. Three safety tokens (`CORPUS_UNMUTATED`, `PATH_PORTABLE`, `SAFETY_DEFAULTS_RESPECTED`) are appended unconditionally then asserted as proof, beside two neighbours that *are* derived from real SHA-256 diffs. Five `*_final_state.py` modules compute `safe = all_closed and False is False and False is False`. 113 evidence tests assert only that a `run_*.json` exists without reading it; 31 assert booleans straight out of hand-authored lock JSON. `test_pip_audit_itself_is_installed` is a bare `importorskip` — it cannot fail, under exactly the condition it was written to catch. `test_proof_center_matches_eval_artifacts` skips in all CI (its eval dir is untracked). Symlink-escape tests monkeypatch `Path.resolve`, the call under test.

**Status: SCOPED.** The `-TauriBundleTarget all` one is ship-blocking for the release matrix and should go first.

## S5 — Open feature asks (not defects)

These are the items from "check multichat, chat surfaces, how the tools work… opt-in on data" that are **not** yet audited. Recording them so scope is explicit rather than implied:

1. **Chat / multichat surfaces** — **AUDITED 2026-07-30. One defect, fixed: chat was broken on every
   fresh install.**

   The surface itself is real and wired: 9 `agent_chat_*` commands registered, `ChatState` managed,
   `AgentChatPanel` mounted at `page.tsx:1953` behind a dynamic import, and genuine multi-session
   support (`agent_chat_list_sessions` / `create_session` / per-session `activeSessionId`).

   **The defect.** `agent_chat.rs::local_model_tag()` hardcoded a fallback of
   `qwen2.5-coder:14b-instruct-q4_K_M`, and `model_puller::required_models_for_budget()` **never
   installs that tag at any budget** — the source even says so: *"For now, skip it to save download
   time."* Two independent lists of model tags with nothing linking them. So a local chat
   participant with no explicit model override asked Ollama for a model that was never downloaded,
   and the first message of every fresh install 404'd.

   **Why no one saw it.** The repo `.env` sets `DETERMINEX_LOCAL_BUILDER_MODEL=…14b…` and the env
   var wins — and `.env` does not ship in the installer. So the bug was invisible on precisely the
   machines where it was developed. Same shape as the clean-host CRT failure.

   **Fixed at the root cause, not the symptom.** The default is now
   `model_puller::DEFAULT_LOCAL_CHAT_MODEL`, a `pub const` living beside the install list and used
   *by* it, so the two cannot drift again. A whitespace-only env var is also no longer allowed to
   resolve to an empty tag — that is the empty-model 404 this file already guarded against in
   `agent_chat_set_model`. Guarded by `agent_chat_default_model_is_always_installed`, which checks
   the floor budget deliberately: a tag present only on a big machine would still leave a low-spec
   install broken, which is the case that actually failed. Rust lib suite 82/82.

   **Verified NOT a bug while here:** the `!startsWith("citadel")` model filters in `SettingsModal`
   and `RoleAssignmentPanel` are correct and must stay as they are. They hide legacy pre-rename
   duplicate tags so the product does not appear to ship someone else's "Citadel"; renaming them to
   `determinex` would hide the real models and re-create the empty-picker failure.

   **Still untested:** an actual end-to-end multi-agent conversation in the packaged app, which
   needs a GUI run.
2. **Toolchain provisioning** — **RESOLVED 2026-07-30. Shipped set decided and the UI now matches.**

   Shipped set is the four the sandboxed oracle really runs: **Rust, Go, Python, TypeScript**
   (`_ORACLE_IMAGES`). Everything else fails closed, by design — CLAUDE.md's reasoning stands: the
   richer per-language oracles in `determinex_oracle.py` run a **direct host subprocess**, and buying
   verification by executing model-generated code outside the sandbox would trade a correctness gap
   for a security one.

   **The defect this exposed was worse than a stale label.** `MarketplacePanel.toggle()` only writes
   an addon id into `localStorage` — nothing is provisioned — and the card then rendered
   **"Installed"**. So clicking Install on `kotlin-oracle` told the user the Kotlin toolchain was
   present, and they would then meet the oracle's fail-closed refusal having just been told it was
   there. Exactly the LLM-card defect Ryan caught live ("supposedly installed? but not...") in a
   different category.

   Fixed with a `planned` flag on the three unwired oracles (`kotlin-oracle`, `swift-oracle`,
   `cpp-oracle`). A planned addon still appears — the roadmap is worth showing — but it cannot be
   toggled, cannot render as installed even if a stale `localStorage` id survives an upgrade, does not
   count toward the installed total, and its button reads **Planned** rather than Install. Kotlin and
   Swift descriptions were also present-tense ("gradle test. JVM oracle for Android…"), reading
   exactly like a working oracle; both now state that no sandboxed oracle ships yet and that the
   oracle fails closed for that language, matching the correction `cpp-oracle` already had.

   Guarded by `frontend/src/lib/__tests__/addons.planned.test.ts` (4 tests) pinning both directions:
   every oracle absent from `_ORACLE_IMAGES` must be `planned`, and no wired oracle may be — flagging
   a working oracle as planned would disable a real capability, which is the opposite failure.

   Verified: tsc clean, 319 frontend tests, 12 product-honesty guards.
3. **Upfront/preloaded links** — **AUDITED 2026-07-30. Eight URLs (not seven). No dead links.**

   | Status | URL |
   | --- | --- |
   | 200 | `aistudio.google.com/apikey`, `console.anthropic.com/settings/keys`, `console.groq.com/keys`, `openrouter.ai/keys`, `platform.moonshot.ai/console/api-keys` |
   | 302 → login | `console.mistral.ai/api-keys/` → `auth.mistral.ai/self-service/login/browser?return_to=…api-keys/` — correct, and it preserves the target path |
   | 403 JS challenge | `platform.deepseek.com/api_keys`, `platform.openai.com/api-keys` |

   The two 403s are bot protection, not missing pages: the status is 403 rather than 404 and the
   bodies are challenge pages. **Least certain:** OpenAI's challenge body also contains the string
   "404", which I could not attribute — it is most likely an asset reference in the challenge
   markup, and the documented public URL for OpenAI keys is exactly this one, but it is the single
   link worth confirming by eye in a browser.

   **Do not add a naive HTTP link-checker to CI for these.** Three of the eight would fail it while
   being perfectly correct, and a red check everyone learns to ignore is worse than no check. If
   these ever need automated coverage, the assertion has to be "not 404 and DNS resolves", not
   "200".
4. **On-the-fly edit → user** — **RESOLVED 2026-07-30.** The updater produces signed artifacts and
   the guarding test is green for the first time. Full write-up:
   **[`docs/release/UPDATER_ARTIFACTS.md`](../release/UPDATER_ARTIFACTS.md)**.

   **Root cause:** the bundler *silently* skips updater signing when
   `TAURI_SIGNING_PRIVATE_KEY_PASSWORD` is **undefined** — no error, no warning, both installers
   built, zero `.sig`. And on Windows an empty value cannot define it, because assigning `""`
   *deletes* the variable (`Test-Path Env:\X` False, `GetEnvironmentVariable` null, `cmd /c if
   defined X` UNDEFINED; .NET documents the same). So a **passwordless updater key can never be
   signed with on Windows**, and the failure mode is silence.

   **How it was proven rather than guessed** — a negative control needing no key change: set the
   password to a deliberately wrong *non-empty* value and rebuild. If the config were being ignored,
   nothing would change. Instead the bundler failed loudly with
   `failed to decode secret key: incorrect updater private key password`. That one result establishes
   that the bundler honours `createUpdaterArtifacts` and does attempt signing, and that the only
   difference between signing and doing nothing is whether the variable is defined. Every prior
   attempt reasoned from absence, which is why it survived several sessions.

   **Fixed** with a password-protected keypair (old passwordless key retained as `.passwordless.bak`),
   the new pubkey in `tauri.conf.json`, and a build script that now **throws** on a missing password
   instead of quietly shipping unsigned installers.

   **A test would have hidden the fix.** It demanded a `*.zip` as well as a `.sig`, so it would have
   stayed red even once the defect was gone. `createUpdaterArtifacts: true` emits installer + detached
   `.sig` and **no** archive; the zip is the legacy `"v1Compatible"` shape. I had mis-read the
   plugin's `#[cfg(windows)] impl Update` doc block — it lists what the updater can *consume*, not what
   the bundler *produces* — and recorded that wrong conclusion in this repo. Corrected in the test and
   the doc.

   **Owner action before publishing:** the pubkey is compiled into the app, so the currently staged
   installers embed the *old* key and cannot accept updates signed with the new one. Re-stage from the
   freshly signed installers, then re-run clean-host verification (re-staging moves the freshness
   anchor and correctly invalidates the existing evidence). Still unproven, and unprovable locally:
   the true end-to-end update, which needs a published release and two versions.

5. **Opt-in on data** — **AUDITED 2026-07-30. One finding, fixed.**
   * **Telemetry is correctly opt-in and needs nothing.** `vanguard_state.rs` defaults `enabled` to
     `false` via an `AtomicBool`, the user must turn it on from the UI, and the orchestrator reads
     `is_vanguard_enabled` *before* writing any training pair. Documented, atomic, no default-on
     path. This is the pattern the rest of the app should be judged against.
   * **The updater ignored the offline network policy — FIXED.** `UpdateNotice` scheduled its
     `check()` unconditionally 6 s after mount, so an install set to `offline` still made an
     outbound HTTPS request to github.com on every launch. The app ships an explicit
     `offline | cloaked | online` policy and `AiRouterContext` already refuses to route a cloud
     model under `offline`, so the updater was breaking a guarantee the rest of the product keeps —
     in a product whose entire position is local-first. The objection "it is only a version string"
     misses what was promised: the user asked for no network and something went to the network.
     Now gated on the policy, with `offline` also suppressing the rendered notice (otherwise a
     policy flip while a notice is displayed leaves an Install button that calls out anyway).
     `cloaked` deliberately still checks — it carries no repository identifiers, so suppressing it
     would cost those users their security fixes for no privacy gain. Guarded by
     `frontend/src/components/__tests__/UpdateNotice.offline.test.tsx` (4 tests), which pins both
     directions: a test that only asserted "offline blocks" would pass on a component that never
     checked at all.
   * **Egress traced 2026-07-30. Nothing to fix.** Every outbound endpoint the *installed app* can
     reach, enumerated from the Rust source rather than assumed:

     | Destination | When | Notes |
     | --- | --- | --- |
     | `localhost:11434` | model calls, health probe, VRAM unload on exit | local only |
     | `github.com/login/*` | user clicks Sign in | device flow; `github_open_verification` allowlists `https://github.com/` **only**, with tests rejecting `https://evil.example` and plain `http://` |
     | `ollama.com/download/…` | user opts into installing Ollama | setup, user-initiated |
     | GitHub releases | update check | now gated on the offline policy (see above) |
     | Provider APIs | a model call, once the user configures a key | gated by network policy |

     **No code uploads corpus writes, Cloak audit maps, or logs anywhere.** Cloak writes to
     `run_dir/cloak_audit/*.json` on disk; there is no `post`/`put`/`upload`/`boto3` path in
     `scripts/determinex_cloak/` or `corpus_manager.py`. The Hetzner sync is a separate,
     operator-initiated SSH tool, not something the app does.

   * **First-run disclosure exists and is prominent.** `SetupWizard` **step 1** is "Network & Privacy
     Policy", states "This controls what data leaves your …", and explains that Cloaked "means cloud
     calls are allowed only through privacy gates that obfuscate identifiers". The consent surface is
     the first thing a new user sees, not buried in settings.

---

## S8 — 2026-07-30 05:00-07:00: the two highest-severity items, closed

### S0.7 CLOSED — the Tauri app ACL is on, and proven not to brick IPC

`frontend/src-tauri/permissions/app-commands.toml` now declares one permission per registered
command plus an `allow-app-commands` set, referenced from `capabilities/default.json`. Its mere
existence is the mechanism: Tauri 2.10 only ACL-checks a command when
`plugin_command.is_some() || has_app_acl_manifest`, so with no `permissions/` directory **all 173
commands were reachable from any webview with no permission and no window restriction** — including
`run_terminal_command`, which shells to `powershell -ExecutionPolicy Bypass` with
`CREATE_NO_WINDOW`.

Turning an ACL on is not free: an omitted command is DENIED at runtime and the feature silently
stops working, which is invisible without launching the GUI. So this was verified **statically**
against the generated schema after codegen:

```
__app-acl__ present: True
permissions=173  permission_sets=1  distinct_allowed=173
registered=173   MISSING from ACL: 0   in ACL but not registered: 0
```

Two guards in `tests/test_tauri_acl.py`: the generated manifest must cover the registered set
(catches runtime denial), and the `.toml` must not drift from it (catches a forgotten permission on
a clean checkout, before any build).

What this buys, stated precisely: the surface is not narrower today (all 173 are allowed), but the
capability's `windows` list now actually applies to app commands, and a command added later is
denied by default instead of silently exposed.

**Also removed:** `shell:allow-execute` and `shell:allow-spawn`. Both were unscoped, and unscoped
shell in Tauri v2 fails closed (`tauri-plugin-shell` `scope.rs` returns `Error::NotFound` on a scope
miss); `@tauri-apps/plugin-shell` is not even a frontend dependency and nothing imports it. They
granted nothing and only made the capability read as though arbitrary shell execution were
permitted — the first thing an enterprise reviewer will find.

### S0.8 CLOSED — credential reads are scoped to the opened project, not the drive

`env_manager.rs`'s own docstring states the rule: *"never read outside the open workspace."* It was
not enforced. The only check was `is_safe_path(WorkspaceRoot, target)`, and `WorkspaceRoot` is the
system drive so the file browser can open a project anywhere — so the assertion was only "somewhere
on C:", and `reveal_env_var` would return cleartext from **any** `.env` on the drive, including this
repository's own.

Browsing broadly and reading credentials are different privileges, so they now have different roots.
A new `ProjectRoot` state holds the project the user actually opened, set by `set_project_root`,
which `page.tsx` calls from the same effect that reacts to `explorerRoot`. `list_env_vars` (key
names still describe someone's project) and `reveal_env_var` both consult it. `None` means no
project is open and credential reads are **refused outright** rather than falling back to the browse
root.

Verified by Rust unit tests, which run without a GUI — the escape it guards against is not
observable from the UI: no-project-open refuses; an `.env` inside the project is allowed; a
not-yet-created `.env` is allowed (the guard resolves the PARENT, so a missing file is not mistaken
for an escape); a sibling directory is refused; and `..` traversal out of the project is refused.

Coherence checked rather than assumed: `page.tsx` renders `<BuildCenter workspacePath={explorerRoot} />`
and `BuildCenter` passes that to `EnvManager`, so the value the panel sends is exactly the value
registered — the boundary permits it and the panel keeps working.

### Soundness: a skipped correctness suite is no longer recorded as a pass

`run_correctness_tests` returns `(True, <signal>)` for all five of its skip signals, and both call
sites in `hive/executor.py` tested the boolean first — so the `elif` skip branch was **unreachable**
and a step whose tests never ran was recorded as `correctness_result="pass"`. That fed the gamma
channel of the adjudication score (`tests_exist=True`) and the dspy trainset
(`compiler_result=PASS`, `score=1.0`) with a verification that had not happened. Triggers are
ordinary: a harness path the Builder never wrote, a language outside rust/go/python (TypeScript
included, which `validate_project` now genuinely verifies — so a whole TS session recorded every
step's tests as passing), a timeout, a missing runner.

The tuple being matched was also incomplete and used equality: `harness_read_error` was absent
entirely, and two signals append an exception message, so exact membership could never have matched
them even had the branch been reachable. Now checked first, by prefix, derived from `compiler.py`
rather than a copied list.

Skipped steps are also **excluded** from the monitor trainset rather than relabelled — letting them
fall through would emit `compiler_result="FAIL"`/`score=0.2`, teaching the monitor that correct code
is wrong, which is the mirror image of the bug rather than a fix for it.

### Product honesty, continued

* **S3.5 CLOSED** — the model-readiness gate is wired. `ConceptLab` always gated spec generation on
  `specGenerationBlockMessage(workReadiness)`, but `page.tsx` never passed the prop and that helper
  returns `null` for `undefined`, so the branch was dead in every build: the Work tab would generate
  a spec and launch a hive session on an install whose Builder and Monitor roles resolve to absent
  models, with no warning at all.
* **S3.12 CLOSED** — BigCodeBench's `defaultTotal` was 1140 while `args` launched `--n 500`, and
  score is `resolved / defaultTotal`, so a run that solved everything it attempted displayed 43.9%.
  The Stop button's `.catch` was dead code (`invokeSafe` never rejects) and its "Stopped" log ran
  before the promise settled; it now reports whether the kill was confirmed. The Flywheel rendered
  `0` under a tooltip reading "Exact line count." on a failed read; a failed read now renders `—`
  and says so.

## S9 — NEW, found 2026-07-30 08:00: a cold Docker makes the first build time out

Surfaced while re-validating the `executor.py` change against the hive limits test, which failed
twice with **0 retries** and step 1 left `pending` — never a compile failure, just never finishing.
The actual error, from the second run:

```
'... rust:1.82-slim sh -c "... cargo check"' timed out after 120 seconds.
Fix Docker or set DETERMINEX_REQUIRE_DOCKER=0 (reduces isolation).
```

`COMPILE_TIMEOUT = 60` and `_docker_oracle_run` passes `timeout + 60`, the extra 60 s commented as
"image pull / container start".

**Corrected 2026-07-30 09:40 — my first reading of this was wrong and the severity is lower.** I
originally measured a trivial `docker run ... 'echo ready'` at **19 s** and concluded the 120 s budget
was inherently marginal. That measurement was itself taken while Docker Desktop was still
initialising. Re-measured with the daemon genuinely warm, running the *exact* failing oracle command
against a hello-world crate:

```
docker run --rm --network=none -v /c/tmp/probe:/workspace -w /workspace \
  -e CARGO_TARGET_DIR=/tmp/cargo-target rust:1.82-slim sh -c 'cargo build --message-format short'
  → Finished dev profile in 1.02s   |   10 s wall clock   (budget: 120 s)
```

10 s against a 120 s budget is ample, not marginal. So the three consecutive failures were confined
to Docker Desktop's post-reboot warm-up window, and that window is transient and self-resolving — not
a standing defect. My "container start alone is 19 s" claim is contradicted by this measurement and
should not be relied on.

**What remains genuinely a product finding.** The 60 s overhead does not cover an **image pull**, and
that is exactly the first-run case: a new user's first build must fetch 808 MB of `rust:1.82-slim`
inside a budget sized for container start. That will time out on any normal connection, and the user's
first-ever spec fails with a message about fixing Docker. The compile itself runs `--network=none`, so
a no-dependency project never needs the crates index — the cost is the pull, nothing else.

The oracle's *behaviour* is correct throughout: it fails closed rather than reporting an unverified
pass, which is the doctrine working as designed. The defect is the budget, not the verdict.

**FIXED.** `_ensure_oracle_image(image, lang_key)` in `scripts/hive/compiler.py` now makes the image
local *before* the timed run, so provisioning is never charged to the compile budget. Three details
that were not obvious:

* **A pull failure raises, it does not return non-zero.** Had it returned an rc like a normal
  `docker run`, the caller would have recorded a registry outage or a dead network as a *compile
  error* — writing an environment problem into the WAL as though the generated code were wrong. For a
  system whose entire reward signal is "this failure was the code's fault", that is training-data
  corruption, not a cosmetic message bug.
* **`determinex-oracle-ts:20` is built locally and must never be pulled.** `docker pull` on it fails
  with "pull access denied", which reads as an auth problem and sends the operator looking for
  registry credentials that do not exist. The missing-image path consults `_ORACLE_IMAGE_HINT` and
  names the `docker build` command instead.
* **Presence is memoised per process** (`_IMAGES_PRESENT`), because the oracle runs once per step per
  attempt and `docker image inspect` on every compile is pure added latency.

The `timeout + 60` budget is unchanged and its comment now says what the 60 s actually covers
(container start and teardown, measured ~9 s of the 10 s warm total).

Guarded by `tests/test_oracle_image_provisioning.py` (7 tests). Mock-based deliberately: they assert
which docker verbs run and in what order, which a real-Docker test cannot observe, because a warm
machine never pulls and the regression would be invisible.

**Still open, deliberately:** pre-pulling during `SetupWizard`'s install phase would move the wait to
where a user expects one. Not done here — that is a UI change, and this fix already removes the
failure.

### S9b — the same investigation found the actual cause, and it is not the pull

Third re-run still failed, so I stopped inferring and ran the oracle directly against the hung
session's own workspace. It returned in **74.3 s** with a correct verdict:

```
Compiler Oracle: FAIL
src/main.rs:5:10: error[E0425]: cannot find function `exit` in module `env`: not found in `env`
```

Two things follow, and both matter more than the pull fix.

**The loop is functional and was never broken.** The 1.5 B builder wrote `env::exit(0)` — a real
mistake, `exit` lives in `std::process` — and the oracle caught it with a real rustc error, which is
the closed loop doing exactly its job. The apparent "hang" was the retry loop grinding through
attempts, each paying a full compile, until the level budget cut it off mid-flight. `retries: 0` in
the step file was **stale**: that file was last written at 04:30 and never updated again, so reading
it as "zero retries happened" was my error, not the system's.

**Docker compile latency on this Windows/WSL2 host is wildly variable, and that is the real defect.**
Three measurements of the *same* trivial hello-world compile, same image already local:

| When | Wall clock | Against `timeout + 60` = 180 s |
| --- | --- | --- |
| Warm probe | **10 s** | ample |
| Direct oracle call | **74 s** | fits, but 7× the warm figure |
| During the failing runs | **>180 s** | exceeded — reported as a Docker timeout |

`COMPILE_TIMEOUT = 60` is calibrated for a fast daemon. On this host a trivial compile intermittently
exceeds the whole 180 s budget, so the oracle reports a timeout instead of a verdict. It **fails
closed**, which is correct and is the doctrine holding — it never reports an unverified pass. But a
user whose first build takes 3 attempts × ~75 s sees a long unexplained wait, and one whose daemon is
having a bad minute sees "Fix Docker" for code that would have compiled.

**Not fixed here, deliberately.** Raising `COMPILE_TIMEOUT` trades a false timeout for a longer hang
on genuinely stuck builds, and picking the number needs latency data from more than one machine — a
single degraded Windows box is not a basis for changing the oracle's timing for everyone. What this
box justifies is recording the variance, not guessing a constant.

**The limits test itself never went green on this box, and I stopped re-running it.** Five attempts:
three hit the 120 s Docker timeout, one hit a 900 s level budget mid-retry-loop, one was cut off. Each
failure was environmental — Docker latency — not a verdict about the code, and a sixth run under the
same conditions would produce the same non-signal. It is also self-defeating to run it concurrently
with the test suite, because `container_scan` and the oracle then compete for the same daemon, which
is what produced the >180 s measurement above.

What replaced it as evidence is stronger for the question actually being asked. Running
`validate_project` directly against the failing session's workspace produced a **correct verdict with
real rustc output** in 74 s. That establishes the oracle path end to end — worktree, container, cargo,
error capture — which is what a green limits run would have established, minus the scheduling luck.
The `executor.py` correctness-skip change has its own unit test
(`tests/test_correctness_skip_is_not_a_pass.py`); it is not resting on the limits test.

So: the loop is confirmed working, and the limits test is confirmed *unreliable on a Windows/WSL2
Docker host* — which is itself S9b, and worth knowing before treating a red limits run as a code
regression.

**Status: S9 pull-budget FIXED and guarded. S9b latency variance CHARACTERISED, not fixed —
needs multi-host data. Compiler loop confirmed FUNCTIONAL by direct oracle run, not by the limits
test.**

## S7 — RESOLVED 2026-07-30 11:35: the installer works; the verification script looked in the wrong directory

Full write-up: [`docs/release/NSIS_SILENT_INSTALL.md`](../release/NSIS_SILENT_INSTALL.md).

> **CLOSED 2026-07-31 on a clean VM, and it found two more defects on the way out.** NSIS is now
> clean-host verified — install 0, launch survived 12 s with `vc_runtime_preinstalled: false`,
> uninstall 0, transcript validates. Two additions to the story below:
>
> * **A third reason the directory looked wrong: WOW64 redirection.** The NSIS stub is 32-bit
>   (`x86-unicode`) and this smoke runs as SYSTEM, so `%LOCALAPPDATA%` =
>   `…\system32\config\systemprofile\…` gets redirected to `SysWOW64` for the *files* while the HKCU
>   uninstall entry keeps the un-redirected path. Files and registry disagree, which reads exactly
>   like the original complaint. Artefact of installing as SYSTEM, not a product defect; the 64-bit
>   MSI is unaffected.
> * **S7.1 / S7.2 — two more checks that reported success without checking**, same shape as S7
>   itself: `installer_sha256_verified` was hardcoded `true` whenever there was nothing to compare
>   against (and the release gate *requires* that field to be true), and `-ManifestPath` defaulted to
>   a dated bundle directory six bundles stale, which is what made the first defect reachable. Both
>   fixed; the "newest download bundle" rule was written by hand in six places and is now one
>   function. Guarded by `tests/test_download_manifest_resolution.py` (14 tests).

**Correcting my own entry from 11:00 the same day.** I wrote that `$INSTDIR` was left as the relative
literal `placeholder\Determinex` so `SetOutPath` failed. **That was wrong.** The NSIS installer
installs correctly in every case, verified on a developer host:

| Invocation | Result |
| --- | --- |
| `/S`, remembered-location key cleared | installs to `%LOCALAPPDATA%\Determinex` — 11 files, all six CRT DLLs, `uninstall.exe` |
| `/S`, remembered location present | installs **there** (this is what fooled me) |
| `/S /D=<abs>` | installs to that path |
| `uninstall.exe /S` | removes the directory and the Add/Remove entry cleanly |

`$INSTDIR` with no `/D=` resolves from the remembered previous install location — the default value of
`HKCU:\SOFTWARE\<Publisher>\<ProductName>`, read by `RestorePreviousInstallLocation` — and only falls
back to `$LOCALAPPDATA\<ProductName>` when that key is absent. Ordinary NSIS behaviour.

**How the wrong conclusion happened, since it matters more than the bug:** I ran `/S`, checked
`%LOCALAPPDATA%\Determinex`, found nothing, and inferred nothing was installed — then "confirmed by
absence" that no `placeholder` directory existed, which was true and consistent with the wrong theory.
File timestamps settled it: `C:\tmp\determinex-smoke-install\uninstall.exe` was stamped 11:15, during
the runs I had recorded as installing nothing. **I made precisely the error the smoke script makes** —
checking a hardcoded guess instead of asking the installer where it went.

**The real defect, fixed:** `run_windows_clean_host_install_smoke.ps1` looked in the wrong places.

* `Find-InstalledExe` listed `C:\tmp\determinex-smoke-install\determinex.exe` **first** — a developer
  scratch path holding a 2026-07-21 binary, so a local run validated a **stale artifact**. Invisible to
  the gate, because a clean host lacks that path.
* The per-user candidate was `$LOCALAPPDATA\Programs\Determinex`, but the installer uses
  `$LOCALAPPDATA\Determinex` — no `Programs` segment. **This is what the clean-host run hit:** a correct
  install could never be found, which reads exactly like "installed nothing". Same mismatch in the
  uninstall path, which threw "not found under Program Files" while searching three other places.

**Gate consequence:** the recorded clean-host verdict is most likely a directory-lookup artifact, so a
re-run with the fixed script is expected to pass. **Not re-run** — that needs the VM, since a developer
host cannot reproduce the absent-VC++-runtime condition the gate exists to test. SETUP.md continues to
lead with the MSI meanwhile.

**An NSIS installer hook to repair `$INSTDIR` was written, built and tested. It changed nothing**,
because `$INSTDIR` is always absolute, and was removed rather than left in — dead code claiming to fix
a non-existent bug would misdirect the next reader.

Also disproved: WebView2 (present here, `pv 150.0.4078.105`), a silent `MessageBox` → `Quit` (both
unreachable), UAC (`currentUser` → `RequestExecutionLevel user`; a non-elevated shell is supported),
`/NCRC`, and a quoted `InstallLocation` poisoning the next install (nothing reads it back).

### Original report (2026-07-30 04:00)

Found by testing the second shipped installer on a clean host for the first time. Only the MSI had
ever been verified there.

On a pristine Windows 11 VM with no VC++ runtime, `Determinex_0.1.0_x64-setup.exe /S`:

* downloads with a matching sha256,
* **exits 0**,
* writes an uninstall registry entry whose `InstallLocation` is
  `C:\Windows\system32\config\systemprofile\AppData\Local\Determinex`,
* and **that directory does not exist.** No `determinex.exe` anywhere under Program Files,
  Program Files (x86), LOCALAPPDATA, ProgramData or C:\Users.

So the installer registers itself as installed and leaves nothing behind, while reporting success.
Note the path shape differs from the MSI's (`...\Local\Determinex`, with no `Programs` segment),
which is why the first search missed it and is worth knowing when scrubbing test hosts.

**Caveat stated deliberately:** this ran as SYSTEM through `az vm run-command`. The MSI installs and
launches fine in that same context, so session 0 is not inherently fatal — but NSIS per-user install
semantics may legitimately differ under SYSTEM in a way the MSI's per-machine install does not. So
this is CONFIRMED as "exits 0 having installed nothing when run as SYSTEM", and NOT yet confirmed
for a normal interactive user.

**Consequence for release.** The download bundle publishes this file as `windows_nsis_setup`, and
the release notes tell users to "Download the installer for your platform". Anyone taking the `.exe`
rather than the `.msi` may get a silent no-op. The MSI is verified end to end; until NSIS is
verified in an interactive session, the honest options are to publish the MSI only, or to test NSIS
with a real logged-on user first.

**Status: SCOPED.** Needs one interactive-session test to determine whether this is SYSTEM-specific
or a real product defect.

## S6 — Launch-reaction audit (the three-waves checklist), answered

Audited 2026-07-30 against the actual code, not against intent.

### A. CLA — **absent. Highest-leverage pre-public fix.**

`CONTRIBUTING.md` and `.github/PULL_REQUEST_TEMPLATE.md` exist. There is **no CLA, no DCO, and no
CLA bot or workflow** anywhere in `.github/`. Confirmed by direct search.

Why this one is urgent in a way the others are not: it is the only item on this entire list that
gets **harder after** the repo goes public, not easier. Today Ryan holds 100% of the copyright, so
dual licensing (AGPL for everyone / commercial for the Fortune-500 legal department that bans
AGPL) is a decision he can make unilaterally. The moment an external PR merges without a CLA or
DCO, that contributor's copyright is in the tree and re-licensing needs their agreement —
retroactively chasing sign-off, or reverting their work. Every merged PR raises the cost.

**Action:** add a CLA (CLA Assistant is the usual bot) or at minimum a DCO sign-off requirement,
*before* the repo is public. This is measured in minutes now and in lawyers later.

### B. Hardware auto-tuning and engine decoupling — **partial, and honestly so**

What exists and is genuinely good: `hardware.rs` probes dedicated VRAM via `nvidia-smi`,
`rocm-smi`, and `system_profiler`, subtracts a driver/context reserve, carries real timeouts, and
has a comment recording a live incident where a stuck `nvidia-smi` hung the async
`initialize_system`. `calculate_tier` maps the VRAM budget to model tier and `num_ctx`.

What the checklist asks for and is **not** there:
* **No CPU SIMD detection.** No AVX/AVX-512/NEON probe anywhere in the tree.
* **No GPU backend selection** (Metal/CUDA/Vulkan). This is defensible rather than missing:
  inference is delegated to **Ollama**, which does its own backend selection, so the IDE has no
  backend to choose. Worth stating explicitly instead of implying we tune it.
* **GPU layer offloading is not set** — again, Ollama's job.

**Engine decoupling: the inference engine is decoupled; the sidecar is not.** Ollama is a separate
process the app provisions, so a llama.cpp/GGUF-format advance arrives via Ollama with no
Determinex rebuild. But `determinex-hive.exe` — the 68 MB PyInstaller bundle that *is* the engine
logic — is baked into the installer, so a one-line Python fix requires a full rebuild and
reinstall. That is the coupling that will actually bite, and it is the same finding as S5.4.

### C. Hardened execution sandboxing — **confirmed gap, and worse than the checklist assumes**

The predicted attack (hostile repo → prompt-injected agent → shell on the host) is **live today**,
via two independent paths:

1. **S2.8** — `_run_compile_check` / `_run_target_tests` run `make`, `cmake`, `mvn`, `./gradlew`,
   `npx --yes`, `pytest`, `bundle exec` through raw `subprocess.run(cwd=worktree)` on a worktree
   **with the model's patch already applied**. No container, no `intake.hardened_runner`. `make`
   and `cmake` execute repo-controlled build logic with host privileges; `npx --yes` also fetches.
   Compounding it: `parallel_execution_layer_audit.py` classifies that path as
   `HIVE_SANDBOXED_PATH` **by path prefix**, so the audit's clean headline (485 sites, 0
   `MUST_MIGRATE_TO_HARDENED_RUNNER`) is partly an assertion about functions that do not have the
   property.
2. **S0.7 + S0.8** — `run_terminal_command` shells to `powershell -ExecutionPolicy Bypass` with
   `CREATE_NO_WINDOW`, and it is one of 173 commands that are **exempt from the ACL** because no
   app ACL manifest exists. The workspace boundary is `C:\`.

The project's own carve-out in `CLAUDE.md` states model-generated code is never auto-executed raw.
For the hive's own compile/test path that is currently not true. **This is the item to fix first**
— it is the one where an adversary, not a mistake, is the failure mode.

### D. Declarative toolchain specs — **absent; toolchains are hardcoded**

* `_ORACLE_IMAGES` in `scripts/hive/compiler.py` is a Python dict with **four** entries: rust, go,
  python, typescript.
* There is **no `toolchains/` manifest directory**.
* `determinex_oracle.py`'s registry is richer but its entries are Python `verify_fn` **callables** —
  code, not data. A new language is a core code change either way.

So the predicted bottleneck is real: every language pack routes through Ryan. And the mismatch is
already user-visible — the Marketplace advertises `cpp-oracle` ("C/C++ / CMake") as **installed**
while `validate_project` fails closed for C/C++ (S3.9).

One latent detail found while checking this: `compiler.py` resolves the image as
`_ORACLE_IMAGES.get(..., "ubuntu:22.04")` — a silent default for unconfigured languages. It is
currently unreachable because the language dispatch fails closed first, but it is the same
"permissive default" shape as the rest of this document and should become an explicit error.

**Action (scoped, not urgent for day 1):** move language definitions to
`toolchains/<lang>.json` (detect command, image, build/test/lint commands, LSP binary, install
hint) and have both the compiler oracle and the Marketplace read that one file. Doing it before
the contributor wave arrives is much cheaper than after.

## Recommended order

1. **S0.7 – S0.10** (ACL manifest, secrets boundary, PowerShell injection, pin the two CI actions). These are the ones where an attacker, not a mistake, is the failure mode.
2. **S1.4, S1.5, S1.11, S1.13** — four named gates that structurally cannot fail. S1.5 in particular means no dependency licence has ever been checked for an AGPL release.
3. **S1.7, S1.6, S1.10, S1.14** — the packet-writer/`_latest_packet` family, which will keep manufacturing green releases until the writers stop asserting literals.
4. **S3.1 – S3.9** — the product-honesty set. Cheapest per unit of trust, and this project's entire value claim is that it does not overstate.
5. **S2.3 – S2.6** — soundness. Highest consequence, but these need the hive limits test re-run and are the riskiest to touch under time pressure.
