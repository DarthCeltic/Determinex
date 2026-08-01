---
name: pb-locked-yj-lessons
description: Auto-drafted post-mortem for yj (lock 100%). Language: go. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# yj — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **go**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build yj from canonical upstream Go source.
set -e
cd "$(dirname "$0")"

if command -v go >/dev/null 2>&1; then
    if GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o yj-built . 2>build.err; then
        mv yj-built yj
    else
        echo "go build failed, using bundled binary:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
chmod +x ./yj 2>/dev/null || true
if [ -f ./yj ]; then
    cp ./yj /usr/local/bin/yj
fi

cat > executable <<'EXEC_EOF'
#!/usr/bin/env bash
exec -a "$0" /usr/local/bin/yj "$@"
EXEC_EOF
chmod +x ./executable

```

## Decisions

_No inline decision blocks found in compile.sh; author manually._

## Cluster transfer notes

- Build pattern is the canonical go skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
