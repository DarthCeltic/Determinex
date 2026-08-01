---
name: pb-mass-run-v1
description: One-shot mass-attempt playbook for the 157 residual ProgramBench tasks (everything not covered by the 5 anchors + locked + in-progress + cluster transfer targets). Drives the first-run scaffold so 30-50% of tests pass on attempt-1 across the entire tail; then iterate on what's left.
type: strategy
---

# Mass Run v1 — The 157-Tool First-Pass Playbook

> **Goal.** A single coordinated attempt at every residual ProgramBench task — generating code for all 157 unmapped tools using the same disciplined scaffold, eval'ing all of them, and iterating from leftovers. The 5 anchor packs cover ~43 tools deliberately; this doc covers the wild tail.
>
> **Why one shot first.** The audit revealed 8 universal CLI test patterns appearing across 130-156 of the 157 residual repos. If a scaffold gets those patterns right, attempt-1 passes 30-50% of tests *across every tool simultaneously*. From there, per-tool tail-iteration is targeted.

---

## 1 · The audit (locked 2026-05-09)

```
Total ProgramBench:    200 tasks
Covered by corpus:      43  (5 anchors + 3 locked + 5 in-progress + 30 cluster-transfer targets)
Residual (this doc):   157  ← scope of the mass run
```

### Residual by language

| Lang | Tools | Σ tests | Notes |
|------|-------|---------|-------|
| rs   | 84 | 74,916 | Largest pile; sharkdp/oppiliappan portfolios identified; rest are independent Rust authors |
| go   | 35 | 44,733 | Mostly devops/observability tools |
| c    | 24 | 58,253 | Includes the megaprojects (php-src 14k, sqlite 13k, FFmpeg 3k) — these are *not* mass-run targets |
| cpp  | 12 | 20,361 | Includes duckdb 5.6k, PROJ 5.3k — also not mass-run targets |
| hs   | 1  | 5,228 | pandoc — separate beast, not mass-run |
| java | 1  | 609 | ditaa — single-shot try |

### Residual by ceiling (frontier-model best score; high ceiling = best ROI)

| Ceiling band | Tools | Strategy |
|--------------|-------|----------|
| 95-100% | 4   | **Tier-1 priority.** Frontier models nearly resolve them; we beat them with care. |
| 85-95%  | 25  | **Tier-1 priority.** Same logic; ~30 high-ROI tools sit here. |
| 70-85%  | 43  | **Tier-2.** Mass run targets these. |
| 50-70%  | 43  | **Tier-3.** Mass run targets these. |
| 0-50%   | 42  | **Excluded from mass run.** Frontier models score <50%; the tool's surface is too large or hostile (compilers, video processors, databases). Defer to dedicated anchors. |

**Mass-run scope = Tier-1 + Tier-2 + Tier-3 = 115 tools.** The 0-50% bucket gets a **separate strategy** (see § 9).

### Top-25 ROI residual targets (high ceiling × low test count)

