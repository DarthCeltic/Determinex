# User-facing audit — 2026-07-29

Audited as a **new user**, not as the author: install the app, open it, click things. The
question throughout was "what does someone who has never seen this hit?" rather than "does
the code look right".

Five defects, four fixed. The unfixed one is the biggest, and it is not in the code.

---

## 1. BLOCKER — a fresh install cannot reach a working state

**Not fixed. Needs an owner decision, and it outranks every release gate.**

A brand-new user installs, runs setup, and is told *"Missing local model coverage for 2
roles"* with no in-app way to resolve it. Traced end to end:

`src-tauri/src/ipc_hive/roles.rs` defaults a fresh install to:

| role | default | obtainable by a new user? |
|---|---|---|
| oracle | `local/fast` → `qwen2.5-coder:3b-instruct` | **yes** — `model_puller.rs` pulls it from Ollama |
| architect | `local/fast` → same | **yes** |
| builder | `determinex/engineer` → `determinex-engineer-v11-dsl` | **no** |
| monitor | `determinex/observer` → `determinex-observer-v6-dsl` | **no** |

Why the last two are unobtainable, in order:

1. `model_puller.rs` pulls **only** the public qwen base models. Its own comment says the
   fine-tuned GGUFs are "handled separately via GitHub Releases download".
2. The README points at HuggingFace instead — and those three repos
   (`darthceltic85/determinex-engineer`, `-observer-llama-3.2`, `-sentinel`) are
   **private**. Every download link 401s for anyone but the owner.
3. **Nothing in the UI explains how to get them.** A search across `frontend/src` for
   `ollama create`, `Modelfile`, `huggingface` or `Releases` finds no user-facing guidance
   at all.
4. The shipped Modelfiles cannot bootstrap them. `Modelfile.engineer` reads:

       FROM determinex-engineer-v11-dsl

   It derives *from* the model it is supposed to create — a parameter overlay
   (num_ctx/temperature/keep_alive), not a GGUF import. It only works once the model is
   already in Ollama.

Then `lib/work-readiness.ts` resolves `determinex/engineer` to exactly
`determinex-engineer-v11-dsl`, finds it missing, returns `ready: false`, and
`specGenerationBlockMessage` blocks spec generation.

So the install succeeds and the product does not start. Three ways out:

* **Flip the HF repos public** (one command, owner-only) **and** add in-app guidance plus a
  Modelfile that imports from the downloaded GGUF. Keeps the DSL-tuned builder as the
  default.
* **Default builder/monitor to public base models** so a fresh install works out of the
  box, with the fine-tuned models as an explicit upgrade. Entirely in-repo, but it changes
  what the product *is* out of the box — the DSL-tuned builder is the differentiator, so
  this is a product call, not a bug fix.
* Both.

I did not choose for you. Changing the default builder silently downgrades the headline
capability; leaving it means a public launch where nobody can run it.

---

## 2. FIXED — "Idea Lab" was a menu item that did nothing

`lib/surfaceGroups.ts` advertised a surface:

    { id: "idea", label: "Idea Lab", kind: "addon",
      what: "Single-function idea to verified program." }

There was no `addonItems` entry with that id. So clicking it set `activeAddon = "idea"`,
`selectedAddon` resolved to `null`, and the dock render — guarded by
`addonDockOpen && selectedAddon` — produced **nothing**. The menu closed and the app sat
there.

It was also a duplicate. The capability it described is the `search` member, whose panel
`VerifiedSearch.tsx` opens with *"Verified Search = the Correctness Amplifier, driven from
the IDE"* and calls `preview_idea_oracle` then `build_idea`. Removed the phantom entry from
the taxonomy, the `WorkspaceAddon` union and `runtimeAddonIds`; the capability is still
offered once, through the entry that opens.

## 3. FIXED — the guard written for exactly this bug never looked at panels

`lib/__tests__/surfaceGroups.test.ts` has a test called **"never offers a surface that
cannot open"**, whose own comment describes a previous instance:

> `skin` sat in the taxonomy pointing at an addon id that was never in `addonItems`, so the
> drawer advertised a panel, the user clicked it, and nothing could render.

But it checked membership of the `WorkspaceAddon` **type union**:

    return m.kind === "addon" ? !addons.has(m.id) : !sidebars.has(m.id);

A type union is a list of allowed strings. Adding `| "idea"` satisfies it while no panel
exists — so the guard passed for as long as the defect was live. It now parses the real
`addonItems` registry (id paired with the `panel:` that follows) and throws if the parse
finds fewer than 15 panels, so a broken regex fails loudly instead of vacuously.

