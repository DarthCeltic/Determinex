"""executors/c.py — concrete C language executor.

13 of 115 in-scope residual ProgramBench tools have a C upstream. Build cost
is tiny (~0.5s) since we compile a single source file with `cc -O2`. Uses
POSIX argv parsing — no dependencies, no autoconf, no make.

The 8 universal CLI patterns are implemented with the same clap-style wording
and rc=1 on unknown args as Python/Rust/Go so cross-language test goldens
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

_MAIN_C = r"""/* {tool_name} -- Determinex mass-run C scaffold.
 *
 * Bakes in the 8 universal CLI patterns: invalid, multiple, help, empty,
 * no-*, unknown, version, missing. Tool-specific behavior is the iteration
 * target.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <sys/stat.h>

static const char *TOOL   = "{tool_name}";
static const char *VER    = "0.1.0";

static void print_usage(FILE *fp) {{
    fprintf(fp,
        "Usage: %s [OPTIONS] [INPUT...]\n\n"
        "Options:\n"
        "  -h, --help     show this help and exit\n"
        "  -V, --version  show version and exit\n"
        "  -o, --output FILE  write output to FILE\n"
        "      --no-color disable color output\n"
        "      --color    enable color output\n",
        TOOL);
}}

static int write_buf(const char *out_path, const char *buf, size_t n) {{
    FILE *out = out_path ? fopen(out_path, "wb") : stdout;
    if (!out) {{
        fprintf(stderr, "%s: write error: %s\n", TOOL, strerror(errno));
        return 2;
    }}
    if (fwrite(buf, 1, n, out) != n) {{
        fprintf(stderr, "%s: short write\n", TOOL);
        if (out != stdout) fclose(out);
        return 2;
    }}
    if (out != stdout) fclose(out);
    return 0;
}}

static int process_stdin(const char *out_path) {{
    /* Read all of stdin into a growing buffer. */
    size_t cap = 4096, len = 0;
    char *buf = malloc(cap);
    if (!buf) return 2;
    for (;;) {{
        if (len + 4096 > cap) {{
            cap *= 2;
            char *nb = realloc(buf, cap);
            if (!nb) {{ free(buf); return 2; }}
            buf = nb;
        }}
        size_t got = fread(buf + len, 1, cap - len, stdin);
        len += got;
        if (got == 0) break;
    }}
    if (len == 0) {{
        free(buf);
        return 0;  /* empty stdin -> exit 0 (pattern 4) */
    }}
    int rc = write_buf(out_path, buf, len);
    free(buf);
    return rc;
}}

static int process_file(const char *path, const char *out_path) {{
    struct stat st;
    if (stat(path, &st) != 0) {{
        fprintf(stderr, "%s: cannot access '%s': No such file or directory\n",
                TOOL, path);
        return 2;
    }}
    if (S_ISDIR(st.st_mode)) {{
        fprintf(stderr, "%s: '%s' is a directory\n", TOOL, path);
        return 2;
    }}
    FILE *fp = fopen(path, "rb");
    if (!fp) {{
        fprintf(stderr, "%s: '%s': %s\n", TOOL, path, strerror(errno));
        return 2;
    }}
    size_t cap = (size_t)st.st_size + 1;
    char *buf = malloc(cap);
    if (!buf) {{ fclose(fp); return 2; }}
    size_t n = fread(buf, 1, cap, fp);
    fclose(fp);
    int rc = write_buf(out_path, buf, n);
    free(buf);
    return rc;
}}

