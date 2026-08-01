# Action Sheet — eudoxia0__hashcards.48aa136

**Current:** 14.97%  (239/1596)
**Pass / Fail / Skip:** 239 / 833 / 4
**Gap to 100%:** 85.03 percentage points (1357 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_stats_export_check.test_export_output_file_matches_stdout`
  - reason: test_export_output_file_matches_stdout depends on test_export_json_and_count_matches_stats
- `tests.test_harvest.test_drill_cache_basic_functionality`
  - reason: Drill cache tests require web server interaction - not easily testable via CLI
- `tests.test_harvest.test_drill_action_grade`
  - reason: Internal grade mapping not observable via CLI
- `tests.test_harvest.test_performance_update`
  - reason: Performance update testing requires drill interaction

## Failure clusters

833 failed tests grouped into 16 buckets (sorted by count).

### `missing_dict_key` — 380 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_parsing.test_code_blocks_in_cards`
  > KeyError: 'cards'
- `tests.test_advanced_parsing.test_inline_code_in_cards`
  > KeyError: 'cards'
- `tests.test_advanced_parsing.test_bold_text_in_cards`
  > KeyError: 'cards'
- *(... 377 more in this cluster)*

### `other_assertion` — 157 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_args_shows_help`
  > AssertionError: assert b'A plain text-based spaced repetition system' in b'Usage: hashcards <COMMAND> [OPTIONS]\n       hashcards --help\n       hashcards --version\n\nCommands:\n  drill    Practice c
- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'A plain text-based spaced repetition system' in b'hashcards 0.1.0\nTool that emits structured JSON on stdout (tests json.loads it)\n\nUsage:\n  hashcards <COMMAND> [OPTIONS]\n
  >  +  where b'hashcards 0.1.0\nTool that emits structured JSON on stdout (tests json.loads it)\n\nUsage:\n  hashcards <COMMAND> [OPTIONS]\n\nCommands:\n  drill    Practice cards\n  check    Check cards\
- `tests.test_basic_invocation.test_help_flag_short`
  > AssertionError: assert b'A plain text-based spaced repetition system' in b'hashcards 0.1.0\nTool that emits structured JSON on stdout (tests json.loads it)\n\nUsage:\n  hashcards <COMMAND> [OPTIONS]\n
  >  +  where b'hashcards 0.1.0\nTool that emits structured JSON on stdout (tests json.loads it)\n\nUsage:\n  hashcards <COMMAND> [OPTIONS]\n\nCommands:\n  drill    Practice cards\n  check    Check cards\
- *(... 154 more in this cluster)*

### `boolean_false` — 85 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_collection_operations.test_collection_initialization`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp0sk0yix5/hashcards.db').exists
- `tests.test_database_coverage.test_database_schema_initialization`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpe__dt86c/hashcards.db').exists
  >  +      where PosixPath('/tmp/tmpe__dt86c/hashcards.db') = <test_database_coverage.TempCollection object at 0x7fb70e289360>.db_path
- `tests.test_database_coverage.test_check_creates_database_if_missing`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp3qwrw6hs/hashcards.db').exists
  >  +      where PosixPath('/tmp/tmp3qwrw6hs/hashcards.db') = <test_database_coverage.TempCollection object at 0x7fb70cb7a170>.db_path
- *(... 82 more in this cluster)*

### `rc_unexpected_zero` — 66 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_drill_command.test_drill_nonexistent_directory`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'drill', '/nonexistent/path'], returncode=0, stdout=b'{"drill": []}\n', stderr=b'').returncode
- `tests.test_error_handling.test_malformed_frontmatter`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '/tmp/tmp87w9jo3h'], returncode=0, stdout=b'{"check": "ok"}\n', stderr=b'').returncode
- `tests.test_error_handling.test_unclosed_frontmatter`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '/tmp/tmpx6dcjsk3'], returncode=0, stdout=b'{"check": "ok"}\n', stderr=b'').returncode
- *(... 63 more in this cluster)*

### `string_output_mismatch` — 42 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_check.test_check_example_prints_ok_newline_to_stdout`
  > assert '{"check": "ok"}\n' == 'ok\n'
  >   
  >   - ok
  >   + {"check": "ok"}
