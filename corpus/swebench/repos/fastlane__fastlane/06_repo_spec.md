---
name: swebench-fastlane__fastlane
description: SWE-bench repo behavioral spec for fastlane/fastlane. Aggregated from 7 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# fastlane/fastlane — SWE-bench Repo Spec

> **7 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 7 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `fastlane/lib/fastlane/actions/zip.rb` | 2 |
| `fastlane/lib/fastlane/actions/download_dsyms.rb` | 1 |
| `frameit/lib/frameit/device.rb` | 1 |
| `fastlane/lib/fastlane/fast_file.rb` | 1 |
| `match/lib/match/storage/s3_storage.rb` | 1 |
| `fastlane_core/lib/fastlane_core/print_table.rb` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: archives a directory with shell escaped path - ./fastlane/spec/actions_specs/zip_spec.rb[1:1:1:8], sets default values for optional include and exclude parameters - ./fastlane/spec/actions_specs/zip_spec.rb[1:1:1:1], downloads dsyms with more recent uploaded_date - ./fastlane/spec/actions_specs/download_dsyms_spec.rb[1:1:1:8:1], should detect iPhone 13 in portrait and landscape based on priority - ./frameit/spec/device_spec.rb[1:1:1:2], works when no cache is provided - ./fastlane/spec/actions_specs/import_from_git_spec.rb[1:1:1:3:1]**

Sample FAIL_TO_PASS test names (first 10):
```
  archives a directory with shell escaped path - ./fastlane/spec/actions_specs/zip_spec.rb[1:1:1:8]
  sets default values for optional include and exclude parameters - ./fastlane/spec/actions_specs/zip_spec.rb[1:1:1:1]
  downloads dsyms with more recent uploaded_date - ./fastlane/spec/actions_specs/download_dsyms_spec.rb[1:1:1:8:1]
  should detect iPhone 13 in portrait and landscape based on priority - ./frameit/spec/device_spec.rb[1:1:1:2]
  works when no cache is provided - ./fastlane/spec/actions_specs/import_from_git_spec.rb[1:1:1:3:1]
  downloads only file-like objects and skips folder-like objects - ./match/spec/storage/s3_storage_spec.rb[1:1:3:3]
  doesn't crash when lane_context contains non unicode text - ./fastlane/spec/lane_manager_base_spec.rb[1:1:1:3]
```

## Section 4 — Problem-theme distribution

Top themes across 7 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| regression | 2 | 28.6% |
| edge_case | 1 | 14.3% |
| wrong_output | 1 | 14.3% |
| documentation | 1 | 14.3% |
| config_environment | 1 | 14.3% |
| encoding_unicode | 1 | 14.3% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `fastlane__fastlane-19207`

**Files likely affected**: `fastlane/lib/fastlane/actions/zip.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['archives a directory with shell escaped path - ./fastlane/spec/actions_specs/zip_spec.rb[1:1:1:8]']`

