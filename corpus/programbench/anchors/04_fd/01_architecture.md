---
name: fd-architecture
description: Architecture for fd. Rust + clap + ignore + regex; parallel walker driven by rayon; exec subsystem with placeholder substitution; smart-case heuristic.
type: architecture
---

# fd — Architecture Blueprint

## Language choice

**Rust.** Justification:
1. Reference is Rust; the crates `clap`, `ignore`, `regex`, `rayon`, `globset` are mandatory dependencies — reproducing them in another language is more work than just using them.
2. PB containers ship `cargo/rustc 1.92`. `cargo build --release` is the standard build path.
3. The `ignore` crate (also from BurntSushi, the ripgrep author) handles `.gitignore`/`.fdignore`/`.ignore` semantics that are very hard to re-derive.
4. Rust's `regex` crate is the SAME engine fd's reference uses; output divergence on edge regexes is impossible.

Fallback: Python with `pathspec` + `regex` + `os.walk` is **not viable** for 100% — the gitignore semantics are too subtle.

## Core data structures (Rust)

### `Opts` (clap-derived)
```rust
#[derive(Parser)]
struct Opts {
    pattern: Option<String>,
    paths: Vec<PathBuf>,
    #[arg(short = 't', long = "type", value_enum)]
    file_type: Vec<FileType>,
    #[arg(short = 'e', long = "extension")]
    extensions: Vec<String>,
    #[arg(short = 'H', long = "hidden")]
    hidden: bool,
    #[arg(short = 'I', long = "no-ignore")]
    no_ignore: bool,
    #[arg(short = 'L', long = "follow")]
    follow: bool,
    #[arg(short = 'p', long = "full-path")]
    full_path: bool,
    #[arg(short = 'F', long = "fixed-strings")]
    literal: bool,
    #[arg(short = 'g', long = "glob")]
    glob: bool,
    #[arg(short, long = "ignore-case")]
    ignore_case: bool,
    #[arg(short = 's', long = "case-sensitive")]
    case_sensitive: bool,
    #[arg(long = "max-depth")]
    max_depth: Option<usize>,
    #[arg(long = "min-depth")]
    min_depth: Option<usize>,
    #[arg(long = "exact-depth")]
    exact_depth: Option<usize>,
    #[arg(short = 'S', long = "size", value_parser = parse_size)]
    size: Vec<SizeFilter>,
    #[arg(long = "changed-within")]
    changed_within: Option<String>,
    #[arg(long = "changed-before")]
    changed_before: Option<String>,
    #[arg(short = 'x', long = "exec", num_args = 1.., allow_hyphen_values = true, value_terminator = ";")]
    exec: Vec<String>,
    #[arg(short = 'X', long = "exec-batch", num_args = 1..)]
    exec_batch: Vec<String>,
    #[arg(short = '0', long = "print0")]
    null_separator: bool,
    #[arg(long = "color", default_value = "auto")]
    color: ColorMode,
    // ...
}
```

### `Filter` chain
A line-of-defense pipeline applied to each `DirEntry`:
```
gitignore_skip → hidden_skip → depth_check → type_filter → extension_filter →
size_filter → mtime_filter → name_match (regex/glob/literal) → emit
```

### `Exec` placeholder substitution
Templates with placeholders:
- `{}` → full path
- `{.}` → path without extension
- `{/}` → basename (with extension)
- `{//}` → parent directory
- `{/.}` → basename without extension

Runs per-result (`-x`) or batched (`-X`). Multiple `-x` chains run sequentially, separated by `;`.

## Module breakdown

