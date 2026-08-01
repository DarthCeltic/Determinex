---
name: pb-per-language-scaffolds
description: Concrete, copy-pasteable compile.sh + main.{py,go,rs,c} scaffolds for ProgramBench mass run. Each scaffold bakes in the 8 universal patterns from universal_cli_patterns.md.
type: scaffold-templates
---

# Per-Language Scaffolds

Drop-in scaffolds for the four languages covered by the 115 in-scope residual tools. Every scaffold passes the 8-pattern check-list out of the box; tool-specific work is grafted on top.

For the broader 25-family sprint runway, see [`language_family_sprint_matrix.md`](language_family_sprint_matrix.md). This file remains the concrete copy-paste source for the highest-yield executable families; the matrix tells agents which family to choose and when.

## Executable contract

Keep `compile.sh` tiny and language-specific. Its job is only to create a real `./executable` file in the current directory.

- Python: copy `main.py` to `executable`; never symlink it. ProgramBench moves `./executable` into `/opt` before hashing, and symlinks can break after the move.
- Go/Rust/C/C++: compile directly to `executable`, or copy the built binary from `target/release/<tool>` after the build.
- Do not make a giant universal `compile.sh`. Put language behavior in source files or a small language-specific launcher, then keep the compile step boring.
- First official eval for each tool must verify `./executable` is a real file (`test -f ./executable && test ! -L ./executable`) before trusting score output.

## Python — best for: anything with simple CLI + algorithmic body

`compile.sh`:
```bash
#!/bin/bash
set -e
chmod +x main.py
cp main.py executable
chmod +x executable
```

`main.py`:
```python
#!/usr/bin/env python3
"""<TOOL> reimplementation — Determinex mass run scaffold."""
import sys
import os
from pathlib import Path

TOOL_NAME = "<tool>"
TOOL_VERSION = "0.1.0"

USAGE = f"""\
usage: {TOOL_NAME} [OPTIONS] [INPUT...]

Options:
  -h, --help     show this help and exit
  -V, --version  show version and exit
"""

# Authoritative flag list — used for unknown-flag detection.
KNOWN_FLAGS = {
    "-h", "--help", "-V", "--version",
    # Tool-specific flags — fill in.
}
KNOWN_FLAGS_WITH_ARG = {
    # Flags that consume the next argv slot.
    # e.g. "-o", "--output", "-c", "--config"
}


def parse_args(argv):
    """Strict parse: fail fast on unknown flags."""
    flags = {}
    positionals = []
    i = 1
    while i < len(argv):
        a = argv[i]
        if a == "--":
            positionals.extend(argv[i + 1 :])
            break
        if a.startswith("-") and a != "-":
            # known with arg?
            if a in KNOWN_FLAGS_WITH_ARG:
                if i + 1 >= len(argv):
                    print(f"{TOOL_NAME}: missing argument for {a}", file=sys.stderr)
                    sys.exit(2)
                flags[a] = argv[i + 1]
                i += 2
                continue
            # boolean
            if a in KNOWN_FLAGS:
                flags[a] = True
                i += 1
                continue
            # support --flag=value
            if "=" in a and a.split("=", 1)[0] in KNOWN_FLAGS_WITH_ARG:
                k, v = a.split("=", 1)
                flags[k] = v
                i += 1
                continue
            print(f"{TOOL_NAME}: unknown option: {a}", file=sys.stderr)
            sys.exit(2)
        positionals.append(a)
        i += 1
    return flags, positionals


def main():
    flags, positionals = parse_args(sys.argv)

    if "-h" in flags or "--help" in flags:
        sys.stdout.write(USAGE)
        sys.exit(0)
    if "-V" in flags or "--version" in flags:
        print(f"{TOOL_NAME} {TOOL_VERSION}")
        sys.exit(0)

    # Resolve inputs: positional list, or stdin if none and stdin is piped.
    if not positionals and not sys.stdin.isatty():
        process_stdin()
    elif not positionals:
        print(f"{TOOL_NAME}: missing argument: <input>", file=sys.stderr)
        sys.exit(2)
    else:
        for p in positionals:
            if p == "-":
                process_stdin()
                continue
            path = Path(p)
            if not path.exists():
                print(f"{TOOL_NAME}: cannot access '{p}': No such file or directory", file=sys.stderr)
                sys.exit(2)
            process_file(path)

    sys.exit(0)


def process_stdin():
    """Tool-specific: handle stdin input. Override per tool."""
    data = sys.stdin.read()
    if not data:
        return  # empty-input default: no-op
    # tool-specific work on `data`


def process_file(path):
    """Tool-specific: handle one file. Override per tool."""
    data = path.read_text(encoding="utf-8", errors="replace")
    if not data:
        return
    # tool-specific work on `data`


if __name__ == "__main__":
    main()
```

