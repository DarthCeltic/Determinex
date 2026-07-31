# Determinex Corpus License Policy

> Version 1.1 · 2026-05-27
>
> Governing principle: **Do not ingest code just because it is public.**
> Ingest code only if license, provenance, security, and corpus purpose are all known.

---

## Policy Statement

Determinex's training corpus is built from code that:

1. **Has a known, permissive license** (green bucket) — not merely "public" or "open source"
2. **Has known provenance** — source repository, commit hash, author information recorded
3. **Has passed secret scanning** — no embedded API keys, private keys, or credentials
4. **Has been deduplicated** — no near-identical examples flooding the corpus
5. **Has a verified failure + repair pair** — the mutation failed compilation, the repair passed
6. **Has an HMAC-signed trace** — tamper-evident record linking input → output → verdict

Code that meets fewer than all six criteria does not enter the corpus.

---

## License Classification

### Green Bucket (auto-ingest allowed)

These licenses permit use, modification, and redistribution with minimal conditions.
Attribution requirements are met by recording the source in the corpus trace.

| SPDX ID | Common Name |
|---------|-------------|
| MIT | MIT License |
| Apache-2.0 | Apache License 2.0 |
| BSD-2-Clause | Simplified BSD |
| BSD-3-Clause | Modified BSD |
| ISC | ISC License |
| Unlicense | Public Domain (Unlicense) |
| CC0-1.0 | Creative Commons Zero |
| 0BSD | Zero-Clause BSD |
| BlueOak-1.0.0 | Blue Oak Model License |
| BSD-2-Clause-Patent | BSD + Patent Grant |

### Yellow Bucket (requires metadata review before training use)

These licenses have conditions (file-level copyleft, attribution chains, patent clauses) that
require review before the code is used for model training. Code may be indexed and analyzed
but not included in training without explicit sign-off.

| SPDX ID | Common Name | Concern |
|---------|-------------|---------|
| MPL-2.0 | Mozilla Public License 2.0 | File-level copyleft |
| EPL-2.0 | Eclipse Public License 2.0 | Weak copyleft |
| EPL-1.0 | Eclipse Public License 1.0 | Weak copyleft |
| CC-BY-4.0 | Creative Commons Attribution 4.0 | Attribution requirements |
| CC-BY-3.0 | Creative Commons Attribution 3.0 | Attribution requirements |
| CC-BY-SA-4.0 | Creative Commons Attribution-ShareAlike 4.0 | Share-alike |
| EUPL-1.2 | European Union Public License 1.2 | Copyleft, jurisdiction-specific |

### Red Bucket (requires explicit legal review — do NOT auto-ingest)

These licenses impose strong copyleft obligations, commercial restrictions, or have terms that
may conflict with AI training use. **No code in this bucket enters the corpus without explicit
written legal approval.**

| SPDX ID | Common Name | Reason |
|---------|-------------|--------|
| GPL-2.0-only | GNU GPL v2 | Strong copyleft |
| GPL-2.0-or-later | GNU GPL v2+ | Strong copyleft |
| GPL-3.0-only | GNU GPL v3 | Strong copyleft |
| GPL-3.0-or-later | GNU GPL v3+ | Strong copyleft |
| AGPL-3.0-only | GNU AGPL v3 | Network copyleft |
| AGPL-3.0-or-later | GNU AGPL v3+ | Network copyleft |
| LGPL-2.0-only | GNU LGPL v2 | Library copyleft — training use uncertain |
| LGPL-2.1-only | GNU LGPL v2.1 | Library copyleft — training use uncertain |
| LGPL-2.1-or-later | GNU LGPL v2.1+ | Library copyleft — training use uncertain |
| LGPL-3.0-only | GNU LGPL v3 | Library copyleft — training use uncertain |
| LGPL-3.0-or-later | GNU LGPL v3+ | Library copyleft — training use uncertain |
| SSPL-1.0 | Server Side Public License | Extremely broad copyleft |
| Commons-Clause | Commons Clause addendum | Commercial restrictions |
| BUSL-1.1 | Business Source License 1.1 | Delayed open-source; production restrictions |

### Unknown (fail-closed — do NOT ingest)

If no license can be detected, the code is treated as if it has unknown license obligations and
is **not** ingested. This is the fail-closed default.

---

## Detection Priority

The license detector checks in this order:

1. **SPDX-License-Identifier** header in the source file (highest confidence)
2. **LICENSE / COPYING** file in the repository root (high confidence)
3. **package.json** `license` field (high confidence)
4. **setup.py / setup.cfg / pyproject.toml** `license` field (high confidence)
5. **pom.xml** `<licenses><license><name>` (high confidence)
6. **build.gradle / build.gradle.kts** license field (medium confidence)
7. **README** license section (low confidence — may be inaccurate)

---

## Provenance Requirements

Every corpus record must include:

- `source_benchmark`: The benchmark or repository collection it came from
- `task_id`: Unique identifier for this specific task/instance
- `input_hash`: SHA-256 hash of the input (failing code state)
- `output_hash`: SHA-256 hash of the output (repair patch)
- `schema_version`: `"determinex-agent-trace-v1"` — schema for this record format
- `_sig`: HMAC-BLAKE2b-256 signature over canonical JSON of all fields

---

## Secret Scanning

Before any code enters the corpus pipeline:

1. The file is scanned for 16 categories of secrets:
   - LLM API keys (Anthropic `sk-ant-*`, OpenAI `sk-*`)
   - Cloud keys (AWS `AKIA*`, GCP service account JSON, AWS secret key)
   - VCS tokens (GitHub `ghp_*`, `gho_*`, `ghs_*`)
   - Service tokens (Slack `xox*`, Stripe `sk_live_*`, Twilio `AC*`)
   - Private keys (RSA PEM, PGP private key block)
   - JWT tokens
   - Database URLs with embedded credentials
   - Generic API key/token/password variable assignments

2. Any single finding causes the **entire file** to be rejected, not just the line.
   (Redaction is for screenshots. Secrets in code mean the file is suspect.)

3. Obvious placeholders and documentation examples are excluded from scanning
   (comment lines, `YOUR_API_KEY_HERE`, `EXAMPLE` as a standalone word, etc.)

---

## Java Corpus Strategy

Java repair tasks are extracted via mutation-based testing:

1. Index Maven/Gradle projects meeting license requirements
2. Identify null-check and guard candidates
3. Apply controlled mutations (remove null check → expect NPE)
4. Run test suite — confirm failure
5. Restore original code — confirm pass
6. Record the `(mutated, test_failure, repair)` triple
7. Write signed corpus record via `CorpusManager`

No raw Java code from the internet enters the corpus directly. Only the
**verified failure → verified repair** pair is stored, with full provenance.

---

## Enforcement

The license policy is enforced at multiple levels:

1. **Code gate** (`license_detector.py` + `spdx_normalizer.py`): runtime check on every file
2. **Test suite** (`tests/corpus/`): 40+ tests covering all license categories and detection methods
3. **Static enforcement** (`tests/test_no_raw_corpus_writes.py`): no code path can bypass CorpusManager
4. **Lock manifest** (`locks/sentinel/CORPUS_LICENSE_LOCK_001.json`): test-enforced freeze

---

## Policy Exceptions

Exceptions require written approval from the project owner (Ryan Gurganious)
and must be recorded in `assurance/security/license_exception_log.json` with:
- Date of approval
- SPDX ID and rationale
- Legal reviewer name
- Scope (specific files, not blanket exception)

---

*See also: `docs/SUPPLY_CHAIN_SECURITY.md`, `assurance/controls/control_matrix.json`*