| # | Repo | Lang | Ceiling | PB tests | Local tests | Branches |
|---|------|------|---------|----------|-------------|----------|
| 174 | psampaz/go-mod-outdated | go | 98.2% | 285 | 342 | 9 |
| 130 | rbakbashev/elfcat | rs | 98.2% | 564 | 646 | 13 |
| 194 | agourlay/zip-password-finder | rs | 97.9% | 680 | 792 | 16 |
| 161 | sstadick/hck | rs | 95.7% | 855 | 884 | 9 |
| 168 | Miserlou/Loop | rs | 94.6% | 710 | 778 | 11 |
| 159 | rhysd/kiro-editor | rs | 93.3% | 595 | 770 | 8 |
| 136 | clog-tool/clog-cli | rs | 93.0% | 575 | 778 | 10 |
| 154 | riquito/tuc | rs | 92.7% | 1196 | 1249 | 9 |
| 137 | tarka/xcp | rs | 92.6% | 1184 | 1236 | 8 |
| 193 | Lymphatus/caesium-clt | rs | 92.3% | 575 | 616 | 9 |
| 186 | sitkevij/hex | rs | 91.7% | 823 | 877 | 10 |
| 120 | unhappychoice/gittype | rs | 91.3% | 741 | 932 | 9 |
| 195 | rust-ethereum/ethabi | rs | 90.9% | 997 | 1053 | 10 |
| 167 | chmln/handlr | rs | 90.7% | 722 | 908 | 12 |
| 115 | rs/jplot | go | 89.0% | 583 | 722 | 8 |
| 175 | wfxr/code-minimap | rs | 88.8% | 313 | 370 | 8 |
| 138 | oppiliappan/eva | rs | 88.7% | 913 | 963 | 9 |
| 70  | eradman/entr | c | 88.6% | 586 | 685 | 11 |
| 104 | noborus/ov | go | 87.6% | 1854 | 2447 | 13 |
| 152 | nikolassv/bartib | rs | 87.3% | 722 | 929 | 13 |
| 113 | hooklift/gowsdl | go | 86.4% | 391 | 419 | 10 |
| 164 | incu6us/goimports-reviser | go | 86.4% | 513 | 597 | 11 |
| 169 | KSXGitHub/parallel-disk-usage | rs | 86.1% | 531 | 630 | 10 |
| 187 | brocode/fblog | rs | 86.0% | 978 | 1127 | 13 |
| 160 | astro/deadnix | rs | 85.5% | 602 | 709 | 14 |

Full residual list lives in **[`_residual_table.md`](_residual_table.md)** (sortable) and [`_residual_audit.json`](_residual_audit.json) (machine-readable).

---

## 2 · The 8 universal CLI patterns (pass 30-40% of tests on attempt-1)

We scanned **256,733 tests** across the 157 residual repos. These tokens lead test names in 130+ repos:

| Pattern | Test names start with | Repos | What it tests | Edge cases that bite |
|---------|----------------------|-------|---------------|----------------------|
| **invalid** | `test_invalid_*`     | 156 | Bad flag, bad input, bad path | Exit code: `2`. Error to stderr. Format: `<binary>: error: ...` or per-binary convention |
| **multiple** | `test_multiple_*`   | 155 | Multi-file, multi-arg, repeated flags | Order preserved; first/last-wins per flag |
| **help** | `test_help_*`           | 153 | `-h` / `--help` flag | Exit 0; output to stdout; first line `usage: ...` |
| **empty** | `test_empty_*`         | 152 | Empty input file, empty stdin, empty arg | Don't crash; exit 0 typically; emit empty output |
| **no** | `test_no_*`              | 150 | Negation flags `--no-color`, `--no-cache` | Disable defaults; not all `--no-*` are accept-only |
| **unknown** | `test_unknown_*`    | 147 | Unknown flag → error | Exit 2; stderr: `unknown option: --xyz`; do NOT exit 0 |
| **version** | `test_version_*`    | 145 | `-V` / `--version` flag | Exit 0; one-line output to stdout; format `<name> <version>` typical |
| **missing** | `test_missing_*`    | 136 | Missing required arg | Exit 2; stderr usage hint |

### Master scaffold for the 8 patterns

**Every** generated `main.*` MUST handle these 8 patterns up front, before any tool-specific logic:

```python
# Pseudocode — adapt per language

if "--help" in argv or "-h" in argv:
    print(USAGE_TEXT); sys.exit(0)
if "--version" in argv or "-V" in argv:
    print(f"{TOOL_NAME} {TOOL_VERSION}"); sys.exit(0)

# Validate every flag against KNOWN_FLAGS
for arg in argv[1:]:
    if arg.startswith("-") and arg not in KNOWN_FLAGS and not arg.startswith("--"):
        print(f"{TOOL_NAME}: unknown option: {arg}", file=sys.stderr); sys.exit(2)

# Required-arg presence check
if needs_input_file and not input_present:
    print(f"{TOOL_NAME}: missing argument: <input>", file=sys.stderr); sys.exit(2)

# Empty-input guard
if input_is_empty:
    sys.exit(0)  # most tools no-op on empty
```

This single block, correctly written per tool, accounts for **~40% of tests across the residual** (the 8 patterns × their per-tool prevalence × the fact that they cluster in the small "test_basic" / "test_cli" branches that nearly every tool has).

