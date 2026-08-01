---
name: swebench-rubocop__rubocop
description: SWE-bench repo behavioral spec for rubocop/rubocop. Aggregated from 16 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# rubocop/rubocop — SWE-bench Repo Spec

> **16 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 16 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `changelog/fix_interpolated_string_detection.md` | 1 |
| `lib/rubocop/cop/mixin/frozen_string_literal.rb` | 1 |
| `changelog/fix_return_exit_code_0_with_display_only_correctable.md` | 1 |
| `lib/rubocop/runner.rb` | 1 |
| `changelog/fix_false_positives_for_style_guard_clause.md` | 1 |
| `lib/rubocop/cop/style/guard_clause.rb` | 1 |
| `changelog/fix_false_positives_for_style_redundant_parenthese.md` | 1 |
| `lib/rubocop/cop/style/redundant_parentheses.rb` | 1 |
| `lib/rubocop/cop/style/safe_navigation.rb` | 1 |
| `changelog/fix_false_positives_for_style_safe_navigation.md` | 1 |
| `lib/rubocop/cop/layout/empty_lines_around_method_body.rb` | 1 |
| `lib/rubocop/cop/layout/block_alignment.rb` | 1 |
| `lib/rubocop/cop/mixin/range_help.rb` | 1 |
| `changelog/fix_fix_empty_lines_around_method_body_for_methods.md` | 1 |
| `lib/rubocop/cop/layout/leading_comment_space.rb` | 1 |
| `changelog/fix_update_layout_leading_comment_space_to_accept.md` | 1 |
| `lib/rubocop/cop/style/dig_chain.rb` | 1 |
| `changelog/fix_an_incorrect_autocorrect_for_style_dig_chain.md` | 1 |
| `lib/rubocop/cop/style/file_null.rb` | 1 |
| `changelog/fix_false_positives_for_style_file_null.md` | 1 |
| `lib/rubocop/cop/layout/line_continuation_spacing.rb` | 1 |
| `changelog/fix_update_layout_line_continuation_spacing_to_ignore.md` | 1 |
| `lib/rubocop/cop/style/empty_else.rb` | 1 |
| `lib/rubocop/cop/style/hash_syntax.rb` | 1 |
| `lib/rubocop/cop/style/multiple_comparison.rb` | 1 |
| `changelog/fix_false_negatives_for_style_multiple_comparison.md` | 1 |
| `lib/rubocop/cop/style/yoda_condition.rb` | 1 |
| `changelog/change_update_style_access_modifier_declarations_to_add.md` | 1 |
| `config/default.yml` | 1 |
| `lib/rubocop/cop/style/access_modifier_declarations.rb` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: allows "#$a" with freeze, allows "#@@a" with freeze, allows "#@a" with freeze, returns 0 if there are no offenses shown, does not register an offense when using a local variable assigned in a conditional expression in a branch**

Sample FAIL_TO_PASS test names (first 10):
```
  allows "#$a" with freeze
  allows "#@@a" with freeze
  allows "#@a" with freeze
  returns 0 if there are no offenses shown
  does not register an offense when using a local variable assigned in a conditional expression in a branch
  does not register an offense when using local variables assigned in multiple conditional expressions in a branch
  does not register an offense for parentheses around a method chain with `do`...`end` block in keyword argument
  does not register an offense for parentheses around a method chain with `do`...`end` block in keyword argument for safe navigation call
  does not register an offense for parentheses around a method chain with `do`...`end` numblock in keyword argument
  does not register an offense for parentheses around a method chain with `do`...`end` numblock in keyword argument for safe navigation call
```

## Section 4 — Problem-theme distribution

Top themes across 16 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| wrong_output | 13 | 81.2% |
| other | 3 | 18.8% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `rubocop__rubocop-13362`

**Files likely affected**: `changelog/fix_interpolated_string_detection.md`, `lib/rubocop/cop/mixin/frozen_string_literal.rb`
**FAIL_TO_PASS** (3 tests, first 3): `['allows "#$a" with freeze', 'allows "#@@a" with freeze', 'allows "#@a" with freeze']`

**Problem statement (excerpt):**
> 'Style/RedundantFreeze' does not consider variable interpolation as interpolation I often disable 'Style/VariableInterpolation' because I don't see any problems with strings like '"#@top/#@bottom"', I prefer this less verbose style. But 'Style/RedundantFreeze' doesn't consider this syntax as interpolation, so it thinks that the string is built frozen.
 
 ## Steps to reproduce
 
 File 'test.rb':
 

### Sample 2 — `rubocop__rubocop-13375`

**Files likely affected**: `changelog/fix_return_exit_code_0_with_display_only_correctable.md`, `lib/rubocop/runner.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['returns 0 if there are no offenses shown']`

**Problem statement (excerpt):**
> Exit status is inconsistent with the output when --display-only-correctable is on ## Expected behavior
 
 When Rubocop responds with "no offenses detected", I expect exit status to be 0 for CI to pass.
 This is not always the case when  --display-only-correctable flag is on. 
 
 ## Actual behavior
 
 When there are uncorrectable issues in the codebase and no correctable ones, 'rubocop --display-on

### Sample 3 — `rubocop__rubocop-13393`

**Files likely affected**: `changelog/fix_false_positives_for_style_guard_clause.md`, `lib/rubocop/cop/style/guard_clause.rb`
**FAIL_TO_PASS** (2 tests, first 3): `['does not register an offense when using a local variable assigned in a conditional expression in a branch', 'does not register an offense when using local variables assigned in multiple conditional expressions in a branch']`

