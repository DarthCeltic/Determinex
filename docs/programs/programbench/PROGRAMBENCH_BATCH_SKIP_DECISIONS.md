# ProgramBench Batch Skip Decisions

`PROGRAMBENCH_BATCH_SKIP_DECISION_LOCK_001` applies the skip taxonomy to all known Batch 001 and Doxygen rows.

Current decisions:

- Doxygen is skipped because operator policy admission is required for a scan-failed official artifact.
- Batch 001 replay candidates with no image metadata are skipped pending exact image metadata and provenance.

Skipped tasks are not model failures, benchmark failures, executable tasks, cache-ready tasks, or training rows.