```
src/main.rs            entrypoint
src/cli.rs             clap definitions + post-parse validation
src/walk.rs            ignore::WalkBuilder driver (parallel)
src/filter/mod.rs      Filter trait + chain
src/filter/regex.rs    pattern → RegexMatcher (smart-case)
src/filter/glob.rs     pattern → globset
src/filter/literal.rs  -F fixed-strings
src/filter/types.rs    FileType: f, d, l, x, e, p, s
src/filter/size.rs     +1k/-2m/=10b parsing + matching
src/filter/time.rs     --changed-within "1d", "30min" etc.
src/exec.rs            Exec template + spawn
src/output.rs          formatting, --null, color, -l (long format)
src/error.rs           ErrorReport with [fd error]: prefix
```

## Build script

`compile.sh`:
```bash
#!/bin/bash
set -e
# Cache dir on T: drive (PB containers preserve this between probes when re-running)
export CARGO_HOME=/tmp/cargo
export CARGO_TARGET_DIR=/tmp/target
cargo build --release 2>&1 | tail -20
cp target/release/fd ./executable
```

**Compile time risk**: 1.5-3 min cold. If retries are slow, use `cargo check` until logic is correct, then one final `cargo build --release` — but PB tests need a working binary, not just a passing check.

## Critical implementation decisions

### Decision 1: Use `ignore` crate, not custom walker
`ignore::WalkBuilder` handles `.gitignore`, `.fdignore`, `.ignore`, global git ignore, hidden-file rules — everything. Hand-rolling fails 50+ tests immediately.

```rust
use ignore::WalkBuilder;
let mut wb = WalkBuilder::new(&path);
wb.hidden(!opts.hidden)
  .ignore(!opts.no_ignore)
  .git_ignore(!opts.no_ignore)
  .git_global(!opts.no_ignore)
  .git_exclude(!opts.no_ignore)
  .max_depth(opts.max_depth)
  .follow_links(opts.follow);
let walker = wb.build_parallel();
```

### Decision 2: Smart-case at regex compile time
```rust
let case_insensitive = opts.ignore_case || (!opts.case_sensitive && pattern_is_all_lowercase(&pat));
let regex = RegexBuilder::new(&pat).case_insensitive(case_insensitive).build()?;
```

`pattern_is_all_lowercase` checks for any uppercase Unicode char.

### Decision 3: `-p` / `--full-path` matches against the FULL path
Without `-p`, fd matches against just the **basename** of each candidate. With `-p`, against the full path. **Easy to invert.** Default is basename.

### Decision 4: `-g` / `--glob` mutually exclusive with regex
When `-g` is given, the pattern is parsed as a glob (`globset` crate), not as regex. Implies `-F` semantics for plain strings.

### Decision 5: `-x cmd ARGS ;` parsing
`-x` consumes args until `;` or end-of-args. clap's `value_terminator = ";"` does this. The `;` itself is NOT passed to the command.

### Decision 6: `-X cmd ARGS` batch
Single command, all results passed as args at end. Subject to MAX_ARG_LEN — split into batches if exceeded.

### Decision 7: Color output
`--color auto` (default): emit ANSI codes only if stdout is a TTY. PB tests always pipe — so default is no color. Tests with `--color always` exercise the color path.

The color scheme (LS_COLORS-compatible):
- directory: `1;34` (bold blue)
- symlink: `1;36` (bold cyan)
- executable: `1;32` (bold green)
- file: default (no codes)

### Decision 8: Smart depth handling
Depth 0 = the search-root itself. fd reports the search root only when `--exact-depth 0` or `--min-depth 0`. Default `--min-depth 1` excludes the root.

### Decision 9: Output order
By default fd's parallel walker has **non-deterministic order**. PB tests likely sort or use `--threads 1`. Verify: if tests fail with order issues, force single-threaded with the env var or a flag.

## What NOT to implement (defer)

- `--owner user` Unix-only filter — implement only if eval shows tests using it.
- `--changed-within` time parsing — implement; cheap with `humantime` crate or hand-rolled.
- `--prune` — recent flag; verify version against the commit pin.
- `--strip-cwd-prefix` — small flag; defer until eval shows.
- Color customization via LS_COLORS env var — implement default scheme; honor LS_COLORS only if tested.
