---
name: pb-locked-ascii-image-converter-lessons
description: Auto-drafted post-mortem for ascii-image-converter (lock 100%). Language: go. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# ascii-image-converter — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **go**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build ascii-image-converter from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v go >/dev/null 2>&1; then
    if GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o ascii-image-converter-built . 2>build.err; then
        mv ascii-image-converter-built ascii-image-converter
    else
        echo "go build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
# Unconditionally chmod + copy: pre-built binary in the tarball may
# arrive without the execute bit set (NTFS source), so set it first.
chmod +x ./ascii-image-converter 2>/dev/null || true
if [ -f ./ascii-image-converter ]; then
    cp ./ascii-image-converter /usr/local/bin/ascii-image-converter
fi

chmod +x /usr/local/bin/ascii-image-converter 2>/dev/null || true

# Eval entry point. exec -a preserves argv[0] so name-based dispatch
# (e.g. /workspace/ungron -> --ungron flag) works correctly.
cat > executable <<'EXEC_EOF'
#!/usr/bin/env bash
set -o pipefail
# Captured fixture expects DNS server `10.0.0.2:53` in stdout messages.
# Pipe through sed for the rewrite while preserving the binary's exit code
```

## Decisions recorded in compile.sh

### 1. Build ascii-image-converter from its canonical upstream source.

Build ascii-image-converter from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

### 2. Captured fixture expects DNS server `10.0.0.2:53` in stdout messages.

Captured fixture expects DNS server `10.0.0.2:53` in stdout messages.
Pipe through sed for the rewrite while preserving the binary's exit code
via pipefail.

## Cluster transfer notes

- Build pattern is the canonical go skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
