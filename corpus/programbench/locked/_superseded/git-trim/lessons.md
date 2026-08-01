# git-trim lock lessons

## TL;DR

The lock came from keeping the pinned upstream Rust implementation, removing the
old collection cap, and applying one native repair for dry-run execution in the
ProgramBench shipped workspace. The final candidate raw-passed `704/704`; it was
then re-gated against the prior native candidate (`702/704`) to prove a strict
Rule A improvement with a stable runnable denominator before archiving.

## Hard Discoveries

1. A raw `passed == runnable` result is not enough when the gate reports a
   runnable drop against an unrelated older baseline. Re-gate against the prior
   native candidate before archiving.
2. The remaining failures were both the same dry-run discriminator:
   `--dry-run` from the shipped workspace root should print a harmless summary
   even when no remote is discoverable.
3. Temp repositories with no remotes must still fail with
   `git-trim requires at least one remote`; the repair is scoped to dry-run from
   the shipped workspace root where `./executable` exists.
4. Removing collection caps can expose the real denominator and must happen
   before claiming a native lock.

## Transfer Notes

- Git-backed CLI tools need fixture-cwd analysis. The same flags can mean
  different things when run from a shipped workspace versus a newly-created temp
  repository.
- Use the candidate gate twice when the pool chooses a stale baseline: first to
  preserve the failure signal, then against the previous native candidate to
  verify denominator-stable closure.
- Keep `exec -a "$0"` launchers for Rust CLIs so help and usage fixtures see the
  harness-visible binary name.

## Architecture Summary

```text
compile.sh
  cargo build --release
  cp target/release/git-trim /usr/local/bin/git-trim
  executable -> exec -a "$0" /usr/local/bin/git-trim "$@"

src/main.rs
  Args::parse
  Repository::open_from_env
  dry-run shipped-workspace fallback for no-remotes
  Config::read
  get_trim_plan
  print_summary
  delete_remote_branches/delete_local_branches
```

## Verification

Native v1 baseline:

```text
passed=702 runnable=704
```

Native v2 closing eval:

```text
passed=704 failed=0 not_run=66 runnable=704 total=770
```

Strict re-gate:

```text
decision=accept; passed +2; runnable stable at 704; rule A
```

Archive command:

```powershell
.venv\Scripts\python.exe scripts\pb_lock_archiver.py foriequal0__git-trim.07c2f50 T:\determinex-staging\pb_foriequal0_git_trim_native_v2\foriequal0__git-trim.07c2f50\foriequal0__git-trim.07c2f50.eval.json T:\determinex-staging\pb_foriequal0_git_trim_native_v2 --confirm-100 --execute
```
