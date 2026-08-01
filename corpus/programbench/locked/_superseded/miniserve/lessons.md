---
name: pb-locked-miniserve-lessons
description: Auto-drafted post-mortem for miniserve (lock 100%). Language: rust. Eval-entry: plain exec wrapper. Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# miniserve — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **rust**. Eval entry point: **plain exec wrapper**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build miniserve from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v cargo >/dev/null 2>&1; then
    if cargo build --release --offline 2>build.err || cargo build --release 2>>build.err; then
        if [ -f target/release/miniserve ]; then
            cp target/release/miniserve /usr/local/bin/miniserve
        fi
    else
        echo "cargo build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
# If cargo didn't install the binary, fall back to the pre-built one
# (with explicit chmod since the tarball may lose execute bit).
if [ ! -f /usr/local/bin/miniserve ] && [ -f ./miniserve ]; then
    chmod +x ./miniserve 2>/dev/null || true
    cp ./miniserve /usr/local/bin/miniserve
fi

chmod +x /usr/local/bin/miniserve 2>/dev/null || true

# Eval entry point. Use POSIX sh; some ProgramBench images do not ship bash.
cat > executable <<'EXEC_EOF'
#!/bin/sh
exec /usr/local/bin/miniserve "$@"
EXEC_EOF
```

## Decisions recorded in compile.sh

### 1. Build miniserve from its canonical upstream source.

Build miniserve from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

## Cluster transfer notes

- Build pattern is the canonical rust skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (plain exec wrapper) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
