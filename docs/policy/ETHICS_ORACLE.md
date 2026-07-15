# Ethics Oracle — Deterministic Behavioral Guardrail

> **Authored**: 2026-06-06 · Ryan Gurganious  
> **Status**: **Implemented 2026-07-01** — see `scripts/determinex_safety.py` (the pre-existing L0-L4
> `SafetyEngine`, already live-wired into `determinex_hive.py` / `hive/api_client.py` /
> `hive/compiler.py` / `hive/workspace.py`, was audited before build and found to already cover 4
> of the 5 violation classes below under different names — L0 Content Policy = weapons/CBRN +
> CSAM, L2 Egress Filter + L3 Output Scanner = data exfiltration, L4 Corpus HMAC = a
> secret-keyed integrity check. This spec's genuinely missing pieces were added additively:
> a tamper-evident hash-chained WAL (`wal_append()`/`verify_wal_integrity()`, Layers 0-6 write to
> it, not just corpus signing), tiered per-subject escalation (`EscalationState`, warn/restrict/
> cutoff, hard-blocks regardless of engine mode once escalated), **Layer 5 — License Scan**
> (`check_license()`, SPDX/copyleft header detection, wired into `sign_corpus_entry()` fail-closed),
> and **Layer 6 — Runtime Integrity** (`check_runtime_integrity()`, self-hash of the gate's own
> files against a manifest — the ToS-circumvention signal; fails closed if the manifest was never
> generated, never silently passes). Test coverage: `tests/test_safety_escalation.py` (21 cases).
> **Known, documented gap**: Child Safety (CSAM) is a text-keyword net only (Layer 0) — there is no
> offline media-hash/image classifier. This is not faked as covered; it is the one class in this
> spec without a real deterministic signal beyond keyword matching, called out here so it isn't
> mistaken for done. Phase 3 (Hive Mind pre-flight integration) is live for specs/egress/output;
> Phase 4 (Tauri Compliance Dashboard panel) and Phase 5 (third-party attestation) remain open.  
> **Patent relevance**: Candidate claim for provisional filing

---

## Concept

Determinex applies the compiler-oracle philosophy to code quality: the compiler is the only judge, deterministic, zero hallucination. The Ethics Oracle extends this same discipline to behavioral compliance.

```
ethics_oracle(action) → {1 = clean, anything else = violation}
```

Binary. Deterministic. No LLM-as-judge. An actual running gate that produces a verifiable audit log — not a policy document, not a ToS checkbox.

---

## Why This Matters

Healthcare, government, and defense buyers (HIPAA, FedRAMP, CMMC) require demonstrable audit trails for AI behavioral compliance. Every existing approach relies on:
- Policy documents (no enforcement)
- ToS checkboxes (no audit trail)
- LLM self-assessment (gameable, stochastic)

Determinex's Ethics Oracle produces a **cryptographically-anchored, deterministic log** that oversight bodies can audit. Nobody else has this — not because they couldn't, but because they didn't apply the compiler-oracle philosophy to the ethics layer.

---

## Violation Classes (Enumerable, Deterministic)

Each violation class has a specific, computable signal. Vague categories get exploited; enumerable signals don't.

| Violation Class | Examples | Deterministic Signal |
|---|---|---|
| Weapons / CBRN | Targeting system code, bioweapon synthesis routes | AST pattern match on known signatures |
| Data exfiltration | Bypassing Project Cloak, raw PII in outbound payloads | Network call inspector + Cloak audit layer |
| Child safety | Prohibited content generation categories | Hash/classifier gate (offline model, not API) |
| License violation | GPL code injected into commercial corpus | SPDX header scan on every training sample |
| ToS circumvention | Stripping ethics layer, forking without license | Binary integrity check on the runtime |

---

## Tiered Response (Escalation Curve)

Flat cutoffs punish misconfiguration the same as malicious use. The escalation curve produces a cleaner audit trail and protects legitimate users.

```
Violations 1–2  → warning + logged to tamper-evident WAL
Violations 3–5  → IDE restricted mode (read-only, no model calls)
Violations 6+   → corpus cut; redownload + re-agree to ToS required
```

The redownload mechanic creates a **documented consent trail** on every reset — legally meaningful, auditable.

The accumulation threshold is configurable per deployment context (enterprise can tighten; research can loosen). The log is always written regardless of threshold.

---

## Accumulation Logic

```python
def ethics_gate(action: Action, context: Context) -> int:
    """Returns 1 (clean) or violation code. Never stochastic."""
    for check in VIOLATION_CHECKS:
        result = check.run(action, context)  # deterministic
        if result != CHECK_CLEAN:
            WAL.write(action, check.violation_class, result)  # atomic fsync
            return result.code
    return 1  # clean
```

WAL writes are `os.fsync()` atomic — same invariant as the Compiler Oracle training WAL. No write-cache races.

---

## Relationship to Existing Determinex Architecture

- **Compiler Oracle** — ground truth for code correctness  
- **Project Cloak** — privacy gate (prevents PII/identifier leakage to cloud AI)  
- **Ethics Oracle** — behavioral compliance gate (prevents misuse categories)

The Ethics Oracle sits in the same layer as Cloak: a pre-flight check before any model call or corpus write. If the gate returns non-1, the action is blocked and logged before reaching the model.

---

## Patent Claim Candidate

"A system and method for deterministic behavioral compliance auditing in AI coding assistants, comprising: an enumerable violation-class registry with per-class computable signals; a binary gate function returning a canonical clean value or a violation code; a tamper-evident append-only audit log with atomic writes; and a tiered escalation response including corpus cutoff and re-consent mechanics."

This is distinct from:
- LLM-as-judge systems (stochastic, gameable)
- Policy filtering (pre-call, not post-audit)
- RLHF reward shaping (training-time, not runtime enforcement)

---

## Implementation Path

1. **Phase 1** — DONE (2026-07-01): violation classes enumerated (L0-L6), WAL appender shipped
   as a purpose-built hash-chained/fsync JSONL log rather than reusing the PB training WAL
   (`scripts/pb_wal.py`) or the general run ledger (`scripts/run_ledger.py`) — both were audited
   first; neither's schema fit a tamper-evident decision log, so `wal_append()`/
   `verify_wal_integrity()` in `determinex_safety.py` is the canonical home going forward.
2. **Phase 2** — DONE (2026-07-01): per-class signal detectors implemented — L0 keyword/regex
   content policy, L1 intent classifier, L2 egress secret/PII scan, L3 AST+regex output scanner,
   L4 HMAC corpus integrity, L5 SPDX license scan, L6 self-hash runtime integrity. CSAM remains
   keyword-only (documented gap above); no image/hash classifier exists.
3. **Phase 3** — PARTIAL: live at spec/egress/output call sites (`determinex_hive.py`,
   `hive/api_client.py`, `hive/compiler.py`, `hive/workspace.py`). Escalation-tier enforcement
   (`_enforce()` hard-blocking at RESTRICT/CUTOFF) is wired through all of those same call sites
   since they all route through `SafetyEngine._enforce()`. Not yet done: a dedicated pre-flight
   check at Hive session start that surfaces a subject's current tier before work begins, rather
   than discovering it mid-pipeline on the next violation.
4. **Phase 4**: Expose audit log via Tauri frontend panel (Compliance Dashboard) — not started.
5. **Phase 5**: Third-party attestation — generate cryptographic proof artifact (same pattern as Cloak audit) — not started.

---

*Determinex · Ryan Gurganious*
