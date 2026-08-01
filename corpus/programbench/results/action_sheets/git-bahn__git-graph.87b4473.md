# Action Sheet — git-bahn__git-graph.87b4473

**Current:** 20.92%  (178/851)
**Pass / Fail / Skip:** 178 / 552 / 2
**Gap to 100%:** 79.08 percentage points (673 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_formatting.test_custom_format_refs_decoration`
  - reason: Binary bug: %d placeholder causes panic at src/print/unicode.rs:952
- `tests.test_formatting.test_wrap_very_large_width`
  - reason: Binary bug: wrap width 1000 causes panic at src/print/unicode.rs:952

## Failure clusters

552 failed tests grouped into 18 buckets (sorted by count).

### `other_assertion` — 347 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_version_output`
  > AssertionError: assert b'git-graph' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic.test_version_short_flag`
  > AssertionError: assert b'git-graph' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-V'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic.test_help_short`
  > AssertionError: assert b'Usage:' in b'Structured Git graphs for your branching model\nhttps://github.com/mlange-42/git-graph\n'
  >  +  where b'Structured Git graphs for your branching model\nhttps://github.com/mlange-42/git-graph\n' = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0, stdout=b'Structured Git gra
- *(... 344 more in this cluster)*

### `string_output_mismatch` — 98 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_model_subcommand_list_ignores_extra_positional_and_succeeds`
  > AssertionError: assert [] == ['simple', 'none', 'git-flow']
  >   
  >   Right contains 3 more items, first extra item: 'simple'
  >   
  >   Full diff:
  >   + []
  >   - [
  >   -     'simple',...
- `eval.tests.test_subcommand_dispatch.test_subcommand_routing_model_list_does_not_print_graph`
  > AssertionError: assert ['simple'] == ['simple', 'none', 'git-flow']
  >   
  >   Right contains 2 more items, first extra item: 'none'
  >   
  >   Full diff:
  >     [
  >         'simple',
  >   -     'none',
- `eval.tests.test_git_graph.test_version_exact`
  > AssertionError: assert '' == 'git-graph 0.7.0\n'
  >   
  >   - git-graph 0.7.0
- *(... 95 more in this cluster)*

### `rc_unexpected_zero` — 26 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic.test_no_args_outside_git_repo`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'(\n(col\n*\n<\n<-\n</svg>\n<circle\n<svg\n>\n@\nAlice Author <alice@example.com>\nAnother paragraph in the body\nA
- `tests.test_basic.test_invalid_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-flag-xyz'], returncode=0, stdout=b'Test commit message\nFirst commit\nSecond commit\nThird commit\nUsage:\nCommands:\nUsage:\nm
- `tests.test_error_handling.test_max_count_invalid`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--max-count', 'invalid'], returncode=0, stdout=b'<svg\nFirst commit\nThird commit\n', stderr=b'').returncode
- *(... 23 more in this cluster)*

### `uncategorized` — 20 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_git_graph.test_format_oneline_structure`
  > StopIteration
- `tests.test_svg.test_single_commit_svg_structure`
  > xml.etree.ElementTree.ParseError: no element found: line 1, column 0
- `tests.test_svg.test_linear_history_svg_contains_lines`
  > xml.etree.ElementTree.ParseError: no element found: line 1, column 0
- *(... 17 more in this cluster)*

### `rc_mismatch_got0_want1` — 12 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_output_validation.test_svg_output_structure`
  > AssertionError: assert 0 == 1
  >  +  where 0 = <built-in method count of str object at 0x7f632b1ec030>('<svg')
  >  +    where <built-in method count of str object at 0x7f632b1ec030> = ''.count
- `eval.tests.test_argparse_validation.test_invalid_value_validation_messages[args1-1-ERROR: No branching model named 'notamodel' found]`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-m', 'notamodel'], returncode=0, stdout='', stderr='').returncode
- `eval.tests.test_argparse_validation.test_invalid_value_validation_messages[args2-1-Option max-count must be a positive number, but got 'abc']`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-n', 'abc'], returncode=0, stdout='', stderr='').returncode
- *(... 9 more in this cluster)*

### `subprocess_failed` — 10 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_repository.test_path_option_absolute_path`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--path', '/tmp/pytest-of-root/pytest-0/test_path_option_absolute_path2/test_repo']' returned non-zero exit status 1.
- `tests.test_repository.test_path_option_subdirectory_within_repo`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--path', '/tmp/pytest-of-root/pytest-0/test_path_option_subdirectory_2/test_repo/nested/deep']' returned non-zero exit status 1.
- `tests.test_repository.test_path_option_dotgit_directory_directly`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--path', '/tmp/pytest-of-root/pytest-0/test_path_option_dotgit_direct2/test_repo/.git']' returned non-zero exit status 1.
- *(... 7 more in this cluster)*

### `boolean_false` — 8 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_config_handling.test_models_created_under_home_and_xdg_config_home`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = (PosixPath('/tmp/pytest-of-root/pytest-0/test_models_created_under_home2/xdg/git-graph/models') / 'git-flow.toml').exists
- `eval.tests.test_color_and_svg.test_svg_flag_outputs_svg`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f969f248030>('<svg')
  >  +    where <built-in method startswith of str object at 0x7f969f248030> = ''.startswith
  >  +      where '' = <built-in method lstrip of str object at 0x7f969f248030>()
  >  +        where <built-in method lstrip of str object at 0x7f969f248030> = ''.lstrip
- `eval.tests.test_subcommand_dispatch.test_global_flag_before_subcommand_is_accepted_for_model`
  > AssertionError: assert False
  >  +  where False = <built-in method issubset of set object at 0x7f38dc37c900>(set())
  >  +    where <built-in method issubset of set object at 0x7f38dc37c900> = {'git-flow', 'none', 'simple'}.issubset
  >  +      where {'git-flow', 'none', 'simple'} = set(['simple', 'none', 'git-flow'])
  >  +    and   set() = set([])
- *(... 5 more in this cluster)*

### `returned_none` — 7 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_help_lists_commands_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f3993dde680>('^Commands:\\s*$', 'git-graph\nbranching model\ngit-graph\ngit-flow\nsimple\nnone\nInitial commit\nâ\x97\x8f\n', flags=re.MULTILINE)
  >  +    where <function search at 0x7f3993dde680> = re.search
  >  +    and   'git-graph\nbranching model\ngit-graph\ngit-flow\nsimple\nnone\nInitial commit\nâ\x97\x8f\n' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='git-graph\nb
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_usage.test_help_lists_options_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f3993dde680>('^Options:\\s*$', 'git-graph\nbranching model\ngit-graph\ngit-flow\nsimple\nnone\nInitial commit\nâ\x97\x8f\n', flags=re.MULTILINE)
  >  +    where <function search at 0x7f3993dde680> = re.search
  >  +    and   'git-graph\nbranching model\ngit-graph\ngit-flow\nsimple\nnone\nInitial commit\nâ\x97\x8f\n' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='git-graph\nb
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_usage.test_help_mentions_subcommand_model`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f3993dde680>('^\\s*model\\b', 'git-graph\nbranching model\ngit-graph\ngit-flow\nsimple\nnone\nInitial commit\nâ\x97\x8f\n', flags=re.MULTILINE)
  >  +    where <function search at 0x7f3993dde680> = re.search
  >  +    and   'git-graph\nbranching model\ngit-graph\ngit-flow\nsimple\nnone\nInitial commit\nâ\x97\x8f\n' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='git-graph\nb
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 4 more in this cluster)*

### `rc_mismatch_got1_want0` — 5 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_path_handling.test_explicit_path`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--path', '/tmp/tmpdg8xohj9'], returncode=1, stdout=b'Structured Git graphs for your branching model\nhttps://github.com/mlange-42/git-gra
- `tests.test_path_handling.test_path_to_parent_directory`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--path', '/tmp/tmpiowhtcsr/subdir'], returncode=1, stdout=b'Structured Git graphs for your branching model\nhttps://github.com/mlange-42/
- `tests.test_path_handling.test_path_relative`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--path', '../../tmp/tmpy407_t64'], returncode=1, stdout=b'Structured Git graphs for your branching model\nhttps://github.com/mlange-42/gi
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want2` — 4 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse_validation.test_repeat_disallowed_option_color_is_exit_2`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--color', 'never', '--color', 'always'], returncode=0, stdout='', stderr='').returncode
- `eval.tests.test_help_usage.test_invalid_subcommand_has_error_and_usage_on_stderr_or_stdout`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'notasubcmd'], returncode=0, stdout='(\n(col\n*\n<\n<-\n</svg>\n<circle\n<svg\n>\n@\nAlice Author <alice@example.com>\nAnother paragraph i
- `eval.tests.test_help_usage.test_invalid_subcommand_help_shows_error_and_usage`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'notasubcmd', '--help'], returncode=0, stdout='', stderr='').returncode
- *(... 1 more in this cluster)*

