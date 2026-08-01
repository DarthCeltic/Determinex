# Action Sheet — svenstaro__genact.16f96e3

**Current:** 0.42%  (1/236)
**Pass / Fail / Skip:** 1 / 229 / 0
**Gap to 100%:** 99.58 percentage points (235 tests)

## Failure clusters

229 failed tests grouped into 3 buckets (sorted by count).

### `other_assertion` — 121 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli.test_list_modules_long_flag`
  > AssertionError: --list-modules failed: genact: error: unrecognized argument: --list-modules
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--list-modules'], returncode=2, stdout='', stderr='genact: error: unrecognized argument: --list-modules\n').returncode
- `tests.test_cli.test_completion_bash_generates_valid_script`
  > AssertionError: bash completion failed: genact: error: unrecognized argument: --print-completions
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--print-completions', 'bash'], returncode=2, stdout='', stderr='genact: error: unrecognized argument: --print-completions\n').returncode
- `tests.test_cli.test_completion_zsh_generates_valid_script`
  > AssertionError: zsh completion failed: genact: error: unrecognized argument: --print-completions
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--print-completions', 'zsh'], returncode=2, stdout='', stderr='genact: error: unrecognized argument: --print-completions\n').returncode
- *(... 118 more in this cluster)*

### `rc_mismatch_got2_want0` — 77 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_core_coverage.test_terraform_multiple_cloud_providers`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--modules', 'terraform', '--exit-after-modules', '1', '--speed-factor', '1000'], returncode=2, stdout='', stderr='genact: error: unrecogn
- `tests.test_core_coverage.test_mkinitcpio_hooks_output`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--modules', 'mkinitcpio', '--exit-after-modules', '1', '--speed-factor', '1000'], returncode=2, stdout='', stderr='genact: error: unrecog
- `tests.test_core_coverage.test_mkinitcpio_os_release`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--modules', 'mkinitcpio', '--exit-after-modules', '1', '--speed-factor', '1000'], returncode=2, stdout='', stderr='genact: error: unrecog
- *(... 74 more in this cluster)*

### `string_output_mismatch` — 31 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli.test_version_long_flag`
  > AssertionError: assert 'genact 0.1.0\n' == 'genact 1.5.1\n'
  >   
  >   - genact 1.5.1
  >   ?          ^^^
  >   + genact 0.1.0
  >   ?        ++  ^
- `tests.test_cli.test_version_short_flag`
  > AssertionError: assert 'genact 0.1.0\n' == 'genact 1.5.1\n'
  >   
  >   - genact 1.5.1
  >   ?          ^^^
  >   + genact 0.1.0
  >   ?        ++  ^
- `tests.test_cli.test_help_long_flag`
  > assert "genact 0.1.0...: 'default'\n" == 'A nonsense a...int version\n'
  >   
  >   - A nonsense activity generator
  >   + genact 0.1.0
  >     
  >   - Usage: executable [OPTIONS]
  >   + usage: genact [OPTIONS] [ARGS]
  >     ...
- *(... 28 more in this cluster)*

