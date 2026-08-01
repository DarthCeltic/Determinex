---
name: swebench-facebook__docusaurus
description: SWE-bench repo behavioral spec for facebook/docusaurus. Aggregated from 5 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# facebook/docusaurus — SWE-bench Repo Spec

> **5 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `packages/docusaurus/src/server/brokenLinks.ts` | 1 |
| `packages/docusaurus-plugin-content-docs/src/client/docsClientUtils.ts` | 1 |
| `packages/docusaurus-utils/src/markdownLinks.ts` | 1 |
| `packages/docusaurus-theme-classic/src/theme/CodeBlock/Content/String.tsx` | 1 |
| `packages/docusaurus-theme-classic/src/options.ts` | 1 |
| `website/docusaurus.config.js` | 1 |
| `packages/docusaurus-utils/src/markdownUtils.ts` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: accepts valid non-strict link with anchor, getActiveDocContext, getActiveVersion for regular docs versions, getActiveVersion is not sensitive to version order, getActiveVersion is not sensitive to isLast attribute**

Sample FAIL_TO_PASS test names (first 10):
```
  accepts valid non-strict link with anchor
  getActiveDocContext
  getActiveVersion for regular docs versions
  getActiveVersion is not sensitive to version order
  getActiveVersion is not sensitive to isLast attribute
  does not replace non-Markdown links
  handles stray spaces
  accepts valid theme config
  can unwrap a simple mdx code block with CRLF
```

## Section 4 — Problem-theme distribution

Top themes across 5 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| documentation | 4 | 80.0% |
| regression | 1 | 20.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `facebook__docusaurus-10130`

**Files likely affected**: `packages/docusaurus/src/server/brokenLinks.ts`
**FAIL_TO_PASS** (1 tests, first 3): `['accepts valid non-strict link with anchor']`

**Problem statement (excerpt):**
> Broken links checker: inconsistent trailing slash behavior ### Have you read the Contributing Guidelines on issues?
 
 - [X] I have read the [Contributing Guidelines on issues](https://github.com/facebook/docusaurus/blob/main/CONTRIBUTING.md#issues).
 
 ### Prerequisites
 
 - [X] I'm using the latest version of Docusaurus.
 - [X] I have tried the 'npm run clear' or 'yarn clear' command.
 - [X] I h

### Sample 2 — `facebook__docusaurus-10309`

**Files likely affected**: `packages/docusaurus-plugin-content-docs/src/client/docsClientUtils.ts`
**FAIL_TO_PASS** (4 tests, first 3): `['getActiveDocContext', 'getActiveVersion for regular docs versions', 'getActiveVersion is not sensitive to version order']`

**Problem statement (excerpt):**
> Setting the 'current' version's path to '/' freezes 'docsVersionDropdown' ### Have you read the Contributing Guidelines on issues?
 
 - [X] I have read the [Contributing Guidelines on issues](https://github.com/facebook/docusaurus/blob/main/CONTRIBUTING.md#issues).
 
 ### Prerequisites
 
 - [X] I'm using the latest version of Docusaurus.
 - [X] I have tried the 'npm run clear' or 'yarn clear' comm

### Sample 3 — `facebook__docusaurus-8927`

**Files likely affected**: `packages/docusaurus-utils/src/markdownLinks.ts`
**FAIL_TO_PASS** (2 tests, first 3): `['does not replace non-Markdown links', 'handles stray spaces']`

**Problem statement (excerpt):**
> Same file + extension in directory names breaks relative image assets ### Have you read the Contributing Guidelines on issues?  - [X] I have read the [Contributing Guidelines on issues](https://github.com/facebook/docusaurus/blob/main/CONTRIBUTING.md#issues).  ### Prerequisites  - [X] I'm using the latest version of Docusaurus. - [X] I have tried the 'npm run clear' or 'yarn clear' command. - [X] 

### Sample 4 — `facebook__docusaurus-9183`

**Files likely affected**: `packages/docusaurus-theme-classic/src/theme/CodeBlock/Content/String.tsx`, `packages/docusaurus-theme-classic/src/options.ts`, `website/docusaurus.config.js`
**FAIL_TO_PASS** (1 tests, first 3): `['accepts valid theme config']`

**Problem statement (excerpt):**
> Allow case-insensitivity for code block language ### Have you read the Contributing Guidelines on issues?  - [X] I have read the [Contributing Guidelines on issues](https://github.com/facebook/docusaurus/blob/main/CONTRIBUTING.md#issues).  ### Description  Hey, I tried to add PHP for code highlighting in the code blocks and according to the doc for this PHP needs to be added in the prism array.
 A

### Sample 5 — `facebook__docusaurus-9897`

**Files likely affected**: `packages/docusaurus-utils/src/markdownUtils.ts`
**FAIL_TO_PASS** (1 tests, first 3): `['can unwrap a simple mdx code block with CRLF']`

**Problem statement (excerpt):**
> End-of-line CRLF sequence causes TabItem compilation error ### Have you read the Contributing Guidelines on issues?
 
 - [X] I have read the [Contributing Guidelines on issues](https://github.com/facebook/docusaurus/blob/main/CONTRIBUTING.md#issues).
 
 ### Prerequisites
 
 - [X] I'm using the latest version of Docusaurus.
 - [X] I have tried the 'npm run clear' or 'yarn clear' command.
 - [X] I h

## Section 6 — Builder guidance

When building a fix for an instance in facebook/docusaurus:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. packages/docusaurus/src/server/brokenLinks.ts appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 5 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "facebook/docusaurus"`).

First 20 instance_ids:

- `facebook__docusaurus-10130` (dataset: `swe-bench-multilingual-test`)
- `facebook__docusaurus-10309` (dataset: `swe-bench-multilingual-test`)
- `facebook__docusaurus-8927` (dataset: `swe-bench-multilingual-test`)
- `facebook__docusaurus-9183` (dataset: `swe-bench-multilingual-test`)
- `facebook__docusaurus-9897` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
