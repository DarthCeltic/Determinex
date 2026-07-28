# LUNARIAN NODE v0 — Fleet Signal Aggregation Specification

> **Status:** OWNER-RESOLVED v0.2 — paper design only. Build is post-announce.
> Disclosure content is pre-filing provisional written-description material.
> **Owner:** Ryan Gurganious, Lunarian Data Systems. **Drafted:** 2026-06-11.
> **Provenance key:** `[PRIOR]` = consolidates existing Determinex design work.
> `[NEW]` = introduced in this draft, needs Ryan's verdict before claim triage.
>
> This document is provisional patent written-description material. It is NOT a
> product specification and NOT a build commitment. All `[NEW]` mechanisms are
> candidate claims for the provisional filing; `[PRIOR]` mechanisms extend
> existing Determinex claims to the fleet context. See §9 for the claim candidate
> list and `docs/patent/claim_charts/` for triage.
>
> Patent-relevant: `docs/patent/claim_charts/claims_likely_novel.md` NOVEL-10–13;
> `docs/patent/claim_charts/claims_needing_narrowing.md` NARROW-04;
> `docs/patent/MORPH_REGISTER.md` M-10.

---

## 1. Purpose and one-sentence answers

The Node is the Lunarian-side endpoint where users who opt in submit
compiler-verified, Cloak-obfuscated training signal, and from which improved
model weights flow back to the fleet.

**The journalist answer ("what leaves my machine?"):**
Nothing, by default. If you opt in: Cloaked training pairs (identifiers
replaced in x_NNNN space, semantic glossary NEVER transmitted), the compiler
verdict metadata, and a coarse environment fingerprint. Never raw source,
never identifiers, never the glossary that could reverse the Cloak, never
file paths, never anything outside the pair itself. `[PRIOR — Cloak doctrine]`

**The enterprise answer:** your deployment is a sealed cartridge; signal
stays inside your boundary unless your contract says otherwise, and what
crosses is the same Cloaked-pair format, contractually scoped. `[PRIOR —
corpus cartridge model]`

**The skeptic answer ("why should Lunarian trust submissions?"):** it
doesn't. Every inbound pair is re-verified by replay before it can touch any
corpus. A stated verdict is never enough — Section 5 doctrine applied to
strangers. `[NEW — replay-verification ingestion gate]`

---

## 2. Data flow (end to end)

```
USER MACHINE                      LUNARIAN NODE                    FLEET
-----------                       -------------                    -----
ForgeDaemon harvests        →  (1) Intake API (authenticated,
failure→fix pair                  tier-tagged, rate-limited)
        ↓                              ↓
Local eligibility gate         (2) Provenance Guard
(Section 12, existing)             schema + signature + dedupe
        ↓                              ↓
Project Cloak applied          (3) REPLAY VERIFICATION
to the pair itself                 re-compile + re-run in sealed
(corpus-grade cloak)               container; verdict recomputed
        ↓                              ↓
Consent check (opt-in          (4) Eligibility Gate (node-side,
flag, tier policy)                 mirrors local gate + corpus
        ↓                          quality rules)
Submit (TLS, signed                    ↓
client manifest)               (5) DP Aggregation layer
                                   (differential privacy noise /
                                   k-anonymity thresholds before
                                   any pair enters a shared
                                   corpus) [PRIOR]
                                       ↓
                               (6) Cartridge Router
                                   community corpus | school
                                   cartridge | enterprise
                                   cartridge (sealed) [PRIOR]
                                       ↓
                               (7) Training runs (ForgeDaemon-
                                   class, node-scale)
                                       ↓
                               (8) Signed OTA weight deltas   →   Ollama
                                   published per tier              hot-swap
                                                                   [PRIOR]
```

---

## 3. Submission schema (v0)

One submission = one verified pair + envelope. JSON, versioned.

