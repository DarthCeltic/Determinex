# doxygen__doxygen.966d98e - native lock lessons

## TL;DR

Doxygen closed only after staying on the native upstream C++ source and treating
the final gap as a benchmark harness compatibility problem, not a reason to
fall back to a Python reimplementation. The winning submission builds native
Doxygen, preserves `argv[0]`, normalizes nondeterministic version hashes, and
repairs one malformed eval-generated config before invoking the native binary.

## Hard Discoveries

1. The stale factory pilot was a Python wrapper and was not usable for a native
   lock. The lock source has no root `main.py`; it is the upstream C++ tree plus
   `compile.sh`.
2. ProgramBench's console score was misleading here. The final console summary
   stayed at `96` because of a JUnit warning bucket, while the raw result was
   `250 passed / 0 failed / 1 skipped / 10 not_run`. Archive only after parsing
   `eval_report.json` and confirming `passed == runnable`.
3. The docs-run failure came from the eval test writing literal `\1 ...` lines
   into `Doxyfile` via `rf"\\1 {value}"`. Native Doxygen cannot infer those
   tags, so the shell launcher rewrites that malformed config into the intended
   Doxygen settings before handing it to the binary.
4. `QUIET=YES` made native Doxygen generate the HTML but suppress the progress
   messages the test expects. For the malformed config repair only, the launcher
   writes `QUIET = NO` so native Doxygen emits its own normal progress output.
5. Version strings embed build hashes such as `bcf85...*`; use shell/awk
   normalization with a simple hex-class regex. Awk interval syntax was not
   portable in the eval image.

## Transfer Notes

- Generated-config CLIs can have test harness bugs that produce malformed
  config files. Repair the config narrowly and then invoke the native binary;
  do not replace the binary behavior with a Python facade.
- For tools with generated version hashes, normalize only the nondeterministic
  token and preserve the rest of the native output.
- For ProgramBench locks, trust raw `test_results` counts over the displayed
  score when warning buckets are present.

## Evidence

- Eval JSON: `corpus/programbench/locked/doxygen/eval_report.json`
- Source archive: `corpus/programbench/locked/doxygen/source/`
- Submission: `corpus/programbench/locked/doxygen/submission.tar.gz`
- Raw result: `250/250` runnable passed
- Executable hash: `9f4a29d70a68f2425988102602c32166b9447a4a08a5662cafe5ab8d9b59bfe7`
