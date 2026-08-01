# Action Sheet — gromacs__gromacs.665ea4c

**Current:** 0.32%  (4/1264)
**Pass / Fail / Skip:** 4 / 336 / 10
**Gap to 100%:** 99.68 percentage points (1260 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_current.test_water_group_high_molecule_count`
  - reason: Binary crashes (SIGSEGV) with water-only group - known bug
- `tests.test_disre_successful_workflows.test_disre_basic_workflow`
  - reason: Test data not created yet. Run: cd eval/test_resources/test_disre_minimal && ./create_tpr.sh
- `tests.test_disre_successful_workflows.test_disre_multiple_outputs`
  - reason: Test data not created yet
- `tests.test_disre_successful_workflows.test_disre_with_ntop_parameter`
  - reason: Test data not created yet
- `tests.test_disre_successful_workflows.test_disre_maxdr_auto_detection`
  - reason: Test data not created yet
- *(... 5 more skipped)*

## Failure clusters

336 failed tests grouped into 7 buckets (sorted by count).

### `other_assertion` — 177 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_angle.test_angle_distribution_basic`
  > AssertionError: assert 'angles_backbone' in ''
- `tests.test_angle.test_dihedral_distribution_basic`
  > AssertionError: assert 'dihedrals_backbone' in ''
- `tests.test_angle.test_invalid_index_file_angles`
  > AssertionError: Should fail with invalid index file
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'angle', '-f', '/workspace/eval/test_resources/test_angle/trpcage.xtc', '-n', '/tmp/pytest-of-root/pytest-0/test_invalid_index_file_angles
- *(... 174 more in this cluster)*

### `missing_file` — 76 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_angle.test_angle_vs_time_output`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_angle_vs_time_output2/angle_vs_time.xvg'
- `tests.test_angle.test_angle_vs_time_all_flag`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_angle_vs_time_all_flag2/angle_vs_time_all.xvg'
- `tests.test_angle.test_binwidth_parameter`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_binwidth_parameter2/angle_dist_binwidth2.xvg'
- *(... 73 more in this cluster)*

### `boolean_false` — 38 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_angle.test_chandler_correlation`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = (PosixPath('/tmp/pytest-of-root/pytest-0/test_chandler_correlation2') / 'chandler_corr.xvg').exists
- `tests.test_chi_rama_helix.test_chi_with_normhisto_flag`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_chi_with_normhisto_flag2/chi_order.xvg').exists
- `tests.test_chi_rama_helix.test_chi_rama_flag_enables_ramachandran`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_chi_rama_flag_enables_ram2/chi_order.xvg').exists
- *(... 35 more in this cluster)*

### `rc_unexpected_zero` — 36 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_awh.test_awh_skip_zero_default`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'awh', '-f', '/workspace/eval/test_resources/test_energy/test.edr', '-s', '/workspace/eval/test_resources/test_energy/test.tpr', '-skip', 
- `tests.test_awh.test_awh_time_range_begin_only`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'awh', '-f', '/workspace/eval/test_resources/test_energy/test.edr', '-s', '/workspace/eval/test_resources/test_energy/test.tpr', '-b', '10
- `tests.test_awh.test_awh_time_range_end_only`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'awh', '-f', '/workspace/eval/test_resources/test_energy/test.edr', '-s', '/workspace/eval/test_resources/test_energy/test.tpr', '-e', '50
- *(... 33 more in this cluster)*

### `string_output_mismatch` — 6 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_check.test_single_xtc_file`
  > AssertionError: assert '' == '     :-) GRO...trpcage.xtc\n'
  >   
  >   -      :-) GROMACS - gmx check, VERSION (-:
  >   - 
  >   - Executable:   /workspace/executable
  >   - Data prefix:  /workspace/install
  >   - Working dir:  /workspace
  >   - Command line:...
- `tests.test_check.test_single_gro_structure`
  > AssertionError: assert '' == '     :-) GRO... --------\n\n'
  >   
  >   -      :-) GROMACS - gmx check, VERSION (-:
  >   - 
  >   - Executable:   /workspace/executable
  >   - Data prefix:  /workspace/install
  >   - Working dir:  /workspace
  >   - Command line:...
- `tests.test_check.test_compare_identical_trajectories`
  > AssertionError: assert '' == '     :-) GRO...d correctly\n'
  >   
  >   -      :-) GROMACS - gmx check, VERSION (-:
  >   - 
  >   - Executable:   /workspace/executable
  >   - Data prefix:  /workspace/install
  >   - Working dir:  /workspace
  >   - Command line:...
- *(... 3 more in this cluster)*

### `rc_mismatch_got2_want0` — 2 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic.test_gmx_no_args`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout='', stderr="usage: gromacs [OPTIONS] [ARGS]\nTry 'gromacs --help' for more information.\n").returncode
- `tests.test_basic.test_gmx_version`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-version'], returncode=2, stdout='', stderr="gromacs: unknown option: -version\nusage: gromacs [OPTIONS] [ARGS]\nTry 'gromacs --help' for

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_current.test_nojump_flag_affects_translational_dipole`
  > assert None is not None

