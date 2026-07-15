# Frontend Approval Packet Round-Trip

> Locked under `locks/sentinel/FRONTEND_APPROVAL_PACKET_ROUNDTRIP_LOCK_001.json`.

Round-trip through the locked `HumanApprovalSigningFlow` and
`SourceApplyGateFlow`. Backend builds the packet → operator approve or
reject → source apply gate check. NEVER mutates source.

Stages exercised:

| Stage | Signing decision | Apply-gate decision |
|---|---|---|
| approve (fixture) | `IDE_APPROVAL_FIXTURE_ONLY` | `IDE_SOURCE_APPLY_DRY_RUN_READY` |
| reject | `IDE_APPROVAL_REJECTED` | `IDE_SOURCE_APPLY_BLOCKED_NOT_SIGNED` |
| stale packet | `IDE_APPROVAL_BLOCKED_STALE_PACKET` | — |
| diff mismatch | `IDE_APPROVAL_BLOCKED_DIFF_MISMATCH` | — |
| verifier failed | `IDE_APPROVAL_BLOCKED_VERIFIER_NOT_PASSED` | — |

Even the approved-fixture stage keeps
`source_mutation_authorized=False`. The "DRY_RUN_READY" decision means
the gate would *let* the apply proceed if a non-fixture signature
arrived — but the fixture signature itself is not real authorization.
