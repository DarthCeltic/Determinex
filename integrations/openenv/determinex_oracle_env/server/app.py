"""
FastAPI application for the Determinex Oracle Environment.

Exposes DeterminexOracleEnv over HTTP and WebSocket, compatible with OpenEnv's
EnvClient. See envs/coding_env/server/app.py in meta-pytorch/OpenEnv for the
reference pattern this mirrors.

Usage:
    uvicorn determinex_oracle_env.server.app:app --host 0.0.0.0 --port 8000

Configuration (env vars, since task_dir/language are per-deployment, not
per-request -- one running server instance serves one task family):
    DETERMINEX_ORACLE_ENV_TASK_DIR   path to the reference project skeleton
    DETERMINEX_ORACLE_ENV_LANGUAGE   oracle key, e.g. "rust" / "go" / "python"
"""

import os

from openenv.core.env_server import create_app

from ..models import DeterminexOracleAction, DeterminexOracleObservation
from .environment import DeterminexOracleEnv


def _make_env() -> DeterminexOracleEnv:
    return DeterminexOracleEnv(
        task_dir=os.environ.get("DETERMINEX_ORACLE_ENV_TASK_DIR"),
        language=os.environ.get("DETERMINEX_ORACLE_ENV_LANGUAGE"),
    )


app = create_app(
    _make_env,
    DeterminexOracleAction,
    DeterminexOracleObservation,
    env_name="determinex_oracle_env",
)


def main():
    import uvicorn

    port = int(os.environ.get("SBX_SERVICE_PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