### `rc_mismatch_got1_want2` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_models.test_model_invalid_name`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- `tests.test_models.test_model_flag_with_invalid_model`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- `tests.test_models.test_model_case_sensitivity`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- *(... 1 more in this cluster)*

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_subcommands.TestSubcommandHelp.test_help_subcommand_output`
  > AssertionError: assert b'Usage:\nCommands:\nmodel\n' == b'git-graph\n...x97\xc2\x8f\n'
  >   
  >   At index 0 diff: b'U' != b'g'
  >   
  >   Full diff:
  >   + (b'Usage:\nCommands:\nmodel\n')
  >   - (b'git-graph\nbranching model\ngit-graph\ngit-flow\nsimple\nnone\nInitial com'
  >   -  b'mit\n\xc3\xa2\xc2\x97\xc2\x8f\n')
- `tests.test_subcommands.TestSubcommandArguments.test_model_list_short_flag`
  > AssertionError: assert b'' == b'simple\n'
  >   
  >   Full diff:
  >   - (b'simple\n')
  >   + b''
- `tests.test_subcommands.TestSubcommandOrdering.test_help_with_subcommand_name`
  > AssertionError: assert b'Prints or p...ets\nUsage:\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'Prints or permanently sets\nUsage:\n')

### `missing_file` — 2 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_models.test_model_config_file_format`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_model_config_file_format2/test_repo/.git/git-graph.toml'
- `tests.test_models.test_model_config_file_not_world_writable`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_model_config_file_not_wor2/test_repo/.git/git-graph.toml'

