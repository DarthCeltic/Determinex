# Action Sheet — facebookresearch__fasttext.1142dc4

**Current:** 17.17%  (114/664)
**Pass / Fail / Skip:** 114 / 238 / 0
**Gap to 100%:** 82.83 percentage points (550 tests)

## Failure clusters

238 failed tests grouped into 11 buckets (sorted by count).

### `other_assertion` — 157 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_autotune.TestAutotune.test_autotune_invalid_metric`
  > AssertionError: assert (0 != 0 or b'Unknown metric' in b'Read 0M words\nNumber of words:  100\nNumber of labels: 5\nProgress: 100.0% words/sec/thread: 1000 lr: 0.000000 avg.loss: 1.000000 ETA:   0h 0m
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'supervised', '-input', '/tmp/pytest-of-root/pytest-0/test_autotune_invalid_metric2/train_at_bad_metric.txt', '-output', '/tmp/pytest-of-r
  >  +  and   b'Read 0M words\nNumber of words:  100\nNumber of labels: 5\nProgress: 100.0% words/sec/thread: 1000 lr: 0.000000 avg.loss: 1.000000 ETA:   0h 0m 0s\n' = CompletedProcess(args=['/workspace/e
- `tests.test_basic_invocation.TestNoArguments.test_no_args_lists_all_commands`
  > AssertionError: assert b'supervised' in b''
- `tests.test_basic_invocation.TestInvalidCommand.test_invalid_command_shows_usage`
  > AssertionError: assert b'usage: fasttext' in b'Unknown command: invalidcommand\n'
  >  +  where b'Unknown command: invalidcommand\n' = CompletedProcess(args=['/workspace/executable', 'invalidcommand'], returncode=1, stdout=b'usage: fasttext <command> <args>\n\nThe commands supported by
- *(... 154 more in this cluster)*

### `rc_unexpected_zero` — 28 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.TestNoArguments.test_no_args_shows_usage`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'usage: fasttext <command> <args>\n\nThe commands supported by fasttext are:\n\n  supervised              train a s
- `tests.test_error_handling.TestInvalidInputHandling.test_test_with_missing_model`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'test', '/tmp/pytest-of-root/pytest-0/test_test_with_missing_model2/nonexistent.bin', '/tmp/pytest-of-root/pytest-0/test_test_with_missing
- `tests.test_error_handling.TestInvalidInputHandling.test_supervised_without_dash_in_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'supervised', '-input', '/tmp/pytest-of-root/pytest-0/test_supervised_without_dash_i2/train.txt', '-output', '/tmp/pytest-of-root/pytest-0
- *(... 25 more in this cluster)*

### `string_output_mismatch` — 23 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_errors_edge_cases.test_invalid_command_name_prints_usage_and_exits_nonzero`
  > AssertionError: assert 'Unknown comm...commandname\n' == 'usage: fastt...t vectors\n\n'
  >   
  >   + Unknown command: invalidcommandname
  >   - usage: fasttext <command> <args>
  >   - 
  >   - The commands supported by fasttext are:
  >   - 
  >   -   supervised              train a supervised classifier...
- `tests.test_errors_edge_cases.test_missing_model_file_throws_clear_error`
  > AssertionError: assert 'Model file c...t/model.bin\n' == 'terminate ca...or loading!\n'
  >   
  >   + Model file cannot be opened: /nonexistent/model.bin
  >   - terminate called after throwing an instance of 'std::invalid_argument'
  >   -   what():  /nonexistent/model.bin cannot be opened for loading!
- `tests.test_errors_edge_cases.test_test_command_missing_args_shows_usage`
  > AssertionError: assert 'Empty model path.\n' == 'usage: fastt...threshold\n\n'
  >   
  >   + Empty model path.
  >   - usage: fasttext test <model> <test-data> [<k>] [<th>]
  >   - 
  >   -   <model>      model filename
  >   -   <test-data>  test data filename (if -, read from stdin)
  >   -   <k>          (optional; 1 by default) predict top k labels
- *(... 20 more in this cluster)*

### `uncategorized` — 9 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_quantize_dump.TestDump.test_dump_dict`
  > ValueError: invalid literal for int() with base 10: 'the 10 word'
- `tests.test_word_vectors.TestPrintSentenceVectors.test_print_sentence_vector`
  > ValueError: could not convert string to float: b'the'
- `tests.test_word_vectors.TestPrintSentenceVectors.test_sentence_vector_dimensions`
  > ValueError: could not convert string to float: b'this'
- *(... 6 more in this cluster)*

### `bytes_output_mismatch` — 7 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.TestNoArguments.test_no_args_stderr_not_stdout`
  > AssertionError: assert b'usage: fast...t vectors\n\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'usage: fasttext <command> <args>\n\nThe commands supported by fasttext are'
  >   +  b':\n\n  supervised              train a supervised classifier\n  quantize   '
  >   +  b'             quantize a model to reduce the memory usage\n  test         '
  >   +  b'           evaluate a supervised classifier\n  test-label              pr'...
- `tests.test_basic_invocation.TestInvalidCommand.test_invalid_command_stderr_not_stdout`
  > AssertionError: assert b'usage: fast...t vectors\n\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'usage: fasttext <command> <args>\n\nThe commands supported by fasttext are'
  >   +  b':\n\n  supervised              train a supervised classifier\n  quantize   '
  >   +  b'             quantize a model to reduce the memory usage\n  test         '
  >   +  b'           evaluate a supervised classifier\n  test-label              pr'...
- `tests.test_error_handling.TestInvalidInputHandling.test_predict_with_missing_model`
  > AssertionError: assert b'Model file ...t/model.bin\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'Model file cannot be opened for loading: /nonexistent/model.bin\n')
- *(... 4 more in this cluster)*

### `rc_mismatch_got101_want2` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_quantize_dump.TestDump.test_dump_input_matrix`
  > AssertionError: assert 101 == 2
  >  +  where 101 = len(['the', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', ...])
- `tests.test_quantize_dump.TestDump.test_dump_output_matrix`
  > AssertionError: assert 101 == 2
  >  +  where 101 = len(['__label__class1', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', ...])
- `tests.test_quantize_dump.test_dump_input_shows_input_matrix`
  > AssertionError: assert 101 == 2
  >  +  where 101 = len(['the', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', ...])
- *(... 1 more in this cluster)*

### `rc_mismatch_got100_want10` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_word_vectors.TestPrintWordVectors.test_print_word_vector_for_known_word`
  > assert 100 == 10
  >  +  where 100 = len([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...])
- `tests.test_word_vectors.TestPrintWordVectors.test_word_vector_dimensions_match`
  > assert 100 == 10
  >  +  where 100 = len([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...])
- `tests.test_model_io.test_cbow_model_save_load`
  > AssertionError: assert 100 == 10
  >  +  where 100 = len(['0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', ...])

### `empty_list_or_string` — 3 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_vectors_queries.test_print_ngrams_basic`
  > IndexError: list index out of range
- `tests.test_vectors_queries.test_print_ngrams_short_word`
  > IndexError: list index out of range
- `tests.test_vectors_queries.test_print_ngrams_word_with_spaces`
  > IndexError: list index out of range

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_autotune.test_autotune_with_different_modelsize_units`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpq8xm5rs7/model_k.ftz').exists
  >  +      where PosixPath('/tmp/tmpq8xm5rs7/model_k.ftz') = Path('/tmp/tmpq8xm5rs7/model_k.ftz')
- `tests.test_quantize_dump.test_dump_all_options_on_bin_model`
  > AssertionError: assert False
  >  +  where False = <built-in method isdigit of str object at 0x7f44c9847430>()
  >  +    where <built-in method isdigit of str object at 0x7f44c9847430> = 'the 10 word'.isdigit

### `rc_mismatch_got100_want15` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_model_io.test_skipgram_model_save_load`
  > AssertionError: assert 100 == 15
  >  +  where 100 = len(['0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', ...])

### `rc_mismatch_got101_want6` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_vectors_queries.test_print_word_vectors_oov_word`
  > AssertionError: assert 101 == 6
  >  +  where 101 = len(['unknownword', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', ...])