## 4. FIXED — Learning Studio's two calls-to-action were dead clicks

    <a href="#repo-clinic">Open in Repo Clinic</a>
    <a href="#idea-lab">Open in Idea Lab</a>

Nothing in the app carries those ids. A user reading *"Want to act on a fix? Open in Repo
Clinic"* got a changed URL hash and no navigation — while Repo Clinic sat one panel away in
the same window. Both now call the workbench's real switchers (`handleAddonLaunch`, and the
`hive` sidebar for the new-project flow). When no handler is supplied they render as plain
text, so the component can never present a clickable promise it cannot keep again.

## 5. FIXED — the Correctness Amplifier was described as a snippet search

The registry entry read:

    id: "search", label: "Verified Search",
    description: "Find verified snippets and project context."

That describes retrieval, which this panel is not, and it sits directly above
**"Find in Files — literal, gitignore-aware text search"**. Anyone wanting text search
would click the one labelled Search and land in an idea-to-program builder. `surfaceGroups.ts`
already described the same surface correctly ("The Correctness Amplifier"); the registry
description now matches the panel and the taxonomy.

---

## 6. BLOCKER (fix landed, verification pending) — the installed app could not start at all

Found by finally running the clean-host smoke on a freshly provisioned Azure VM. The MSI
installs with exit code 0, the app appears under `C:\Program Files\Determinex`, and then
**`determinex.exe` dies ~2 s after launch with `0xC0000135` (`STATUS_DLL_NOT_FOUND`)**. A
first install on a clean Windows machine produced an app that could never open.

`determinex.exe` links the MSVC C runtime dynamically, and a clean Windows 11 image has no
`vcruntime140.dll` / `vcruntime140_1.dll` / `msvcp140.dll` and no VC++ redistributable.

The package was *trying* to handle this: `bundle.resources` ships `vc_redist.x64.exe`
(25.6 MB, present in the installed tree), and `windows/vc_redist.wxs` declared a CustomAction
to run it. **The custom action was never in the MSI.** The WiX linker prunes at fragment
granularity, and nothing referenced that fragment, so it was discarded — silently, because
discarding an unreferenced fragment is not an error. Querying the shipped MSI directly:
`CustomAction` had no `InstallVcRedist`, `Binary` had no `VcRedistExe`, and
`InstallExecuteSequence` had no matching row. `tauri build` had reported success throughout.

Diagnosis was not guesswork:

| probe | result |
| --- | --- |
| `notepad.exe` in the same session | resident 15 s — rules out "no interactive desktop" |
| WebView2 runtime | present, 150.0.4078.105 — rules out a missing webview |
| `determinex.exe`, runtime absent | exits `0xC0000135` after 2032 ms |
| `determinex.exe`, after installing the shipped redist | **resident 15 s** |
| `determinex-hive.exe` | unaffected either way — PyInstaller bundles its own CRT |

Same binaries, same host, one variable.

**First fix attempt, and why it was wrong.** Tauri 2.10 exposes `componentRefs` /
`componentGroupRefs` / `featureRefs` / `featureGroupRefs` / `mergeRefs` but no
`customActionRefs`, so a CustomAction cannot be referenced directly. Because pruning is
per-fragment, anchoring the fragment with a referenced `Component` retains it. That worked —
the rebuilt MSI's `CustomAction` table contained
`InstallVcRedist | 3170 | INSTALLDIR | "[INSTALLDIR]resources\vc_redist.x64.exe" ...`
sequenced at 4001, right after `InstallFiles`.

**And the app still would not launch.** The verbose MSI log said why:

```
MSI_LUA : Custom Action 'InstallVcRedist' is running with sufficient privileges.
CustomAction InstallVcRedist returned actual error code 1618
   but will be translated to success due to continue marking
Property(S): ALLUSERS = 1
```

`1618` is `ERROR_INSTALL_ALREADY_RUNNING`. The action executes *inside* our own MSI
transaction, and Windows Installer permits one install at a time, so a nested redistributable
install can never succeed there — and `Return="ignore"` converted that permanent failure into
a reported success. Chaining a redistributable properly needs a Burn bootstrapper wrapping the
MSI, which the Tauri bundler does not produce. So the shipped-redist approach was not
misconfigured; it was **impossible**.

**Actual fix: app-local CRT deployment.** The DLLs now ship beside `determinex.exe`, where the
loader searches before `System32`. No elevation, no network, no install-time action, identical
behaviour for MSI and NSIS. Microsoft's redistributable licence permits app-local deployment.
The 25.6 MB redistributable, the WiX fragment and the NSIS hook are all deleted — net ~24 MB
smaller. See `frontend/src-tauri/CRT_RUNTIME.md`.

