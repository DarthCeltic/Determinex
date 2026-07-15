"""executors/go.py — concrete Go language executor.

Third concrete executor. 28 of 115 in-scope residual ProgramBench tools have
a Go upstream — second-biggest after Rust. Build cost is dramatically lower
than Rust (1-3s vs 90-180s cold) since the standard library covers most CLI
needs without external deps.

Scaffolds a single-file Go program using stdlib `flag` parsing. The 8 universal
CLI patterns are baked in with iter-1's clap-style wording and rc=1 on unknown
arguments so cross-language test goldens stay aligned with the Python + Rust
scaffolds.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import time
from pathlib import Path

from .base import (
    Executor, ExecutorError,
    ProbeResult, ScaffoldResult, BuildResult, EvalResult,
)
from .python import PythonExecutor, _derive_tool_name


# ---------------------------------------------------------------------------
# go.mod template
# ---------------------------------------------------------------------------

_GO_MOD = """module {module_name}

go 1.21
"""


# ---------------------------------------------------------------------------
# main.go — bakes in the 8 universal CLI patterns with iter-1 conventions.
#
# stdlib `flag` package only — no external deps means no `go mod download`
# step, which keeps the cold build under ~3 seconds.
# ---------------------------------------------------------------------------

_MAIN_GO = '''// {tool_name} — Determinex mass-run Go scaffold.
//
// Bakes in the 8 universal CLI patterns: invalid, multiple, help, empty,
// no-*, unknown, version, missing. Tool-specific behavior is the iteration
// target.

package main

import (
\t"flag"
\t"fmt"
\t"io"
\t"os"
\t"strings"
)

const (
\ttoolName    = "{tool_name}"
\ttoolVersion = "0.1.0"
)

func usage() {{
\tfmt.Fprintf(os.Stdout,
\t\t"Usage: %s [OPTIONS] [INPUT...]\\n\\n"+
\t\t\t"Options:\\n"+
\t\t\t"  -h, --help     show this help and exit\\n"+
\t\t\t"  -V, --version  show version and exit\\n"+
\t\t\t"  -o, --output FILE  write output to FILE\\n"+
\t\t\t"      --no-color disable color output\\n"+
\t\t\t"      --color    enable color output\\n",
\t\ttoolName)
}}

func main() {{
\t// Manual arg parsing — stdlib `flag` package mangles the help/version
\t// output and doesn't support --long-equals-value cleanly. We need full
\t// control to match iter-1 wording and exit codes.
\targs := os.Args[1:]

\tvar (
\t\toutputFile string
\t\tnoColor    bool
\t\tcolor      bool
\t\tpositionals []string
\t)

\ti := 0
\tfor i < len(args) {{
\t\ta := args[i]
\t\tswitch {{
\t\tcase a == "--":
\t\t\tpositionals = append(positionals, args[i+1:]...)
\t\t\ti = len(args)
\t\tcase a == "-":
\t\t\tpositionals = append(positionals, "-")
\t\t\ti++
\t\tcase a == "-h" || a == "--help":
\t\t\tusage()
\t\t\tos.Exit(0)
\t\tcase a == "-V" || a == "--version":
\t\t\tfmt.Printf("%s %s\\n", toolName, toolVersion)
\t\t\tos.Exit(0)
\t\tcase a == "--no-color":
\t\t\tnoColor = true
\t\t\ti++
\t\tcase a == "--color":
\t\t\tcolor = true
\t\t\ti++
\t\tcase a == "-o" || a == "--output":
\t\t\tif i+1 >= len(args) {{
\t\t\t\tfmt.Fprintf(os.Stderr, "error: missing argument for %s\\n", a)
\t\t\t\tos.Exit(1)
\t\t\t}}
\t\t\toutputFile = args[i+1]
\t\t\ti += 2
\t\tcase strings.HasPrefix(a, "--output="):
\t\t\toutputFile = strings.TrimPrefix(a, "--output=")
\t\t\ti++
\t\tcase strings.HasPrefix(a, "-") && len(a) > 1:
\t\t\t// Unknown flag — clap-style wording + rc=1 (iter-1 convention)
\t\t\tfmt.Fprintf(os.Stderr, "error: unexpected argument '%s' found\\n\\n", a)
\t\t\tfmt.Fprintf(os.Stderr, "Usage: %s [OPTIONS] [INPUT...]\\n\\n", toolName)
\t\t\tfmt.Fprintf(os.Stderr, "For more information, try '--help'.\\n")
\t\t\tos.Exit(1)
\t\tdefault:
\t\t\tpositionals = append(positionals, a)
\t\t\ti++
\t\t}}
\t}}

\t_ = noColor
\t_ = color
\t_ = flag.NewFlagSet // keep `flag` import meaningful for future use

\t// Resolve inputs: positional list, or stdin if none
\tif len(positionals) == 0 {{
\t\tstat, _ := os.Stdin.Stat()
\t\tif (stat.Mode() & os.ModeCharDevice) == 0 {{
\t\t\tos.Exit(processStdin(outputFile))
\t\t}}
\t\tos.Exit(0)
\t}}

\trc := 0
\tfor _, p := range positionals {{
\t\tif p == "-" {{
\t\t\trc |= processStdin(outputFile)
\t\t\tcontinue
\t\t}}
\t\tinfo, err := os.Stat(p)
\t\tif os.IsNotExist(err) {{
\t\t\tfmt.Fprintf(os.Stderr, "%s: cannot access '%s': No such file or directory\\n",
\t\t\t\ttoolName, p)
\t\t\tos.Exit(2)
\t\t}}
\t\tif info != nil && info.IsDir() {{
\t\t\tfmt.Fprintf(os.Stderr, "%s: '%s' is a directory\\n", toolName, p)
\t\t\tos.Exit(2)
\t\t}}
\t\tdata, err := os.ReadFile(p)
\t\tif err != nil {{
\t\t\tfmt.Fprintf(os.Stderr, "%s: '%s': %s\\n", toolName, p, err)
\t\t\tos.Exit(2)
\t\t}}
\t\trc |= writeOut(outputFile, data)
\t}}
\tos.Exit(rc)
}}

func processStdin(outputFile string) int {{
\tdata, err := io.ReadAll(os.Stdin)
\tif err != nil {{
\t\treturn 2
\t}}
\tif len(data) == 0 {{
\t\treturn 0
\t}}
\treturn writeOut(outputFile, data)
}}

func writeOut(outputFile string, data []byte) int {{
\tif outputFile != "" {{
\t\tif err := os.WriteFile(outputFile, data, 0o644); err != nil {{
\t\t\tfmt.Fprintf(os.Stderr, "%s: write error: %s\\n", toolName, err)
\t\t\treturn 2
\t\t}}
\t\treturn 0
\t}}
\tos.Stdout.Write(data)
\treturn 0
}}
'''


# ---------------------------------------------------------------------------
# compile.sh — Go build (stdlib only → fast cold build)
# ---------------------------------------------------------------------------

_COMPILE_SH = """#!/bin/bash
set -e
# Per-instance GOPATH / GOCACHE isolation so parallel workers don't fight
# over the module download cache.
export GOPATH="${GOPATH:-/tmp/go_path}"
export GOCACHE="${GOCACHE:-/tmp/go_cache}"
mkdir -p "$GOPATH" "$GOCACHE"

