# ProgramBench Operator Action Queue

`PROGRAMBENCH_OPERATOR_ACTION_QUEUE_LOCK_001` converts batch state and skip decisions into explicit operator actions.

Action types include image metadata submission, operator provenance submission, security policy admission, pinned base digest, original build recipe, scanner installation, scan policy review, bounded rerun authorization, and metadata-only no-action entries.

Current Doxygen action: `SUPPLY_SECURITY_POLICY_ADMISSION`.

Current missing Batch 001 action: `SUPPLY_IMAGE_METADATA`.

Actions describe required evidence only. They do not authorize execution.
