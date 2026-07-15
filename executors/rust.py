"""executors/rust.py — concrete Rust language executor.

Second concrete executor after PythonExecutor; highest-leverage language profile
since 68 of 115 in-scope residual ProgramBench tools are Rust. Inherits the
shared 7-phase contract from base.Executor and overrides probe / scaffold /
build / eval with Rust-specific behavior.

What this owns:
  probe       same task.yaml + tests.json read as PythonExecutor, but flags
              upstream language="rust" if task.yaml says so (informational)
  scaffold    Cargo.toml + src/main.rs + compile.sh
              src/main.rs ships the 8 universal CLI patterns implemented in
              clap-4 with rc=1 on unknown args (matches the iter-1 wording
              the Python scaffold already converged on, so test goldens stay
              consistent across language executors)
  build       cargo build --release -> cp target/release/<bin> ./executable
              with a stripped-down CARGO_HOME so multiple parallel tools
              don't clobber each other's lock dirs
  pack        inherited from base.Executor (deterministic tar via mass_run_v2_pack)
  eval        inherited path (same programbench harness invocation as Python)
  classify    inherited (central taxonomy)
  report      inherited

Build cost on Tier-0 hardware:
  cold:  90-180s first cargo build (deps fetch + compile)
  warm:  8-20s incremental (CARGO_TARGET_DIR cached)
  the per-instance CARGO_HOME isolation prevents N×N lock contention when
  evaluating multiple tools in parallel.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

from .base import (
    Executor, ExecutorError,
    ProbeResult, ScaffoldResult, BuildResult, EvalResult,
)
from .python import PythonExecutor, _derive_tool_name  # reuse probe + helpers


# ---------------------------------------------------------------------------
# Cargo.toml template
# ---------------------------------------------------------------------------

_CARGO_TOML = """[package]
name = "{crate_name}"
version = "0.1.0"
edition = "2021"

[[bin]]
name = "{crate_name}"
path = "src/main.rs"

[profile.release]
strip = true
lto = false
codegen-units = 16

