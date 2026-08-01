---
name: swebench-vuejs__core
description: SWE-bench repo behavioral spec for vuejs/core. Aggregated from 53 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# vuejs/core — SWE-bench Repo Spec

> **53 bug-fix instances** across 2 dataset(s); language(s): python, ts.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 48 |
| swe-bench-multilingual-test | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `packages/compiler-sfc/src/script/resolveType.ts` | 7 |
| `packages/runtime-core/src/hydration.ts` | 6 |
| `packages/compiler-sfc/src/style/pluginScoped.ts` | 5 |
| `packages/reactivity/src/effect.ts` | 3 |
| `packages/runtime-core/src/apiWatch.ts` | 3 |
| `packages/compiler-sfc/src/script/utils.ts` | 3 |
| `packages/reactivity/src/baseHandlers.ts` | 3 |
| `packages/runtime-core/src/renderer.ts` | 3 |
| `packages/runtime-core/src/component.ts` | 3 |
| `packages/compiler-sfc/src/style/cssVars.ts` | 2 |
| `packages/runtime-core/src/index.ts` | 2 |
| `packages/runtime-dom/src/apiCustomElement.ts` | 2 |
| `packages/runtime-core/src/helpers/renderSlot.ts` | 2 |
| `packages/compiler-core/src/transforms/transformElement.ts` | 2 |
| `packages/shared/src/general.ts` | 2 |
| `packages/compiler-sfc/src/script/defineEmits.ts` | 2 |
| `packages/compiler-sfc/src/script/defineProps.ts` | 2 |
| `packages/compiler-sfc/src/script/definePropsDestructure.ts` | 2 |
| `packages/compiler-sfc/src/script/context.ts` | 2 |
| `packages/compiler-sfc/src/compileScript.ts` | 2 |
| `packages/compiler-core/src/babelUtils.ts` | 2 |
| `packages/shared/src/escapeHtml.ts` | 1 |
| `packages/runtime-core/src/helpers/renderList.ts` | 1 |
| `packages/compiler-core/src/tokenizer.ts` | 1 |
| `packages/reactivity/src/arrayInstrumentations.ts` | 1 |
| `packages/reactivity/src/dep.ts` | 1 |
| `packages/runtime-core/src/hmr.ts` | 1 |
| `packages/compiler-ssr/src/transforms/ssrTransformTransitionGroup.ts` | 1 |
| `packages/runtime-core/src/apiInject.ts` | 1 |
| `packages/server-renderer/src/helpers/ssrRenderSlot.ts` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: packages/runtime-core/__tests__/apiWatch.spec.ts > api: watch > should be executed correctly, packages/runtime-core/__tests__/hydration.spec.ts > SSR hydration > mismatch handling > escape css var name, packages/runtime-core/__tests__/helpers/renderList.spec.ts > renderList > should render items in a reactive array correctly, packages/compiler-sfc/__tests__/compileStyle.spec.ts > SFC scoped CSS > nesting selector with atrule and comment, packages/compiler-core/__tests__/parse.spec.ts > compiler: parse > Element > v-pre with half-open interpolation**

Sample FAIL_TO_PASS test names (first 10):
```
  packages/runtime-core/__tests__/apiWatch.spec.ts > api: watch > should be executed correctly
  packages/runtime-core/__tests__/hydration.spec.ts > SSR hydration > mismatch handling > escape css var name
  packages/runtime-core/__tests__/helpers/renderList.spec.ts > renderList > should render items in a reactive array correctly
  packages/compiler-sfc/__tests__/compileStyle.spec.ts > SFC scoped CSS > nesting selector with atrule and comment
  packages/compiler-core/__tests__/parse.spec.ts > compiler: parse > Element > v-pre with half-open interpolation
  packages/compiler-core/__tests__/parse.spec.ts > compiler: parse > Element > self-closing v-pre
```

## Section 4 — Problem-theme distribution

Top themes across 53 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 3 | 60.0% |
| wrong_output | 2 | 40.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `vuejs__core-11589`

**Files likely affected**: `packages/reactivity/src/effect.ts`, `packages/runtime-core/src/apiWatch.ts`
**FAIL_TO_PASS** (1 tests, first 3): `['packages/runtime-core/__tests__/apiWatch.spec.ts > api: watch > should be executed correctly']`

**Problem statement (excerpt):**
> Inconsistent execution order of Sync Watchers on 'computed' property ### Vue version
 
 3.4.37
 
 ### Link to minimal reproduction
 
 https://play.vuejs.org/#eNqVkktr20AQx7/KsBQsYyEH0lJwZdMHObSHtLQ9LiTKamRvspoV+1AcjL57Rqs4ySEYctFq5/Gf38zsQXzruqKPKFai9MrpLoDHELuNJN121gU4gMMmB2XbLgasc7ivgtrBAI2zLcw4dyZJkrLkAxCsx/DsbC6psQ4ygwE0G8++8FHCJz4WizkcJMGTUEY5ZP0c1pvJClyKvDVYGLuF7Jog+3DQw/w6h55VAYacmRoT/W4FM/

### Sample 2 — `vuejs__core-11739`

**Files likely affected**: `packages/shared/src/escapeHtml.ts`, `packages/compiler-sfc/src/style/cssVars.ts`, `packages/compiler-sfc/src/script/utils.ts`, `packages/runtime-core/src/hydration.ts`
**FAIL_TO_PASS** (1 tests, first 3): `['packages/runtime-core/__tests__/hydration.spec.ts > SSR hydration > mismatch handling > escape css var name']`

