# CEILING_CERT — nikolassv__bartib.6b9b5ce (T2)

## Result

```
passed=1856  failed=0  skipped=2  not_run=0  total=1858
```

Eval confirmed on Hetzner, 2026-06-14, compile version v9.

## Per-Skip Reasons

Both skipped tests are bidir variants (eval.tests.* + tests.*) of a single upstream
`@pytest.mark.skip`:

- `test_subcommands.TestSubcommandRecognition.test_subcommand_has_help[help]`
  - **Source location**: `/workspace/eval/tests/test_subcommands.py:53`
  - **Skip reason**: `"help subcommand doesn't support --help"`
  - **Nature**: Hardcoded `pytest.mark.skip()` call in the test file itself, not a marker on the test function signature. The test checks that `bartib help --help` exits 0 with help text, but bartib's `help` subcommand does not support `--help` flag.

## Structural Rationale

Bartib's `help` subcommand is a built-in Rust clap subcommand that ignores unknown
flags. Adding `--help` support to it would require modifying bartib's source to
explicitly handle `help --help` — a structural change to the binary that would
require editing the upstream codebase. The test fixture is designed around the
current behavior (no `--help` on `help`).

There is no wrapper or conftest trick that can make `bartib help --help` return
exit 0 with help text without modifying the binary itself. The skip is permanent
for this commit hash.

## Reference-Parity Evidence

- v7 eval (Hetzner): p=1854 f=0 sk=2 nr=1 total=1857 (nr=1 was test_edit_command_with_tmux, tmux not installed)
- v8 eval (Hetzner): p=1854 f=2 sk=2 nr=0 total=1858 (f=2 was test_help_does_not_support_help_flag fix regression)
- v9 eval (Hetzner, **canonical**): p=1856 f=0 sk=2 nr=0 total=1858

v9 installs tmux in compile.sh, resolving the nr=1. The 2 remaining items are
permanently skipped upstream tests. Both bidir variants (eval.tests.* + tests.*)
are accounted for.
