# Proof Before Mutation — Demo Script

> Locked under `locks/sentinel/CLAUDE_PROOF_BEFORE_MUTATION_DEMO_SCRIPT_LOCK_001.json`.

The simplest undeniable local demo path. Runs against a fixture
repository under `tests/fixtures/proof_before_mutation_demo_repo`.
**No network, no Docker, no ProgramBench, no training rows.**

## Happy path — 11 steps

1. **Open fixture repo**
2. **Detect issue**
3. **Local model diagnoses** (locally admitted; output untrusted)
4. **Determinex quarantines patch** (`REAL_PATCH_PLAN_QUARANTINE_LOCK_001`)
5. **Temp verifier runs** (isolated temp workspace)
6. **User approval required**
7. **Patch body hash is bound** (canonical sha256 + HMAC)
8. **Source mutation applies only after approval**
9. **Post-apply verifier runs** (never defaults to pass)
10. **Signed evidence appears**
11. **Training remains blocked unless separately eligible**

## Blocked path — 3 refusal scenarios

1. **Missing approval** → `SOURCE_MUTATION_BLOCKED_NO_APPROVAL`
2. **Changed patch body** → `SOURCE_MUTATION_BLOCKED_BODY_HASH_MISMATCH` (CLAUDE-AUTH-001 attack scenario blocked)
3. **Missing verifier** → `SOURCE_MUTATION_BLOCKED_VERIFIER_NOT_PASSED`

Every refusal writes an evidence record.

## Constraints (test-enforced)

| Constraint | Refusal if violated |
|---|---|
| Network model required | `DEMO_BLOCKED_NETWORK_REQUIRED` |
| Docker required | `DEMO_BLOCKED_NETWORK_REQUIRED` |
| ProgramBench required | `DEMO_BLOCKED_NETWORK_REQUIRED` |
| Training rows written | `DEMO_BLOCKED_NETWORK_REQUIRED` |
| Real user repo referenced | `DEMO_BLOCKED_PATH_INCLUDED` |
| Step numbers non-contiguous | `DEMO_BLOCKED_AUTHORITY_AMBIGUITY` |
| Blocked-step not flagged | `DEMO_BLOCKED_MISSING_BLOCKED_PATH` |
| "Proof Before Mutation" phrase missing | `DEMO_BLOCKED_MISSING_PHRASE` |

## What this lock does NOT yet do

It declares the demo. A later rung wires a CI-executable runner
that exercises all 11 + 3 steps against the fixture repo.
