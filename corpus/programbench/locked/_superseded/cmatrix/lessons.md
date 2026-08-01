---
name: pb-locked-cmatrix-lessons
description: Auto-drafted post-mortem for cmatrix (lock 100%). Language: c. Eval-entry: direct binary copy (binary inspected / streaming I/O). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# cmatrix — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **c**. Eval entry point: **direct binary copy (binary inspected / streaming I/O)**.

## Build recipe (from compile.sh)

```sh
#!/bin/bash
set -e
cd "$(dirname "$0")"
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-1772741726}"
if [ -f CMakeLists.txt ]; then
  cmake -S . -B build
  cmake --build build
  cp build/cmatrix ./executable 2>/dev/null || cp build/src/cmatrix ./executable
else
  if [ -f autogen.sh ]; then ./autogen.sh; fi
  if [ -f configure ]; then ./configure; fi
  make
  cp cmatrix ./executable 2>/dev/null || cp src/cmatrix ./executable
fi
chmod +x ./executable
```

## Decisions

_No inline decision blocks found in compile.sh; author manually._

## Cluster transfer notes

- Build pattern is the canonical c skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (direct binary copy (binary inspected / streaming I/O)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
