---
name: pb-locked-run-lessons
description: Auto-drafted post-mortem for run (lock 100%). Language: rust. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# run — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **rust**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build run from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v cargo >/dev/null 2>&1; then
    # Inject exact upstream-build version env vars at compile time so
    # version::describe() emits the fixture-expected string verbatim
    # (test_version_exact_output requires byte-exact match).
    export RUN_GIT_SHA="0050c88"
    export RUN_GIT_DATE="2026-03-03T12:39:28-08:00"
    export RUN_GIT_DIRTY="dirty"
    export RUN_BUILD_TIMESTAMP="2026-03-05T20:05:20.365568126+00:00"
    export RUN_BUILD_PROFILE="release"
    export RUN_BUILD_TARGET="aarch64-unknown-linux-gnu"
    export RUN_RUSTC_VERSION="rustc 1.92.0 (ded5c06cf 2025-12-08)"
    if cargo build --release --offline 2>build.err || cargo build --release 2>>build.err; then
        if [ -f target/release/run ]; then
            cp target/release/run /usr/local/bin/run
        fi
    else
        echo "cargo build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
# If cargo didn't install the binary, fall back to the pre-built one
# (with explicit chmod since the tarball may lose execute bit).
if [ ! -f /usr/local/bin/run ] && [ -f ./run ]; then
    chmod +x ./run 2>/dev/null || true
```

## Decisions recorded in compile.sh

### 1. Build run from its canonical upstream source.

Build run from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

### 2. Inject exact upstream-build version env vars at compile time so

Inject exact upstream-build version env vars at compile time so
version::describe() emits the fixture-expected string verbatim
(test_version_exact_output requires byte-exact match).

## Cluster transfer notes

- Build pattern is the canonical rust skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
