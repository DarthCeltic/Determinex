"""executors/python.py — concrete Python executor.

First language profile to implement the 7-phase executor contract end-to-end.
The Python executor is the cheapest: `compile.sh` is `cp main.py executable`,
no toolchain needed, scaffold smoke-tests in milliseconds.

What this owns:
  probe       — load task.yaml + tests.json from the programbench data dir;
                surface declared flags + dependencies + test count
  scaffold    — write source/{main.py, compile.sh, README_DETERMINEX.md} via
                the same PYTHON_TEMPLATE that mass_run_v2_scaffold.py uses
  build       — chmod + cp main.py -> executable; verify it's not a symlink
                (programbench moves the file to /opt and symlinks break)
  pack        — inherited from base.Executor (deterministic tar via mass_run_v2_pack)
  eval        — call the official programbench eval harness via subprocess;
                read back the eval.json the harness writes to disk
  classify    — inherited from base.Executor (routes through central taxonomy)
  report      — inherited from base.Executor (markdown summary)

Cockpit integration: every phase writes a LedgerEvent so the live monitor
shows progress per tool per phase.

Usage (programmatic):
    from executors.python import PythonExecutor
    ex = PythonExecutor()
    probe   = ex.probe(instance_id="psampaz__go-mod-outdated.bb79367")
    scaff   = ex.scaffold(probe, work_dir=Path("T:/.../psampaz.../"))
    build   = ex.build(scaff.work_dir)
    pack    = ex.pack(build.work_dir)
    eval_r  = ex.eval(pack.submission_path.parent, instance_id=probe.instance_id)
    classif = ex.classify(eval_r)
    report  = ex.report(eval_r, classif)
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional

from .base import (
    Executor, ExecutorError,
    ProbeResult, ScaffoldResult, BuildResult, EvalResult,
)


# Where programbench task definitions live (env-overridable for cross-machine repro)
_DEFAULT_TASKS_DIR = Path(os.environ.get(
    "DETERMINEX_PB_TASKS_DIR",
    "T:/Dev/ProgramBench/src/programbench/data/tasks",
))
_DEFAULT_PB_DIR = Path(os.environ.get(
    "PROGRAMBENCH_DIR",
    "T:/Dev/ProgramBench",
))


# Source-of-truth template — reuses the same PYTHON_TEMPLATE from mass_run_v2_scaffold.
# We import it lazily so the executor module stays importable even if scaffold.py
# isn't on path.
def _get_python_template() -> str:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
    from mass_run_v2_scaffold import PYTHON_TEMPLATE  # type: ignore[import-not-found]
    return PYTHON_TEMPLATE


def _get_compile_sh() -> str:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
    from mass_run_v2_scaffold import COMPILE_SH  # type: ignore[import-not-found]
    return COMPILE_SH


def _derive_tool_name(instance_id: str) -> tuple[str, str]:
    """Parse 'author__tool.hash' → (tool, author)."""
    head, _, _ = instance_id.partition(".")
    author, _, tool = head.partition("__")
    return tool or head, author or "unknown"


# ---------------------------------------------------------------------------
# Executor
# ---------------------------------------------------------------------------

class PythonExecutor(Executor):
    """Concrete Python language executor. Default scaffold + thin compile."""
    family: str = "python"
    file_ext: str = ".py"
    executable_name: str = "executable"

    def __init__(
        self,
        *,
        tasks_dir: Path = _DEFAULT_TASKS_DIR,
        programbench_dir: Path = _DEFAULT_PB_DIR,
    ):
        self.tasks_dir = tasks_dir
        self.programbench_dir = programbench_dir

    # ── probe ─────────────────────────────────────────────────────────────
    def probe(self, instance_id: str) -> ProbeResult:
        """Load task.yaml + tests.json from the programbench data dir.

        The full upstream-binary probe lives in scripts/determinex_programbench_probe.py;
        here we only extract metadata the scaffold needs (declared flags / deps /
        test count). The expensive probe (extracting JUnit fixtures) stays in
        the dedicated probe script.
        """
        task_dir = self.tasks_dir / instance_id
        if not task_dir.is_dir():
            raise ExecutorError(f"probe: task dir not found: {task_dir}")

        declared_flags: list[str] = []
        declared_subcommands: list[str] = []
        deps: list[str] = []
        test_count = 0
        notes: list[str] = []

        # task.yaml — best-effort PyYAML import
        task_yaml = task_dir / "task.yaml"
        if task_yaml.is_file():
            try:
                import yaml  # type: ignore[import-untyped]
                td = yaml.safe_load(task_yaml.read_text(encoding="utf-8")) or {}
                # Common field names across PB task definitions
                if isinstance(td.get("flags"), list):
                    declared_flags = list(td["flags"])
                if isinstance(td.get("subcommands"), list):
                    declared_subcommands = list(td["subcommands"])
                if isinstance(td.get("dependencies"), list):
                    deps = list(td["dependencies"])
                if "language" in td:
                    notes.append(f"upstream language: {td['language']}")
            except ImportError:
                notes.append("pyyaml not installed; task.yaml not parsed")
            except Exception as e:
                notes.append(f"task.yaml parse warning: {type(e).__name__}: {e}")

        # tests.json — count tests if present (the harness publishes per-task counts)
        tests_json = task_dir / "tests.json"
        if tests_json.is_file():
            try:
                import json
                tj = json.loads(tests_json.read_text(encoding="utf-8"))
                if isinstance(tj, list):
                    test_count = len(tj)
                elif isinstance(tj, dict) and "tests" in tj:
                    test_count = len(tj["tests"])
            except Exception as e:
                notes.append(f"tests.json parse warning: {type(e).__name__}: {e}")

        return ProbeResult(
            instance_id=instance_id,
            upstream_language=None,
            declared_flags=declared_flags,
            declared_subcommands=declared_subcommands,
            deps=deps,
            test_count=test_count,
            notes=notes,
        )

    # ── scaffold ──────────────────────────────────────────────────────────
    def scaffold(self, probe: ProbeResult, work_dir: Path) -> ScaffoldResult:
        """Write source/{main.py, compile.sh, README_DETERMINEX.md}. Idempotent."""
        source = work_dir / "source"
        source.mkdir(parents=True, exist_ok=True)

        tool_name, author = _derive_tool_name(probe.instance_id)

        main_py = _get_python_template().format(
            tool_name=tool_name,
            tool_name_repr=repr(tool_name),
        )
        (source / "main.py").write_text(main_py, encoding="utf-8", newline="\n")
        (source / "compile.sh").write_text(_get_compile_sh(), encoding="utf-8", newline="\n")
        try:
            os.chmod(source / "compile.sh", 0o755)
        except OSError:
            pass

        readme = (
            f"# {tool_name} — Python executor scaffold\n\n"
            f"- **instance_id**: {probe.instance_id}\n"
            f"- **author**: {author}\n"
            f"- **executor**: python ({self.file_ext})\n"
            f"- **declared flags**: {probe.declared_flags or '(none from task.yaml)'}\n"
            f"- **test count**: {probe.test_count or 'unknown'}\n"
            f"- **notes**: {probe.notes or '(none)'}\n\n"
            f"## Eval command\n"
            f"```\n"
            f"cd {self.programbench_dir} && PYTHONUTF8=1 uv run programbench eval "
            f"{work_dir.parent} --filter '{author}' --force\n"
            f"```\n"
        )
        (source / "README_DETERMINEX.md").write_text(readme, encoding="utf-8", newline="\n")

        return ScaffoldResult(
            work_dir=work_dir,
            files_written=[source / "main.py", source / "compile.sh", source / "README_DETERMINEX.md"],
        )

    # ── build ─────────────────────────────────────────────────────────────
    def build(self, work_dir: Path) -> BuildResult:
        """Run compile.sh; verify ./executable is a real file (not a symlink).

        ProgramBench moves the executable to /opt before hashing, and symlinks
        break after the move. This check catches that class of bug at build time
        instead of at hash-failure time.
        """
        source = work_dir / "source"
        compile_sh = source / "compile.sh"
        if not compile_sh.is_file():
            raise ExecutorError(f"build: no compile.sh at {compile_sh}")

        t0 = time.time()
        if os.name == "nt":
            main_py = source / "main.py"
            if not main_py.is_file():
                raise ExecutorError(f"build: no main.py at {main_py}")
            executable = source / self.executable_name
            shutil.copyfile(main_py, executable)
            try:
                os.chmod(executable, 0o755)
            except OSError:
                pass
            proc = subprocess.CompletedProcess(
                args=["python-native-copy", str(main_py), str(executable)],
                returncode=0,
                stdout="",
                stderr="",
            )
        else:
            proc = subprocess.run(
                ["bash", "./compile.sh"],
                cwd=str(source),
                capture_output=True, text=True, timeout=60,
            )
        elapsed = time.time() - t0
        executable = source / self.executable_name
        ok = (
            proc.returncode == 0
            and executable.is_file()
            and not executable.is_symlink()
        )
        if not ok and executable.is_symlink():
            # Honest error: the audit caught this class of bug across SWE-bench too
            raise ExecutorError(
                f"build: {executable} is a symlink — ProgramBench moves it to /opt "
                "before hashing and the link will break. compile.sh must produce a "
                "real file (use `cp`, not `ln -s`)."
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
        """Run the official programbench eval harness for this one tool.

        work_dir should be the PARENT of the per-instance dir (programbench eval
        scans subdirs); our scaffold convention is mass_run_v2_*/<instance_id>/.
        """
        run_dir = work_dir.parent
        author = _derive_tool_name(instance_id)[1]

        # programbench's CLI takes a directory containing one or more
        # <instance_id>/submission.tar.gz entries. Always route through the
        # resource guard: some "single" evals still fan out inside Docker via
        # pytest-xdist and subprocess-heavy tests.
        import sys as _sys
        _scripts = Path(__file__).resolve().parent.parent / "scripts"
        if str(_scripts) not in _sys.path:
            _sys.path.insert(0, str(_scripts))
        from programbench_resource_guard import build_eval_cmd  # type: ignore[import-not-found]

        cmd, policy = build_eval_cmd(
            scaffold_root=run_dir,
            filter_re=author,
            instance_id=instance_id,
            force=True,
        )
        if policy.quarantined:
            return EvalResult(
                instance_id=instance_id,
                error=f"eval quarantined by resource guard: {policy.reason}",
            )
        env = os.environ.copy()
        env["PYTHONUTF8"] = "1"
        try:
            proc = subprocess.run(
                cmd, cwd=str(self.programbench_dir),
                capture_output=True, text=True, timeout=policy.timeout_seconds, env=env,
            )
        except subprocess.TimeoutExpired:
            return EvalResult(
                instance_id=instance_id,
                error=f"eval timed out after {policy.timeout_seconds}s",
            )
        except FileNotFoundError as e:
            return EvalResult(
                instance_id=instance_id,
                error=f"eval: programbench/uv not on PATH ({e}) — set PROGRAMBENCH_DIR env var",
            )

        # The harness writes <instance_id>/<instance_id>.eval.json
        inst_dir = work_dir
        eval_json: Optional[Path] = None
        for p in inst_dir.glob("*.eval.json"):
            eval_json = p
            break
        if eval_json is None:
            err = (proc.stderr or proc.stdout or "")[:500]
            return EvalResult(
                instance_id=instance_id,
                error=f"eval: no eval.json written. stderr/stdout: {err}",
            )

        import json as _json
        try:
            d = _json.loads(eval_json.read_text(encoding="utf-8"))
        except Exception as e:
            return EvalResult(instance_id=instance_id, error=f"eval JSON parse: {e}")

        if d.get("error_code"):
            return EvalResult(
                instance_id=instance_id,
                error=f"eval error_code={d['error_code']} details={str(d.get('error_details',''))[:200]}",
                eval_json_path=eval_json,
            )

        results = d.get("test_results", [])
        passed = sum(1 for r in results if r.get("status") == "passed")
        failed = sum(1 for r in results if r.get("status") == "failure")
        total = passed + failed
        score = round(100 * passed / total, 1) if total else 0.0
        return EvalResult(
            instance_id=instance_id,
            score=score,
            passed=passed,
            total=total,
            eval_json_path=eval_json,
        )


# ---------------------------------------------------------------------------
# CLI — one-shot end-to-end run for a single tool
# ---------------------------------------------------------------------------

def _cli() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Python executor — run one tool through all 7 phases")
    ap.add_argument("instance_id", help="e.g. psampaz__go-mod-outdated.bb79367")
    ap.add_argument("--work-dir", type=Path, default=None,
                    help="work dir (default: T:/determinex-programbench/_executor_test/<instance>/)")
    ap.add_argument("--skip-eval", action="store_true",
                    help="skip the official eval (useful for scaffold+build smoke)")
    args = ap.parse_args()

    work_dir = args.work_dir or Path(
        f"T:/determinex-programbench/_executor_test/{args.instance_id}"
    )
    work_dir.mkdir(parents=True, exist_ok=True)

    ex = PythonExecutor()
    print(f"=== probe {args.instance_id} ===")
    probe = ex.probe(args.instance_id)
    print(f"  flags: {probe.declared_flags}")
    print(f"  tests: {probe.test_count}")
    print(f"  notes: {probe.notes}")

    print(f"=== scaffold {work_dir} ===")
    sc = ex.scaffold(probe, work_dir)
    print(f"  wrote {len(sc.files_written)} files")

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
        print("=== skipping eval (--skip-eval) ===")
        return 0

    print(f"=== eval ===")
    e = ex.eval(work_dir, args.instance_id)
    if e.error:
        print(f"  ERROR: {e.error}")
        return 1
    print(f"  score: {e.score}/100  ({e.passed}/{e.total})")

    print(f"=== classify ===")
    c = ex.classify(e)
    print(f"  top families: {sorted(c.families.items(), key=lambda kv: -kv[1])[:5]}")

    print(f"=== report ===")
    r = ex.report(e, c)
    print()
    print(r.summary_md)
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
