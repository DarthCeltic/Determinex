# Action Sheet — sharkdp__hyperfine.327d5f4

**Current:** 41.95%  (125/298)
**Pass / Fail / Skip:** 125 / 173 / 0
**Gap to 100%:** 58.05 percentage points (173 tests)

## Failure clusters

173 failed tests grouped into 8 buckets (sorted by count).

### `other_assertion` — 59 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_command_timer.test_shell_none_mode_direct_execution`
  > AssertionError: With --shell=none, $HOME must NOT be expanded and should fail to execute
  > assert "Error: Failed to run command '$HOME':" in ''
  >  +  where '' = CompletedProcess(args=['/workspace/executable', '--runs', '1', '--shell=none', '-i', 'echo', '$HOME'], returncode=0, stdout="Benchmark 1: echo\n  Time (mean ± σ):     2.0 ms ± 100.0 ms 
- `tests.test_command_timer.test_timer_captures_cpu_time_and_memory`
  > AssertionError: Missing required field: memory_usage_byte
  > assert 'memory_usage_byte' in {'command': "python3 -c 'sum(range(100000))'", 'exit_codes': [0, 0, 0], 'max': 0.022206145993550308, 'mean': 0.019333847997283254, ...}
- `tests.test_command_timer.test_timer_wall_clock_vs_cpu_time_difference`
  > AssertionError: CPU time (0.046s) should be much less than wall-clock time (0.052s) for sleep
  > assert 0.046481456396577414 < (0.05164606266286379 * 0.5)
- *(... 56 more in this cluster)*

### `rc_unexpected_zero` — 51 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_command_timer.test_duplicate_parameter_names_error`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-L', 'x', '1,2', '-L', 'x', '3,4', 'echo {x}'], returncode=0, stdout="Benchmark 1: echo 3\n  Time (mean ± σ):     869.0 µs ± 434.2 µs    
- `tests.test_command_timer.test_command_name_count_mismatch_error`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--parameter-scan', 'val', '1', '3', 'echo {val}', '--command-name', 'a', '--command-name', 'b'], returncode=0, stdout="Benchmark 1: a\n  
- `tests.test_edge_cases.test_parseint_error_in_parameter_scan`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-P', 'x', 'abc', '10', 'echo {x}'], returncode=0, stdout="Benchmark 1: echo abc\n  Time (mean ± σ):     1.1 ms ± 182.7 ms    [User: 1.0 m
- *(... 48 more in this cluster)*

### `string_output_mismatch` — 33 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_command_timer.test_parameter_substitution_no_overlapping`
  > AssertionError: assert ['echo a baz'...ho quux quux'] == ['echo a baz'...o {bar} quux']
  >   
  >   At index 1 diff: 'echo a quux' != 'echo {bar} baz'
  >   
  >   Full diff:
  >     [
  >         'echo a baz',
  >   -     'echo {bar} baz',...
- `tests.test_command_timer.test_parameter_scan_with_command_name_substitution`
  > AssertionError: assert ['cmd-{val}',... 2', 'echo 3'] == ['cmd-1', 'cmd-2', 'cmd-3']
  >   
  >   At index 0 diff: 'cmd-{val}' != 'cmd-1'
  >   
  >   Full diff:
  >     [
  >   -     'cmd-1',
  >   ?          ^...
- `tests.test_edge_cases.test_zero_step_parameter_error`
  > AssertionError: assert 'error: Found...COMMAND>...\n' == 'Error: Zero ...ameter step\n'
  >   
  >   - Error: Zero is not a valid parameter step
  >   + error: Found argument '-D' which wasn't expected
  >   + USAGE:
  >   +     hyperfine [OPTIONS] <COMMAND>...
- *(... 30 more in this cluster)*

### `rc_mismatch_got1_want0` — 23 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_edge_cases.test_valid_decimal_range_with_step`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-P', 'x', '0.5', '1.5', '-D', '0.5', '--runs', '1', 'echo {x}'], returncode=1, stdout="error: Found argument '-D' which wasn't expected\n
- `tests.test_edge_cases.test_decimal_parameter_precision`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-P', 'x', '0.1', '0.3', '-D', '0.1', '--runs', '1', 'echo {x}'], returncode=1, stdout="error: Found argument '-D' which wasn't expected\n
- `tests.test_edge_cases.test_parameter_step_larger_than_range`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-P', 'x', '1', '5', '-D', '10', '--runs', '1', 'echo {x}'], returncode=1, stdout="error: Found argument '-D' which wasn't expected\nUSAGE
- *(... 20 more in this cluster)*

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_command_timer.test_parameter_list_cartesian_product`
  > AssertionError: assert ['echo 1-a', ...', 'echo 2-b'] == ['echo 1-a', ...', 'echo 2-b']
  >   
  >   At index 1 diff: 'echo 1-b' != 'echo 2-a'
  >   
  >   Full diff:
  >     [
  >         'echo 1-a',
  >   +     'echo 1-b',...
- `tests.test_parameters.test_multiple_parameters_cartesian_product`
  > AssertionError: assert 'Benchmark 1:... echo x=2_y=b' == 'Benchmark 1:..._y=b\nx=2_y=b'
  >   
  >     Benchmark 1: echo x=1_y=a
  >   - x=1_y=a
  >   - x=1_y=a
  >     
  >   - Benchmark 2: echo x=2_y=a
  >   ?                     ^   ^...
- `tests.test_parameters.test_three_parameter_combination`
  > AssertionError: assert 'Benchmark 1:...k 8: echo 2yB' == 'Benchmark 1:...k 8: echo 2yB'
  >   
  >     Benchmark 1: echo 1xA
  >     
  >   - Benchmark 2: echo 2xA
  >   ?                   ^ ^
  >   + Benchmark 2: echo 1xB
  >   ?                   ^ ^...

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_errors_warnings.test_long_command_line_handling`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fce119ff760>('Time \\(abs ≡\\):\\s+\\d+\\.\\d+ [µm]s\\s+\\[User: \\d+\\.\\d+ [µm]s, System: \\d+\\.\\d+ [µm]s\\]', 'Benchmark 1: echo aaaaaaaaaaaaaaaaaaaaaaaaaa
  >  +    where <function search at 0x7fce119ff760> = <module 're' from '/usr/lib/python3.10/re.py'>.search
  >  +    and   'Benchmark 1: echo aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
- `tests.test_errors_warnings.test_command_with_special_shell_characters`
  > assert None
  >  +  where None = <function search at 0x7fce119ff760>('Time \\(abs ≡\\):\\s+\\d+\\.\\d+ [µm]s\\s+\\[User: \\d+\\.\\d+ [µm]s, System: \\d+\\.\\d+ [µm]s\\]', 'Benchmark 1: echo "test$USER"\n  Time (mean 
  >  +    where <function search at 0x7fce119ff760> = <module 're' from '/usr/lib/python3.10/re.py'>.search
  >  +    and   'Benchmark 1: echo "test$USER"\n  Time (mean ± σ):     814.6 µs ± 100.0 µs    [User: 1.0 ms, System: 1.0 ms]\n  Range (min … max):   814.6 µs … 814.6 µs    1 runs\n\n' = CompletedProcess(a

### `rc_mismatch_got2_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_comparison.test_reference_equal_ordering_case`
  > AssertionError: assert 2 == 3
  >  +  where 2 = len([{'command': 'sleep 0.2', 'exit_codes': [0, 0, 0], 'max': 0.20192621200112626, 'mean': 0.2015410343349989, ...}, {'command': 'sleep 0.2', 'exit_codes': [0, 0, 0], 'max': 0.2021812440

### `missing_file` — 1 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_lifecycle.test_conclude_with_process_cleanup`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_conclude_with_process_cle2/conclude_marker.txt'

