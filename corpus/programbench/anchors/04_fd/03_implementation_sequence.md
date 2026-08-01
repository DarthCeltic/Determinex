---
name: fd-impl-sequence
description: fd build order. Walker first; pattern matching second; filters in cheap-to-expensive order; exec last.
type: implementation-sequence
---

# fd — Implementation Sequence

> **Cargo cold-build is 1.5-3 minutes.** Iterate with `cargo check` for quick feedback; only do `cargo build --release` when the logic is sound.

## Phase A — Walker + basic match (target: 35-50%)

1. **`ignore::WalkBuilder` walker** with default settings (hidden=excluded, gitignore=on). Iterate single-threaded for now. Gate: `fd .` lists files matching everything in cwd, except hidden/ignored.
2. **Regex pattern (basename only)**: `Regex::is_match(entry.file_name())`. Gate: `fd foo` finds files with `foo` in basename.
3. **Smart-case**: detect any uppercase char; case-insensitive if none. Gate: `fd Foo` is case-sensitive; `fd foo` matches `Foo` and `foo`.
4. **Output**: paths relative to search root, one per line, no trailing newline-after-empty.

## Phase B — Path & pattern modes (target: 60-72%)

5. **`-p` / `--full-path`**: regex against the entry's full relative path. Gate: `fd -p 'src/.*\.rs'`.
6. **`-F` / `--fixed-strings`**: literal substring. Gate: `fd -F .` matches every file (literal `.`).
7. **`-g` / `--glob`**: globset pattern. Gate: `fd -g '*.py'` matches Python files.
8. **`-i`, `-s` overrides**: explicit case-mode wins over smart-case.

## Phase C — Filters (target: 75-86%)

9. **`-t` type filter**: `f`, `d`, `l`, `x`, `e`. Gate: `fd -t d` lists directories only.
10. **`-e` extension filter**: case-insensitive on the extension. Gate: `fd -e PY` matches `.py` files.
11. **`-H` hidden**, **`-I` no-ignore**: toggle WalkBuilder flags. Gate: `fd -H` includes `.hidden_file`.
12. **`--max-depth`, `--min-depth`, `--exact-depth`**: pass to WalkBuilder. Gate: `fd -d 1` only direct children.
13. **`-S` size filter**: parse `+1k`, `-2m`, `=10b`. Gate: `fd -S +1m`.
14. **`--changed-within`, `--changed-before`**: parse durations + dates. Gate: `fd --changed-within 1d`.

## Phase D — Output formatting (target: 88-92%)

15. **`-0` / `--print0`**: NUL separator instead of newline.
16. **`-l` / `--list-details`**: ls-like long format with mode, owner, group, size, mtime.
17. **`--color always|auto|never`**: ANSI codes for type-based colorization (dirs blue, symlinks cyan, executables green).
18. **TTY detection for `--color auto`**: use `atty` crate or `IsTerminal` impl on `Stdout`.

## Phase E — Exec subsystem (target: 93-97%)

19. **`-x CMD args... ;`**: parse via clap `value_terminator = ";"`. Spawn one subprocess per result.
20. **Placeholder substitution**: `{}`, `{.}`, `{/}`, `{//}`, `{/.}` — replace in each arg before spawn.
21. **`-X CMD args...`**: batch — pass all results as final positional args. Split into batches if MAX_ARG_LEN exceeded (rare in tests).
22. **Multiple `-x` chains**: `fd -x foo {} \; -x bar {}` runs both per result.

## Phase F — Edge sweep (target: 98-100%)

23. **`-E` exclude pattern** (runtime; in addition to gitignore).
24. **`--no-ignore-vcs`** vs `--no-ignore` semantics.
25. **Symlink follow `-L`** with cycle detection.
26. **Mutual-exclusion errors** (`-g` and `-F` together → error).
27. **Multi-search-root** positional args `fd pat dir1 dir2`.
28. **`--threads N`** affects walker concurrency.
29. **Empty pattern** matches everything; explicit verification.
30. **Leading `./` in output** when search root is `.`.

## The 90→100% gap

Where this anchor's tail typically lives:

1. **Smart-case Unicode handling**. `Köln` must be uppercase; `λambda` must NOT be uppercase (no Unicode case distinction for Greek lambda lowercase letter).
2. **Gitignore re-include rules** (`!important.txt`).
3. **Exec placeholder edge cases** — `{/.}` for `foo.tar.gz` is `foo.tar` (only last extension stripped), not `foo`.
4. **Exec-batch arg-list overflow** with very long input.
5. **`-l` long format byte-perfect spacing** — column alignment must match reference exactly.
6. **Color codes for executable detection** — `S_IXUSR | S_IXGRP | S_IXOTH` check.
7. **Depth 0 / search-root behavior** — fd default excludes the root itself.
8. **`--no-ignore` + hidden** — hidden files come back unless `-H` also given.
9. **Pattern compilation errors** — emit `[fd error]: regex parse error: ...` exactly.
10. **Path separator** — Linux containers always `/`, but Windows-built test fixtures might leak `\` in expected output. (PB is Linux-only — non-issue in PB tests.)

## Failure-category triage

```
Group A — Walker semantics (gitignore, hidden, depth)
Group B — Pattern compilation (case, regex/glob/literal)
Group C — Filter semantics (type, extension, size, mtime)
Group D — Output formatting (color, -l, -0)
Group E — Exec semantics (placeholders, batching)
Group F — Error/exit-code mapping
```

Group A failures cluster around gitignore tests — fix once via `WalkBuilder` settings.

## Performance note

A 1.5-3min cold compile means each retry burns time. **Cache the `target/` directory** between attempts if PB containers permit. Set `CARGO_TARGET_DIR=/tmp/target` and reuse.

If cargo cold-build pushes attempts past the 5-minute Docker timeout, downgrade to `cargo build` (debug mode, ~30 sec) for early-phase iteration. Switch to `--release` only for final submission.
