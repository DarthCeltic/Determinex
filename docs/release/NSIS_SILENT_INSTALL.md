# S7 — the NSIS installer works. The verification script was looking in the wrong directory.

> **Status 2026-07-31: closed.** NSIS is clean-host verified on a genuinely clean VM
> (`vc_runtime_preinstalled: false`), install→launch→uninstall all pass, and the transcript
> validates. Jump to [Re-run on a clean host](#re-run-on-a-clean-host--done-and-it-passes). The
> re-run exposed two further "reported success without checking" defects in the smoke script
> itself; both are fixed and guarded.

**Corrected 2026-07-30 11:35.** An earlier revision of this file (committed the same day) claimed the
installer left `$INSTDIR` as an unresolved relative path so `SetOutPath` failed. **That was wrong.**
The installer installs correctly in every case tested. S7 was a measurement defect.

## What the installer actually does

`$INSTDIR` with no `/D=` comes from, in order:

1. the **remembered previous install location** — the default value of
   `HKCU:\SOFTWARE\<Publisher>\<ProductName>`, read by `RestorePreviousInstallLocation`;
2. otherwise `$LOCALAPPDATA\<ProductName>` for `INSTALLMODE currentUser`.

That is ordinary NSIS "install where you installed it last time" behaviour, and it is why the same
command appeared to do nothing: it was installing to a remembered path while I checked
`%LOCALAPPDATA%\Determinex`.

Verified on a developer host, all three paths:

| Invocation | Result |
| --- | --- |
| `/S` with the remembered-location key **cleared** | installs to `%LOCALAPPDATA%\Determinex` — 11 files incl. `determinex.exe`, all six CRT DLLs, `uninstall.exe`. Records the remembered dir correctly. |
| `/S` with a remembered location present | installs **there** (`C:\tmp\dtx_nsis_test`, `uninstall.exe` stamped 11:30) |
| `/S /D=<abs path>` | installs to that path |
| `uninstall.exe /S` | removes the directory **and** the Add/Remove entry cleanly |

Exit code 0 throughout, ~9–11 s, which is genuine decompression time for a 105 MB payload.

## How I got it wrong, and what caught it

I ran `/S`, checked `%LOCALAPPDATA%\Determinex`, found nothing, and concluded nothing was installed.
I then confirmed "by absence" that no `placeholder` directory existed anywhere — which was true, and
which I read as supporting the relative-path theory. Both observations were consistent with the wrong
explanation, so the theory survived.

What actually settled it was checking **file timestamps in the other candidate directories**:
`C:\tmp\determinex-smoke-install\uninstall.exe` was stamped 11:15 — during the runs I had recorded as
installing nothing — and `HKCU:\SOFTWARE\Determinex Contributors\Determinex` held the path it had gone
to. The installer had been working the whole time.

Two lessons worth keeping. Confirming a theory by *absence* is weak when the thing you are looking for
was never expected in that location. And **I reproduced the exact error the smoke script makes** — I
checked one hardcoded guess of an install directory instead of asking the installer where it went.

## The real defect (S7), and it is fixed

`run_windows_clean_host_install_smoke.ps1` looked in the wrong places:

1. `Find-InstalledExe` listed **`C:\tmp\determinex-smoke-install\determinex.exe` first** — one
   developer's scratch directory, which on this machine still held a binary from 2026-07-21. A local
   run therefore validated a **stale artifact from a previous session**. It survived because a clean
   host lacks that path, so the gate never saw it; only a developer re-running locally was misled.
2. The per-user candidate was **`$LOCALAPPDATA\Programs\Determinex`**, but the installer uses
   `$LOCALAPPDATA\Determinex` — no `Programs` segment. So a *correct* per-user install would never be
   found, and that failure reads exactly like "the installer installed nothing". **This is what the
   clean-host run hit.** The uninstall path had the same mismatch and threw "not found under Program
   Files" while searching three other locations.

Both fixed: the correct per-user directory is now first, the stale developer path is gone, and the
error message names what was actually searched.

Still not covered, and worth adding if this recurs: nothing reads
`HKCU:\SOFTWARE\<Publisher>\<Product>` to discover where the installer *said* it installed. A
directory allow-list will always be a guess.

## Re-run on a clean host — done, and it passes

**2026-07-31, Azure VM `dtx-fresh2`.** The prediction above held. Transcript:
`assurance/evidence/full_release_closure/clean_host_install_transcript_20260731_nsis.json`,
`clean_host_install_transcript.py --validate` → `status: passed`, zero errors.

| Observation | Value |
| --- | --- |
| install exit code | 0 |
| installed to | `C:\Windows\SysWOW64\config\systemprofile\AppData\Local\Determinex\determinex.exe` |
| launch | survived the full 12 s window, no exit code |
| `vc_runtime_preinstalled` | **false** — so the launch had to rely on the installer shipping the CRT |
| proof-center marker | present in the installed binary |
| workspace resources | `determinex-hive.exe` + `_up_\_up_\determinex_model_registry.json` present |
| uninstall exit code | 0 |
| `installer_sha256_verified` | true — *basis:* matched manifest artifact `Determinex_0.1.0_x64-setup.exe` by hash |
| `authenticode_status` | `NotSigned` — the known code-signing blocker, unrelated to this |

`vc_runtime_preinstalled: false` is the load-bearing line. It is what makes the successful launch
mean something: on a host that already has the MSVC runtime the app starts whether or not the
installer did its job, which is how a real 0xC0000135 bug hid until 2026-07-29.

### A third reason the install directory looked wrong: WOW64 redirection

Tauri's NSIS stub is a **32-bit** process (`makensis` reports `x86-unicode`). This smoke runs as
SYSTEM under `az vm run-command`, where `%LOCALAPPDATA%` is
`C:\Windows\system32\config\systemprofile\AppData\Local` — and Windows silently redirects
`system32` → `SysWOW64` for a 32-bit process. So the installer's **files** land under `SysWOW64`
while the **HKCU uninstall entry** records the un-redirected `system32` path. Files and registry
disagree, and the result reads exactly like the original S7 complaint: *"exits 0, writes an
uninstall entry, and that directory does not exist."*

This is an artefact of installing as SYSTEM, not a product defect — an interactive install runs as
the user, where `%LOCALAPPDATA%` has no `system32` segment to redirect. But this script does run as
SYSTEM, so `Find-InstalledExe` and the uninstall lookup now both check the redirected location too.
The 64-bit MSI is unaffected, which is why the same VM shows it at
`...\system32\config\systemprofile\AppData\Local\Programs\Determinex\` — different bitness, and
`Programs\` rather than the NSIS layout.

## Two further defects the re-run exposed

Both are the same shape as the original S7: a check that reported success without checking.

1. **`installer_sha256_verified` was hardcoded true whenever there was nothing to compare against.**
   The `-InstallerPath` branch sets `Artifact` to `$null`, and the else-branch read
   `$installerSha256Verified = $true`. Since `_release_gates` *requires* that field to be true, the
   one field standing between the gate and the wrong artifact was set to satisfy it unconditionally.
   The first re-run of the day duly attested `installer_sha256_verified: true` for installer
   `d1f369ef…` while the manifest the script had loaded listed `ff21a812…`. Now it fails closed,
   matches an explicitly-supplied installer against the manifest **by hash**, and records
   `installer_sha256_basis` so a reader can tell a real match from "nothing to compare against".

2. **`-ManifestPath` defaulted to `determinex_download_bundle_20260707`** — a dated directory that
   goes stale the moment anyone packages a bundle, and it was six bundles stale. That default is why
   defect 1 was reachable at all. The same mtime-ordered "newest bundle" rule was written out by
   hand in **six** places and skipped by two more that hardcoded the date; it is now one function,
   `determinex_release_gates.newest_download_manifest_path`, with a PowerShell twin in this smoke
   (needed because a clean host has no repo venv) pinned to agree by
   `tests/test_download_manifest_resolution.py`.

## Consequence for the release gate

`clean_host` was **already** passing before this run, on the MSI transcript
(`clean_host_install_transcript_20260730T1815Z.json`, installer `3f72e1d4…`). Worth stating plainly:
that transcript was produced by the pre-fix script, so its `installer_sha256_verified: true` was
vacuous — the hash happens to be the manifest's MSI, so the pass was *correct*, just not *verified*.
Under the fixed script it now earns the same verdict.

So this run does not flip a gate. What it closes is the narrower open item — "NSIS clean-host re-run
with the fixed script (MSI is verified; NSIS isn't)". Both Windows installers are now clean-host
verified, and SETUP.md leading with the MSI is a preference rather than a necessity.

## Also disproved along the way

* **WebView2** — this host has it (`pv 150.0.4078.105`), and the installer works here, so the
  `Abort "$(webview2AbortError)"` path was never involved.
* **A silent `MessageBox` falling through to `Quit`** — only two exist; one is compiled out
  (`MINIMUMWEBVIEW2VERSION ""`), the other is on a previous-version uninstall path.
* **UAC** — `INSTALLMODE currentUser` compiles to `RequestExecutionLevel user`; the reproducing shell
  was non-elevated, which is the supported case.
* **The self-CRC check** — `/NCRC /S` behaves identically.
* **A quoted `InstallLocation` poisoning the next install** — line 670 does write
  `"$\"$INSTDIR$\""`, quotes included, but nothing reads that value back into `$INSTDIR`.
  `RestorePreviousInstallLocation` reads `MANUPRODUCTKEY`, which is stored unquoted.
* **An NSIS installer hook to repair `$INSTDIR`** — written, built and tested. It changed nothing,
  because `$INSTDIR` is always absolute. Removed rather than left in: dead code that claims to fix a
  non-existent bug is worse than no code, and it would have misdirected the next reader.
