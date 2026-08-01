---
name: pb-locked-seqtk-lessons
description: Auto-drafted post-mortem for seqtk (lock 100%). Language: c. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# seqtk — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **c**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build seqtk from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v gcc >/dev/null 2>&1; then
    if [ -f Makefile ]; then
        make 2>build.err || true
    fi
    if [ ! -f ./seqtk ]; then
        gcc -O2 -Wall -o seqtk *.c 2>>build.err || true
    fi
fi
chmod +x ./seqtk 2>/dev/null || true
if [ -f ./seqtk ]; then
    cp ./seqtk /usr/local/bin/seqtk
fi

chmod +x /usr/local/bin/seqtk 2>/dev/null || true

# Eval entry point. exec -a preserves argv[0] so name-based dispatch
# (e.g. /workspace/ungron -> --ungron flag) works correctly.
cat > executable <<'EXEC_EOF'
#!/usr/bin/env bash
exec -a "$0" /usr/local/bin/seqtk "$@"
EXEC_EOF
chmod +x ./executable

```

## Decisions recorded in compile.sh

### 1. Build seqtk from its canonical upstream source.

Build seqtk from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

## Cluster transfer notes

- Build pattern is the canonical c skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
