---
name: swebench-babel__babel
description: SWE-bench repo behavioral spec for babel/babel. Aggregated from 5 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# babel/babel — SWE-bench Repo Spec

> **5 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `packages/babel-parser/src/parser/expression.js` | 1 |
| `packages/babel-generator/src/node/parentheses.ts` | 1 |
| `packages/babel-generator/src/source-map.ts` | 1 |
| `packages/babel-traverse/src/scope/lib/renamer.ts` | 1 |
| `packages/babel-helpers/src/index.ts` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: es2015/yield/yield following arrow in params, es2017/async functions/await following arrow inside params, unary postfix, inputSourceMap without sourcesContent, .shorthand after renaming `ObjectProperty`**

Sample FAIL_TO_PASS test names (first 10):
```
  es2015/yield/yield following arrow in params
  es2017/async functions/await following arrow inside params
  unary postfix
  inputSourceMap without sourcesContent
  .shorthand after renaming `ObjectProperty`
  declaration name conflict helper entrypoint
```

## Section 4 — Problem-theme distribution

Top themes across 5 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 3 | 60.0% |
| wrong_output | 1 | 20.0% |
| api_change | 1 | 20.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `babel__babel-13928`

**Files likely affected**: `packages/babel-parser/src/parser/expression.js`
**FAIL_TO_PASS** (2 tests, first 3): `['es2015/yield/yield following arrow in params', 'es2017/async functions/await following arrow inside params']`

**Problem statement (excerpt):**
> [Bug]: incorrectly rejects 'await' when following a function with an arrow in default parameters ### 💻
 
 - [ ] Would you like to work on a fix?
 
 ### How are you using Babel?
 
 Programmatic API ('babel.transform', 'babel.parse')
 
 ### Input code
 
 '''js
 (async function () {
   function f(_=()=>null) {}
   await null;
 });
 '''
 
 or
 
 '''js
 (function* () {
   function f(_=()=>null) {}
   y

### Sample 2 — `babel__babel-14532`

**Files likely affected**: `packages/babel-generator/src/node/parentheses.ts`
**FAIL_TO_PASS** (1 tests, first 3): `['unary postfix']`

**Problem statement (excerpt):**
> [Bug]: Function Statements Require a Function Name ### 💻  - [X] Would you like to work on a fix?  ### How are you using Babel?  @babel/cli  ### Input code  '''js
 const v0 = [
     {
         5: 'foo',
         v20(val, x) {
             let v1 = {};
             v4(8, 'a', 7, 3, 'a');
             (() => {
                 array[args]++;
                 return f2[v14(10, true).attr.v6 - 2](y[2].

### Sample 3 — `babel__babel-15445`

**Files likely affected**: `packages/babel-generator/src/source-map.ts`
**FAIL_TO_PASS** (1 tests, first 3): `['inputSourceMap without sourcesContent']`

**Problem statement (excerpt):**
> [Bug]: generating source maps fails due to 'sourcesContent' being undefined ### 💻  - [X] Would you like to work on a fix?  ### How are you using Babel?  Programmatic API ('babel.transform', 'babel.parse')  ### Input code  I am trying to transform code via:
 '''js
 const { transformSync } = require('@babel/core');
 const codeMap = transformSync(code, babelOpts);
 '''
 where 'code' is:
 
 '''js
  va

### Sample 4 — `babel__babel-15649`

**Files likely affected**: `packages/babel-traverse/src/scope/lib/renamer.ts`
**FAIL_TO_PASS** (1 tests, first 3): `['.shorthand after renaming `ObjectProperty`']`

**Problem statement (excerpt):**
> [Bug]: shorthand of 'ObjectProperty' inside 'ObjectPattern' not updated after 'path.scopre.rename()' ### 💻  - [x] Would you like to work on a fix?  ### How are you using Babel?  Programmatic API ('babel.transform', 'babel.parse')  ### Input code  '''js
 const traverse = require('@babel/traverse').default;
 
 const code = '
     const {a} = b;
     const {c: d} = b;
     console.log(a);
 '
 
 const

### Sample 5 — `babel__babel-16130`

**Files likely affected**: `packages/babel-helpers/src/index.ts`
**FAIL_TO_PASS** (1 tests, first 3): `['declaration name conflict helper entrypoint']`

**Problem statement (excerpt):**
> [Bug]: 'transform-classes' and 'transform-object-super' plugins produce code which stack overflow if var named 'set' in source code ### 💻  - [ ] Would you like to work on a fix?  ### How are you using Babel?  Programmatic API ('babel.transform', 'babel.parse')  ### Input code  '''js
 let set;
 class C {
   foo() {
     super.bar = 1;
   }
 }
 '''
 
 [REPL](https://babeljs.io/repl#?browsers=default

## Section 6 — Builder guidance

When building a fix for an instance in babel/babel:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. packages/babel-parser/src/parser/expression.js appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 5 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "babel/babel"`).

First 20 instance_ids:

- `babel__babel-13928` (dataset: `swe-bench-multilingual-test`)
- `babel__babel-14532` (dataset: `swe-bench-multilingual-test`)
- `babel__babel-15445` (dataset: `swe-bench-multilingual-test`)
- `babel__babel-15649` (dataset: `swe-bench-multilingual-test`)
- `babel__babel-16130` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
