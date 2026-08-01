# Action Sheet — filosottile__age.706dfc1

**Current:** 13.2%  (137/1038)
**Pass / Fail / Skip:** 137 / 417 / 50
**Gap to 100%:** 86.80 percentage points (901 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_age_targeted_coverage.TestDecryptPassphrasePaths.test_decrypt_passphrase_file_with_identity_gives_error`
  - reason: batchpass plugin not available
- `tests.test_age_targeted_coverage.TestEncryptedIdentityFile.test_encrypt_to_encrypted_identity`
  - reason: batchpass not available for encrypted identity test
- `tests.test_age_targeted_coverage.TestRecipientParseEdgeCases.test_ssh_rsa_recipient_from_file`
  - reason: RSA not supported
- `tests.test_age_targeted_coverage.TestMultipleIdentityTypes.test_encrypt_with_rsa_identity`
  - reason: RSA identity encrypt not supported
- `tests.test_age_targeted_coverage.TestMultipleIdentityTypes.test_encrypt_with_ed25519_identity`
  - reason: ed25519 identity encrypt not supported
- *(... 45 more skipped)*

## Failure clusters

417 failed tests grouped into 11 buckets (sorted by count).

### `rc_mismatch_got1_want0` — 228 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_age_advanced.TestRecipientsFile.test_recipients_file_short_flag`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-R', '/tmp/tmp0dd4hkrl/recipients.txt'], returncode=1, stdout=b'', stderr=b'age: error: no valid recipients\n').returncode
- `tests.test_age_advanced.TestRecipientsFile.test_recipients_file_long_flag`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--recipients-file', '/tmp/tmpkt3w2rc1/recipients.txt'], returncode=1, stdout=b'', stderr=b'age: error: no valid recipients\n').returncode
- `tests.test_age_advanced.TestRecipientsFile.test_recipients_file_multiple_keys`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-R', '/tmp/tmpywi90vsu/recipients.txt'], returncode=1, stdout=b'', stderr=b'age: error: no valid recipients\n').returncode
- *(... 225 more in this cluster)*

### `other_assertion` — 164 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_age_advanced.TestErrorEdgeCases.test_help_with_encrypt_flags`
  > AssertionError: assert b'Usage:' in b'age: error: unrecognized argument: -help\n'
  >  +  where b'age: error: unrecognized argument: -help\n' = CompletedProcess(args=['/workspace/executable', '-p', '-help'], returncode=2, stdout=b'', stderr=b'age: error: unrecognized argument: -help\n'
- `tests.test_age_advanced.TestErrorEdgeCases.test_help_short_with_flags`
  > AssertionError: assert b'Usage:' in b'age: error: unrecognized argument: -h\n'
  >  +  where b'age: error: unrecognized argument: -h\n' = CompletedProcess(args=['/workspace/executable', '-p', '-h'], returncode=2, stdout=b'', stderr=b'age: error: unrecognized argument: -h\n').stderr
- `tests.test_age_basic.TestNoArgs.test_no_args_shows_usage`
  > AssertionError: assert b'Usage:' in b'usage: age [--encrypt] [-r RECIPIENT] [--decrypt] [-i IDENTITY] [file]\n'
  >  +  where b'usage: age [--encrypt] [-r RECIPIENT] [--decrypt] [-i IDENTITY] [file]\n' = CompletedProcess(args=['/workspace/executable'], returncode=1, stdout=b'', stderr=b'usage: age [--encrypt] [-r R
- *(... 161 more in this cluster)*

### `rc_mismatch_got2_want0` — 8 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_age_batchpass.TestBatchpassBasic.test_batchpass_encrypt_decrypt`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-e', '-j', 'batchpass'], returncode=2, stdout=b'', stderr=b'age: error: unrecognized argument: -j\n').returncode
- `tests.test_age_batchpass.TestBatchpassBasic.test_batchpass_encrypt_to_file`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-e', '-j', 'batchpass', '-o', '/tmp/tmpvi3zeh3q/enc.age', '/tmp/tmpvi3zeh3q/input.txt'], returncode=2, stdout=b'', stderr=b'age: error: unrecogniz
- `tests.test_age_batchpass.TestBatchpassBasic.test_batchpass_armored_encrypt_decrypt`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-e', '-j', 'batchpass', '-a'], returncode=2, stdout=b'', stderr=b'age: error: unrecognized argument: -j\n').returncode
- *(... 5 more in this cluster)*

### `string_output_mismatch` — 7 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_age_core_gaps.test_encrypt_no_recipients_error`
  > AssertionError: assert 'age: error: ...s specified\n' == 'age: error: .../age/report\n'
  >   
  >   + age: error: no recipients specified
  >   - age: error: missing recipients
  >   - age: hint: did you forget to specify -r/--recipient, -R/--recipients-file or -p/--passphrase?
  >   - age: report unexpected or unhelpful errors at https://filippo.io/age/report
- `tests.test_age_core_gaps.test_decrypt_no_identities_error`
  > AssertionError: assert 'age: error: ...es provided\n' == 'age: error: .../age/report\n'
  >   
  >   + age: error: no identity files provided
  >   - age: error: the file is not passphrase-encrypted, identities are required
  >   - age: hint: specify identities with -i/--identity or -j to decrypt this file
  >   - age: report unexpected or unhelpful errors at https://filippo.io/age/report
- `tests.test_age_core_gaps.test_decrypt_wrong_identity_no_match`
  > AssertionError: assert 'age: error: ...ities found\n' == 'age: error: .../age/report\n'
  >   
  >   + age: error: no valid identities found
  >   - age: error: no identity matched any of the recipients
  >   - age: report unexpected or unhelpful errors at https://filippo.io/age/report
- *(... 4 more in this cluster)*

### `missing_file` — 2 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_age_basic.TestEncryptX25519.test_encrypt_to_file_decrypt_from_file`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp39rohdpo/dec.txt'
- `tests.test_age_keygen_extra.TestEncryptDecryptRoundtrip.test_file_roundtrip`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp7yv613_j/dec.bin'

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_age_coverage_boost.TestMoreArmorCoverage.test_armor_to_file_and_decrypt`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp9009r7wb/output.age').exists
- `tests.test_main_gaps.test_version_flag`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f4e19bb3af0>('v')
  >  +    where <built-in method startswith of str object at 0x7f4e19bb3af0> = 'age 1.1.1'.startswith

### `rc_unexpected_zero` — 2 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_age_error_paths.TestFlagConflicts.test_passphrase_with_recipients_file_fails`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-p', '-R', '/tmp/tmpaiy1ri3i/rec.txt'], returncode=0, stdout=b'age-encryption.org/v1\n---\n;c?c\x13\x94\xb3H\x1d&2\xd8\x17\x8dOH\x19G\xd6
- `tests.test_age_error_paths.TestFlagConflicts.test_identity_with_passphrase_fails`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-p', '-e', '-i', '/tmp/tmpmayvdoz0/key_89185604.txt'], returncode=0, stdout=b'age-encryption.org/v1\n---\n\xd1B\xbf7\x8c1\xa6\xbco\xe0\xf

### `json_output_missing_or_bad` — 1 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_age_inspect.TestInspectBasic.test_inspect_multiple_recipients`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_age_keygen_extra.TestEncryptDecryptRoundtrip.test_multiline_content`
  > AssertionError: assert b'' == b'line1\nline2\nline3\n'
  >   
  >   Full diff:
  >   - (b'line1\nline2\nline3\n')
  >   + b''

### `rc_mismatch_got2_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_multiple_input_files_error`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'file1.txt', 'file2.txt'], returncode=2, stdout=b'', stderr=b'age: error: unexpected argument: file2.txt\n').returncode

### `rc_mismatch_got0_want1` — 1 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_errors.test_passphrase_with_identity_encryption_error`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-e', '-p', '-i', '/tmp/pytest-of-root/pytest-0/test_passphrase_with_identity_2/identity.txt'], returncode=0, stdout=b'age-encryption.org/