Cost: ~110 LOC. Compiles in 0s. Iterates fast. **Default to Python unless the tool's reference is in Go/Rust AND the test surface is performance-sensitive.**

---

## Go — best for: CLI tools, network tools, concurrency, when reference is Go

`compile.sh`:
```bash
#!/bin/bash
set -e
go mod init tool >/dev/null 2>&1 || true
go mod tidy >/dev/null 2>&1 || true
go build -o executable .
```

`go.mod`:
```
module tool

go 1.21
```

`main.go`:
```go
package main

import (
	"fmt"
	"io"
	"os"
)

const (
	toolName    = "<tool>"
	toolVersion = "0.1.0"
)

const usageText = `usage: <tool> [OPTIONS] [INPUT...]

Options:
  -h, --help     show this help and exit
  -V, --version  show version and exit
`

// Tool-specific known flags. Add as needed.
var knownBool = map[string]bool{
	"-h": true, "--help": true, "-V": true, "--version": true,
}
var knownArg = map[string]bool{
	// e.g. "-o": true, "--output": true,
}

type parsed struct {
	flags       map[string]string
	positionals []string
}

func parseArgs(argv []string) (parsed, error) {
	out := parsed{flags: map[string]string{}}
	for i := 1; i < len(argv); i++ {
		a := argv[i]
		if a == "--" {
			out.positionals = append(out.positionals, argv[i+1:]...)
			return out, nil
		}
		if len(a) > 1 && a[0] == '-' && a != "-" {
			if knownArg[a] {
				if i+1 >= len(argv) {
					return out, fmt.Errorf("missing argument for %s", a)
				}
				out.flags[a] = argv[i+1]
				i++
				continue
			}
			if knownBool[a] {
				out.flags[a] = "true"
				continue
			}
			return out, fmt.Errorf("unknown option: %s", a)
		}
		out.positionals = append(out.positionals, a)
	}
	return out, nil
}

func main() {
	p, err := parseArgs(os.Args)
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s: %s\n", toolName, err)
		os.Exit(2)
	}
	if _, ok := p.flags["-h"]; ok {
		os.Exit(printHelp())
	}
	if _, ok := p.flags["--help"]; ok {
		os.Exit(printHelp())
	}
	if _, ok := p.flags["-V"]; ok {
		os.Exit(printVersion())
	}
	if _, ok := p.flags["--version"]; ok {
		os.Exit(printVersion())
	}

	// Resolve inputs.
	if len(p.positionals) == 0 {
		stat, _ := os.Stdin.Stat()
		if (stat.Mode() & os.ModeCharDevice) == 0 {
			processStdin()
		} else {
			fmt.Fprintf(os.Stderr, "%s: missing argument: <input>\n", toolName)
			os.Exit(2)
		}
	} else {
		for _, name := range p.positionals {
			if name == "-" {
				processStdin()
				continue
			}
			f, err := os.Open(name)
			if err != nil {
				fmt.Fprintf(os.Stderr, "%s: cannot access '%s': %s\n", toolName, name, err)
				os.Exit(2)
			}
			processReader(f)
			_ = f.Close()
		}
	}
	os.Exit(0)
}

func printHelp() int    { fmt.Print(usageText); return 0 }
func printVersion() int { fmt.Printf("%s %s\n", toolName, toolVersion); return 0 }

func processStdin() { processReader(os.Stdin) }

func processReader(r io.Reader) {
	data, err := io.ReadAll(r)
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s: read error: %s\n", toolName, err)
		os.Exit(2)
	}
	if len(data) == 0 {
		return
	}
	// Tool-specific: act on `data`.
	_ = data
}
```

Cost: ~120 LOC. Compiles in 1-3s. Use when a Go tool's surface needs concurrency or stdlib-only network primitives.

---

## Rust — best for: when reference is Rust AND clap/serde are needed

`compile.sh`:
```bash
#!/bin/bash
set -e
export CARGO_HOME=/tmp/cargo
export CARGO_TARGET_DIR=/tmp/target
cargo build --release 2>&1 | tail -10
cp target/release/tool ./executable
```

`Cargo.toml`:
```toml
[package]
name = "tool"
version = "0.1.0"
edition = "2021"

[[bin]]
name = "tool"
path = "src/main.rs"

[profile.release]
strip = true
lto = false
codegen-units = 16

[dependencies]
clap = { version = "4", features = ["derive"] }
```