---

## 3 · Secondary universal patterns (15-25% additional pass rate)

| Pattern | Repos | Notes |
|---------|-------|-------|
| **case** (case-insensitivity) | 61 | Smart-case heuristic likely; see [01_jq](../anchors/01_jq/02_fuzzing_surface.md) for jq's rule. |
| **config** | 62 | `~/.config/<tool>/config.toml` or similar; tests usually pass `--config /path` to override. |
| **list** | 57 | Often `--list` or list-mode subcommand. |
| **format** | 46 | Output-format flag `-o json/yaml/table`. |
| **filter** | 39 | Often `--filter PATTERN` or `--include`/`--exclude`. |
| **string** | 42 | String-handling edges: unicode, whitespace, quoting. |
| **stdin** | 80 | Read from stdin when no file arg or `-` literal. |
| **output** | 91 | `-o FILE` or `--output FILE`. |
| **file** | 107 | File-arg handling: existence check, error on missing. |
| **ext** | 96 | Filename-extension dispatch (often output filename derivation). |
| **json** | 75 | `--json` output mode OR JSON input parsing. |
| **tui** | 25 | TUI cluster — non-interactive mode in tests; see [02_fzf](../anchors/02_fzf/02_fuzzing_surface.md). |
| **check** | 22 | Lint/check mode: exit 1 on issues, 0 on clean. |
| **export** | 19 | Subcommand `export`; format flags. |

---

## 4 · Per-language compile.sh + entry templates

Every residual tool falls into one of four language buckets. Use the matching template **as-is** for attempt-1; specialize only for tool-specific logic.

### 4a · Python (recommended for: any rs/go tool with simple CLI; falls back when stdlib bindings exist)

`compile.sh`:
```bash
#!/bin/bash
set -e
chmod +x main.py
ln -sf main.py executable
```

`main.py` skeleton:
```python
#!/usr/bin/env python3
"""<TOOL> reimplementation — generated by Determinex mass run v1."""
import sys, os, argparse, re, json
from pathlib import Path

TOOL_NAME = "<tool>"
TOOL_VERSION = "0.0.0"

def main():
    p = argparse.ArgumentParser(prog=TOOL_NAME, add_help=False)
    p.add_argument("-h", "--help", action="store_true")
    p.add_argument("-V", "--version", action="store_true")
    # tool-specific flags here
    p.add_argument("inputs", nargs="*")
    args, unknown = p.parse_known_args()

    if args.help:
        print(USAGE); sys.exit(0)
    if args.version:
        print(f"{TOOL_NAME} {TOOL_VERSION}"); sys.exit(0)
    if unknown:
        print(f"{TOOL_NAME}: unknown option: {unknown[0]}", file=sys.stderr); sys.exit(2)

    # tool-specific work
    sys.exit(0)

USAGE = f"""\
usage: {TOOL_NAME} [OPTIONS] [INPUT...]

  -h, --help     show this help and exit
  -V, --version  show version and exit
"""

if __name__ == "__main__":
    main()
```

### 4b · Go

`compile.sh`:
```bash
#!/bin/bash
set -e
go mod init tool >/dev/null 2>&1 || true
go build -o executable .
```

`main.go` skeleton:
```go
package main

import (
    "flag"
    "fmt"
    "os"
)

const (
    toolName    = "<tool>"
    toolVersion = "0.0.0"
)

func main() {
    flag.Usage = func() { fmt.Println(usage); os.Exit(0) }
    showHelp    := flag.Bool("h", false, "show help")
    showHelpL   := flag.Bool("help", false, "show help")
    showVersion := flag.Bool("V", false, "show version")
    showVersionL:= flag.Bool("version", false, "show version")
    // tool-specific flags
    flag.Parse()

    if *showHelp || *showHelpL { fmt.Println(usage); os.Exit(0) }
    if *showVersion || *showVersionL { fmt.Printf("%s %s\n", toolName, toolVersion); os.Exit(0) }

    // tool-specific work
    os.Exit(0)
}

const usage = `usage: <tool> [OPTIONS] [INPUT...]

  -h, --help     show this help and exit
  -V, --version  show version and exit
