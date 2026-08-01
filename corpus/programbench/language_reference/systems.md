# Systems/runtime conventions — applies regardless of implementation language

> Injected by `scripts/determinex_pb_reimpl.py::build_prompt()` for EVERY task, not just
> native-language ones. Distinct from `CROSS_TOOL_PITFALLS` (observable OUTPUT conventions —
> number formatting, which stream gets error text) and from the per-language reference files
> (language SYNTAX/stdlib API). This is the OS/container runtime the compiled binary or script
> actually executes in, and its conventions are the same no matter what language wrote the code.

## Exit codes

- The process exit code is only the low 8 bits (`code & 0xFF`) — a `return 300;`/`exit(300)`
  actually exits 44 (`300 % 256`). Never assume a larger value survives.
- **A process killed by a signal** reports exit code `128 + signal_number` to the parent shell/
  harness: SIGINT (2) → 130, SIGABRT (6) → 134, SIGKILL (9) → 137, SIGSEGV (11) → 139,
  SIGTERM (15) → 143. If observed reference behavior shows one of these exact codes for some
  input, that almost always means the REAL tool crashed/was killed on that input — reproducing
  the crash-cause (not just hardcoding the number) is what actually satisfies the test.
- **Language-specific panic/abort defaults** (when nothing else is specified): an unhandled Rust
  panic exits **101**; an unhandled Go panic exits **2**; a C++ uncaught exception calls
  `std::terminate` → `abort()` → exit **134** (128+SIGABRT); a C program that segfaults (null
  deref, buffer overrun into unmapped memory) exits **139**.
- This harness's own timeout convention (unrelated to the tool's own behavior, but shows up in
  logs/observations) is rc=**124** — if you see 124 in a reference observation, the REAL tool
  hung or ran long on that input; make sure your reimplementation doesn't introduce an infinite
  loop or blocking read on that same case.
- Conventional (not universal — verify against the actual per-tool probe): rc=0 success, rc=1
  generic runtime/IO error, rc=2 usage/argument error for `clap`-family Rust CLIs specifically
  (see `language_reference/rust.md`) — this 1-vs-2 split is NOT a language guarantee, it's a
  per-ecosystem convention some tools follow and others don't.

## TTY / terminal detection

- Real CLI tools frequently branch on whether stdout (or stdin) is a real terminal:
  `isatty(fd)` in C, `std::io::IsTerminal` in Rust (stable since 1.70), `term.IsTerminal` /
  `golang.org/x/term` in Go (stdlib-adjacent; without the module, check `stat` on the fd or
  assume non-TTY when running headless), `isatty()`/`os.isatty(fd)` conceptually in any language.
  Under the test harness, stdout is virtually always a **pipe**, not a TTY — so any "auto-detect
  color / auto-detect interactive mode" logic must correctly detect **non-interactive** and
  behave like a real CLI would when piped (colors off by default, no interactive prompts, no
  progress spinners that assume cursor control).
- **ncurses/TUI tools opening a terminal in a non-TTY context**: a real ncurses-based tool run
  with no controlling terminal fails immediately with an error like
  `"Error opening terminal: unknown."` — if the reference behavior for a "no TTY" case shows
  exactly this kind of failure (not real rendered output), reproduce the FAILURE, don't try to
  fake a rendered frame; the harness sometimes drives real TUI tests through a pty (tmux-backed)
  specifically so genuine rendering IS expected in those cases — check whether the specific
  observation was captured via a pty (real escape-sequence output) or a plain pipe (should fail
  or degrade) before deciding which behavior to reproduce.

## Environment variables

- `NO_COLOR` (any non-empty value) and `--no-color`/`--color` flags are a near-universal CLI
  convention for disabling ANSI output — honor both if the tool's probe shows ANSI at all.
- `HOME` and XDG variables (`XDG_CONFIG_HOME`, defaulting to `~/.config` when unset) are the
  common convention for where a CLI tool's config file lives, if the tool has one.
- `LANG`/`LC_ALL` affect locale-sensitive formatting (number/date separators, collation order)
  in some stdlib functions in some languages — if a reference case's output depends on locale,
  match the OBSERVED formatting literally rather than relying on the language's locale-aware
  default, since the test container's locale may not be predictable.
- An unset env var is not the same as one set to an empty string — check with the language's
  "does this exist" API (`std::env::var` → `Err`, Go `os.LookupEnv`, C `getenv` → `NULL`,
  C++ `std::getenv` → `nullptr`) rather than treating a lookup failure the same as `""`.

## Container / root-user runtime

- **The eval harness runs as root inside its container.** Any test that expects a permission
  error (chmod'd-unreadable file, protected directory) may behave differently than it would for
  a non-root user, because root bypasses most filesystem permission checks on Linux. If a
  reference case's expected behavior looks like it assumes a permission failure that root
  wouldn't actually hit, reproduce what the REAL reference binary does in THIS container
  (usually: the operation still succeeds), not what "normally" would happen for a regular user.
- All files created by your program during a test run are owned by root and world-writable by
  default umask — this is rarely something your code needs to handle explicitly, but don't add
  your own permission-check logic that assumes a non-root, restricted environment.

## stdio buffering

- When stdout is a pipe (the normal case under this harness), C/C++/Go/Rust standard I/O is
  typically **fully buffered**, not line-buffered — output may not actually reach the reader
  until the buffer fills or the program exits/flushes explicitly. If a test expects to see
  partial output before the process finishes (rare, but possible for a long-running or streaming
  tool), an explicit flush after each logical chunk may be required; for a normal single-shot CLI
  that just runs to completion and exits, relying on the implicit flush-on-exit is fine and is
  what most real tools do too — don't add unnecessary manual flushing that could reorder
  stdout/stderr relative to what the reference binary actually produced.
- If both stdout and stderr are written and a test checks their exact combined/interleaved
  order, be aware that unbuffered stderr can interleave with buffered stdout in ways your local
  manual testing (usually run in a real terminal, where stdout is line-buffered) won't reveal —
  match the reference's observed per-stream content, don't assume terminal-like interleaving.

## Encoding

- Assume UTF-8 for all text I/O unless a reference case specifically demonstrates otherwise.
  Byte-vs-character-count distinctions matter differently per language (see the per-language
  reference file for that language's specific `len`/indexing semantics) but the underlying
  encoding convention across this whole environment is UTF-8.
