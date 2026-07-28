# ProgramBench Paused Tool 100% Lock Gap Report

Generated from official eval JSON artifacts. This report is guidance for post-lane work; it does not change scores.

## Snapshot

| Tool | Passed | Runnable | Score | Remaining Failures |
|---|---:|---:|---:|---:|
| `dutree` | 558 | 947 | 58.92% | 359 |
| `csview` | 317 | 347 | 91.35% | 30 |
| `grex` | 1147 | 1405 | 81.64% | 258 |
| `fzf` | 742 | 1212 | 61.22% | 470 |
| `hck` | 775 | 856 | 90.54% | 81 |

## Diagnosis

### dutree

The failures are dominated by byte-exact directory tree output: directory totals, aggregation thresholds, depth pruning, hidden/exclude filtering, symlink accounting, LS_COLORS, and byte/KiB rendering all interact. The current implementation is close enough for shallow CLI tests but lacks an upstream-compatible filesystem accounting model.

Top failure clusters:

- 27x `stdout/stderr fixture exactness | AssertionError: assert '[ test 16.28... 0 B\n' == '[ test 16.53... 0 B\n'`
  Sample: `tests.test_core.test_basic_directory_traversal`
- 26x `argument/tree transform interaction | AssertionError: assert '[ test 16.28... 12.28 KiB\n' == '[ test 16.53... 12.53 KiB\n'`
  Sample: `tests.test_core.test_summary_flag`
- 21x `color/env exactness | AssertionError: assert '[ testdir 4.... 0 B\n' == '[ testdir 17... 0 B\n'`
  Sample: `tests.test_colors.test_ls_colors_basic_parsing`
- 17x `argument/tree transform interaction | AssertionError: assert '[ dir1 6.75 ... 256 B\n' == '[ dir1 2.94 ... 256 B\n'`
  Sample: `tests.test_core.test_depth_limit_deep`
- 16x `argument/tree transform interaction | AssertionError: assert '[ test 16.28... 0 B\n' == '[ test 16.53... 0 B\n'`
  Sample: `tests.test_core.test_depth_limit_1`
- 11x `argument/tree transform interaction | AssertionError: assert '[ test 16.28... 1.53 KiB\n' == '[ test 16.53... 1.59 KiB\n'`
  Sample: `tests.test_core.test_aggregation_threshold`
- 10x `stdout/stderr fixture exactness | AssertionError: assert '[ test 13.53... 0 B\n' == '[ test 13.59... 0 B\n'`
  Sample: `tests.test_core.test_combined_exclude_and_hidden_flags`
- 9x `stdout/stderr fixture exactness | AssertionError: assert '[ test 12.52... 0 B\n' == '[ test 12.51... 0 B\n'`
  Sample: `tests.test_core.test_files_only_flag`
- 7x `stdout/stderr fixture exactness | AssertionError: assert '[ test 16666... 0 B\n' == '[ test 16928... 0 B\n'`
  Sample: `tests.test_core.test_bytes_flag_formatting`
- 5x `argument/tree transform interaction | AssertionError: assert '[ test 16.53... 12.53 KiB\n' == '[ test 16.28... 12.28 KiB\n'`
  Sample: `tests.test_flags.test_aggr_2m`

100% rebuild path:

- Build a filesystem snapshot layer that records path type, apparent size, disk-usage size, symlink target size, hidden status, and deterministic child order before rendering.
- Port the aggregation model as a pure tree transform: depth cut, files-only, exclude/no-hidden filters, then small-file aggregation. Do not mix these rules into print code.
- Create one renderer that consumes annotated tree nodes and emits Unicode/ASCII, colorized/plain, bytes/human sizes from the same model.
- Add a local fixture replay harness that runs selected extracted `dutree` test resources against the override without editing tests.

Regression tripwires:

- `-a` optional value parsing must not consume following flags.
- Official gate requires runnable stability; filesystem tests can become runnable/unrunnable if paths or permission behavior drift.
- Do not special-case single golden files; the same size model feeds most remaining failures.

### csview

The remaining failures are table byte-exactness and sniffing edge cases: style `grid`, `ascii2`, and `none`, header-only tables, wide emoji, sniff limit truncation, non-UTF8 byte offsets, and file-not-found text. The CSV parser mostly works; the ceiling is formatter parity.

Top failure clusters:

- 3x `stdout/stderr fixture exactness | AssertionError: assert '┌──────┬────...───┴──────┘\n' == '┌──────┬────...───┴──────┘\n'`
  Sample: `tests.test_edge_cases.test_header_only_no_data_rows`
