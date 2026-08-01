---
name: swebench-googlecontainertools__jib
description: SWE-bench repo behavioral spec for googlecontainertools/jib. Aggregated from 5 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# googlecontainertools/jib — SWE-bench Repo Spec

> **5 bug-fix instances** across 1 dataset(s); language(s): java.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `jib-maven-plugin/CHANGELOG.md` | 2 |
| `jib-cli/src/main/java/com/google/cloud/tools/jib/cli/jar/JarFiles.java` | 1 |
| `docs/google-cloud-build.md` | 1 |
| `jib-gradle-plugin/README.md` | 1 |
| `jib-plugins-common/src/main/java/com/google/cloud/tools/jib/plugins/common/PluginConfigurationProcessor.java` | 1 |
| `jib-maven-plugin/README.md` | 1 |
| `jib-core/src/main/java/com/google/cloud/tools/jib/registry/RegistryAuthenticator.java` | 1 |
| `jib-core/src/main/java/com/google/cloud/tools/jib/registry/RegistryEndpointCaller.java` | 1 |
| `jib-core/src/main/java/com/google/cloud/tools/jib/registry/credentials/DockerConfigCredentialRetriever.java` | 1 |
| `jib-core/CHANGELOG.md` | 1 |
| `jib-gradle-plugin/CHANGELOG.md` | 1 |
| `jib-maven-plugin/src/main/java/com/google/cloud/tools/jib/maven/MavenProjectProperties.java` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 5 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in googlecontainertools/jib:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. jib-maven-plugin/CHANGELOG.md appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 5 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "googlecontainertools/jib"`).

First 20 instance_ids:

- `googlecontainertools__jib-4144` (dataset: `multi-swe-bench`)
- `googlecontainertools__jib-4035` (dataset: `multi-swe-bench`)
- `googlecontainertools__jib-2542` (dataset: `multi-swe-bench`)
- `googlecontainertools__jib-2536` (dataset: `multi-swe-bench`)
- `googlecontainertools__jib-2688` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
