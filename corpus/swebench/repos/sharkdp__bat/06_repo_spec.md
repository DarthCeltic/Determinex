---
name: swebench-sharkdp__bat
description: SWE-bench repo behavioral spec for sharkdp/bat. Aggregated from 18 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# sharkdp/bat — SWE-bench Repo Spec

> **18 bug-fix instances** across 2 dataset(s); language(s): python, rust.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 10 |
| swe-bench-multilingual-test | 8 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `CHANGELOG.md` | 14 |
| `src/bin/bat/clap_app.rs` | 7 |
| `src/bin/bat/app.rs` | 6 |
| `Cargo.lock` | 5 |
| `src/bin/bat/main.rs` | 4 |
| `src/printer.rs` | 4 |
| `Cargo.toml` | 4 |
| `src/syntax_mapping.rs` | 3 |
| `src/assets.rs` | 3 |
| `src/pretty_printer.rs` | 3 |
| `doc/long-help.txt` | 2 |
| `doc/short-help.txt` | 2 |
| `assets/manual/bat.1.in` | 2 |
| `src/lib.rs` | 2 |
| `src/input.rs` | 2 |
| `src/controller.rs` | 2 |
| `src/assets/ignored_suffixes.rs` | 1 |
| `src/syntax_mapping/ignored_suffixes.rs` | 1 |
| `src/bin/bat/assets.rs` | 1 |
| `src/clap_app.rs` | 1 |
| `README.md` | 1 |
| `.gitignore` | 1 |
| `assets/completions/bat.zsh.in` | 1 |
| `assets/completions/bat.fish.in` | 1 |
| `assets/completions/_bat.ps1.in` | 1 |
| `assets/completions/bat.bash.in` | 1 |
| `src/bin/bat/config.rs` | 1 |
| `src/theme.rs` | 1 |
| `src/config.rs` | 1 |
| `src/vscreen.rs` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: ignored_suffix_arg, disable_pager_if_disable_paging_flag_comes_after_paging, map_syntax_and_ignored_suffix_work_together, cache_clear, highlighting_independant_from_map_syntax_case**

Sample FAIL_TO_PASS test names (first 10):
```
  ignored_suffix_arg
  disable_pager_if_disable_paging_flag_comes_after_paging
  map_syntax_and_ignored_suffix_work_together
  cache_clear
  highlighting_independant_from_map_syntax_case
  header_very_narrow_terminal
  paging_does_not_override_simple_plain
  simple_plain_does_not_override_paging
  does_not_print_unwanted_file_named_cache
```

## Section 4 — Problem-theme distribution

Top themes across 18 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| config_environment | 2 | 25.0% |
| other | 2 | 25.0% |
| encoding_unicode | 1 | 12.5% |
| json_serialization | 1 | 12.5% |
| wrong_output | 1 | 12.5% |
| regression | 1 | 12.5% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `sharkdp__bat-1892`

**Files likely affected**: `src/assets/ignored_suffixes.rs`, `src/bin/bat/clap_app.rs`, `CHANGELOG.md`, `src/bin/bat/app.rs`, `src/syntax_mapping.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['ignored_suffix_arg']`