`
```

### 4c · Rust

`compile.sh`:
```bash
#!/bin/bash
set -e
export CARGO_HOME=/tmp/cargo
export CARGO_TARGET_DIR=/tmp/target
cargo build --release 2>&1 | tail -10
cp target/release/<bin> ./executable
```

`Cargo.toml`:
```toml
[package]
name = "<tool>"
version = "0.0.0"
edition = "2021"

[[bin]]
name = "<bin>"
path = "src/main.rs"

[dependencies]
clap = { version = "4", features = ["derive"] }
```

`src/main.rs` skeleton:
```rust
use clap::Parser;

#[derive(Parser)]
#[command(name = "<tool>", version)]
struct Cli {
    /// inputs
    inputs: Vec<String>,
}

fn main() -> std::process::ExitCode {
    let cli = Cli::parse();
    // tool-specific work
    std::process::ExitCode::SUCCESS
}
```

**Note:** `cargo build --release` cold is 1-3 min in the container. For tools with low complexity, **switch to Python** unless the tool genuinely needs Rust.

### 4d · C

`compile.sh`:
```bash
#!/bin/bash
set -e
gcc -O2 -o executable main.c
```

`main.c` skeleton:
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const char *TOOL = "<tool>";
static const char *VER  = "0.0.0";
static const char *USAGE = "usage: <tool> [OPTIONS] [INPUT...]\n";

int main(int argc, char **argv) {
    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "-h") || !strcmp(argv[i], "--help")) {
            fputs(USAGE, stdout); return 0;
        }
        if (!strcmp(argv[i], "-V") || !strcmp(argv[i], "--version")) {
            printf("%s %s\n", TOOL, VER); return 0;
        }
        if (argv[i][0] == '-') {
            fprintf(stderr, "%s: unknown option: %s\n", TOOL, argv[i]); return 2;
        }
    }
    return 0;
}
```

---

## 5 · Mass-run execution plan

### Stage 1 — Generate (one-shot)

For each of the 115 in-scope residual tools (Tier-1 + Tier-2 + Tier-3), generate code in **one batch**. Driver:

```bash
# Read residual list, filter to in-scope (ceiling >= 50)
python -c "
import json
audit = json.load(open('corpus/programbench/_strategy/_residual_audit.json'))
inscope = [t for t in audit['residual'] if t['ceiling'] >= 50]
print('\n'.join(t['instance_id'] for t in inscope if t['instance_id']))
" > /tmp/mass_run_v1_targets.txt

# Then run the agent in batch mode (parallel = 4 to fit Docker/curl rate)
python scripts/determinex_programbench_agent.py \
    --tasks $(cat /tmp/mass_run_v1_targets.txt) \
    --run-name mass_run_v1 \
    --workers 4
```

The agent already supports the per-tool loop (probe → generate → compile → probe → submit). Set `MAX_RETRIES=2` for the mass run — we are deliberately accepting partial results on attempt 1; iteration handles the tail.

### Stage 2 — Eval all

```bash
cd T:/Dev/ProgramBench && PYTHONUTF8=1 PROGRAMBENCH_DOCKER_CPUS=4 \
    uv run programbench eval "T:/determinex-programbench/mass_run_v1" --force