[dependencies]
clap = {{ version = "4", features = ["derive"] }}
"""


# ---------------------------------------------------------------------------
# main.rs — bakes in the 8 universal CLI patterns with iter-1's wording.
#
# clap-4 already produces the clap-style "error: unexpected argument '<x>'
# found" wording our Python scaffold has to emit manually, so this is
# mostly idiomatic clap + a default handler that mirrors the Python scaffold's
# stdin / file behavior.
# ---------------------------------------------------------------------------

_MAIN_RS = '''//! {tool_name} — Determinex mass-run Rust scaffold.
//!
//! Bakes in the 8 universal CLI patterns: invalid, multiple, help, empty,
//! no-*, unknown, version, missing. Tool-specific behavior is the iteration
//! target.

use std::fs;
use std::io::{{self, Read, Write}};
use std::path::PathBuf;
use std::process::ExitCode;

use clap::Parser;

const TOOL_NAME: &str = "{tool_name}";

#[derive(Parser, Debug)]
#[command(name = TOOL_NAME, version, about = "Determinex Rust scaffold")]
struct Cli {{
    /// Input file paths (use "-" for stdin)
    inputs: Vec<String>,

    /// Write output to FILE
    #[arg(short = 'o', long = "output")]
    output: Option<PathBuf>,

    /// Disable color output
    #[arg(long = "no-color")]
    no_color: bool,

    /// Enable color output (default depends on terminal)
    #[arg(long = "color")]
    color: bool,
}}

fn main() -> ExitCode {{
    // clap-4 already emits "error: unexpected argument '<x>' found" with rc=2
    // for unknown flags. We override exit code to match the rc=1 convention
    // most residual Rust tool tests expect.
    let cli = match Cli::try_parse() {{
        Ok(c) => c,
        Err(e) => {{
            // Help (--help / -h) and Version (--version / -V) print to stdout
            // with exit 0; everything else is a usage error.
            use clap::error::ErrorKind;
            match e.kind() {{
                ErrorKind::DisplayHelp | ErrorKind::DisplayVersion => {{
                    e.print().ok();
                    return ExitCode::SUCCESS;
                }}
                _ => {{
                    e.print().ok();
                    return ExitCode::from(1);
                }}
            }}
        }}
    }};

    // Resolve inputs: positional list, or stdin if none
    if cli.inputs.is_empty() {{
        if !atty_stdin() {{
            return run_stdin(&cli);
        }}
        // bare invocation, no stdin: exit 0 (pattern 4 — empty input)
        return ExitCode::SUCCESS;
    }}

    for inp in &cli.inputs {{
        if inp == "-" {{
            let rc = run_stdin(&cli);
            if rc != ExitCode::SUCCESS {{
                return rc;
            }}
            continue;
        }}
        let path = PathBuf::from(inp);
        if !path.exists() {{
            eprintln!("{{}}: cannot access '{{}}': No such file or directory",
                      TOOL_NAME, inp);
            return ExitCode::from(2);
        }}
        if path.is_dir() {{
            eprintln!("{{}}: '{{}}' is a directory", TOOL_NAME, inp);
            return ExitCode::from(2);
        }}
        match fs::read_to_string(&path) {{
            Ok(data) => {{
                if let Err(e) = write_out(&cli, &data) {{
                    eprintln!("{{}}: write error: {{}}", TOOL_NAME, e);
                    return ExitCode::from(2);
                }}
            }}
            Err(e) => {{
                eprintln!("{{}}: '{{}}': {{}}", TOOL_NAME, inp, e);
                return ExitCode::from(2);
            }}
        }}
    }}
    ExitCode::SUCCESS
}}

fn run_stdin(cli: &Cli) -> ExitCode {{
    let mut buf = String::new();
    if io::stdin().read_to_string(&mut buf).is_err() {{
        return ExitCode::from(2);
    }}
    if buf.is_empty() {{
        return ExitCode::SUCCESS;
    }}
    if let Err(e) = write_out(cli, &buf) {{
        eprintln!("{{}}: write error: {{}}", TOOL_NAME, e);
        return ExitCode::from(2);
    }}
    ExitCode::SUCCESS
}}

fn write_out(cli: &Cli, data: &str) -> io::Result<()> {{
    if let Some(out_path) = &cli.output {{
        fs::write(out_path, data.as_bytes())
    }} else {{
        io::stdout().write_all(data.as_bytes())
    }}
}}

/// std::io::IsTerminal exists in 1.70+; fall back to false if unavailable.
fn atty_stdin() -> bool {{
    use std::io::IsTerminal;
    io::stdin().is_terminal()
}}
'''


# ---------------------------------------------------------------------------
# compile.sh — Cargo build → cp the binary
# ---------------------------------------------------------------------------

_COMPILE_SH = """#!/bin/bash
set -e
# Per-instance CARGO_HOME / CARGO_TARGET_DIR isolation so parallel workers
# don't fight over the lock file. The /tmp path is deliberate: it stays inside
# the cleanroom image and gets thrown away after eval.
export CARGO_HOME="${CARGO_HOME:-/tmp/cargo_home}"
export CARGO_TARGET_DIR="${CARGO_TARGET_DIR:-/tmp/cargo_target}"
mkdir -p "$CARGO_HOME" "$CARGO_TARGET_DIR"

cargo build --release 2>&1 | tail -20

# Copy the binary to ./executable. We don't use a symlink — programbench moves
# the file to /opt before hashing, and symlinks break after the move.
BIN="$(ls "$CARGO_TARGET_DIR/release/"*.exe 2>/dev/null | head -n 1)"
if [ -z "$BIN" ]; then
    BIN="$(find "$CARGO_TARGET_DIR/release/" -maxdepth 1 -type f -perm /111 ! -name '*.d' ! -name '*.rlib' | head -n 1)"
