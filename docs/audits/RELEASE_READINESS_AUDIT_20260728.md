# Determinex — Release Readiness Audit (2026-07-28)

Requested as a "user / tech / senior POV audit — make sure it's serious and
legit" before release. Everything below was verified against the repo or a
running app, not inferred. Where I could fix something safely I did, and it is
marked FIXED with the commit reasoning.

**Verification baseline at time of writing**

| Gate | Result |
|---|---|
| Rust unit + integration | **60 passed** (was 27 at session start) |
| Python IDE governance locks | **595 passed** |
| Frontend (vitest) | **167 passed / 38 files** (was 86) |
| `tsc --noEmit` | clean |
| `next build` | **compiles clean**, 6/6 static pages (see E-1) |
| Secret hygiene | `.env` ignored + untracked; no real credentials in tracked files |

---

## SENIOR POV — is this releasable?

### S-1. Published benchmark numbers credited the wrong models — **FIXED**

The most serious class of defect this project can have, because its entire
thesis is that a claim must be earned.

README and `docs/papers/ARCHITECTURE.md` both published:

```
C1 Engineer v11-dsl   89%   40/45
C3 Observer  v6-dsl   82%   37/45
```

Those numbers belong to **v10-dsl** and **v5-dsl**. The shipped v11/v6 models
*were* evaluated — 2026-04-16, artifacts on disk — and scored **lower**:

| Model | Real result | Artifact |
|---|---|---|
| engineer-v11-dsl | 57/70 = **81.4%** (earlier run 53/70) | `eval_citadel-engineer-v11-dsl_20260416_225204.json` |
| observer-v6-dsl | 53/70 = **75.7%** | `eval_citadel-observer-v6-dsl_20260416_235354.json` |
| sentinel-v5-dsl | **no eval artifact exists** | — |

No 45-probe v11 or v6 eval exists at all, so `40/45` was never that model's
number in any form.

`CLAUDE.md` compounded it by stating the v11/v6 re-eval was *"queued"* when it
had already run three months earlier and come back lower — which is plausibly
why nobody went looking.

Both documents now separate the verified 45-probe generation (v10/v5/v3,
correctly attributed) from the shipped 70-probe generation, state that the two
probe sets are not comparable, and claim no delta. No combined system score is
given for the shipped generation, because with Sentinel unevaluated any total
would be part measurement and part assumption.

**`WHITE_PAPER.md` needed no change** — it had this right all along, including
the 70-probe caveat. The most rigorous document was the accurate one.

### S-2. The rest of the public claim surface is genuinely strong — **no action**

Verified by reading, not assumed. README states ProgramBench as **0/200
legitimate locks** and explains the provenance correction that invalidated the
old "65 locks / 32.5%". SWE-bench configurations are marked as **lower bounds**
with the reason (disk-pressured Docker workers). It says outright that
"Benchmark results are not product support, not release support, and not
product readiness", and that open availability and `PATENT_FILED` remain false.

That is unusually disciplined. S-1 is the exception, not the pattern.

### S-3. The "100%" privacy claim contradicted our own audit — **FIXED**

README claimed *"100% of repo identifiers obfuscated before any cloud call"* —
the one absolute in a document that hedges everything else.

Checking the evidence made it worse than a style problem. The audit artifact at
`assurance/evidence/cloak_hash_chain_and_leak_audit/` records:

```
perfect_privacy_claimed: false
raw_source_exported:     false
```

The audit **deliberately declines** to claim perfect privacy, while the README
asserted it. That is the no-overclaim rule broken against the project's own
artifact.

Restated as what was established: identifiers are AST-obfuscated, raw source is
never exported, the audit passed and found no leak **in the audited run**. Added
a boundary note quoting the artifact and pointing at `DETERMINEX_CLOAK_AUDIT=1`
for anyone wanting a stronger claim with fresh evidence. No other absolute
privacy claim exists in WHITE_PAPER, ARCHITECTURE or CLAUDE.md.

### S-4. External agent asserted the wrong license — **FIXED**

The DataHub hackathon work produced by another agent states: *"Apache 2.0
license is already included."* It is not. Verified: `LICENSE`,
`frontend/package.json`, `Cargo.toml` and `pyproject.toml` all say
**AGPL-3.0-or-later**, consistently.

