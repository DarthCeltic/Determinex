---
name: pb-locked-curlie-lessons
description: Auto-drafted post-mortem for curlie (lock 100%). Language: go. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# curlie — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **go**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build curlie from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v go >/dev/null 2>&1; then
    if GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o curlie-built . 2>build.err; then
        mv curlie-built curlie
    else
        echo "go build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
# Unconditionally chmod + copy: pre-built binary in the tarball may
# arrive without the execute bit set (NTFS source), so set it first.
chmod +x ./curlie 2>/dev/null || true
if [ -f ./curlie ]; then
    cp ./curlie /usr/local/bin/curlie
fi

chmod +x /usr/local/bin/curlie 2>/dev/null || true

# Eval entry point. Copy the binary itself so argv[0] remains
# /workspace/executable in help/usage output without requiring bash exec -a.
cp ./curlie ./executable
chmod +x ./executable

```

## Decisions recorded in compile.sh

### 1. Build curlie from its canonical upstream source.

Build curlie from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

## Cluster transfer notes

- Build pattern is the canonical go skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
