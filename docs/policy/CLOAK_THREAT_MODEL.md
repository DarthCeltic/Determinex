# Project Cloak — Threat Model

> Companion to `docs/PROJECT_CLOAK.md` and `docs/COMPANION_CLOAK_SAFETY.md`.
> This document enumerates **specific leak vectors**, the controls that mitigate
> each, the verifying tests/audits, and the residual risk. Locked under
> `locks/sentinel/CLOAK_THREAT_MODEL_LOCK_001.json`.

---

## 1. Scope and Trust Model

**Asset under protection:** proprietary identifier names in a private source
repository — function names, class names, method names, variable names,
parameter names, module names, and constants.

**Adversary:** a cloud LLM provider (or anyone with access to their request
logs) who receives obfuscated API requests issued by the Determinex agent during
SWE-bench, ProgramBench, or hive sessions.

**What is NOT in scope** (must be communicated to operators):
- File and directory **paths** are visible in region mode.
- **String literals** are not obfuscated by default.
- **Algorithmic structure** (control flow, AST shape) is preserved.
- **Comments inside source** are stripped, but the prompt assembled around the
  region is not stripped — operator-written prompts are sent verbatim.
- Cloak does not defend against an adversary who has **local host access**.
  Treat the obfuscation map (`cloak_map_<instance_id>.json`) as a secret.

**Implementation surface:**
- `scripts/determinex_cloak.py` — orchestration entry, error types.
- `scripts/determinex_cloak/` — modular pipeline (classifier, symbol_map,
  transformer, restoration, context, lang_extractor, safe_list,
  _treesitter_bridge).
- `scripts/determinex_cloak_treesitter.py` — tree-sitter parser bridge.
- `scripts/determinex_cloak_go.py`, `scripts/determinex_cloak_ts.py` — language
  extractors.
- `scripts/verify_cloak.py` — post-run audit, scans request logs for any
  identifier appearing in the per-instance reverse map.
- `scripts/cloak_audit.py` — audit log writer.

---

## 2. Leak Vectors and Controls

Each vector lists: **how it leaks → what mitigates it → how we verify → residual
risk**.

### 2.1 Identifier in source body

A raw private identifier (`authenticate_user`) appears inside the API request
body alongside obfuscated tokens.

| | |
|---|---|
| Mitigation | AST-aware identifier rewrite (`scripts/determinex_cloak/transformer.py`); `_REGION_THRESHOLD = 0` forces region mode always. |
| Verification | `scripts/verify_cloak.py` post-run pattern-match scan against every API request. SWE-bench B-Cloaked run verified 1,813,760 identifiers across 300 instances with zero leaks. |
| Test | `tests/test_cloak_smoke.py::CloakSmokeTests::obfuscate_replaces_private_identifiers`. |
| Residual risk | LOW. Star-import resolution holes (see 2.6) and single-character/dunder exemptions (2.7) are documented exceptions, not bugs. |

### 2.2 Identifier in docstring

A private identifier referenced inside a function or class docstring is sent to
the model unmodified.

| | |
|---|---|
| Mitigation | Docstring identifier-token regex swap (decision 3.3, "Option D"); `#` comments stripped entirely before send. |
| Verification | `verify_cloak.py` scans docstring content along with code. |
| Test | `tests/test_cloak_smoke.py::CloakSmokeTests::obfuscate_replaces_private_identifiers` covers docstrings. |
| Residual risk | LOW for tokens; MEDIUM for prose-form references. Cloak only swaps token-shaped substrings, so "the authenticate_user helper" gets cloaked but "the user authenticator" does not. |

### 2.3 Identifier in compile-error feedback loop

The Compiler Oracle runs against the **restored** worktree. The resulting error
message contains real identifiers (`error: cannot find function authenticate_user`).
Without re-obfuscation, that message would be injected into the next Architect
prompt verbatim and leak.

| | |
|---|---|
| Mitigation | Error re-obfuscation pass: compile-stage stderr is sent through the same forward map before any prompt that returns to the cloud Architect (`determinex_swebench_agent.py` `_feedback_inject` site). |
| Verification | `tests/test_cloak_smoke.py::CloakSmokeTests::restore_patch_passes_through_unknown_tokens` covers asymmetric AI-invented tokens; integration is exercised by SWE-bench B-Cloaked audit. |
| Residual risk | MEDIUM. Error formats from new compilers may produce identifier-shaped tokens that pre-date the symbol map (e.g., when a stack frame references a stdlib helper named after one of ours). Audit step continues to scan. |

### 2.4 Identifier in API request *metadata*

Headers, model-routing fields, query parameters, and the user-agent string
constructed by LiteLLM or the HTTP client could embed identifier-shaped
strings (e.g., function-call schemas).

| | |
|---|---|
| Mitigation | `DETERMINEX_CLOAK_AUDIT=1` logs the **full** outbound request (headers + body). `verify_cloak.py` scans the full payload, not just `messages[].content`. |
| Verification | Audit run on B-Cloaked Rosetta OFF passed with zero leaks across complete request envelopes. |
| Residual risk | LOW. Any new provider integration must be re-audited; do not assume LiteLLM provider X is safe because provider Y is. |

