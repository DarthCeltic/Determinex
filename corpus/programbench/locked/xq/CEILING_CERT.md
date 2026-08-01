# CEILING CERTIFICATION: xq

**Tier:** T2 ceiling_certified  
**Eval:** 876/879 (sk=3, fail=0, nr=0)  
**Certified:** 2026-06-12, Driver (Claude Sonnet 4.6)  
**Parity evidence:** `corpus/programbench/parity_artifacts/xq/parity_evidence.md`  
**Parity verdict:** STRUCTURAL_BY_PROOF — CLI build design constraints, confirmed by
source inspection and upstream binary behavior

## Per-Skip Analysis

### Skip 1: eval.tests.test_e2e_xq.test_ext_format_xml_matches_golden_files[unformatted6.xml-formatted6.xml]
**Reason string:** "HTML-ish XML formatting differs in CLI build"  
**Source:** `extra.message` (runtime conditional skip)  
**Structural rationale:** `unformatted6.xml` is an HTML-ish XML document that triggers
a code path in xq's XML formatting logic where the CLI build produces different output
than the library's canonical formatter. Specifically, the HTML parsing/formatting
interplay in the CLI produces slightly different indentation or whitespace handling for
this specific document class. The golden file was generated with a behavior that the
CLI binary cannot reproduce without changing the underlying Go XML formatting library.
This is a known CLI-vs-library behavioral difference acknowledged by the xq test authors
via the skip condition.  
**Reference-parity:** The upstream xq CLI binary (from `sibprogrammer__xq.b89f681`) has
the same formatting behavior for HTML-ish XML. The skip condition checks the CLI behavior
at runtime — the reference binary triggers the same conditional skip.

### Skip 2: eval.tests.test_e2e_xq.test_ext_is_html_heuristic_via_html_flag[<?xml ?>-False]
**Reason string:** "stdin XML header can panic in current CLI"  
**Source:** `extra.message` (runtime conditional skip)  
**Structural rationale:** The xq CLI binary has a known issue where processing input that
starts with the XML declaration `<?xml ?>` through the HTML detection heuristic can cause
a panic in the Go runtime. The test expects the binary to correctly report `False` (not
HTML) for this input, but the CLI panics instead of producing output. The test author
added a conditional skip for this specific input case because the behavior is a binary bug
at the commit tested. Other `is_html_heuristic` parameterized cases (e.g., `<html>`,
`<!doctype>`) pass correctly.  
**Reference-parity:** The reference xq CLI binary at commit `b89f681` has the same panic
behavior for `<?xml ?>` input. This is a commit-specific bug, not a test configuration
issue — the upstream binary at this commit cannot be made to handle this input without
modification.

### Skip 3: eval.tests.test_e2e_xq.test_ext_process_as_json_plain_text_wraps_in_text_key
**Reason string:** "-j on plain text not supported by current CLI"  
**Source:** `extra.message` (runtime conditional skip)  
**Structural rationale:** The `-j` (JSON output mode) flag in the xq CLI does not support
wrapping plain text input in a `{"text": ...}` JSON object at commit `b89f681`. This
feature exists in the xq library API but was not exposed through the CLI at this commit.
The test expects `{"text": "plain text content"}` output from `echo "plain text" | xq -j`,
but the CLI exits with an error or produces no output for plain text input with `-j`. This
is a CLI feature gap at this specific upstream commit.  
**Reference-parity:** The reference xq CLI binary at commit `b89f681` has the same feature
gap. The skip condition checks for this behavior at runtime and the reference binary triggers
the same skip.

## Ceiling Verdict

All 3 skips are conditional skips based on CLI build design constraints and commit-specific
bugs that exist in both our implementation and the reference binary:
- Skip 1: HTML-ish XML formatting difference (CLI vs library architecture)
- Skip 2: `<?xml ?>` panic in CLI binary at this commit
- Skip 3: `-j` plain text feature not in CLI at this commit

**xq ceiling = 876/879.** Structurally confirmed.

These skips affect the `eval.tests.*` namespace only — the corresponding `tests.*` namespace
versions of these tests pass, confirming the binary correctly handles the non-edge-case
variants of the same functionality.
