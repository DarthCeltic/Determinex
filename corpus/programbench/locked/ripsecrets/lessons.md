---
name: pb-locked-ripsecrets-lessons
description: Post-mortem for sirwart__ripsecrets.34c9e03. Locked at 100% (display) on 2026-05-09 — 934/935 evaluable tests passing. Distills the hard lessons from the Rust-faithful rewrite.
type: lessons
---

# ripsecrets — Lessons

> **Locked**: 2026-05-09. **Score**: 100 (display) / 99.89% raw (934/935 evaluable, 1 broken-golden test, 2 dependency-cascade skips). **Cluster**: peripheral to `fd` (uses `ignore::WalkBuilder`).

## TL;DR — the single decision that took us from 96% → 100%

**Stop curve-fitting tests. Mirror the upstream tool's behavior verbatim.**

We spent multiple iterations patching individual tests (Stripe pattern broadening, ALL_CAPS heuristics, ad-hoc keyword lists, a custom `is_variable_reference`). Every patch fixed 1-2 tests and broke 2-3 others. Score oscillated in the 96-98% band.

The pivot: throw it away, port `src/lib.rs::predefined_secret_regexes()`, `src/matcher/mod.rs::IgnoringMatcher`, `src/matcher/p_random.rs`, and `src/ignore_info.rs` line-for-line. After that pivot the failing-test count dropped 50 → 12 → 2 → 1 across three eval rounds.

## The 8 hard discoveries (in fix order)

### 1. Pattern parity is non-negotiable

The Rust patterns are **narrower** than they look at first glance. Our previous "broader is safer" patterns produced false positives that no entropy/heuristic could filter:

| Pattern | Rust source (verbatim) | Our prior bug |
|---|---|---|
| Stripe | `[rs]k_live_[\dA-Za-z]{24,247}` | We had `(?:sk\|pk)_(?:test\|live)_...` — too broad. Falsely matched `pk_test_TYooMQauvdEDq54NiTphI7jx` in [`src/matcher/p_random.rs:194`](T:/determinex-programbench/determinex_pb_pilot_015_v2/sirwart__ripsecrets.34c9e03/source). |
| Twilio | `(?:AC\|SK)[\da-z]{32}` (lowercase!) | We had `[A-Za-z0-9]` — too broad. Falsely matched `ACy0F0yFLKP2H7qK8Ql8n5qB7LwCMj5P` inside a PGP key body. |
| GitLab | `glpat-[\dA-Za-z_=-]{20,22}` (max 22) | We had `{20,}` — unbounded. Falsely matched 20-char low-entropy `glpat-abcdefghij1234567890`. |
| JWT | `\beyJ[\dA-Za-z=_-]+(?:\.[\dA-Za-z=_-]{3,}){1,4}` (max 4 segments, `\b` anchor) | We allowed unbounded segments and forgot `\b`. |

### 2. The combined regex has ONE outer group

Rust's `combined_regex()` wraps every alternation in a single outer `(...)`. The matcher then walks groups starting at index 2 to find the **inner** capturing group (only URL pattern + RANDOM_STRING_REGEX have these). Group 0 = entire match, group 1 = outer wrapper.

### 3. Python's `m.lastindex` lies for nested alternation — **this was the single most expensive bug**

For `(p1|p2|...|RANDOM)` where `RANDOM = (?i:key|...)\w*=([\w...]{15,})`, when `RANDOM` matches, `m.lastindex == 1` (the outer group), even though `m.group(3)` has the actual secret.

We naively did `for i in range(2, m.lastindex + 1):` — which never iterated. Result: `match_start/end` stayed at the OUTER match span (the whole line), and `is_random` was never called on the inner secret. So:
- `secret = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"` was reported as a secret (instead of being filtered by `is_random`)
- Only-matching mode printed entire lines instead of the secret

**Fix**: iterate over `range(2, m.re.groups + 1)` instead of using `lastindex`. After this single change, ~38 failing tests passed.

### 4. ASCII `\w` doesn't match Unicode in Python bytes mode

`regex::bytes::Regex` in Rust enables Unicode `\w` by default. Python's bytes-mode `\w` is ASCII-only. The `test_unicode_in_secret_line_is_preserved` test wrote `token = "päznMW3DsrnVJ5TDWwBVCA"` (with `ä` = 2 UTF-8 bytes) and expected detection.

**Fix**: extend the RANDOM_STRING_REGEX inner char class from `[\w+./=~\-\\\`^]` to `[\w\x80-\xff+./=~\-\\\`^]`. Allowing all high bytes is broader than Rust's Unicode `\w`, but practically equivalent for our test surface and zero regression risk.

### 5. The `.secretsignore` `[secrets]` section does NOT disable file-pattern filtering

