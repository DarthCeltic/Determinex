---
name: fd-corpus-impact
description: What fd adds to the Determinex Oracle. The corpus's first Rust-portfolio fixture; sharkdp idiom training; gitignore-walker training pairs; smart-case unicode pairs.
type: corpus-impact
---

# fd — Corpus Impact

## What this teaches the Oracle

Locking fd adds the corpus's first **portfolio-idiom training set**: a single author's CLI conventions applied across multiple tools. Six new failure-category families:

1. **clap-derivation failure pairs**
   - `value_terminator = ";"` for multi-arg flags
   - `value_enum` for restricted choice flags
   - `num_args = 1..` for variadic positionals
   - Mutually exclusive flag groups
   These are Rust-specific; the corpus currently has thin Rust coverage.

2. **`ignore`-crate failure pairs**
   - `WalkBuilder.git_ignore(false)` vs `git_global(false)` vs `git_exclude(false)` distinction
   - Hidden-file vs ignored-file ordering
   - Depth-zero handling
   These are subtle and hard to derive from man pages; the WAL becomes the documentation.

3. **Smart-case Unicode failure pairs**
   - Greek/Cyrillic case-distinct
   - Combining-mark case detection
   - Surrogate-pair edge

4. **Exec-placeholder failure pairs**
   - Multiple-extension stripping (`foo.tar.gz` → `foo.tar` not `foo`)
   - Quoting edge cases when paths contain spaces
   - `-X` batching boundary

5. **`--color auto` plumbing pairs**
   - TTY detection on stdout vs stderr
   - Honoring `NO_COLOR` env var (NEW standard sharkdp follows)
   - Color codes survive pipes only when `--color always`

6. **sharkdp error-format pairs**
   - Brackets, lowercase binary name, colon-space
   - Where errors emit (stderr always)
   - Exit-code mapping

## What this makes faster beyond the immediate cluster

- **Every Rust CLI tool downstream of Determinex.** The Determinex project itself shells out to a Rust validator binary; the clap conventions become the canonical answer for every Rust subcommand the Oracle has to scaffold.
- **The `_lib/rs/walker.rs` fixture** is the answer for any "find files matching predicate, respect gitignore" task forever. That's a recurring pattern in dev tooling.
- **The `_lib/rs/exec.rs` fixture** is the answer for any "for each match, spawn a subprocess with placeholders" task — `xargs`-likes, build runners, batch processors.
- **The smart-case fixture** transfers to every search tool the Oracle ever scaffolds in any language.

## Compounding with already-locked tools

| Locked tool | Compounding effect |
|-------------|--------------------|
| zoxide      | None direct. zoxide is by `ajeetdsouza`, not sharkdp; uses different conventions. |
| yj          | None. |
| ripsecrets  | **Some.** ripsecrets is a regex-on-files tool (closer to ripgrep family). The gitignore walker may transfer; verify against ripsecrets's actual implementation when fd locks. |

## Compounding with currently-in-progress tools

| In-progress tool | Current % | Lift from fd lock |
|------------------|-----------|--------------------|
| htmlq          | 91.6% | None (jq cluster). |
| **shellharden** | 87/100 (1095/1292) | **Mostly exhausted fd-style lift.** The stdin/file-mode and syntax/suggest plumbing gains are in; the remaining gap is shell lexical correctness, not sharkdp-style CLI conformance. |
| csview         | ~81% | None. |
| **dutree**     | ~54% | **Indirect.** dutree's walker is conceptually similar to fd's but the codebase is by a different author. Some pattern transfer, but ~3-5% expected lift only. dutree's main gap is its tree-aggregation logic, not the walker. |

## Training data emitted

For a 1,405-test target with ~7 attempts: **~30-50 high-quality training rows**.

But: because the cluster is sharkdp-coherent, the **per-tool extra emissions** as siblings build on the fixture are higher quality than any other anchor's. ripgrep's later WAL pairs reuse fd's walker terminology, multiplying the cross-tool training value.

## Strategic value

**fd is the highest-density anchor for the cluster size.** Justification:
1. Five-tool author-coherent cluster (fd + ripgrep + hexyl + pastel + onefetch).
2. Lock-rate projection: 5 of 7 to 100% (highest of any cluster).
3. The reusable fixture set is the most general — usable beyond ProgramBench in any Rust CLI tooling task.
4. Determinex already uses Rust internally (frontend src-tauri); this corpus directly improves the Oracle's competence in Determinex's own primary language.

## Action when locked

1. Move artifact from `T:/determinex-programbench/<run>/sharkdp__fd.40d8eb3/source/` into `corpus/programbench/locked/fd/`.
2. Extract:
   - `corpus/programbench/_lib/rs/sharkdp_cli.rs`
   - `corpus/programbench/_lib/rs/walker.rs`
   - `corpus/programbench/_lib/rs/color.rs`
   - `corpus/programbench/_lib/rs/error.rs`
   - `corpus/programbench/_lib/rs/smart_case.rs`
   - `corpus/programbench/_lib/rs/exec.rs`
3. Append WAL training pairs to `data/programbench_corpus.jsonl`.
4. Update `corpus/programbench/README.md` status board.
5. **Do not spend the next shellharden pass on sharkdp conformance.** The 87 plateau says the next lift is a shell lexer/word model, documented in `in_progress/anordal__shellharden.6a6ffd4/iteration_log.md`.
6. Smoke-test ripgrep using the walker fixture — confirm projected high-cluster lift.
7. Commit with tag `programbench-anchor-4-locked`.
