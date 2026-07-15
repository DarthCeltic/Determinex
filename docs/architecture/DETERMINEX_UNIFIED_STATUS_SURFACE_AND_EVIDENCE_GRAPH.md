# Determinex Unified Status Surface And Evidence Graph

`DETERMINEX_UNIFIED_STATUS_SURFACE_AND_EVIDENCE_GRAPH_LOCK_001` is the first read-only cross-lane integration surface.

It consumes Claude/IDE evidence, Codex/ProgramBench evidence, and proof-control evidence without mutating any lane. It does not authorize source mutation, ProgramBench execution, artifact import, scanning, training eligibility, operator approval, or release workflow.

## Current Unified Truth

| Dimension | Status |
| --- | --- |
| unified status | READY |
| Claude lane | READY_WITH_MUTATION_AND_TRAINING_BLOCKED |
| Codex lane | READY_WITH_OPERATOR_IMPORT_AND_SECURITY_BLOCKERS |
| proof control | READY_NON_AUTHORIZING |
| source mutation authorized | false |
| ProgramBench execution authorized | false |
| artifact import authorized | false |
| training eligible | false |
| evidence health | HEALTHY |

## Consumed Evidence

The status surface reads these records:

- `assurance/evidence/determinex_ide_tauri_integrated_final_state/run_20260528.json`
- `assurance/evidence/claude_lane_live_model_ready_final_state/run_20260527.json`
- `assurance/evidence/real_local_model_admission/run_20260528.json`
- `assurance/evidence/real_human_approval_admission/run_20260528.json`
- `assurance/evidence/source_mutation_apply_dry_run/run_20260527.json`
- `assurance/evidence/programbench_batch001_import_scan_campaign_final_state/programbench_batch001_import_scan_campaign_final_state_run_20260528.BATCH001_IMPORT_SCAN_CAMPAIGN_FINAL_STATE_WRITTEN.json`
- `assurance/evidence/programbench_batch001_lookup_campaign_final_state/programbench_batch001_lookup_campaign_final_state_run_20260528.BATCH001_LOOKUP_CAMPAIGN_FINAL_STATE_WRITTEN.json`
- `assurance/evidence/programbench_batch001_artifact_import_requests/programbench_batch001_artifact_import_request_packet_run_20260528.ARTIFACT_IMPORT_REQUEST_PACKET_WRITTEN.json`
- `assurance/evidence/programbench_batch001_scan_queue/programbench_batch001_scan_queue_run_20260528.BATCH001_SCAN_QUEUE_WRITTEN.json`
- `assurance/evidence/programbench_doxygen_lane_final_state/doxygen__doxygen.966d98e.DOXYGEN_LANE_FINAL_STATE_WRITTEN.json`
- `assurance/evidence/proof_control_plane_final_state/run_20260528.PROOF_CONTROL_PLANE_FINAL_STATE_WRITTEN.json`
- `assurance/evidence/proof_gap_packets/run_20260528.PROOF_GAP_PACKET_WRITTEN.json`
- `assurance/evidence/evidence_index.json`

## Graph Integrity

The unified graph encodes explicit denials:

- Metadata-only registry digests do not grant execution.
- Model output does not grant source mutation.
- Human approval alone does not grant source mutation without verifier and apply gates.
- Blocked or skipped ProgramBench work does not become training data.
- Operator packet templates do not become approvals.
- Scan queues do not grant execution without scan results and a policy decision.
- Proof gap packets do not grant authority.
- Frontend UI state does not mutate backend source without the approval gate.

## Next Unblockers

- `REAL_HUMAN_APPROVAL_FOR_SOURCE_MUTATION`
- `REAL_LOCAL_MODEL_AVAILABLE_IF_NOT_CONFIGURED`
- `OPERATOR_SECURITY_POLICY_ADMISSION_FOR_DOXYGEN`
- `OPERATOR_ARTIFACT_IMPORT_PACKETS_FOR_BATCH001`
- `UNIFIED_GLOBAL_OPERATOR_ACTION_QUEUE`
- `GLOBAL_TRAINING_ELIGIBILITY_GUARD`

## Reproduction

```powershell
.\.venv\Scripts\python.exe scripts\status\unified_status_surface.py --json
.\.venv\Scripts\python.exe -m pytest tests\status\test_determinex_unified_status_surface_and_evidence_graph_lock.py -q
```
