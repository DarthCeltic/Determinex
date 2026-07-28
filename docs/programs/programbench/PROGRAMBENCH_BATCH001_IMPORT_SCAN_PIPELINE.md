# ProgramBench Batch001 Import/Scan Pipeline

This campaign continues from `PROGRAMBENCH_BATCH001_LOOKUP_CAMPAIGN_FINAL_STATE_LOCK_001`.

The ten Batch001 targets have exact DockerHub manifest digests admitted as metadata-only evidence. This campaign moves them to the next safe boundary: artifact import request, import preflight, operator import packet templates, import evidence gate, scan queue, and scan policy precheck.

## Result

- metadata-admitted targets: 10
- import request packets written: 10
- local import preflight ready: 0
- local import preflight blocked: 10
- operator artifact import templates written: 10
- scan queue entries: 10
- scans performed: 0
- execution performed: false
- training rows written: false

The live preflight is blocked because no already-authorized local safe import method is present. The next unblocker is operator-supplied exact artifact import provenance.

## Boundaries

This campaign does not import artifacts, run Docker, run ProgramBench, rebuild, remediate, grant policy exceptions, or create training rows.

Any future imported artifact remains quarantine-only until exact digest/file-hash verification and scan evidence are admitted. A scan pass does not imply execution; a scan failure routes to security decision and operator policy admission.
