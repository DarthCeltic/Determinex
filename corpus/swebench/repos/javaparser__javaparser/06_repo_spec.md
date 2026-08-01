---
name: swebench-javaparser__javaparser
description: SWE-bench repo behavioral spec for javaparser/javaparser. Aggregated from 2 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# javaparser/javaparser — SWE-bench Repo Spec

> **2 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 2 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `javaparser-core/src/main/java/com/github/javaparser/ast/Node.java` | 1 |
| `javaparser-symbol-solver-core/src/main/java/com/github/javaparser/symbolsolver/javaparsermodel/TypeExtractor.java` | 1 |

## Section 3 — Test framework signal

Detected: **Java/JUnit (TestClass.testMethod)**

Sample FAIL_TO_PASS test names (first 10):
```
  NodeTest
  Issue4560Test
```

## Section 4 — Problem-theme distribution

Top themes across 2 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| regression | 1 | 50.0% |
| other | 1 | 50.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `javaparser__javaparser-4538`

**Files likely affected**: `javaparser-core/src/main/java/com/github/javaparser/ast/Node.java`
**FAIL_TO_PASS** (1 tests, first 3): `['NodeTest']`

**Problem statement (excerpt):**
> Node.PostOrderIterator broken for root without children The Node.PostOrderIterator does not check if the root has children before peeking.
 
 Example:
 '''java
 var root = new CompilationUnit();
 var nodes = root.findAll(Node.class, TreeTraversal.PREORDER);
 nodes.stream().map(Node::getClass).forEach(System.out::println);
 '''
 Throws:
 '''
 Exception in thread "main" java.util.EmptyStackException

### Sample 2 — `javaparser__javaparser-4561`

**Files likely affected**: `javaparser-symbol-solver-core/src/main/java/com/github/javaparser/symbolsolver/javaparsermodel/TypeExtractor.java`
**FAIL_TO_PASS** (1 tests, first 3): `['Issue4560Test']`

**Problem statement (excerpt):**
> Does not solve 'String.format' on multiline strings. Hello. I think I've found a bug with the Java method resolution where it can't solve the 'String.format' method on multi-line strings.
 
 Here's a minimal working example.
 
 - I'm on Java 21 and I'm using 'com.github.javaparser:javaparser-symbol-solver-core:3.26.2'.
 
 Two files:
 '''java
 package my.example;
 
 public class MyExample {
 
   pu

## Section 6 — Builder guidance

When building a fix for an instance in javaparser/javaparser:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. javaparser-core/src/main/java/com/github/javaparser/ast/Node.java appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 2 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "javaparser/javaparser"`).

First 20 instance_ids:

- `javaparser__javaparser-4538` (dataset: `swe-bench-multilingual-test`)
- `javaparser__javaparser-4561` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