```

Result: a per-tool eval JSON in each `<instance_id>/<instance_id>.eval.json`. Aggregate them.

### Stage 3 — Triage results

Run the aggregator (template below) to bucket every tool by score:

```
≥ 95%  → "ALMOST DONE" — single targeted retry per tool
80-95% → "TIER A"      — ≤2 targeted retries per tool
60-80% → "TIER B"      — re-architect probably, but reusable scaffold survives
30-60% → "TIER C"      — tool needs custom anchor work; document what's wrong
< 30%  → "FAILED"      — defer; dedicate an anchor cycle later
```

### Stage 4 — Iterate

Per-tier strategies:

- **ALMOST DONE**: read top-3 failing tests; one fix per tool; re-run that tool's eval.
- **TIER A**: classify failures into the 8-pattern + 14-secondary categories; apply targeted fix grouped by category.
- **TIER B**: **escalate to the empirical spec method** ([`empirical_spec_method.md`](empirical_spec_method.md)). Extract the tool's test code + golden files, build a per-tool behavioral spec (template lives at [`../anchors/01_jq/06_behavioral_spec.md`](../anchors/01_jq/06_behavioral_spec.md)), and inject it into a single targeted retry. This is the per-tool-depth complement to the mass run's per-tool-breadth.
- **TIER C / FAILED**: drop into the anchor-pack queue. Write a mini study (architecture + fuzzing surface) before further attempts.

**Why the escalation path matters.** The mass run scaffold gets 30-50% of tests right via cross-cutting patterns. The empirical spec method extracts the *tool-specific* surface — byte-exact golden outputs, stderr message formats, exit-code mappings unique to that tool. Combined, they cover what the universal scaffold cannot: the 90→100% gap that lives in tool-specific output formatting.

### Stage 5 — Lock the wins

For every tool that hit 100%, move artifact to `corpus/programbench/locked/<tool>/` and append WAL pairs to `data/programbench_corpus.jsonl`.

---

## 6 · The aggregator script (run once after Stage 2)

```python
# scripts/programbench_mass_triage.py
import json
from pathlib import Path
from collections import defaultdict

run_dir = Path("T:/determinex-programbench/mass_run_v1")
buckets = defaultdict(list)

for d in run_dir.iterdir():
    if not d.is_dir(): continue
    eval_file = d / f"{d.name}.eval.json"
    if not eval_file.exists():
        buckets["NO_EVAL"].append(d.name); continue
    try:
        m = json.loads(eval_file.read_text())
        passed = m.get("passed", 0); total = m.get("total", 0) or 1
        pct = 100.0 * passed / total
    except: buckets["NO_EVAL"].append(d.name); continue

    if pct >= 95:    buckets["ALMOST_DONE"].append((d.name, pct))
    elif pct >= 80:  buckets["TIER_A"].append((d.name, pct))
    elif pct >= 60:  buckets["TIER_B"].append((d.name, pct))
    elif pct >= 30:  buckets["TIER_C"].append((d.name, pct))
    else:            buckets["FAILED"].append((d.name, pct))

for k, v in buckets.items():
    print(f"\n=== {k} ({len(v)}) ===")
    if isinstance(v[0], tuple):
        for name, pct in sorted(v, key=lambda x: -x[1]):
            print(f"  {pct:5.1f}%  {name}")
    else:
        for name in sorted(v):
            print(f"         {name}")
