# Action Sheet — bellard__quickjs.d7ae12a

**Current:** 0.0%  (0/3036)
**Pass / Fail / Skip:** 0 / 350 / 0
**Gap to 100%:** 100.00 percentage points (3036 tests)

## Failure clusters

350 failed tests grouped into 4 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 260 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced_features.test_proxy_basic_get_trap`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--eval', "\nconst target = {name: 'Alice', age: 30};\nconst handler = {\n  get(target, prop) {\n    console.log('Getting', prop);\n    re
- `tests.test_advanced_features.test_proxy_set_trap_modification`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--eval', "\nconst target = {x: 10};\nconst handler = {\n  set(target, prop, value) {\n    console.log('Setting', prop, 'to', value);\n   
- `tests.test_advanced_features.test_proxy_ownkeys_trap`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--eval', "\nconst target = {a: 1, b: 2, c: 3};\nconst handler = {\n  ownKeys(target) {\n    console.log('ownKeys called');\n    return ['
- *(... 257 more in this cluster)*

### `other_assertion` — 63 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_atom_memory_gaps.test_large_int_atoms`
  > AssertionError: Script failed: usage: quickjs [OPTIONS] [ARGS]
  >   Try 'quickjs --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_large_int_atoms2/test.js'], returncode=2, stdout='', stderr="usage: quickjs [OPTIONS] [ARGS]\nTry 'quic
- `tests.test_atom_memory_gaps.test_wrapped_primitives`
  > AssertionError: Script failed: usage: quickjs [OPTIONS] [ARGS]
  >   Try 'quickjs --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_wrapped_primitives2/test.js'], returncode=2, stdout='', stderr="usage: quickjs [OPTIONS] [ARGS]\nTry 'q
- `tests.test_atom_memory_gaps.test_closure_captured_variables`
  > AssertionError: Script failed: usage: quickjs [OPTIONS] [ARGS]
  >   Try 'quickjs --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_closure_captured_variable2/test.js'], returncode=2, stdout='', stderr="usage: quickjs [OPTIONS] [ARGS]\
- *(... 60 more in this cluster)*

### `string_output_mismatch` — 26 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_errors.test_syntax_error_unclosed_brace`
  > AssertionError: assert 'quickjs: unk...nformation.\n' == 'SyntaxError:...dline>:1:10\n'
  >   
  >   - SyntaxError: invalid property name
  >   -     at <cmdline>:1:10
  >   + quickjs: unknown option: --eval
  >   + usage: quickjs [OPTIONS] [ARGS]
  >   + Try 'quickjs --help' for more information.
- `tests.test_errors.test_syntax_error_unclosed_function`
  > AssertionError: assert 'quickjs: unk...nformation.\n' == 'SyntaxError:...dline>:1:17\n'
  >   
  >   - SyntaxError: unexpected token in expression: ''
  >   -     at <cmdline>:1:17
  >   + quickjs: unknown option: --eval
  >   + usage: quickjs [OPTIONS] [ARGS]
  >   + Try 'quickjs --help' for more information.
- `tests.test_errors.test_syntax_error_invalid_identifier`
  > AssertionError: assert 'quickjs: unk...nformation.\n' == 'SyntaxError:...mdline>:1:5\n'
  >   
  >   - SyntaxError: expecting ';'
  >   -     at <cmdline>:1:5
  >   + quickjs: unknown option: --eval
  >   + usage: quickjs [OPTIONS] [ARGS]
  >   + Try 'quickjs --help' for more information.
- *(... 23 more in this cluster)*

### `rc_mismatch_got2_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cutils_gaps.test_utf8_out_of_range_codepoint`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-e', 'console.log(String.fromCodePoint(0x200000))'], returncode=2, stdout='', stderr="quickjs: unknown option: -e\nusage: quickjs [OPTION

