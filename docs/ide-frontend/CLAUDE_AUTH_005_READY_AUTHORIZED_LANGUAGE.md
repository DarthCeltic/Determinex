# Ready does NOT mean Authorized

> Locked under
> `locks/sentinel/CLAUDE_AUTH_005_READY_AUTHORIZED_LANGUAGE_LOCK_001.json`.

Remediates the deferred **CLAUDE-AUTH-005** finding: backend and
frontend status surfaces use a wide vocabulary, and a reader might
equate `*_READY` with `AUTHORIZED`.

## Eight disjoint classes

Every status token in the Claude IDE lane classifies into one of:

| Class | Means | Sample tokens |
|---|---|---|
| `capability_available` | Code/UI is wired up — nothing has been granted | `IDE_BACKEND_COMMAND_SURFACE_READY`, `*_PANEL_READY` |
| `evidence_present` | An artifact (verifier run, snapshot) exists | `ROLLBACK_SNAPSHOT_WRITTEN`, `POST_APPLY_VERIFIER_PASSED` |
| `request_pending` | Waiting on operator / external | `LIVE_MODEL_NOT_ADMITTED` |
| `admission_present` | Gate has admitted (not yet approved) | `LIVE_MODEL_ADMITTED`, `REAL_LOCAL_MODEL_ADMITTED` |
| `approval_present` | Operator has approved (still must pass apply gate) | `REAL_HUMAN_APPROVAL_ACCEPTED`, `*_FIXTURE` |
| `execution_authorized` | Execution can proceed (currently empty) | — |
| `source_mutation_authorized` | Source mutation has happened | `SOURCE_MUTATION_APPLIED_AFTER_APPROVAL` (only) |
| `training_eligible` | Training corpus can ingest (currently empty) | — |

## Hard invariants

1. **No `*_READY` token classifies into a class that implies authorization.**
2. **No `*_FIXTURE` approval token classifies as `source_mutation_authorized`.**
3. **No frontend surface token classifies into an authorization-implying class.**
4. **No existing token classifies as `training_eligible`** (negative default).
5. **Exactly one token classifies as `source_mutation_authorized`**:
   `SOURCE_MUTATION_APPLIED_AFTER_APPROVAL`, emitted only by the apply
   gate after every check (approval, verifier, snapshot, body hash,
   symlink refusal).

## Classifier

`scripts/repair/ready_authorized_vocabulary.py::classify(token)`
returns a `TokenClassification` or `None`. Unknown tokens return
`None` by design — auto-classification would defeat the lock; new
tokens must be added explicitly with a rationale.

## What this lock does NOT change

It does not rewrite the existing token surface. The classifier
sits beside the existing records and is what operators and
downstream agents should consult when deciding *what is actually
authorized right now*. Token renames are a future cosmetic change;
the load-bearing safety lives in the classifier and its tests.
