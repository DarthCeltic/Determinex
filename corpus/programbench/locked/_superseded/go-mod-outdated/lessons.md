---
name: pb-locked-go-mod-outdated-lessons
description: Auto-drafted post-mortem for go-mod-outdated (lock 100%). Language: go. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# go-mod-outdated — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **go**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build go-mod-outdated from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v go >/dev/null 2>&1; then
    if GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o go-mod-outdated-built . 2>build.err; then
        mv go-mod-outdated-built go-mod-outdated
    else
        echo "go build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
# Unconditionally chmod + copy: pre-built binary in the tarball may
# arrive without the execute bit set (NTFS source), so set it first.
chmod +x ./go-mod-outdated 2>/dev/null || true
if [ -f ./go-mod-outdated ]; then
    cp ./go-mod-outdated /usr/local/bin/go-mod-outdated
fi

chmod +x /usr/local/bin/go-mod-outdated 2>/dev/null || true

# Eval entry point. exec -a preserves argv[0] so name-based dispatch
# (e.g. /workspace/ungron -> --ungron flag) works correctly.
cat > executable <<'EXEC_EOF'
#!/bin/bash
exec -a "$0" /usr/local/bin/go-mod-outdated "$@"
EXEC_EOF
chmod +x ./executable
```

## Decisions recorded in compile.sh

### 1. Build go-mod-outdated from its canonical upstream source.

Build go-mod-outdated from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

## Cluster transfer notes

- Build pattern is the canonical go skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
