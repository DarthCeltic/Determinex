---
name: swebench-facebook__zstd
description: SWE-bench repo behavioral spec for facebook/zstd. Aggregated from 29 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# facebook/zstd — SWE-bench Repo Spec

> **29 bug-fix instances** across 1 dataset(s); language(s): c.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 29 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `lib/compress/zstd_compress.c` | 17 |
| `lib/zstd.h` | 12 |
| `programs/fileio.c` | 7 |
| `lib/decompress/zstd_decompress.c` | 6 |
| `programs/zstdcli.c` | 5 |
| `programs/zstd.1.md` | 4 |
| `programs/fileio.h` | 4 |
| `lib/compress/zstdmt_compress.c` | 4 |
| `lib/compress/zstd_compress_internal.h` | 2 |
| `lib/compress/zstd_lazy.c` | 1 |
| `lib/compress/zstd_lazy.h` | 1 |
| `programs/fileio_types.h` | 1 |
| `lib/common/error_private.h` | 1 |
| `lib/decompress/zstd_decompress_internal.h` | 1 |
| `lib/common/zstd_errors.h` | 1 |
| `lib/common/error_private.c` | 1 |
| `zlibWrapper/zstd_zlibwrapper.c` | 1 |
| `lib/common/zstd_internal.h` | 1 |
| `lib/decompress/zstd_decompress_block.c` | 1 |
| `CHANGELOG` | 1 |
| `lib/compress/zstdmt_compress.h` | 1 |
| `lib/compress/zstd_ldm.c` | 1 |
| `lib/compress/zstd_ldm.h` | 1 |
| `build/cmake/lib/CMakeLists.txt` | 1 |
| `programs/Makefile` | 1 |
| `appveyor.yml` | 1 |
| `lib/Makefile` | 1 |
| `lib/compress/zstd_opt.c` | 1 |
| `programs/bench.c` | 1 |
| `programs/util.h` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 29 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in facebook/zstd:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. lib/compress/zstd_compress.c appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 29 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "facebook/zstd"`).

First 20 instance_ids:

- `facebook__zstd-3942` (dataset: `multi-swe-bench`)
- `facebook__zstd-3530` (dataset: `multi-swe-bench`)
- `facebook__zstd-3438` (dataset: `multi-swe-bench`)
- `facebook__zstd-3362` (dataset: `multi-swe-bench`)
- `facebook__zstd-3223` (dataset: `multi-swe-bench`)
- `facebook__zstd-2451` (dataset: `multi-swe-bench`)
- `facebook__zstd-2130` (dataset: `multi-swe-bench`)
- `facebook__zstd-2094` (dataset: `multi-swe-bench`)
- `facebook__zstd-1837` (dataset: `multi-swe-bench`)
- `facebook__zstd-1733` (dataset: `multi-swe-bench`)
- `facebook__zstd-1726` (dataset: `multi-swe-bench`)
- `facebook__zstd-1540` (dataset: `multi-swe-bench`)
- `facebook__zstd-1532` (dataset: `multi-swe-bench`)
- `facebook__zstd-1530` (dataset: `multi-swe-bench`)
- `facebook__zstd-1459` (dataset: `multi-swe-bench`)
- `facebook__zstd-1458` (dataset: `multi-swe-bench`)
- `facebook__zstd-1416` (dataset: `multi-swe-bench`)
- `facebook__zstd-1390` (dataset: `multi-swe-bench`)
- `facebook__zstd-1243` (dataset: `multi-swe-bench`)
- `facebook__zstd-1107` (dataset: `multi-swe-bench`)
- ... (9 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
