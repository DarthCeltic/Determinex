# Claude Authority Leak Remediation — Final State

> Locked under
> `locks/sentinel/CLAUDE_AUTHORITY_LEAK_REMEDIATION_FINAL_STATE_LOCK_001.json`.

Rung 9 (finale) of the Claude Opus 4.8 merge-audit authority-leak
remediation campaign.

The finale evaluator at
`scripts/repair/claude_authority_leak_remediation_final_state.evaluate`
reads the eight prior rungs' lock manifests on disk and asserts:

1. Each rung's lock manifest exists, parses, declares the right
   `lock_id`, and has `scope_discipline` declaring
   `source_mutation_authorized: false` and a closed
   `training_eligible` (or `training_eligibility_opened`) key.
2. The evidence artifact path inside each manifest exists on
   disk.
3. The campaign-aggregate invariants
   (`source_mutation_authorized`, `training_eligible`) remain
   `false`.

If all conditions hold, the finale record's
`safe_for_cross_lane_boundary` is `True` and `decision` is
`CLAUDE_AUTHORITY_LEAK_REMEDIATION_FINAL_STATE_PASSED`.

## Eight remediation dimensions

| Dimension | Finding | Lock |
|---|---|---|
| diff_body_binding | CLAUDE-AUTH-001 | `REAL_APPROVAL_DIFF_BODY_CONTENT_BINDING_LOCK_001` |
| fixture_refusal | CLAUDE-AUTH-002 | `APPLY_GATE_FIXTURE_REFUSAL_LOCK_001` |
| post_apply_verifier_default_pass | CLAUDE-AUTH-003 | `POST_APPLY_VERIFIER_NO_DEFAULT_PASS_LOCK_001` |
| model_admission_bypass | CLAUDE-AUTH-004 | `MODEL_ADMISSION_NO_BYPASS_LOCK_001` |
| tauri_command_alignment | CLAUDE-AUTH-006 | `TAURI_COMMAND_VERB_ALIGNMENT_LOCK_001` |
| diagnose_prompt_opacity | CLAUDE-AUTH-007 | `DIAGNOSE_PROMPT_OPACITY_ENFORCEMENT_LOCK_001` |
| approval_signature_binding | CLAUDE-AUTH-008 | `APPROVAL_SIGNATURE_CRYPTOGRAPHIC_BINDING_LOCK_001` |
| rollback_symlink_semantics | CLAUDE-AUTH-009 | `ROLLBACK_SYMLINK_SEMANTICS_LOCK_001` |

## Deferred to a future campaign

| Finding | Reason |
|---|---|
| CLAUDE-AUTH-005 | Cross-lane status surface labelling; surface-only |
| CLAUDE-AUTH-010 | Evidence index in-place mutability; operational |
| CLAUDE-AUTH-011 | Local model config save path inside repo |
| CLAUDE-AUTH-012 | Frontend invoke client late refusal |
| CLAUDE-AUTH-013 | No minimum stale_after freshness floor |
| CLAUDE-AUTH-014 | No device/operator identity binding |
| CLAUDE-AUTH-015 | No final write-confirmation step |
| CLAUDE-AUTH-016 | No replay-protection / nonce |
| CLAUDE-AUTH-017 | Cross-lane global_operator_action_queue |

## What this lock does NOT prove

The finale does NOT re-run the eight prior gates at runtime. It
asserts the locks are *in place* and declare the right safety
invariants. Runtime enforcement is each rung's per-test
responsibility. The finale is the campaign-level umbrella claim
operators read before extending the cross-lane boundary.