That is not a cosmetic error on a public submission — AGPL and Apache 2.0
impose materially different obligations on anyone who uses the entry. Corrected
in `docs/hackathon/DATAHUB_HACKATHON_2026.md` — both the license line and the
demo-video script. Left the *correct* Apache references alone: dbt, Airflow and
DataHub genuinely are Apache 2.0.

Minor, for confirmation only: the manifests say `or-later` while an earlier
decision was recorded as "AGPL-3.0-only". On-disk state is internally
consistent, so this is a wording question, not a defect.

---

## TECH POV

### T-1. `invokeSafe` on writes — the root cause behind most of this session

Documented as Issue 1 in `IDE_SHELL_AUDIT_20260727.md`. A void Tauri command
resolves to `null` on **success**, and `invokeSafe` returns `null` on
**failure**, so for any write the two are the same value and `try/catch` around
it is dead code. Direct consequences found and fixed: silent editor data loss,
a false privacy assurance, ten swallowed git writes, an inert Apply button, and
a "refused" message for a stage that had succeeded.

**Now enforced in CI** by `commandContract.test.ts`, which cross-references
every frontend `invoke` against the registered Rust handlers. Proven to fail:
a temporary canary invoking a nonexistent command made it fail and name the
call site.

**The argument half is now enforced too** (`argContract.test.ts`), and it found
**seven live bugs** on first run:

| Command | Sent | Consequence |
|---|---|---|
| `get_ollama_models`, `check_ollama_status` | `base_url` | `Option<String>` → arrived `None`; **a custom Ollama base URL was ignored entirely** |
| `get_programbench_snapshot` | `run_id`, `expected_total` | same silent-`None` |
| `launch_benchmark_run`, `stop_benchmark_run` | `benchmark_id`, `script_name` | required `String` → command **rejects**; benchmark launch/stop never worked |
| `reveal_session_output` ×3 | `session_id` | rejects; HiveBuildLoop's "Open Output Folder" was broken |

Two of those three `reveal_session_output` sites were written *by me* earlier in
the session, by copying the existing broken pattern — which is precisely why this
had to become a test rather than a habit.

The mechanism was settled from `tauri-macros-2.5.5` source, not from comments:
the lookup key is `param_name.to_lower_camel_case()` and the default is
`ArgumentCase::Camel`. That mattered because this repo's history contains **both**
beliefs — the original `cloneRepo` shipped `remote_url` calling snake_case
"convention", a later commit called it broken.

### T-1b. Why full `tauri-specta` was NOT done — measured, not avoided

| Migration cost | Count |
|---|---|
| Commands to annotate `#[specta::specta]` | 159 |
| Structs needing `derive(specta::Type)` | 94 |
| **Commands returning untyped `serde_json::Value`** | **38 (24%)** |

Those 38 would generate `unknown` in TypeScript, so specta would deliver **zero
shape safety on a quarter of the API** — including the hive commands — while
costing ~250 annotation sites and multi-minute compile cycles per fix pass.

The correct sequencing is therefore: (1) contract tests — **done**, and they
caught 8 real bugs specta would also have caught; (2) replace those 38
`serde_json::Value` returns with typed structs, which is the real prerequisite;
(3) then specta, which at that point actually buys shape checking.

### T-2. Two test suites were protecting the bugs they appeared to cover — **FIXED**

- `gitService.test.ts` simulated git in memory, and its `vi.fn()` **threw**
  where the real `invokeSafe` **swallowed** — so it passed while production did
  the opposite.
- `SettingsContext.test.tsx` asserted "syncs through invokeSafe", literally
  pinning the swallow in place.

Both rewritten. `git.rs` went from **zero tests to 9** running against real
`git` in throwaway repos.

**A green suite in this repo was weak evidence.** That is the single most
important thing for the next person to know.

### T-3. Security of the surfaces added this session — reviewed

| Surface | Control |
|---|---|
| `reveal_env_var` | Workspace-boundary checked; returns **one** key per call; never logs values; reveals dropped on reload |
| `list_env_vars` | Masked previews only — a listing carries no usable credential |
| OAuth token | Never crosses IPC; stored server-side in the existing `GITHUB_TOKEN` row; scopes limited to `repo read:user` |
| `github_open_verification` | Accepts only `https://github.com/...` — deliberately not a general URI launcher |
| `list_ci_runs` | No shell; argv array; `limit` clamped 1–100; read-only (no re-run/cancel) |
| Repair patch plan | Snapshot + restore in a `finally`; proposal only — the sole write path is Review's human-approved `apply_staged_diff` |

