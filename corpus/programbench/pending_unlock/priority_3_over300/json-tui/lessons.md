---
name: pb-locked-json-tui-lessons
description: Auto-drafted post-mortem for json-tui (lock 100%). Language: c. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# json-tui — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **c**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build json-tui from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v make >/dev/null 2>&1 && [ -f Makefile ]; then
    make 2>build.err || true
fi
if [ ! -f ./json-tui ] && command -v cmake >/dev/null 2>&1 && [ -f CMakeLists.txt ]; then
    mkdir -p build
    (cd build && cmake .. && cmake --build .) 2>>build.err || true
    find build -type f -perm -111 -name 'json-tui' -exec cp {} ./json-tui \; 2>/dev/null || true
fi
if [ ! -f ./json-tui ] && command -v g++ >/dev/null 2>&1; then
    g++ -O2 -std=c++17 -o json-tui $(find . -name '*.cpp' -not -path './build/*' | head -200) 2>>build.err || true
fi
chmod +x ./json-tui 2>/dev/null || true
if [ -f ./json-tui ]; then
    cp ./json-tui /usr/local/bin/json-tui
fi

chmod +x /usr/local/bin/json-tui 2>/dev/null || true

# Eval entry point. exec -a preserves argv[0] so name-based dispatch
# (e.g. /workspace/ungron -> --ungron flag) works correctly.
cat > executable <<'EXEC_EOF'
#!/usr/bin/env bash
exec -a "$0" /usr/local/bin/json-tui "$@"
EXEC_EOF
```

## Decisions recorded in compile.sh

### 1. Build json-tui from its canonical upstream source.

Build json-tui from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

## Cluster transfer notes

- Build pattern is the canonical c skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
