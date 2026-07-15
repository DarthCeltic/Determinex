# Post-Apply Verifier

> Locked under `locks/sentinel/POST_APPLY_VERIFIER_LOCK_001.json`.

`scripts/repair/post_apply_verifier.py` runs a hardened verifier
callable on the user's workspace after a real source-apply has
completed.

Outcomes:

| Decision | rollback_recommended | training_eligible |
|---|---|---|
| `POST_APPLY_VERIFIER_PASSED` | False | False |
| `POST_APPLY_VERIFIER_FAILED` | True | False |
| `POST_APPLY_VERIFIER_BLOCKED_NO_APPLY` | False | False |

Notes:

- Passing the verifier does NOT auto-create a training row.
  Training eligibility is a separately-gated rung.
- Failing the verifier sets `rollback_recommended=True`. Rung 10
  executes the rollback.
- The verifier callable is pluggable; default is the locked
  `stub_verifier_pass` from SafePatchWorkspace's surface.
