# Determinex Safety Architecture

> **Honest scope statement**: Determinex's safety system is a logged, deterministic
> policy floor. It reliably catches known-bad categories and produces a complete
> audit trail. It does not prevent all misuse. Novel attacks, multi-step
> composition across innocuous-looking specs, and unknown malware shapes will
> not be caught by the current layers. Those are unsolved problems in the field,
> not solved ones.

---

## What is built and running

Five independent layers, all fail-closed (deny on unexpected error):

### Fairness Audit Utility
**File:** `scripts/fairness/audit.py`
**Policy:** `docs/policy/AI_FAIRNESS_AUDIT.md`

Determinex can compute deterministic group fairness metrics for supplied binary
decision datasets: selection rate, true positive rate, false positive rate,
demographic parity difference, equal opportunity difference, and equalized odds
difference. This is measurement only. It does not debias models, certify dataset
representativeness, or prove deployment fairness.

### L0 — Content Policy
**File:** `scripts/determinex_safety.py` → `_DENY_PATTERNS` / `pre_spec_gate()`
**Called:** At session creation, before anything else runs.

Pre-compiled regex scan across the full spec text. A single match in any category
raises `SafetyDenied` immediately — the session is never created.

**28 absolute-deny categories** (zero-exception): ransomware, disk wipers, droppers,
trojans, bootkits, botnets, shellcode, buffer-overflow exploit code, CVE
weaponization, privilege-escalation exploits, DDoS tools, exploit scanners,
credential stealers, stuffing tools, phishing kits, RATs, keyloggers,
stalkerware, covert screen capture, astroturfing networks, disinfo generators,
harassment bots, doxxing tools, academic fraud, identity forgery, financial
fraud tooling, CSAM, weapons synthesis instructions, attacks on critical
infrastructure.

**12 ethical-harm categories** (legal but harmful): covert surveillance,
deepfakes, voice cloning for fraud, OSINT aggregation for targeting, dark-pattern
manipulation, addiction-optimization systems, fake review generation,
discriminatory proxy screening, wage theft automation, spam infrastructure,
unauthorized crypto mining, predatory lending tools.

**What L0 catches:** Unsophisticated direct requests in one spec.
**What L0 does not catch:** The same intent expressed across multiple specs,
encoded in unusual phrasing, or through indirect composition.

---

### L1 — Intent Classifier
**File:** `scripts/determinex_safety.py` → `_COMPILED_INTENT` / `check_spec()`
**Called:** After L0 passes, still pre-session.

Catches reframing. A signal keyword alone is not a match — it must co-occur
with an amplifying context pattern in the same text. "Monitor" passes.
"Monitor without the user's knowledge" triggers `COVERT_MONITORING`.

Ten signal+amplifier pairs covering: covert monitoring, covert tracking,
non-consensual data collection, automated harassment, AV/EDR evasion,
code injection into process memory, persistence mechanisms, credential
exfiltration, obfuscation for evasion, synthetic identity fraud.

**What L1 catches:** Single-spec reframing using indirect language.
**What L1 does not catch:** Distributed multi-spec composition where no
individual spec contains both a signal and its amplifier.

---

### L2 — Egress Filter
**File:** `scripts/hive/safety_gate.py` → `pre_api_gate()`
**Called:** Before every cloud API call, without exception.

Scans all outbound prompt content for 16 categories of secrets (LLM API keys,
cloud credentials, VCS tokens, service tokens, PEM private keys, JWTs, database
URLs with embedded credentials). Also blocks credential environment variable
assignments and enforces Cloak (blocks cloud calls when `DETERMINEX_REQUIRE_CLOAK=1`
and obfuscation is inactive).

**What L2 catches:** Secrets leaking to cloud providers, plaintext source code
going to cloud AI without Cloak.
**What L2 does not catch:** Secrets encoded in non-standard formats or split
across multiple calls.

---

### L3 — Output Scanner
**File:** `scripts/determinex_safety.py` → `check_output()` /
`scripts/hive/compiler.py` → `scan_builder_output_security()`
**Called:** After Builder generates code, before corpus write.

