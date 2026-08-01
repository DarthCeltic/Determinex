---
name: swebench-faker-ruby__faker
description: SWE-bench repo behavioral spec for faker-ruby/faker. Aggregated from 2 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# faker-ruby/faker — SWE-bench Repo Spec

> **2 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 2 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `lib/faker/default/internet.rb` | 2 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: test_password, test_email_with_abbreviations**

Sample FAIL_TO_PASS test names (first 10):
```
  test_password
  test_email_with_abbreviations
```

## Section 4 — Problem-theme distribution

Top themes across 2 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| documentation | 1 | 50.0% |
| wrong_output | 1 | 50.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `faker-ruby__faker-2705`

**Files likely affected**: `lib/faker/default/internet.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['test_password']`

**Problem statement (excerpt):**
> Faker::Internet.password method doesn't add numbers anymore ## Describe the bug
 The docs and comments suggest numbers are included, but looking at the source code it only includes lowercase, uppercase, and symbols.
 
 ## To Reproduce
 Describe a way to reproduce your bug. To get the Faker version, run 'Faker::VERSION'.
 
 Use the reproduction script below to reproduce the issue:
 
 '''
 # frozen_

### Sample 2 — `faker-ruby__faker-2970`

**Files likely affected**: `lib/faker/default/internet.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['test_email_with_abbreviations']`

**Problem statement (excerpt):**
> Latest version generates invalid email addresses ## Describe the bug
 
 When letting faker generate email addresses based on names, it now generates invalid email addresses, where older versions did not.
 
 Example:
 
 '''ruby
 # Faker 3.4.1
 Faker::Internet.unique.email(name: " Msgr. Titus Harvey")
 # => "harvey.msgr..titus@russel-von.example"
 '''
 
 The email is invalid as two sequential dots a

## Section 6 — Builder guidance

When building a fix for an instance in faker-ruby/faker:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. lib/faker/default/internet.rb appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 2 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "faker-ruby/faker"`).

First 20 instance_ids:

- `faker-ruby__faker-2705` (dataset: `swe-bench-multilingual-test`)
- `faker-ruby__faker-2970` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
