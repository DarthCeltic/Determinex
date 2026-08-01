# Action Sheet — sharkdp__bat.f822bd0

**Current:** 2.55%  (30/1178)
**Pass / Fail / Skip:** 30 / 624 / 23
**Gap to 100%:** 97.45 percentage points (1148 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_diff.test_diff_submodule_graceful`
  - reason: Cannot create submodule in test environment
- `tests.test_harvest.test_pager_basic`
  - reason: Pager test requires PTY for interactive paging
- `tests.test_harvest.test_pager_basic_arg`
  - reason: Complex pager test requiring PTY and mocked pagers - skipped for harvest
- `tests.test_harvest.test_pager_overwrite`
  - reason: Complex pager test requiring PTY and mocked pagers - skipped for harvest
- `tests.test_harvest.test_pager_arg_override_env_withconfig`
  - reason: Complex pager test requiring PTY and mocked pagers - skipped for harvest
- *(... 18 more skipped)*

## Failure clusters

624 failed tests grouped into 5 buckets (sorted by count).

### `rc_mismatch_got1_want0` — 462 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_cache.test_cache_help`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'cache', '--help'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 23\n    USAGE = f"bat {TOOL_VERSION}\\n\\nA cat(1) 
- `tests.test_cache.test_cache_build_custom_source`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'cache', '--build', '--target', '/tmp/bat_test_x4t7zp6u/cache', '--source', '/workspace/tests/examples/cache_source'], returncode=1, stdou
- `tests.test_cache.test_cache_clear_removes_files`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'cache', '--build', '--target', '/tmp/bat_test_je4s5ie9/cache', '--source', '/workspace/tests/examples/cache_source'], returncode=1, stdou
- *(... 459 more in this cluster)*

### `other_assertion` — 148 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cache.test_cache_invalid_syntax_file_error`
  > assert 'bad.sublime-syntax: Invalid YAML file syntax' in '  File "/workspace/main.py", line 23\n    USAGE = f"bat {TOOL_VERSION}\\n\\nA cat(1) clone with syntax highlighting and Git integration.\\n\\n
  >  +  where '  File "/workspace/main.py", line 23\n    USAGE = f"bat {TOOL_VERSION}\\n\\nA cat(1) clone with syntax highlighting and Git integration.\\n\\nUSAGE:\\n    bat [OPTIONS] [FILE]...\\n    bat 
- `tests.test_decorations_gaps.test_line_numbers_wrap_continuation`
  > AssertionError:   File "/workspace/main.py", line 23
  >       USAGE = f"bat {TOOL_VERSION}\n\nA cat(1) clone with syntax highlighting and Git integration.\n\nUSAGE:\n    bat [OPTIONS] [FILE]...\n    bat [OPTIONS] [--] [FILE]...\n\nFLAGS:\n    -h, --help   
  >               ^
  >   SyntaxError: unterminated string literal (detected at line 23)
  >   
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--style=numbers', '--terminal-width=40', '--decorations=always', '--color=always', '/workspace/eval/test_resources/test_decorations_gaps/
- `tests.test_decorations_gaps.test_grid_only_no_numbers`
  > AssertionError:   File "/workspace/main.py", line 23
  >       USAGE = f"bat {TOOL_VERSION}\n\nA cat(1) clone with syntax highlighting and Git integration.\n\nUSAGE:\n    bat [OPTIONS] [FILE]...\n    bat [OPTIONS] [--] [FILE]...\n\nFLAGS:\n    -h, --help   
  >               ^
  >   SyntaxError: unterminated string literal (detected at line 23)
  >   
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--style=grid', '--decorations=always', '--color=always', '/workspace/eval/test_resources/test_decorations_gaps/long_lines.txt'], returnco
- *(... 145 more in this cluster)*

### `string_output_mismatch` — 11 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cache.test_cache_build_and_clear_conflict`
  > assert '  File "/wor...at line 23)\n' == "error: the a...y '--help'.\n"
  >   
  >   +   File "/workspace/main.py", line 23
  >   +     USAGE = f"bat {TOOL_VERSION}\n\nA cat(1) clone with syntax highlighting and Git integration.\n\nUSAGE:\n    bat [OPTIONS] [FILE]...\n    bat [OPTIONS] [--] [FILE]...\n\nFLAGS:\n    -h, --help 
  >   
  >   ...Full output truncated (8 lines hidden), use '-vv' to show
- `tests.test_cache.test_cache_source_requires_build`
  > assert '  File "/wor...at line 23)\n' == "error: the f...y '--help'.\n"
  >   
  >   +   File "/workspace/main.py", line 23
  >   +     USAGE = f"bat {TOOL_VERSION}\n\nA cat(1) clone with syntax highlighting and Git integration.\n\nUSAGE:\n    bat [OPTIONS] [FILE]...\n    bat [OPTIONS] [--] [FILE]...\n\nFLAGS:\n    -h, --help 
  >   
  >   ...Full output truncated (9 lines hidden), use '-vv' to show
- `tests.test_config.test_invalid_config_file_flag`
  > assert '  File "/wor...at line 23)\n' == 'error: unexp...e <COMMAND>\n'
  >   
  >   +   File "/workspace/main.py", line 23
  >   +     USAGE = f"bat {TOOL_VERSION}\n\nA cat(1) clone with syntax highlighting and Git integration.\n\nUSAGE:\n    bat [OPTIONS] [FILE]...\n    bat [OPTIONS] [--] [FILE]...\n\nFLAGS:\n    -h, --help 
  >   
  >   ...Full output truncated (9 lines hidden), use '-vv' to show
- *(... 8 more in this cluster)*

### `rc_mismatch_got1_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_core.test_invalid_style_component_error`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--color=never', '--style=invalid-style', '/workspace/eval/test_resources/test_core/multiline.txt'], returncode=1, stdout='', stderr='  Fi
- `tests.test_error_gaps.test_error_from_string`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--terminal-width=0'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 23\n    USAGE = f"bat {TOOL_VERSION}\\n\\nA cat(

### `sigpipe_unhandled` — 1 test(s)

**Quick patch ideas:**
- Top of main.py: `import signal; signal.signal(signal.SIGPIPE, signal.SIG_DFL)`

**Sample failures:**

- `tests.test_error_gaps.test_broken_pipe_exits_cleanly`
  > BrokenPipeError: [Errno 32] Broken pipe

