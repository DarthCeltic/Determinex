---
name: cloak-safety
description: |
  Load when user discusses sending proprietary code to cloud APIs, privacy requirements,
  identifier obfuscation, data leakage risks, or cloaking/uncloaking workflows.
  Load when user asks whether their code is safe to send to Claude, GPT, Gemini, or any
  external model. Do NOT load for general coding questions with no privacy angle.
depends: []
---

# Project Cloak: Safety Properties and Threat Model

*A companion to the Determinex white paper. Ryan Gurganious · 2026*

---

## What Cloak Protects

Project Cloak's threat model is narrow and precise: **a cloud API provider must not be able to reconstruct proprietary identifiers from the inputs they receive.**

Cloak does not protect:
- File structure (directory layout and filenames are preserved in region mode)
- Algorithmic patterns (the structure of the code is preserved; only names change)
- String literals that are not identifiers (user-facing strings are not obfuscated by default)

What it protects absolutely:
- Every function name, class name, variable name, parameter name, and module name in the repository — replaced with opaque `x_NNNN` tokens before any bytes leave the machine.

---

## The Threat Model

**Adversary:** A cloud API provider (or anyone with access to their logs) who receives obfuscated API requests.

**What they see:** A syntactically valid version of the repository where every identifier is replaced with `x_NNNN`. They can see the code structure, control flow, and algorithms. They cannot see `authenticate_user`, `validate_payment`, `internal_fraud_score`, or any other business-critical name.

**What they cannot do:** Reconstruct the original identifiers. The mapping from real names to `x_NNNN` tokens is kept in a local cryptographic table that never leaves the machine.

**What the system verifies:** After every obfuscation pass, Cloak runs a pattern-match scan against the API request body to confirm zero identifier leakage. The audit artifact (`DETERMINEX_CLOAK_AUDIT=1`) produces a cryptographic proof of this verification.

---

## The Obfuscation Pipeline

Cloak's 7-component pipeline (fully described in docs/PROJECT_CLOAK.md):

1. **AST parsing** — per-language parsers (tree-sitter) extract every identifier definition and reference in the repository
2. **Scope-aware mapping** — identifiers are mapped to `x_NNNN` tokens consistently across files (same real name → same token everywhere)
3. **Region extraction** — the minimal code region needed to solve the target issue is extracted, not the full repository
4. **Obfuscation** — region content is transformed with the consistent mapping
5. **Semantic key injection** — a "glossary" of functional descriptions for high-frequency tokens is provided to the cloud model (what `x_4421` does, not what it is named)
6. **API call** — obfuscated region sent to cloud; cloud produces obfuscated patch
7. **Restoration** — patch is applied with reverse mapping; real identifiers restored before any disk write

---

## Why Region Mode Is Non-Negotiable

Early versions of Cloak sent whole-file content to the cloud model. This produced a specific failure: models with large context windows would echo back large sections of the file unmodified, and the patch application layer would reject the result as "too large to be a targeted fix."

Region mode was introduced to solve this. The model receives only the relevant code region, produces a targeted patch, and the patch application layer has a well-defined scope to apply it within.

The privacy properties are identical between region mode and whole-file mode — both obfuscate all identifiers. But region mode produces better patches and avoids the wholesale-rewrite failure mode.

The `_REGION_THRESHOLD = 0` setting forces region mode always. This is the hardened default.

---

## The Audit Artifact

Running with `DETERMINEX_CLOAK_AUDIT=1` produces a log of every outbound API request body. A post-run script (`scripts/verify_cloak.py`) scans this log for any identifier that appears in the original repository's identifier table.

The SWE-bench B-Cloaked run verified **1,813,760 identifiers across 300 instances** with zero restoration failures and zero privacy leaks.

The artifact is a machine-verifiable proof that the obfuscation pipeline maintained privacy throughout the run. It can be independently audited by anyone with access to the repository and the log file.

---

## Known Limitations

**String literals.** User-facing strings (error messages, log lines, UI copy) are not obfuscated. A string like `"Invalid authentication token for user"` would appear in the API request. If string literals contain proprietary identifiers, the `--obfuscate-strings` flag should be used (experimental; may break model coherence).

**File paths.** The relative paths of files in the repository are visible in region mode. A path like `src/payment/fraud_detection.py` reveals that a payment fraud detection module exists. Cloak does not currently obfuscate file paths.

**Comments.** Code comments are stripped before API calls. This is intentional — comments often contain the highest-value proprietary context.

**Algorithmic structure.** A sophisticated adversary could infer what a function does from its control flow, even with all names replaced. Cloak is not a semantic obfuscator. It protects names, not logic.

---

## Error Message Re-Obfuscation

When the cloud model produces a patch that fails the compile gate, the error message from the compiler contains real identifiers from the restored code. These real-identifier error messages must not be fed directly back to the cloud model.

Cloak handles this: compile errors generated from the real worktree are re-obfuscated through the same mapping before being injected into the next Architect prompt. The cloud model sees `x_4421 undefined on line 47` — never the real identifier.

This is one of the harder correctness properties to maintain and was explicitly verified during the hardening sprint.

---

## Practical Deployment Checklist

For a production deployment of Cloak:

- [ ] Set `DETERMINEX_CLOAK=1`
- [ ] Set `DETERMINEX_CLOAK_AUDIT=1` for the first run to generate audit artifact
- [ ] Run `scripts/verify_cloak.py` on the audit log to confirm zero leakage
- [ ] Review `_REGION_THRESHOLD = 0` is set (region mode always on)
- [ ] Confirm string literals don't contain proprietary identifiers (or use `--obfuscate-strings`)
- [ ] Review file paths for sensitive structure before running

---

## Gotchas — Known Failure Modes

**Do NOT load this Skill when:** The user is asking a general security question (XSS, CSRF, auth patterns) with no mention of sending code to an external model. That routes to general security context, not Cloak.

- **Star-import hole (Python):** `from module import *` causes identifiers imported via star to pass through uncloaked if the star resolver fails. Check the log for `"star-import holes"` warnings. If present, the cloud model may have seen real names for those specific identifiers.
- **String literal leakage:** Cloak does not obfuscate string literals by default. If a function name appears inside a string (e.g., `error = "authenticate_user failed"`), that string reaches the cloud API unmodified. Use `--obfuscate-strings` only if you have verified it doesn't break model coherence.
- **File path leakage:** Relative paths like `src/payment/fraud_detection.py` are visible in region mode. A sophisticated adversary can infer module purpose from path structure alone. Cloak does not currently obfuscate file paths.
- **Error re-obfuscation gap:** Compile errors from the restored worktree contain real identifiers. These MUST be re-obfuscated before feeding back to the cloud Architect. If this step is skipped, real identifiers leak through the retry loop.
- **Tree-sitter unavailable (silent fallback):** If `determinex_cloak_treesitter` is not installed, the bridge silently sets `_TS_AVAILABLE = False` and falls back to regex. Regex coverage for Go generics, Rust macros, and TypeScript decorators is incomplete. Check at boot that tree-sitter is active before claiming privacy sovereignty.
- **Region threshold misconfiguration:** If `_REGION_THRESHOLD` is not set to `0`, Cloak may send whole-file content in some cases, which degrades patch quality and can cause the model to echo large unchanged sections. Hardened default is region mode always.

---

*Related documents: docs/PROJECT_CLOAK.md · COMPANION_VIBE_CODING.md · docs/WHITE_PAPER.md Section 9*
