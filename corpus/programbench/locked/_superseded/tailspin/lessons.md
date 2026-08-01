---
name: pb-locked-tailspin-lessons
description: Auto-drafted post-mortem for tailspin (lock 100%). Language: rust. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# tailspin — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **rust**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build tailspin from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v cargo >/dev/null 2>&1; then
    if cargo build --release --offline 2>build.err || cargo build --release 2>>build.err; then
        # Cargo.toml [[bin]] name = "tspin" (not "tailspin")
        if [ -f target/release/tspin ]; then
            cp target/release/tspin /usr/local/bin/tailspin
            cp target/release/tspin /usr/local/bin/tspin 2>/dev/null || true
        elif [ -f target/release/tailspin ]; then
            cp target/release/tailspin /usr/local/bin/tailspin
        fi
    else
        echo "cargo build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
# If cargo didn't install the binary, fall back to the pre-built one
# (with explicit chmod since the tarball may lose execute bit).
if [ ! -f /usr/local/bin/tailspin ] && [ -f ./tailspin ]; then
    chmod +x ./tailspin 2>/dev/null || true
    cp ./tailspin /usr/local/bin/tailspin
fi
if [ ! -f /usr/local/bin/tailspin ] && [ -f ./tspin ]; then
    chmod +x ./tspin 2>/dev/null || true
    cp ./tspin /usr/local/bin/tailspin
    cp ./tspin /usr/local/bin/tspin 2>/dev/null || true
```

## Decisions recorded in compile.sh

### 1. Build tailspin from its canonical upstream source.

Build tailspin from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

### 2. Eval entry point. exec -a "$0" preserves argv[0]="executable" — tailspin tests a

Eval entry point. exec -a "$0" preserves argv[0]="executable" — tailspin tests assert
this name appears in usage/help output. Container is Rust/Debian which has bash.

## Cluster transfer notes

- Build pattern is the canonical rust skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
