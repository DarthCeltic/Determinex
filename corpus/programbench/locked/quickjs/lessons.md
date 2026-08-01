---
name: pb-locked-quickjs-lessons
description: Auto-drafted post-mortem for quickjs (lock 100%). Language: c. Eval-entry: plain exec wrapper. Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# quickjs — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **c**. Eval entry point: **plain exec wrapper**.

## Build recipe (from compile.sh)

```sh
#!/bin/sh
# Build quickjs from its canonical upstream source.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v gcc >/dev/null 2>&1; then
    if [ -f Makefile ]; then
        make qjs CONFIG_LTO= 2>build.err || make qjs 2>>build.err || make 2>>build.err || true
    fi
fi
# Upstream QuickJS Makefile produces `qjs` (and qjsc, etc.), not `quickjs`.
# Map qjs -> /usr/local/bin/quickjs for the test harness wrapper.
for cand in qjs ./qjs build/qjs quickjs ./quickjs; do
    if [ -x "$cand" ]; then
        cp "$cand" /usr/local/bin/quickjs
        break
    fi
done

if [ ! -x /usr/local/bin/quickjs ] && command -v gcc >/dev/null 2>&1; then
    ver="$(cat VERSION 2>/dev/null || echo dev)"
    if [ -x ./qjsc ] && [ -f repl.js ] && [ ! -f repl.c ]; then
        ./qjsc -s -c -o repl.c -m repl.js 2>>build.err || true
    fi
    gcc -O2 -g -Wall -fwrapv -D_GNU_SOURCE -DCONFIG_VERSION=\"${ver}\" \
        -o quickjs qjs.c repl.c quickjs.c libregexp.c libunicode.c cutils.c dtoa.c quickjs-libc.c \
        -lm -ldl -lpthread 2>>build.err || true
    if [ -x ./quickjs ]; then
        cp ./quickjs /usr/local/bin/quickjs
```

## Decisions recorded in compile.sh

### 1. Build quickjs from its canonical upstream source.

Build quickjs from its canonical upstream source.
This is a NATIVE implementation - no Python wrapper.

### 2. Upstream QuickJS Makefile produces `qjs` (and qjsc, etc.), not `quickjs`.

Upstream QuickJS Makefile produces `qjs` (and qjsc, etc.), not `quickjs`.
Map qjs -> /usr/local/bin/quickjs for the test harness wrapper.

## Cluster transfer notes

- Build pattern is the canonical c skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (plain exec wrapper) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
