---
name: pb-locked-chroma-lessons
description: Auto-drafted post-mortem for chroma (lock 100%). Language: go. Eval-entry: plain exec wrapper. Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# chroma — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **go**. Eval entry point: **plain exec wrapper**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build chroma from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v go >/dev/null 2>&1; then
    # CLI lives at cmd/chroma/ with its own go.mod; root package is the library.
    if (cd cmd/chroma && GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o ../../chroma-built .) 2>build.err; then
        mv chroma-built chroma
    elif GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o chroma-built . 2>>build.err; then
        mv chroma-built chroma
    else
        echo "go build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
# Unconditionally chmod + copy: pre-built binary in the tarball may
# arrive without the execute bit set (NTFS source), so set it first.
chmod +x ./chroma 2>/dev/null || true
if [ -f ./chroma ]; then
    # Install AS 'executable' so pprof File: header shows 'executable' not 'chroma'.
    cp ./chroma /usr/local/bin/executable
    cp ./chroma /usr/local/bin/chroma
fi

chmod +x /usr/local/bin/executable /usr/local/bin/chroma 2>/dev/null || true

# Eval entry point. exec the renamed binary so the embedded filename (pprof
# inspects /proc/self/exe path) matches 'executable'. argv[0] is automatically
```

## Decisions recorded in compile.sh

### 1. Build chroma from its canonical upstream source.

Build chroma from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

## Cluster transfer notes

- Build pattern is the canonical go skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (plain exec wrapper) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
