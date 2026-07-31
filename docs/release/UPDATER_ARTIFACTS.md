# Updater artifacts — RESOLVED 2026-07-30

**Root cause: the bundler silently skips updater signing when `TAURI_SIGNING_PRIVATE_KEY_PASSWORD` is
*undefined*, and on Windows an empty value cannot define it — so a passwordless updater key can never
produce a `.sig`.** Fixed by switching to a password-protected key. `tauri build` now reports:

```
Finished [tauri_cli::bundle] 2 updater signatures at:
    T:\determinex-target\release\bundle\msi\Determinex_0.1.0_x64_en-US.msi.sig
    T:\determinex-target\release\bundle\nsis\Determinex_0.1.0_x64-setup.exe.sig
```

`tests/test_windows_installer_runtime.py::test_a_built_msi_has_a_signed_update_artifact_beside_it`
is green for the first time (18/18 in that file).

Investigated and fixed with `tauri-cli 2.10.1` / `tauri-plugin-updater 2.10.1` on Windows 11.

## How it was proven, rather than guessed

The decisive step was a **negative control** that needed no key change: set the password variable to a
deliberately wrong non-empty value and rebuild. If the bundler had been ignoring the config, nothing
would change. Instead it failed loudly:

```
failed to decode secret key: incorrect updater private key password: Wrong password for that key
Error [tauri_cli_node] failed to decode secret key: ...
exit=1
```

That single result separates the two candidate explanations: the bundler **does** honour
`createUpdaterArtifacts` and **does** attempt signing — the only difference between signing and
silently doing nothing is whether the password variable is *defined at all*. Everything before this
had been inference from absence, which is why it went unresolved for so long.

## What was changed

* A new **password-protected** keypair (32-char random password). The old passwordless key is kept at
  `~/.determinex-updater/determinex_updater.key.passwordless.bak` rather than destroyed.
* The password lives beside the key at `~/.determinex-updater/updater_key_password.txt`, outside the
  repo. `build_release_package.ps1` reads it automatically if present.
* `plugins.updater.pubkey` in `tauri.conf.json` updated to the new public key (key id `9A6B839BE79C5470`).
* The build script now **throws** when the password is missing instead of warning: shipping installers
  with no `.sig` yields an update endpoint every installed client refuses, which presents to a user as
  "updates simply never work".

### Consequence you must know about

The public key is compiled into the app, so **the previously staged installers embed the old key**.
They cannot accept updates signed with the new one. Before publishing:

1. re-stage from the freshly built, signed installers (`package_download_bundle.py`), then
2. re-run the clean-host verification, because re-staging moves the freshness anchor and correctly
   invalidates the existing clean-host and first-e2e evidence.

Doing the key change *before* first publication is exactly why it was safe. After publication it would
have permanently stranded every installed copy.

## Investigation record — the OLD passwordless key (superseded)

Kept because the reasoning is what led to the fix. Everything in this section refers to the
now-replaced passwordless key (id `62B157F0D05086B2`), not the current one.

**That keypair was valid and matched the then-configured public key.** Signing a probe file
succeeded:

```powershell
$env:TAURI_SIGNING_PRIVATE_KEY = (Get-Content -LiteralPath $key -Raw).Trim()
npx tauri signer sign --password= C:\tmp\sig_probe.txt
#   -> Your file was signed successfully
```

The emitted signature's key id (`…yhlDQ8Fex…`) matches the `plugins.updater.pubkey` in
`tauri.conf.json` (`RWSyhlDQ8Fex…`; the `RUS`/`RWS` prefixes differ by minisign convention, the key
bytes do not). So *nothing is wrong with the key, the pubkey, or their pairing* — a hypothesis that
had previously been assumed rather than tested.

Note `--password=` as a **single token**. PowerShell drops an empty `""` argument when calling a
native executable, so `-p ""` silently becomes "no password argument" and the next token (the file
path) is consumed as the password value. That produced
`error: the following required arguments were not provided: <FILE>` — a message that points at the
wrong problem entirely.

## The load-bearing discovery: an empty password cannot be passed on Windows

`build_release_package.ps1` contained this, with a rationale that is false on its own platform:

```powershell
# Set explicitly even when empty: the signer prompts for a password interactively
# when the variable is absent, and a prompt in a non-interactive build hangs.
if (-not $env:TAURI_SIGNING_PRIVATE_KEY_PASSWORD) {
    $env:TAURI_SIGNING_PRIVATE_KEY_PASSWORD = ""
}
```

Measured:

| Probe | Result |
| --- | --- |
| `$env:X = ""` then `Test-Path Env:\X` | `False` |
| `[Environment]::GetEnvironmentVariable('X')` | `$null` |
| `cmd /c "if defined X …"` | `CHILD_SEES_UNDEFINED` |

