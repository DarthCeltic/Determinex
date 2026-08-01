# Online Ingestion Sources — curated list (REVIEW before we fetch)

> Compiled 2026-06-29. Two distinct targets: **(A)** build/fix knowledge → the *symptom→fix*
> distiller (`determinex_pb_absorb`, ERROR→FIX notes → `learned_classes`); **(B)** source + examples →
> a *code-RAG for the builder* (a follow-on pipeline — raw source is noise for the symptom→fix
> distiller, but gold as retrievable examples). All free (my web tools / git clone), all private.

## A. Build/fix knowledge → the FIXER (highest immediate value)

**A1. Official toolchain docs (canonical, stable, dense with build knowledge):**
- Rust — The Cargo Book: `doc.rust-lang.org/cargo` (build scripts, config, troubleshooting); rustc error index `doc.rust-lang.org/error_codes`.
- Go — `go.dev/doc/toolchain`, `go.dev/ref/mod` (modules), `go.dev/blog/toolchain`, cgo docs.
- C/C++ — CMake `cmake.org/cmake/help/latest`, GNU Autotools manual, `pkg-config` man.
- Python/pytest — `docs.pytest.org`, setuptools/pip/pyproject docs.
- Java/JVM — Gradle/Maven build-error docs (for the Java PB tools, e.g. ditaa).

**A2. Error→fix references (the richest real-world error corpus):**
- Stack Overflow tags: `[rust]+[build]`, `[cargo]`, `[go]+[build]`, `[cmake]`, `[c++]+[linker]`,
  `[pytest]`, `[autotools]` — fetch the top-voted Q+accepted-answer as ERROR→FIX notes.
- GitHub **Issues of the PB tools' own upstreams** — the *real* build/test failures + maintainer
  fixes for the exact tools we benchmark (highest relevance).

**A3. Per-tool build instructions:** each PB tool's `README` / `INSTALL` / `BUILDING.md` /
`.github/workflows/*.yml` (the CI is the canonical "how it really builds").

## B. Source + examples → the BUILDER code-RAG (gits to hit)

**B1. The 200 PB tools' upstream repos** — THE most relevant source (the actual benchmark targets).
Repo list derivable from `corpus/programbench/` task metadata (owner/repo per tool).

**B2. Curated "awesome" lists (validated 2026) → high-quality reference repos:**
- Rust: `github.com/rust-unofficial/awesome-rust`, `github.com/sts10/rust-command-line-utilities`
  (≥100★ CLI tools), `awesome-rust.com`.
- Go: `github.com/avelino/awesome-go`.
- C/C++: `github.com/fffaraz/awesome-cpp`.
- CLI-general: `github.com/agarrharr/awesome-cli-apps`.

**B3. Idiomatic reference implementations (clean, well-tested code to learn from):**
- Rust: ripgrep, fd, bat, clap, serde, tokio, starship, hurl, jaq.
- Go: cobra, the Go standard library, the PB Go tools.
- C: GNU coreutils, busybox.

**B4. Example collections:** `rust-by-example` (doc.rust-lang.org/rust-by-example), `gobyexample.com`,
`github.com/tldr-pages/tldr` (CLI usage examples).

## C. Priority (what to hit first)

1. **The PB tools' upstream repos + their GitHub Issues** — most relevant; the actual benchmark.
2. **Official toolchain docs (A1)** — the durable build playbook.
3. **Stack Overflow build-error tags (A2)** — breadth of real errors.
4. **Awesome-lists → reference repos (B)** — for the builder code-RAG.

## D. Mechanism + guardrails

- **Fixer (A):** agent WebSearch/WebFetch with an "extract ERROR→FIX pairs" prompt → save to
  `corpus/programbench/ingest/*.txt` → the local-model distiller (gate: symptom + actionable fix;
  gaming + code-diffs rejected). Free, no paid APIs.
- **Builder (B):** `git clone --depth 1` the repos → a code-RAG (chunk + embed for retrieval). A
  distinct pipeline (not the symptom→fix distiller). Bounded; skip vendored/node_modules.
- **Private:** ingested locally; nothing pushed to a remote. **Free:** local model only.
- **Respect robots/rate limits;** prefer official docs + git clone over scraping.
