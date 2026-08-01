# Family: go_cli  [STUB]

> Tools written in Go. Use `cobra`/`urfave-cli` for arg parsing typically.

Sprint exemplar: `cheat__cheat` — 3.91% → 6.51% (+2.60pp). Low lift — many tests need `$EDITOR` subprocess we can't fake.

## Status: STUB — needs filling

The Go family is underrepresented in sprint 1/2 exemplars. Build out as more Go tools are processed.

## Initial conventions (to verify with more probes)

- Help output via `cobra` typically has `Use:` line + `Available Commands` list
- Errors via stderr with no specific prefix
- rc=1 for runtime errors, rc=2 for usage errors (cobra default)
- Subcommands common: `<tool> <subcmd> [flags] [args]`

## Known traps from cheat

- `test_edit_remove` tests need `$EDITOR` to be invoked; scaffold can stub but loses these tests
- Config in YAML at `~/.config/<tool>/conf.yml`

## Exemplar tool

| Tool | Best | Best dir |
|---|---|---|
| `cheat__cheat` | 6.51% | `T:/determinex-programbench/determinex_pb_cheat_v1/` |
