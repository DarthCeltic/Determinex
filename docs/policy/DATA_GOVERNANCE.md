# Data Governance

Determinex training data must be verdict-rich, provenance-aware, and signed.

## Accepted Corpus Shape

```text
task
context
attempt
verifier result
failure class
repair
final verifier result
diff
language
tools used
signature
```

## Source Intake

Raw source is not training data. Source may be used to generate verifier-backed
repair tasks only after license, secret, malware, dedupe, and quality gates
pass.

## Storage

Corpus storage defaults to `T:/determinex_corpus`. C drive is not the artifact
store for large benchmark, corpus, or model data.
