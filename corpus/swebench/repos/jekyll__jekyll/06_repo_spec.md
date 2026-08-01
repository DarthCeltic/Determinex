---
name: swebench-jekyll__jekyll
description: SWE-bench repo behavioral spec for jekyll/jekyll. Aggregated from 5 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# jekyll/jekyll — SWE-bench Repo Spec

> **5 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `lib/jekyll/utils.rb` | 2 |
| `lib/jekyll/filters.rb` | 1 |
| `features/post_data.feature` | 1 |
| `lib/jekyll/drops/excerpt_drop.rb` | 1 |
| `lib/jekyll/drops/document_drop.rb` | 1 |
| `lib/jekyll.rb` | 1 |
| `features/incremental_rebuild.feature` | 1 |
| `lib/jekyll/readers/data_reader.rb` | 1 |
| `lib/jekyll/data_hash.rb` | 1 |
| `lib/jekyll/data_entry.rb` | 1 |
| `lib/jekyll/drops/site_drop.rb` | 1 |
| `lib/jekyll/site.rb` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: TestFilters#test_: filters where_exp filter should filter objects across multiple conditions, TestUtils#test_: The `Utils.slugify` method should not replace Unicode 'Mark', 'Letter', or 'Number: Decimal Digit' category characters, features/post_data.feature:30  Scenario: Use page.name variable, features/incremental_rebuild.feature:70  Scenario: Rebuild when a data file is changed, TestSite#test_: static files in a collection should not be revisited in `Site#each_site_file`**

Sample FAIL_TO_PASS test names (first 10):
```
  TestFilters#test_: filters where_exp filter should filter objects across multiple conditions
  TestUtils#test_: The `Utils.slugify` method should not replace Unicode 'Mark', 'Letter', or 'Number: Decimal Digit' category characters
  features/post_data.feature:30  Scenario: Use page.name variable
  features/incremental_rebuild.feature:70  Scenario: Rebuild when a data file is changed
  TestSite#test_: static files in a collection should not be revisited in `Site#each_site_file`
```

## Section 4 — Problem-theme distribution

Top themes across 5 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| wrong_output | 3 | 60.0% |
| other | 2 | 40.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `jekyll__jekyll-8047`

**Files likely affected**: `lib/jekyll/filters.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['TestFilters#test_: filters where_exp filter should filter objects across multiple conditions']`

**Problem statement (excerpt):**
> Where_exp not working with more than 2 operators I have this code working locally
 
 '''
 <ul>
 {% assign posts=site.posts | where_exp: "post", "post.categories contains 'one' or post.categories contains 'four' " %}
 <ul>
 {% for post in posts %}
 <li><a href="{{ post.url }}">{{ post.title }}</a></li>
 {% endfor %}
 </ul>
 
 '''
 and this one generating the following error
 
 '''
 <ul>
 {% assign 

### Sample 2 — `jekyll__jekyll-8167`

**Files likely affected**: `lib/jekyll/utils.rb`
**FAIL_TO_PASS** (1 tests, first 3): `["TestUtils#test_: The `Utils.slugify` method should not replace Unicode 'Mark', 'Letter', or 'Number: Decimal Digit' category characters"]`

**Problem statement (excerpt):**
> slugify replaces Tamil vowel marks with hyphen   - I updated to the latest 'github-pages'
   - I ran 'bundle exec jekyll doctor' to check my configuration
   - I read the contributing document at https://jekyllrb.com/docs/contributing/
 
 ## My Environment
 
 | Software         | Version(s) |
 | ---------------- | ---------- |
 | Operating System |  OSX 10.15.2 (19C57)   |
 | 'jekyll'         | 3.

### Sample 3 — `jekyll__jekyll-8761`

**Files likely affected**: `features/post_data.feature`, `lib/jekyll/drops/excerpt_drop.rb`, `lib/jekyll/drops/document_drop.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['features/post_data.feature:30  Scenario: Use page.name variable']`

**Problem statement (excerpt):**
> '{{ page.name }}' doesn't return anything on posts <!--
   Hi! Thanks for considering to file a bug with Jekyll. Please take the time to
   answer the basic questions. Please try to be as detailed as possible.
 
   If you are unsure this is a bug in Jekyll, or this is a bug caused
   by a plugin that isn't directly related to Jekyll, or if this is just
   a generic usage question, please consider 

### Sample 4 — `jekyll__jekyll-8771`

**Files likely affected**: `lib/jekyll.rb`, `features/incremental_rebuild.feature`, `lib/jekyll/readers/data_reader.rb`, `lib/jekyll/data_hash.rb`, `lib/jekyll/utils.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['features/incremental_rebuild.feature:70  Scenario: Rebuild when a data file is changed']`

**Problem statement (excerpt):**
> Incremental regeneration ignores changes to data files ## My Environment
 
 <!--
   Replace the values in the Version(s) column with the ones in your build. If you're not
   using 'github-pages', just replace it with "No".
 -->
 
 | Software         | Version(s) |
 | ---------------- | ---------- |
 | Operating System |     MacOS High Sierra  10.13.6     |
 | 'jekyll'         |  4.0.0.pre.alpha1  

### Sample 5 — `jekyll__jekyll-9141`

**Files likely affected**: `lib/jekyll/site.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['TestSite#test_: static files in a collection should not be revisited in `Site#each_site_file`']`

**Problem statement (excerpt):**
> [Bug]: jekyll reports two files have conflicts but they are the same file.  ### Operating System  Mac OS 12.6  ### Ruby Version  ruby 3.0.0p0 (2020-12-25 revision 95aff21468) [x86_64-darwin20]  ### Jekyll Version  jekyll 4.2.2  ### GitHub Pages Version  latest  ### Expected Behavior  I expect two files are same file to not result in a conflict warning when I run bundle exec jekyll serve
 
 '''
   

## Section 6 — Builder guidance

When building a fix for an instance in jekyll/jekyll:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. lib/jekyll/utils.rb appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 5 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "jekyll/jekyll"`).

First 20 instance_ids:

- `jekyll__jekyll-8047` (dataset: `swe-bench-multilingual-test`)
- `jekyll__jekyll-8167` (dataset: `swe-bench-multilingual-test`)
- `jekyll__jekyll-8761` (dataset: `swe-bench-multilingual-test`)
- `jekyll__jekyll-8771` (dataset: `swe-bench-multilingual-test`)
- `jekyll__jekyll-9141` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