```json
{
  "schema_version": "0.1",
  "client": {
    "determinex_version": "...",
    "tier": "individual | school | enterprise",
    "client_signature": "ed25519 over payload",
    "opt_in_receipt": "hash of the consent record version accepted"
  },
  "environment": {
    "os_family": "windows | linux | mac",
    "gpu_class": "<=6GB | <=12GB | <=24GB | cpu",
    "toolchain": ["rustc 1.8x", "go 1.2x"]
  },
  "pair": {
    "language": "...",
    "failure_class": "scaffold | recipe-miss | algorithmic | environmental",
    "before": "<Cloaked code, x_NNNN space>",
    "after":  "<Cloaked code, x_NNNN space>",
    "test_ref": { "harness_id": "<public harness identifier>", "version_hash": "<pinned harness commit/version>" },
    "test_surface": "<Cloaked test or harness excerpt — fallback when test_ref absent>",
    "verdict": { "passed": "N", "total": "N", "exit_codes": ["..."] }
  },
  "provenance": {
    "local_replay_count": "N",
    "cloak_audit": "zero-leak attestation hash",
    "dedupe_key": "content-derived hash (post-cloak)"
  }
}
```

**Test surface (dual-mode):** `test_ref` (harness_id + version_hash) is the PREFERRED form
when a public harness exists (e.g., ProgramBench, established CI suites). The node replays
against its own pinned mirror of the referenced harness at the specified version —
submitted `test_surface` content is ignored for execution, retained for audit only.
`test_surface` (inline, Cloaked) is the fallback for bespoke or enterprise pairs with no
public harness equivalent. `[NEW — dual-mode schema, owner verdict 2026-06-11]`

**Explicitly NEVER in schema:** raw identifiers, semantic glossary, file paths,
repo names, usernames, machine names, timestamps finer than day, full hardware
fingerprints. `[PRIOR — Cloak zero-leak doctrine extended to envelope metadata;
NEW — the coarse-bucket environment rule]`

---

## 4. Consent and tiers

**Individual (free forever):** opt-in is OFF by default, loudly visible,
revocable. Revocation = no further submissions + deletion of attributable
envelopes (pairs already DP-aggregated into a shared corpus are
non-attributable by construction — state this honestly in the consent
text rather than promising impossible retroactive extraction). `[PRIOR —
"loudly, verifiably opt-in from day one"]`

**School cartridge:** enterprise-grade deployment donated; signal rights
per written agreement with the district; student-generated signal gets a
stricter eligibility gate (age/PII scrubbing layered ON TOP of Cloak) and
its own cartridge — **SEALED BY DEFAULT.** Sealed school pairs are never
mixed into community corpus absent a formal gated promotion decision. Any
promotion requires ALL of the following to be satisfied and logged:
(1) COPPA/FERPA compliance review, (2) district agreement amendment
authorizing the specific data use, (3) minor-specific scrub layer
independently audited, (4) differential privacy aggregation applied,
(5) signed sign-off recorded in the public transparency ledger. No
promotion is automatic and no promotion occurs by administrative convenience
alone. *Public-facing statement: sealed; any future sharing only under a
published consent and compliance framework.* `[PRIOR — Catawba model; NEW —
sealed-by-default + gated promotion pathway, owner verdict 2026-06-11]`

**Enterprise cartridge:** sealed by default; signal stays inside the
boundary; any cross-boundary contribution is contract-scoped, Cloaked,
and replay-verified like everything else. `[PRIOR]`

**Data ownership posture:** the user/org owns their pairs; Lunarian holds
a license to train on submitted Cloaked pairs per the consent record
version in force at submission time. Consent records are versioned and
hash-referenced in every envelope so "what did they agree to" is always
answerable. `[NEW — needs the eventual real attorney; flag for trust /
Golden Leash alignment]`

---

## 5. Ingestion pipeline detail

### (2) Provenance Guard `[PRIOR — bidirectional IP layer, inbound side]`

Schema validation, client signature check, consent-receipt check, dedupe
(content hash), per-client rate limits, tier tagging. Rejects are logged
with reason codes; nothing rejected is retained beyond the audit log.

### (3) Replay Verification `[NEW — the load-bearing mechanism]`

The node NEVER trusts a submitted verdict. Each pair is re-executed in a
sealed, network-isolated container: compile `before` (must fail as claimed
or pair is rejected as unverifiable), compile+run `after` against the test
corpus (must pass as claimed, exit codes included). Recomputed verdict must
match submitted verdict exactly; any divergence = reject + reason code +
provenance flag on the submitting client.

**Test surface resolution:** when the submitted pair includes a `test_ref`
(harness_id + version_hash), the node resolves and executes replay against
its own pinned mirror of that harness at the specified version. The submitted
`test_surface` content is ignored for replay execution (retained for audit).
This closes test-surface gaming for any pair referencing a recognized public
harness: the test corpus is the node's canonical copy, not the submitter's
claim. `[NEW — test_ref dual-mode, owner verdict 2026-06-11]`

