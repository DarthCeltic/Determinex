---
name: pb-locked-flamelens-lessons
description: Auto-drafted post-mortem for flamelens (lock 100%). Language: rust. Eval-entry: exec -a (argv0=executable, clap usage name). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# flamelens — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **rust**. Eval entry point: **exec -a (argv0=executable, clap usage name)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build flamelens from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v cargo >/dev/null 2>&1; then
    if cargo build --release --offline 2>build.err || cargo build --release 2>>build.err; then
        if [ -f target/release/flamelens ]; then
            cp target/release/flamelens /usr/local/bin/flamelens
        fi
    else
        echo "cargo build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
# If cargo didn't install the binary, fall back to the pre-built one
# (with explicit chmod since the tarball may lose execute bit).
if [ ! -f /usr/local/bin/flamelens ] && [ -f ./flamelens ]; then
    chmod +x ./flamelens 2>/dev/null || true
    cp ./flamelens /usr/local/bin/flamelens
fi

chmod +x /usr/local/bin/flamelens 2>/dev/null || true

# Eval entry point. argv[0]=executable so clap shows 'Usage: executable'.
cat > executable <<'EXEC_EOF'
#!/usr/bin/env bash
exec -a "executable" /usr/local/bin/flamelens "$@"
EXEC_EOF
```

## Decisions recorded in compile.sh

### 1. Build flamelens from its canonical upstream source.

Build flamelens from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

## Cluster transfer notes

- Build pattern is the canonical rust skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (argv0=executable, clap usage name)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
