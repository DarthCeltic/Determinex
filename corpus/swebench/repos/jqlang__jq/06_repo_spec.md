---
name: swebench-jqlang__jq
description: SWE-bench repo behavioral spec for jqlang/jq. Aggregated from 26 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# jqlang/jq — SWE-bench Repo Spec

> **26 bug-fix instances** across 2 dataset(s); language(s): c, python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 17 |
| swe-bench-multilingual-test | 9 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/main.c` | 8 |
| `docs/content/manual/manual.yml` | 6 |
| `jq.1.prebuilt` | 5 |
| `src/builtin.c` | 5 |
| `src/parser.c` | 4 |
| `src/parser.y` | 4 |
| `src/jv.c` | 4 |
| `src/builtin.jq` | 3 |
| `src/execute.c` | 2 |
| `src/lexer.h` | 1 |
| `src/lexer.c` | 1 |
| `src/lexer.l` | 1 |
| `src/parser.h` | 1 |
| `src/compile.c` | 1 |
| `src/compile.h` | 1 |
| `src/opcode_list.h` | 1 |
| `docs/content/manual/dev/manual.yml` | 1 |
| `Makefile.am` | 1 |
| `src/jv_print.c` | 1 |
| `NEWS.md` | 1 |
| `src/jv_aux.c` | 1 |
| `src/jv.h` | 1 |
| `src/jv_type_private.h` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: tests/shtest, tests/jqtest, tests/jqtest, tests/shtest, tests/jqtest**

Sample FAIL_TO_PASS test names (first 10):
```
  tests/shtest
  tests/jqtest
  tests/jqtest
  tests/shtest
  tests/jqtest
  tests/shtest
  tests/jqtest
  tests/jqtest
  tests/shtest
```

## Section 4 — Problem-theme distribution

Top themes across 26 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| wrong_output | 4 | 44.4% |
| encoding_unicode | 1 | 11.1% |
| json_serialization | 1 | 11.1% |
| config_environment | 1 | 11.1% |
| crash_or_traceback | 1 | 11.1% |
| other | 1 | 11.1% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `jqlang__jq-2235`

**Files likely affected**: `src/main.c`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/shtest']`

**Problem statement (excerpt):**
> Add -0 command-line option It'd be nice to be able to use ASCII 'NUL' instead of 'LF' for non-raw-output mode for use with 'xargs -0' and such.  In raw output mode, of course, one can use '-j' and output '"\u0000"' as necessary.
 
 As a workaround until this is done, use raw-output mode and output raw values, but pipe all strings to 'tojson' first: 'jq -rj '... | if type=="string" then tojson else

### Sample 2 — `jqlang__jq-2598`

**Files likely affected**: `src/parser.c`, `docs/content/manual/manual.yml`, `src/parser.y`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/jqtest']`

