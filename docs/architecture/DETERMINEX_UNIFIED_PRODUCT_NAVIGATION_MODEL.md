# Determinex — Unified Product Navigation Model

> Locked under
> `locks/sentinel/DETERMINEX_UNIFIED_PRODUCT_NAVIGATION_MODEL_LOCK_001.json`.

Determinex is not only a new-project tool and not only a repair tool.
It serves all coding setups and all coder levels through five
distinct product surfaces with one shared proof / authority /
evidence spine.

## Five surfaces

| Surface | Purpose |
|---|---|
| **Idea Lab** | Turn a beginner's idea into a runnable, verifier-checked local app |
| **Repo Clinic** | Diagnose, repair, refactor, update an existing codebase under approval gates |
| **Maintenance Bay** | Dependency updates, security fixes, migrations, docs/tests/lint cleanup |
| **Learning Studio** | Explain, teach, compare, walk through code at the operator's chosen level |
| **Proof / Operator Center** | Read-only view of evidence, gates, queues, training status, claim safety |

## Shared authority vocabulary

The 8 disjoint classes from
`CLAUDE_AUTH_005_READY_AUTHORIZED_LANGUAGE_LOCK_001`:

```
capability_available
evidence_present
request_pending
admission_present
approval_present
execution_authorized
source_mutation_authorized
training_eligible
```

## Hard rules (test-enforced)

1. Every required surface must be present.
2. Every surface must declare at least one **visible blocked state**.
3. No surface's `source_mutation_boundary` may say "authorized by default", "open by default", "auto-apply", or "no approval required".
4. **Learning Studio** boundary must say "non-mutating" or "routes to repo_clinic/idea_lab gates".
5. **Proof Operator Center** boundary must say "read-only" or "non-authorizing".
6. No surface's `training_eligibility_boundary` may open training; every surface must explicitly state training stays False / does not open.

## What the lock does NOT do

It does not render the React tree. The backend view-model is the
source of truth; a later wiring rung mounts the frontend. Surface
keys are stable across the campaign.
