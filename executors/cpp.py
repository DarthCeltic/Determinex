"""executors/cpp.py — concrete C++ language executor.

6 of 115 in-scope residual ProgramBench tools have a C++ upstream — smallest
of the four major language groups. Mostly a sibling of CExecutor with a
C++17 toolchain and a slightly more idiomatic main.cpp using std::string +
<filesystem> for path handling.

Same iter-1 clap-style wording + rc=1 convention so cross-language goldens
stay aligned.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import time
from pathlib import Path

from .base import (
    BuildResult,
    EvalResult,
    Executor,
    ExecutorError,
    ProbeResult,
    ScaffoldResult,
)
from .python import PythonExecutor, _derive_tool_name

_MAIN_CPP = r"""// {tool_name} -- Determinex mass-run C++ scaffold.
//
// Bakes in the 8 universal CLI patterns with iter-1 clap-style wording.

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <unistd.h>

namespace fs = std::filesystem;

static constexpr const char* TOOL_NAME = "{tool_name}";
static constexpr const char* TOOL_VER  = "0.1.0";

static void print_usage(std::ostream& os) {{
    os << "Usage: " << TOOL_NAME << " [OPTIONS] [INPUT...]\n\n"
       << "Options:\n"
       << "  -h, --help     show this help and exit\n"
       << "  -V, --version  show version and exit\n"
       << "  -o, --output FILE  write output to FILE\n"
       << "      --no-color disable color output\n"
       << "      --color    enable color output\n";
}}

static int write_buf(const std::string& out_path, const std::string& buf) {{
    if (out_path.empty()) {{
        std::cout.write(buf.data(), static_cast<std::streamsize>(buf.size()));
        return 0;
    }}
    std::ofstream out(out_path, std::ios::binary);
    if (!out) {{
        std::cerr << TOOL_NAME << ": write error opening " << out_path << "\n";
        return 2;
    }}
    out.write(buf.data(), static_cast<std::streamsize>(buf.size()));
    return out ? 0 : 2;
}}

static int process_stdin(const std::string& out_path) {{
    std::ostringstream ss;
    ss << std::cin.rdbuf();
    std::string buf = ss.str();
    if (buf.empty()) return 0;
    return write_buf(out_path, buf);
}}

static int process_file(const std::string& path, const std::string& out_path) {{
    std::error_code ec;
    if (!fs::exists(path, ec)) {{
        std::cerr << TOOL_NAME << ": cannot access '" << path
                  << "': No such file or directory\n";
        return 2;
    }}
    if (fs::is_directory(path, ec)) {{
        std::cerr << TOOL_NAME << ": '" << path << "' is a directory\n";
        return 2;
    }}
    std::ifstream in(path, std::ios::binary);
    if (!in) {{
        std::cerr << TOOL_NAME << ": '" << path << "': open failed\n";
        return 2;
    }}
    std::ostringstream ss;
    ss << in.rdbuf();
    return write_buf(out_path, ss.str());
}}

