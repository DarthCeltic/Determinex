# Real Approval Diff/Body Content Binding

> Locked under `locks/sentinel/REAL_APPROVAL_DIFF_BODY_CONTENT_BINDING_LOCK_001.json`.

Remediates **CLAUDE-AUTH-001**: previously the approval bound only a
hash of the operator-rendered diff string. A caller could pass that
diff alongside tampered `plan_entries.new_content` and the apply gate
would write the tampered content.

The fix:

- `scripts/repair/patch_body_hash.compute(plan_entries)` produces a
  canonical sha256 over a sorted, normalized list of
  `(operation, path, sha256(new_content), len(new_content))` rows
- `RealHumanApprovalAdmissionRecord.canonical_patch_body_hash` is the
  new field admission binds at approval time
- `source_mutation_apply_after_approval` recomputes from
  `plan_entries` at apply time and refuses on mismatch:
  - `SOURCE_MUTATION_BLOCKED_MISSING_BODY_HASH` — approval has no
    binding, or the supplied entries cannot produce a valid hash
  - `SOURCE_MUTATION_BLOCKED_BODY_HASH_MISMATCH` — supplied entries
    produce a hash that does not match the approved one

The attack scenario `test_claude_auth_001_attack_scenario_blocked` is
the regression: clean diff narrative + tampered body → blocked.
