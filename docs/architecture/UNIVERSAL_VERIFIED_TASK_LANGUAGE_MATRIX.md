# Universal Verified Task Language Matrix

Determinex's benchmark adapters must preserve the native language of the task.
Python wrappers are allowed only when the source language is Python or the
benchmark explicitly tests a Python harness. Native-language validators are the
default oracle.

## Corpus Expansion Rule

The language matrix is now a benchmark campaign map, not just a lock list. Every
run must write one of:

```text
signed success trace
signed reject trace
signed infrastructure-failure trace
signed repair-task trace
```

Corpus coverage is tracked across language, framework, build system, failure
type, validator, source kind, license bucket, benchmark source, repair outcome,
safety outcome, and model/router used. Synthetic mutation traces provide
breadth, benchmark failures provide external relevance, and real project traces
provide narrative depth.

| Language | Primary validator | Project validator | Corpus target |
|---|---|---|---|
| Python | `python -m pytest -q` | pytest/unittest/ruff optional | repo repair, BigCodeBench |
| Bash | `bash -n`, command exit checks | shellcheck optional | Terminal-Bench, CLI tasks |
| Go | `go test ./...` | Go modules | SWE-bench multilingual, IDE repair |
| Rust | `cargo test --locked` | Cargo | ProgramBench, Aider Polyglot |
| TypeScript | `npx tsc --noEmit`, npm tests | npm/pnpm/yarn | SWE-bench Pro, frontend repos |
| JavaScript | npm tests | npm/pnpm/yarn | repo repair, browser tooling |
| Java | `javac`, `mvn test`, `gradle test` | Maven/Gradle/JUnit | IDE repair, DebugBench, enterprise tasks |
| C | `gcc`, Make, CMake | Make/CMake | DebugBench, systems repair |
| C++ | `g++`, Make, CMake | Make/CMake/gtest | DebugBench, IDE repair |
| Ruby | `ruby -c`, bundle/rake | Bundler | SWE-bench multilingual |
| PHP | `php -l`, composer tests | Composer/PHPUnit | SWE-bench multilingual |
| SQL | sqlite/postgres execution | schema/result comparator | BIRD, BIRD-Critic |

## Adapter Rule

Every adapter emits a `TaskSpec` with:

- `language` set to the real source language
- native `validation_commands`
- privacy/cloak policy
- retry budget
- scorer

No benchmark adapter should silently turn a Java, C++, Go, Rust, or TypeScript
repair into a Python-only task.

## Lock Acceptance Bars

Each language lock must cover:

- native project detection
- package/module/workspace discovery
- test discovery
- baseline verifier pass
- controlled mutation failure
- repair/restoration path
- native oracle pass after repair
- format/checker gate when available
- license/provenance metadata
- supply-chain/source safety traps
- HMAC-signed corpus record
- lock manifest

Go-specific traps already covered by `GO_REPAIR_LOCK_001`:

- `go:generate` with `curl | sh`
- `go:generate` environment exfiltration
- `init()` network calls
- unsafe `TestMain` shell execution
- cgo command injection
- suspicious local `replace` directives
- module path spoofing
- dirty `gofmt`

Initial Go extractor categories:

- nil pointer due to removed guard
- missing error check
- interface nil confusion
- JSON marshal/unmarshal mismatch
- table-test regression

C/C++ traps already covered by `NATIVE_C_CPP_REPAIR_LOCK_001`:

- Makefile `curl | bash`
- CMake `execute_process` network execution
- CMake `add_custom_command` network execution
- runtime `system()` shell/network execution
- missing license rejection
- native null-guard mutation and restoration

Initial native C/C++ extractor categories:

- null guard removal
- off-by-one
- header include failure
- linker symbol missing
- CMake config failure

TypeScript traps already covered by `TYPESCRIPT_REPAIR_LOCK_001`:

- `postinstall` curl pipe execution
- script environment exfiltration
- prompt injection in package metadata
- dirty `tsc --noEmit`
- `node_modules` exclusion
- optional-chain mutation and restoration

Initial TypeScript extractor categories:

- optional chain removal
- React prop mismatch
- async state bug
- DOM selector failure
- CSS/layout regression

SQL traps already covered by `SQL_ORACLE_LOCK_001`:

- blocks mutating SQL (`DROP`, `DELETE`, `UPDATE`, `INSERT`, `ALTER`, `CREATE`)
- blocks `PRAGMA writable_schema`
- blocks multi-statement SQL
- allows read-only `SELECT` / `WITH`
- normalizes unordered result sets
- preserves ordered comparison when requested
- signs SQL repair traces

Initial SQL oracle categories:

- schema load
- query execution error
- wrong result comparison
- predicate flip mutation
- repaired SQL verification

Browser agent traps already covered by `BROWSER_AGENT_LOCK_001`:

- `javascript:` URL blocking
- `data:text/html` URL blocking
- credential URL blocking
- local-network/IP-only URL blocking
- payment/PII form-submit blocking
- executable download blocking
- browser page prompt injection detection
- replay trace signing

Initial browser oracle categories:

- URL match
- DOM selector existence
- replay record
- signed `browser_trace` corpus row
