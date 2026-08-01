# Rust — language grounding for native ProgramBench reimplementation

> Source of truth for how this reference is used: `scripts/determinex_pb_reimpl.py::build_prompt()`
> injects this file (truncated to a char budget) into the builder prompt for every Rust task.
> This is NOT the upstream project's source and NOT a technique-RAG hit from another real
> project — it's language-level grounding, independent of any specific tool being reimplemented.
> CLI-convention sections below are absorbed from `corpus/programbench/families/wave1/rust_cli/FAMILY.md`
> (an orphaned pre-native-only-rule scaffold generator — see that file's header note) rather than
> left unused or silently duplicated.

## Build reality (exact, not approximate)

The harness compiles with **exactly**: `rustc --edition 2021 -O -o <bin> main.rs` — see
`scripts/determinex_observe.py::_compile_native()`. Consequences:
- **Single file.** No `Cargo.toml`, no `mod other_file;`, no crate structure. Everything is one
  `main.rs`. Use `mod foo { ... }` **inline blocks** if you want internal namespacing.
- **No external crates.** `std` only — no `clap`, no `serde`, no `regex` crate. Argument parsing,
  JSON/TOML/CSV handling, and regex must all be hand-rolled from `std`.
- **Edition 2021** — safe to use `?` in `fn main() -> Result<...>`, array `IntoIterator`,
  disjoint closure capture. Do NOT rely on anything gated behind a later edition or nightly-only
  features (`-O` release build, stable `rustc`, no `#![feature(...)]`).

## Core semantics a reimplementation actually trips on

- **Ownership/borrowing**: a `String` moved into a function is gone at the call site unless you
  pass `&str`/`&String` or `.clone()`. CLI code almost always wants `&str` parameters and to only
  own strings at the point they're built (`format!`, `to_string()`) or read (`args: Vec<String>`).
- **Error handling**: prefer `Result<T, String>` or a small custom error enum over `unwrap()` in
  anything that touches user input or the filesystem — a panicking `unwrap()` on a missing file
  produces a *panic backtrace* on stderr and rc=101, not the tool's real "file not found" message
  and rc=1. Tests assert exact stderr wording + rc; a panic will fail both.
- **`std::process::exit(code)`** is how you actually control the exit code from `main()` — a bare
  `fn main()` returning normally always exits 0; `fn main() -> Result<(), E>` exits 1 on `Err` but
  prints `Error: {:?}` (Debug, not Display) unless you handle the error yourself first. Most CLIs
  should have `fn main() { std::process::exit(real_main()); }` with a `real_main() -> i32`.
- **Integer/string conversions**: `"5".parse::<i32>()` returns `Result`; a raw `.unwrap()` on
  malformed numeric input panics — tests that pass garbage into a `--count` flag expect a clean
  error message + rc=2, not a panic.

## `std`-only API surface for CLI tools

| Need | API |
|---|---|
| argv | `std::env::args().collect::<Vec<String>>()` (first element is argv[0]) |
| env vars | `std::env::var("NAME")` → `Result<String, VarError>`; `std::env::var_os` for non-UTF8 |
| read stdin | `std::io::stdin().lines()` or `.read_to_string(&mut buf)` |
| write stdout/stderr | `println!`/`eprintln!`, or `std::io::Write` on a locked/buffered handle for perf-sensitive loops |
| read a file | `std::fs::read_to_string(path)` → `io::Result<String>`; `std::fs::read` for bytes |
| write a file | `std::fs::write(path, contents)` |
| file metadata / exists | `std::path::Path::new(p).exists()`, `std::fs::metadata` |
| walk a directory | `std::fs::read_dir(path)` (non-recursive; hand-roll recursion via a stack/queue) |
| run a subprocess | `std::process::Command::new(prog).args([...]).output()` / `.status()` |
| exact error text for a missing file | `std::io::Error::kind() == ErrorKind::NotFound` → format your own POSIX-style message; **do not** print Rust's raw `Debug` error, tests check literal wording |
| ANSI color | raw escape codes (`"\x1b[32m"` ... `"\x1b[0m"`) — there is no `colored`/`termcolor` crate available |
| simple regex-like matching | `str::contains`, `str::starts_with`, `str::split`, or a hand-rolled glob matcher — the `regex` crate is unavailable |

## CLI ecosystem conventions (absorbed from `families/wave1/rust_cli/FAMILY.md`)

Most real Rust CLIs use `clap`, which is unavailable here — but the *tests* were written against
a real clap-based binary, so they still expect clap's exact conventions. Reproduce clap's
observable behavior by hand:

- **Help** (`-h`/`--help`): stdout, rc=0, contains the tool description + a `Usage:` line + an
  `Options:` section.
- **Version** (`-V`/`--version`): stdout, rc=0, exact format `"<tool> <semver>\n"`.
- **Unknown flag**: rc=**2** (not 1, not 255), wording
  `"error: unexpected argument '<flag>' found\n\nUsage: <tool> [OPTIONS]...\n\nFor more information, try '--help'.\n"`.
- **Missing value for a flag**: rc=2,
  `"error: a value is required for '<flag> <NAME>' but none was supplied\n"`.
- **Invalid enum value**: rc=2,
  `"error: invalid value '<v>' for '<flag> <NAME>'\n  [possible values: a, b, c]\n"`.
- **Runtime/IO errors** (file not found, etc.): rc=**1**, wording varies per tool — this is
  the split that costs the most tests when reversed: **argparse errors = 2, runtime errors = 1**.
- **Conflicting flags**: rc=1 (occasionally 2 — verify against the actual observed probe),
  `"error: the argument '<X>' cannot be used with '<Y>'"`.
- Errors go to stderr only; help/version go to stdout.
- Honor `--no-color` and the `NO_COLOR` env var if the tool uses ANSI at all.
- A flag like `--editor`/`--pager` should be stored as a plain string, **never** validated with
  a `which`-style existence check — tests commonly pass a program that isn't installed in the
  test container and still expect success.

## Known traps

1. `unwrap()`/`expect()` anywhere near user input or file I/O — turns a clean rc=1 error into a
   rc=101 panic backtrace. Tests check exact stderr text; panics never match.
2. Printing `{:?}` (Debug) instead of `{}` (Display) for an error — Rust's derived Debug output
   looks nothing like a real CLI's error wording.
3. Forgetting `std::process::exit()` — relying on `main`'s return value alone under-specifies the
   exit code for anything beyond the trivial 0/1 case.
4. Assuming ANSI escape codes are stripped by default — real clap/CLI tools only strip them when
   stdout isn't a TTY or `--no-color`/`NO_COLOR` is set; a test capturing a pipe expects them gone.