**Problem statement (excerpt):**
> Elif and optional else not working **Describe the bug**
 
 'if' has an optional 'else' clause but it seems to not work in combination with one or more 'elif' clauses.
 
 **To Reproduce**
 
 '''sh
 $ jq --version
 jq-1.6-159-gcff5336
 
 $ jq -n '1,2,3 | if . == 1 then 1 elif . == 2 then 2 end'
 jq: error: syntax error, unexpected end (Unix shell quoting issues?) at <top-level>, line 1:
 1,2,3 | if 

### Sample 3 — `jqlang__jq-2650`

**Files likely affected**: `src/parser.c`, `src/parser.y`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/jqtest']`

**Problem statement (excerpt):**
> Can't chain generic object indexes <!--
 READ THIS FIRST!
 
 If you have a usage question, please ask us on either Stack Overflow (https://stackoverflow.com/questions/tagged/jq) or in the #jq channel (https://web.libera.chat/#jq) on Libera.Chat (https://libera.chat/).
 
 -->
 
 **Describe the bug**
 When selecting subfields (e.g. '.foo.bar'), using the generic notation (e.g. '.["foo"].["bar"]') th

### Sample 4 — `jqlang__jq-2658`

**Files likely affected**: `src/main.c`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/shtest']`

**Problem statement (excerpt):**
> Assertion failure when using --jsonargs with invalid JSON and printing $ARGS Reproduction:
 '''sh
 $ ./jq --version
 jq-1.6-159-gcff5336
 
 $ ./jq -n --jsonargs '$ARGS' 123 'invalid json'
 {
   "positional": [
     123,
 Assertion failed: (0 && "Invalid value"), function jv_dump_term, file jv_print.c, line 221.
     [1]    9056 abort      ./jq -n --jsonargs '$ARGS' 123 'invalid json'
 
 # for some

### Sample 5 — `jqlang__jq-2681`

**Files likely affected**: `src/parser.c`, `src/lexer.h`, `src/parser.y`, `src/lexer.c`, `src/lexer.l`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/jqtest']`

**Problem statement (excerpt):**
> The keyword 'label' can't be used as a binding name :( '''
 jq -n '. as $label | $label'
 jq: error: syntax error, unexpected label, expecting IDENT (Unix shell quoting issues?) at <top-level>, line 1:
 . as $label | $label
 jq: 1 compile error
 '''
 
 We should make sure all keywords can be used as '$keyword' bindings. 

### Sample 6 — `jqlang__jq-2728`

**Files likely affected**: `src/main.c`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/shtest']`

**Problem statement (excerpt):**
> [Feature] support no_color env to disable ansi_color output It would be nice to control the coloring via an environment variable. My use case is that I have 'jq' running inside [wasm-terminal](https://github.com/wasmerio/wasmer-js) and would like to suppress its ansi_coloring when wasm-terminal detects that jq's input is being piped to another program (WASI's 'isatty' is not supported in the brows

### Sample 7 — `jqlang__jq-2750`

**Files likely affected**: `src/execute.c`, `src/compile.c`, `src/parser.c`, `src/compile.h`, `src/opcode_list.h`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/jqtest']`

**Problem statement (excerpt):**
> Strange behaviour when using two piped try catch error **Describe the bug**
 
 When having two piped try/catch the catch for the first try seems to be executed even thought its try expression did not throw an error.
 
 **To Reproduce**
 
 '''sh
 # current jq master (cff5336)
 $ jq --version
 jq-1.6-159-gcff5336
 
 $ jq -n 'try null catch error(["catch-a", .]) | try error("error-b") catch error(["c

### Sample 8 — `jqlang__jq-2839`

**Files likely affected**: `src/jv.c`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/jqtest']`

**Problem statement (excerpt):**
> Calling jv_cmp() on two decNumber numbers can still cause a segfault OSS-fuzz report: https://bugs.chromium.org/p/oss-fuzz/issues/detail?id=61166
 (It results fixed because the reproducer is '3E506760210+63E-6855002263', and now constant folding doesn't call 'jv_cmp()' unnecessarily for number addition, but the problem still exists)
 
 Even with the fix from #2818, comparing two decNumber numbers 

## Section 6 — Builder guidance

When building a fix for an instance in jqlang/jq:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/main.c appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 26 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "jqlang/jq"`).

First 20 instance_ids:

- `jqlang__jq-2235` (dataset: `swe-bench-multilingual-test`)
- `jqlang__jq-2598` (dataset: `swe-bench-multilingual-test`)
- `jqlang__jq-2650` (dataset: `swe-bench-multilingual-test`)
- `jqlang__jq-2658` (dataset: `swe-bench-multilingual-test`)
- `jqlang__jq-2681` (dataset: `swe-bench-multilingual-test`)
- `jqlang__jq-2728` (dataset: `swe-bench-multilingual-test`)
- `jqlang__jq-2750` (dataset: `swe-bench-multilingual-test`)
- `jqlang__jq-2839` (dataset: `swe-bench-multilingual-test`)
- `jqlang__jq-2919` (dataset: `swe-bench-multilingual-test`)
- `jqlang__jq-3238` (dataset: `multi-swe-bench`)
- `jqlang__jq-3165` (dataset: `multi-swe-bench`)
- `jqlang__jq-3161` (dataset: `multi-swe-bench`)
- `jqlang__jq-2919` (dataset: `multi-swe-bench`)
- `jqlang__jq-2840` (dataset: `multi-swe-bench`)
- `jqlang__jq-2839` (dataset: `multi-swe-bench`)
- `jqlang__jq-2824` (dataset: `multi-swe-bench`)
- `jqlang__jq-2821` (dataset: `multi-swe-bench`)
- `jqlang__jq-2728` (dataset: `multi-swe-bench`)
- `jqlang__jq-2674` (dataset: `multi-swe-bench`)
- `jqlang__jq-2658` (dataset: `multi-swe-bench`)
- ... (6 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
