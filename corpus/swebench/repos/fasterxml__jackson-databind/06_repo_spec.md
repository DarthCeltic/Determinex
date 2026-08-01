---
name: swebench-fasterxml__jackson-databind
description: SWE-bench repo behavioral spec for fasterxml/jackson-databind. Aggregated from 42 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# fasterxml/jackson-databind — SWE-bench Repo Spec

> **42 bug-fix instances** across 1 dataset(s); language(s): java.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 42 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `release-notes/VERSION-2.x` | 24 |
| `src/main/java/com/fasterxml/jackson/databind/introspect/POJOPropertiesCollector.java` | 4 |
| `release-notes/CREDITS-2.x` | 4 |
| `src/main/java/com/fasterxml/jackson/databind/node/ObjectNode.java` | 3 |
| `src/main/java/com/fasterxml/jackson/databind/ObjectMapper.java` | 3 |
| `src/main/java/com/fasterxml/jackson/databind/AnnotationIntrospector.java` | 2 |
| `src/main/java/com/fasterxml/jackson/databind/introspect/AnnotationIntrospectorPair.java` | 2 |
| `src/main/java/com/fasterxml/jackson/databind/deser/std/ThrowableDeserializer.java` | 2 |
| `src/main/java/com/fasterxml/jackson/databind/deser/BeanDeserializerBase.java` | 2 |
| `src/main/java/com/fasterxml/jackson/databind/deser/BeanDeserializer.java` | 2 |
| `src/main/java/com/fasterxml/jackson/databind/JsonNode.java` | 2 |
| `src/main/java/com/fasterxml/jackson/databind/cfg/CoercionConfigs.java` | 2 |
| `src/main/java/com/fasterxml/jackson/databind/DeserializationFeature.java` | 2 |
| `src/main/java/com/fasterxml/jackson/databind/jsontype/impl/StdTypeResolverBuilder.java` | 2 |
| `src/main/java/com/fasterxml/jackson/databind/deser/std/FactoryBasedEnumDeserializer.java` | 2 |
| `src/main/java/com/fasterxml/jackson/databind/deser/std/StdDeserializer.java` | 2 |
| `src/main/java/com/fasterxml/jackson/databind/deser/BeanDeserializerFactory.java` | 1 |
| `src/main/java/com/fasterxml/jackson/databind/introspect/PotentialCreator.java` | 1 |
| `src/main/java/com/fasterxml/jackson/databind/type/TypeFactory.java` | 1 |
| `src/main/java/com/fasterxml/jackson/databind/deser/std/EnumDeserializer.java` | 1 |
| `src/main/java/com/fasterxml/jackson/databind/deser/impl/FieldProperty.java` | 1 |
| `src/main/java/com/fasterxml/jackson/databind/deser/impl/MethodProperty.java` | 1 |
| `src/main/java/com/fasterxml/jackson/databind/ext/CoreXMLDeserializers.java` | 1 |
| `src/main/java/com/fasterxml/jackson/databind/deser/std/FromStringDeserializer.java` | 1 |
| `src/main/java/com/fasterxml/jackson/databind/PropertyName.java` | 1 |
| `src/main/java/com/fasterxml/jackson/databind/util/EnumValues.java` | 1 |
| `src/main/java/com/fasterxml/jackson/databind/ser/std/ReferenceTypeSerializer.java` | 1 |
| `src/main/java/com/fasterxml/jackson/databind/deser/std/CollectionDeserializer.java` | 1 |
| `src/main/java/com/fasterxml/jackson/databind/jsontype/impl/TypeNameIdResolver.java` | 1 |
| `src/main/java/com/fasterxml/jackson/databind/jsontype/impl/ClassNameIdResolver.java` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 42 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in fasterxml/jackson-databind:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. release-notes/VERSION-2.x appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 42 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "fasterxml/jackson-databind"`).

First 20 instance_ids:

- `fasterxml__jackson-databind-4641` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4615` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4487` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4486` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4469` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4468` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4426` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4365` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4360` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4338` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4325` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4320` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4311` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4304` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4257` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4230` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4228` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4219` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4189` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-databind-4186` (dataset: `multi-swe-bench`)
- ... (22 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
