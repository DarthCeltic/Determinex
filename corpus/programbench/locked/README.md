---
name: pb-locked-tools
description: Post-mortems for tools at 100%. Each subdirectory holds the locked source, the WAL training pairs, and the lessons-learned report.
type: locked-index
---

# Locked Tools

Tools at 100% on ProgramBench, with their post-mortems.

## Layout per locked tool

```
locked/<tool>/
├── source/                  ← exact files from the winning submission
│   ├── compile.sh
│   └── main.* (and friends)
├── lessons.md              ← what was hard, what we'd do faster next time
├── training_pairs.jsonl    ← the (error → fix) pairs from the build session
└── eval_report.json        ← the final eval output proving 100%
```

## Currently locked

| Tool | Locked on | Cluster | Notes |
|------|-----------|---------|-------|
| zoxide | (pre-2026-05-09) | (independent) | First lock |
| yj | (pre-2026-05-09) | jq cluster (peripheral) | YAML/JSON/TOML converter |
| ripsecrets | 2026-05-09 | fd cluster (peripheral) | Rust-faithful Python port. 935/935 testable, 2 xdist+pytest-dependency cascade skips. See `ripsecrets/lessons.md` for the 8 hard discoveries (combined-regex group walk, `m.lastindex` lies for nested alternation, etc.). |
| htmlq | 2026-05-09 | jq cluster (peripheral) | Rust-faithful Python port (BS4+html5lib+soupsieve). 2056/2056 testable, 2 infrastructure skips. See `htmlq/lessons.md` for the 8 hard discoveries — capstone: kuchiki `Descendants` iterator-invalidation quirk in `--remove-nodes` (verified against the real upstream binary built from source after the user caught me about to game the eval). |

| doxygen | 2026-06-03 | docs/config CLI | Native upstream C++ source. Raw `250/250` runnable passed; console score warning documented in `doxygen/README.md`. |
| fasttext | 2026-06-03 | C++ ML CLI | Native upstream C++ source. Raw `353/353` runnable passed; no Python tool wrapper. |

When each tool fully locks, populate its `lessons.md` from the WAL records and update `corpus/programbench/README.md` status board.