Replay is the anti-poisoning floor: a poisoned pair must now actually compile
and pass to enter the pipeline at all, which converts "inject garbage" attacks
into "submit working code" — and working code that passes its own tests is,
definitionally, lower-toxicity signal.

### (3a) Replay Host Requirements `[NEW — owner verdict 2026-06-11; REQUIRED]`

Replay runs on a **dedicated sealed host**. This is a hard requirement, not a preference.
Zero shared hosts, volumes, or credentials with the eval fleet. The replay host has no
outbound network access; runs ephemeral containers with resource caps per job; holds no
campaign-related data or lock-evidence artifacts. The separation is an integrity
requirement: the eval fleet's task-image isolation produces the published lock claims;
any contamination from untrusted submitted pairs would corrupt those claims. Cost
optimization is explicitly NOT a justification for sharing hardware with the eval fleet.
`[NEW]`

### (4) Node-side Eligibility Gate `[PRIOR — Section 12 gate, mirrored]`

Quality rules beyond correctness: minimum diff substance (no whitespace
churn), license heuristics, duplicate-family suppression, per-language
balance quotas, and a toxicity layer for what replay can't catch (see §6).

### (5) DP Aggregation `[PRIOR — federated/DP design]`

Pairs enter a shared corpus only after k-anonymity thresholds per pattern
family and DP noise on aggregate statistics.

**v0 honesty note:** full DP-SGD training is NOT a v0 commitment. v0 commits
to aggregation-side anonymity thresholds and publishes exactly what is and
isn't DP-protected. Do not let marketing say "differential privacy" beyond
what is implemented. `[NEW — the claims-smaller-than-proof rule applied to
privacy claims]`

---

## 6. Anti-poisoning threat model

Replay defeats false-verdict injection. Remaining vectors and v0 answers:

