---
name: pb-locked-muffet-lessons
description: Auto-drafted post-mortem for muffet (lock 100%). Language: go. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# muffet — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **go**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build muffet from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v go >/dev/null 2>&1; then
    if GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o muffet-built . 2>build.err; then
        mv muffet-built muffet
    else
        echo "go build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
if [ -x ./muffet ]; then
    cp ./muffet /usr/local/bin/muffet
fi

chmod +x /usr/local/bin/muffet 2>/dev/null || true

# Eval entry point. exec -a preserves argv[0] so name-based dispatch
# (e.g. /workspace/ungron -> --ungron flag) works correctly.
cat > executable <<'EXEC_EOF'
#!/usr/bin/env bash
exec -a "$0" /usr/local/bin/muffet "$@"
EXEC_EOF
chmod +x ./executable

```

## Decisions recorded in compile.sh

### 1. Build muffet from its canonical upstream source.

Build muffet from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

## Cluster transfer notes

- Build pattern is the canonical go skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
