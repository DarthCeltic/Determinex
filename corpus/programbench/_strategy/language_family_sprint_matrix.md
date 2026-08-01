---
name: pb-language-family-sprint-matrix
description: 25 ProgramBench language-family scaffold cards for parallel anchor/mass-run work.
type: sprint-runway
---

# ProgramBench Language-Family Sprint Matrix

Purpose: give Claude/Codex/Builder agents a ready runway for the next ProgramBench sprint without redoing discovery. Each family below has a default executable contract, compile strategy, first probes, and best-fit task shape.

Hard rule for every family: `compile.sh` must create a real root-level `./executable` file. Never symlink. Always run `scripts/programbench_image_preflight.py <instance_id> --source-dir <source>` before the first official eval.

## Shared First-Run Checklist

1. Read `task.yaml`, `tests.json`, and any golden resources with `scripts/determinex_programbench_probe.py`.
2. Build the upstream binary from the task source when tests appear contradictory.
3. Pick the smallest language-specific executable, not a universal god script.
4. Add smoke tests to `compile.sh` only for contract-critical behavior.
5. Package from the source root: `tar -czf submission.tar.gz -C source .`.
6. Run image preflight on source and tar before official eval.
7. Preserve passing tests; fix one failure family per eval cycle.

## Family Cards

| # | Family | Default executable | Compile shape | Best for | First probes |
|---|--------|--------------------|---------------|----------|--------------|
| 01 | Python | `main.py` copied to `executable` | `cp main.py executable` | parsers, text transforms, JSON/YAML, quick CLI clones | help/version, stdin/file parity, unknown flags |
| 02 | Bash/POSIX sh | generated shell script | `cp main.sh executable` | wrappers, file plumbing, small Unix filters | quoting, empty stdin, glob/no-glob behavior |
| 03 | AWK | shell launcher around `awk -f main.awk` | create launcher file | line-oriented table/text tools | FS/OFS, blank lines, numeric coercion |
| 04 | sed/regex shell | shell launcher | create launcher file | simple regex rewrite tools | GNU vs BSD flags, in-place flags, regex dialect |
| 05 | Go | native binary | `go build -o executable .` | network CLIs, concurrent walkers, clap-like tools | flag parser, path walking, stdout/stderr bytes |
| 06 | Rust | native binary | `cargo build --release`, copy binary | ripgrep/fd/fzf siblings, performance-sensitive tools | clap errors, UTF-8 lossiness, env vars |
| 07 | C | native binary | `cc -O2 -o executable *.c` | compression, byte filters, POSIX utilities | binary stdin/stdout, exit codes, locale |
| 08 | C++ | native binary | `c++ -O2 -std=c++17 -o executable *.cpp` | compression/search/index tools | binary safety, filesystem traversal |
| 09 | Node.js | copied JS launcher | `cp main.js executable` with shebang | JSON/HTML/package tools | npm-free runtime, ESM/CJS mismatch |
| 10 | TypeScript | transpile or JS handoff | `tsc` if present, else checked-in JS | typed ports where TS source is clearer | dependency-free emit, source maps off |
| 11 | Ruby | copied Ruby launcher | `cp main.rb executable` | Ruby-native CLIs, text formatters | option parser messages, encodings |
| 12 | PHP | copied PHP launcher | shell wrapper or executable PHP file | composer-style small CLIs | argv quirks, stream wrappers |
| 13 | Perl | copied Perl launcher | `cp main.pl executable` | regex-heavy legacy Unix tools | regex dialect, `@ARGV`, taint-free paths |
| 14 | Lua | shell launcher around `lua main.lua` | create launcher file | embeddable config/format tools | Lua version, nil/false outputs |
| 15 | Java | jar or shell launcher | `javac`, launcher calls `java Main` | JVM-native CLIs, XML/JSON tools | classpath, startup stderr, CRLF |
| 16 | Kotlin | jar or Java fallback | `kotlinc` if present, else Java port | Kotlin-origin CLIs | runtime availability, jar manifest |
| 17 | Scala | jar or Java fallback | `scalac` if present, else Java port | Scala-origin tools | collection ordering, JVM flags |
| 18 | C#/.NET | self-contained or script launcher | `dotnet build` if SDK exists | .NET-origin CLIs | runtime availability, path separators |
| 19 | PowerShell | `.ps1` plus shell launcher | launcher calls `pwsh`/`powershell` | Windows-shaped CLIs | quoting, CRLF, pipeline objects vs text |
| 20 | R | shell launcher around `Rscript` | create launcher file | stats/table tools | CSV NA/NaN, factor-free parsing |
| 21 | Julia | shell launcher around `julia` | create launcher file | numeric/table tools | startup cost, NaN/Inf formatting |
| 22 | Dart | compiled or `dart run` launcher | `dart compile exe` if available | Flutter/Dart-origin CLIs | SDK availability, Unicode output |
| 23 | Elixir/Erlang | escript or shell launcher | `mix escript.build` if available | BEAM-origin CLIs | atom/string output, startup |
| 24 | Haskell | native binary or runghc launcher | `ghc -O2` if available | parser-heavy functional CLIs | lazy IO, exact errors |
| 25 | Swift | native binary or fallback port | `swiftc -O` if available | Swift-origin CLIs | Foundation availability, UTF-8 paths |

## Default Source Layout

Use this inside each task work directory:

```text
source/
  compile.sh
  main.<family-ext>
  README_DETERMINEX.md
  probes/
    smoke.txt
```

`README_DETERMINEX.md` should include:

- instance id
- source family
- upstream language and version if known
- eval command used
- current score
- top remaining failure families
- exact preflight command

## Routing Rules

- Start in Python for unknown small tools unless binary I/O, speed, or upstream compatibility argues otherwise.
- Prefer Rust for fd/ripgrep/fzf/sharkdp siblings because clap-2/clap-3 messages and path walking dominate.
- Prefer Go for HTTP/network CLIs and tools with Go upstream dependencies.
- Prefer C/C++ for compression and byte-exact binary transforms.
- Prefer shell/AWK/sed only for narrow line filters with simple option surfaces.
- For rare families, use their card to decide whether native runtime is available; otherwise port semantics into Python while preserving the upstream CLI.

## Claude Launch Prompt

Use this verbatim when handing off a family/tool:

```text
You are working in Determinex ProgramBench. Read:
1. docs/PROGRAMBENCH.md
2. corpus/programbench/_strategy/language_family_sprint_matrix.md
3. corpus/programbench/_strategy/per_language_scaffolds.md
4. The relevant anchor pack under corpus/programbench/anchors/

Pick one tool/family only. Build a real root-level executable, run image preflight before official eval, preserve all passing tests, and fix one failure family per eval cycle. Do not edit eval fixtures unless upstream binary proves they are wrong.
```

