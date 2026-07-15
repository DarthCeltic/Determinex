"""executors/ — language-family executors for Determinex benchmark builds.

Each per-language executor owns the full lifecycle of a tool build through the
contract:

    probe -> scaffold -> build -> pack -> eval -> classify -> report

The shared protocol lives in `base.py`. Profiles live in per-language modules
(`python_executor.py`, `rust_executor.py`, etc.). The IDE / orchestrator picks
an executor by family and calls its lifecycle methods in order.

See `executors/README.md` for the design rationale, contract details, and the
mapping to `corpus/programbench/_strategy/language_family_sprint_matrix.md`.
"""

from .base import (
    Executor, ExecutorContract,
    ProbeResult, ScaffoldResult, BuildResult, PackResult,
    EvalResult, ClassifyResult, ReportResult,
    ExecutorError,
)
from .python import PythonExecutor
from .rust import RustExecutor
from .go import GoExecutor
from .c import CExecutor
from .cpp import CppExecutor

__all__ = [
    # Protocol + base class
    "Executor", "ExecutorContract",
    # Result types
    "ProbeResult", "ScaffoldResult", "BuildResult", "PackResult",
    "EvalResult", "ClassifyResult", "ReportResult",
    # Errors
    "ExecutorError",
    # Concrete executors
    "PythonExecutor",
    "RustExecutor",
    "GoExecutor",
    "CExecutor",
    "CppExecutor",
]