- `eval.tests.test_stats.test_stats_json_example_dir_exact_output`
  > assert '{"cardsInDbC...yCount": 0}\n' == '{\n  "cardsI...ount": 0\n}\n'
  >   
  >   + {"cardsInDbCount": 0, "cardsInDeckCount": 0, "cardsReviewedTodayCount": 0}
  >   - {
  >   -   "cardsInDeckCount": 16,
  >   -   "cardsInDbCount": 0,
  >   -   "texMacroCount": 1,
  >   -   "cardsReviewedTodayCount": 0
- `eval.tests.test_orphans.test_orphans_list_empty_when_no_db`
  > assert '{"orphans": []}' == ''
  >   
  >   + {"orphans": []}
- *(... 39 more in this cluster)*

### `bytes_output_mismatch` — 37 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_comprehensive_coverage.test_orphans_list_empty_for_new_collection`
  > assert (16 == 0 or b'{"orphans": []}\n' == b'\n'
  >  +  where 16 = len(b'{"orphans": []}\n')
  >  +    where b'{"orphans": []}\n' = CompletedProcess(args=['/workspace/executable', 'orphans', 'list', '/tmp/tmpvj1phr9h'], returncode=0, stdout=b'{"orphans": []}\n', stderr=b'').stdout
  >   
  >   At index 0 diff: b'{' != b'\n'
  >   
  >   Full diff:
  >   - b'\n'
- `tests.test_export_command.test_export_to_file`
  > AssertionError: assert (3 == 0 or b'ok\n' == b''
  >  +  where 3 = len(b'ok\n')
  >  +    where b'ok\n' = CompletedProcess(args=['/workspace/executable', 'export', '--output', '/tmp/tmpw5ys22e4/export.json', '/tmp/tmpw5ys22e4'], returncode=0, stdout=b'ok\n', stderr=b'').stdout
  >   
  >   Full diff:
  >   - b''
  >   + b'ok\n')
- `tests.test_stats_command.test_stats_default_format_not_implemented`
  > assert (b'not implemented' in b'{"cardsindbcount": 0, "cardsindeckcount": 0, "cardsreviewedtodaycount": 0}\n' or 75 == 0 or b'<' in b'{"cardsInDbCount": 0, "cardsInDeckCount": 0, "cardsReviewedTodayCo
  >  +  where b'{"cardsindbcount": 0, "cardsindeckcount": 0, "cardsreviewedtodaycount": 0}\n' = <built-in method lower of bytes object at 0x7f90895e6b10>()
  >  +    where <built-in method lower of bytes object at 0x7f90895e6b10> = b'{"cardsInDbCount": 0, "cardsInDeckCount": 0, "cardsReviewedTodayCount": 0}\n'.lower
  >  +  and   75 = len(b'{"cardsInDbCount": 0, "cardsInDeckCount": 0, "cardsReviewedTodayCount": 0}\n')
  >  +    where b'{"cardsInDbCount": 0, "cardsInDeckCount": 0, "cardsReviewedTodayCount": 0}\n' = CompletedProcess(args=['/workspace/executable', 'stats', '/tmp/tmpgpwzja4v'], returncode=0, stdout=b'{"car
  >  +  and   b'{"cardsInDbCount": 0, "cardsInDeckCount": 0, "cardsReviewedTodayCount": 0}\n' = CompletedProcess(args=['/workspace/executable', 'stats', '/tmp/tmpgpwzja4v'], returncode=0, stdout=b'{"cards
- *(... 34 more in this cluster)*

### `rc_mismatch_got0_want1` — 16 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_check_command.test_check_nonexistent_directory`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '/nonexistent/path/that/does/not/exist'], returncode=0, stdout=b'{"check": "ok"}\n', stderr=b'').returncode
- `tests.test_check_command.test_check_file_instead_of_directory`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '/tmp/tmpryvedlxx/test.txt'], returncode=0, stdout=b'{"check": "ok"}\n', stderr=b'').returncode
- `tests.test_export_command.test_export_nonexistent_directory`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'export', '/nonexistent/path'], returncode=0, stdout=b'{"export": "ok"}\n', stderr=b'').returncode
- *(... 13 more in this cluster)*

### `rc_mismatch_got0_want2` — 15 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_orphans_command.test_orphans_invalid_subcommand`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'orphans', 'invalid'], returncode=0, stdout=b'hashcards orphans\n\nManage orphan cards (cards not in any deck)\n\nUsage:\n  hashcards orph
- `tests.test_orphans_command.test_orphans_no_subcommand`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'orphans'], returncode=0, stdout=b'drill\ncheck\nstats\norphans\nexport\n--card-limit\n--port\n--from-deck\n--open-browser\n', stderr=b'')
- `tests.test_stats_command.test_stats_json_multiple_decks`
  > assert 0 == 2
- *(... 12 more in this cluster)*

