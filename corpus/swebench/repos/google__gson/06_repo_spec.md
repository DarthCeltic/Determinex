---
name: swebench-google__gson
description: SWE-bench repo behavioral spec for google/gson. Aggregated from 14 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# google/gson — SWE-bench Repo Spec

> **14 bug-fix instances** across 2 dataset(s); language(s): java, python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 9 |
| multi-swe-bench | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `gson/src/main/java/com/google/gson/internal/bind/JsonTreeReader.java` | 2 |
| `gson/src/main/java/com/google/gson/stream/JsonWriter.java` | 2 |
| `gson/src/main/java/com/google/gson/Gson.java` | 2 |
| `gson/src/main/java/com/google/gson/internal/bind/TreeTypeAdapter.java` | 2 |
| `gson/src/main/java/com/google/gson/DefaultDateTypeAdapter.java` | 1 |
| `gson/src/main/java/com/google/gson/FieldNamingPolicy.java` | 1 |
| `gson/src/main/java/com/google/gson/stream/JsonReader.java` | 1 |
| `gson/src/main/java/com/google/gson/internal/bind/util/ISO8601Utils.java` | 1 |
| `gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java` | 1 |
| `gson/src/main/java/com/google/gson/JsonPrimitive.java` | 1 |
| `gson/src/main/java/com/google/gson/GsonBuilder.java` | 1 |
| `UserGuide.md` | 1 |
| `gson/src/main/java/com/google/gson/internal/bind/TypeAdapterRuntimeTypeWrapper.java` | 1 |
| `gson/src/main/java/com/google/gson/internal/bind/SerializationDelegatingTypeAdapter.java` | 1 |
| `gson/src/main/java/com/google/gson/internal/Streams.java` | 1 |
| `gson/src/main/java/com/google/gson/internal/bind/JsonAdapterAnnotationTypeAdapterFactory.java` | 1 |
| `gson/src/main/java/com/google/gson/internal/$Gson$Types.java` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: com.google.gson.internal.bind.JsonTreeReaderTest#testSkipValue_emptyJsonObject, com.google.gson.internal.bind.JsonTreeReaderTest#testSkipValue_filledJsonObject, com.google.gson.stream.JsonWriterTest#testNonFiniteDoublesWhenLenient, com.google.gson.DefaultDateTypeAdapterTest#testNullValue, com.google.gson.functional.FieldNamingTest#testUpperCaseWithUnderscores**

Sample FAIL_TO_PASS test names (first 10):
```
  com.google.gson.internal.bind.JsonTreeReaderTest#testSkipValue_emptyJsonObject
  com.google.gson.internal.bind.JsonTreeReaderTest#testSkipValue_filledJsonObject
  com.google.gson.stream.JsonWriterTest#testNonFiniteDoublesWhenLenient
  com.google.gson.DefaultDateTypeAdapterTest#testNullValue
  com.google.gson.functional.FieldNamingTest#testUpperCaseWithUnderscores
  com.google.gson.functional.NamingPolicyTest#testGsonWithUpperCaseUnderscorePolicySerialization
  com.google.gson.functional.NamingPolicyTest#testGsonWithUpperCaseUnderscorePolicyDeserialiation
  com.google.gson.stream.JsonReaderTest#testHasNextEndOfDocument
  com.google.gson.internal.bind.JsonTreeReaderTest#testHasNext_endOfDocument
  com.google.gson.internal.bind.util.ISO8601UtilsTest#testDateParseInvalidDay
```

## Section 4 — Problem-theme distribution

Top themes across 14 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| crash_or_traceback | 5 | 55.6% |
| other | 1 | 11.1% |
| documentation | 1 | 11.1% |
| json_serialization | 1 | 11.1% |
| wrong_output | 1 | 11.1% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `google__gson-1014`