fi
if [ -z "$BIN" ]; then
    echo "compile.sh: no release binary produced under $CARGO_TARGET_DIR/release/" >&2
    exit 1
fi
cp "$BIN" ./executable
chmod +x ./executable
"""


# ---------------------------------------------------------------------------
# Executor
# ---------------------------------------------------------------------------

class RustExecutor(Executor):
    """Concrete Rust language executor."""
    family: str = "rust"
    file_ext: str = ".rs"
    executable_name: str = "executable"

    def __init__(
        self,
        *,
        tasks_dir: Path | None = None,
        programbench_dir: Path | None = None,
    ):
        # Delegate the same defaults PythonExecutor uses
        py = PythonExecutor(
            tasks_dir=tasks_dir or PythonExecutor().tasks_dir,
            programbench_dir=programbench_dir or PythonExecutor().programbench_dir,
        )
        self.tasks_dir = py.tasks_dir
        self.programbench_dir = py.programbench_dir
        self._py = py  # delegate probe + eval since both are language-neutral

    # ── probe ─────────────────────────────────────────────────────────────
    def probe(self, instance_id: str) -> ProbeResult:
        """Reuse PythonExecutor.probe; the task.yaml read is language-neutral."""
        return self._py.probe(instance_id)

    # ── scaffold ──────────────────────────────────────────────────────────
    def scaffold(self, probe: ProbeResult, work_dir: Path) -> ScaffoldResult:
        """Write source/{Cargo.toml, src/main.rs, compile.sh, README_DETERMINEX.md}."""
        source = work_dir / "source"
        src_dir = source / "src"
        src_dir.mkdir(parents=True, exist_ok=True)

        tool_name, author = _derive_tool_name(probe.instance_id)
        # Cargo package names must be lowercase + ascii. Most tool names already
        # comply; normalize the rest.
        crate_name = "".join(c if (c.isalnum() or c in "_-") else "_" for c in tool_name.lower())

        cargo_toml = _CARGO_TOML.format(crate_name=crate_name)
        (source / "Cargo.toml").write_text(cargo_toml, encoding="utf-8", newline="\n")

        main_rs = _MAIN_RS.format(tool_name=tool_name)
        (src_dir / "main.rs").write_text(main_rs, encoding="utf-8", newline="\n")

        (source / "compile.sh").write_text(_COMPILE_SH, encoding="utf-8", newline="\n")
        try:
            os.chmod(source / "compile.sh", 0o755)
        except OSError:
            pass

        readme = (
            f"# {tool_name} — Rust executor scaffold\n\n"
            f"- **instance_id**: {probe.instance_id}\n"
            f"- **author**: {author}\n"
            f"- **executor**: rust (clap-4)\n"
            f"- **crate name**: {crate_name}\n"
            f"- **declared flags**: {probe.declared_flags or '(none from task.yaml)'}\n"
            f"- **test count**: {probe.test_count or 'unknown'}\n\n"
            f"## Build cost\n"
            f"- cold: 90-180s (cargo fetch + compile)\n"
            f"- warm: 8-20s (incremental, CARGO_TARGET_DIR cached)\n\n"
            f"## Eval command\n"
            f"```\n"
            f"cd {self.programbench_dir} && PYTHONUTF8=1 uv run programbench eval "
            f"{work_dir.parent} --filter '{author}' --force\n"
            f"```\n"
        )
        (source / "README_DETERMINEX.md").write_text(readme, encoding="utf-8", newline="\n")

        return ScaffoldResult(
            work_dir=work_dir,
            files_written=[
                source / "Cargo.toml",
                src_dir / "main.rs",
                source / "compile.sh",
                source / "README_DETERMINEX.md",
            ],
        )

    # ── build ─────────────────────────────────────────────────────────────
    def build(self, work_dir: Path) -> BuildResult:
        """Run compile.sh (cargo build --release + cp). Verify ./executable
        is a real file, not a symlink — programbench moves it to /opt and
        symlinks break after the move."""
        source = work_dir / "source"
        compile_sh = source / "compile.sh"
        if not compile_sh.is_file():
            raise ExecutorError(f"build: no compile.sh at {compile_sh}")

        # Verify cargo is on PATH up front for a better error than a bash NPE
        if not shutil.which("cargo"):
            raise ExecutorError(
                "build: cargo not on PATH — install Rust via https://rustup.rs/ "
                "or run scripts/determinex_doctor.py for a full toolchain report"
            )

        t0 = time.time()
        proc = subprocess.run(
            ["bash", "./compile.sh"],
            cwd=str(source),
            capture_output=True, text=True,
            timeout=600,    # 10 min for cold cargo compile
        )
        elapsed = time.time() - t0
        executable = source / self.executable_name
        ok = (
            proc.returncode == 0
            and executable.is_file()
            and not executable.is_symlink()
        )
        if not ok and executable.is_symlink():
            raise ExecutorError(
                f"build: {executable} is a symlink — programbench moves it to /opt "
                "before hashing and the link will break. compile.sh must `cp` the "
                "release binary, not symlink it."
            )
        return BuildResult(
            work_dir=work_dir,
            executable_path=executable if executable.is_file() else None,
            elapsed_seconds=round(elapsed, 2),
            stdout=proc.stdout[-2000:],
            stderr=proc.stderr[-2000:],
            ok=ok,
        )

    # ── eval ──────────────────────────────────────────────────────────────
    def eval(self, work_dir: Path, instance_id: str) -> EvalResult:
        """Reuse PythonExecutor.eval — the programbench harness invocation is
        language-neutral; it just runs ./executable inside the cleanroom image."""
        return self._py.eval(work_dir, instance_id)


# ---------------------------------------------------------------------------
# CLI — one-shot end-to-end run for a single tool (mirrors python.py)
# ---------------------------------------------------------------------------

def _cli() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Rust executor — run one tool through all 7 phases")
    ap.add_argument("instance_id", help="e.g. burntsushi__ripgrep.3b7fd44")
    ap.add_argument("--work-dir", type=Path, default=None)
    ap.add_argument("--skip-eval", action="store_true",
                    help="skip the official eval (useful for scaffold+build smoke)")
    ap.add_argument("--skip-build", action="store_true",
                    help="skip the cargo build (scaffold-only smoke)")
    args = ap.parse_args()

    work_dir = args.work_dir or Path(
        f"T:/determinex-programbench/_executor_rust_test/{args.instance_id}"
    )
    work_dir.mkdir(parents=True, exist_ok=True)

    ex = RustExecutor()
    print(f"=== probe {args.instance_id} ===")
    probe = ex.probe(args.instance_id)
    print(f"  flags: {probe.declared_flags}")
    print(f"  tests: {probe.test_count}")
    print(f"  notes: {probe.notes}")

    print(f"=== scaffold {work_dir} ===")
    sc = ex.scaffold(probe, work_dir)
    print(f"  wrote {len(sc.files_written)} files")

    if args.skip_build:
        print("=== skipping build (--skip-build) ===")
        return 0

    print(f"=== build (this may take 90-180s cold) ===")
    b = ex.build(work_dir)
    print(f"  ok={b.ok}  elapsed={b.elapsed_seconds}s  exec={b.executable_path}")
    if not b.ok:
        print(f"  stderr: {b.stderr[:400]}")
        return 1

    print(f"=== pack ===")
    p = ex.pack(work_dir)
    print(f"  submission: {p.submission_path}  ({p.n_files} files)")

    if args.skip_eval:
        print("=== skipping eval (--skip-eval) ===")
        return 0

    print(f"=== eval ===")
    e = ex.eval(work_dir, args.instance_id)
    if e.error:
        print(f"  ERROR: {e.error}")
        return 1
    print(f"  score: {e.score}/100  ({e.passed}/{e.total})")
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