Assigning an empty string **deletes** the variable; .NET's `SetEnvironmentVariable` documents the
same behaviour. So "defined but empty" is not expressible, and that guard could never have worked.

It is not merely cosmetic: `tauri signer sign` genuinely blocks on an interactive password prompt
when the variable is absent. Reproduced live — the call hung until killed. A passwordless updater key
therefore has **no way** to satisfy the bundler's signing step through the environment, because the
bundler takes no password flag.

## Correcting one thing this file previously got wrong

An earlier revision recorded that a `.zip` beside the MSI is the expected v2 artifact, citing the
`#[cfg(windows)] impl Update` doc block in `tauri-plugin-updater`. That block lists what the updater
*can consume* — MSI, NSIS exe, and zipped forms of each — not what `createUpdaterArtifacts: true`
*produces*. The real v2 output on Windows is the **installer plus a detached `.sig`, with no archive**;
the zip belongs to the legacy `"v1Compatible"` mode, which the config schema describes as "Generates
legacy zipped v1 compatible updaters", and `install_inner` accepts either
(`if infer::archive::is_zip(bytes)`).

This mattered: the test demanded a zip as well as a `.sig`, so it would have stayed red even after the
real defect was fixed — a check failing for a reason unrelated to the thing it guards, which is worse
than no check because it hides the moment the bug is actually gone. Test corrected to require the
`.sig` per installer and to verify it decodes to a minisign signature.

## Ruled out — do not re-test these

* The config key name and nesting — `bundle.createUpdaterArtifacts: true`, schema-confirmed against
  `node_modules/@tauri-apps/cli/config.schema.json`, parsed back out of the file to be sure.
* `"v1Compatible"` vs `true` — the schema documents `v1Compatible` as the *legacy zipped* form.
  `true` produces installer + detached `.sig` and **no** archive; see the correction section above,
  which supersedes an earlier claim in this file that a `.zip` was expected.
* `TAURI_SIGNING_PRIVATE_KEY` given a **path** instead of key content — fails silently and produces
  no artifacts, because a Windows path is not base64 (it breaks on the `:` at offset 1). The script
  now passes content and sets `_PATH` separately.
* A separate `updater` bundle target — `--bundles` accepts only `msi`/`nsis` on Windows.
* An explicit `bundle.targets` array — no change, and it breaks 3 of the 4 `release.yml` jobs, since
  that workflow builds macOS and Linux from the same config. Guarded by
  `tests/test_workflow_hygiene.py`.
* Platform config overrides — none exist; `src-tauri/` contains exactly one `tauri.conf.json`, no
  `.json5`, no `Tauri.toml`.
* `tauri bundle` vs `tauri build` — **before the fix**, both ran to completion, emitted msi + nsis,
  and never mentioned the updater step in `--verbose`. Not a subcommand difference: the missing
  password suppressed it in both. After the fix, both sign.
* Artifacts landing somewhere unexpected — `find` over the whole target tree for `*.sig`,
  `*.msi.zip`, `*setup.exe.zip` returns nothing.
* The CLI's own diagnostic. The binary contains the string *"The bundler was configured to create
  updater artifacts but no updater-enabled targets were built. Please enable one of these targets:
  app, appimage, msi, nsis"* — and it correctly never fires, because msi and nsis are both
  updater-enabled and both were built. So the bundler is not rejecting the targets; it simply never
  reaches the updater step.

## Side effect of investigating this: target ≠ staged

Running `tauri build`/`tauri bundle` to test the above **rewrote the installers in
`T:\determinex-target\release\bundle\`** with different bytes (the NSIS CRC moved from `0xA23A9A6F`
to `0xB3295F9E`). It did *not* invalidate any release gate, and that is by design rather than luck:
`_release_artifacts_built_at` anchors freshness on the `source_path` entries in
`download_manifest.json`, which point at the **staged** copies under
`.tmp\determinex-download-bundles\installers\`. Those were untouched, so the clean-host and
end-to-end evidence still refers to exactly the binaries it was gathered against. Verified after the
rebuild: still 7 passed / 4 deferred / 1 partial.

The consequence to remember is the reverse direction. The staged installers are now **older than**
the ones in the target directory, so re-running `package_download_bundle.py` would pick up the newly
built binaries, move the freshness anchor, and correctly invalidate the clean-host and first-e2e
evidence — requiring a fresh clean-host run before those gates pass again. Repackage only when you
intend to re-verify, not as a tidy-up step.

## Status

**Resolved.** Both installers are signed, the test is green, and the build script now refuses to
produce unsigned installers rather than doing it quietly.

Still unproven, and deliberately left so: the **end-to-end** update — publishing a release, an
installed build discovering it, downloading and applying it. That needs a published release and two
versions, so it cannot be verified locally. What is now proven is that the artifacts an installed
build looks for actually exist and are correctly signed against the key compiled into the app, which
is the part that was broken.
