# Action Sheet — rbakbashev__elfcat.52f8cc7

**Current:** 12.32%  (88/714)
**Pass / Fail / Skip:** 88 / 556 / 1
**Gap to 100%:** 87.68 percentage points (626 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_elf_parsing.test_parse_elf32_if_available`
  - reason: 32-bit compilation not available

## Failure clusters

556 failed tests grouped into 10 buckets (sorted by count).

### `missing_file` — 260 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_defs_utils.test_machine_x86`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_machine_x862/x86_exec.elf.html'
- `tests.test_defs_utils.test_machine_x86_64`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_machine_x86_642/x86_64_exec.elf.html'
- `tests.test_defs_utils.test_machine_arm_aarch32`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_machine_arm_aarch322/arm32_exec.elf.html'
- *(... 257 more in this cluster)*

### `rc_mismatch_got1_want0` — 120 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_elf_variants.test_big_endian_elf`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/tmp/tmp_6r3buit/bigendian.elf'], returncode=1, stdout=b'', stderr=b'').returncode
- `tests.test_elf_variants.test_elf_with_linux_abi`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpf790ikis/linux_abi.elf'], returncode=1, stdout=b'', stderr=b'').returncode
- `tests.test_elf_variants.test_elf_with_abi_version`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/tmp/tmp6buwkvef/abi_ver.elf'], returncode=1, stdout=b'', stderr=b'').returncode
- *(... 117 more in this cluster)*

### `other_assertion` — 87 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_h_flag_shows_usage`
  > AssertionError: assert b'Usage:' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert b'0.1.10' in b'elfcat\nUsage: elfcat <filename>\n'
  >  +  where b'elfcat\nUsage: elfcat <filename>\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'elfcat\nUsage: elfcat <filename>\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_v_flag`
  > AssertionError: assert b'elfcat' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-v'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 84 more in this cluster)*

### `boolean_false` — 46 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_input_handling.test_relative_path_basename_in_output`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpyzpl0kob/nested.elf.html').exists
- `tests.test_edge_cases.test_minimal_elf_header`
  > assert False
- `tests.test_path_handling.test_relative_path`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp5fmlygua/test.elf.html').exists
- *(... 43 more in this cluster)*

### `string_output_mismatch` — 21 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_defs_utils.test_nonexistent_file_error`
  > assert '' == 'Failed to re... (os error 2)'
  >   
  >   - Failed to read file "/tmp/nonexistent_file_xyz_12345_unique.elf": No such file or directory (os error 2)
- `tests.test_defs_utils.test_invalid_elf_magic`
  > AssertionError: assert '' == 'Failed to pa...t an ELF file'
  >   
  >   - Failed to parse ELF: mismatched magic: not an ELF file
- `tests.test_smoke.test_help_flag`
  > AssertionError: assert 'Usage: elfca... <filename>\n' == 'Usage: elfca...tml to CWD.\n'
  >   
  >     Usage: elfcat <filename>
  >   - Writes <filename>.html to CWD.
  >   ?                              -
  >   + Writes <filename>.html to CWD
  >   + elfcat
  >   + Usage: elfcat <filename>
- *(... 18 more in this cluster)*

### `rc_mismatch_got0_want1` — 14 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_usage`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'Failed\nFailed to\nFailed to parse ELF\nFailed to read file\nNo such file or directory\nUsage: elfcat <filename>\n
- `tests.test_basic_invocation.test_no_arguments`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'Failed\nFailed to\nFailed to parse ELF\nFailed to read file\nNo such file or directory\nUsage: elfcat <filename>\n
- `tests.test_edge_cases.test_invalid_endianness_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_edge_cases/invalid_endianness.elf'], returncode=0, stdout='', stderr='').returncode
- *(... 11 more in this cluster)*

### `rc_unexpected_zero` — 4 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_help_usage.test_no_args_is_nonzero_and_prints_usage`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout='Failed\nFailed to\nFailed to parse ELF\nFailed to read file\nNo such file or directory\nUsage: elfcat <filename>\nW
- `tests.test_basic.test_nonexistent_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/nonexistent/file/path.elf'], returncode=0, stdout='Failed\nFailed to\nFailed to parse ELF\nFailed to read file\nNo such file or director
- `eval.tests.test_elfcat_behavior.test_no_args_errors_with_usage`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'Failed\nFailed to\nFailed to parse ELF\nFailed to read file\nNo such file or directory\nUsage: elfcat <filename>\n
- *(... 1 more in this cluster)*

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_elfcat_behavior.test_help_exact`
  > AssertionError: assert b'Usage: elfc... <filename>\n' == b'Usage: elfc...tml to CWD.\n'
  >   
  >   At index 54 diff: b'\n' != b'.'
  >   
  >   Full diff:
  >   - (b'Usage: elfcat <filename>\nWrites <filename>.html to CWD.\n')
  >   ?                                                           -   -
  >   + (b'Usage: elfcat <filename>\nWrites <filename>.html to CWD\nelfcat\nUsage: elf'
- `eval.tests.test_elfcat_behavior.test_short_help_exact`
  > AssertionError: assert b'' == b'Usage: elfc...tml to CWD.\n'
  >   
  >   Full diff:
  >   - (b'Usage: elfcat <filename>\nWrites <filename>.html to CWD.\n')
  >   + b''

### `rc_mismatch_got4_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_version_format`
  > AssertionError: assert 4 == 2
  >  +  where 4 = len(['elfcat', 'Usage:', 'elfcat', '<filename>'])

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7fa6228f5120>(b'elfcat \\d+\\.\\d+\\.\\d+', b'elfcat\nUsage: elfcat <filename>\n')
  >  +    where <function match at 0x7fa6228f5120> = re.match
  >  +    and   b'elfcat\nUsage: elfcat <filename>\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'elfcat\nUsage: elfcat <filename>\n', stderr=b'').stdout

