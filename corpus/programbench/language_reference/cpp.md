# C++ — language grounding for native ProgramBench reimplementation

> Injected by `scripts/determinex_pb_reimpl.py::build_prompt()` for every C++ task. This is
> language-level grounding, independent of any specific tool being reimplemented — not the
> upstream project's source, not a technique-RAG hit from another real project. No family
> convention file exists for C++ in `corpus/programbench/families/` (audited 2026-07-16), so
> everything below is language grounding only, nothing absorbed.

## Build reality (exact, not approximate)

The harness compiles with: `c++ -O2 -std=c++17 -o <bin> main.cpp` (falling back to `g++`/`clang++`)
— see `scripts/determinex_observe.py::_compile_native()`. Consequences:
- **C++17, exactly** — safe to use `std::optional`, `std::variant`, `std::filesystem`,
  structured bindings (`auto [a, b] = pair;`), `if constexpr`. Do **not** use C++20 features
  (concepts, ranges, `std::format`, coroutines) — they will fail to compile.
- **Single file.** No separate headers/translation units, no build system, no external libraries
  beyond the standard library (no Boost, no fmtlib, no third-party JSON).

## Core semantics a reimplementation actually trips on

- **RAII, not manual free**: prefer `std::string`/`std::vector`/`std::unique_ptr` over raw
  `new`/`delete` — a raw `new` without a matching `delete` on every exit path (including
  exception paths) leaks; RAII containers/smart pointers clean up automatically even when an
  exception unwinds the stack.
- **Exceptions vs error codes**: an uncaught exception terminates the program via `std::terminate`
  — this prints an implementation-defined message (NOT the tool's real error wording) and exits
  with a nonzero code that varies by platform/compiler, not the code the real tool would give.
  Wrap fallible logic (`std::stoi` on bad input, `.at()` on an out-of-range index) in `try/catch`
  near the top of `main` if you want a clean, controlled error message + exit code.
- **`std::string` vs `char*`**: `std::string` owns/manages its buffer and handles embedded nulls
  and length correctly — prefer it over raw C-string manipulation everywhere except when calling
  a C API that specifically needs `const char*` (`.c_str()`).
- **`std::filesystem` (C++17, safe to use)**: `std::filesystem::exists(path)`,
  `std::filesystem::path`, `std::filesystem::directory_iterator` — real stdlib, no external
  dependency, genuinely available at `-std=c++17`.
- **Exit codes**: `return N;` from `main`, or `std::exit(N);` (does NOT run local-scope
  destructors on the way out — prefer a normal `return` from `main` unless you specifically need
  to bail out from deep in a call stack).

## Standard-library API surface for CLI tools

| Need | API |
|---|---|
| argv/argc | `int main(int argc, char *argv[])` |
| env vars | `std::getenv("NAME")` (from `<cstdlib>`; returns `nullptr` if unset) |
| read stdin | `std::getline(std::cin, line)` in a loop, or `std::cin >> x` for whitespace-delimited tokens |
| write stdout/stderr | `std::cout <<` / `std::cerr <<` |
| read a file | `std::ifstream` + `std::getline`/`.read()`; check `.is_open()`/`.good()` before use |
| write a file | `std::ofstream` |
| file exists / stat / walk a dir | `std::filesystem` (`exists`, `is_directory`,
  `directory_iterator`, `recursive_directory_iterator`) — genuinely stdlib at C++17, use it |
| run a subprocess | `std::system(cmd)` (same shell-injection caveat as C) — there is no
  stdlib process-spawn-with-argv-array API before C++26; `std::system` is what's actually available |
| numeric parsing with error detection | `std::stoi`/`std::stod` (throw `std::invalid_argument`/
  `std::out_of_range` on bad input — catch these explicitly rather than letting them propagate) |
| string search | `std::string::find`, `std::string_view` for non-owning slices,
  `<regex>` (genuinely stdlib, but notoriously slow — fine for CLI-scale input) |
| formatting output | `<iomanip>` (`std::setw`, `std::setprecision`) for column/precision control;
  `std::format` is **not available** (that's C++20) |

## Known traps

1. Letting `std::stoi`/`.at()` throw uncaught — produces an implementation-defined terminate
   message, not the tool's real "invalid input" error text. Catch explicitly near `main`.
2. Mixing `printf`-family calls with `std::cout` without `std::ios::sync_with_stdio(false)`
   awareness — if you disable sync for performance, do it once at the very top of `main` and then
   commit to one I/O style consistently, or output can interleave out of order.
3. Reaching for a C++20 feature (`std::format`, concepts, ranges `|` pipeline syntax) — compiles
   fine in your head, fails to compile under the harness's pinned `-std=c++17`.
4. Raw `new[]`/`delete[]` mismatches (`new` paired with `delete` instead of `delete[]`, or vice
   versa) — undefined behavior; avoid raw arrays entirely in favor of `std::vector`.
5. Comparing `std::string` to a C-string literal with `==` is fine and safe in C++ (operator
   overload) — don't over-correct by reaching for `strcmp` out of C habit; that's the C idiom,
   not the C++ one, and mixing them (e.g., `strcmp(str.c_str(), other.c_str())`) is needless.
