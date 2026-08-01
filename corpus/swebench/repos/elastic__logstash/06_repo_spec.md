---
name: swebench-elastic__logstash
description: SWE-bench repo behavioral spec for elastic/logstash. Aggregated from 38 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# elastic/logstash — SWE-bench Repo Spec

> **38 bug-fix instances** across 1 dataset(s); language(s): java.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 38 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `logstash-core/src/main/java/org/logstash/common/io/DeadLetterQueueWriter.java` | 14 |
| `logstash-core/src/main/java/org/logstash/common/BufferedTokenizerExt.java` | 7 |
| `logstash-core/lib/logstash/environment.rb` | 7 |
| `docs/static/settings-file.asciidoc` | 6 |
| `config/logstash.yml` | 3 |
| `docker/data/logstash/env2yaml/env2yaml.go` | 3 |
| `tools/jvm-options-parser/src/main/java/org/logstash/launchers/JvmOptionsParser.java` | 3 |
| `logstash-core/build.gradle` | 3 |
| `logstash-core/lib/logstash/agent.rb` | 3 |
| `logstash-core/src/main/java/org/logstash/ackedqueue/io/FileCheckpointIO.java` | 3 |
| `logstash-core/src/main/java/org/logstash/util/CheckedSupplier.java` | 3 |
| `logstash-core/src/main/java/org/logstash/util/ExponentialBackoff.java` | 3 |
| `build.gradle` | 3 |
| `logstash-core/src/main/java/org/logstash/log/CustomLogEventSerializer.java` | 2 |
| `docs/static/troubleshoot/ts-logstash.asciidoc` | 2 |
| `logstash-core/locales/en.yml` | 2 |
| `docs/static/running-logstash-command-line.asciidoc` | 2 |
| `logstash-core/lib/logstash/runner.rb` | 2 |
| `tools/jvm-options-parser/build.gradle` | 2 |
| `logstash-core/src/main/java/org/logstash/execution/AbstractPipelineExt.java` | 2 |
| `logstash-core/src/main/java/org/logstash/secret/password/PasswordParamConverter.java` | 2 |
| `logstash-core/lib/logstash/webserver.rb` | 2 |
| `logstash-core/src/main/java/org/logstash/secret/password/PasswordValidator.java` | 2 |
| `logstash-core/src/main/java/org/logstash/secret/password/SymbolValidator.java` | 2 |
| `logstash-core/src/main/java/org/logstash/secret/password/Validator.java` | 2 |
| `logstash-core/spec/logstash/settings_spec.rb` | 2 |
| `logstash-core/src/main/java/org/logstash/secret/password/EmptyStringValidator.java` | 2 |
| `logstash-core/src/main/java/org/logstash/secret/password/LowerCaseValidator.java` | 2 |
| `logstash-core/src/main/java/org/logstash/secret/password/DigitValidator.java` | 2 |
| `logstash-core/src/main/java/org/logstash/secret/password/LengthValidator.java` | 2 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 38 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in elastic/logstash:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. logstash-core/src/main/java/org/logstash/common/io/DeadLetterQueueWriter.java appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 38 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "elastic/logstash"`).

First 20 instance_ids:

- `elastic__logstash-17021` (dataset: `multi-swe-bench`)
- `elastic__logstash-17020` (dataset: `multi-swe-bench`)
- `elastic__logstash-17019` (dataset: `multi-swe-bench`)
- `elastic__logstash-16968` (dataset: `multi-swe-bench`)
- `elastic__logstash-16681` (dataset: `multi-swe-bench`)
- `elastic__logstash-16579` (dataset: `multi-swe-bench`)
- `elastic__logstash-16569` (dataset: `multi-swe-bench`)
- `elastic__logstash-16482` (dataset: `multi-swe-bench`)
- `elastic__logstash-16195` (dataset: `multi-swe-bench`)
- `elastic__logstash-16094` (dataset: `multi-swe-bench`)
- `elastic__logstash-16079` (dataset: `multi-swe-bench`)
- `elastic__logstash-15969` (dataset: `multi-swe-bench`)
- `elastic__logstash-15964` (dataset: `multi-swe-bench`)
- `elastic__logstash-15928` (dataset: `multi-swe-bench`)
- `elastic__logstash-15925` (dataset: `multi-swe-bench`)
- `elastic__logstash-15697` (dataset: `multi-swe-bench`)
- `elastic__logstash-15680` (dataset: `multi-swe-bench`)
- `elastic__logstash-15241` (dataset: `multi-swe-bench`)
- `elastic__logstash-15233` (dataset: `multi-swe-bench`)
- `elastic__logstash-15008` (dataset: `multi-swe-bench`)
- ... (18 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
