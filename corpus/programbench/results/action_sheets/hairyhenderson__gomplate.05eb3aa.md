# Action Sheet — hairyhenderson__gomplate.05eb3aa

**Current:** 1.49%  (52/3496)
**Pass / Fail / Skip:** 52 / 1340 / 0
**Gap to 100%:** 98.51 percentage points (3444 tests)

## Failure clusters

1340 failed tests grouped into 4 buckets (sorted by count).

### `rc_mismatch_got1_want0` — 940 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_additional_functions.test_coll_pick`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-i', '{{ $m := coll.Dict "a" 1 "b" 2 "c" 3 }}{{ $picked := coll.Pick "a" "c" $m }}{{ $picked.a }}'], returncode=1, stdout=b'', stderr=b' 
- `tests.test_additional_functions.test_coll_omit`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-i', '{{ $m := coll.Dict "a" 1 "b" 2 "c" 3 }}{{ $omitted := coll.Omit "b" $m }}{{ coll.Has $omitted "b" }}'], returncode=1, stdout=b'', s
- `tests.test_additional_functions.test_coll_append`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-i', '{{ $s := coll.Slice 1 2 3 }}{{ $appended := coll.Append $s 4 5 }}{{ len $appended }}'], returncode=1, stdout=b'', stderr=b'  File "
- *(... 937 more in this cluster)*

### `other_assertion` — 396 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_handling.test_invalid_flag_combination_in_and_file`
  > assert (b'only one of' in b'  File "/workspace/main.py", line 201\n    {\'argv\': [\'--template\', \'{{"hello"}}\', \'--output\', \'/dev/null\', \'--exec-pipe\'], \'rc\': 2, \'stderr\': \'flag needs a
  >  +  where b'  File "/workspace/main.py", line 201\n    {\'argv\': [\'--template\', \'{{"hello"}}\', \'--output\', \'/dev/null\', \'--exec-pipe\'], \'rc\': 2, \'stderr\': \'flag needs an argument: --ex
  >  +  and   b'  File "/workspace/main.py", line 201\n    {\'argv\': [\'--template\', \'{{"hello"}}\', \'--output\', \'/dev/null\', \'--exec-pipe\'], \'rc\': 2, \'stderr\': \'flag needs an argument: --ex
- `tests.test_error_handling.test_input_output_count_mismatch`
  > assert b'same number' in b'  File "/workspace/main.py", line 201\n    {\'argv\': [\'--template\', \'{{"hello"}}\', \'--output\', \'/dev/null\', \'--exec-pipe\'], \'rc\': 2, \'stderr\': \'flag needs an
  >  +  where b'  File "/workspace/main.py", line 201\n    {\'argv\': [\'--template\', \'{{"hello"}}\', \'--output\', \'/dev/null\', \'--exec-pipe\'], \'rc\': 2, \'stderr\': \'flag needs an argument: --ex
- `tests.test_test_functions.test_test_fail`
  > assert b'failure message' in b'  File "/workspace/main.py", line 201\n    {\'argv\': [\'--template\', \'{{"hello"}}\', \'--output\', \'/dev/null\', \'--exec-pipe\'], \'rc\': 2, \'stderr\': \'flag need
  >  +  where b'  File "/workspace/main.py", line 201\n    {\'argv\': [\'--template\', \'{{"hello"}}\', \'--output\', \'/dev/null\', \'--exec-pipe\'], \'rc\': 2, \'stderr\': \'flag needs an argument: --ex
- *(... 393 more in this cluster)*

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_help_has_flags_section`
  > assert None
  >  +  where None = <function search at 0x7fe5297ae680>('(?m)^Flags:\\s*$', '')
  >  +    where <function search at 0x7fe5297ae680> = re.search
  >  +    and   '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 201\n    {\'argv\': [\'--template\', \'{{"hello"}}\', \'-
- `eval.tests.test_help_usage.test_help_contains_expected_indentation_for_short_long_flag_pair`
  > assert None
  >  +  where None = <function search at 0x7fe5297ae680>('(?m)^\\s*-d, --datasource datasource\\s{2,}datasource in alias=URL form\\.', '')
  >  +    where <function search at 0x7fe5297ae680> = re.search
  >  +    and   '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 201\n    {\'argv\': [\'--template\', \'{{"hello"}}\', \'-

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_usage.test_help_trailing_newline_present`
  > assert False
  >  +  where False = <built-in method endswith of str object at 0x7fe529838030>('\n')
  >  +    where <built-in method endswith of str object at 0x7fe529838030> = ''.endswith
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 201\n    {\'argv\': [\'--template\', \'{{"hello"}}\', \
- `eval.tests.test_gomplate_behavior.test_env_var_missing_errors_and_nonzero_exit`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x7ff190874030>('Hello, ')
  >  +    where <built-in method startswith of str object at 0x7ff190874030> = ''.startswith
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '-i', 'Hello, {{ .Env.USER }}'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 201\n    {\'argv\': [\'--template

