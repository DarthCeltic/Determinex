# Action Sheet — ninja-build__ninja.cc60300

**Current:** 21.77%  (442/2030)
**Pass / Fail / Skip:** 442 / 973 / 1
**Gap to 100%:** 78.23 percentage points (1588 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_build_basic.test_second_run_no_work`
  - reason: test_second_run_no_work depends on test_build_default_creates_output

## Failure clusters

973 failed tests grouped into 16 buckets (sorted by count).

### `other_assertion` — 384 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_features.test_phony_target`
  > AssertionError: assert (b'real.txt' in b'' or b'[' in b'')
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'all'], returncode=0, stdout=b'', stderr=b'').stdout
  >  +  and   b'' = CompletedProcess(args=['/workspace/executable', 'all'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_advanced_features.test_targets_with_depth`
  > AssertionError: assert b':' in b'in1.txt\ngcc\nrule1\n'
  >  +  where b'in1.txt\ngcc\nrule1\n' = CompletedProcess(args=['/workspace/executable', '-t', 'targets', 'depth', '1'], returncode=0, stdout=b'in1.txt\ngcc\nrule1\n', stderr=b'').stdout
- `tests.test_advanced_features.test_tool_inputs_with_depth`
  > AssertionError: assert 'txt' in ''
- *(... 381 more in this cluster)*

### `rc_mismatch_got7_want0` — 175 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_features.test_default_target`
  > AssertionError: assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['/workspace/executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').re
- `tests.test_advanced_features.test_variables_in_build_file`
  > AssertionError: assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['/workspace/executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').re
- `tests.test_advanced_features.test_implicit_dependencies`
  > AssertionError: assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['/workspace/executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').re
- *(... 172 more in this cluster)*

### `boolean_false` — 156 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_advanced_features.test_pool_usage`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = (PosixPath('/tmp/tmp9godalh3') / 'output1.o').exists
  >  +      where PosixPath('/tmp/tmp9godalh3') = Path('/tmp/tmp9godalh3')
  >  +        where '/tmp/tmp9godalh3' = <conftest.TempFiles object at 0x7fba20bae350>.path
- `tests.test_advanced_features.test_build_with_dependencies`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = (PosixPath('/tmp/tmp81yjn_pe') / 'a.txt').exists
  >  +      where PosixPath('/tmp/tmp81yjn_pe') = Path('/tmp/tmp81yjn_pe')
  >  +        where '/tmp/tmp81yjn_pe' = <conftest.TempFiles object at 0x7fba20bd9e10>.path
- `tests.test_advanced_features.test_clean_with_rule_flag`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = (PosixPath('/tmp/tmpypbl4gsu') / 't1.txt').exists
  >  +      where PosixPath('/tmp/tmpypbl4gsu') = Path('/tmp/tmpypbl4gsu')
  >  +        where '/tmp/tmpypbl4gsu' = <conftest.TempFiles object at 0x7fba20c29c30>.path
- *(... 153 more in this cluster)*

### `string_output_mismatch` — 71 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_one_more_push.test_compdb_with_no_commands`
  > AssertionError: assert ('digraph\noutput.txt\n->\n' == ''
  >   
  >   + digraph
  >   + output.txt
  >   + -> or 'digraph\noutput.txt\n->\n' == '[]'
  >   
  >   - []
  >   + digraph
- `tests.test_cli_basic.test_no_work_quiet`
  > AssertionError: assert 'TOUCH\ncusto...\ntarget1.txt' == ''
  >   
  >   + TOUCH
  >   + custom_output.txt
  >   + Entering directory
  >   + target1.txt
- `tests.test_argparse_validation.test_quiet_suppresses_status_output`
  > AssertionError: assert 'error: unexp... information.' == ''
  >   
  >   + error: unexpected argument '-C' found
  >   + Error: unexpected argument '-C' found
  >   + unknown flag: unexpected argument '-C' found
  >   + Unknown flag: unexpected argument '-C' found
  >   + Usage: ninja [OPTIONS] [ARGS]...
  >   + USAGE: ninja [OPTIONS] [ARGS]......
- *(... 68 more in this cluster)*

### `rc_unexpected_zero` — 61 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_handling.test_invalid_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-flag-that-does-not-exist'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_handling.test_nonexistent_directory_change`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-C', '/nonexistent/directory/path'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_more_subtools.test_warning_phonycycle_err`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-w', 'phonycycle=err'], returncode=0, stdout=b'output.txt\ntxt\ntouch output.txt\n', stderr=b'').returncode
- *(... 58 more in this cluster)*

### `missing_file` — 40 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_absolute_final.test_in_variable`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpe1uwr64d/output.txt'
- `tests.test_absolute_final.test_out_variable`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpjt3dqsdk/result.txt'
- `tests.test_absolute_final.test_rule_variable_override`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp_51amad9/out1.txt'
- *(... 37 more in this cluster)*

### `subprocess_failed` — 20 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_build_execution.test_build_already_up_to_date`
  > subprocess.CalledProcessError: Command '['/workspace/executable']' returned non-zero exit status 7.
- `tests.test_build_execution.test_modified_input_triggers_rebuild`
  > subprocess.CalledProcessError: Command '['/workspace/executable']' returned non-zero exit status 7.
- `tests.test_clean.test_clean_verbose_mode_with_depfiles`
  > subprocess.CalledProcessError: Command '['/workspace/executable']' returned non-zero exit status 7.
- *(... 17 more in this cluster)*

### `rc_mismatch_got0_want1` — 17 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_argparse_validation.test_option_requires_argument_messages[-f]`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-f'], returncode=0, stdout='', stderr='').returncode
- `tests.test_argparse_validation.test_option_requires_argument_messages[-C]`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-C'], returncode=0, stdout='digraph\na.txt\n', stderr='').returncode
- `tests.test_argparse_validation.test_option_requires_argument_messages[-t]`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-t'], returncode=0, stdout='', stderr='').returncode
- *(... 14 more in this cluster)*

### `uncategorized` — 16 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_browse.test_browse_server_starts_and_responds`
  > requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=9001): Max retries exceeded with url: /?all (Caused by NewConnectionError("HTTPConnection(host='localhost', port=9001): F
- `tests.test_browse.test_browse_root_redirects_to_default_target`
  > requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=9002): Max retries exceeded with url: / (Caused by NewConnectionError("HTTPConnection(host='localhost', port=9002): Faile
- `tests.test_browse.test_browse_target_with_dependencies`
  > requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=9003): Max retries exceeded with url: /?intermediate.txt (Caused by NewConnectionError("HTTPConnection(host='localhost', 
- *(... 13 more in this cluster)*

### `json_output_missing_or_bad` — 14 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_advanced_features.test_compdb_with_rule`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_absolute_final_70.test_compdb_with_complex_commands`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_comprehensive_quality.test_compdb_tool_outputs_json`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 11 more in this cluster)*

### `rc_mismatch_got7_want1` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_no_build_file_error`
  > AssertionError: assert 7 == 1
  >  +  where 7 = CompletedProcess(args=['/workspace/executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').re
- `tests.test_basic_invocation.test_no_build_file_error`
  > AssertionError: assert 7 == 1
  >  +  where 7 = CompletedProcess(args=['/workspace/executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').re
- `tests.test_edge_cases.test_invalid_build_file_syntax`
  > AssertionError: assert 7 == 1
  >  +  where 7 = CompletedProcess(args=['/workspace/executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').re
- *(... 3 more in this cluster)*

### `returned_none` — 4 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic.test_version`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7fba2189e170>(b'\\d+\\.\\d+\\.\\d+', b'.git\n')
  >  +    where <function match at 0x7fba2189e170> = re.match
  >  +    and   b'.git\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'.git\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f6d352e6170>(b'\\d+\\.\\d+\\.\\d+', b'.git\n')
  >  +    where <function match at 0x7f6d352e6170> = re.match
  >  +    and   b'.git\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'.git\n', stderr=b'').stdout
- `tests.test_argparse_validation.test_unknown_short_flag_is_error_and_mentions_flag`
  > assert None
  >  +  where None = <function search at 0x7f26e1c4a680>("invalid option -- 'o'", '')
  >  +    where <function search at 0x7f26e1c4a680> = re.search
  >  +    and   '' = CompletedProcess(args=['/workspace/executable', '-o'], returncode=1, stdout='', stderr='').stderr
- *(... 1 more in this cluster)*

### `rc_mismatch_got1_want0` — 4 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_final_coverage_push.test_stats_mode_detailed`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-d', 'stats', 'target0', 'target1', 'target2', 'target3', 'target4', 'target5', 'target6', 'target7', 'target8', 'target9'], returncode=1
- `tests.test_debug_modes.test_keeprsp_preserves_response_file`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-d', 'keeprsp'], returncode=1, stdout='ninja subtools:\nbrowse\nclean\ncommands\ninputs\ndeps\ngraph\nquery\ntargets\ncompdb\n', stderr='
- `tests.test_debug_modes.test_keeprsp_with_minimal_rspfile_content`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-d', 'keeprsp'], returncode=1, stdout='ninja subtools:\nbrowse\nclean\ncommands\ninputs\ndeps\ngraph\nquery\ntargets\ncompdb\n', stderr='
- *(... 1 more in this cluster)*

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_comprehensive_quality.test_quiet_mode_suppresses_progress`
  > AssertionError: assert (85 < 20 or b'browse\ncle...target2.txt\n' == b''
  >  +  where 85 = len(b'browse\nclean\ngraph\nquery\ntargets\ncompdb\noutput.txt\ninput.txt\ntarget1.txt\ntarget2.txt\n')
  >  +    where b'browse\nclean\ngraph\nquery\ntargets\ncompdb\noutput.txt\ninput.txt\ntarget1.txt\ntarget2.txt\n' = CompletedProcess(args=['/workspace/executable', '--quiet', '-f', 'build.ninja'], return
  >   
  >   Full diff:
  >   - b''
  >   + (b'browse\nclean\ngraph\nquery\ntargets\ncompdb\noutput.txt\ninput.txt\ntarget1'
  >   +  b'.txt\ntarget2.txt\n'))
- `tests.test_tool_comprehensive.test_compdb_with_empty_database`
  > AssertionError: assert (b'digraph\noutput.txt\n->\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'digraph\noutput.txt\n->\n') or b'digraph\noutput.txt\n->\n' == b'[]\n'
  >   
  >   At index 0 diff: b'd' != b'['
  >   

### `empty_list_or_string` — 2 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_help_main.test_help_starts_with_usage_line`
  > IndexError: list index out of range
- `tests.test_help_subtool_clean.test_clean_help_usage_line`
  > IndexError: list index out of range

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_build_execution.test_phony_target_builds_dependencies`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])