**Problem statement (excerpt):**
> SSR Hydration errors stemming from v-bind in CSS coupled with child component style bindings ### Vue version
 
 3.4.38
 
 ### Link to minimal reproduction
 
 [Vue SFC Playground Reproduction](https://play.vuejs.org/#__SSR__eNqNU8Fu1DAQ/ZWROaRIbYKAU9hWgqoScICK9uhLNpkEt45t2c6S1Wq/gBNfwC/yCYydbHazC1VPu37zZvL8/GbD3huTrjpkOVu40grjwaHvzBVXojXaerjW9KtQ+Xt0HmqrW0jSbIaGAQlXXJVaEcdYbRxcQoW1UHgbTmcbrgCWRfnYW

### Sample 3 — `vuejs__core-11870`

**Files likely affected**: `packages/runtime-core/src/helpers/renderList.ts`
**FAIL_TO_PASS** (1 tests, first 3): `['packages/runtime-core/__tests__/helpers/renderList.spec.ts > renderList > should render items in a reactive array correctly']`

**Problem statement (excerpt):**
> use v-for rendering a shallowReactive array, array item incorrectly converted to a reactive object ### Vue version  3.5.3  ### Link to minimal reproduction  https://play.vuejs.org/#eNp9UsFOAjEQ/ZVJL0CCoNETggkaDnpQg94oh2aZXYq7bdN2V8hm/91pcREM4dJ03sy8efPamk2NGVQlshEbu8RK48GhLw3kQmUTzrzj7IErWRhtPdTg1iLP9fccReJlhX2wmPZBuhaABlKrC+gQZ+eeK64SrRyRnvZNrRU7mPyHuwuuAOpwAAghRoG+26HbTafXD3BD57JHxOPhXi6Jo8BjYXL

### Sample 4 — `vuejs__core-11899`

**Files likely affected**: `packages/compiler-sfc/src/style/pluginScoped.ts`
**FAIL_TO_PASS** (1 tests, first 3): `['packages/compiler-sfc/__tests__/compileStyle.spec.ts > SFC scoped CSS > nesting selector with atrule and comment']`

**Problem statement (excerpt):**
> @ queries in scoped nested CSS lack nesting selector ### Vue version
 
 3.5.4
 
 ### Link to minimal reproduction
 
 https://play.vuejs.org/#eNp9UtFqwjAU/ZWQpw20CjoYXSebw8H2sI1tj4ER22utpklI0loR/303qXUyxLebc849PffQHX3UOqoroDFNHJRacAcTJglJsqImqeDW3jO6UIrRABPyjPN/fs4N8lNukgHC7f5hSgYntvi0biuA2FRpyIIwQnOya73nPF3nRlUy66dKKBMTA9md3/PsQwlZwYmSYosGBkASLjNyVfKmvykyt4zJ7XCom+vO7pxh7vfQ0rP7zjnCA8jOvwOYDELKCe1

### Sample 5 — `vuejs__core-11915`

**Files likely affected**: `packages/compiler-core/src/tokenizer.ts`
**FAIL_TO_PASS** (2 tests, first 3): `['packages/compiler-core/__tests__/parse.spec.ts > compiler: parse > Element > v-pre with half-open interpolation', 'packages/compiler-core/__tests__/parse.spec.ts > compiler: parse > Element > self-closing v-pre']`

**Problem statement (excerpt):**
> v-pre not ignoring {{ inside textarea ### Vue version  3.5.4  ### Link to minimal reproduction  https://jsfiddle.net/h4ds29me/  ### Steps to reproduce  When you include vue via CDN (https://unpkg.com/vue@3/dist/vue.global.prod.js) and wrap a textarea in v-pre, the {{ aren't ignored and it escapes everything after that (assuming there is no closing }}). 
 See this jsfiddle for an example: 
 https:/

## Section 6 — Builder guidance

When building a fix for an instance in vuejs/core:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. packages/compiler-sfc/src/script/resolveType.ts appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 53 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "vuejs/core"`).

First 20 instance_ids:

- `vuejs__core-11589` (dataset: `swe-bench-multilingual-test`)
- `vuejs__core-11739` (dataset: `swe-bench-multilingual-test`)
- `vuejs__core-11870` (dataset: `swe-bench-multilingual-test`)
- `vuejs__core-11899` (dataset: `swe-bench-multilingual-test`)
- `vuejs__core-11915` (dataset: `swe-bench-multilingual-test`)
- `vuejs__core-11899` (dataset: `multi-swe-bench`)
- `vuejs__core-11854` (dataset: `multi-swe-bench`)
- `vuejs__core-11813` (dataset: `multi-swe-bench`)
- `vuejs__core-11761` (dataset: `multi-swe-bench`)
- `vuejs__core-11694` (dataset: `multi-swe-bench`)
- `vuejs__core-11680` (dataset: `multi-swe-bench`)
- `vuejs__core-11625` (dataset: `multi-swe-bench`)
- `vuejs__core-11517` (dataset: `multi-swe-bench`)
- `vuejs__core-11515` (dataset: `multi-swe-bench`)
- `vuejs__core-11502` (dataset: `multi-swe-bench`)
- `vuejs__core-11491` (dataset: `multi-swe-bench`)
- `vuejs__core-11338` (dataset: `multi-swe-bench`)
- `vuejs__core-11201` (dataset: `multi-swe-bench`)
- `vuejs__core-11165` (dataset: `multi-swe-bench`)
- `vuejs__core-11026` (dataset: `multi-swe-bench`)
- ... (33 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
