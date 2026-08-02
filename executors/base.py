"""executors/base.py — the language-family executor protocol.

Every per-language executor implements the seven-phase contract:

    probe       inspect the task fixture; extract task.yaml, tests.json,
                upstream README, declared CLI surface, dependency requirements
    scaffold    write the per-language source tree to a work dir
                (compile.sh, main.<ext>, README_DETERMINEX.md, probes/)
    build       compile / install dependencies / produce ./executable
    pack        tar source -> submission.tar.gz with deterministic mtime/perms
    eval        run programbench eval / pytest / official harness; emit eval JSON
    classify    feed eval JSON to scripts/failure_classifier.py
    report      summarize: per-tool score, family histogram, recommendations

Each phase returns a structured result and writes a ledger event so the cockpit
sees the entire lifecycle. Phases are independently runnable — re-running a
later phase doesn't re-do earlier ones unless explicitly asked.

The contract is intentionally minimal. Per-language executors override the
phases that differ (e.g. RustExecutor.build runs cargo; PythonExecutor.build
just chmod+cp). The shared scaffolds + pack + eval + classify + report logic
lives here in the base class.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol

# ---------------------------------------------------------------------------
# Result types — one per phase
# ---------------------------------------------------------------------------


@dataclass
class ProbeResult:
    instance_id: str
    upstream_language: str | None = None
    declared_flags: list[str] = field(default_factory=list)
    declared_subcommands: list[str] = field(default_factory=list)
    deps: list[str] = field(default_factory=list)
    test_count: int = 0
    notes: list[str] = field(default_factory=list)


@dataclass
class ScaffoldResult:
    work_dir: Path
    files_written: list[Path] = field(default_factory=list)


@dataclass
class BuildResult:
    work_dir: Path
    executable_path: Path | None
    elapsed_seconds: float = 0.0
    stdout: str = ""
    stderr: str = ""
    ok: bool = False


@dataclass
class PackResult:
    submission_path: Path
    sha256: str | None = None
    n_files: int = 0


@dataclass
class EvalResult:
    instance_id: str
    score: float = 0.0  # 0..100
    passed: int = 0
    total: int = 0
    eval_json_path: Path | None = None
    error: str = ""


@dataclass
class ClassifyResult:
    instance_id: str
    families: dict[str, int] = field(default_factory=dict)
    other_count: int = 0


@dataclass
class ReportResult:
    instance_id: str
    summary_md: str = ""
    recommendations: list[dict] = field(default_factory=list)


class ExecutorError(Exception):
    """Phase failed in a way the orchestrator should treat as terminal."""


# ---------------------------------------------------------------------------
# Protocol — what every language executor MUST implement
# ---------------------------------------------------------------------------


class ExecutorContract(Protocol):
    """Type protocol — duck-checked, not inherited from."""

    family: str  # e.g. "python", "rust", "go", "c"
    file_ext: str  # primary source extension, e.g. ".py", ".rs", ".go"
    executable_name: str  # always "executable" — programbench contract

    def probe(self, instance_id: str) -> ProbeResult: ...
    def scaffold(self, probe: ProbeResult, work_dir: Path) -> ScaffoldResult: ...
    def build(self, work_dir: Path) -> BuildResult: ...
    def pack(self, work_dir: Path) -> PackResult: ...
    def eval(self, work_dir: Path, instance_id: str) -> EvalResult: ...
    def classify(self, eval_result: EvalResult) -> ClassifyResult: ...
    def report(self, eval_result: EvalResult, classify: ClassifyResult) -> ReportResult: ...


# ---------------------------------------------------------------------------
# Base class — default implementations the language profiles inherit
# ---------------------------------------------------------------------------


class Executor:
    """Default executor with the shared lifecycle wiring.

    Per-language subclasses override the phases that differ:
        - PythonExecutor.build         -> chmod +x main.py && cp -> executable
        - RustExecutor.build           -> cargo build --release && cp target/release/<bin>
        - GoExecutor.build             -> go build -o executable .
        - CExecutor.build              -> cc -O2 -o executable *.c
        - NodeExecutor.build           -> cp main.js executable (with shebang)
        - ShellExecutor.build          -> shebang + chmod
        - JavaExecutor.build           -> javac + jar + launcher script
    """

    family: str = "base"
    file_ext: str = ""
    executable_name: str = "executable"

    # ── probe ─────────────────────────────────────────────────────────────
    def probe(self, instance_id: str) -> ProbeResult:
        """Default: load task.yaml + tests.json from programbench data dir."""
        raise NotImplementedError("override probe() per language")

    # ── scaffold ──────────────────────────────────────────────────────────
    def scaffold(self, probe: ProbeResult, work_dir: Path) -> ScaffoldResult:
        """Default: subclasses write per-language main.<ext> + compile.sh + README."""
        raise NotImplementedError("override scaffold() per language")

    # ── build ─────────────────────────────────────────────────────────────
    def build(self, work_dir: Path) -> BuildResult:
        """Run the scaffold's compile.sh."""
        raise NotImplementedError("override build() per language")

    # ── pack ──────────────────────────────────────────────────────────────
    def pack(self, work_dir: Path) -> PackResult:
        """Default: tar source/ -> submission.tar.gz with deterministic mtimes.

        Concrete implementation lives in scripts/mass_run_v2_pack.py. This
        method is a thin shim around it so per-language executors can override
        for unusual packaging (e.g. JVM jar manifests).
        """
        # Allow the Python-side pack helper to do the work; subclasses can
        # replace this if they need different archive layout.
        import sys as _sys

        _scripts = Path(__file__).resolve().parent.parent / "scripts"
        if str(_scripts) not in _sys.path:
            _sys.path.insert(0, str(_scripts))
        from mass_run_v2_pack import pack_one  # type: ignore[import-not-found]

        sub = pack_one(work_dir)
        if sub is None:
            raise ExecutorError(f"pack: no source dir in {work_dir}")
        return PackResult(
            submission_path=sub, n_files=sum(1 for _ in (work_dir / "source").rglob("*"))
        )

    # ── eval ──────────────────────────────────────────────────────────────
    def eval(self, work_dir: Path, instance_id: str) -> EvalResult:
        """Default: programbench eval. Reads result back from <inst>/<inst>.eval.json."""
        raise NotImplementedError("override eval() if not using programbench harness")

    # ── classify ──────────────────────────────────────────────────────────
    def classify(self, eval_result: EvalResult) -> ClassifyResult:
        """Default: route through scripts/failure_classifier.py central taxonomy."""
        import json
        import sys as _sys

        _scripts = Path(__file__).resolve().parent.parent / "scripts"
        if str(_scripts) not in _sys.path:
            _sys.path.insert(0, str(_scripts))
        from failure_classifier import classify_test_results  # type: ignore[import-not-found]

        if not eval_result.eval_json_path or not eval_result.eval_json_path.exists():
            return ClassifyResult(instance_id=eval_result.instance_id)
        d = json.loads(eval_result.eval_json_path.read_text(encoding="utf-8"))
        families = dict(classify_test_results(d.get("test_results", [])))
        return ClassifyResult(
            instance_id=eval_result.instance_id,
            families=families,
            other_count=families.get("other", 0),
        )

    # ── report ────────────────────────────────────────────────────────────
    def report(self, eval_result: EvalResult, classify: ClassifyResult) -> ReportResult:
        """Default: short markdown summary; recommendations come from the advisor."""
        lines = [
            f"# {eval_result.instance_id}",
            f"- score: **{eval_result.score}/100**",
            f"- passed/total: {eval_result.passed}/{eval_result.total}",
            f"- top failure family: {max(classify.families.items(), key=lambda kv: kv[1])[0] if classify.families else '(none)'}",
            "",
            "## Family histogram",
        ]
        for fam, n in sorted(classify.families.items(), key=lambda kv: -kv[1]):
            lines.append(f"  - {fam}: {n}")
        return ReportResult(
            instance_id=eval_result.instance_id,
            summary_md="\n".join(lines),
        )
