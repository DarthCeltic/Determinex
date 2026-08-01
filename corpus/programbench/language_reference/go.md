# Go — language grounding for native ProgramBench reimplementation

> Injected by `scripts/determinex_pb_reimpl.py::build_prompt()` for every Go task. This is
> language-level grounding, independent of any specific tool being reimplemented — not the
> upstream project's source, not a technique-RAG hit from another real project. CLI-convention
> notes below are absorbed from `corpus/programbench/families/wave1/go_cli/FAMILY.md` (a stub,
> orphaned pre-native-only-rule scaffold generator) rather than left unused or silently duplicated.

## Build reality (exact, not approximate)

The harness compiles with: `go mod init m` then `go build -o <bin> .` in a directory containing
a single `main.go` — see `scripts/determinex_observe.py::_compile_native()`. Consequences:
- **Single file, package main.** No existing `go.mod` dependency list to lean on — the module is
  created fresh and empty. Any `import` beyond the standard library will fail to resolve at
  build time (no network at build); **standard library only**.
- Everything must live in that one `main.go` — no separate files, no internal packages.

## Core semantics a reimplementation actually trips on

- **Explicit error returns**: Go has no exceptions. Every fallible stdlib call returns
  `(value, error)`; an unchecked `error` that later causes a nil-pointer dereference panics with
  a `panic: runtime error...` stack trace on stderr and exit code 2 — not the tool's real error
  message. Check every error explicitly.
- **`os.Exit(code)`** is the only way to control the process exit code from anywhere other than
  falling off the end of `main` (which exits 0). `os.Exit` does **not** run deferred functions —
  flush any buffered `os.Stdout`/files *before* calling it, not via `defer`.
- **Zero values**: an uninitialized `string` is `""`, an uninitialized `int` is `0`, an
  uninitialized pointer/slice/map is `nil`. A flag that wasn't passed on the command line will
  silently be its zero value unless you give it an explicit default — this is a common source of
  "flag defaults to empty instead of the tool's real default" test failures.
- **Slices vs arrays**: almost always want `[]T` (slice), not `[N]T` (fixed array) — slices are
  what `append`, string splitting, and most stdlib functions actually return/expect.
- **String vs `[]byte` vs `rune`**: Go strings are UTF-8 byte sequences; `len(s)` counts *bytes*,
  not characters. Iterating `for i, r := range s` gives you runes (Unicode code points) correctly;
  indexing `s[i]` gives you a raw byte. Tests with non-ASCII input will fail on naive byte-index
  logic that assumed 1 byte == 1 character.

## `stdlib`-only API surface for CLI tools

| Need | API |
|---|---|
| argv | `os.Args` (index 0 is the program name; real args start at index 1) |
| env vars | `os.Getenv("NAME")` (returns `""` if unset — use `os.LookupEnv` to distinguish unset from empty) |
| read stdin | `bufio.NewScanner(os.Stdin)` (line-by-line) or `io.ReadAll(os.Stdin)` |
| write stdout/stderr | `fmt.Println`/`fmt.Fprintln(os.Stderr, ...)` |
| read a file | `os.ReadFile(path)` → `([]byte, error)` |
| write a file | `os.WriteFile(path, data, perm)` |
| file exists / stat | `os.Stat(path)`; check `os.IsNotExist(err)` |
| walk a directory | `filepath.WalkDir(root, fn)` (recursive, stdlib, no external deps needed) |
| run a subprocess | `os/exec.Command(name, args...).Output()` / `.Run()` |
| minimal flag parsing | `flag` package (`flag.String`, `flag.Bool`, `flag.Parse()`) — note its
  defaults/error format do **not** match `cobra`'s; if the tool under test uses cobra-style output,
  hand-roll `os.Args` parsing instead of relying on `flag`'s own `-h` text |
| ANSI color | raw escape codes — no external color library available |
| JSON | `encoding/json` (real stdlib package, safe to use — this is genuinely in `std`) |
| regex | `regexp` (also genuinely in `std` — Go's regex IS stdlib, unlike Rust's) |

## CLI ecosystem conventions (absorbed from `families/wave1/go_cli/FAMILY.md`, a stub — verify against the actual probe, this family has few confirmed exemplars)

- Real Go CLIs commonly use `cobra` or `urfave/cli`, neither available here — reproduce their
  *observable* shape by hand from the probe, don't assume these defaults blindly:
  - `cobra`-style help typically shows a `Use:` line + an `Available Commands:` list.
  - Errors commonly go to stderr with no fixed prefix (varies per tool).
  - Common convention: rc=1 for runtime errors, rc=2 for usage/argument errors — but this is
    *less reliably true* for Go than for Rust/clap; confirm against the tool's actual probed
    exit codes before hard-coding this split.
  - Subcommand-style invocation is common: `<tool> <subcmd> [flags] [args]`.
- Config file conventions often follow `~/.config/<tool>/<name>.yml` (XDG-style), but this is a
  convention, not a language guarantee — only rely on it if the probe/spec confirms it.

## Known traps

1. Ignoring an `error` return and later hitting a nil dereference — produces a raw Go panic
   trace, not the tool's real error message. Always check `if err != nil`.
2. Relying on `flag` package's own `-h` output format when the real tool uses `cobra` — the
   observable help text will not match; write the help string by hand from the probe/spec.
3. Calling `os.Exit()` before flushing a buffered writer (`bufio.Writer`) — buffered output is
   silently lost since `os.Exit` skips deferred flushes.
4. Assuming `len(s)` on a Go string counts characters — it counts UTF-8 bytes; wrong for any
   test with multi-byte Unicode input.
5. Leaving a flag's zero value as the effective default instead of setting the tool's real
   documented default explicitly.
