---
name: swebench-projectlombok__lombok
description: SWE-bench repo behavioral spec for projectlombok/lombok. Aggregated from 17 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# projectlombok/lombok — SWE-bench Repo Spec

> **17 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 17 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/core/lombok/javac/handlers/HandleSuperBuilder.java` | 5 |
| `src/core/lombok/javac/handlers/JavacHandlerUtil.java` | 4 |
| `src/core/lombok/eclipse/handlers/EclipseHandlerUtil.java` | 3 |
| `src/core/lombok/javac/handlers/HandleBuilder.java` | 2 |
| `src/core/lombok/eclipse/handlers/HandleSuperBuilder.java` | 2 |
| `src/core/lombok/javac/handlers/HandleExtensionMethod.java` | 2 |
| `src/core/lombok/javac/handlers/HandleVal.java` | 1 |
| `src/core/lombok/eclipse/handlers/HandleFieldDefaults.java` | 1 |
| `src/core/lombok/javac/handlers/HandleFieldDefaults.java` | 1 |
| `src/stubs/com/sun/tools/javac/code/Symbol.java` | 1 |
| `src/core/lombok/javac/handlers/HandleUtilityClass.java` | 1 |
| `src/core/lombok/ConfigurationKeys.java` | 1 |
| `src/core/lombok/core/configuration/NullAnnotationLibrary.java` | 1 |
| `src/core/lombok/core/handlers/HandlerUtil.java` | 1 |
| `website/templates/features/configuration.html` | 1 |
| `src/core/lombok/javac/handlers/HandleNonNull.java` | 1 |
| `src/core/lombok/eclipse/handlers/HandleNonNull.java` | 1 |
| `src/core/lombok/javac/handlers/HandleHelper.java` | 1 |
| `src/core/lombok/eclipse/handlers/HandleBuilder.java` | 1 |
| `src/core/lombok/javac/JavacNode.java` | 1 |
| `src/core/lombok/eclipse/EclipseNode.java` | 1 |
| `src/core/lombok/bytecode/SneakyThrowsRemover.java` | 1 |
| `AUTHORS` | 1 |
| `src/core/lombok/bytecode/PreventNullAnalysisRemover.java` | 1 |
| `src/core/lombok/bytecode/FixedClassWriter.java` | 1 |
| `src/core/lombok/eclipse/handlers/HandleStandardException.java` | 1 |
| `src/core/lombok/javac/handlers/HandleStandardException.java` | 1 |
| `doc/changelog.markdown` | 1 |

## Section 3 — Test framework signal

Detected: **Go test (TestName)**

Sample FAIL_TO_PASS test names (first 10):
```
  javac-ValInLambda.java(lombok.transform.TestWithDelombok)
  javac-FieldDefaultsViaConfigOnRecord.java(lombok.transform.TestWithDelombok)
  javac-OnXJava8Style.java(lombok.transform.TestWithDelombok)
  javac-BuilderDefaultsTargetTyping.java(lombok.transform.TestWithDelombok)
  javac-SuperBuilderWithDefaultsAndTargetTyping.java(lombok.transform.TestWithDelombok)
  javac-SuperBuilderNameClashes.java(lombok.transform.TestWithDelombok)
  javac-ExtensionMethodNonStatic.java(lombok.transform.TestWithDelombok)
  javac-UtilityClassGeneric.java(lombok.transform.TestWithDelombok)
  javac-NullLibrary3.java(lombok.transform.TestWithDelombok)
  javac-NonNullOnRecordTypeUse.java(lombok.transform.TestWithDelombok)
