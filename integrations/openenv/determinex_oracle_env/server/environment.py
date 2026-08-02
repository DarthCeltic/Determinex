"""
integrations/openenv/determinex_oracle_env/server/environment.py
------------------------------------------------------------------
Server-side Environment: wraps Determinex's Universal Ground-Truth Oracle
(scripts/determinex_oracle.py) behind the OpenEnv Environment interface.

This does NOT reimplement verification. Per Determinex's own audit-before-build
rule, it imports and calls the existing, already-proven oracle module --
the exact same code path Determinex's Hive Mind loop and ProgramBench harness
use as "the entire reward model" (CLAUDE.md). Nothing about the reward
signal is novel here; only the OpenEnv-compatible packaging is new.

Episode semantics:
  reset(task_dir=..., language=...)  -> copy a reference project skeleton
                                          into a fresh, isolated tempdir
  step(DeterminexOracleAction)          -> write/remove files, run oracle.verify(),
                                          return the real pass/fail verdict
  done = True once the oracle passes (task solved) or the toolchain for the
  requested language is unavailable on this host (can't proceed).
"""

from __future__ import annotations

import shutil
import sys
import tempfile
import uuid
from pathlib import Path

from openenv.core.env_server.interfaces import Action, Environment, Observation

from ..models import DeterminexOracleAction, DeterminexOracleObservation, DeterminexOracleState

_SCRIPTS_DIR = Path(__file__).resolve().parents[4] / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

import determinex_oracle as _oracle  # noqa: E402  (Determinex's real oracle module)

_RAW_TAIL_CHARS = 2000


class DeterminexOracleEnv(Environment):
    """Compiler/test-verified coding environment. No LLM judge, ever.

    Args:
        task_dir: Path to a reference project skeleton (e.g. a
            corpus/programbench/per_tool_overrides/<tool>/ directory, or any
            buildable project scaffold). Copied fresh into an isolated
            workspace on every reset() so episodes never corrupt each other
            or the reference.
        language: Oracle key from determinex_oracle.get_oracle() (e.g. "rust",
            "go", "python", "typescript"). Can be overridden per-episode via
            reset(language=...).
    """

    def __init__(self, task_dir: str | None = None, language: str | None = None):
        super().__init__()
        self._default_task_dir = Path(task_dir) if task_dir else None
        self._default_language = language
        self._state = DeterminexOracleState()

    def reset(
        self,
        seed: int | None = None,
        episode_id: str | None = None,
        **kwargs,
    ) -> Observation:
        task_dir = Path(kwargs.get("task_dir", self._default_task_dir or ""))
        language = kwargs.get("language", self._default_language)
        if not task_dir or not task_dir.is_dir():
            raise ValueError(
                f"DeterminexOracleEnv.reset(): task_dir '{task_dir}' does not exist. "
                "Pass task_dir=<reference project skeleton> either at construction "
                "or as a reset() kwarg."
            )
        if not language:
            raise ValueError("DeterminexOracleEnv.reset(): language is required.")

        workdir = Path(tempfile.mkdtemp(prefix="determinex_oracle_env_"))
        shutil.rmtree(workdir)  # copytree requires the destination not exist
        shutil.copytree(task_dir, workdir)

        self._state = DeterminexOracleState(
            episode_id=episode_id or str(uuid.uuid4()),
            step_count=0,
            language=language,
            workdir=str(workdir),
            attempts=0,
        )
        observation = DeterminexOracleObservation(done=False, reward=None)
        return self._apply_transform(observation)

    def step(self, action: Action, timeout_s: float | None = None, **kwargs) -> Observation:
        if not isinstance(action, DeterminexOracleAction):
            raise ValueError(f"Expected DeterminexOracleAction, got {type(action)}")
        if not self._state.workdir:
            raise RuntimeError("DeterminexOracleEnv.step() called before reset().")

        workdir = Path(self._state.workdir)
        for rel in action.remove:
            target = workdir / rel
            if target.exists():
                target.unlink()
        for rel, content in action.files.items():
            target = workdir / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")

        self._state.step_count += 1
        self._state.attempts += 1

        try:
            oracle = _oracle.get_oracle(self._state.language)
            result = oracle.verify(workdir)
            observation = DeterminexOracleObservation(
                done=result.passed,
                reward=1.0 if result.passed else 0.0,
                passed=result.passed,
                oracle=result.oracle,
                total=result.total,
                n_passed=result.n_passed,
                failures=[f"{f.name}: {f.text[:300]}" for f in result.failures[:20]],
                raw_tail=result.raw[-_RAW_TAIL_CHARS:],
            )
        except _oracle.OracleUnavailable as e:
            observation = DeterminexOracleObservation(
                done=True,
                reward=0.0,
                passed=False,
                error=str(e),
            )

        return self._apply_transform(observation)

    @property
    def state(self) -> DeterminexOracleState:
        return self._state
