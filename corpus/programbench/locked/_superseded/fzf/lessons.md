---
name: pb-locked-fzf-lessons
description: Auto-drafted post-mortem for fzf (lock 100%). Language: go. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# fzf — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **go**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build fzf from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v go >/dev/null 2>&1; then
    if GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w -X main.version=0.68.0 -X main.revision=5676da4a" -o fzf-built . 2>build.err; then
        mv fzf-built fzf
    elif [ -d ./cmd/fzf ] && GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w -X main.version=0.68.0 -X main.revision=5676da4a" -o fzf-built ./cmd/fzf 2>>build.err; then
        mv fzf-built fzf
    elif [ -d ./cmd ]; then
        for main_go in $(find ./cmd -mindepth 2 -maxdepth 2 -name main.go | sort); do
            pkg="${main_go%/main.go}"
            if GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w -X main.version=0.68.0 -X main.revision=5676da4a" -o fzf-built "$pkg" 2>>build.err; then
                mv fzf-built fzf
                break
            fi
        done
        if [ ! -f fzf ]; then
            echo "go build failed, using bundled binary if present:" >&2
            sed 's/^/  /' build.err >&2
        fi
    else
        echo "go build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
if [ -f ./fzf ]; then
    chmod +x ./fzf 2>/dev/null || true
```

## Decisions recorded in compile.sh

### 1. Build fzf from its canonical upstream source.

Build fzf from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

### 2. Eval entry point. exec -a preserves argv[0] for help/usage tests that

Eval entry point. exec -a preserves argv[0] for help/usage tests that
expect the harness-visible executable name.

## Cluster transfer notes

- Build pattern is the canonical go skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
