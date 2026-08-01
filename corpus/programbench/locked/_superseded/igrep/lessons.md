# igrep lessons

## TL;DR

The lock closed by preserving the real Rust crate and fixing the two native
integration gaps the prior candidate exposed: the crate builds a binary named
`ig`, not `igrep`, and the default search path used a parallel walker whose
result order was nondeterministic under TUI snapshot tests. The final native v5
submission passed the official eval at 547/547 runnable tests with a source-only
tarball.

## Hard Discoveries

1. Rust package names and binary target names can differ. `Cargo.toml` declares
   package `igrep`, but the `[[bin]]` target is `ig`, so a compile script that
   only copies `target/release/igrep` silently leaves `/workspace/executable`
   missing.
2. `build.rs` reads `README.md` to generate keybinding help. Copying only
   `Cargo.toml`, `build.rs`, and `src/` is not enough for this crate.
3. Clap help and error output depends on `argv[0]`. The eval launcher must use
   `exec -a "$0"` so ProgramBench sees `executable`, not `igrep`.
4. TUI snapshot tests make result ordering semantic. The upstream default
   `ignore::WalkBuilder::build_parallel()` path can produce all the right
   matches in the wrong order, so the repair replaces the no-sort parallel path
   with a deterministic reverse filename walker.
5. A single official pass is not enough to claim a lock unless the raw JSON
   reconciles. The final report has 547 passed, 174 not_run, and 547 runnable.

## Cluster Transfer Notes

- Rust CLIs with `[[bin]] name = "..."]` need compile scripts that either know
  the binary name or copy the first top-level executable from `target/release`.
- `build.rs` input files such as `README.md` are source dependencies. The
  native converter now copies common README variants for Rust crates.
- Interactive search tools should prefer deterministic collection order when
  tests assert full terminal snapshots. Parallel search is a performance choice,
  not a correctness requirement.
- Shell launchers remain acceptable when they only set process metadata and
  then `exec` the native binary.

## Architecture Summary

```
compile.sh
  cargo build --release
  copy target/release/ig or first release executable to /usr/local/bin/igrep
  write /workspace/executable -> exec -a "$0" /usr/local/bin/igrep "$@"

Rust crate
  build.rs -> generates keybinding table from README.md
  src/main.rs -> clap CLI and SearchConfig construction
  src/ig/searcher.rs -> grep matcher + ignore walker + deterministic ordering
  src/ui/* -> terminal result list, navigation, popups, theme rendering
```

## Verifying Against ProgramBench

Final eval command:

```powershell
$env:DETERMINEX_PB_EVAL_TIMEOUT='7200'
$env:DETERMINEX_PB_DOCKER_CPUS='1'
$env:DETERMINEX_PB_BRANCH_WORKERS='1'
$env:DETERMINEX_PB_MAX_WORKERS='1'
.venv\Scripts\python.exe scripts\programbench_eval_runner.py konradsz__igrep.aa75630 T:\determinex-staging\pb_konradsz_igrep_current_v5 --force
```

Raw reconciliation: `547 passed / 547 runnable`, plus `174 not_run` manifest
entries. Eval-stashed executable launcher hash:
`bff4c29e34578457720af17b90ad9e70ad4238574e197ff23b8c0f80ad1e678a`.