### 2.5 Identifier in tool/function-calling schema

If the agent advertises a tool schema like `{"name": "authenticate_user", ...}`
for function-call style requests, the schema is part of the request body and
will leak.

| | |
|---|---|
| Mitigation | Cloak does not currently rewrite tool schemas. **Operational rule**: do not register tools whose names mirror private identifiers. Tool names must come from the closed vocabulary in `scripts/agent/tool_registry.py` (generic verbs: `read_file`, `write_file`, `compile_check`, etc.). |
| Verification | `verify_cloak.py` flags any tool schema whose name appears in the symbol map. |
| Residual risk | MEDIUM. Operator discipline required. Add a new tool → review against private name table. |

### 2.6 Star-import pass-through (Python)

`from module import *` exposes identifiers via the star resolver. If the
classifier cannot resolve `module`, those identifiers are not added to the
private-identifier set and may pass through unobfuscated when referenced later.

| | |
|---|---|
| Mitigation | Star-import warnings are emitted by `CloakContext.star_import_warnings` and persisted to the per-instance audit JSONL. The SWE-bench astropy-12907 sample logged 169 star-import holes — auditable, not silent. |
| Verification | `verify_cloak.py` reports the star-import-hole count alongside leak count. Any star hole > 0 surfaces a WARN in the audit summary. |
| Residual risk | MEDIUM. Star imports remain a known sharp edge. Operators reviewing audit JSONL must inspect warning lines before claiming "zero leakage." |

### 2.7 Single-character and dunder exemptions

By design, `i`, `j`, `x`, `n`, `_`, `__`, and any name matching `^__.*__$` are
exempt from obfuscation (decisions 1.4 and 2.1).

| | |
|---|---|
| Mitigation | Documented exemption; the cloud model relies on these to read idiomatic loop variables and dunder methods. |
| Verification | `tests/test_cloak_smoke.py::CloakSmokeTests::obfuscate_preserves_single_chars_and_dunders`. |
| Residual risk | LOW. Single-letter names carry no proprietary meaning; dunder names are language protocol, not business logic. |

### 2.8 File path leakage in region mode

Region-mode requests include the file path (`src/payment/fraud_detection.py`).
A sophisticated adversary can infer module purpose from the path alone.

| | |
|---|---|
| Mitigation | None implemented yet. Operator-facing warning in `COMPANION_CLOAK_SAFETY.md` §80-83. Future work: path-hash mode flag. |
| Verification | `verify_cloak.py` lists every distinct path emitted per run so operators can review for sensitive structure. |
| Residual risk | MEDIUM. Operators must accept the path-as-context tradeoff. Path obfuscation is on the roadmap but does not gate the lock. |

### 2.9 String-literal leakage

A user-facing string `"Invalid authenticate_user token"` contains an identifier
substring. Cloak does not obfuscate string literals by default.

| | |
|---|---|
| Mitigation | `--obfuscate-strings` experimental flag exists but is off by default (may break model coherence). |
| Verification | `verify_cloak.py` scans string-literal bodies inside the obfuscated source and flags any identifier-shaped substring. |
| Residual risk | MEDIUM. Operators with high-sensitivity string content should review per-instance audit JSONL before claiming clean run. |

### 2.10 Plaintext fallback on internal error

If the obfuscator hits an internal exception, returning the original source
would catastrophically leak. The fail-closed invariant prevents this.

| | |
|---|---|
| Mitigation | `CloakObfuscationError` raised; never returns plaintext. `to_dict()` deliberately excludes the source it failed on. |
| Verification | `tests/test_cloak_smoke.py::CloakFailClosedTests::obfuscate_source_fail_closed_on_internal_error`, `obfuscate_source_str_fail_closed_propagates_through_context`, `cloak_obfuscation_error_to_dict_redacts_source`. |
| Residual risk | LOW. Invariant has explicit fail-closed tests; any regression flips a unit test red. |

### 2.11 Tree-sitter silent regex fallback

If `determinex_cloak_treesitter` fails to import, the bridge sets
`_TS_AVAILABLE = False` and falls back to regex coverage. Regex coverage for
Go generics, Rust macros, and TypeScript decorators is incomplete.

| | |
|---|---|
| Mitigation | `determinex doctor` boot-check verifies tree-sitter availability for each declared language; surfaces FAIL when sovereignty claim depends on it. |
| Verification | `tests/test_cloak_smoke.py::CloakSmokeTests` runs against the tree-sitter path; CI installs the bridge. |
| Residual risk | MEDIUM if operator runs Cloak in an env that hasn't installed tree-sitter parsers. Documented in `COMPANION_CLOAK_SAFETY.md` §122. |

### 2.12 Region threshold misconfiguration

If `_REGION_THRESHOLD` is set to a positive value, Cloak may emit whole-file
content for small files, which degrades patch quality and broadens the
adversary's view.