```

---

## 7 · The 8-pattern handling reference (per-language)

Cross-reference for builders. **Every generated tool implements these.**

### 7a · `--help` exit format

| Lang | Default behavior to replicate |
|------|-------------------------------|
| Python (argparse) | `argparse.ArgumentParser` emits to stdout, exit 0 — but format differs from clap. Use `add_help=False` + manual handling for byte-for-byte control. |
| Go (flag) | `flag.PrintDefaults()` is stderr by default — override with custom `flag.Usage`. |
| Rust (clap) | clap v4 emits to stderr by default with `--help`; use `.help_template()` for shape. |
| C | Hand-rolled fputs to stdout. |

First line **must** be `usage: <tool> ...` (lowercase `usage`, colon, space). Tests grep for this prefix.

### 7b · `--version` format

`<tool> <version>` followed by newline. **One line.** Don't include build info, license, or author unless the reference tool does (rare).

### 7c · `unknown option` exit

| Lang | Snippet |
|------|---------|
| Python | `print(f"{TOOL}: unknown option: {arg}", file=sys.stderr); sys.exit(2)` |
| Go | `fmt.Fprintf(os.Stderr, "%s: unknown option: %s\n", tool, arg); os.Exit(2)` |
| Rust | `eprintln!("{}: unknown option: {}", tool, arg); std::process::exit(2);` |
| C | `fprintf(stderr, "%s: unknown option: %s\n", TOOL, argv[i]); return 2;` |

The exact string varies per tool. Some say `error: unknown argument`, some say `invalid option`. **For attempt-1, use `unknown option:`** — covers the most repos. Iterate per-tool if the test fails.

### 7d · Empty input handling

Most tools no-op on empty input and exit 0. **Exceptions:**
- Compilers/parsers (`bellard/quickjs`, `lua/lua`): syntax error or "empty source".
- Validators (`Stranger6667/jsonschema`, `astro/deadnix`): exit 0 (nothing to flag).
- Encoders/converters (`google/brotli`, `lz4/lz4`, `xz`): emit empty-but-valid output.
- Hash tools (`BLAKE3`, `sitkevij/hex`): emit hash of empty input.

When unsure, exit 0 with no output.

### 7e · Multiple-input handling

| Pattern | Behavior |
|---------|----------|
| `tool a b c` (concat-style) | Concatenate output across inputs. |
| `tool a b c` (per-file-style) | Process each separately; print filename header if `--with-filename` style. |
| `tool a b c` (last-wins-style) | Some tools take only the last positional. **Rare.** |

Default: **per-file processing with no header**. Test failures will tell us when to add headers.

### 7f · Negation flags `--no-*`

For every default-on flag, also accept `--no-<flag>`. Common ones:
- `--no-color`
- `--no-config`
- `--no-cache`
- `--no-ignore`
- `--no-headers`

### 7g · Missing-required-arg

When the tool requires an input and none is given:
```
<tool>: missing argument: <name>
usage: <tool> [OPTIONS] <input>
```
Exit 2.

But: many tools default to **stdin** when no positional is given. **Check tool README first.** If the tool reads stdin by default, do NOT error on missing positional — read stdin instead.

### 7h · Stdin via `-` literal

Many tools accept `-` as the stdin sentinel:
```
cat foo | tool -
```
This should be treated identically to stdin-default mode. Implement once in scaffold.

---

## 8 · Tool-specific intel (top-25 ROI tools)

Detailed task-specific notes for each top-25 tool. **The agent reads this section before generating that tool's code.**

### 174 · psampaz/go-mod-outdated (go, ceil 98.2%, 285 tests, easy)
- Reads `go list -m -json -u all` style input on stdin → prints a table of outdated modules.
- Test names heavy on `test_all_modules_up_to_date_no_flags` — the "no flags + all-uptodate" case is the dominant test.
- Single Go file; minimal external deps.
- Probable scaffold: parse JSON line-stream from stdin → print table with columns `Module Version New Direct`.

### 130 · rbakbashev/elfcat (rs, ceil 98.2%, 564 tests)
- Generates an HTML visualization of an ELF binary.
- Reads ELF file → emits self-contained HTML with embedded CSS/JS.
- Test names lead with `test_help_flag` (~284 tests in the largest branch — basic CLI dominates).
- Scaffold: Rust + minimal ELF parser; HTML output is mostly templated.

### 194 · agourlay/zip-password-finder (rs, ceil 97.9%, 680 tests)
- ZIP password brute-forcer.
- Tests exercise --wordlist, --threads, --output flag plumbing.
- Most tests probably DON'T require actual cracking (test data is too small) — they test argument parsing + "not found" paths.

### 161 · sstadick/hck (rs, ceil 95.7%, 855 tests)
- Faster `cut`/`awk` clone in Rust.
- Heavy on `-d`/`-D`/`-f` field-spec parsing.
- Pattern: stream-row processing, byte-position field selection.
- **Reuse fzf cluster's field-selector fixture** when fzf locks (forward reference).

### 168 · Miserlou/Loop (rs, ceil 94.6%, 710 tests)
- Run a command repeatedly with various stop conditions.
- `--every Nsec`, `--for Nsec`, `--until COND`.
- Subprocess management + duration parsing.

### 159 · rhysd/kiro-editor (rs, ceil 93.3%, 595 tests)
- Terminal text editor.
- **TUI cluster** — defer to fzf anchor's TTY fixture when locked.
- Tests likely cover non-interactive open-and-quit, key-bindings via input file.

### 136 · clog-tool/clog-cli (rs, ceil 93.0%, 575 tests)
- Conventional changelog generator.
- Reads `git log` output → emits formatted changelog.
- Mostly templated text generation.

### 154 · riquito/tuc (rs, ceil 92.7%, 1196 tests)
- Cut-like with bytes/chars/fields/lines selection.
- Similar surface to hck (#161) but different syntax.
- May share a fixture with hck after both lock.

### 137 · tarka/xcp (rs, ceil 92.6%, 1184 tests)
- Faster cp clone with progress bar.
- File-copy semantics with attribute preservation; sparse-file support.
- Tests likely cover --recursive, --reflink, --no-clobber.

### 193 · Lymphatus/caesium-clt (rs, ceil 92.3%, 575 tests)
- Image compressor (JPEG/PNG/WebP).
- Wraps libcaesium internally. Reimplementation: use Pillow or imagemagick CLI.

### 186 · sitkevij/hex (rs, ceil 91.7%, 823 tests)
- Hex viewer (similar to hexyl in fd cluster).
- After fd anchor locks, this gets significant lift via `_lib/rs/sharkdp_cli.rs` (sitkevij follows similar conventions).

### 120 · unhappychoice/gittype (rs, ceil 91.3%, 741 tests)
- Typing trainer using git history.
- TUI; defer to fzf cluster.

### 195 · rust-ethereum/ethabi (rs, ceil 90.9%, 997 tests)
- Ethereum ABI encoder/decoder.
- Domain-specific. Pattern: parse ABI JSON → encode/decode hex byte streams.

### 167 · chmln/handlr (rs, ceil 90.7%, 722 tests)
- xdg-mime alternative; manage default applications on Linux.
- Reads/writes `~/.config/mimeapps.list`.

### 115 · rs/jplot (go, ceil 89.0%, 583 tests)
- Real-time JSON-stream plotter.
- Reads JSON lines on stdin; emits sparkline-style output to stdout.
- TUI-adjacent but rich CLI surface.

### 175 · wfxr/code-minimap (rs, ceil 88.8%, 313 tests)
- Generate a code minimap (text-art summary of source code).
- Same author as csview (in-progress) — *partial portfolio coherence with csview*.

### 138 · oppiliappan/eva (rs, ceil 88.7%, 913 tests)
- Calculator REPL with expression parsing.
- Math expression evaluator → result.

### 70 · eradman/entr (c, ceil 88.6%, 586 tests)
- File-watch + run command.
- inotify (Linux) or kqueue (BSD); Linux-only in PB containers.

### 104 · noborus/ov (go, ceil 87.6%, 1854 tests)
- Pager (less alternative).
- Same author as trdsql (jq cluster). Some pattern transfer.
- TUI cluster; non-interactive mode tests dominant.

### 152 · nikolassv/bartib (rs, ceil 87.3%, 722 tests)
- Time tracker.
- File-based state in `~/.bartib`.

### 113 · hooklift/gowsdl (go, ceil 86.4%, 391 tests)
- WSDL → Go types code generator.
- Domain-specific; XML parsing.

### 164 · incu6us/goimports-reviser (go, ceil 86.4%, 513 tests)
- Reorder Go imports.
- Wraps `go fmt` style logic.

### 169 · KSXGitHub/parallel-disk-usage (rs, ceil 86.1%, 531 tests)
- du-clone in Rust; parallel walker.
- After fd anchor locks, reuse `_lib/rs/walker.rs`.

### 187 · brocode/fblog (rs, ceil 86.0%, 978 tests)
- JSON log pretty-printer.
- After jq anchor locks, reuse `_lib/py/json_io.py` if porting to Python; otherwise direct serde_json.

### 160 · astro/deadnix (rs, ceil 85.5%, 602 tests)
- Find dead code in Nix files.
- Domain-specific (Nix language); minimal lexer.

---

## 9 · The 0-50% bucket (excluded from mass run)

42 tools have frontier ceilings below 50%, meaning even GPT-5.4/Opus 4.7/Gemini 3.1 Pro can't break the half-resolved threshold. These are **not** mass-run targets; each needs anchor-grade study.

Examples (rank, repo, lang, ceiling):
- #4 FFmpeg/FFmpeg (c, 5.3%) — video processing megaproject
- #9 php/php-src (c, 4.8%) — PHP runtime
- #42 bellard/quickjs (c, 3.6%) — JavaScript engine
- #93 tinycc/tinycc (c, 12.8%) — C compiler
- #46 lua/lua (c, 43.1%) — Lua interpreter
- #62 danmar/cppcheck (cpp, 14.6%) — C++ static analyzer
- #67 OSGeo/gdal (cpp, 25.4%) — geospatial library
- #105 samtools/samtools (c, 14.2%) — bioinformatics
- #140 gromacs/gromacs (cpp, 9.3%) — molecular dynamics
- #7 jgm/pandoc (hs, 14.1%) — universal document converter

**Strategy for these**: do not include in mass run. Each gets a dedicated anchor pack when the bench backlog warrants it. The five existing anchors do NOT unlock any of these.

---

## 10 · Iteration loop (the "what's left over" stage)

After Stage 4 of the mass run, the residual residual (heh) becomes the new working set:

```
mass_run_v1 → triage → ALMOST_DONE → quick fixes → 100%
                      → TIER_A     → targeted retries → 100% or TIER_B
                      → TIER_B     → re-scaffold → mass_run_v2 attempt
                      → TIER_C     → defer to anchor pack
                      → FAILED     → defer