`is_safe_path` canonicalizes both sides before `starts_with`, so `..` and
symlinks are handled.

### T-4. Dead surface — largely closed

The 34 surfaces now map 1:1 into nine rail groups, enforced by a test that
parses the real type unions, so a new panel with no home fails the build. That
test immediately found and removed `ideation` — a 345-line surface nothing
could activate. OutputPanel, CICDPanel and EnvManager were all permanently-empty
shells and now read real data.

---

## USER POV

### U-1. The first-run path works, with one hard dependency

Setup Wizard → network policy → hardware probe → Ollama install → model pull →
workspace onboarding. Verified end to end in a real session, including a
genuinely fresh install.

The hard dependency is a **local model**. Until this session the default router
value (`"auto"`) was being passed as an Ollama tag, so `build_idea` was refused
out of the box — **every** verified build failed on a clean install. Fixed and
regression-tested.

### U-2. The flagship loop runs end to end — verified live

Verified Search → synthesize sound oracle → sample local model → oracle-verified
program → **Stage for review** → Review shows the real diff with working
Apply/Reject. Driven by hand in the running app, not inferred. That queue was
structurally incapable of holding anything at the start of the session.

### U-3. Navigation is no longer the obstacle

18 rail icons + three overlapping menus (two of which silently clipped their own
tails, which is why Review and Merge were unreachable) → nine groups with a
drawer that names each surface and explains what it is and does before you spend
screen space on it. Panels are resizable and closable.

---

## ENVIRONMENT

### E-1. `next build` — RESOLVED, and my first diagnosis was wrong

`✓ Compiled successfully`, `✓ Generating static pages (6/6)`, then
`EBUSY: rmdir 'frontend/out'`.

I originally recorded this as "the specific signature of a process holding it as
its current working directory... most likely a stale Next.js static-generation
worker that did not exit cleanly", and said it clears on reboot. **That was
wrong.** Re-checked 2026-07-28 with the actual process list:

```
cargo.exe     26252  "cargo" run --no-default-features --color always --
determinex.exe 34684  T:\determinex-target\debug\determinex.exe
```

`npm run tauri dev` was running. `tauri.conf.json` sets
`frontendDist: "../out"`, so the live dev app holds that directory — which is why
it "survived" killing node workers and why it appeared to need a reboot: a reboot
closed the app.

**So this is not a defect and not a reboot requirement. It is an ordinary
constraint: you cannot run `npm run build` while `npm run tauri dev` is running.**
Close the dev app, then build. Worth a line in the release checklist and worth a
clearer error than `EBUSY` if it is cheap to add.

I did not kill the running app to prove it conclusively — that is the one-line
confirmation to run before packaging.

---

## What I would not ship without

1. **S-4** — correct the Apache/AGPL claim on the DataHub submission.
2. **S-3** — restate or re-evidence the "100%" Cloak claim.
3. ~~**E-1** — one clean `next build` from a fresh boot.~~ **Not a blocker.** The
   dev app holds `frontend/out`; close it and build. A Tauri *package* run is still
   unverified end to end.
4. A decision on **pushing** — 68 commits are local only; nothing has left this
   machine.

Everything else on the shell audit's list is either DONE or explicitly scoped.


---

# Addendum — 2026-07-29: what running the release paths actually found

The 2026-07-28 audit reasoned about the release paths. This addendum records what happened
when they were **executed** for the first time. Three of the four findings below were
invisible to reading, to the type system, and to the whole test suite.

## The Linux release build had never been run

`scripts/release/build_linux_packages_docker.sh` is a complete, end-to-end script —
webkit2gtk stack, Node 20, Rust, Linux sidecar via PyInstaller,
`tauri build --bundles appimage,deb,rpm`, then `package_download_bundle.py`. It had **zero
callers**: `git grep build_linux_packages_docker` finds nothing outside the file itself.

Running it surfaced two blockers in the first three minutes.

### 1. `npm ci` cannot succeed cross-platform (also blocks CI)

    npm error Missing: abbrev@2.0.0 from lock file
    npm error Missing: yallist@4.0.0 from lock file      (~11 of these)

Not a container problem. The committed lockfile is not cross-platform complete:

