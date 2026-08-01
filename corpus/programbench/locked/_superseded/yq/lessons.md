---
name: pb-locked-yq-lessons
description: Auto-drafted post-mortem for yq (lock 100%). Language: go. Eval-entry: unknown. Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# yq — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **go**. Eval entry point: **unknown**.

## Build recipe (from compile.sh)

```sh
#!/bin/bash
set -e
cd "$(dirname "$0")"
export PATH="/usr/local/go/bin:$HOME/go/bin:$PATH"
go build -o ./executable .
chmod +x ./executable
```

## Decisions

_No inline decision blocks found in compile.sh; author manually._

## Cluster transfer notes

- Build pattern is the canonical go skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (unknown) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