# stdlib-only main.go — no `go mod download` needed
go build -o executable .

chmod +x ./executable
"""


# ---------------------------------------------------------------------------
# Executor
# ---------------------------------------------------------------------------

class GoExecutor(Executor):
    """Concrete Go language executor."""
    family: str = "go"
    file_ext: str = ".go"
    executable_name: str = "executable"

    def __init__(
        self,
        *,
        tasks_dir: Path | None = None,
        programbench_dir: Path | None = None,
    ):
        py = PythonExecutor(
            tasks_dir=tasks_dir or PythonExecutor().tasks_dir,
            programbench_dir=programbench_dir or PythonExecutor().programbench_dir,
        )
        self.tasks_dir = py.tasks_dir
        self.programbench_dir = py.programbench_dir
        self._py = py  # delegate probe + eval

    def probe(self, instance_id: str) -> ProbeResult:
        return self._py.probe(instance_id)

    def scaffold(self, probe: ProbeResult, work_dir: Path) -> ScaffoldResult:
        source = work_dir / "source"
        source.mkdir(parents=True, exist_ok=True)

        tool_name, author = _derive_tool_name(probe.instance_id)
        # Go module names: just lowercase + alnum + slashes; "tool" suffices
        module_name = "".join(c if (c.isalnum() or c in "-_") else "_" for c in tool_name.lower())
        if not module_name:
            module_name = "tool"

        (source / "go.mod").write_text(_GO_MOD.format(module_name=module_name),
                                       encoding="utf-8", newline="\n")
        (source / "main.go").write_text(_MAIN_GO.format(tool_name=tool_name),
                                        encoding="utf-8", newline="\n")
        (source / "compile.sh").write_text(_COMPILE_SH, encoding="utf-8", newline="\n")
        try:
            os.chmod(source / "compile.sh", 0o755)
        except OSError:
            pass

        readme = (
            f"# {tool_name} — Go executor scaffold\n\n"
            f"- **instance_id**: {probe.instance_id}\n"
            f"- **author**: {author}\n"
            f"- **executor**: go (stdlib flag, no external deps)\n"
            f"- **module**: {module_name}\n"
            f"- **declared flags**: {probe.declared_flags or '(none from task.yaml)'}\n"
            f"- **test count**: {probe.test_count or 'unknown'}\n\n"
            f"## Build cost\n"
            f"- cold: ~1-3s\n"
            f"- warm: <1s (GOCACHE hit)\n\n"
            f"## Eval command\n"
            f"```\n"
            f"cd {self.programbench_dir} && PYTHONUTF8=1 uv run programbench eval "
            f"{work_dir.parent} --filter '{author}' --force\n"
            f"```\n"
        )
        (source / "README_DETERMINEX.md").write_text(readme, encoding="utf-8", newline="\n")

        return ScaffoldResult(
            work_dir=work_dir,
            files_written=[source / "go.mod", source / "main.go",
                           source / "compile.sh", source / "README_DETERMINEX.md"],
        )

    def build(self, work_dir: Path) -> BuildResult:
        source = work_dir / "source"
        compile_sh = source / "compile.sh"
        if not compile_sh.is_file():
            raise ExecutorError(f"build: no compile.sh at {compile_sh}")
        if not shutil.which("go"):
            raise ExecutorError(
                "build: `go` not on PATH — install Go from https://go.dev/ or "
                "run scripts/determinex_doctor.py for a full toolchain report"
            )

        t0 = time.time()
        proc = subprocess.run(
            ["bash", "./compile.sh"],
            cwd=str(source),
            capture_output=True, text=True, timeout=120,
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
                "before hashing and the link will break."
            )
        return BuildResult(
            work_dir=work_dir,
            executable_path=executable if executable.is_file() else None,
            elapsed_seconds=round(elapsed, 2),
            stdout=proc.stdout[-2000:],
            stderr=proc.stderr[-2000:],
            ok=ok,
        )

    def eval(self, work_dir: Path, instance_id: str) -> EvalResult:
        return self._py.eval(work_dir, instance_id)


def _cli() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Go executor — run one tool through all 7 phases")
    ap.add_argument("instance_id")
    ap.add_argument("--work-dir", type=Path, default=None)
    ap.add_argument("--skip-eval", action="store_true")
    ap.add_argument("--skip-build", action="store_true")
    args = ap.parse_args()

    work_dir = args.work_dir or Path(
        f"T:/determinex-programbench/_executor_go_test/{args.instance_id}"
    )
    work_dir.mkdir(parents=True, exist_ok=True)

    ex = GoExecutor()
    print(f"=== probe {args.instance_id} ===")
    probe = ex.probe(args.instance_id)
    print(f"  flags: {probe.declared_flags}  tests: {probe.test_count}  notes: {probe.notes}")

    print(f"=== scaffold {work_dir} ===")
    sc = ex.scaffold(probe, work_dir)
    print(f"  wrote {len(sc.files_written)} files")

    if args.skip_build:
        return 0

    print(f"=== build ===")
    b = ex.build(work_dir)
    print(f"  ok={b.ok}  elapsed={b.elapsed_seconds}s  exec={b.executable_path}")
    if not b.ok:
        print(f"  stderr: {b.stderr[:400]}")
        return 1

    print(f"=== pack ===")
    p = ex.pack(work_dir)
    print(f"  submission: {p.submission_path}  ({p.n_files} files)")

    if args.skip_eval:
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
