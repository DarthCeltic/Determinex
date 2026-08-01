# Action Sheet — gabotechs__dep-tree.60a95a2

**Current:** 28.58%  (419/1466)
**Pass / Fail / Skip:** 419 / 720 / 2
**Gap to 100%:** 71.42 percentage points (1047 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_subcommand_dispatch.TestSubcommandHelp.test_help_command_for_subcommand[help]`
  - reason: 'help help' is redundant
- `tests.test_harvest.test_root_integration[tree .root_test/main.py --json --exclude .root_test/*.py]`
  - reason: Known failure in original test - error message too short

## Failure clusters

720 failed tests grouped into 11 buckets (sorted by count).

### `other_assertion` — 362 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'dep-tree [command]' in b'dep-tree\nUsage:\nentropy\ntree\ncheck\nexplain\nconfig\ndep-tree\nUsage:\nFlags:\n'
  >  +  where b'dep-tree\nUsage:\nentropy\ntree\ncheck\nexplain\nconfig\ndep-tree\nUsage:\nFlags:\n' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'dep-tree\nUsage:\ne
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'dep-tree [command]' in b'dep-tree\nUsage:\nFlags:\ndep-tree version\ndep-tree version\ndep-tree\nUsage:\nentropy\nentropy\n--no-browser-open\n'
  >  +  where b'dep-tree\nUsage:\nFlags:\ndep-tree version\ndep-tree version\ndep-tree\nUsage:\nentropy\nentropy\n--no-browser-open\n' = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0
- `tests.test_basic_invocation.test_help_command`
  > AssertionError: assert b'dep-tree [command]' in b'dep-tree\nUsage:\nentropy\ntree\ncheck\nexplain\nconfig\nFlags:\n'
  >  +  where b'dep-tree\nUsage:\nentropy\ntree\ncheck\nexplain\nconfig\nFlags:\n' = CompletedProcess(args=['/workspace/executable', 'help'], returncode=0, stdout=b'dep-tree\nUsage:\nentropy\ntree\ncheck\
- *(... 359 more in this cluster)*

### `rc_unexpected_zero` — 93 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_check_command.test_check_without_config`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_check_command.test_check_with_deny_rule_violation`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_check_command.test_check_with_allow_rule_violation`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 90 more in this cluster)*

### `string_output_mismatch` — 73 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_main.test_h_equals_help_exact`
  > AssertionError: assert 'dep-tree\nUs...ge:\nFlags:\n' == 'dep-tree\nUs...rowser-open\n'
  >   
  >   + dep-tree
  >   + Usage:
  >   + entropy
  >   + tree
  >   + check
  >   + explain...
- `eval.tests.test_help_main.test_help_main_baseline_exact_match`
  > AssertionError: assert 'dep-tree\nUs...ge:\nFlags:\n' == '\n      ____... a command.\n'
  >   
  >   + dep-tree
  >   - 
  >   -       ____         _ __       _
  >   -      |  _ \   ___ |  _ \    _| |_  _ __  ___   ___
  >   -      | | | | / _ \| |_) |  |_   _||  __|/ _ \ / _ \
  >   -      | |_| ||  __/| .__/     | |  | |  |  __/|  __/...
- `eval.tests.test_help_subcommands.test_subcommand_help_exit_code_zero_and_stdout[entropy-help_entropy.txt]`
  > AssertionError: assert 'Entropy: 0.00\n' == '(default) Re...ault false)\n'
  >   
  >   + Entropy: 0.00
  >   - (default) Renders a 3d force-directed graph in the browser
  >   - 
  >   - Usage:
  >   -   dep-tree entropy [flags]
  >   - ...
- *(... 70 more in this cluster)*

### `missing_file` — 60 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_additional_features.TestMultipleEntrypoints.test_entropy_multiple_entrypoints`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp9gd31fay/out.html'
- `tests.test_coverage_boost.TestEntropyVariants.test_entropy_with_enable_gui`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpwvbh8sbn/out.html'
- `tests.test_coverage_boost.TestEntropyVariants.test_entropy_python_project`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp9t6qbl55/out.html'
- *(... 57 more in this cluster)*

### `boolean_false` — 37 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_config_command.test_config_generates_sample`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/workspace/test_deptree_0mxjx9q6/.dep-tree.yml').exists
- `tests.test_config_command.test_config_with_custom_path`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/workspace/test_deptree_m2prxqg8/.dep-tree.yml').exists
- `tests.test_edge_cases.test_entropy_enable_gui_flag`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/workspace/test_deptree_1kda29o9/output.html').exists
- *(... 34 more in this cluster)*

### `rc_mismatch_got2_want0` — 33 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_no_args_shows_help`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'Usage: dep-tree [command] [options]\n\nCommands:\n  tree      Display dependency tree\n  entropy   Cal
- `tests.test_config_command.test_config_init_alias`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'init'], returncode=2, stdout=b'', stderr=b'unknown command: init\n').returncode
- `tests.test_entropy_command.test_entropy_as_default_command`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'main.py', '--no-browser-open'], returncode=2, stdout=b'', stderr=b'unknown command: main.py\n').returncode
- *(... 30 more in this cluster)*

### `missing_dict_key` — 25 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_tree_command.TestTreeGlobalFlags.test_tree_with_exclude_pattern`
  > KeyError: 'tree'
- `tests.test_language_features.test_tsconfig_paths_resolution_with_flag_enabled`
  > KeyError: 'tree'
- `tests.test_language_features.test_es_module_reexport_star`
  > KeyError: 'tree'
- *(... 22 more in this cluster)*

### `rc_mismatch_got0_want1` — 19 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_argparse_validation.test_unknown_flag_errors[args1-unknown flag: --bad]`
  > AssertionError: assert 0 == 1
  >  +  where 0 = RunResult(returncode=0, stdout='No entrypoints specified\n', stderr='').returncode
- `eval.tests.test_argparse_validation.test_unknown_flag_errors[args2-unknown flag: --bad]`
  > AssertionError: assert 0 == 1
  >  +  where 0 = RunResult(returncode=0, stdout='Entropy: 0.00\n', stderr='').returncode
- `eval.tests.test_argparse_validation.test_unknown_flag_errors[args3-unknown flag: --bad]`
  > AssertionError: assert 0 == 1
  >  +  where 0 = RunResult(returncode=0, stdout='Configuration file not found\n', stderr='').returncode
- *(... 16 more in this cluster)*

### `returned_none` — 6 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f10f1d66680>(b'v\\d+\\.\\d+\\.\\d+', b'dep-tree version\ndep-tree version\ndep-tree\nUsage:\nentropy\nentropy\n--no-browser-open\n--render-path\n--enable-gui\nt
  >  +    where <function search at 0x7f10f1d66680> = re.search
  >  +    and   b'dep-tree version\ndep-tree version\ndep-tree\nUsage:\nentropy\nentropy\n--no-browser-open\n--render-path\n--enable-gui\ntree\n' = CompletedProcess(args=['/workspace/executable', '--versi
- `tests.test_basic.TestHelpAndVersion.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fb5e3577760>(b'v\\d+\\.\\d+\\.\\d+', b'dep-tree version\ndep-tree version\ndep-tree\nUsage:\nentropy\nentropy\n--no-browser-open\n--render-path\n--enable-gui\nt
  >  +    where <function search at 0x7fb5e3577760> = re.search
  >  +    and   b'dep-tree version\ndep-tree version\ndep-tree\nUsage:\nentropy\nentropy\n--no-browser-open\n--render-path\n--enable-gui\ntree\n' = CompletedProcess(args=['/workspace/executable', '--versi
- `tests.test_basic.TestHelpAndVersion.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fb5e3577760>(b'v\\d+\\.\\d+\\.\\d+', b'dep-tree version\ndep-tree\nUsage:\nentropy\nentropy\n--no-browser-open\n--render-path\n--enable-gui\ntree\n--json\n')
  >  +    where <function search at 0x7fb5e3577760> = re.search
  >  +    and   b'dep-tree version\ndep-tree\nUsage:\nentropy\nentropy\n--no-browser-open\n--render-path\n--enable-gui\ntree\n--json\n' = CompletedProcess(args=['/workspace/executable', '-v'], returncode=
- *(... 3 more in this cluster)*

### `bytes_output_mismatch` — 6 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_final_coverage_boost.TestDiverseScenarios.test_tree_with_multiple_entrypoints_fails_correctly`
  > assert (0 == 1 or b'1 entrypoint' in b'')
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'tree', 'a.py', 'b.py', 'c.py', '--json'], returncode=0, stdout=b'{\n  "nodes": [],\n  "links": [],\n  "entrypoints": [\n    "a.py",\n    
  >  +  and   b'' = CompletedProcess(args=['/workspace/executable', 'tree', 'a.py', 'b.py', 'c.py', '--json'], returncode=0, stdout=b'{\n  "nodes": [],\n  "links": [],\n  "entrypoints": [\n    "a.py",\n  
- `tests.test_subcommand_dispatch.TestSubcommandHelp.test_help_command_for_subcommand[entropy]`
  > AssertionError: assert b'' == b'Entropy: 0.00\n'
  >   
  >   Full diff:
  >   - (b'Entropy: 0.00\n')
  >   + b''
- `tests.test_subcommand_dispatch.TestSubcommandHelp.test_help_command_for_subcommand[tree]`
  > AssertionError: assert b'' == b'No entrypoints specified\n'
  >   
  >   Full diff:
  >   - (b'No entrypoints specified\n')
  >   + b''
- *(... 3 more in this cluster)*

### `rc_mismatch_got2_want1` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_unknown_flag_errors[args0-unknown flag: --nonexistent-flag]`
  > AssertionError: assert 2 == 1
  >  +  where 2 = RunResult(returncode=2, stdout='', stderr='unknown command: --nonexistent-flag\n').returncode
- `eval.tests.test_argparse_validation.test_missing_value_for_string_flag[args0-flag needs an argument: --config]`
  > AssertionError: assert 2 == 1
  >  +  where 2 = RunResult(returncode=2, stdout='', stderr='unknown command: --config\n').returncode
- `eval.tests.test_argparse_validation.test_mutually_exclusive_overlap_flags_combined_short`
  > AssertionError: assert 2 == 1
  >  +  where 2 = RunResult(returncode=2, stdout='', stderr='unknown flag: -lr\n').returncode
- *(... 3 more in this cluster)*

