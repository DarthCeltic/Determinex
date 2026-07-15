# Claude IDE Public Claims Ledger

> Locked under `locks/sentinel/CLAUDE_PUBLIC_CLAIMS_LEDGER_LOCK_001.json`.

Public-facing language for the Claude IDE lane. Every claim
classifies into one of five disjoint states.

## Classifications

| Class | Means |
|---|---|
| `implemented` | Live today; gates in place |
| `implemented_but_gated_or_blocked` | Live but always gated behind explicit checks |
| `planned` | On the roadmap; not yet shipped |
| `research_track` | Under investigation; no shipping commitment |
| `not_claimed` | Not in scope for this lane |

## Live ledger

### Implemented

- **Local model detection / admission** — `REAL_LOCAL_MODEL_ADMISSION_LOCK_001`
- **Local model healthcheck** — precondition for diagnose
- **Diagnose with verifier context** — output never trusted; never applied
- **Quarantined patch plan** — schema/path-validated
- **Temp patch verifier** — isolated temp workspace
- **Human approval source mutation gate** — fixture approvals refused at apply
- **Canonical patch body binding** — sha256-bound; tampered bodies refused
- **Post-apply verifier** — never defaults to pass

### Implemented but gated or blocked

- **Cryptographic local approval binding** — HMAC-SHA256 over canonical payload; asymmetric crypto upgrade pending
- **Rollback snapshot** — taken before any mutation; symlinked workspaces refused
- **Frontend repair panel** — view-model + visual audit locked; live React mount in progress
- **Source mutation** — implemented; ALWAYS gated by approval, verifier, snapshot, body-hash, symlink-refusal

### Planned

- **Release readiness** — install/demo/repo-scrub incomplete
- **Public packaging** — signed installer/demo bundle not yet shipped

### Research track

- **Federated / Forge** — not implemented in Claude IDE lane
- **Mobile console** — not implemented in Claude IDE lane

### Not claimed

- **Training eligibility** — `training_eligible` remains False everywhere in the Claude lane

## Hard rules (test-enforced)

1. `training_eligibility` is NEVER `implemented` (or any classification implying live capability).
2. `release_readiness` and `public_packaging` are NEVER `implemented`.
3. No claim key contains `benchmark`, `programbench`, or `swebench` — benchmark execution belongs to the Codex/ProgramBench lane.
4. `source_mutation` must declare its gates explicitly.

Marketing or website copy that diverges from this ledger must be
updated. The ledger is the source of truth.