### `returned_none` — 11 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_main_help.test_help_has_usage_line`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f86f4626680>('^Usage: executable <COMMAND>\\s*$', 'hashcards 0.1.0\nTool that emits structured JSON on stdout (tests json.loads it)\n\nUsage:\n  hashcards <COMM
  >  +    where <function search at 0x7f86f4626680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_main_help.test_help_lists_each_command[help]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f86f4626680>('^\\s*help\\s+', 'hashcards 0.1.0\nTool that emits structured JSON on stdout (tests json.loads it)\n\nUsage:\n  hashcards <COMMAND> [OPTIONS]\n\nCo
  >  +    where <function search at 0x7f86f4626680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_subcommand_help.test_subcommand_help_shape[args0-^Drill cards through a web interface\\s*$-^Usage: executable drill \\[OPTIONS\\] \\[DIRECTORY\\]\\s*$]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f86f4626680>('^Drill cards through a web interface\\s*$', '--card-limit\n--port\n--from-deck\n--open-browser\n--format\n--output\nUsage:\n', flags=re.MULTILINE)
  >  +    where <function search at 0x7f86f4626680> = re.search
  >  +    and   '--card-limit\n--port\n--from-deck\n--open-browser\n--format\n--output\nUsage:\n' = CompletedProcess(args=['/workspace/executable', 'drill', '--help'], returncode=0, stdout='--card-limit\n
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 8 more in this cluster)*

### `rc_mismatch_got0_want3` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_collection_operations.test_stats_counts_all_cards`
  > assert 0 == 3
- `tests.test_collection_operations.test_stats_with_mixed_card_types`
  > assert 0 == 3
- `tests.test_cli_edge_cases.test_stats_with_multiple_deck_files`
  > assert 0 == 3
- *(... 5 more in this cluster)*

### `uncategorized` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_db_gaps2.test_export_session_with_no_reviews`
  > sqlite3.OperationalError: no such table: sessions
- `tests.test_harvest.test_fsrs_initial_stability_easy`
  > requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=35615): Max retries exceeded with url: / (Caused by NewConnectionError("HTTPConnection(host='127.0.0.1', port=35615): Fai
- `tests.test_harvest.test_fsrs_initial_stability_good`
  > requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=35099): Max retries exceeded with url: / (Caused by NewConnectionError("HTTPConnection(host='127.0.0.1', port=35099): Fai
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want4` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_collection_operations.test_stats_multiple_decks`
  > assert 0 == 4
- `tests.test_collection.test_collection_nested_subdirectories`
  > assert 0 == 4
- `tests.test_collection.test_collection_unusual_deck_names`
  > assert 0 == 4
- *(... 1 more in this cluster)*

### `missing_file` — 3 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_collection.test_collection_reuses_existing_database`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpyk4dcjji/hashcards.db'
- `tests.test_database.test_database_persists_across_commands`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/hc_db_tko5t4q1/hashcards.db'
- `tests.test_database.test_database_readonly_commands_dont_modify`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/hc_db_dfn2eb_v/hashcards.db'

### `rc_mismatch_got15_want0` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_collection_operations.test_orphans_empty_for_new_collection`
  > assert 15 == 0
  >  +  where 15 = len(b'{"orphans": []}')
  >  +    where b'{"orphans": []}' = <built-in method strip of bytes object at 0x7f908984d330>()
  >  +      where <built-in method strip of bytes object at 0x7f908984d330> = b'{"orphans": []}\n'.strip
  >  +        where b'{"orphans": []}\n' = CompletedProcess(args=['/workspace/executable', 'orphans', 'list', '/tmp/tmpjmzp715r'], returncode=0, stdout=b'{"orphans": []}\n', stderr=b'').stdout
- `tests.test_orphans_command.test_orphans_list_no_orphans`
  > assert 15 == 0
  >  +  where 15 = len(b'{"orphans": []}')
  >  +    where b'{"orphans": []}' = <built-in method strip of bytes object at 0x7f9089642770>()
  >  +      where <built-in method strip of bytes object at 0x7f9089642770> = b'{"orphans": []}\n'.strip
  >  +        where b'{"orphans": []}\n' = CompletedProcess(args=['/workspace/executable', 'orphans', 'list', '/tmp/tmp5l67ewb6'], returncode=0, stdout=b'{"orphans": []}\n', stderr=b'').stdout

### `rc_mismatch_got0_want16` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_stats_export_check.test_stats_cwd_default_directory`
  > assert 0 == 16

### `rc_mismatch_got0_want150` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_collection.test_collection_large_many_decks`
  > assert 0 == 150

