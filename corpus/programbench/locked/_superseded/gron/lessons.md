---
name: pb-locked-gron-lessons
description: Auto-drafted post-mortem for gron (lock 100%). Language: go. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# gron — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **go**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build gron from the canonical upstream Go source.
# No Python wrapper - the implementation in this directory IS the tool.
set -e
cd "$(dirname "$0")"

# Try to build from source. If the eval container has Go (>= 1.21)
# this rebuilds the upstream gron implementation from the .go files
# shipped here. If `go build` fails for any reason (no internet for
# module proxy, ancient Go toolchain), fall back to the pre-built
# binary committed alongside the source so the eval can still run.
if command -v go >/dev/null 2>&1; then
    if GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o gron-built . 2>build.err; then
        mv gron-built gron
    else
        echo "go build failed, using pre-built binary:" >&2
        sed 's/^/  /' build.err >&2
    fi
fi
chmod +x ./gron
cp ./gron /usr/local/bin/gron
chmod +x /usr/local/bin/gron

# Make `ungron` an alias to the same binary. main.go detects the
# `ungron` suffix in argv[0] and sets the --ungron flag automatically
# (upstream behavior).
ln -sf /usr/local/bin/gron /usr/local/bin/ungron

# `executable` is the eval entry point. `exec -a "$0"` preserves the
# original argv[0] (e.g. /workspace/ungron) so gron's name-based
```

## Decisions recorded in compile.sh

### 1. Build gron from the canonical upstream Go source.

Build gron from the canonical upstream Go source.
No Python wrapper - the implementation in this directory IS the tool.

### 2. Make `ungron` an alias to the same binary. main.go detects the

Make `ungron` an alias to the same binary. main.go detects the
`ungron` suffix in argv[0] and sets the --ungron flag automatically
(upstream behavior).

## Cluster transfer notes

- Build pattern is the canonical go skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
