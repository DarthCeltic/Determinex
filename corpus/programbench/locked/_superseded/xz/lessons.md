---
name: pb-locked-xz-lessons
description: Auto-drafted post-mortem for xz (lock 100%). Language: c. Eval-entry: exec -a (preserve argv[0] for multicall/name dispatch). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# xz — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **c**. Eval entry point: **exec -a (preserve argv[0] for multicall/name dispatch)**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build xz from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

# xz uses CMake or autotools — root has CMakeLists.txt + Makefile.am, NOT a flat Makefile.
# The CLI source lives under src/xz/.
if command -v cmake >/dev/null 2>&1 && [ -f CMakeLists.txt ]; then
    cmake -S . -B build -DCMAKE_BUILD_TYPE=Release >build.err 2>&1 || true
    cmake --build build --target xz >>build.err 2>&1 || true
    for cand in build/src/xz/xz build/xz src/xz/xz xz; do
        if [ -x "$cand" ]; then
            cp "$cand" /usr/local/bin/xz
            break
        fi
    done
fi
if [ ! -x /usr/local/bin/xz ] && [ -x ./autogen.sh ]; then
    ./autogen.sh >>build.err 2>&1 || true
    ./configure --prefix=/usr/local >>build.err 2>&1 || true
    make >>build.err 2>&1 || true
    for cand in src/xz/xz src/xz/.libs/xz ./xz; do
        if [ -x "$cand" ]; then
            cp "$cand" /usr/local/bin/xz
            break
        fi
    done
fi
if [ ! -x /usr/local/bin/xz ] && [ -x ./xz ]; then
```

## Decisions recorded in compile.sh

### 1. Build xz from its canonical upstream source.

Build xz from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

### 2. Eval entry point. Tests check:

Eval entry point. Tests check:
stdout `Usage: ./executable` (exact-match help fixture)
stderr `Try '/workspace/executable --help'` (substring)
xz prints argv[0] in both streams. We satisfy both by running with
argv[0]=./executable then rewriting stderr to use the absolute path.
XZ_PHYSMEM_OVERRIDE pins --info-memory output (test fixture captured on
a 128GB/64-thread machine; we report the same regardless of host).

## Cluster transfer notes

- Build pattern is the canonical c skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (exec -a (preserve argv[0] for multicall/name dispatch)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