| | packages |
|---|---|
| Windows resolve (committed lock) | 787 |
| Linux resolve | 804 |
| Linux adds | 43 (`@emnapi/*`, `*-wasm32-wasi` bindings) |
| Linux drops | 26 (`abbrev`, `@npmcli/*`, `@isaacs/fs-minipass`) |

The dropped set is exactly what `npm ci` demanded. `npm install --package-lock-only` on
Windows reports "up to date", so this is not ordinary drift — it is a per-platform
optional-dependency divergence that a single lockfile generated on one platform does not
capture.

**This also breaks CI.** `.github/workflows/release_package_matrix.yml`'s `ubuntu-24.04`
job runs bare `npm ci`, so the Linux half of the release matrix would fail the moment the
billing block clears. Nobody had found it because neither path had ever run.

An assumption of mine was wrong here and is worth recording: I predicted a
Linux-generated lock would fail on Windows in the same way. Tested instead of assumed —
`npm ci --dry-run` on Windows **accepts** the Linux lock (adds 37, removes 28, exit 0), so
one lock may serve both. That is being verified by an isolated Windows `npm ci` +
`tsc` + `next build` against the Linux lock before anything is committed, because a
dry-run proves resolvability, not that the app builds.

### 2. Twenty-four shell scripts were stored with CRLF

The build died at:

    set: pipefail: invalid option name

bash had read `set -euo pipefail\r`. `.gitattributes` has declared `*.sh text eol=lf`
since early on, but these files predate the rule — and because git normalises on diff they
read as **unmodified forever** while being unrunnable on any Linux host. They are precisely
the Linux-targeted ones: `install_hetzner_stack.sh`, `setup_runpod.sh`, `worker_v2.sh`,
`register_models.sh`, `build_linux_packages_docker.sh`, and the `testing/` chain.

Scoping matters here. The first conversion pass touched 365 files, pulling in 341
`compile.sh` under `corpus/programbench/locked/**` — locked PB evidence archives whose
bytes are the record of what a run built, and which `pb_override_scan` reads. Reverted;
evidence stays byte-identical. Two CRLF files remain on purpose, both upstream test
fixtures where the line endings are the test data.

## 3. `clean_host` cannot be satisfied by any machine except a GitHub runner

`run_windows_clean_host_install_smoke.ps1`:

```powershell
$IsGitHubWindowsRunner = ($env:GITHUB_ACTIONS -eq "true") -and [bool]$env:GITHUB_RUN_ID
clean_host_fresh_install = $IsGitHubWindowsRunner
runner.host_reused_from_developer_machine = -not $IsGitHubWindowsRunner
```

The gate requires `clean_host_fresh_install: true`. That field is wired to *being inside
GitHub Actions* — not to any property of the host. Consequences both ways:

* **Too strict.** A freshly provisioned Azure Windows VM (one exists:
  `determinex-clean-host`, D2s v7) yields `false` and self-labels as a reused developer
  host. Reprovisioning does not help, because the machine's actual cleanliness is never
  examined.
* **Too weak.** An environment variable is not proof. Anything that can set
  `GITHUB_ACTIONS=true` produces an authorizing transcript.

A stronger design would attest from evidence the runner can check — no prior install in
the uninstall registry, no dev toolchain on PATH, low uptime — and keep the GitHub-runner
path as one way to satisfy it. That is a change to what a release gate *attests*, so it is
recorded here for an owner decision rather than made unilaterally.

## 4. The download bundle's checksums were never wrong

Worth stating because it contradicts an assumption in the earlier audit. Verified rather
than assumed:

* evidence signatures: **1622 scanned, 1622 already valid, 0 broken**
* bundle checksums: both recorded SHA-256 values **match the built artifacts exactly**

The manifest's "missing" entries are the 193 MB MSI and 188 MB NSIS installer, which live
in the build output. 381 MB of binary does not belong in git; the manifest is accurate and
the binaries are simply not staged.

## Standing blockers after this pass

| gate | status | who can clear it |
|---|---|---|
| `linux_packages` | blocked | now buildable locally via Docker — was never run |
| `clean_host` | blocked | GitHub billing, or an owner decision on what the gate attests |
| `windows_trust` | deferred | needs a code-signing certificate (procurement) |
| `installer` | partial | resolves with the Linux artifacts above |

`release_ready` remains `false`, correctly.