**Problem statement (excerpt):**
> Style/GuardClause autocorrect results in non-running code --------
 
 ## Expected behavior
 
 Since Style/GuardClause is marked as safely autocorrectable rule, it should not replace working code with non-working.
 
 ## Actual behavior
 
 Please don't mind that the code itself is ugly, I'm working with legacy codebase and trying to apply Rubocop to setup. I created an example based on real-life cod

### Sample 4 — `rubocop__rubocop-13396`

**Files likely affected**: `changelog/fix_false_positives_for_style_redundant_parenthese.md`, `lib/rubocop/cop/style/redundant_parentheses.rb`
**FAIL_TO_PASS** (5 tests, first 3): `['does not register an offense for parentheses around a method chain with `do`...`end` block in keyword argument', 'does not register an offense for parentheses around a method chain with `do`...`end` block in keyword argument for safe navigation call', 'does not register an offense for parentheses around a method chain with `do`...`end` numblock in keyword argument']`

**Problem statement (excerpt):**
> 'Style/RedundantParentheses' are NOT redundant ## Expected behavior
 
 Describe here how you expected RuboCop to behave in this particular situation.
 
 '''ruby
 class MoneyController < ApplicationController
   def index
     render json: (ExchangeRate.supported_rates.map do |k, v|
       [k, v.select { |k, _v| %i[iso_code name symbol html_entity].include?(k) }.to_h]
     end.to_h.camelize)
   end

### Sample 5 — `rubocop__rubocop-13424`

**Files likely affected**: `lib/rubocop/cop/style/safe_navigation.rb`, `changelog/fix_false_positives_for_style_safe_navigation.md`
**FAIL_TO_PASS** (1 tests, first 3): `['allows an object check followed by 4 chained method calls with safe navigation']`

**Problem statement (excerpt):**
> Autocorrected safe navigation violates new navigation chain rules ## Expected behavior
 Autocorrect should not introduce futher errors. Either autocorrecting now expands safe navigation chains, ignores/encourages object checks, or the offence isn't autocorrectable). 
 
 ## Actual behavior
 Was getting a warning from rubocop upon updating to 1.68.0 that the navigation chains were too long. Code tha

### Sample 6 — `rubocop__rubocop-13431`

**Files likely affected**: `lib/rubocop/cop/layout/empty_lines_around_method_body.rb`, `lib/rubocop/cop/layout/block_alignment.rb`, `lib/rubocop/cop/mixin/range_help.rb`, `changelog/fix_fix_empty_lines_around_method_body_for_methods.md`
**FAIL_TO_PASS** (2 tests, first 3): `['registers an offense for methods with empty lines and arguments spanning multiple lines', 'registers an offense for methods with empty lines, empty arguments spanning multiple lines']`

**Problem statement (excerpt):**
> EmptyLinesAroundMethodBody false negative if method has arguments spanning multiple lines ## Expected behavior
 
 With ['Layout/EmptyLinesAroundMethodBody'](https://docs.rubocop.org/rubocop/cops_layout.html#layoutemptylinesaroundmethodbody), I'd expect the following:
 
 '''
 # good
 
 def foo(
   arg
 )
   # ...
 end
 
 # bad
 
 def bar(
   arg
 )
 
   # ...
 end
 '''
 
 ## Actual behavior
 
 The 

### Sample 7 — `rubocop__rubocop-13479`

**Files likely affected**: `lib/rubocop/cop/layout/leading_comment_space.rb`, `changelog/fix_update_layout_leading_comment_space_to_accept.md`
**FAIL_TO_PASS** (1 tests, first 3): `['does not register an offense for a multiline shebang starting on the first line']`

**Problem statement (excerpt):**
> Multiline shebangs vs Layout/LeadingCommentSpace ## Is your feature request related to a problem? Please describe.
 
 Some tools allow multi-line shebangs - eg in this nix-shell script that runs a reproducible version of ruby + some associated packages:
 
 
 '''ruby
 #!/usr/bin/env nix-shell
 #! nix-shell -i ruby --pure
 #! nix-shell -p ruby gh git
 #! nix-shell -I nixpkgs=https://github.com/NixOS

### Sample 8 — `rubocop__rubocop-13503`

**Files likely affected**: `lib/rubocop/cop/style/dig_chain.rb`, `changelog/fix_an_incorrect_autocorrect_for_style_dig_chain.md`
**FAIL_TO_PASS** (1 tests, first 3): `['registers an offense and corrects with safe navigation method chain']`

**Problem statement (excerpt):**
> Wrong autocorrect for 'Style/DigChain' ## Expected behavior.
 '''
 hoge = [{ a: { b: 'b' } }, nil].sample
 hoge&.dig(:a)&.dig(:b)
 '''
 
 After running 'rubocop -A'
 
 '''
 hoge&.dig(:a, :b)
 '''
 
 
 ## Actual behavior.
 '''
 hoge&.dig(:a)&.dig(:b)
 '''
 
 After running 'rubocop -A'.
 
 '''
 hoge & dig(:a, :b)
 '''
 
  Output of ''rubocop --debug''.
 
 '''
 Offenses: test.rb:3:5: C: [Corrected] L

## Section 6 — Builder guidance

When building a fix for an instance in rubocop/rubocop:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. changelog/fix_interpolated_string_detection.md appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 16 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "rubocop/rubocop"`).

First 20 instance_ids:

- `rubocop__rubocop-13362` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13375` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13393` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13396` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13424` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13431` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13479` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13503` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13560` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13579` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13627` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13653` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13668` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13680` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13687` (dataset: `swe-bench-multilingual-test`)
- `rubocop__rubocop-13705` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