`src/main.rs`:
```rust
use std::io::{self, Read};
use std::path::PathBuf;
use std::process::ExitCode;

use clap::Parser;

const TOOL_NAME: &str = "<tool>";

#[derive(Parser)]
#[command(name = TOOL_NAME, version, disable_help_flag = false)]
struct Cli {
    /// Inputs (use "-" for stdin)
    inputs: Vec<PathBuf>,

    /// Tool-specific flags go here (with #[arg(...)] decorators)
}

fn main() -> ExitCode {
    let cli = match Cli::try_parse() {
        Ok(c) => c,
        Err(e) => {
            // clap's exit code is 2 for usage errors and 0 for --help/--version
            e.exit();
        }
    };

    if cli.inputs.is_empty() {
        if !atty::is(atty::Stream::Stdin) {
            return process_stdin();
        }
        eprintln!("{}: missing argument: <input>", TOOL_NAME);
        return ExitCode::from(2);
    }

    for p in &cli.inputs {
        if p.to_string_lossy() == "-" {
            if let ExitCode::SUCCESS = process_stdin() { } else { return ExitCode::from(2); }
            continue;
        }
        if !p.exists() {
            eprintln!("{}: cannot access '{}': No such file or directory", TOOL_NAME, p.display());
            return ExitCode::from(2);
        }
        if let Err(e) = process_path(p) {
            eprintln!("{}: {}", TOOL_NAME, e);
            return ExitCode::from(2);
        }
    }
    ExitCode::SUCCESS
}

fn process_stdin() -> ExitCode {
    let mut buf = String::new();
    if io::stdin().read_to_string(&mut buf).is_err() {
        return ExitCode::from(2);
    }
    if buf.is_empty() {
        return ExitCode::SUCCESS;
    }
    // tool-specific
    ExitCode::SUCCESS
}

fn process_path(p: &PathBuf) -> io::Result<()> {
    let data = std::fs::read_to_string(p)?;
    if data.is_empty() { return Ok(()) }
    // tool-specific
    Ok(())
}
```

**Note**: Rust adds `atty` as an indirect dep (`clap` pulls it through default features). If avoiding deps, replace with `std::io::IsTerminal` (Rust 1.70+).

Cost: cold compile 90-180s; warm 8-20s. **Use only when Python/Go are insufficient.**

---

## C — best for: tools where reference is C AND minimal flag surface

`compile.sh`:
```bash
#!/bin/bash
set -e
gcc -O2 -Wall -o executable main.c
```

`main.c`:
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

static const char *TOOL = "<tool>";
static const char *VER  = "0.1.0";

static const char *USAGE =
    "usage: <tool> [OPTIONS] [INPUT...]\n"
    "\n"
    "Options:\n"
    "  -h, --help     show this help and exit\n"
    "  -V, --version  show version and exit\n";

static int process_file(const char *path) {
    FILE *f = fopen(path, "r");
    if (!f) {
        fprintf(stderr, "%s: cannot access '%s': %s\n", TOOL, path, strerror(errno));
        return 2;
    }
    /* tool-specific */
    fclose(f);
    return 0;
}

static int process_stdin(void) {
    /* tool-specific */
    return 0;
}

int main(int argc, char **argv) {
    int positional_start = -1;
    for (int i = 1; i < argc; i++) {
        const char *a = argv[i];
        if (!strcmp(a, "--")) { positional_start = i + 1; break; }
        if (!strcmp(a, "-h") || !strcmp(a, "--help"))    { fputs(USAGE, stdout); return 0; }
        if (!strcmp(a, "-V") || !strcmp(a, "--version")) { printf("%s %s\n", TOOL, VER); return 0; }
        if (a[0] == '-' && strcmp(a, "-") != 0) {
            fprintf(stderr, "%s: unknown option: %s\n", TOOL, a);
            return 2;
        }
        positional_start = i; break;
    }

    if (positional_start < 0 || positional_start >= argc) {
        if (!isatty(STDIN_FILENO)) return process_stdin();
        fprintf(stderr, "%s: missing argument: <input>\n", TOOL);
        return 2;
    }

    int rc = 0;
    for (int i = positional_start; i < argc; i++) {
        if (!strcmp(argv[i], "-")) { rc |= process_stdin(); continue; }
        rc |= process_file(argv[i]);
    }
    return rc;
}
```

Cost: ~80 LOC. Compiles in <1s. Use only for genuinely C-domain tools (system utilities, hash functions, embedded-style work). Most C residuals would be better as Python.

---

## Choosing a language for a residual tool

```
1. Is the reference language listed on programbench.com?         → start there
2. Does the test surface require performance?                    → reference language
3. Otherwise:                                                    → Python (fastest iteration)

Reasons to deviate:
- Tool has a Python pip module (lz4, brotli, blake3, etc.)       → Python
- Tool requires concurrency (oha, gping, miniserve)              → Go or Rust
- Tool needs system calls (entr, dropbear, htop, dust)           → C or Rust
- Tool needs a parser (ast-grep, deadnix, statix)                → Rust
- Tool needs a TUI (kiro-editor, gittype, ov)                    → Go (after fzf locks) or Rust
```

When uncertain, **prototype in Python first**. Cost is lowest; switch language only if the test eval shows perf-bound failures (timeouts).
