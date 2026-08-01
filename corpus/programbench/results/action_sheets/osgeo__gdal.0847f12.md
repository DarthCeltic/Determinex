# Action Sheet — osgeo__gdal.0847f12

**Current:** 7.23%  (74/1023)
**Pass / Fail / Skip:** 74 / 625 / 1
**Gap to 100%:** 92.77 percentage points (949 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest.test_gdal_completion_lco`
  - reason: GPKG driver not available in minimal build

## Failure clusters

625 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 204 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_version_output`
  > AssertionError: assert b'GDAL' in b'gdal 0.1.0\n'
  >  +  where b'gdal 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'gdal 0.1.0\n', stderr=b'').stdout
- `tests.test_basic.test_help_output`
  > AssertionError: assert b'Usage: gdal <COMMAND>' in b'gdal 0.1.0 - bootstrap scaffold\n\nUsage: gdal [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'gdal 0.1.0 - bootstrap scaffold\n\nUsage: gdal [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executable'
- `tests.test_basic.test_help_short_flag`
  > AssertionError: assert b'Usage: gdal <COMMAND>' in b'gdal 0.1.0 - bootstrap scaffold\n\nUsage: gdal [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'gdal 0.1.0 - bootstrap scaffold\n\nUsage: gdal [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executable'
- *(... 201 more in this cluster)*

### `boolean_false` — 181 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_dataset.test_dataset_copy`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpxf4v7e7w/copy.tif').exists
  >  +      where PosixPath('/tmp/tmpxf4v7e7w/copy.tif') = Path('/tmp/tmpxf4v7e7w/copy.tif')
- `tests.test_dataset.test_dataset_copy_overwrite`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpwqhrqsco/copy.tif').exists
  >  +      where PosixPath('/tmp/tmpwqhrqsco/copy.tif') = Path('/tmp/tmpwqhrqsco/copy.tif')
- `tests.test_dataset.test_dataset_delete`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpoyknw3b7/to_delete.tif').exists
  >  +      where PosixPath('/tmp/tmpoyknw3b7/to_delete.tif') = Path('/tmp/tmpoyknw3b7/to_delete.tif')
- *(... 178 more in this cluster)*

### `json_output_missing_or_bad` — 104 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_dataset_advanced.test_dataset_copy_preserves_content`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_dataset_check_advanced.test_dataset_check_json_usage`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_error_paths.test_json_usage_raster_convert`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 101 more in this cluster)*

### `rc_mismatch_got0_want1` — 54 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic.test_unknown_command_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nonexistent_command'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_dataset_advanced.test_dataset_check_invalid_file`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'dataset', 'check', '/tmp/tmp4np8r9p1/bad.tif'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_paths.test_raster_info_missing_input`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'raster', 'info'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 51 more in this cluster)*

### `missing_file` — 33 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_mdim.test_vector_sql_multiple`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp7gn44r48/out.geojson'
- `tests.test_more_coverage.test_vector_filter_active_layer`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpookmw55d/out.geojson'
- `tests.test_more_coverage.test_vector_sql_dialect`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp6ycu97q_/out.geojson'
- *(... 30 more in this cluster)*

### `string_output_mismatch` — 31 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_help_format.test_global_help`
  > AssertionError: assert 'gdal 0.1.0 -...int version\n' == 'Usage: gdal ...se of GDAL.\n'
  >   
  >   + gdal 0.1.0 - bootstrap scaffold
  >   - Usage: gdal <COMMAND> [OPTIONS]
  >   - where <COMMAND> is one of:
  >   -   - convert:  Convert a dataset (shortcut for 'gdal raster convert' or 'gdal vector convert').
  >   -   - dataset:  Commands to manage datasets.
  >   -   - driver:   Command for driver specific operations....
- `tests.test_help_format.test_help_short_flag`
  > AssertionError: assert 'gdal 0.1.0 -...int version\n' == 'Usage: gdal ...se of GDAL.\n'
  >   
  >   + gdal 0.1.0 - bootstrap scaffold
  >   - Usage: gdal <COMMAND> [OPTIONS]
  >   - where <COMMAND> is one of:
  >   -   - convert:  Convert a dataset (shortcut for 'gdal raster convert' or 'gdal vector convert').
  >   -   - dataset:  Commands to manage datasets.
  >   -   - driver:   Command for driver specific operations....
- `tests.test_help_format.test_raster_subcommand_help`
  > AssertionError: assert '' == 'Usage: gdal ...se of GDAL.\n'
  >   
  >   - Usage: gdal raster <SUBCOMMAND> [OPTIONS]
  >   - where <SUBCOMMAND> is one of:
  >   -   - as-features:     Create features from pixels of a raster dataset
  >   -   - aspect:          Generate an aspect map
  >   -   - blend:           Blend/compose two raster datasets
  >   -   - calc:            Perform raster algebra...
- *(... 28 more in this cluster)*

### `rc_unexpected_zero` — 7 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_raster_blend_compare.test_raster_compare_size_difference`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'raster', 'compare', '/workspace/autotest/gcore/data/byte.tif', '/workspace/autotest/gcore/data/1bit_2bands.tif'], returncode=0, stdout=b'
- `tests.test_harvest.test_gdal_question_mark`
  > assert 0 != 0
- `tests.test_mdim_additional.test_mdim_convert_array_group_mutually_exclusive`
  > assert 0 != 0
- *(... 4 more in this cluster)*

### `rc_mismatch_got2_want0` — 4 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic.test_drivers_output_is_json`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--drivers'], returncode=2, stdout=b'', stderr=b"gdal: unknown option: --drivers\nusage: gdal [OPTIONS] [ARGS]\nTry 'gdal --help' for more
- `tests.test_basic.test_drivers_have_required_fields`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--drivers'], returncode=2, stdout=b'', stderr=b"gdal: unknown option: --drivers\nusage: gdal [OPTIONS] [ARGS]\nTry 'gdal --help' for more
- `tests.test_basic.test_json_usage_output`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--json-usage'], returncode=2, stdout=b'', stderr=b"gdal: unknown option: --json-usage\nusage: gdal [OPTIONS] [ARGS]\nTry 'gdal --help' fo
- *(... 1 more in this cluster)*

### `returned_none` — 4 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_raster_overview.test_overview_add_multiple_levels`
  > assert None is not None
- `tests.test_raster_overview.test_overview_add_single_level`
  > assert None is not None
- `tests.test_raster_overview.test_overview_add_multiple_sequential_calls`
  > assert None is not None
- *(... 1 more in this cluster)*

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_info_shortcut.test_convert_shortcut_vector`
  > NameError: name 'Path' is not defined

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_dataset.test_rename_with_overwrite_succeeds`
  > AssertionError: assert b'different content' == b'II*\x00\x08...0\x00\x00\x00'
  >   
  >   At index 0 diff: b'd' != b'I'
  >   
  >   Full diff:
  >   + (b'different content')
  >   - (b'II*\x00\x08\x00\x00\x00\x10\x00\x00\x01\x03\x00\x01\x00\x00\x00\n\x00'
  >   -  b'\x00\x00\x01\x01\x03\x00\x01\x00\x00\x00\n\x00\x00\x00\x02\x01'...

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_raster_additional.test_compare_nodata_difference`
  > AssertionError: assert 0 == 3
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'raster', 'compare', '--reference', '/workspace/eval/test_resources/test_raster_additional/simple.tif', '/workspace/eval/test_resources/te

