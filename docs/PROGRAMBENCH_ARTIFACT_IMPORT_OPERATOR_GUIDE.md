# ProgramBench Artifact Import Operator Guide

This guide is for supplying exact artifact import provenance for the 10 Batch001 targets whose official ProgramBench image names and exact registry manifest digests have already been admitted as metadata only.

This guide is not an import, approval, scan, execution authorization, ProgramBench rerun authorization, cache-readiness decision, or training eligibility decision.

## Current State

- Image names derived: yes
- Exact manifest digests admitted metadata-only: 10
- Artifacts imported: 0
- Scans run: 0
- Execution authorized: false
- Cache ready: false
- Training eligible: false

## Required Operator Evidence

- `instance_id`
- `image_name`
- `exact_manifest_digest`
- `local_artifact_tar_path or artifact_reference`
- `artifact_file_sha256`
- `source_registry_provenance_notes`
- `digest binding between supplied artifact and manifest digest`
- `operator_identity`
- `operator_signature or local signed evidence convention`
- `timestamp`

## Acceptable Forms

- exact digest image tar exported by controlled process
- signed internal cache record
- registry artifact reference with immutable digest and provenance
- local artifact tar with sha256 and source binding

## Rejected Forms

- latest tags
- name-only images
- tag-only pulls
- screenshots
- prose claims without digest/hash binding
- unverified public images
- fixture packets
- artifact with missing sha256
- artifact with mismatched digest
- artifact that authorizes execution directly

## Inbox And Outbox Flow

- Templates live at `assurance/operator_outbox/programbench/batch001_import_scan`.
- Completed packets should be placed in `assurance/operator_inbox/programbench`.
- Run inbox scan before any review.
- Run packet validation/process-inbox before live packet review.
- The next gate is `PROGRAMBENCH_BATCH001_OPERATOR_ARTIFACT_IMPORT_PACKET_REVIEW_LOCK_001`, only if real operator packets exist.

## Commands

- `python scripts/corpus/programbench/programbench_operator_cli.py actions --json`
- `python scripts/corpus/programbench/programbench_operator_cli.py packets --out assurance/operator_outbox/programbench --json`
- `python scripts/corpus/programbench/programbench_operator_cli.py inbox-scan --json`
- `python scripts/corpus/programbench/programbench_operator_cli.py process-inbox --json`
- `python scripts/corpus/programbench/programbench_operator_cli.py review-live-packets --json`

## Hard Warnings

- packet does not authorize Docker run
- packet does not authorize ProgramBench rerun
- packet does not authorize training
- packet does not bypass scan
- packet does not mark executable
- packet does not mark cache_ready unless a later quarantine-cache gate defines that separately

## Batch001 Targets

| instance_id | image | digest | required packet | current status | next unblocker |
| --- | --- | --- | --- | --- | --- |
| `ammarabouzor__tui-journal.2b4540d` | `` | `sha256:645ee0174df42ac0e471997c21d127a7a4c14e83ac505a5474198ed1eedd8295` | `artifact_import_provenance` | `METADATA_ONLY_DIGEST_ADMITTED_IMPORT_REQUIRED` | `SUPPLY_OPERATOR_ARTIFACT_IMPORT_PACKET` |
| `antonmedv__fx.86d0d34` | `` | `sha256:6aaa8f21511709103371edc8299d14bc7ca257032100587459278029b3fe90d7` | `artifact_import_provenance` | `METADATA_ONLY_DIGEST_ADMITTED_IMPORT_REQUIRED` | `SUPPLY_OPERATOR_ARTIFACT_IMPORT_PACKET` |
| `axodotdev__oranda.27d60c7` | `` | `sha256:2d52e7ec23e60ba0984621b4a1df40b068752b76042a1c09f21420b277ca0e64` | `artifact_import_provenance` | `METADATA_ONLY_DIGEST_ADMITTED_IMPORT_REQUIRED` | `SUPPLY_OPERATOR_ARTIFACT_IMPORT_PACKET` |
| `gabotechs__dep-tree.60a95a2` | `` | `sha256:6e36ddd4c11c5ff2d555c37fdce7d024a09ef1f1064c6b986568d36844d0a9ec` | `artifact_import_provenance` | `METADATA_ONLY_DIGEST_ADMITTED_IMPORT_REQUIRED` | `SUPPLY_OPERATOR_ARTIFACT_IMPORT_PACKET` |
| `jarun__nnn.cb2c535` | `` | `sha256:227579686a4b9ceef979830b76a2a81d7c253996d6ebb1879eb6cd90c46d38fa` | `artifact_import_provenance` | `METADATA_ONLY_DIGEST_ADMITTED_IMPORT_REQUIRED` | `SUPPLY_OPERATOR_ARTIFACT_IMPORT_PACKET` |
| `naggie__dstask.ff57396` | `` | `sha256:ef527e8c3f1bf86f80ade6a34c2a8024fb1b36b110ec76e3e074861ace8007ba` | `artifact_import_provenance` | `METADATA_ONLY_DIGEST_ADMITTED_IMPORT_REQUIRED` | `SUPPLY_OPERATOR_ARTIFACT_IMPORT_PACKET` |
| `nikolassv__bartib.6b9b5ce` | `` | `sha256:8499ab75c1130353c8c777c7c2134ba1e02f7d2e43da2c92f93955be645c3827` | `artifact_import_provenance` | `METADATA_ONLY_DIGEST_ADMITTED_IMPORT_REQUIRED` | `SUPPLY_OPERATOR_ARTIFACT_IMPORT_PACKET` |
| `rcoh__angle-grinder.9c2fc88` | `` | `sha256:7319afca71937ffb9ff2c0af73dd876c54362fc51fd68be294ee03a9b1cefe0b` | `artifact_import_provenance` | `METADATA_ONLY_DIGEST_ADMITTED_IMPORT_REQUIRED` | `SUPPLY_OPERATOR_ARTIFACT_IMPORT_PACKET` |
| `riquito__tuc.16fb471` | `` | `sha256:b7556a4b8118ec2ab3f193cb079f5faeb6a74e13d450568925a205b4fa8bf7da` | `artifact_import_provenance` | `METADATA_ONLY_DIGEST_ADMITTED_IMPORT_REQUIRED` | `SUPPLY_OPERATOR_ARTIFACT_IMPORT_PACKET` |
| `sibprogrammer__xq.b89f681` | `` | `sha256:420168db4a989024b77eadc604bfabf55389b542765a4cc2761f70de9a8c3db8` | `artifact_import_provenance` | `METADATA_ONLY_DIGEST_ADMITTED_IMPORT_REQUIRED` | `SUPPLY_OPERATOR_ARTIFACT_IMPORT_PACKET` |

## Doxygen

Doxygen is intentionally not included in this artifact import guide. It remains blocked pending real operator security policy admission, not Batch001 artifact import provenance.