- 1x `encoding/error byte exactness | AssertionError: Expected exact UTF-8 error message`
  Sample: `tests.test_edge_cases.test_non_utf8_input_error`
- 1x `sniff/windowing exactness | AssertionError: Sniff-limited output should match golden`
  Sample: `tests.test_edge_cases.test_sniff_limit_truncates_wide_content`
- 1x `renderer/table exactness: grid | AssertionError: assert '┌────────┬──...─┴────────┘\n' == '┌────────┬──...─┴────────┘\n'`
  Sample: `tests.test_edge_cases.test_style_grid`
- 1x `renderer/table exactness: ascii2 | AssertionError: assert '+----------+...+---------+\n' == ' name |...울 | 한국 \n'`
  Sample: `tests.test_edge_cases.test_style_ascii2`
- 1x `renderer/table exactness: style none | AssertionError: assert ' item ... #x1F370 \n' == ' item r... #x1F370 \n'`
  Sample: `tests.test_edge_cases.test_style_none_no_borders`
- 1x `sniff/windowing exactness | AssertionError: assert '┌──────┬────... │\n' == '┌─────┬─────...sc17 │\n'`
  Sample: `tests.test_formatting.test_sniff_limited_100`
- 1x `sniff/windowing exactness | AssertionError: assert '┌──────┬────... │\n' == '┌──────┬────...sc17 │\n'`
  Sample: `tests.test_formatting.test_sniff_default_1000`
- 1x `renderer/table exactness: grid | AssertionError: assert '┌───┬───────...───┴──────┘\n' == '┌───┬───────...───┴──────┘\n'`
  Sample: `tests.test_formatting.test_style_grid_with_number`
- 1x `renderer/table exactness: style none | AssertionError: assert ' name age...25 LA \n' == ' name age ... 25 LA \n'`
  Sample: `tests.test_formatting.test_style_none_with_padding`

100% rebuild path:

- Introduce a table-layout oracle object: parsed rows, display widths, padding policy, borders, numbering column, indentation, and style tokens.
- Replay every `eval/test_resources` golden for `grid`, `ascii2`, and `none` through the same renderer and diff bytes before official gates.
- Replace ad-hoc sniff logic with a deterministic 100-row/width sampler that keeps the same row subset the tests expect.
- Calculate UTF-8 parse errors from raw bytes so byte index reporting matches upstream instead of decoded string offsets.

Regression tripwires:

- Unicode display width is not `len()`: emoji and CJK need wcwidth-style accounting.
- `style none` still has padding and separators; it is not raw CSV.
- Header-only and empty-input paths must share the renderer, not bypass it.

### grex

The large behavior swap is done. Remaining failures require a real regex expression tree: verbose nested repetition formatting, prefix/suffix factoring, char-class collapse, per-token colorization, stdin/file input ordering, and clap-style validation. String assembly is now the limiting factor.

Top failure clusters:

- 13x `color/env exactness | AssertionError: assert '\x1b[40;93m(...33m$\x1b[0m\n' == '\x1b[40;93m(...33m$\x1b[0m\n'`
  Sample: `tests.test_anchors_display.test_colorize_verbose_combined`
- 11x `color/env exactness | AssertionError: assert '\x1b[1;33m^\...33m$\x1b[0m\n' == '\x1b[1;33m^\...33m$\x1b[0m\n'`
  Sample: `tests.test_anchors_display.test_colorize_with_repetitions`
- 4x `verbose renderer exactness | AssertionError: assert '(?x)\n^\n I...9}{2}\\.\n$\n' == '(?x)\n^\n I...9}{2}\\.\n$\n'`
  Sample: `tests.test_success_0000.test_succeeds_with_escape_and_verbose_mode_option_008`
- 4x `verbose renderer exactness | AssertionError: assert '(?x)\n^\n I...dca9}\\.\n$\n' == '(?x)\n^\n I...}\n \\.\n$\n'`
  Sample: `tests.test_success_0000.test_succeeds_with_escape_and_surrogate_and_verbose_mode_option_009`
- 4x `verbose renderer exactness | AssertionError: assert '(?x)\n^\n \...f4a9}\\.\n$\n' == '(?x)\n^\n \...f4a9}\\.\n$\n'`
  Sample: `tests.test_success_0000.test_succeeds_with_escape_and_verbose_mode_option_026`
