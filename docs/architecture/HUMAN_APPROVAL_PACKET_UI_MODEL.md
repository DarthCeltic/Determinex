# Human Approval Packet UI Model

> Locked under `locks/sentinel/HUMAN_APPROVAL_PACKET_UI_MODEL_LOCK_001.json`.

IDE-displayable approval packet for source mutation. Carries:
trace_id, workspace_identity, diff_hash, diff_summary, files_changed,
verifier_result, model_route_ref, patch_plan_ref, temp_patch_ref,
risk_summary, approval_required, approval_status, operator_identity,
operator_signature, timestamp, stale_after.

`evaluate_submitted()` returns one of the closed-set status tokens.
Never applies source mutation.