Getting there required one more correction. A first app-local attempt *also* failed, at 33 ms
instead of 1841 ms, because the DLL set was still a guess. Parsing the binary's real import
table settled it — `MSVCP140.dll` **and `MSVCP140_1.dll`**, the latter never placed.
(An earlier parse attempt read data directory index 0, the *export* table, and duly reported
this binary's own `onig_*` symbols as if they were imports.) With the complete set:

| condition | result |
| --- | --- |
| no CRT beside the exe | exited 1841 ms, `0xC0000135` |
| six CRT DLLs beside the exe | **resident 15 s, launch OK** |

**Guards added**, since the config, the build output and the whole test suite were all green
while this was broken:

* `tests/test_windows_installer_runtime.py` parses the built `determinex.exe`'s import table,
  subtracts what Windows itself provides, and fails if anything remaining is not shipped. It is
  derived from the binary rather than a hardcoded name list, so a future native dependency that
  needs shipping fails a test instead of shipping an app that cannot start. Plus: the MSI on
  disk must contain the CRT (this test failed against the previously shipped MSI, confirming it
  targets the real defect), no CustomAction may nest an installer again, and no WiX comment may
  contain `--` (which cost one whole build — candle rejects the file with CNDL0104 and Tauri
  swallows the reason).
* The clean-host smoke now records `runner.vc_runtime_preinstalled`. This dependency is
  exactly what the smoke exists to prove is delivered, so on a host that already has the
  runtime a passing launch check proves nothing. Not enforced — GitHub Windows runners ship
  the redistributable, and requiring its absence would make that blessed path unsatisfiable —
  but recorded, so a reader can tell a real proof from a vacuous one. This mattered
  immediately: the first VM had the runtime installed during diagnosis, so re-using it would
  have produced a green transcript for the wrong reason. Verification moved to a second,
  confirmed-pristine VM (`VC++ runtime: ABSENT`).
* The smoke now records `launch_exit_code` / `launch_exit_code_hex` and uses
  `WaitForExit(ms)` instead of sleep-then-`Refresh`. The first failing transcript said only
  `launch_process_exited_during_smoke: true` — true and useless. `0xC0000135` was the single
  fact that identified the cause, and recovering it took an extra round-trip to the host that
  the transcript exists to make unnecessary.

## 7. BLOCKER (fixed) — there was no way to ship a fix to anyone

The app had **no update mechanism at all**: no `tauri-plugin-updater` in `Cargo.toml`, no
`@tauri-apps/plugin-updater`, no `plugins.updater` config, no signing key. `release.yml` builds
installers on a `v*` tag and attaches them to a GitHub Release, so pushing a fix updated the
*download links* and never touched an installed app.

That property is one-way and it made this urgent rather than merely desirable: **a build shipped
without the updater can never learn to update itself.** Whoever installed the first public
version would have been on manual reinstalls permanently, no matter what later versions did. It
had to be in the first public build.

Now wired end to end: plugin registered, `updater:default` and `process:allow-restart` in the
default capability, `createUpdaterArtifacts: true` so the bundler emits a signed archive, a
minisign keypair generated **outside the repo** (`~/.determinex-updater/`) with the public half
in `tauri.conf.json`, `TAURI_SIGNING_PRIVATE_KEY` passed in `release.yml`, and
`build_release_package.ps1` failing loudly with the exact `tauri signer generate` command if no
key is available rather than dying deep inside the bundler.

`UpdateNotice` does the user-facing half, deliberately quiet: it checks once six seconds after
mount so it never competes with first-run setup, stays silent unless an update exists, swallows
every failure to a console warning (an offline user or a release with no `latest.json` must not
get an error dialog on top of a working app), and never installs without being asked — because
installing relaunches the app, and losing someone's in-progress session to a background update
is worse than shipping the fix a day later.

**Owner action required:** add the private key from `~/.determinex-updater/determinex_updater.key`
to the repo as the `TAURI_SIGNING_PRIVATE_KEY` secret. Losing that key means no already-installed
build can ever accept another update. It was generated without a password; adding one is
recommended, and needs `TAURI_SIGNING_PRIVATE_KEY_PASSWORD` set alongside it.

## 8. BLOCKER (fixed) — the wizard announced work it did not do

`SetupWizard` displayed *"Registering Determinex model swarm with Ollama…"* while calling
`initialize_system`, which pulls base qwen models and registers the fine-tuned Determinex models
only if their GGUFs already happen to be on disk. On a fresh machine they never are. So the
wizard claimed the work, registered nothing, and reached **"System Ready"** on an install where
`roles.rs` defaults Builder and Monitor to models the user had no in-app way to obtain.

The capability had shipped all along: the bundled sidecar exposes
`helper setup.install_determinex_models`, which downloads each GGUF from its now-public
HuggingFace repo, verifies the published sha256 and registers it with a generated Modelfile.
Verified working end to end through the shipped sidecar. **Nothing called it.**

Two new commands close that gap — `check_determinex_models` (cheap, side-effect free) and
`install_determinex_models` — kept separate on purpose: the download is several GB, so it must be
an informed choice rather than something first-run setup spends on someone silently. The wizard
now states honestly what is missing, why it matters (those two roles cannot run without it), and
offers the download, while remaining skippable.

Also fixed here: `bootstrap.rs` registered `determinex-engineer-v10-dsl` /
`-observer-v5-dsl` / `-sentinel-v3`, and the first two are in the router's `STALE_MODEL_IDS`, so
first-run setup registered precisely the tags the router refuses with
`ROUTE_BLOCKED_STALE_MODEL_ID`. Now v11/v6/v5, pinned against the router's `CURRENT_MODEL_IDS` by
a cross-language drift test — the two languages had no connection before.

## 9. Fixed — the shipped app stored gigabytes of weights under %TEMP%

`models_dir()` falls back to `ROOT / ".determinex-models"`, and `ROOT` derives from `__file__`.
Inside the PyInstaller onefile sidecar that is the **extraction directory under %TEMP%**, so the
shipped product's default storage was ephemeral. Observed live from the sidecar:
`gguf storage : C:\Users\<user>\AppData\Local\Temp\.determinex-models`. Several GB of weights and
resumable `.part` files, one temp clean or reboot from deletion mid-download.

Frozen builds now use a durable per-user location (`%LOCALAPPDATA%\Determinex\models`, or
`$XDG_DATA_HOME/determinex/models`); a source checkout keeps the repo-local path developers
expect; `DETERMINEX_MODELS_DIR` still wins. Guarded by a test that asserts the frozen branch
never resolves under temp — the branch that actually ships was the one nothing exercised.

## 10. Noted, not blocking

* **WebView2 is fetched from the internet at install time.** `webviewInstallMode` is unset,
  so Tauri's default `downloadBootstrapper` applies and the MSI carries a
  `DownloadAndInvokeBootstrapper` action that downloads from `go.microsoft.com`. An offline
  install therefore cannot provision a missing webview. In practice Windows 11 ships WebView2
  (confirmed on both clean VMs), so this is a limitation rather than a break; the fully
  offline alternative adds ~130 MB to the installer.
* **A dead branch in the workspace smoke — fixed.** `workspace_command_smoke_performed`
  accepted `determinex-hive.exe` OR `determinex_model_registry.json` next to the exe. The
  registry never lands there: declared as `../../determinex_model_registry.json`, Tauri
  preserves the relative path and installs it to `_up_\_up_\determinex_model_registry.json`, so
  only the sidecar branch could ever pass. The check looked like it accepted either of two
  proofs while only ever evaluating one. Both are now required, and the registry is looked for
  where it actually lands. The `_up_\_up_\` placement itself is inert: nothing in the Rust or
  TypeScript reads that file, only three dev-side Python scripts that run from the repo.
* **Unsigned installers.** `authenticode_status: NotSigned`, so every install *and every
  update* raises SmartScreen. This is the deferred `windows_trust` gate and needs a purchased
  code-signing certificate — owner action, not fixable here.
* **Two different default model directories.** With no `DETERMINEX_MODELS_DIR` set,
  `bootstrap.rs` falls back to `%USERPROFILE%\determinex-models` while the frozen installer now
  uses `%LOCALAPPDATA%\Determinex\models` (fix 9). Benign in the real flow, and traced rather
  than assumed: `run_first_setup` checks `ollama list` first and returns early once the three
  tags exist, and the installer registers them itself via `ollama create`, which imports the
  GGUF into Ollama's own blob store. So nothing reads the directory after registration. Worth
  aligning for coherence, but it cannot currently cause a failure, and aligning it needs
  another full rebuild cycle to ship.

## 11. Second sweep — four more guards that could not fail

Found by deliberately hunting the *shape* of the bugs above rather than waiting for symptoms.

**`first_e2e` passed on evidence three weeks older than the code.** The gate read a status
string out of an evidence file with no binding whatsoever to what was being shipped. One
transcript dated `2026-07-07T16:57:30Z` kept it green across the internal rename, the addition
of the in-app updater, and the entire period when the installed app could not launch at all on
a clean host. Its own `next_action` read *"Keep the transcript current with the release
commit"* — an instruction to a human sitting exactly where a check belonged. Its primary
`result.json` says `LANE_D_BLOCKED_LOCAL_BUILDER_OLLAMA_TIMEOUT`; a superseding rerun file
carried the pass. Now blocked when the proof predates the release artifacts, with both
timestamps named in the blocker. Bound to the download manifest rather than to HEAD on
purpose: gating on every commit would demand a rerun for a docs typo, and a permanently
blocked gate is how checks get quietly relaxed.

**`status.endswith("PASSED")` accepted `"NOT_PASSED"`.** A bare suffix test on an
unconstrained, hand-authored label — in a tree whose real statuses look like
`LANE_D_BLOCKED_LOCAL_BUILDER_OLLAMA_TIMEOUT` — was one unlucky string away from reading a
failure as a pass. Replaced with a helper that excludes negative markers explicitly, and
tested against the negated forms.

**The SBOM gate never checked that the SBOM described what we ship.** It verified three files
existed, parsed, and were correctly branded, then passed — with `next_action` again reading
*"Keep SBOMs regenerated"*. Measured: the npm SBOM was two weeks stale and listed **none** of
`@tauri-apps/plugin-dialog` (shipping for weeks), `@tauri-apps/plugin-process`, or
`@tauri-apps/plugin-updater`. An SBOM is consumed as a supply-chain assertion, so one that
silently omits shipped code is worse than none. Now blocked unless every direct runtime
dependency in `package.json` and `pyproject.toml` appears in the corresponding SBOM. Direct
dependencies only — transitive resolution belongs to the generator, not to a second competing
implementation in a gate. A companion test covers scoped packages emitted as
`group="@tauri-apps"` + `name="plugin-updater"`, because a bare-name lookup would false-positive
on every scoped package, and a check that cries wolf is a check that gets deleted.

**Authenticode signing had never worked.** The signing loop built its arguments in `$Args` — a
PowerShell *automatic* variable — and splatted it inside a scriptblock that `Invoke-Checked`
runs as `& $Command` with no arguments, so inside the block `$Args` is that invocation's own
empty list. Verified directly: assigning the automatic name and reading `.Count` inside `& { }`
yields 0, while any other name yields the real count. `signtool` therefore ran bare and printed
usage. Nothing caught it because the path only executes once a signing thumbprint is
configured, and `windows_trust` is deferred pending a purchased certificate — so it would have
surfaced as a confusing "signing failed" on the first real attempt, looking like a certificate
problem.

**Also, from enabling the updater:** `_artifact_type`'s fallthrough is `return "installer"`,
and the real release flow points `--installer-dir` at the bundler output directory, which now
contains `.msi.zip` and `.msi.sig`. The download manifest would have advertised a 96-byte
detached signature as an installer — the vc_redist bug in the same function, reopened by a
config change nowhere near it. Now rejected, with a companion test that a legitimate `.zip` is
still accepted so the exclusion stays narrow.

## Checked and found sound

Recording these so nobody re-audits them:

* **Mission Control / Roadmap gating.** `internalOnly: true` in the taxonomy,
  `showInternal = false` by default in `SurfaceDrawer`, `showInternal={isInternalBuild()}`
  at the call site, and a test proving Mission Control is hidden without the flag. Correct
  in all four places.
* **First-run sequencing.** The SetupWizard/WorkspaceOnboarding race is handled, with the
  reasoning recorded at `page.tsx:1147` — on a genuinely fresh install both used to mount
  at once.
* **No other orphaned surfaces.** Every other `kind: "addon"` member in the taxonomy has a
  registry panel, including `agent-chat` (an earlier scan of mine missed it — the pattern
  `[a-z]+` excludes hyphens).
* **Dead buttons: 2**, both in `wireframes/AndroidBaselineMock.tsx`, which is a mock.
* **IPC surface.** 171 commands, 171 registered, zero dead invokes.

## Still to verify (shell tooling was unavailable at the end of this pass)

* The seven provider "get an API key" URLs in `SetupWizard`/`ToolsHub` — extracted but not
  yet HTTP-checked. A dead key link is a first-run blocker.
* Whether GitHub Releases actually exist, since `model_puller.rs` names them as the source
  for the fine-tuned GGUFs while the README names HuggingFace. At most one of those can be
  right.
* `tsc` and the frontend suite after fixes 2–5.
