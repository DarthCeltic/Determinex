---
name: swebench-mui__material-ui
description: SWE-bench repo behavioral spec for mui/material-ui. Aggregated from 174 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# mui/material-ui — SWE-bench Repo Spec

> **174 bug-fix instances** across 1 dataset(s); language(s): ts.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 174 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `packages/mui-material/src/Autocomplete/Autocomplete.js` | 9 |
| `docs/src/pages/guides/migration-v4/migration-v4.md` | 7 |
| `packages/mui-joy/src/styles/components.d.ts` | 6 |
| `docs/translations/translations.json` | 6 |
| `packages/mui-joy/src/index.ts` | 6 |
| `packages/mui-joy/src/Select/SelectProps.ts` | 6 |
| `packages/mui-joy/src/Select/Select.tsx` | 6 |
| `packages/mui-base/src/index.d.ts` | 6 |
| `packages/mui-base/src/index.js` | 6 |
| `packages/mui-base/src/AutocompleteUnstyled/useAutocomplete.js` | 6 |
| `packages/mui-base/src/ListboxUnstyled/useListbox.ts` | 6 |
| `packages/mui-joy/src/styles/extendTheme.spec.ts` | 5 |
| `docs/data/joy/pagesApi.js` | 5 |
| `docs/data/joy/pages.ts` | 5 |
| `packages/mui-joy/src/Button/Button.tsx` | 5 |
| `packages/mui-joy/src/MenuList/MenuList.tsx` | 5 |
| `packages/mui-joy/src/Menu/Menu.tsx` | 5 |
| `packages/mui-base/src/useAutocomplete/useAutocomplete.js` | 5 |
| `packages/mui-base/src/useSelect/useSelect.ts` | 5 |
| `packages/mui-material/src/Autocomplete/Autocomplete.d.ts` | 5 |
| `packages/mui-base/src/SelectUnstyled/SelectUnstyled.tsx` | 5 |
| `packages/mui-base/src/InputUnstyled/InputUnstyled.tsx` | 5 |
| `packages/mui-material/src/Grid/Grid.js` | 5 |
| `packages/mui-system/src/style.js` | 4 |
| `packages/mui-material/src/TablePagination/TablePagination.js` | 4 |
| `packages/mui-base/src/useSelect/useSelect.types.ts` | 4 |
| `docs/data/base/components/menu/UseMenu.tsx` | 4 |
| `docs/data/base/components/menu/UseMenu.js` | 4 |
| `packages/mui-system/src/Unstable_Grid/gridGenerator.ts` | 4 |
| `docs/translations/api-docs/autocomplete/autocomplete.json` | 4 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 174 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in mui/material-ui:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. packages/mui-material/src/Autocomplete/Autocomplete.js appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 174 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "mui/material-ui"`).

First 20 instance_ids:

- `mui__material-ui-39962` (dataset: `multi-swe-bench`)
- `mui__material-ui-39775` (dataset: `multi-swe-bench`)
- `mui__material-ui-39688` (dataset: `multi-swe-bench`)
- `mui__material-ui-39679` (dataset: `multi-swe-bench`)
- `mui__material-ui-39536` (dataset: `multi-swe-bench`)
- `mui__material-ui-39465` (dataset: `multi-swe-bench`)
- `mui__material-ui-39457` (dataset: `multi-swe-bench`)
- `mui__material-ui-39353` (dataset: `multi-swe-bench`)
- `mui__material-ui-39196` (dataset: `multi-swe-bench`)
- `mui__material-ui-39108` (dataset: `multi-swe-bench`)
- `mui__material-ui-39071` (dataset: `multi-swe-bench`)
- `mui__material-ui-38916` (dataset: `multi-swe-bench`)
- `mui__material-ui-38801` (dataset: `multi-swe-bench`)
- `mui__material-ui-38788` (dataset: `multi-swe-bench`)
- `mui__material-ui-38544` (dataset: `multi-swe-bench`)
- `mui__material-ui-38247` (dataset: `multi-swe-bench`)
- `mui__material-ui-38188` (dataset: `multi-swe-bench`)
- `mui__material-ui-38182` (dataset: `multi-swe-bench`)
- `mui__material-ui-38169` (dataset: `multi-swe-bench`)
- `mui__material-ui-38167` (dataset: `multi-swe-bench`)
- ... (154 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
