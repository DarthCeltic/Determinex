---
name: pb-locked-pastel-lessons
description: Auto-drafted post-mortem for pastel (lock 100%). Language: rust. Eval-entry: direct binary copy (binary inspected / streaming I/O). Promote to a hand-authored lessons.md before publishing.
type: lessons
auto_generated: true
---

# pastel — Lessons (auto-draft)

> Locked at **100%**. Upstream language: **rust**. Eval entry point: **direct binary copy (binary inspected / streaming I/O)**.

## Build recipe (from compile.sh)

```sh
#!/bin/bash
set -e
cd "$(dirname "$0")"
export PATH="/usr/local/cargo/bin:$HOME/.cargo/bin:$PATH"
export CARGO_HOME="${CARGO_HOME:-$HOME/.cargo}"
cargo build --release
cp target/release/pastel ./executable
chmod +x ./executable
```

## Decisions

_No inline decision blocks found in compile.sh; author manually._

## Cluster transfer notes

- Build pattern is the canonical rust skeleton — see `docs/AGENTS_PROGRAMBENCH_STRATEGY.md` Section 1.
- Eval-entry form (direct binary copy (binary inspected / streaming I/O)) is reusable by same-class tools.

## TODO (human)

- Replace this auto-draft: add the single decision that closed the lock,
  the hard discoveries, and the upstream build command used to adjudicate.
