# ProgramBench Batch001 Metadata Campaign

This campaign continues from `PROGRAMBENCH_BATCH001_UNBLOCK_PRIORITY_LOCK_001`. It works only on Batch001 targets ranked `EASY_METADATA_ONLY`; Doxygen remains blocked pending real operator security policy admission.

## Result

The campaign derived exact expected ProgramBench `task_cleanroom` image names for ten metadata-only targets using the established naming rule:

```text
owner__repo.sha -> programbench/owner_1776_repo.sha:task_cleanroom
```

The repo has an existing DockerHub manifest provenance converter for already-supplied exact manifest metadata, but no implemented live metadata retrieval client. Because of that, `PROGRAMBENCH_BATCH001_SAFE_MANIFEST_LOOKUP_LOCK_001` honestly records `SAFE_MANIFEST_LOOKUP_NOT_SUPPORTED`.

No manifest digests were found or admitted. All ten targets remain blocked on exact image metadata submission. Doxygen remains blocked on operator security policy admission.

## Safety

The campaign did not:

- run Docker
- pull images
- run ProgramBench
- rebuild images
- remediate images
- grant a policy exception
- create fake live packets
- create training rows

Metadata admission, if it happens later, remains metadata-only. It is not execution authority, cache readiness, or training eligibility.
