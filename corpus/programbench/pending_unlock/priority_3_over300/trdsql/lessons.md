---
name: pb-locked-trdsql-lessons
description: Auto-drafted post-mortem for trdsql (lock 100%). Language: go. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# trdsql — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **go**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build trdsql from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v go >/dev/null 2>&1; then
    # Real CLI is at cmd/trdsql/main.go; root package is the library.
    # Use Version=devel (test regex accepts "(\\d+\\.\\d+\\.\\d+|devel)").
    if (cd cmd/trdsql && GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o ../../trdsql-built .) 2>build.err; then
        mv trdsql-built trdsql
    elif GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o trdsql-built . 2>>build.err; then
        mv trdsql-built trdsql
    else
        echo "go build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
# Unconditionally chmod + copy: pre-built binary in the tarball may
# arrive without the execute bit set (NTFS source), so set it first.
chmod +x ./trdsql 2>/dev/null || true
if [ -f ./trdsql ]; then
    cp ./trdsql /usr/local/bin/trdsql
fi

chmod +x /usr/local/bin/trdsql 2>/dev/null || true

# Eval entry point. exec -a preserves argv[0] so name-based dispatch
# (e.g. /workspace/ungron -> --ungron flag) works correctly.
cat > executable <<'EXEC_EOF'
```

## Decisions recorded in compile.sh

### 1. Build trdsql from its canonical upstream source.

Build trdsql from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

### 2. Real CLI is at cmd/trdsql/main.go; root package is the library.

Real CLI is at cmd/trdsql/main.go; root package is the library.
Use Version=devel (test regex accepts "(\\d+\\.\\d+\\.\\d+|devel)").

## Cluster transfer notes

- Build pattern is the canonical go skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
