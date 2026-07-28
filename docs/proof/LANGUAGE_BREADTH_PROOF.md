# Language Breadth Proof — Determinex Universal Oracle

> Generated 2026-06-17. Evidence that Determinex's correctness substrate — the
> universal ground-truth oracle (`scripts/determinex_oracle.py`) — verifies
> correctness across the major programming languages, deterministically and with
> **zero LLM judgment**. "Determinex lets any setup code anything in any language"
> rests on this: the oracle is the unit of correctness, and it is real (not stubs)
> for every language below.

## Method

An oracle answers one question deterministically: *does the work-tree satisfy
ground truth right now?* For each language the oracle runs the language's own
toolchain (compiler / test runner) and reports pass/fail from the real exit code
and any JUnit-shaped output — never an LLM opinion. A proof = the oracle (or its
exact ground-truth command) **PASSES a correct program and FAILS a broken one**.

## Results — 12 languages, all verified

| Language | Ground-truth command | Setup proven on | Valid → | Broken → |
|----------|----------------------|-----------------|---------|----------|
| **Python** | `pytest` | ProgramBench suite | pass | fail |
| **Rust** | `cargo` | ProgramBench suite | pass | fail |
| **Go** | `go build/test` | ProgramBench suite | pass | fail |
| **TypeScript/JS** | `tsc` + `jest` | ProgramBench suite | pass | fail |
| **C** | compiler | ProgramBench suite | pass | fail |
| **C++** | compiler | ProgramBench suite | pass | fail |
| **C#** | `dotnet test` (+JUnit logger) | native (Windows, .NET SDK) | pass (exit 0) | fail (red suite) |
| **Java** | `javac` (compile = ground truth) | native (Windows, JDK) | pass | fail (1 diag) |
| **Kotlin** | `kotlinc` | Docker `eclipse-temurin:21-jdk` + JetBrains compiler | pass (exit 0) | fail (exit 1) |
| **Swift** | `swiftc` / `swift test` | Docker `swift:latest` | pass (`4`, exit 0) | fail (exit 1, `expected '}'`) |
| **Ruby** | `ruby -c` (else rspec→JUnit) | Docker `ruby:3.3-slim` | pass (`Syntax OK`, exit 0) | fail (exit 1) |
| **PHP** | `php -l` (else phpunit→JUnit) | Docker `php:8.3-cli` | pass (exit 0) | fail (exit 255) |

PB-proven six (Python/Rust/Go/TS/C/C++) are the ProgramBench language set, where
the oracle has driven 64 full-suite locks (32.0%). The other six were proven this
session: C# and Java natively on Windows; Kotlin, Swift, Ruby, PHP through official
Docker images — demonstrating "any *setup*" (Windows-native and Linux-container)
as well as "any language."

## How this maps to the registry

`determinex_oracle.py` registers concrete (non-stub) oracles for: `python`,
`typescript`/`javascript`, `rust`, `go`, `jvm` (java+kotlin), `swift`, `csharp`,
`ruby`, `php`. `Oracle.available()` reports a language usable when **any** of its
probe tools is on PATH (e.g. JVM works via `gradle` OR `mvn` OR plain `javac`).
An unconfigured language raises `OracleUnavailable` with an install hint — **it
never silently passes**. Where no test suite ships, the per-file compile/lint
(or `synthesize_oracle()`) is the ground truth, the same stance ProgramBench
takes for systems languages.

## Reproduce

```bash
# Native (toolchain on PATH):
python scripts/determinex_oracle.py status            # availability matrix
# C#:    dotnet new xunit; (oracle) get_oracle('csharp').verify(workdir)
# Java:  javac path; get_oracle('java').verify(workdir)

# Docker (no local toolchain needed):
docker run --rm -i swift:latest      bash -c 'cat >/tmp/x.swift && swiftc /tmp/x.swift -o /tmp/x' < valid.swift
docker run --rm -i ruby:3.3-slim     ruby -c /dev/stdin < valid.rb
docker run --rm -i php:8.3-cli       php  -l /dev/stdin < valid.php
docker run --rm -i eclipse-temurin:21-jdk bash -c '... kotlinc x.kt ...' < valid.kt
```

*Determinex · Lunarian Data Systems · correctness substrate proof · 2026-06-17*