Scans generated code for behavioral indicators of malicious intent — not just
syntactic patterns. Hard-block signals: hardcoded external hosts in HTTP/socket
calls, LSASS reads, `/etc/shadow` reads, Windows credential registry reads,
keylogger API calls, process name masquerade, anti-debug routines, anti-VM
routines, shellcode-structure hex runs, executable memory mapping, crypto miner
pool connections.

Contextual checks (signal+amplifier): destructive `rmtree` targeting system
paths, startup/persistence writes, `shell=True` with string concatenation.

Python-specific: `exec(compile(...))`, `eval(base64...)`, `marshal.loads`,
`pickle.loads(base64...)`.

**What L3 catches:** Known malicious-intent code shapes produced by the Builder.
**What L3 does not catch:** Novel attack patterns, multi-file attacks where no
single file triggers a pattern, obfuscated payloads that pass the scan.

---

### L4 — Corpus Integrity
**File:** `scripts/corpus/corpus_manager.py` / `scripts/determinex_safety.py`
**Called:** On every corpus write; verified at retrain time.

Every corpus record is HMAC-BLAKE2b-256 signed over canonical JSON (sorted keys,
ASCII-safe, NFC-normalized). At retrain ingest, records with missing or
invalid signatures are rejected and written to the rejected log. Tamper events
are written to the audit log.

`SafetyDenied` events from L0–L3 are themselves written to the `safety_refusal`
corpus — they become training signal. The model learns to refuse these categories
through observed refusal examples, not just through inference-time blocking.

**What L4 catches:** Post-hoc tampering with training data, unsigned corpus
entries.
**What L4 does not catch:** Attacks that compromise the HMAC key before it is
used, or manipulation that occurs before the corpus write.

---

## Ethics Oracle (L5) + Runtime Integrity (L6)

**Spec:** `docs/policy/ETHICS_ORACLE.md`
**Code:** `scripts/determinex_safety.py` · **Tests:** `tests/test_safety_escalation.py`
**Status: IMPLEMENTED 2026-07-01.** (This section previously said "NOT
IMPLEMENTED" — true when written, corrected only after the code and tests
landed. Same designed-is-not-shipped standard, applied in both directions.)

What runs today, extending the pre-existing L0–L4 engine:
- **Tamper-evident, hash-chained WAL** — every violation is appended to
  `logs/safety_wal/wal.jsonl`, each record chained to the previous record's
  hash and fsync'd (`wal_append()` / `verify_wal_integrity()`). Tampering is
  detectable by any third party walking the chain from genesis — auditable,
  not just self-consistent to a keyholder.
- **Tiered escalation curve** (per the spec): violations 1–2 → warn (WAL
  only), 3–5 → restricted mode, 6+ → corpus cutoff + re-consent. State is
  per-subject and persisted; only `clear_escalation()` — a deliberate
  operator action — resets it (`record_violation()` / `EscalationState`).
- **License / provenance scan** (`check_license()`) over corpus-bound text.
- **Runtime integrity check** (`check_runtime_integrity()`) against the
  signed manifest at `assurance/security/safety_layer_integrity.json` — the
  safety layer verifies *itself* has not been modified.

L0–L6 are all live. The remaining honest caveat: the violation-class
registry's signals are pattern-based; false-positive risk against the PB
corpus (security tooling discussed in benign context) is real and remains
under test.

---

## Copyright Displacement Guard + Provenance Sidecar (observe mode — not a training gate)

**File:** `scripts/determinex_copyright_guard.py`
**Status: Built. Runs as a fire-and-forget sidecar in the hive executor and PB agent.**

Two complementary systems in one module:

**1. Copyright Guard (verbatim protection)**
Detects contiguous token runs of 50+ tokens (≈ 3–5 lines) matching any registered
protected work. Operators seed `corpus/protected/*.txt`. Findings are logged to
`logs/copyright_guard/audit.jsonl`.

**2. Provenance / Attribution Tagger**
Detects inspiration and derivation from registered reference sources using
three-tier similarity detection:
- `verbatim_reproduction` — ≥50 consecutive matching tokens
- `substantial_similarity` — ≥30 token run OR ≥25% stopword-filtered bigram Jaccard
- `inspiration` — ≥15% stopword-filtered bigram Jaccard