1. **Semantic backdoors** — pairs that compile and pass but teach a harmful
   pattern (e.g., subtly weakened crypto idiom). v0: pattern-family review
   queue for any pair family exceeding influence thresholds; configurable
   per-source influence caps applied to the shared/community corpus (sealed
   cartridges exempt). v0 default caps: per-client ≤1% of any training
   batch; ≤5% of any pattern-family slice; new-client ramp 0.25% until
   reputation threshold met. Claim language: "configurable per-source
   influence threshold with reputation-conditioned ramp." `[NEW — caps
   resolved by owner verdict 2026-06-11]`

2. **Slow corpus skew** — coordinated clients drifting the corpus toward
   degenerate styles. v0: per-client and per-pattern-family quotas +
   before/after eval on a frozen internal benchmark for EVERY corpus release;
   a corpus release that regresses the frozen bench does not ship
   (compiler-oracle discipline applied to the corpus itself). `[NEW — this is
   the node-side analog of "no silent regression overwrites"]`

3. **Test-surface gaming** — submitting trivial tests that anything passes.
   v0: minimum test-surface substance rules in the eligibility gate; pairs
   whose tests don't discriminate (before must FAIL them) are already rejected
   by replay. When the pair uses `test_ref` to reference a public harness,
   the node replays against its own canonical harness mirror — test-surface
   gaming via fabricated inline test content is fully closed for all
   public-harness pairs. `[NEW; test_ref closure owner verdict 2026-06-11]`

4. **Cloak-space collisions** — adversarial x_NNNN patterns designed to
   collide with other clients' cloaked vocab. v0: per-submission namespace
   re-mapping at intake; client cloak-space is never preserved into the
   corpus. `[NEW]`

---

## 7. Return path: OTA weight deltas

Signed (org key in the trust structure), versioned, per-tier model deltas;
clients verify signature before Ollama hot-swap; ForgeDaemon treats an OTA
delta exactly like a local retrain product — same `verified_locked` gating
before it goes live on the user's machine. Users can pin versions and refuse
OTA entirely (local-only mode remains first-class forever).

`[PRIOR — OTA + hot-swap + verified_locked gating; NEW — explicit client-side
gate on inbound weights, symmetric with the node's gate on inbound pairs.
The bidirectional principle, completed.]`

---

## 8. Transparency ledger

Public, rendered-from-JSON (never hand-edited): submission counts by tier,
rejection counts by reason code, corpus release notes with frozen-bench
before/after, and every consent-record version ever in force. Content is never
published; counts always are. `[PRIOR — radical transparency governance,
shipped WITH the product]`

---

## 9. Patent-relevant mechanism list

For claim triage in `docs/patent/claim_charts/`. Full triage in NOVEL-10–13
and NARROW-04.

| # | Mechanism | Tag | Claim chart target |
|---|---|---|---|
| N-10 | Replay-verification ingestion gate: never-trust-submitted-verdicts; bidirectional compile-fail / compile-pass check; test_ref dual-mode (replay against node-canonical harness mirror when available) | `[NEW]` | `claims_likely_novel.md` NOVEL-10 |
| N-11 | Corpus-release gating by frozen-benchmark regression test: a corpus release that regresses the internal frozen bench does not ship | `[NEW]` | `claims_likely_novel.md` NOVEL-11 |
| N-12 | Per-submission cloak-namespace re-mapping at intake: client x_NNNN space never preserved into shared corpus | `[NEW]` | `claims_likely_novel.md` NOVEL-12 |
| N-13 | Client-side verified_locked gating of OTA weight deltas (symmetric trust boundary: same gate inbound pairs / outbound weights) | `[PRIOR mechanism, NEW framing]` | `claims_likely_novel.md` NOVEL-13 |
| N-14 | Tier-gated corpus promotion: multi-condition gate (regulatory review + agreement + scrub + DP + ledger sign-off) required before any sealed cartridge pair migrates to shared corpus | `[NEW]` | `claims_likely_novel.md` NOVEL-14 (needs triage) |
| N-15 | Cloaked-pair + DP aggregation + cartridge routing as a combined privacy pipeline | `[PRIOR]` | `claims_needing_narrowing.md` NARROW-04 |

---

## 10. Resolved questions (owner verdict 2026-06-11)

**All five questions resolved by owner verdict 2026-06-11.**

1. **TEST SURFACE** — RESOLVED 2026-06-11: Dual-mode. `test_ref`
   (harness_id + version_hash) is PREFERRED when a public harness exists;
   inline `test_surface` is fallback for bespoke/enterprise. Node replays
   against its own pinned harness mirror when test_ref resolves; submitted
   test content not executed if canonical copy available.

2. **INFLUENCE CAPS** — RESOLVED 2026-06-11: Per-client ≤1% of any training
   batch; ≤5% of any pattern-family slice; new-client ramp 0.25% until
   reputation threshold met. Shared/community corpus only; sealed cartridges
   exempt. Claim language: "configurable per-source influence threshold with
   reputation-conditioned ramp."

3. **SCHOOL CARTRIDGE** — RESOLVED 2026-06-11: SEALED BY DEFAULT. School
   signal does not feed community corpus absent the full gated promotion
   pathway (§4). No mixing, no DP-aggregation workaround. Public statement:
   "sealed; any future sharing only under a published consent and compliance
   framework."

4. **REPLAY HOST** — RESOLVED 2026-06-11: Dedicated sealed host REQUIRED.
   Zero shared infrastructure with eval fleet. No outbound network; ephemeral
   containers; resource caps; nothing campaign-related on the box. Eval-fleet
   isolation is an integrity requirement for published lock claims.

5. **CONSENT** — RESOLVED 2026-06-11: Versioned-consent-hash mechanism is
   provisional disclosure material as drafted. Parking-lot language for real
   attorney review remains intact.

---

## 11. v0 build scope (post-announce)

Intake API + provenance guard + replay container + eligibility mirror +
flat-file corpus store + transparency ledger render. No DP layer, no training
runs, no OTA in v0 — v0 proves the trust boundary, not the flywheel-at-scale.

Estimate: bounded weeks of work, all deferred until after announce.

**Pre-announce deliverables from this document:**
- (a) §1 answers memorized for any public statement about the fleet
- (b) §9 mechanisms folded into `claim_charts/` before the provisional envelope seals
- (c) Open questions §10 answered by Ryan before claim language is finalized

---

*LUNARIAN NODE v0 · Ryan Gurganious · Lunarian Data Systems · 2026-06-11*
*Pre-filing provisional written-description material. Not legal advice.*
*Not a product specification. Not a build commitment.*