int main(int argc, char **argv) {{
    const char *out_path = NULL;
    int positional_start = -1;

    for (int i = 1; i < argc; i++) {{
        const char *a = argv[i];
        if (strcmp(a, "--") == 0) {{ positional_start = i + 1; break; }}
        if (strcmp(a, "-") == 0) {{ positional_start = i; break; }}
        if (strcmp(a, "-h") == 0 || strcmp(a, "--help") == 0) {{
            print_usage(stdout);
            return 0;
        }}
        if (strcmp(a, "-V") == 0 || strcmp(a, "--version") == 0) {{
            printf("%s %s\n", TOOL, VER);
            return 0;
        }}
        if (strcmp(a, "--no-color") == 0 || strcmp(a, "--color") == 0) {{
            continue;
        }}
        if (strcmp(a, "-o") == 0 || strcmp(a, "--output") == 0) {{
            if (i + 1 >= argc) {{
                fprintf(stderr, "error: missing argument for %s\n", a);
                return 1;
            }}
            out_path = argv[++i];
            continue;
        }}
        if (strncmp(a, "--output=", 9) == 0) {{
            out_path = a + 9;
            continue;
        }}
        if (a[0] == '-' && a[1] != '\0') {{
            /* unknown flag -- clap-style wording + rc=1 (iter-1 convention) */
            fprintf(stderr, "error: unexpected argument '%s' found\n\n", a);
            fprintf(stderr, "Usage: %s [OPTIONS] [INPUT...]\n\n", TOOL);
            fprintf(stderr, "For more information, try '--help'.\n");
            return 1;
        }}
        positional_start = i;
        break;
    }}

    if (positional_start < 0 || positional_start >= argc) {{
        if (!isatty(STDIN_FILENO)) {{
            return process_stdin(out_path);
        }}
        return 0;
    }}

    int rc = 0;
    for (int i = positional_start; i < argc; i++) {{
        if (strcmp(argv[i], "-") == 0) {{
            rc |= process_stdin(out_path);
            continue;
        }}
        rc |= process_file(argv[i], out_path);
    }}
    return rc;
}}
"""


_COMPILE_SH = """#!/bin/bash
set -e
# cc -O2 keeps the binary small for the cleanroom image; -std=c11 for portable
# language defaults; -Wall to catch obvious scaffold bugs early.
cc -O2 -std=c11 -Wall -o executable main.c
chmod +x ./executable
"""


class CExecutor(Executor):
    """Concrete C language executor."""

    family: str = "c"
    file_ext: str = ".c"
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

        (source / "main.c").write_text(
            _MAIN_C.format(tool_name=tool_name), encoding="utf-8", newline="\n"
        )
        (source / "compile.sh").write_text(_COMPILE_SH, encoding="utf-8", newline="\n")
        try:
            os.chmod(source / "compile.sh", 0o755)
        except OSError:
            pass

        readme = (
            f"# {tool_name} — C executor scaffold\n\n"
            f"- **instance_id**: {probe.instance_id}\n"
            f"- **author**: {author}\n"
            f"- **executor**: c (POSIX, no deps)\n"
            f"- **test count**: {probe.test_count or 'unknown'}\n\n"
            f"## Build cost\n- typically <1s with cc -O2\n\n"
            f"## Eval command\n"
            f"```\ncd {self.programbench_dir} && PYTHONUTF8=1 uv run programbench eval "
            f"{work_dir.parent} --filter '{author}' --force\n```\n"
        )
        (source / "README_DETERMINEX.md").write_text(readme, encoding="utf-8", newline="\n")

        return ScaffoldResult(
            work_dir=work_dir,
            files_written=[
                source / "main.c",
                source / "compile.sh",
                source / "README_DETERMINEX.md",
            ],
        )

    def build(self, work_dir: Path) -> BuildResult:
        source = work_dir / "source"
        compile_sh = source / "compile.sh"
        if not compile_sh.is_file():
            raise ExecutorError(f"build: no compile.sh at {compile_sh}")
        if not (shutil.which("cc") or shutil.which("gcc") or shutil.which("clang")):
            raise ExecutorError(
                "build: no C compiler (cc/gcc/clang) on PATH — "
                "run scripts/determinex_doctor.py for a toolchain report"
            )
        t0 = time.time()
        proc = subprocess.run(
            ["bash", "./compile.sh"],
            cwd=str(source),
            capture_output=True,
            text=True,
            timeout=60,
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

    ap = argparse.ArgumentParser(description="C executor — run one tool through all 7 phases")
    ap.add_argument("instance_id")
    ap.add_argument("--work-dir", type=Path, default=None)
    ap.add_argument("--skip-eval", action="store_true")
    ap.add_argument("--skip-build", action="store_true")
    args = ap.parse_args()

    work_dir = args.work_dir or Path(
        f"T:/determinex-programbench/_executor_c_test/{args.instance_id}"
    )
    work_dir.mkdir(parents=True, exist_ok=True)

    ex = CExecutor()
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
