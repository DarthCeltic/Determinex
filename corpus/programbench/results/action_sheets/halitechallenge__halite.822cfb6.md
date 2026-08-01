# Action Sheet — halitechallenge__halite.822cfb6

**Current:** 7.42%  (36/485)
**Pass / Fail / Skip:** 36 / 326 / 4
**Gap to 100%:** 92.58 percentage points (449 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest.test_starter_package_game`
  - reason: javac not available in environment
- `tests.test_harvest.test_java_starter_package_build`
  - reason: javac not available in environment
- `tests.test_harvest.test_rust_starter_package_build`
  - reason: Rust code has compatibility issues with newer Rust versions (thread_rng API changed)
- `eval.tests.test_externalized_environment.test_ext_timeout_evaluation_mixed_bots_seed_998`
  - reason: Original internal timeout test takes ~30s in this environment; cannot meet 5s per-test limit

## Failure clusters

326 failed tests grouped into 13 buckets (sorted by count).

### `other_assertion` — 159 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_halite.TestBasicInvocation.test_no_arguments_fails_with_message`
  > AssertionError: assert b'Please provide the launch command string for at least one bot' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable'], returncode=1, stdout=b'', stderr=b'usage: halite [--help] [--version] [--quiet] [--no-timeout] [--seed SEED] [--width WIDTH] [--height 
- `tests.test_halite.TestBasicInvocation.test_help_flag_displays_usage`
  > AssertionError: assert b'USAGE:' in b'halite 1.0.0\n\nUsage:\n  halite [options] -- <bot_command>...\n  halite [options] --bot <bot_command>...\n\nOptions:\n  --help, -h              Show this help me
  >  +  where b'halite 1.0.0\n\nUsage:\n  halite [options] -- <bot_command>...\n  halite [options] --bot <bot_command>...\n\nOptions:\n  --help, -h              Show this help message and exit\n  --versio
- `tests.test_halite.TestBasicInvocation.test_h_flag_displays_usage`
  > AssertionError: assert b'USAGE:' in b'halite 1.0.0\n\nUsage:\n  halite [options] -- <bot_command>...\n  halite [options] --bot <bot_command>...\n\nOptions:\n  --help, -h              Show this help me
  >  +  where b'halite 1.0.0\n\nUsage:\n  halite [options] -- <bot_command>...\n  halite [options] --bot <bot_command>...\n\nOptions:\n  --help, -h              Show this help message and exit\n  --versio
- *(... 156 more in this cluster)*

### `rc_mismatch_got0_want1` — 45 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_additional_coverage.test_replay_json_structure`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_additional_coverage.test_replay_contains_seed_info`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_map_config.test_nplayers_with_multiple_bots_fails`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-d', '20 20', '-s', '42', '-n', '3', 'python3 /tmp/tmpugdzignp/simplebot.py', 'python3 /tmp/tmpugdzignp/simplebot.py'], returncode=0, std
- *(... 42 more in this cluster)*

### `empty_list_or_string` — 37 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_bot_launch.test_quiet_mode_output_format`
  > IndexError: list index out of range
- `tests.test_map_config.test_default_dimensions_when_not_specified`
  > IndexError: list index out of range
- `tests.test_override_edge_cases.test_seed_zero`
  > IndexError: list index out of range
- *(... 34 more in this cluster)*

### `missing_file` — 27 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `eval.tests.test_args.test_no_args_requires_bot_command`
  > FileNotFoundError: [Errno 2] No such file or directory: 'executable'
- `eval.tests.test_args.test_unknown_flag_is_error[--nonexistent-flag]`
  > FileNotFoundError: [Errno 2] No such file or directory: 'executable'
- `eval.tests.test_args.test_unknown_flag_is_error[--nonexistent]`
  > FileNotFoundError: [Errno 2] No such file or directory: 'executable'
- *(... 24 more in this cluster)*

### `boolean_false` — 13 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_halite.TestMapConfiguration.test_custom_dimensions`
  > assert False
  >  +  where False = any(<generator object TestMapConfiguration.test_custom_dimensions.<locals>.<genexpr> at 0x7f14c731d540>)
- `tests.test_halite.TestMapConfiguration.test_single_player_mode_with_nplayers`
  > assert False
  >  +  where False = any(<generator object TestMapConfiguration.test_single_player_mode_with_nplayers.<locals>.<genexpr> at 0x7f14c731d000>)
- `tests.test_halite.TestGameModes.test_quiet_mode_output_format`
  > assert False
  >  +  where False = any(<generator object TestGameModes.test_quiet_mode_output_format.<locals>.<genexpr> at 0x7f14c733de70>)
- *(... 10 more in this cluster)*

### `rc_mismatch_got2_want0` — 13 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_map_config.test_dimensions_long_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--dimensions', '18 18', '-s', '42', '-q', 'python3 /tmp/tmpvgwgocnd/simplebot.py'], returncode=2, stdout=b'', stderr=b'halite: error: unr
- `tests.test_map_config.test_nplayers_long_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-d', '30 30', '-s', '42', '--nplayers', '3', '-q', 'python3 /tmp/tmpp1jlekcn/simplebot.py'], returncode=2, stdout=b'', stderr=b'halite: e
- `tests.test_override_edge_cases.test_override_mode_long_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-d', '10 10', '-s', '42', '--override', '-q', 'python3 /tmp/tmpepalumxu/simplebot.py', 'Name1', 'python3 /tmp/tmpepalumxu/simplebot.py', 
- *(... 10 more in this cluster)*

### `string_output_mismatch` — 12 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_quiet_smoke.test_quiet_mode_starts_and_prints_command_line_quickly`
  > AssertionError: assert '' == '/bin/true'
  >   
  >   - /bin/true
- `tests.test_init_config.test_version_flag`
  > AssertionError: assert 'halite 1.0.0' == './executable  version: 1.2'
  >   
  >   - ./executable  version: 1.2
  >   + halite 1.0.0
- `tests.test_init_config.test_no_bot_command_error`
  > AssertionError: assert '' == 'Please provi...sage details.'
  >   
  >   - Please provide the launch command string for at least one bot.
  >   - Use the --help flag for usage details.
- *(... 9 more in this cluster)*

### `uncategorized` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_help_usage.test_dash_h_matches_dash_dash_help_exactly`
  > OSError: [Errno 8] Exec format error: '/workspace/environment/executable.'
- `eval.tests.test_help_usage.test_help_precedence_with_other_flags`
  > OSError: [Errno 8] Exec format error: '/workspace/environment/executable.'
- `eval.tests.test_help_usage.test_help_after_double_dash_is_not_treated_as_help`
  > OSError: [Errno 8] Exec format error: '/workspace/environment/executable.'
- *(... 5 more in this cluster)*

### `rc_unexpected_zero` — 7 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_halite.TestMapConfiguration.test_invalid_player_count_fails`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-d', '10 10', '-n', '7', '-q', '-r', 'python3 /workspace/eval/tests/simple_bot.py'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_halite.TestMapConfiguration.test_conflicting_multiplayer_and_nplayers`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-d', '10 10', '-n', '3', '-q', '-r', 'python3 /workspace/eval/tests/simple_bot.py', 'python3 /workspace/eval/tests/simple_bot.py'], retur
- `tests.test_halite.TestErrorHandling.test_invalid_dimension_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-d', '10', '-q', '-r', 'python3 /workspace/eval/tests/simple_bot.py'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 4 more in this cluster)*

### `rc_mismatch_got1_want0` — 2 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_halite.TestReplayGeneration.test_disable_replay_with_r_flag`
  > AssertionError: assert 1 == 0
  >  +  where 1 = len([PosixPath('/tmp/tmp9zq65np1/replay-2120710262-40x40-1779057127.hlt')])
- `tests.test_halite.TestReplayGeneration.test_noreplay_flag`
  > AssertionError: assert 1 == 0
  >  +  where 1 = len([PosixPath('/tmp/tmpvyrx4b6r/replay-1336929510-40x40-1779057475.hlt')])

### `type_error` — 1 test(s)

**Quick patch ideas:**
- Specific TypeError; check arg types vs expected

**Sample failures:**

- `tests.test_init_config.test_noreplay_flag_prevents_file_creation`
  > TypeError: 'NoneType' object is not callable

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_init_config.test_random_dimensions_generation`
  > assert 0 == 3
  >  +  where 0 = len([])

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_executable_behavior.test_version_format_and_number`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f5c32cde680>('version: 1\\.2', 'halite 1.0.0\n')
  >  +    where <function search at 0x7f5c32cde680> = re.search
  >  +    and   'halite 1.0.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout='halite 1.0.0\n', stderr='').stdout