**Problem statement (excerpt):**
> zip() command fails in 2.190.0 if the path contains characters that require escaping, such as '(' <!-- Thanks for helping _fastlane_! Before you submit your issue, please make sure to check the following boxes by putting an x in the [ ] (don't: [x ], [ x], do: [x]) -->
 
 ### New Regression Checklist
 
 - [x] Updated fastlane to the latest version
 - [x] I read the [Contribution Guidelines](https:

### Sample 2 — `fastlane__fastlane-19304`

**Files likely affected**: `fastlane/lib/fastlane/actions/zip.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['sets default values for optional include and exclude parameters - ./fastlane/spec/actions_specs/zip_spec.rb[1:1:1:1]']`

**Problem statement (excerpt):**
> 'zip_command': [!] undefined method 'empty?' for nil:NilClass <!-- Thanks for helping fastlane! Before you submit your issue, please make sure you followed our checklist and check the appropriate boxes by putting an x in the [ ]: [x] -->
 
 ### New Issue Checklist
 
 - [x] Updated fastlane to the latest version
 - [x] I read the [Contribution Guidelines](https://github.com/fastlane/fastlane/blob

### Sample 3 — `fastlane__fastlane-19765`

**Files likely affected**: `fastlane/lib/fastlane/actions/download_dsyms.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['downloads dsyms with more recent uploaded_date - ./fastlane/spec/actions_specs/download_dsyms_spec.rb[1:1:1:8:1]']`

**Problem statement (excerpt):**
> download_dsyms doesn't completes while scanning a whole build history ### Issue Description
 <!-- Please include what's happening, expected behavior, and any relevant code samples -->
 
 We have a long history of iOS builds. We try to use the action above passing it 'after_uploaded_date' to download recent builds only from App Store Connect. It works well and downloads required builds. However, th

### Sample 4 — `fastlane__fastlane-20642`

**Files likely affected**: `frameit/lib/frameit/device.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['should detect iPhone 13 in portrait and landscape based on priority - ./frameit/spec/device_spec.rb[1:1:1:2]']`

**Problem statement (excerpt):**
> [frameit] "fastlane frameit" doesn't detect iPhone 13 Pro   <!-- Thanks for helping fastlane! Before you submit your issue, please make sure you followed our checklist and check the appropriate boxes by putting an x in the [ ]: [x] -->
 
 ### New Issue Checklist
 
 - [x] Updated fastlane to the latest version
 - [x] I read the [Contribution Guidelines](https://github.com/fastlane/fastlane/blob/mas

### Sample 5 — `fastlane__fastlane-20958`

**Files likely affected**: `fastlane/lib/fastlane/fast_file.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['works when no cache is provided - ./fastlane/spec/actions_specs/import_from_git_spec.rb[1:1:1:3:1]']`

**Problem statement (excerpt):**
> [Regression] import_from_git fails to found Fastfile if no cache folder is provided ### New Regression Checklist
 
 - [x] Updated fastlane to the latest version
 - [x] I read the [Contribution Guidelines](https://github.com/fastlane/fastlane/blob/master/CONTRIBUTING.md)
 - [x] I read [docs.fastlane.tools](https://docs.fastlane.tools)
 - [x] I searched for [existing GitHub issues](https://github.co

### Sample 6 — `fastlane__fastlane-20975`

**Files likely affected**: `match/lib/match/storage/s3_storage.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['downloads only file-like objects and skips folder-like objects - ./match/spec/storage/s3_storage_spec.rb[1:1:3:3]']`

**Problem statement (excerpt):**
> Is a directory @ rb_sysopen - error Hi Team,
 
 I am getting "Is a directory @ rb_sysopen - /var/folders/g5/zw7km8512ks2nm6788c74dmm0000gp/T/d20210920-74204-nvj51h/" error while running "fastlane prodution_cert_update nuke:false" tried on mac as well on different server. not getting enough information to fix it. if I use git has storage everything works fine, but I want to store it in S3.
 
 here 

### Sample 7 — `fastlane__fastlane-21857`

**Files likely affected**: `fastlane_core/lib/fastlane_core/print_table.rb`
**FAIL_TO_PASS** (1 tests, first 3): `["doesn't crash when lane_context contains non unicode text - ./fastlane/spec/lane_manager_base_spec.rb[1:1:1:3]"]`

**Problem statement (excerpt):**
> [!] invalid byte sequence in UTF-8 (ArgumentError) Hello 
 
 I'm currently experiencing an issue about UTF-8 error with Fastlane on Bitrise for building my RN app
 
 - Fastlane: 3.5.2
 - Ruby 3.2.0
 
 here's my log
 '''
 > bundler: failed to load command: fastlane (/Users/vagrant/git/vendor/bundle/ruby/3.2.0/bin/fastlane)
 /Users/vagrant/git/vendor/bundle/ruby/3.2.0/gems/terminal-table-3.0.2/lib/t

## Section 6 — Builder guidance

When building a fix for an instance in fastlane/fastlane:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. fastlane/lib/fastlane/actions/zip.rb appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 7 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "fastlane/fastlane"`).

First 20 instance_ids:

- `fastlane__fastlane-19207` (dataset: `swe-bench-multilingual-test`)
- `fastlane__fastlane-19304` (dataset: `swe-bench-multilingual-test`)
- `fastlane__fastlane-19765` (dataset: `swe-bench-multilingual-test`)
- `fastlane__fastlane-20642` (dataset: `swe-bench-multilingual-test`)
- `fastlane__fastlane-20958` (dataset: `swe-bench-multilingual-test`)
- `fastlane__fastlane-20975` (dataset: `swe-bench-multilingual-test`)
- `fastlane__fastlane-21857` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
