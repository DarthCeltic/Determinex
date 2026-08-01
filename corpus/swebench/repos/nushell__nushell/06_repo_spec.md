---
name: swebench-nushell__nushell
description: SWE-bench repo behavioral spec for nushell/nushell. Aggregated from 19 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# nushell/nushell — SWE-bench Repo Spec

> **19 bug-fix instances** across 2 dataset(s); language(s): python, rust.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 14 |
| swe-bench-multilingual-test | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `crates/nu-parser/src/parser.rs` | 5 |
| `crates/nu-command/src/system/run_external.rs` | 4 |
| `crates/nu-engine/src/eval.rs` | 3 |
| `crates/nu-engine/src/eval_ir.rs` | 2 |
| `Cargo.lock` | 2 |
| `src/main.rs` | 2 |
| `crates/nu-parser/src/parse_keywords.rs` | 2 |
| `crates/nu-command/src/filters/find.rs` | 1 |
| `crates/nu-command/src/filesystem/ls.rs` | 1 |
| `crates/nu-command/src/strings/split/column.rs` | 1 |
| `crates/nu-command/src/filters/tee.rs` | 1 |
| `crates/nu-cmd-lang/src/core_commands/do_.rs` | 1 |
| `crates/nu-command/src/env/config/config_nu.rs` | 1 |
| `crates/nu-protocol/src/process/child.rs` | 1 |
| `crates/nu-command/src/env/config/config_env.rs` | 1 |
| `crates/nu-command/src/filesystem/save.rs` | 1 |
| `crates/nu-protocol/src/pipeline/byte_stream.rs` | 1 |
| `crates/nu-protocol/src/config/display_errors.rs` | 1 |
| `crates/nu-cmd-lang/src/core_commands/describe.rs` | 1 |
| `crates/nu-cmd-lang/src/example_support.rs` | 1 |
| `crates/nu-parser/src/flatten.rs` | 1 |
| `crates/nu-protocol/src/ast/pipeline.rs` | 1 |
| `crates/nu-protocol/src/ast/expression.rs` | 1 |
| `crates/nu-protocol/src/ast/expr.rs` | 1 |
| `crates/nu-protocol/src/eval_const.rs` | 1 |
| `crates/nu-protocol/src/debugger/profiler.rs` | 1 |
| `crates/nu-protocol/src/ir/display.rs` | 1 |
| `crates/nu-protocol/src/ast/block.rs` | 1 |
| `crates/nu-protocol/src/ir/mod.rs` | 1 |
| `crates/nuon/src/from.rs` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: shell::environment::env::hides_environment_from_child, shell::pipeline::commands::external::pass_dot_as_external_arguments, commands::find::find_with_bytestream_search_with_char, commands::ls::list_symlink_with_full_path, commands::split_column::to_column**

Sample FAIL_TO_PASS test names (first 10):
```
  shell::environment::env::hides_environment_from_child
  shell::pipeline::commands::external::pass_dot_as_external_arguments
  commands::find::find_with_bytestream_search_with_char
  commands::ls::list_symlink_with_full_path
  commands::split_column::to_column
```

## Section 4 — Problem-theme distribution

Top themes across 19 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| wrong_output | 2 | 40.0% |
| other | 2 | 40.0% |
| config_environment | 1 | 20.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `nushell__nushell-12901`

**Files likely affected**: `crates/nu-command/src/system/run_external.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['shell::environment::env::hides_environment_from_child']`