### `rc_mismatch_got50_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_repository.test_default_behavior_current_directory_is_repo`
  > AssertionError: assert 50 == 1
  >  +  where 50 = len(['(', '(col', '*', '<', '<-', '</svg>', ...])
- `tests.test_repository.test_default_behavior_current_directory_is_subdirectory`
  > AssertionError: assert 50 == 1
  >  +  where 50 = len(['(', '(col', '*', '<', '<-', '</svg>', ...])

### `rc_mismatch_got0_want101` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_handling.test_empty_format_string`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--format', '', '--max-count', '1'], returncode=0, stdout=b'', stderr=b'').returncode

### `rc_mismatch_got2_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_custom_format_string_with_newlines`
  > AssertionError: assert 2 == 3
  >  +  where 2 = len(['Unicode: æ\x97¥æ\x9c¬èª\x9e ä¸\xadæ\x96\x87 ð\x9f\x8e\x89', 'Author: æµ\x8bè¯\x95ç\x94¨æ\x88· ð\x9f\x9a\x80'])

### `rc_mismatch_got1_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_large_repository_many_commits`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len(['*'])

### `rc_mismatch_got6_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_gaps.test_reverse_commit_order`
  > AssertionError: assert 6 == 3
  >  +  where 6 = len(['Author: Bob Committer <bob@example.com>', 'Bob Committer <bob@example.com>', 'Commit', 'Commit with', 'Commit:', 'Commit: Bob Committer <bob@example.com>'])