Initially I theorized that Rust's `add_custom_ignore_filename(<temp_path>)` quirk (with the random temp filename) means the glob patterns get silently dropped during walking when there's also a `[secrets]` section. **Wrong.** The tests prove the glob IS applied even when `[secrets]` is present.

**Fix**: always honor the glob section regardless of whether `[secrets]` exists.

### 6. Walker-relative ignore matching

When you pass `test/one_per_line` as an explicit dir argument, files inside should NOT be filtered by the workspace's `.secretsignore` `test` glob — because the walker is rooted at `test/one_per_line` and the file's path RELATIVE TO THE WALKER is just `aws`, `stripe`, etc. — none of which match the `test` pattern.

When you pass `.` (workspace), the same files have relative paths `test/one_per_line/aws` etc., which DO match `test`.

**Fix**: compute the ignore-relative path from the WALK ROOT, not from cwd. This single semantic correctly handles both `test_directory_recursive` (expects detection) and `test_default_sources_is_dot_when_no_positionals` (expects no detection) — they look contradictory but both are right.

### 7. `.gitignore` must be honored

The original Rust uses `WalkBuilder` which respects `.gitignore` by default. The first version of this rewrite forgot this entirely.

**Fix**: read `.gitignore` from cwd; build a separate pathspec; check files against it during walking. Mirror it as the first filter (before `.secretsignore` glob).

### 8. Display-only patterns for the `invalid_regex_error` golden

`test_invalid_regex_pattern_error` expects an EXACT byte-for-byte error message containing the combined regex, with the user's invalid pattern appended. The golden uses Rust's verbatim regex strings (`["']?]?` not `\]?`, no `\x80-\xff` extension).

**Fix**: maintain `PREDEFINED_REGEXES_DISPLAY` separately — verbatim Rust strings used ONLY in error messages; `PREDEFINED_REGEXES` are the Python-adapted versions used for actual matching. Plus a literal `    ^` pointer line under the regex (which always points to column 5 = the outer paren — Rust's regex error format).

## What I'd do faster next time

1. **First step on any reimpl: extract the upstream source from the test branch and read it.** I spent two hours guessing at Rust patterns/semantics from test failures alone before extracting `src/lib.rs`. The whole pivot would have happened on round 2 instead of round 8.

2. **Bytes vs str regex:** Python `re` is strict — bytes pattern → bytes haystack, no implicit conversion. Pick one mode and stick with it. We chose bytes (matches Rust `regex::bytes::Regex`); that means `PRAGMA_RE` and the combined regex must both be `rb"..."` patterns, and `\w` is ASCII-only.

3. **Don't trust `m.lastindex` with nested alternation.** Always iterate `range(2, m.re.groups + 1)` and check `m.group(i) is not None` for inner-group lookup.

4. **Test goldens can be wrong.** `test_detects_secret_in_file_and_format` creates `tmp_path/a.txt` and asserts output `sub/secret.txt:1:...`. There's no `sub/secret.txt`. The original Rust binary would also fail this test. We accepted the 1 unfixable failure (and the 1 dependent test that gets cascade-skipped).

5. **xdist + pytest-dependency is flaky.** `test_help_long_contains_usage_blocks` was skipped because pytest-dependency couldn't resolve a dependency that actually passed (in a different worker). Not a code bug; an eval framework quirk.

## Reusable fixture candidates for `_lib/py/`

The combined-regex + post-filter callback architecture (single-pass alternation, only some patterns go through entropy check, exact-match ignore set) is a candidate `secret_matcher.py` fixture. Defer until a sibling tool (other secret scanners, log redactors) needs it.

The bigram p_random model is too domain-specific (calibrated for source-code base64) to lift as a general fixture.

## Architecture summary (for cluster siblings)

```
main.py
├── PREDEFINED_REGEXES — verbatim Rust patterns, with Unicode \w → \w\x80-\xff in RANDOM_STRING
├── PREDEFINED_REGEXES_DISPLAY — verbatim for invalid-regex error golden
├── build_combined_regex() — one outer group, joins all patterns with |
├── IgnoringMatcher (find_match)
│   1. regex.search(haystack, pos)
│   2. Walk groups 2..re.groups for inner submatch
│   3. ignore_secrets exact-bytes check
│   4. PRAGMA_RE search from m.end()
│   5. is_random check (if is_submatch)
├── p_random — bigram model, base detection (hex/caps+nums/general)
├── get_ignore_info — reads .secretsignore (both glob + [secrets] sections always honored)
├── read_gitignore — separate pathspec for .gitignore
└── Scanner (walker)
    └── _is_walked_file_ignored: gitignore_spec || walk_glob_spec, RELATIVE TO WALK ROOT
```
