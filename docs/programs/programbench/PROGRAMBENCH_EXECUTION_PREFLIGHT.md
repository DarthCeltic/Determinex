# ProgramBench Execution Preflight

`PROGRAMBENCH_GENERIC_EXECUTION_PREFLIGHT_LOCK_001` checks whether a ProgramBench instance has enough evidence for bounded official-artifact execution.

The generic checks require instance state, artifact authority, exact image and digest, scan evidence, sandbox requirements, accepted policy admission for scan-failed artifacts, bounded rerun scope, max-attempt enforcement, clean evidence, and no pre-run training eligibility.

The live Doxygen result is `GENERIC_EXECUTION_PREFLIGHT_BLOCKED_POLICY_ADMISSION_REQUIRED`.

The preflight is non-executing. It does not run Docker, pull images, run ProgramBench, or create training rows.
