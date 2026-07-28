# Source Mutation Apply Dry-Run

> Locked under `locks/sentinel/SOURCE_MUTATION_APPLY_DRY_RUN_LOCK_001.json`.

Computes what WOULD be applied if a human-approved patch were applied
to original source — without writing. Detects missing approval, stale
source, diff mismatch, and verifier-not-passed.

Source remains unchanged on every path.
