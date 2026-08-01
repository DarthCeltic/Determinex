---
name: swebench-mockito__mockito
description: SWE-bench repo behavioral spec for mockito/mockito. Aggregated from 6 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# mockito/mockito — SWE-bench Repo Spec

> **6 bug-fix instances** across 1 dataset(s); language(s): java.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 6 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/main/java/org/mockito/internal/creation/bytebuddy/InlineDelegateByteBuddyMockMaker.java` | 3 |
| `src/main/java/org/mockito/internal/configuration/plugins/DefaultMockitoPlugins.java` | 2 |
| `src/main/java/org/mockito/internal/framework/DisabledMockHandler.java` | 1 |
| `src/main/java/org/mockito/MockitoFramework.java` | 1 |
| `src/main/java/org/mockito/plugins/InlineMockMaker.java` | 1 |
| `src/main/java/org/mockito/exceptions/misusing/DisabledMockException.java` | 1 |
| `src/main/java/org/mockito/internal/creation/settings/CreationSettings.java` | 1 |
| `src/main/java/org/mockito/mock/MockType.java` | 1 |
| `src/main/java/org/mockito/internal/creation/MockSettingsImpl.java` | 1 |
| `src/main/java/org/mockito/internal/configuration/plugins/Plugins.java` | 1 |
| `src/main/java/org/mockito/internal/MockitoCore.java` | 1 |
| `src/main/java/org/mockito/internal/util/MockNameImpl.java` | 1 |
| `src/main/java/org/mockito/plugins/DoNotMockEnforcer.java` | 1 |
| `src/main/java/org/mockito/internal/configuration/plugins/PluginRegistry.java` | 1 |
| `src/main/java/org/mockito/plugins/DoNotMockEnforcerWithType.java` | 1 |
| `src/main/java/org/mockito/mock/MockCreationSettings.java` | 1 |
| `subprojects/junit-jupiter/src/main/java/org/mockito/junit/jupiter/resolver/CompositeParameterResolver.java` | 1 |
| `src/main/java/org/mockito/Captor.java` | 1 |
| `src/main/java/org/mockito/internal/configuration/CaptorAnnotationProcessor.java` | 1 |
| `src/main/java/org/mockito/internal/util/reflection/GenericMaster.java` | 1 |
| `subprojects/junit-jupiter/src/main/java/org/mockito/junit/jupiter/resolver/CaptorParameterResolver.java` | 1 |
| `subprojects/junit-jupiter/src/main/java/org/mockito/junit/jupiter/resolver/MockParameterResolver.java` | 1 |
| `subprojects/junit-jupiter/src/main/java/org/mockito/junit/jupiter/MockitoExtension.java` | 1 |
| `src/main/java/org/mockito/internal/util/MockUtil.java` | 1 |
| `src/main/java/org/mockito/plugins/MockitoPlugins.java` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 6 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in mockito/mockito:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/main/java/org/mockito/internal/creation/bytebuddy/InlineDelegateByteBuddyMockMaker.java appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 6 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "mockito/mockito"`).

First 20 instance_ids:

- `mockito__mockito-3424` (dataset: `multi-swe-bench`)
- `mockito__mockito-3220` (dataset: `multi-swe-bench`)
- `mockito__mockito-3173` (dataset: `multi-swe-bench`)
- `mockito__mockito-3167` (dataset: `multi-swe-bench`)
- `mockito__mockito-3133` (dataset: `multi-swe-bench`)
- `mockito__mockito-3129` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