**Files likely affected**: `gson/src/main/java/com/google/gson/internal/bind/JsonTreeReader.java`
**FAIL_TO_PASS** (2 tests, first 3): `['com.google.gson.internal.bind.JsonTreeReaderTest#testSkipValue_emptyJsonObject', 'com.google.gson.internal.bind.JsonTreeReaderTest#testSkipValue_filledJsonObject']`

**Problem statement (excerpt):**
> Bug when skipping a value while using the JsonTreeReader When using a 'JsonReader' to read a JSON object, 'skipValue()' skips the structure successfully.
 '''Java
 @Test
 public void testSkipValue_JsonReader() throws IOException {
   try (JsonReader in = new JsonReader(new StringReader("{}"))) {
     in.skipValue();
   }
 }
 '''
 But when using a 'JsonTreeReader' to read a JSON object, 'skipValue(

### Sample 2 — `google__gson-1093`

**Files likely affected**: `gson/src/main/java/com/google/gson/stream/JsonWriter.java`
**FAIL_TO_PASS** (1 tests, first 3): `['com.google.gson.stream.JsonWriterTest#testNonFiniteDoublesWhenLenient']`

**Problem statement (excerpt):**
> JsonWriter#value(java.lang.Number) can be lenient, but JsonWriter#value(double) can't, In lenient mode, JsonWriter#value(java.lang.Number) can write pseudo-numeric values like 'NaN', 'Infinity', '-Infinity':
 '''java
     if (!lenient
         && (string.equals("-Infinity") || string.equals("Infinity") || string.equals("NaN"))) {
       throw new IllegalArgumentException("Numeric values must be fi

### Sample 3 — `google__gson-1100`

**Files likely affected**: `gson/src/main/java/com/google/gson/DefaultDateTypeAdapter.java`
**FAIL_TO_PASS** (1 tests, first 3): `['com.google.gson.DefaultDateTypeAdapterTest#testNullValue']`

**Problem statement (excerpt):**
> call new GsonBuilder().setDateFormat("yyyy-MM-dd").create().toJson exception.[2.8.1] when a pojo object with null-value field and use "GsonBuilder().setDateFormat("yyyy-MM-dd")",will throw exception.
 
 code:
 //data class
 class Person{
   private Date age;
   //getter setter
 }
 
 //demo
 Gson gson = new GsonBuilder().setDateFormat("yyyy-MM-dd").create();
 Person p = new Person(); //age is null

### Sample 4 — `google__gson-2024`

**Files likely affected**: `gson/src/main/java/com/google/gson/FieldNamingPolicy.java`
**FAIL_TO_PASS** (3 tests, first 3): `['com.google.gson.functional.FieldNamingTest#testUpperCaseWithUnderscores', 'com.google.gson.functional.NamingPolicyTest#testGsonWithUpperCaseUnderscorePolicySerialization', 'com.google.gson.functional.NamingPolicyTest#testGsonWithUpperCaseUnderscorePolicyDeserialiation']`

**Problem statement (excerpt):**
> New FieldNamingPolicy: UPPER_CASE_WITH_UNDERSCORES Hi,
 
 currently, I do try to integrate a service that uses a UPPER_CASE_WITH_UNDERSCORES naming scheme for their field names, e.g.:
 
 '''
 {
   "PRODUCT_LIST" : {
     "PRODUCT" : [
       {
       "APPLICATION_CODE" : "secret application code",
       "PRODUCT_TYPE" : "product type value",
       "PRODUCT_NAME" : "product name"
       }
     ]

### Sample 5 — `google__gson-2061`

**Files likely affected**: `gson/src/main/java/com/google/gson/stream/JsonReader.java`, `gson/src/main/java/com/google/gson/internal/bind/JsonTreeReader.java`
**FAIL_TO_PASS** (2 tests, first 3): `['com.google.gson.stream.JsonReaderTest#testHasNextEndOfDocument', 'com.google.gson.internal.bind.JsonTreeReaderTest#testHasNext_endOfDocument']`

**Problem statement (excerpt):**
> JsonReader.hasNext() returns true at END_DOCUMENT JsonReader.hasNext() will return true if we are at the end of the document 
 (reader.peek() == JsonToken.END_DOCUMENT) 

### Sample 6 — `google__gson-2134`

**Files likely affected**: `gson/src/main/java/com/google/gson/internal/bind/util/ISO8601Utils.java`
**FAIL_TO_PASS** (2 tests, first 3): `['com.google.gson.internal.bind.util.ISO8601UtilsTest#testDateParseInvalidDay', 'com.google.gson.internal.bind.util.ISO8601UtilsTest#testDateParseInvalidMonth']`

**Problem statement (excerpt):**
> ISO8061Utils.parse() accepts non-existent dates # Gson version
 2.9.0
 
 # Java / Android version
 ''' 
 java 16 2021-03-16
 Java(TM) SE Runtime Environment (build 16+36-2231)
 Java HotSpot(TM) 64-Bit Server VM (build 16+36-2231, mixed mode, sharing)
 '''
 
 # Description
 Apparently 'ISO8061Utils.parse()' works in a very lenient manner when dealing with dates that do not exist (for instance '2022

### Sample 7 — `google__gson-2158`

**Files likely affected**: `gson/src/main/java/com/google/gson/Gson.java`, `gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java`
**FAIL_TO_PASS** (6 tests, first 3): `['com.google.gson.functional.PrimitiveTest#testByteSerialization', 'com.google.gson.functional.PrimitiveTest#testShortSerialization', 'com.google.gson.functional.PrimitiveTest#testIntSerialization']`

**Problem statement (excerpt):**
> Primitive type adapters don't perform numeric conversion during serialization # Gson version
 2.9.0
 
 # Java / Android version
 Java 17
 
 # Description
 The built-in adapters for primitive types don't perform numeric conversion for serialization. This is most obvious when using Gson's non-typesafe method 'Gson.toJson(Object, Type)':
 '''java
 System.out.println(new Gson().toJson(1.5, byte.class)

### Sample 8 — `google__gson-2311`

**Files likely affected**: `gson/src/main/java/com/google/gson/JsonPrimitive.java`
**FAIL_TO_PASS** (1 tests, first 3): `['com.google.gson.JsonPrimitiveTest#testEqualsIntegerAndBigInteger']`

**Problem statement (excerpt):**
> JsonPrimitive#equals Method behaves incorrect when used with BigInteger # Gson version
 2.9.0
 
 
 # Java / Android version
 Eclipse Adoptium OpenJDK 64-Bit Server VM 17.0.2+8 on Linux
 
 
 # Used tools
 - [ ] Maven; version: 
 - [x] Gradle; version: 7.3.3
 - [ ] ProGuard (attach the configuration file please); version: 
 - [ ] ...
 
 # Description
 Two 'JsonPrimitive's with 'BigInteger' values re

## Section 6 — Builder guidance

When building a fix for an instance in google/gson:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. gson/src/main/java/com/google/gson/internal/bind/JsonTreeReader.java appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 14 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "google/gson"`).

First 20 instance_ids:

- `google__gson-1014` (dataset: `swe-bench-multilingual-test`)
- `google__gson-1093` (dataset: `swe-bench-multilingual-test`)
- `google__gson-1100` (dataset: `swe-bench-multilingual-test`)
- `google__gson-2024` (dataset: `swe-bench-multilingual-test`)
- `google__gson-2061` (dataset: `swe-bench-multilingual-test`)
- `google__gson-2134` (dataset: `swe-bench-multilingual-test`)
- `google__gson-2158` (dataset: `swe-bench-multilingual-test`)
- `google__gson-2311` (dataset: `swe-bench-multilingual-test`)
- `google__gson-2479` (dataset: `swe-bench-multilingual-test`)
- `google__gson-1787` (dataset: `multi-swe-bench`)
- `google__gson-1703` (dataset: `multi-swe-bench`)
- `google__gson-1555` (dataset: `multi-swe-bench`)
- `google__gson-1391` (dataset: `multi-swe-bench`)
- `google__gson-1093` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