**Problem statement (excerpt):**
> Support '--ignored-suffix' to ignore filename suffix in https://github.com/sharkdp/bat/pull/1687, it supported to ignoring known backup/template filename suffixes.
 
 Hopes we can also custom the ignored suffixes in '~/.config/bat/config', 
 
 for example:
 
 - .env.example
 - .env.production
 - config.json.production
 
 We can configure bat in '~/.config/bat/config':
 
 '''bash
 # ~/.config/bat/c

### Sample 2 — `sharkdp__bat-2201`

**Files likely affected**: `CHANGELOG.md`, `src/bin/bat/clap_app.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['disable_pager_if_disable_paging_flag_comes_after_paging']`

**Problem statement (excerpt):**
> Short options '-P' and '-pp' do not take precedence over '--paging=always' set in '~/.config/bat/config' <!-- Hey there, thank you for creating an issue! -->
 
 **Describe the bug you encountered:**
 
 I set '--paging=always' in my '~/.config/bat/config' file. Then I can turn paging off by issuing the long option 'bat --paging=never'. However neither 'bat -P' or 'bat -pp' work.
 
 Note: this issue

### Sample 3 — `sharkdp__bat-2260`

**Files likely affected**: `src/syntax_mapping.rs`, `CHANGELOG.md`
**FAIL_TO_PASS** (1 tests, first 3): `['map_syntax_and_ignored_suffix_work_together']`

**Problem statement (excerpt):**
> The options --map-syntax and --ignored-suffix cannot work together. **Describe the bug you encountered:**
 
 The options '--map-syntax' and '--ignored-suffix' cannot work together.
 
 How to reproduce it:
 
 1.  Prepare a file 'foo.demo' in YAML syntax:
 
     '''yaml
     # file: foo.demo
     foo: "bar"
     '''
 
 2. Use 'bat --map-syntax "*.demo:YAML" foo.demo' can print it with YAML syntax hi

### Sample 4 — `sharkdp__bat-2393`

**Files likely affected**: `src/bin/bat/main.rs`, `CHANGELOG.md`, `src/bin/bat/assets.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['cache_clear']`

**Problem statement (excerpt):**
> 'bat cache --clear' should clear the '--target' dir if specified While 'bat cache --clear' accepts a '--target' dir argument, it always clears the default cache dir regardless of '--target'.
 
 Instead, 'bat cache --clear' should clear the '--target' dir if one is provided.
 
 Fixing this would allow the 'bat cache --clear' function to be tested in an temporary directory. The relevant test is alre

### Sample 5 — `sharkdp__bat-2650`

**Files likely affected**: `src/syntax_mapping.rs`, `CHANGELOG.md`
**FAIL_TO_PASS** (1 tests, first 3): `['highlighting_independant_from_map_syntax_case']`

**Problem statement (excerpt):**
> bat language coloring detection seems to be case sensitive on Windows I have a nuget config file, named NuGet.Config.
 '''xml
 <?xml version="1.0" encoding="utf-8"?>
 <configuration>
   <solution>
     <add key="disableSourceControlIntegration" value="true" />
   </solution>
 </configuration>
 '''
 
 I also have the '.config' extension mapped to XML in my bat config file: 
 '--map-syntax='*.config

### Sample 6 — `sharkdp__bat-2835`

**Files likely affected**: `CHANGELOG.md`, `src/printer.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['header_very_narrow_terminal']`

**Problem statement (excerpt):**
> Long file paths break header <!--
 
 Hey there, thank you for reporting a bug!
 
 Please note that the following bugs have already been reported:
 
 * dpkg: error processing archive /some/path/some-program.deb (--unpack):
   trying to overwrite '/usr/.crates2.json'
 
   See https://github.com/sharkdp/bat/issues/938
 
 -->
 
 **What steps will reproduce the bug?**
 
 1. Run bat with a very very lon

### Sample 7 — `sharkdp__bat-3108`

**Files likely affected**: `CHANGELOG.md`, `src/bin/bat/clap_app.rs`, `src/bin/bat/app.rs`
**FAIL_TO_PASS** (2 tests, first 3): `['paging_does_not_override_simple_plain', 'simple_plain_does_not_override_paging']`

**Problem statement (excerpt):**
> [bat --paging=never --plain] still paging, since version 0.24.0 <!--
 
 Hey there, thank you for reporting a bug!
 
 Please note that the following bugs have already been reported:
 
 * dpkg: error processing archive /some/path/some-program.deb (--unpack):
   trying to overwrite '/usr/.crates2.json'
 
   See https://github.com/sharkdp/bat/issues/938
 
 -->
 
 **What steps will reproduce the bug?**

### Sample 8 — `sharkdp__bat-562`

**Files likely affected**: `Cargo.lock`, `src/clap_app.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['does_not_print_unwanted_file_named_cache']`

**Problem statement (excerpt):**
> Bat is broken for filenames that are prefixes of "cache" The issue with files named "cache" was already identified in #245 and fixed in #275. However, the 'clap' parser doesn't require an exact match: any prefix of the subcommand "cache" will do. So if you try 'bat c' (or "ca", "cac", "cach"), one of the following will happen:
 
 1. If there is a file named "cache", it will print that instead (the

## Section 6 — Builder guidance

When building a fix for an instance in sharkdp/bat:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. CHANGELOG.md appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 18 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "sharkdp/bat"`).

First 20 instance_ids:

- `sharkdp__bat-1892` (dataset: `swe-bench-multilingual-test`)
- `sharkdp__bat-2201` (dataset: `swe-bench-multilingual-test`)
- `sharkdp__bat-2260` (dataset: `swe-bench-multilingual-test`)
- `sharkdp__bat-2393` (dataset: `swe-bench-multilingual-test`)
- `sharkdp__bat-2650` (dataset: `swe-bench-multilingual-test`)
- `sharkdp__bat-2835` (dataset: `swe-bench-multilingual-test`)
- `sharkdp__bat-3108` (dataset: `swe-bench-multilingual-test`)
- `sharkdp__bat-562` (dataset: `swe-bench-multilingual-test`)
- `sharkdp__bat-3189` (dataset: `multi-swe-bench`)
- `sharkdp__bat-3108` (dataset: `multi-swe-bench`)
- `sharkdp__bat-3075` (dataset: `multi-swe-bench`)
- `sharkdp__bat-2896` (dataset: `multi-swe-bench`)
- `sharkdp__bat-2665` (dataset: `multi-swe-bench`)
- `sharkdp__bat-2544` (dataset: `multi-swe-bench`)
- `sharkdp__bat-1518` (dataset: `multi-swe-bench`)
- `sharkdp__bat-1402` (dataset: `multi-swe-bench`)
- `sharkdp__bat-1276` (dataset: `multi-swe-bench`)
- `sharkdp__bat-1197` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
