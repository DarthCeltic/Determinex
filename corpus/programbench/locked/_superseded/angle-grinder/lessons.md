---
name: pb-locked-angle-grinder-lessons
description: Auto-drafted post-mortem for angle-grinder (lock 100%). Language: rust. Eval-entry: direct binary copy (binary inspected / streaming I/O). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# angle-grinder — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **rust**. Eval entry point: **direct binary copy (binary inspected / streaming I/O)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build angle-grinder from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v cargo >/dev/null 2>&1; then
    if cargo build --release --offline 2>build.err || cargo build --release 2>>build.err; then
        if [ -f target/release/ag ]; then
            cp target/release/ag ./executable
        elif [ -f target/release/agrind ]; then
            cp target/release/agrind ./executable
        elif [ -f target/release/angle-grinder ]; then
            cp target/release/angle-grinder ./executable
        fi
    else
        echo "cargo build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
# If cargo didn't produce the binary, fall back to the pre-built one
# (with explicit chmod since the tarball may lose execute bit).
if [ ! -f ./executable ] && [ -f ./agrind ]; then
    chmod +x ./agrind 2>/dev/null || true
    cp ./agrind ./executable
elif [ ! -f ./executable ] && [ -f ./angle-grinder ]; then
    chmod +x ./angle-grinder 2>/dev/null || true
    cp ./angle-grinder ./executable
fi

```

## Decisions recorded in compile.sh

### 1. Build angle-grinder from its canonical upstream source.

Build angle-grinder from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

## Cluster transfer notes

- Build pattern is the canonical rust skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (direct binary copy (binary inspected / streaming I/O)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
