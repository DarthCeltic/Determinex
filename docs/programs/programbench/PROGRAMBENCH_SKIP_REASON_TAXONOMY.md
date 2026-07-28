# ProgramBench Skip Reason Taxonomy

`PROGRAMBENCH_SKIP_REASON_TAXONOMY_LOCK_001` separates infrastructure, security, provenance, and policy blockers from model or benchmark failures.

Required reasons include missing image metadata, missing artifacts, missing provenance, quarantine-only metadata, scan-failed policy requirement, operator policy admission requirement, sandbox requirements missing, execution preflight blocked, stale evidence, and explicit non-failure/non-training classifications.

Doxygen maps to `SCAN_FAILED_POLICY_REQUIRED` and `OPERATOR_POLICY_ADMISSION_REQUIRED`. Missing Batch 001 image rows map to `MISSING_IMAGE_METADATA` and `MISSING_PROVENANCE`.

No skip reason implies training eligibility.