- 4x `verbose renderer exactness | AssertionError: assert '(?x)\n^\n \...dca9}\\.\n$\n' == '(?x)\n^\n \...dca9}\\.\n$\n'`
  Sample: `tests.test_success_0000.test_succeeds_with_escape_and_surrogate_and_verbose_mode_option_027`
- 4x `verbose renderer exactness | AssertionError: assert '(?x)\n^\n \...9}{2}\\.\n$\n' == '(?x)\n^\n \...9}{2}\\.\n$\n'`
  Sample: `tests.test_success_0000.test_succeeds_with_escape_and_verbose_mode_option_029`
- 4x `verbose renderer exactness | AssertionError: assert '(?x)\n^\n \...dca9}\\.\n$\n' == '(?x)\n^\n \...}\n \\.\n$\n'`
  Sample: `tests.test_success_0000.test_succeeds_with_escape_and_surrogate_and_verbose_mode_option_030`
- 3x `verbose renderer exactness | AssertionError: assert '(?x)\n^\n \...\ \\S{3}\n$\n' == '(?x)\n^\n \...\n ){2}\n$\n'`
  Sample: `tests.test_success_0060.test_succeeds_with_verbose_mode_option_067`
- 3x `verbose renderer exactness | AssertionError: assert '(?x)\n^\n I...\W\\W\\W\n$\n' == '(?x)\n^\n I...\W\\W\\W\n$\n'`
  Sample: `tests.test_success_0060.test_succeeds_with_verbose_mode_option_070`

100% rebuild path:

- Create AST node types: Literal, CharClass, Sequence, Alternation, Optional, Repeat, Anchor, FlagGroup, CaptureGroup.
- Make synthesis produce that AST first, then render normal, verbose, and colorized output from the same tree.
- Implement factoring passes on the AST: common prefix/suffix, single-character alternation to ranges, repeated substring detection, and optional branch collapse.
- Add a fixture replay command for `eval/test_resources/test_anchors_display`, `test_char_classes`, and repetition goldens before official gates.
- Move clap-style validation into a table-driven parser so `--with-surrogates`, zero minimums, and empty test cases share exact error text.

Regression tripwires:

- Verbose mode indentation and color tokens must wrap syntax tokens, not whole strings.
- The same AST must render normal and colorized forms; separate string paths will keep diverging.
- Stdin/file collection order changes can pass some tests and regress many others.

### fzf

The accepted line is 742/1212. A later shell-integration patch would have raised passes, but it caused a pytest internal error and changed runnable tests by -151, so the gate correctly rejected it. The remaining accepted failures are mostly fuzzy/filter algorithm semantics, TUI/key rendering, and a smaller help/man/version surface.

Top failure clusters:

- 116x `help/version exactness | assert 2 == 0`
  Sample: `tests.test_advanced.test_bash_integration_script`
- 60x `stdout/stderr fixture exactness | AssertionError: assert 1 == 0`
  Sample: `tests.test_algorithms.test_prefix_match_variations`
- 12x `stdout/stderr fixture exactness | AssertionError: assert 0 == 2`
  Sample: `tests.test_edge_cases_advanced.test_invalid_scheme`
- 10x `stdout/stderr fixture exactness | assert 1 == 0`
  Sample: `tests.test_basic.test_extended_search_exact`
- 10x `help/version exactness | assert 2 == 1`
  Sample: `tests.test_core.test_exit0_with_zero_matches_returns_no_match`
- 6x `stdout/stderr fixture exactness | AssertionError: assert 0 != 0`
  Sample: `tests.test_history.test_history_invalid_path_not_a_directory`
- 6x `stdout/stderr fixture exactness | assert (0 > 0)`
  Sample: `tests.test_keybindings.TestEditingKeys.test_ctrl_a_beginning_of_line`
- 5x `stdout/stderr fixture exactness | AssertionError:`
  Sample: `tests.test_io.test_case_insensitive_by_default`
- 4x `stdout/stderr fixture exactness | AssertionError: assert False`
  Sample: `tests.test_history.test_history_file_created_when_nonexistent`
- 3x `stdout/stderr fixture exactness | AssertionError: assert 1 == 4`
  Sample: `tests.test_algorithms.test_fuzzy_match_spacing`

100% rebuild path:

- Do not reapply the rejected --bash/--zsh/--fish implementation until runnable stability is understood; active source must stay at iter3.
- Build a pure filter-engine test harness first: parse fzf extended search syntax, OR groups, suffix/prefix anchors, quoted exact terms, nth fields, and scoring order.
- Separate non-interactive `-f/--filter` behavior from TUI rendering so algorithm fixes can gate without touching PTY branches.
- For shell integration, reproduce the pytest internal error locally and fix collection/runtime stability before attempting another official gate.
- Treat keybinding/border tests as a second renderer track after filter-engine gains flatten.

