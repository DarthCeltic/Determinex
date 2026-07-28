# Determinex End User License Agreement — SUPERSEDED, NEVER TOOK EFFECT

> **Superseded 2026-07-10.** Determinex moved from a source-available
> commercial-license model to AGPLv3 (see [`../papers/LICENSING.md`](../papers/LICENSING.md)).
> This draft was written to summarize a separate-commercial-agreement model
> that no longer exists — AGPLv3 needs no EULA; the license text in
> `../../LICENSE` is the complete, self-sufficient legal terms for every
> user. This file is kept only as a historical record and was never
> published or in effect. Do not use it for anything.
>
> Original draft note (2026-07-01), preserved for context: this was a
> starting point for legal review of the then-current Source-Available
> License 1.0, not an agreement in effect.

## 1. Relationship to LICENSE

The authoritative license terms are in the repository's `LICENSE` file
("Determinex Source-Available License 1.0"). If anything in this EULA
conflicts with `LICENSE`, `LICENSE` controls until reconciled by legal
review. This draft exists to give end users (who may never open a LICENSE
file) a plain-language summary at install time.

## 2. Plain-language summary (see LICENSE for actual terms)

- **Personal / non-commercial use is free.** Learning, experimentation,
  local productivity — no revenue or commercial advantage derived from
  the Software.
- **Internal Evaluation is permitted** — using Determinex to decide whether to
  enter a commercial agreement, not for production/customer-facing use.
- **Commercial use requires a separate written agreement** with Ryan
  Gurganious / Lunarian Data Systems. Commercial and patent rights are
  reserved.
- Full definitions, obligations, and exceptions (including third-party
  component licenses) are in `LICENSE` — this summary does not replace it.

## 3. Model weights and third-party components

Determinex bundles or downloads model weights derived from third-party base
models (Qwen2.5-Coder — Apache 2.0; Llama-3.2 — Meta's Llama 3.2 Community
License; Mistral-7B — Apache 2.0). See
[`docs/security/MODEL_LICENSING.md`](../security/MODEL_LICENSING.md) for the
current audit of what obligations attach to each, particularly the Llama
Community License's attribution/naming/AUP requirements that apply if
Observer-family weights are ever redistributed.

## 4. No warranty (placeholder — needs real legal language)

The Software is provided "as is." [TODO — legal to draft standard
disclaimer-of-warranty and limitation-of-liability language appropriate for
a source-available commercial license; do not ship without it.]

## 5. Acceptable use

Determinex includes a deterministic safety gate (`scripts/determinex_safety.py`,
the "Ethics Oracle" — see [`docs/policy/ETHICS_ORACLE.md`](../policy/ETHICS_ORACLE.md))
that blocks certain categories of generated content and escalates repeated
violations. [TODO — legal to determine whether/how the underlying policy
categories should be surfaced as explicit EULA terms, and whether
circumventing the safety gate should be an explicit breach condition.]

## 6. Open questions for legal review

- Does the Source-Available License need a distinct consumer-facing EULA
  at all, or should install-time consent simply link to `LICENSE` directly?
- Trademark/naming terms once "Determinex" naming is resolved (see the
  possible name-collision note in project memory — unresolved as of this
  draft).
- Export control / dual-use software considerations given the security-
  tooling nature of parts of the product (Project Cloak, reimplementation
  of security CLIs in the ProgramBench corpus).
