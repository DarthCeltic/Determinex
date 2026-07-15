"""
integrations/openenv/determinex_oracle_env/models.py
----------------------------------------------------
Action/Observation/State types for the Determinex Oracle environment.

The reward this environment emits is never an LLM judge. It is the pass/fail
verdict of a real compiler or test runner (rustc / go build / tsc / pytest /
cargo test / ...), routed through scripts/determinex_oracle.py -- the same
ground-truth surface Determinex's own training loop uses. See README.md for why
that distinction is the entire point of this environment.
"""

from __future__ import annotations

from openenv.core.env_server.interfaces import Action, Observation, State


class DeterminexOracleAction(Action):
    """One submission attempt against the current task workspace.

    `files` are written (created or overwritten) relative to the episode's
    ephemeral workspace before the oracle runs. `remove` deletes paths first
    (e.g. to clear a stale build artifact) -- both are optional so a minimal
    action can just submit one file.
    """

    files: dict[str, str] = {}
    remove: list[str] = []


class DeterminexOracleObservation(Observation):
    """Deterministic compiler/test verdict for the last submitted files.

    `passed` is the whole-suite ground truth (test == total, matching
    Determinex's own ProgramBench lock definition -- see CLAUDE.md). `failures`
    is a compact, human/agent-readable summary, not the full raw log; `raw_tail`
    carries the last slice of real compiler/test output for diagnosis.
    """

    passed: bool = False
    oracle: str = ""
    total: int = 0
    n_passed: int = 0
    failures: list[str] = []
    raw_tail: str = ""
    error: str = ""


class DeterminexOracleState(State):
    """Per-episode workspace + language pin. episode_id/step_count come from State."""

    language: str = ""
    workdir: str = ""
    attempts: int = 0