int main(int argc, char** argv) {{
    std::string out_path;
    std::vector<std::string> positionals;
    bool no_color = false;
    bool color = false;

    for (int i = 1; i < argc; ++i) {{
        std::string a = argv[i];
        if (a == "--") {{
            for (int j = i + 1; j < argc; ++j) positionals.emplace_back(argv[j]);
            break;
        }}
        if (a == "-") {{ positionals.emplace_back("-"); continue; }}
        if (a == "-h" || a == "--help")    {{ print_usage(std::cout); return 0; }}
        if (a == "-V" || a == "--version") {{
            std::cout << TOOL_NAME << " " << TOOL_VER << "\n";
            return 0;
        }}
        if (a == "--no-color") {{ no_color = true; continue; }}
        if (a == "--color")    {{ color    = true; continue; }}
        if (a == "-o" || a == "--output") {{
            if (i + 1 >= argc) {{
                std::cerr << "error: missing argument for " << a << "\n";
                return 1;
            }}
            out_path = argv[++i];
            continue;
        }}
        if (a.rfind("--output=", 0) == 0) {{
            out_path = a.substr(9);
            continue;
        }}
        if (!a.empty() && a[0] == '-' && a.size() > 1) {{
            std::cerr << "error: unexpected argument '" << a << "' found\n\n";
            std::cerr << "Usage: " << TOOL_NAME << " [OPTIONS] [INPUT...]\n\n";
            std::cerr << "For more information, try '--help'.\n";
            return 1;
        }}
        positionals.push_back(a);
    }}

    (void)no_color; (void)color;

    if (positionals.empty()) {{
        if (!isatty(STDIN_FILENO)) return process_stdin(out_path);
        return 0;
    }}

    int rc = 0;
    for (const auto& p : positionals) {{
        if (p == "-") {{ rc |= process_stdin(out_path); continue; }}
        rc |= process_file(p, out_path);
    }}
    return rc;
}}
"""


_COMPILE_SH = """#!/bin/bash
set -e
# c++ -O2 -std=c++17 keeps the binary self-contained for the cleanroom image.
# <filesystem> requires C++17 minimum.
c++ -O2 -std=c++17 -Wall -o executable main.cpp
chmod +x ./executable
"""


class CppExecutor(Executor):
    """Concrete C++ language executor."""

    family: str = "cpp"
    file_ext: str = ".cpp"
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
        self._py = py

    def probe(self, instance_id: str) -> ProbeResult:
        return self._py.probe(instance_id)

    def scaffold(self, probe: ProbeResult, work_dir: Path) -> ScaffoldResult:
        source = work_dir / "source"
        source.mkdir(parents=True, exist_ok=True)
        tool_name, author = _derive_tool_name(probe.instance_id)

        (source / "main.cpp").write_text(
            _MAIN_CPP.format(tool_name=tool_name), encoding="utf-8", newline="\n"
        )
        (source / "compile.sh").write_text(_COMPILE_SH, encoding="utf-8", newline="\n")
        try:
            os.chmod(source / "compile.sh", 0o755)
        except OSError:
            pass

        readme = (
            f"# {tool_name} — C++ executor scaffold\n\n"
            f"- **instance_id**: {probe.instance_id}\n"
            f"- **author**: {author}\n"
            f"- **executor**: cpp (C++17, <filesystem>)\n"
            f"- **test count**: {probe.test_count or 'unknown'}\n\n"
            f"## Build cost\n- typically 1-3s with c++ -O2 -std=c++17\n"
        )
        (source / "README_DETERMINEX.md").write_text(readme, encoding="utf-8", newline="\n")

        return ScaffoldResult(
            work_dir=work_dir,
            files_written=[
                source / "main.cpp",
                source / "compile.sh",
                source / "README_DETERMINEX.md",
            ],
        )

    def build(self, work_dir: Path) -> BuildResult:
        source = work_dir / "source"
        compile_sh = source / "compile.sh"
        if not compile_sh.is_file():
            raise ExecutorError(f"build: no compile.sh at {compile_sh}")
        if not (shutil.which("c++") or shutil.which("g++") or shutil.which("clang++")):
            raise ExecutorError(
                "build: no C++ compiler (c++/g++/clang++) on PATH — "
                "run scripts/determinex_doctor.py for a toolchain report"
            )
        t0 = time.time()
        proc = subprocess.run(
            ["bash", "./compile.sh"],
            cwd=str(source),
            capture_output=True,
            text=True,
            timeout=120,
        )
        elapsed = time.time() - t0
        executable = source / self.executable_name
        ok = proc.returncode == 0 and executable.is_file() and not executable.is_symlink()
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

    ap = argparse.ArgumentParser(description="C++ executor — run one tool through all 7 phases")
    ap.add_argument("instance_id")
    ap.add_argument("--work-dir", type=Path, default=None)
    ap.add_argument("--skip-eval", action="store_true")
    ap.add_argument("--skip-build", action="store_true")
    args = ap.parse_args()

    work_dir = args.work_dir or Path(
        f"T:/determinex-programbench/_executor_cpp_test/{args.instance_id}"
    )
    work_dir.mkdir(parents=True, exist_ok=True)

    ex = CppExecutor()
    probe = ex.probe(args.instance_id)
    print(f"=== probe: {probe.instance_id}  tests={probe.test_count}  notes={probe.notes}")
    sc = ex.scaffold(probe, work_dir)
    print(f"=== scaffold: wrote {len(sc.files_written)} files to {sc.work_dir}")
    if args.skip_build:
        return 0
    b = ex.build(work_dir)
    print(f"=== build: ok={b.ok}  elapsed={b.elapsed_seconds}s  exec={b.executable_path}")
    if not b.ok:
        print(b.stderr[:600])
        return 1
    p = ex.pack(work_dir)
    print(f"=== pack: {p.submission_path} ({p.n_files} files)")
    if args.skip_eval:
        return 0
    e = ex.eval(work_dir, args.instance_id)
    if e.error:
        print(f"ERROR: {e.error}")
        return 1
    print(f"=== eval: {e.score}/100  ({e.passed}/{e.total})")
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
