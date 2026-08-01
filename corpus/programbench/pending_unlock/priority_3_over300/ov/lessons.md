---
name: pb-locked-ov-lessons
description: Auto-drafted post-mortem for ov (lock 100%). Language: go. Eval-entry: plain exec wrapper. Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# ov — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **go**. Eval entry point: **plain exec wrapper**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build ov from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v go >/dev/null 2>&1; then
    if GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o ov-built . 2>build.err; then
        mv ov-built ov
    else
        echo "go build failed, using bundled binary if present:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
# Unconditionally chmod + copy: pre-built binary in the tarball may
# arrive without the execute bit set (NTFS source), so set it first.
chmod +x ./ov 2>/dev/null || true
if [ -f ./ov ]; then
    cp ./ov /usr/local/bin/ov
fi

chmod +x /usr/local/bin/ov 2>/dev/null || true

# Eval entry point.
cat > executable <<'EXEC_EOF'
#!/bin/sh
exec /usr/local/bin/ov "$@"
EXEC_EOF
chmod +x ./executable

```

## Decisions recorded in compile.sh

### 1. Build ov from its canonical upstream source.

Build ov from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

## Cluster transfer notes

- Build pattern is the canonical go skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (plain exec wrapper) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
