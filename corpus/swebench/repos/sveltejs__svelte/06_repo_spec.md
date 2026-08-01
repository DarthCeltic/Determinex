---
name: swebench-sveltejs__svelte
description: SWE-bench repo behavioral spec for sveltejs/svelte. Aggregated from 272 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# sveltejs/svelte — SWE-bench Repo Spec

> **272 bug-fix instances** across 1 dataset(s); language(s): js.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 272 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `packages/svelte/src/compiler/errors.js` | 34 |
| `packages/svelte/src/compiler/phases/3-transform/client/visitors/template.js` | 33 |
| `packages/svelte/src/compiler/phases/2-analyze/validation.js` | 31 |
| `packages/svelte/src/compiler/phases/2-analyze/index.js` | 28 |
| `packages/svelte/types/index.d.ts` | 26 |
| `packages/svelte/src/compiler/migrate/index.js` | 26 |
| `packages/svelte/src/internal/client/runtime.js` | 20 |
| `packages/svelte/src/compiler/phases/3-transform/server/transform-server.js` | 19 |
| `packages/svelte/src/compiler/phases/3-transform/client/transform-client.js` | 15 |
| `packages/svelte/src/compiler/warnings.js` | 14 |
| `packages/svelte/src/compiler/phases/2-analyze/css/css-prune.js` | 14 |
| `packages/svelte/src/compiler/phases/scope.js` | 14 |
| `packages/svelte/src/internal/client/render.js` | 14 |
| `packages/svelte/messages/compile-errors/template.md` | 12 |
| `packages/svelte/src/internal/client/dom/elements/attributes.js` | 11 |
| `packages/svelte/src/compiler/types/template.d.ts` | 11 |
| `packages/svelte/src/internal/server/index.js` | 11 |
| `sites/svelte-5-preview/src/routes/docs/content/03-appendix/02-breaking-changes.md` | 11 |
| `packages/svelte/src/compiler/phases/3-transform/client/utils.js` | 10 |
| `packages/svelte/src/compiler/phases/1-parse/state/tag.js` | 9 |
| `packages/svelte/src/compiler/phases/1-parse/state/element.js` | 9 |
| `packages/svelte/src/compiler/phases/3-transform/css/index.js` | 9 |
| `packages/svelte/src/internal/client/index.js` | 8 |
| `packages/svelte/src/internal/client/reactivity/props.js` | 7 |
| `packages/svelte/src/compiler/types/css.d.ts` | 7 |
| `packages/svelte/src/internal/client/proxy.js` | 7 |
| `packages/svelte/src/compiler/phases/3-transform/utils.js` | 7 |
| `packages/svelte/src/constants.js` | 7 |
| `packages/svelte/src/compiler/phases/3-transform/client/visitors/RegularElement.js` | 6 |
| `packages/svelte/src/compiler/phases/types.d.ts` | 6 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 272 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in sveltejs/svelte:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. packages/svelte/src/compiler/errors.js appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 272 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "sveltejs/svelte"`).

First 20 instance_ids:

- `sveltejs__svelte-15115` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-15086` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-15083` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-15057` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-15020` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-15013` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14993` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14942` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14937` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14935` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14907` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14811` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14699` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14691` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14677` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14640` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14629` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14626` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14620` (dataset: `multi-swe-bench`)
- `sveltejs__svelte-14607` (dataset: `multi-swe-bench`)
- ... (252 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*

---

## Section 8 — Anchor-grade hand-curated reference (top-5 by instance count, 272 instances, JS/TS)

### Repo overview
Svelte is the JavaScript UI framework with a compiler-based approach (no virtual DOM). Bug fixes
cluster in the compiler (`packages/svelte/src/compiler/`) and the runtime (`packages/svelte/src/internal/`).

### High-leverage bug zones

| Subsystem | Touch count | Common bug pattern |
|-----------|------------|--------------------|
| `packages/svelte/src/compiler/errors.js` | 34 | Error message text + code mapping |
| `packages/svelte/src/compiler/phases/3-transform/client/visitors/template.js` | 33 | Template AST → JS code generation |
| `packages/svelte/src/compiler/phases/2-analyze/validation.js` | 31 | Static analysis warnings + errors |
| `packages/svelte/src/compiler/phases/1-parse/` | ~20 | Source → AST parsing edge cases |
| `packages/svelte/src/internal/client/` | ~20 | Reactive runtime; effect scheduling |
| `packages/svelte/src/compiler/phases/3-transform/css/` | ~15 | Scoped CSS selector transformation |

### Test framework
**vitest** with snapshot tests for compiler output. FAIL_TO_PASS names look like:
`packages/svelte/tests/compiler/test.js > if-block` or `> reactivity > derived-store`.

### Builder rules specific to Svelte

1. **AST visitor pattern**: don't mutate nodes in-place during traversal. Return a new node or null.
2. **Compiler phases**: parse → analyze → transform. Bugs in earlier phases cascade. Fix at the earliest phase.
3. **Error codes**: every compiler error has a numeric code. Adding new errors needs the code in `errors.js`.
4. **Reactivity**: `$state`, `$derived`, `$effect` (Svelte 5 runes). Bugs often involve effect re-execution timing.
5. **TypeScript type generation**: `.svelte` files generate `.d.ts` — verify `script lang="ts"` paths.
6. **Snapshot tests**: use `vitest -u` to update only after manual verification.
7. **CSS scoping**: hashes are deterministic per component; don't change hash logic without updating snapshots.

### Where 90→100% lives

- `test_*template*` → template parser edges (slot, snippet, await, each)
- `test_*reactivity*` → `$state` / `$derived` / `$effect` interaction
- `test_*validation*` → static analyzer edge cases (warnings vs errors)
- `test_*css*` → scoped class hashing; nested selectors
- `test_*types*` → TypeScript generation correctness

### Estimated lock cost per instance
~10-25 min on Sonnet; ~30-60 min on local Qwen 14b. Compiler bugs often need understanding of multi-phase interaction.
