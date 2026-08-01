---
name: swebench-jordansissel__fpm
description: SWE-bench repo behavioral spec for jordansissel/fpm. Aggregated from 2 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# jordansissel/fpm — SWE-bench Repo Spec

> **2 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 2 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `lib/fpm/package/deb.rb` | 1 |
| `lib/fpm/package/empty.rb` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: should reject 'this is not valid', should reject 'hello = world', should reject 'hello ()', should reject 'hello (>)', should reject 'hello (1234)'**

Sample FAIL_TO_PASS test names (first 10):
```
  should reject 'this is not valid'
  should reject 'hello = world'
  should reject 'hello ()'
  should reject 'hello (>)'
  should reject 'hello (1234)'
  should default to 'all'
```

## Section 4 — Problem-theme distribution

Top themes across 2 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| regression | 1 | 50.0% |
| edge_case | 1 | 50.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `jordansissel__fpm-1829`

**Files likely affected**: `lib/fpm/package/deb.rb`
**FAIL_TO_PASS** (6 tests, first 3): `["should reject 'this is not valid'", "should reject 'hello = world'", "should reject 'hello ()'"]`

**Problem statement (excerpt):**
> Debian versioned provides allows invalid version strings Hi folks, I've been specifying '--provides 'foo (<< 1.0.0-54)'' for quite a while, but fpm only recently started passing through the version string ( #1788 #1803 ).
 
 My '<<' inequality is broken: dpkg only allows exact version Provides with '='. If fpm checked for that, I would have caught the error at build time rather than install time. 

### Sample 2 — `jordansissel__fpm-1850`

**Files likely affected**: `lib/fpm/package/empty.rb`
**FAIL_TO_PASS** (1 tests, first 3): `["should default to 'all'"]`

**Problem statement (excerpt):**
> 'empty' package type could set the architecture to "all" by default Since empty packages have no files, there's not much to really be "architecture specific" by default.
 
 I don't know what negative impact this change might have.
 
 Currently, empty packages default to _native_ which is whatever the host machine is:
 
 '''
 % fpm -s empty -t rpm -n example
 Created package {:path=>"example-1.0-1.

## Section 6 — Builder guidance

When building a fix for an instance in jordansissel/fpm:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. lib/fpm/package/deb.rb appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 2 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "jordansissel/fpm"`).

First 20 instance_ids:

- `jordansissel__fpm-1829` (dataset: `swe-bench-multilingual-test`)
- `jordansissel__fpm-1850` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
