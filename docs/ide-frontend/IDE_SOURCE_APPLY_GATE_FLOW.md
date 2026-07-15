# IDE Source Apply Gate Flow

> Locked under `locks/sentinel/IDE_SOURCE_APPLY_GATE_FLOW_LOCK_001.json`.

Pure decision surface. Consumes a signing record + packet + observed
source state. Returns DRY_RUN_READY, FIXTURE_ONLY, or specific block
reason. Never mutates the original repo.