Regression tripwires:

- Any patch that changes runnable total is reject-only even if passed count rises.
- Shell integration handlers can alter branch collection behavior; verify total/runnable before trusting pass deltas.
- Filter mode must return rc 0 with empty stdout for no selected lines only where upstream does; rc drift is common here.

### hck

hck is now a near-lock tool at 775/856. The remaining failures are not broad recovery; they are cut-like semantics: delimiter literal handling, header/index ordering, duplicate and mixed selections, invalid field-spec errors, invalid UTF-8 byte passthrough, and a few compressed input/help exactness cases.

Top failure clusters:

- 15x `stdout/stderr fixture exactness | assert 2 == 0`
  Sample: `tests.test_hck.TestDelimiterHandling.test_comma_delimiter_literal`
- 3x `argument/tree transform interaction | AssertionError: assert 0 != 0`
  Sample: `tests.test_edge_cases.test_leading_comma_in_field_spec_error`
- 2x `argument/tree transform interaction | AssertionError: assert '\n\n\n\n' == ''`
  Sample: `tests.test_fields_exclude.test_exclude_complete_overlap`
- 2x `stdout/stderr fixture exactness | AssertionError: assert 0 == 2`
  Sample: `eval.tests.test_argparse_validation.test_negative_number_is_not_accepted_as_value_without_double_dash`
- 2x `encoding/error byte exactness | AssertionError: assert [b'a\xef\xbf\...f\xbdz', b'c'] == [b'a\xed\xa0\x80z', b'c']`
  Sample: `eval.tests.test_executable_externalized.test_ext_test_read_several_single_values_with_invalid_utf8`
- 2x `stdout/stderr fixture exactness | AssertionError: assert 2 == 0`
  Sample: `eval.tests.test_executable_externalized.test_ext_test_reorder_no_split_found`
- 1x `stdout/stderr fixture exactness | AssertionError: assert 0 != 0`
  Sample: `tests.test_edge_cases.test_leading_delimiter`
- 1x `stdout/stderr fixture exactness | AssertionError: assert ('age' in 'name\nAlice\nBob\n' or '30' in 'name\nAlice\nBob\n')`
  Sample: `tests.test_mixed_selection.test_mixed_selection_output_ordering`
- 1x `stdout/stderr fixture exactness | AssertionError: assert '' == '\n\n'`
  Sample: `tests.test_delimiters.test_nonexistent_field_selection`
- 1x `encoding/error byte exactness | AssertionError: assert b'valid\tinva...f\xbd\ttail\n' == b'valid\tinva...f\xfe\ttail\n'`
  Sample: `tests.test_edge_cases.test_invalid_utf8_passthrough`

100% rebuild path:

- Replace remaining delimiter handling with a byte-oriented splitter that preserves leading/trailing empty fields and supports literal delimiter mode exactly.
- Represent selections as ordered selector nodes: field index, range, open range, header field, regex header, complement, and duplicates. Render from that list without dedup unless upstream does.
- Move field-spec validation before row processing so leading comma, trailing comma, double comma, zero, and inverted ranges produce exact rc/message.
- Keep invalid UTF-8 as bytes through selection and output; decode only for display paths that explicitly require text.
- Treat compression as an input adapter layer, not parser logic; xz/gzip/bzip2 errors should not corrupt normal stdin behavior.

Regression tripwires:

- Do not normalize Unicode replacement characters on byte-mode tests.
- Header-field and numeric-field selection order must follow user selection order, not table order.
- Delimiter literal mode and regex delimiter mode need separate paths; merging them regresses comma/tab cases.

## Shared Infrastructure Needed

- Add per-tool fixture replay commands before official Docker gates, using extracted tests under `T:/determinex-programbench/_extracted_tests/<slug>/...`.
- Keep official gate JSON as source of truth; local replay is only for fast byte-diff debugging.
- For each paused tool, replace one-off string emitters with a structured intermediate model, then render from that model.
- Before a new fzf shell-integration attempt, compare baseline and candidate `not_run`, `error`, `total`, and `runnable` counts locally; the prior rejected patch proved pass deltas can be misleading.
- For near-lock hck, keep patches narrow and byte-oriented; it is closer to 100 than the larger paused trio.
- Continue 4-lane Docker gating for remaining tools while these three get deeper hand-specialist rebuilds.
