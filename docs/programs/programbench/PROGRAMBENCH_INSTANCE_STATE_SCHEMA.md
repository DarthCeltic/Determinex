# ProgramBench Instance State Schema

`PROGRAMBENCH_INSTANCE_STATE_SCHEMA_LOCK_001` defines the common state record used by the Codex ProgramBench campaign apparatus.

The schema normalizes per-instance artifact authority, rebuild/remediation authority, scan status, security execution authority, policy admission status, bounded rerun status, score/cache/executable/training flags, skip status, next unblocker, and evidence references.

The Doxygen cleanroom lane is represented as:

- `artifact_authority`: `ARTIFACT_AUTHORITY_PRESENT`
- `security_execution_authority`: `SECURITY_EXECUTION_AUTHORITY_ABSENT_PENDING_OPERATOR_POLICY_ADMISSION`
- `bounded_rerun_status`: `BOUNDED_RERUN_BLOCKED_SECURITY_PREFLIGHT`
- `training_eligible`: `TRAINING_ELIGIBLE_FALSE`

This schema does not authorize Docker, ProgramBench execution, rebuilds, remediation, cache readiness, or training rows.
