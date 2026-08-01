# Action Sheet — burntsushi__xsv.f430466

**Current:** 2.48%  (38/1535)
**Pass / Fail / Skip:** 38 / 1042 / 1
**Gap to 100%:** 97.52 percentage points (1497 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_commands_basic.test_headers_command`
  - reason: test_headers_command depends on test_count_headers_vs_no_headers

## Failure clusters

1042 failed tests grouped into 4 buckets (sorted by count).

### `other_assertion` — 569 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_command`
  > assert ('nonexistent_command' in '  File "/workspace/main.py", line 1118\n    def\n       ^\nSyntaxError: invalid syntax\n' or 'match' in '  file "/workspace/main.py", line 1118\n    def\n       ^\nsy
  >  +  where '  file "/workspace/main.py", line 1118\n    def\n       ^\nsyntaxerror: invalid syntax\n' = <built-in method lower of str object at 0x7f8494298390>()
  >  +    where <built-in method lower of str object at 0x7f8494298390> = '  File "/workspace/main.py", line 1118\n    def\n       ^\nSyntaxError: invalid syntax\n'.lower
- `tests.test_basic.test_invalid_command`
  > assert (b'Could not match' in b'  File "/workspace/main.py", line 1118\n    def\n       ^\nSyntaxError: invalid syntax\n' or b'Usage:' in b'  File "/workspace/main.py", line 1118\n    def\n       ^\nS
  >  +  where b'  File "/workspace/main.py", line 1118\n    def\n       ^\nSyntaxError: invalid syntax\n' = CompletedProcess(args=['/workspace/executable', 'invalidcommand'], returncode=1, stdout=b'', std
  >  +  and   b'  File "/workspace/main.py", line 1118\n    def\n       ^\nSyntaxError: invalid syntax\n' = CompletedProcess(args=['/workspace/executable', 'invalidcommand'], returncode=1, stdout=b'', std
  >  +  and   b'' = CompletedProcess(args=['/workspace/executable', 'invalidcommand'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 1118\n    def\n       ^\nSyntaxError: invalid sy
- `tests.test_basic.test_missing_file`
  > assert (b'no such file' in b'  file "/workspace/main.py", line 1118\n    def\n       ^\nsyntaxerror: invalid syntax\n' or b'not found' in b'  file "/workspace/main.py", line 1118\n    def\n       ^\ns
- *(... 566 more in this cluster)*

### `rc_mismatch_got1_want0` — 439 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_additional_commands.test_flatten_basic`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'flatten', '/tmp/tmp68lt0_45/data.csv'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 1118\n    def\n       ^\nSyn
- `tests.test_additional_commands.test_flatten_separator`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'flatten', '-s', '---', '/tmp/tmprueaq7sa/data.csv'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 1118\n    def\n
- `tests.test_additional_commands.test_flatten_condense`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'flatten', '-c', '10', '/tmp/tmpoofjo_i3/data.csv'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 1118\n    def\n 
- *(... 436 more in this cluster)*

### `string_output_mismatch` — 33 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_errors.test_invalid_command_name`
  > assert 'File "/works...nvalid syntax' == 'Could not ma...ts", "table"]'
  >   
  >   - Could not match 'invalidcommand' with any of the allowed variants: ["cat", "count", "fixlengths", "flatten", "fmt", "frequency", "headers", "help", "index", "input", "join", "partition", "reverse"
  >   + File "/workspace/main.py", line 1118
  >   +     def
  >   +        ^
  >   + SyntaxError: invalid syntax
- `tests.test_errors.test_uppercase_command_rejected`
  > assert 'File "/works...nvalid syntax' == "xsv expects ...mean 'count'?"
  >   
  >   - xsv expects commands in lowercase. Did you mean 'count'?
  >   + File "/workspace/main.py", line 1118
  >   +     def
  >   +        ^
  >   + SyntaxError: invalid syntax
- `tests.test_errors.test_select_missing_required_argument`
  > assert 'File "/works...nvalid syntax' == 'Invalid argu...select --help'
  >   
  >   + File "/workspace/main.py", line 1118
  >   +     def
  >   +        ^
  >   + SyntaxError: invalid syntax
  >   - Invalid arguments.
  >   - ...
- *(... 30 more in this cluster)*

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_main_gapfill.test_broken_pipe_exit_zero`
  > AssertionError: assert '' == 'a,b'
  >   
  >   - a,b

