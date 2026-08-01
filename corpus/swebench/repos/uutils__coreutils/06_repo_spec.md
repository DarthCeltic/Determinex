---
name: swebench-uutils__coreutils
description: SWE-bench repo behavioral spec for uutils/coreutils. Aggregated from 5 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# uutils/coreutils — SWE-bench Repo Spec

> **5 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/uu/env/src/env.rs` | 1 |
| `.vscode/cspell.dictionaries/workspace.wordlist.txt` | 1 |
| `src/uu/cksum/src/cksum.rs` | 1 |
| `src/uucore/src/lib/lib.rs` | 1 |
| `src/uu/mkdir/src/mkdir.rs` | 1 |
| `src/uu/cp/src/cp.rs` | 1 |
| `src/uu/tr/src/tr.rs` | 1 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  test_env::test_env_arg_ignore_signal_empty
  test_env::test_env_arg_ignore_signal_special_signals
  test_env::test_env_arg_ignore_signal_invalid_signals
  test_env::test_env_arg_ignore_signal_valid_signals
  test_cksum::test_non_utf8_filename
  test_mkdir::test_mkdir_parent_mode_skip_existing_last_component_chmod
  test_cp::test_cp_no_file
  test_tr::test_trailing_backslash
```

## Section 4 — Problem-theme distribution

Top themes across 5 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 3 | 60.0% |
| encoding_unicode | 1 | 20.0% |
| regression | 1 | 20.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `uutils__coreutils-6377`

**Files likely affected**: `src/uu/env/src/env.rs`, `.vscode/cspell.dictionaries/workspace.wordlist.txt`
**FAIL_TO_PASS** (4 tests, first 3): `['test_env::test_env_arg_ignore_signal_empty', 'test_env::test_env_arg_ignore_signal_special_signals', 'test_env::test_env_arg_ignore_signal_invalid_signals']`

**Problem statement (excerpt):**
> 'env': implement '--ignore-signal' '''
 
        --ignore-signal[=SIG]
               set handling of SIG signal(s) to do nothing
 ''' 

### Sample 2 — `uutils__coreutils-6575`

**Files likely affected**: `src/uu/cksum/src/cksum.rs`, `src/uucore/src/lib/lib.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['test_cksum::test_non_utf8_filename']`

**Problem statement (excerpt):**
> cksum: can't handle non-UTF-8 filenames On linux (and some other platforms), filenames aren't necessarily valid UTF-8. We shouldn't claim that the argument is invalid in those cases:
 
 '''console
 $ touch $'funky\xffname'
 $ cksum $'funky\xffname'
 4294967295 0 funky�name
 $ cargo run -q cksum $'funky\xffname'
 error: invalid UTF-8 was detected in one or more arguments
 
 Usage: target/debug/core

### Sample 3 — `uutils__coreutils-6682`

**Files likely affected**: `src/uu/mkdir/src/mkdir.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['test_mkdir::test_mkdir_parent_mode_skip_existing_last_component_chmod']`

**Problem statement (excerpt):**
> mkdir -p fails on existing directories that the current user doesn't have permission to access I stumbled upon this from a weird 'ansible' error.
 
 '''
  $ ansible -m ping <redacted-hostname> --become-user unprivileged-user
 <redacted-hostname> | UNREACHABLE! => {
     "changed": false,
     "msg": "Failed to create temporary directory. In some cases, you may have been able to authenticate and di

### Sample 4 — `uutils__coreutils-6690`

**Files likely affected**: `src/uu/cp/src/cp.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['test_cp::test_cp_no_file']`

**Problem statement (excerpt):**
> Zsh completion broken for 'cp' Hi,
 
 After installing through [pacman](https://archlinux.org/packages/extra/x86_64/uutils-coreutils/files/), the zsh completion for cp seems broken.
 
 When I type in 'cp file <Tab>', zsh suggests only the flags, and I have to type the target path without completion. This does not seem to be the case with 'mv', and I haven't found it anywhere else either. 

### Sample 5 — `uutils__coreutils-6731`

**Files likely affected**: `src/uu/tr/src/tr.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['test_tr::test_trailing_backslash']`

**Problem statement (excerpt):**
> tr: doesn't warn about unescaped trailing backslash '''console
 $ true | tr '\\\' 'asdf'
 tr: warning: an unescaped backslash at end of string is not portable
 $ true | cargo run -q --features tr -- tr '\\\' 'asdf'
 $
 '''
 
 Found while reading #6713. Root cause is that the "escapedness"-property is being guessed based on the last two characters, even though it depends on whether the total amount

## Section 6 — Builder guidance

When building a fix for an instance in uutils/coreutils:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/uu/env/src/env.rs appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 5 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "uutils/coreutils"`).

First 20 instance_ids:

- `uutils__coreutils-6377` (dataset: `swe-bench-multilingual-test`)
- `uutils__coreutils-6575` (dataset: `swe-bench-multilingual-test`)
- `uutils__coreutils-6682` (dataset: `swe-bench-multilingual-test`)
- `uutils__coreutils-6690` (dataset: `swe-bench-multilingual-test`)
- `uutils__coreutils-6731` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
