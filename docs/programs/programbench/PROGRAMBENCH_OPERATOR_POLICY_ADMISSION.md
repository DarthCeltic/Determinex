# ProgramBench Operator Policy Admission

`PROGRAMBENCH_GENERIC_OPERATOR_POLICY_ADMISSION_LOCK_001` generalizes policy admission for ProgramBench instances.

A live admission must bind the exact instance id, image name, digest, scan evidence, sandbox requirements, policy exception request, maximum attempts, allowed scope, timestamp, and operator signature or accepted local signed convention.

Fixtures may exercise accepted and rejected paths in tests, but fixture admissions are not live approvals. Without a real operator admission file, Doxygen remains `GENERIC_POLICY_ADMISSION_REQUIRED`.

This gate does not grant a policy exception and does not authorize ProgramBench execution by itself.