Reference sources (OSS projects, academic papers, patents) are seeded from
`corpus/references/<subdir>/` with per-directory `metadata.json`. When a match
is found, an `AttributionTag` is produced and written to `logs/copyright_guard/attribution.jsonl`.

**Provenance mode — explicit boundary:**

The sidecar runs in `observe` mode by default (`DETERMINEX_PROVENANCE_MODE=observe`).
In observe mode:

- The sidecar logs attribution tags and copyright alerts to append-only audit logs.
- It is **not wired into training rewards or corpus filtering**. `blocks_corpus_ingestion`
  always returns `False`. The compiler is the only oracle on the training-corpus path.
- It never raises and never slows the compile gate.
- Permissive-licensed OSS references (MIT, Apache-2.0, etc.) never produce
  `CopyrightAlert` even on verbatim matches — those produce `AttributionTag` only,
  because verbatim reuse of MIT-licensed code with attribution is the system working.

Setting `DETERMINEX_PROVENANCE_MODE=enforce` changes behavior:
- Verbatim hits on non-permissive (proprietary/unknown) reference sources additionally
  produce `CopyrightAlerts`. Callers may then gate on `report.blocks_corpus_ingestion`.
- Does NOT affect protected-works detection (Pass 1), which always alerts regardless of mode.

**Wiring:** The sidecar is inserted as a non-blocking step in `scripts/hive/executor.py`
(after step-integrity checks, before corpus write) and `scripts/determinex_programbench_agent.py`
(after template-leak detector, before compile gate). Both insertions are wrapped in
`try/except Exception` — any provenance failure is logged at DEBUG level and never
propagates to the compile or eval path.

To use the full provenance API:
```python
from determinex_copyright_guard import get_guard

guard = get_guard()  # auto-seeds from corpus/protected/ and corpus/references/
report = guard.check_provenance(generated_output, task_id="run_001")
if report.has_copyright_violation:          # only True for genuine protected-work hits
    log.warning("Copyright alert: %s", report.copyright_alerts)
if report.has_attributions:
    output += "\n" + report.format_reference_block(style="code_comment")
guard.log_attribution(report)              # write consolidated record to attribution log
```

Legacy API (backward-compatible):
```python
alert = guard.check(generated_output, task_id="run_001")  # returns first CopyrightAlert or None
```

---

## Configuration reference

| Variable | Default | Effect |
|---|---|---|
| `DETERMINEX_SAFETY_MODE` | `strict` | `strict`=raise on violation, `warn`=log only, `audit`=always pass (test only) |
| `DETERMINEX_REQUIRE_DOCKER` | `1` | Block fallback to non-Docker compiler execution |
| `DETERMINEX_REQUIRE_CLOAK` | `1` | Block cloud calls without identifier obfuscation active |
| `DETERMINEX_PROVENANCE_MODE` | `observe` | `observe`=sidecar only, never gates ingestion; `enforce`=CopyrightAlert on non-permissive verbatim hits |
| `DETERMINEX_COPYRIGHT_MIN_TOKENS` | `50` | Minimum consecutive-token run to trigger copyright alert |
| `DETERMINEX_PROTECTED_WORKS_DIR` | `corpus/protected` | Auto-seed directory for registered protected works |
| `DETERMINEX_REFERENCES_DIR` | `corpus/references` | Auto-seed directory for attribution reference sources |
| `DETERMINEX_COPYRIGHT_AUDIT_LOG` | `logs/copyright_guard/audit.jsonl` | Copyright alert audit log path |
| `DETERMINEX_ATTRIBUTION_LOG` | `logs/copyright_guard/attribution.jsonl` | Attribution tag audit log path |
| `DETERMINEX_SUBSTANTIAL_TOKENS` | `30` | Minimum token run for substantial-similarity tier |
| `DETERMINEX_SUBSTANTIAL_BIGRAM` | `0.25` | Bigram Jaccard threshold for substantial similarity |
| `DETERMINEX_INSPIRATION_BIGRAM` | `0.15` | Bigram Jaccard threshold for inspiration tier |

---

*Determinex · Ryan Gurganious*
*Safety doc last updated: 2026-06-10 — provenance sidecar wiring + observe/enforce mode documented*
