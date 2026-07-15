"""
DeterminexOracleEnv client
------------------------
Client-side wrapper for training/eval loops. Mirrors envs/coding_env/client.py
in meta-pytorch/OpenEnv.
"""

from __future__ import annotations

from openenv.core.client_types import StepResult
from openenv.core.env_client import EnvClient

from .models import DeterminexOracleAction, DeterminexOracleObservation, DeterminexOracleState


class DeterminexOracleEnvClient(EnvClient[DeterminexOracleAction, DeterminexOracleObservation, DeterminexOracleState]):
    def _step_payload(self, action: DeterminexOracleAction) -> dict:
        return {"files": action.files, "remove": action.remove}

    def _parse_result(self, payload: dict) -> StepResult[DeterminexOracleObservation]:
        obs = DeterminexOracleObservation(**payload["observation"])
        return StepResult(
            observation=obs,
            reward=payload.get("reward"),
            done=bool(payload.get("done", False)),
        )

    def _parse_state(self, payload: dict) -> DeterminexOracleState:
        return DeterminexOracleState(
            episode_id=payload.get("episode_id"),
            step_count=payload.get("step_count", 0),
            language=payload.get("language", ""),
            workdir=payload.get("workdir", ""),
            attempts=payload.get("attempts", 0),
        )
