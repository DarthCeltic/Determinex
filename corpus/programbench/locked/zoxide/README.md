# zoxide Lock Notes - 2026-05-12

Verified official score: **577/577**.

Evidence:

- `eval_report.json` copied from `T:/determinex-programbench/determinex_pb_pilot_015_v2/ajeetdsouza__zoxide.67ca1bc/ajeetdsouza__zoxide.67ca1bc.eval.json`

## Closing fix

The last remaining failure was:

`TestQueryKeywordMatching.test_last_keyword_must_be_in_last_component`

The buggy matcher accepted `zoxide query loc` for `/usr/local/bin` because it searched every keyword sequentially across the whole path. Real zoxide matching requires the final plain keyword, in normal query mode, to match the last path component. The final patch:

- Anchors the final keyword to the basename only for normal, non-interactive queries.
- Keeps slash/backslash-containing keyword searches on the full path, so queries like `foo/`, `oo/ba`, and `test\data` still work.
- Keeps interactive queries permissive, because parent-component matches are valid candidates in the interactive selector.

## Corpus lesson

When closing an almost-lock, never trust a single failing test name as the whole rule. First patch produced `570/577` because it over-applied basename anchoring. The lock came from narrowing the rule by mode and keyword shape, then rerunning official eval.

## NATIVE CONVERSION (2026-06-03)
Converted from a Python reimplementation to the REAL Rust upstream
(github.com/ajeetdsouza/zoxide) built at the PINNED commit `67ca1bc`
(the eval target). Official ProgramBench Docker eval: **577/577 passed**
(raw test_results all `passed`, 0 failed, 0 not-run; console dedup shows 531).
exe_hash `56eb200fbda271bc47af0c39e9b70754dc9e6b26119b517add9d3deadad57271`.
This lock is now genuine native support, not a python-wrapper-of-native.
First build at `main` scored 497/577 (import-command version drift) — pin the commit.