| | |
|---|---|
| Mitigation | `_REGION_THRESHOLD = 0` is the **hardened default**, asserted at module load. |
| Verification | `tests/test_cloak_smoke.py::CloakSmokeTests::obfuscate_replaces_private_identifiers` indirectly exercises region mode. A specific guard test asserts the constant value. |
| Residual risk | LOW. Constant is local to the module; any change requires explicit code review. |

### 2.13 Map persistence leakage

The per-instance symbol map (`cloak_map_<instance_id>.json`) is written to
`logs/swebench/cloak_audit/`. If this file is shipped to a third party
alongside the API request log, the adversary can reconstruct all real names.

| | |
|---|---|
| Mitigation | Operator policy: **never ship the cloak_map file** outside the local machine. Audit log + map = full reconstruction. Map files are git-ignored. |
| Verification | `.gitignore` includes `logs/swebench/cloak_audit/cloak_map_*.json`. |
| Residual risk | LOW (local). HIGH if operator violates the policy. Documented in §1 trust model above. |

### 2.14 Out-of-band telemetry channels

Determinex emits observability events to `logs/events/` and a SQLite DB
(`.determinex/chrono.sqlite`). If telemetry includes raw prompt content,
restoration must occur before write.

| | |
|---|---|
| Mitigation | Observability event writers strip prompt bodies and only retain hash + length. Real-identifier-bearing telemetry stays on-disk in the restored worktree, never on cloud-bound channels. |
| Verification | `tests/test_immutability_guard.py` indirectly confirms inspection commands do not mutate corpus; event log content is JSON, grep-auditable. |
| Residual risk | LOW for cloud egress; the local SQLite DB is treated as a host secret. |

---

## 3. Audit Procedure

Every claim of "zero leakage" requires the following sequence:

1. Set `DETERMINEX_CLOAK=1` and `DETERMINEX_CLOAK_AUDIT=1` for the entire run.
2. Confirm `determinex doctor` passes the `cloak` and `tree-sitter` checks.
3. After the run completes, execute:
   ```
   python scripts/verify_cloak.py logs/swebench/<run-id>/cloak_audit/ --strict
   ```
4. Verify exit code 0, leak count 0, and review the printed star-import-hole
   count.
5. Archive the audit directory under
   `assurance/evidence/cloak_audits/<run-id>/`.
6. Add the audit summary line to `docs/EVIDENCE_INDEX.md`.

### What a leak count of 0 does and does not prove

`verify_cloak.py` defines a leak as *an identifier from the run's forward map
appearing in an API request*. That map is produced by the same extractor whose
output was obfuscated — so **an identifier the extractor never captured cannot
appear in the map, and therefore cannot be reported as a leak.** The auditor is
blind in exactly the places the extractor is blind.

A green audit is therefore proof that *everything Cloak obfuscated stayed
obfuscated*. It is **not** proof that nothing leaked. The two are only the same
thing if extraction is complete, which is a separate property with a separate
test.

That separate test is `tests/test_cloak_language_coverage.py`. It plants
`zzq`-prefixed identifiers — nonsense to any safe-list — in a per-language fixture
and asserts none survive. Because it knows the names independently of the map, it
is the only check that can find an extraction gap. It has found real ones: three
of nine languages had no working grammar and TypeScript had neither a grammar nor
a regex fallback (a silent plaintext path, 2026-07-26), and JavaScript instance
fields written the conventional way — `this.field = 0`, an assignment to a
member_expression rather than a `field_definition` — survived obfuscation until
2026-07-28. Every one of those was invisible to `verify_cloak.py` by construction.

So: run the language-coverage suite as part of any privacy claim, and treat its
result as a precondition for reading the audit's leak count at all.

A run with a non-zero star-import-hole count is **not** a leak by itself, but
operators must explicitly inspect each warning before publishing privacy
claims.

---

## 4. Out of Scope

The following are explicitly NOT defended:

- Local host compromise (Cloak protects against the cloud provider, not against
  malware on the operator's machine).
- Side-channel inference from request timing, token count, or model selection.
- Adversaries with access to the operator's GitHub clone or backup tarballs.
- Adversaries who already possess a partial real-name vocabulary and can
  pattern-match against AST shape.
- Inference attacks that combine multiple obfuscated requests across runs to
  recover identifier semantics (defense: rotate the symbol map per session,
  which Cloak already does — one map per `instance_id`).

---

## 5. Change Log

| Date | Change |
|---|---|
| 2026-04-28 | Initial Cloak implementation (`CLOAK_LOCK_001`). |
| 2026-05-05 | Pipeline hardening sprint: C/C++ false-positives, TypeScript dangling-commit, paren-stripped anchor matching, feedback re-injection fix. |
| 2026-05-27 | This document. Threat-model lock `CLOAK_THREAT_MODEL_LOCK_001` established alongside Rung 6 of the pre-release hardening sprint. |

---

*Lock: `locks/sentinel/CLOAK_THREAT_MODEL_LOCK_001.json`. Related:
`docs/PROJECT_CLOAK.md`, `docs/COMPANION_CLOAK_SAFETY.md`,
`docs/THREAT_MODEL.md`, `locks/sentinel/CLOAK_LOCK_001.json`.*
