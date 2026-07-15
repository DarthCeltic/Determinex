# Local Model Config Wizard

> Locked under `locks/sentinel/LOCAL_MODEL_CONFIG_WIZARD_LOCK_001.json`.

Safe wizard for writing a local-model config file. Defaults:
`enabled=False`, `dry_run_default=True`. Network providers, unpinned
ids, stale ids, unknown providers, and unsupported task classes are
all blocked.

The wizard writes JSON files to a caller-supplied `config_root`. It
never invokes a model.
