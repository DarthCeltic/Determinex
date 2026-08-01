# eva lock lessons

## TL;DR

The lock came from replacing the old Python scaffold with the pinned upstream
Rust source, building the real `eva` binary with `cargo build --release
--features build-binary`, and preserving the harness-visible executable name
with a Bash `exec -a "$0"` launcher. The final gap was not math behavior; it was
REPL history-banner compatibility across contradictory branch fixtures.

## Hard Discoveries

1. `eva`'s binary target is gated behind the `build-binary` Cargo feature, so a
   plain release build can succeed without producing `target/release/eva`.
2. Empty input is not one behavior in the ProgramBench surface. Some branches
   require numeric REPL output for empty stdin, while legacy relative-invocation
   branches require the missing-history banner on immediate EOF.
3. The history banner cannot be printed unconditionally. It regresses
   branch fixtures that compare stdout exactly for empty-line REPL input.
4. The launcher must preserve `argv[0]`; several CLI fixtures reason about the
   harness-visible executable name rather than the upstream binary name.

## Transfer Notes

- Rust CLIs with feature-gated binary targets need the exact upstream feature
  set in `compile.sh`, not just `cargo build --release`.
- REPL tools need branch-by-branch stdin shape analysis before patching prompts
  or banners. Treat empty argv, empty stdin, and immediate EOF as separate
  cases.
- Preserve `argv[0]` with `exec -a "$0"` for native CLIs whose usage/help or
  mode selection can depend on the invoked name.

## Architecture Summary

```text
compile.sh
  cargo build --release --features build-binary
  cp target/release/eva /usr/local/bin/eva
  executable -> exec -a "$0" /usr/local/bin/eva "$@"

src/main.rs
  clap parse -> command mode when INPUT is non-empty
             -> REPL mode when INPUT is empty
  REPL mode -> rustyline history load/save
            -> eval_expr with previous-answer state
            -> fmt::pprint for radix/fix formatting
```

## Verification

Closing raw eval:

```text
passed=963 failed=0 not_run=347 runnable=963 total=1310
```

Archive command:

```powershell
.venv\Scripts\python.exe scripts\pb_lock_archiver.py oppiliappan__eva.41ae245 T:\determinex-staging\pb_oppiliappan_eva_native_v4\oppiliappan__eva.41ae245\oppiliappan__eva.41ae245.eval.json T:\determinex-staging\pb_oppiliappan_eva_native_v4 --confirm-100 --execute
```