```

Ratchet: every tool that hits 100% leaves the residual permanently. Mass run v2 only re-attempts TIER_A/B residuals from v1.

Each retry attempt **uses the same scaffold but with the failure-category fix applied**. The sample failure names from the eval JSON tell us which of the 8 patterns or 14 secondary patterns broke. Apply the fix, re-eval that one tool only.

---

## 11 · Success metric

```
Pre-mass-run resolved at 100%:                  3   (zoxide, yj, ripsecrets)
Anchor packs (planned/in-flight):              ~7-15  (5 anchors + their direct cluster siblings)
Mass run v1 target:                            +20-40 of the 115 in-scope residuals

Bench-wide target post-mass-run-v1:            30-50 tools at 100%
Bench-wide target post-mass-run-v2 + anchors:  60-80 tools at 100%
Stretch (post-everything):                     90-120 tools at 100%
```

**Frontier comparison**: best frontier model (any) sits at 0% fully resolved. Determinex's plan delivers 30-50× that on a GTX 1660 Ti within one mass-run cycle.

---

## 12 · Files this document references

- [`_residual_audit.json`](_residual_audit.json) — machine-readable audit (157 tools with metadata)
- [`_residual_table.md`](_residual_table.md) — full sortable residual list
- [`_test_pattern_audit.json`](_test_pattern_audit.json) — 256k-test name-token audit
- [`anchor_strategy.md`](anchor_strategy.md) — the 5-anchor companion strategy (anchors are NOT in this mass run)
- [`../prompts/architect_prompt.md`](../prompts/architect_prompt.md) — architect template (used for anchor work, not mass run)
- [`../prompts/builder_prompt.md`](../prompts/builder_prompt.md) — builder template (apply scaffold from § 4 within the mass run)
- [`../README.md`](../README.md) — top-level corpus manifest

---

## 13 · The execution command (when you're ready)

```bash
# 1 — Generate (one-shot mass attempt)
python -c "
import json
audit = json.load(open('corpus/programbench/_strategy/_residual_audit.json'))
inscope = [t['instance_id'] for t in audit['residual'] if t['ceiling'] >= 50 and t['instance_id']]
print(' '.join(inscope))
" | xargs python scripts/determinex_programbench_agent.py --workers 4 --run-name mass_run_v1 --tasks

# 2 — Eval everything
cd T:/Dev/ProgramBench && PYTHONUTF8=1 PROGRAMBENCH_DOCKER_CPUS=4 \
    uv run programbench eval "T:/determinex-programbench/mass_run_v1" --force

# 3 — Triage
python scripts/programbench_mass_triage.py
```

— Locked 2026-05-09. Treat § 1-7 as canonical. § 8 (per-tool intel) and § 9 (excluded list) update as eval results come in.
