# ProgramBench Evidence Graph Integrity Guard

`PROGRAMBENCH_EVIDENCE_GRAPH_INTEGRITY_GUARD_LOCK_001` verifies that the ProgramBench evidence graph has no invalid path to execution or training eligibility.

It blocks training eligibility from skipped records, executable status from metadata-only records, rerun authorization without preflight, fixture policy admission as live approval, cache readiness from scan failure without exception, and model-failure classification for security/provenance skips.