```

## Section 4 — Problem-theme distribution

Top themes across 17 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| import_module | 4 | 23.5% |
| crash_or_traceback | 3 | 17.6% |
| documentation | 3 | 17.6% |
| wrong_output | 2 | 11.8% |
| other | 2 | 11.8% |
| concurrency | 1 | 5.9% |
| config_environment | 1 | 5.9% |
| performance | 1 | 5.9% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `projectlombok__lombok-2792`

**Files likely affected**: `src/core/lombok/javac/handlers/HandleVal.java`
**FAIL_TO_PASS** (1 tests, first 3): `['javac-ValInLambda.java(lombok.transform.TestWithDelombok)']`

**Problem statement (excerpt):**
> [BUG] @val raises "Type cannot be resolved" on generic code **Describe the bug**
 
 '''
 .../LombokValTest.java:43: error: Cannot use 'val' here because initializer expression does not have a representable type: Type cannot be resolved
                 val decrypted = decipher.doFinal(encrypted);
 '''
 
 **To Reproduce**
 
 '''java
 package prodist.java.sts;
 
 import static org.junit.jupiter.api.

### Sample 2 — `projectlombok__lombok-3009`

**Files likely affected**: `src/core/lombok/eclipse/handlers/HandleFieldDefaults.java`, `src/core/lombok/javac/handlers/HandleFieldDefaults.java`
**FAIL_TO_PASS** (1 tests, first 3): `['javac-FieldDefaultsViaConfigOnRecord.java(lombok.transform.TestWithDelombok)']`

**Problem statement (excerpt):**
> [BUG] lombok.fieldDefaults.default* errors with records **Describe the bug**
 When 'lombok.config' is specified with 'lombok.fieldDefaults.defaultPrivate = true' and/or 'lombok.fieldDefaults.defaultFinal = true' compilation fails with the following: 
 
 'error: @FieldDefaults is only supported on a class or an enum.'
 
 **To Reproduce**
 
 'lombok.config':
 '''
 lombok.fieldDefaults.defaultPrivate

### Sample 3 — `projectlombok__lombok-3042`

**Files likely affected**: `src/core/lombok/eclipse/handlers/EclipseHandlerUtil.java`, `src/core/lombok/javac/handlers/JavacHandlerUtil.java`
**FAIL_TO_PASS** (1 tests, first 3): `['javac-OnXJava8Style.java(lombok.transform.TestWithDelombok)']`

**Problem statement (excerpt):**
> [BUG] Adding an annotation that takes an array argument to a generated constructor results in NPE during compilation on 1.18.22 **Describe the bug**
 Adding an annotation that takes an array argument to a generated constructor results in NPE during compilation
 
 **To Reproduce**
 Compiling the following test class
 '''
 import lombok.AllArgsConstructor;
 
 @AllArgsConstructor(onConstructor_ = @An

### Sample 4 — `projectlombok__lombok-3052`

**Files likely affected**: `src/core/lombok/javac/handlers/HandleBuilder.java`, `src/core/lombok/javac/handlers/HandleSuperBuilder.java`
**FAIL_TO_PASS** (2 tests, first 3): `['javac-BuilderDefaultsTargetTyping.java(lombok.transform.TestWithDelombok)', 'javac-SuperBuilderWithDefaultsAndTargetTyping.java(lombok.transform.TestWithDelombok)']`

**Problem statement (excerpt):**
> [BUG] Using @Builder.Default with Java 11 may lead to wrong generic type **Describe the bug**
 When trying to compile a class annotated with '@Builder' and a '@Builder.Default' value, its types cannot be determined correctly which causes an error for the compiler.
 
 This issue occurs within Java 11 but not Java 8.
 
 **To Reproduce**
 The following code cannot be compiled.
 '''MyTest.java
 import

### Sample 5 — `projectlombok__lombok-3215`

**Files likely affected**: `src/core/lombok/eclipse/handlers/HandleSuperBuilder.java`, `src/core/lombok/javac/handlers/HandleSuperBuilder.java`
**FAIL_TO_PASS** (1 tests, first 3): `['javac-SuperBuilderNameClashes.java(lombok.transform.TestWithDelombok)']`

**Problem statement (excerpt):**
> [BUG] @SuperBuilder compilation issue **Describe the bug**
 
 I faced strange issue when Lombok failed to compile the code with the error: "The constructor B(A.ABuilder<capture#1-of ?,capture#2-of ?>) is undefined"
 
 **To Reproduce**
 
 '''
 @SuperBuilder
 class A extends B {}
 
 @SuperBuilder
 @Getter
 class B {
 	private final int a ;
 }
 '''
 
 However if I rename B to B1 then everything works

### Sample 6 — `projectlombok__lombok-3312`

**Files likely affected**: `src/core/lombok/javac/handlers/HandleExtensionMethod.java`
**FAIL_TO_PASS** (1 tests, first 3): `['javac-ExtensionMethodNonStatic.java(lombok.transform.TestWithDelombok)']`

**Problem statement (excerpt):**
> [BUG] ExtensionMethod transforms unrelated method call **Describe the bug**
 When using the ExtensionMethod feature, unrelated method calls are processed, resulting in unwanted behaviour.
 
 **To Reproduce**
 A minimal example for reproducing this issue is:
 '''java
 import lombok.experimental.ExtensionMethod;
 
 @ExtensionMethod({java.lang.String.class, Bug.Extension.class})
 public class Bug {
 

### Sample 7 — `projectlombok__lombok-3326`

**Files likely affected**: `src/stubs/com/sun/tools/javac/code/Symbol.java`, `src/core/lombok/javac/handlers/HandleUtilityClass.java`
**FAIL_TO_PASS** (1 tests, first 3): `['javac-UtilityClassGeneric.java(lombok.transform.TestWithDelombok)']`

**Problem statement (excerpt):**
> [BUG] UtilityClass with generics produces NullPointerException in Javac **Describe the bug**
 
 '@UtilityClass' together with a generic method and two methods of the same name causes Javac to crash with NPE in Java 11, 17, 18 and 19 but not 8 (not tested others).
 
 There are a lot of small changes that make the code compile:
 
 * 'static' is added to the inner class 'DTO';
 * one of the 'convert'

### Sample 8 — `projectlombok__lombok-3350`

**Files likely affected**: `src/core/lombok/ConfigurationKeys.java`, `src/core/lombok/core/configuration/NullAnnotationLibrary.java`, `src/core/lombok/core/handlers/HandlerUtil.java`, `website/templates/features/configuration.html`
**FAIL_TO_PASS** (1 tests, first 3): `['javac-NullLibrary3.java(lombok.transform.TestWithDelombok)']`

**Problem statement (excerpt):**
> [FEATURE]  Support Jakarta Nonnull/Nullable annotations I ran into an issue with using Jakarta's '@Nullable' instead of javax (or checker).
 
 I tried to add the config property :
 '''
 lombok.addNullAnnotations = CUSTOM:jakarta.annotation.Nonnull:jakarta.annotation.Nullable
 '''
 
 And it seems to partially work (e.g. for return values), but when using '@Builder' the  '@Nullable' is not copied to

## Section 6 — Builder guidance

When building a fix for an instance in projectlombok/lombok:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/core/lombok/javac/handlers/HandleSuperBuilder.java appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 17 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "projectlombok/lombok"`).

First 20 instance_ids:

- `projectlombok__lombok-2792` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3009` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3042` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3052` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3215` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3312` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3326` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3350` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3371` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3422` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3479` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3486` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3571` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3594` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3602` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3674` (dataset: `swe-bench-multilingual-test`)
- `projectlombok__lombok-3697` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
