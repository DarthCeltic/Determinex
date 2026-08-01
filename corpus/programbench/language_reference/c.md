# C — language grounding for native ProgramBench reimplementation

> Injected by `scripts/determinex_pb_reimpl.py::build_prompt()` for every C task. This is
> language-level grounding, independent of any specific tool being reimplemented — not the
> upstream project's source, not a technique-RAG hit from another real project. No family
> convention file exists for C in `corpus/programbench/families/` (audited 2026-07-16 — the
> families/ system only covers rust_cli/go_cli/python_cli/node_cli and a handful of shell/text
> archetypes), so everything below is language grounding only, nothing absorbed.

## Build reality (exact, not approximate)

The harness compiles with: `cc -O2 -o <bin> main.c` (falling back to `gcc`/`clang` if `cc` is
unavailable) — see `scripts/determinex_observe.py::_compile_native()`. Consequences:
- **Single file, no `-std=` flag passed** — the compiler's *default* dialect applies (typically
  gnu17/gnu11 on a modern `cc`/`gcc`). Don't rely on a specific standard's exact feature set;
  stick to widely-portable C (C99-and-later features are safe; avoid anything genuinely
  compiler-specific beyond common GNU extensions like `__attribute__`, which are fine since the
  harness itself uses `cc`/`gcc`).
- **No external libraries.** Only what's in `<...>` from the C standard library / POSIX headers
  actually present on the build image — no vendored `.h` files, no `-l` linker flags.
- `-O2` optimization is on — undefined behavior (signed overflow, uninitialized reads, strict
  aliasing violations) is *more* likely to produce surprising output than under `-O0`.

## Core semantics a reimplementation actually trips on

- **Manual memory management**: every `malloc` needs a matching `free`; a leaked allocation
  won't fail compilation or usually even fail a test, but a **double-free or use-after-free**
  can crash (segfault, rc=139) non-deterministically, which is much worse for test stability
  than a leak. When in doubt, prefer a fixed-size stack buffer over a heap allocation for CLI
  tools that process bounded input.
- **No bounds checking**: `char buf[64]; strcpy(buf, argv[1]);` on a longer arg overflows the
  buffer — this is the single most common crash-inducing bug. Use `snprintf`/`strncpy` (and
  always null-terminate manually — `strncpy` does **not** guarantee null-termination if the
  source is >= the destination size) or size-check before copying.
- **Exit codes**: `return N;` from `main` or `exit(N);` — both set the process exit code to
  `N & 0xFF` (only the low 8 bits survive). A tool that tries to "return" a code >255 will not
  behave as naively expected.
- **`errno`**: set by many stdlib/POSIX calls on failure (`fopen`, `open`, `stat`, ...) but only
  meaningful **immediately** after a call that failed — read it right away, don't let another
  function call clobber it first. `perror()`/`strerror(errno)` give a real, POSIX-shaped message.
- **String literals vs mutable buffers**: a `char *s = "abc";` string literal is read-only —
  writing through it is undefined behavior (often a segfault). Use `char s[] = "abc";` (or a
  heap copy) if you intend to mutate it.

## Standard-library API surface for CLI tools

| Need | API |
|---|---|
| argv/argc | `int main(int argc, char *argv[])` |
| env vars | `getenv("NAME")` (returns `NULL` if unset — check before using) |
| read stdin | `fgets`/`getline` (POSIX, handles arbitrary line length) or `fread` for binary |
| write stdout/stderr | `printf`/`fprintf(stderr, ...)` |
| read a file | `fopen(path, "r")` + `fread`/`fgets`; check the return for `NULL` before use |
| write a file | `fopen(path, "w")` + `fwrite`/`fprintf`; always `fclose` |
| file exists / stat | `stat(path, &st)` (POSIX, available on the build image) |
| walk a directory | `opendir`/`readdir`/`closedir` (POSIX; recurse manually with your own stack) |
| run a subprocess | `system(cmd)` (simple, but shell-injection-prone — only safe with fixed,
  non-user-controlled command strings) or `fork`+`exec`/`posix_spawn` for real argument-vector control |
| string search/parsing | `strstr`, `strtok` (note: `strtok` is stateful/not reentrant — avoid
  nesting two `strtok` loops), `sscanf` for structured parsing, `strtol`/`strtod` for numeric
  parsing with error detection (check `endptr` to detect a failed/partial parse) |
| basic argv flag parsing | `getopt`/`getopt_long` (POSIX, available — genuinely usable here,
  unlike a "crate" in Rust) |

## Known traps

1. `strcpy`/`strcat`/`sprintf` on unbounded input — the classic buffer overflow. Use the
   length-checked variants (`snprintf`, `strncpy` + manual null-termination, or size-check first).
2. Forgetting to check `malloc`'s return for `NULL` before writing through the pointer.
3. Comparing `strcmp(a, b)` result to a boolean-like truthy check instead of `== 0` — `strcmp`
   returns 0 on equality, and many first drafts get this backwards.
4. Leaving a file handle unclosed on an early-return error path — not usually fatal for a short
   CLI run, but can matter for tests that check file locking/flush behavior.
5. Assuming `int` is 64-bit — it's conventionally 32-bit on the build platform; use `long`/
   `long long`/`int64_t` (`<stdint.h>`) for anything that needs to hold a large count or file size.
