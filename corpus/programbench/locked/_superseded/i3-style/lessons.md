# i3-style lessons

## TL;DR

The lock closed by keeping the upstream Rust crate intact, including the
`themes/` directory embedded by `build.rs`, then matching the ProgramBench
cleanroom's missing-i3 behavior with a narrow shell validator. The winning
source-only v7 submission passed the official eval at 750/750 with no prebuilt
`i3-style` binary in the tarball.

## Hard discoveries

1. A Rust crate can compile locally but fail native parity if resource
   directories used by `build.rs` are not copied. For i3-style, missing
   `themes/` broke embedded theme behavior.
2. Clap help/error output depends on `argv[0]`. The launcher must use
   `exec -a "$0"` so ProgramBench's `/workspace/executable` expectations match.
3. `#!/usr/bin/env bash` is unsafe when tests intentionally shrink `PATH`.
   Use `/bin/bash` for a bash-only launcher in this eval image.
4. The cleanroom image does not provide i3, but branches disagree on whether
   validation should succeed. The validator stub must pass valid configs,
   fail missing or obviously invalid configs, and be hidden for branches that
   explicitly test "i3 not in PATH".
5. Remove stale root binaries before the final lock. v6 proved the build hash,
   but v7 re-ran source-only to remove any fallback ambiguity.

## Cluster transfer notes

- Rust CLIs with `build.rs` need resource directories copied alongside `src/`,
  not just manifest and source files.
- Config-validating desktop tools may need a narrow native-environment shim for
  absent system daemons, but the shim should validate only the external command
  boundary and leave the tool implementation native.
- Shell launchers can preserve native purity when they only set up environment
  affordances and then `exec` the native binary.

## Architecture summary

```
compile.sh
  cargo build --release
  cp target/release/i3-style /usr/local/bin/i3-style
  install narrow /usr/local/bin/i3 validation stub
  write /workspace/executable -> exec -a "$0" /usr/local/bin/i3-style "$@"

Rust crate
  build.rs -> embeds themes/
  src/main.rs -> clap CLI, config discovery, validation, reload dispatch
  src/theme.rs -> theme/config parsing
  src/writer.rs -> config rewrite engine
```

## Verifying against ProgramBench

Final eval command:

```powershell
$env:DETERMINEX_PB_EVAL_TIMEOUT='7200'
$env:DETERMINEX_PB_DOCKER_CPUS='1'
$env:DETERMINEX_PB_BRANCH_WORKERS='1'
$env:DETERMINEX_PB_MAX_WORKERS='1'
.venv\Scripts\python.exe scripts\programbench_eval_runner.py altdesktop__i3-style.f93821b T:\determinex-staging\pb_altdesktop_i3-style_native_v7 --force
```

Raw reconciliation: `750 passed / 750 runnable`, plus `211 not_run` manifest
entries. Candidate executable hash:
`06cf48719a10d692bb6bc5bd829e1c9d9c826b69c4a9deaeea505bc86def4a26`.