**Problem statement (excerpt):**
> Child processes can inherit initial environment variables after 'hide-env' ### Describe the bug  When we spawn child processes, we do not clear environment variables. This means it is possible for child processes to inherit environment variables that are supposed to be hidden via 'hide-env'.  ### How to reproduce  1. set a environment variable in the parent shell.
   '''nushell
   $env.TEST = 1
  

### Sample 2 — `nushell__nushell-12950`

**Files likely affected**: `crates/nu-command/src/system/run_external.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['shell::pipeline::commands::external::pass_dot_as_external_arguments']`

**Problem statement (excerpt):**
> git add cannot add file with path . ### Describe the bug
 
 cannot use 'git add .' to add file to git 
 
 $ git add . 
 fatal: empty string is not a valid pathspec. please use . instead if you meant to match all paths
 
 ### How to reproduce
 
 1. add some new file to a git repo
 2. run 'git add . ' to add file 
 
 ### Expected behavior
 
 should add file with 'git add .' not git add ./file1' 
 
 

### Sample 3 — `nushell__nushell-13246`

**Files likely affected**: `crates/nu-command/src/filters/find.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['commands::find::find_with_bytestream_search_with_char']`

**Problem statement (excerpt):**
> 'find' command incorrectly output the result as lowercase To reproduce: '''nushell > "ABC" | save foo.txt; open "foo.txt" | find "ABC"  ╭───┬─────╮ │ 0 │ abc │ ╰───┴─────╯ '''  'git bisect' showed that the bug was introduced by #12774.  <!-- Edit the body of your new issue then click the ✓ "Create Issue" button in the top right of the editor. The first line will be the issue title. Assignees and L

### Sample 4 — `nushell__nushell-13605`

**Files likely affected**: `crates/nu-command/src/filesystem/ls.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['commands::ls::list_symlink_with_full_path']`

**Problem statement (excerpt):**
> 'ls -f' should output absolute path for symlinks in 'target' column ### Describe the bug
 
 'help ls' says:
 '''
 help ls | find "full-path"
 ╭───┬──────────────────────────────────────────────────────╮
 │ 0 │   -f, --full-paths - display paths as absolute paths │
 ╰───┴──────────────────────────────────────────────────────╯
 '''
 'ls -l' outputs the symlink target in the 'target' column, which is

### Sample 5 — `nushell__nushell-13831`

**Files likely affected**: `crates/nu-command/src/strings/split/column.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['commands::split_column::to_column']`

**Problem statement (excerpt):**
> Add --number flag to split column ### Related problem
 
 I'm trying to parse CSV-like strings, like the output of 'getent hosts', which may contain the separator in the last column. 'split row' already has the '-n'/'--number' flag, which allows the number of items returned to be limited. As far as I can tell, there's currently no way to do the same for columns.
 
 ### Describe the solution you'd l

## Section 6 — Builder guidance

When building a fix for an instance in nushell/nushell:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. crates/nu-parser/src/parser.rs appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 19 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "nushell/nushell"`).

First 20 instance_ids:

- `nushell__nushell-12901` (dataset: `swe-bench-multilingual-test`)
- `nushell__nushell-12950` (dataset: `swe-bench-multilingual-test`)
- `nushell__nushell-13246` (dataset: `swe-bench-multilingual-test`)
- `nushell__nushell-13605` (dataset: `swe-bench-multilingual-test`)
- `nushell__nushell-13831` (dataset: `swe-bench-multilingual-test`)
- `nushell__nushell-13870` (dataset: `multi-swe-bench`)
- `nushell__nushell-13357` (dataset: `multi-swe-bench`)
- `nushell__nushell-12901` (dataset: `multi-swe-bench`)
- `nushell__nushell-12118` (dataset: `multi-swe-bench`)
- `nushell__nushell-11948` (dataset: `multi-swe-bench`)
- `nushell__nushell-11672` (dataset: `multi-swe-bench`)
- `nushell__nushell-11493` (dataset: `multi-swe-bench`)
- `nushell__nushell-11292` (dataset: `multi-swe-bench`)
- `nushell__nushell-11169` (dataset: `multi-swe-bench`)
- `nushell__nushell-10629` (dataset: `multi-swe-bench`)
- `nushell__nushell-10613` (dataset: `multi-swe-bench`)
- `nushell__nushell-10405` (dataset: `multi-swe-bench`)
- `nushell__nushell-10395` (dataset: `multi-swe-bench`)
- `nushell__nushell-10381` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
