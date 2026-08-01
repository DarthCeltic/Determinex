---
name: swebench-anuraghazra__github-readme-stats
description: SWE-bench repo behavioral spec for anuraghazra/github-readme-stats. Aggregated from 19 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# anuraghazra/github-readme-stats — SWE-bench Repo Spec

> **19 bug-fix instances** across 1 dataset(s); language(s): js.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 19 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `readme.md` | 10 |
| `api/index.js` | 9 |
| `src/common/utils.js` | 7 |
| `src/cards/stats-card.js` | 5 |
| `api/pin.js` | 4 |
| `src/cards/wakatime-card.js` | 4 |
| `src/cards/top-languages-card.js` | 4 |
| `src/cards/repo-card.js` | 4 |
| `api/top-langs.js` | 3 |
| `src/cards/types.d.ts` | 3 |
| `src/utils.js` | 3 |
| `src/renderRepoCard.js` | 3 |
| `api/wakatime.js` | 2 |
| `src/fetchers/top-languages-fetcher.js` | 2 |
| `src/fetchers/repo-fetcher.js` | 2 |
| `src/fetchers/stats-fetcher.js` | 2 |
| `src/common/Card.js` | 2 |
| `src/fetchStats.js` | 2 |
| `src/renderStatsCard.js` | 2 |
| `src/fetchRepo.js` | 2 |
| `.gitignore` | 1 |
| `src/cards/gist-card.js` | 1 |
| `api/gist.js` | 1 |
| `api/status/up.js` | 1 |
| `src/common/retryer.js` | 1 |
| `src/fetchers/gist-fetcher.js` | 1 |
| `cloudflare/index.js` | 1 |
| `api/status/pat-info.js` | 1 |
| `cloudflare/adapter.js` | 1 |
| `wrangler.toml` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 19 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in anuraghazra/github-readme-stats:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. readme.md appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 19 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "anuraghazra/github-readme-stats"`).

First 20 instance_ids:

- `anuraghazra__github-readme-stats-3442` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-2844` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-2491` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-2228` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-2099` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-2075` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-1608` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-1378` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-1370` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-1314` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-1041` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-721` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-293` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-148` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-117` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-105` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-99` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-88` (dataset: `multi-swe-bench`)
- `anuraghazra__github-readme-stats-58` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
