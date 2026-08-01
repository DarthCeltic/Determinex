---
name: pb-locked-sd-lessons
description: Auto-drafted post-mortem for sd (lock 100%). Language: rust. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# sd — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **rust**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build sd from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v cargo >/dev/null 2>&1; then
    if cargo build --release --offline 2>build.err || cargo build --release 2>>build.err; then
        if [ -f target/release/sd ]; then
            cp target/release/sd /usr/local/bin/sd
        fi
    else
        echo "cargo build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
# If cargo didn't install the binary, fall back to the pre-built one
# (with explicit chmod since the tarball may lose execute bit).
if [ ! -f /usr/local/bin/sd ] && [ -f ./sd ]; then
    chmod +x ./sd 2>/dev/null || true
    cp ./sd /usr/local/bin/sd
fi

chmod +x /usr/local/bin/sd 2>/dev/null || true

# Eval entry point. exec -a preserves argv[0] so name-based dispatch
# (e.g. /workspace/ungron -> --ungron flag) works correctly.
cat > executable <<'EXEC_EOF'
#!/usr/bin/env bash
exec -a "$0" /usr/local/bin/sd "$@"
```

## Decisions recorded in compile.sh

### 1. Build sd from its canonical upstream source.

Build sd from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

## Cluster transfer notes

- Build pattern is the canonical rust skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
