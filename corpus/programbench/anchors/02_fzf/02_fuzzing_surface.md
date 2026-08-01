---
name: fzf-fuzzing-surface
description: Specific testable behaviors in fzf. Heavy emphasis on --filter mode; query-syntax matrix; field-selector edges; tie-break ordering; exit codes.
type: fuzzing-surface
---

# fzf — Fuzzing Attack Surface

2,164 tests across 11 branches. The 1,017-test branch is almost certainly the matcher correctness suite. The 616/347-test branches likely cover query syntax + field selection. Bake these flags in:

## CLI matrix

### Search / matching
- `--algo=v1|v2` (default v2)
- `-i` / `--ignore-case`, `-x` / `--exact`, default smart-case
- `+i` / `--case-sensitive`
- `--literal` (no fuzzy)
- `--scheme=default|path|history` — bonus profile presets
- `-e` / `--exact` — same as quote-prefix on every word
- `-q QUERY` / `--query QUERY` — pre-fill (then read stdin)
- `-f QUERY` / `--filter QUERY` — non-interactive; **the PB-test path**
- `--phony` (a.k.a. `--disabled`) — match all, query is a label

### Result control
- `--no-sort` (preserves input order, filter only)
- `--tac` (reverse input order)
- `--tiebreak=KIND[,KIND...]` (KIND ∈ length, chunk, pathname, begin, end, index)
- `--no-multi` / `-m` / `--multi=N`
- `--exit-0` / `-0` (exit immediately if no matches)
- `--select-1` / `-1` (auto-select if exactly one match)

### Field selectors
- `-d DELIM` / `--delimiter=DELIM` (default `\t`, can be regex)
- `-n FIELDS` / `--nth=FIELDS` (which fields to match against)
- `--with-nth=FIELDS` (which fields to display)
- Field syntax: `1`, `2`, `-1` (last), `1..3` (range), `..3` (first three), `2..` (second to end)

### I/O
- `--read0` (input separator is NUL)
- `--print0` (output separator is NUL)
- `--ansi` (strip ANSI codes from input lines)
- `--no-headers`

### Output prints
- `--print-query` (prefix output with the query line)
- `--expect=KEYS` (interactive)

### Headers / preview / interactive — usually skipped in tests
- `--height`, `--min-height`, `--reverse`, `--layout`, `--border`, `--margin`, `--padding`
- `--preview`, `--preview-window`, `--prompt`, `--header`, `--info`
- `--bind=...` mappings — interactive

## Query-syntax matrix (parser must implement all)

| Syntax | Meaning | Example |
|--------|---------|---------|
| `word` | fuzzy match | `app` matches `application` |
| `'word` | exact substring | `'app` matches `app` exactly somewhere |
| `^prefix` | prefix match | `^lib` matches `libfoo` |
| `suffix$` | suffix match | `.txt$` matches `note.txt` |
| `!word` | NOT fuzzy | excludes lines fuzzy-matching `word` |
| `!'word` | NOT exact | excludes lines containing `word` |
| `!^prefix` | NOT prefix | |
| `!suffix$` | NOT suffix | |
| `=word` | exact equal-to-line | matches line that IS exactly `word` |
| `space` | AND between terms | `app txt` = both must match |
| `\space` | escaped space (literal) | matches `a b` literally |
| `pipe` `\|` | OR within term group | `app \| foo` matches either |

Precedence: parse query → split on unescaped spaces → each token is a Term group → split Term group on `|` → Term. AND across the top-level groups; OR within a group. **A negation can apply only to a non-OR term.**

## Output-format edges (where 90→100% lives)

1. **Filter output ordering**: `--filter X` emits matches in **score-desc, index-asc** order. Same as interactive's default top-to-bottom.
2. **Score equality + tie-break**: when scores tie, secondary key is `--tiebreak` ordering. Default is `length` → shorter wins → then `index` (input order).
3. **Empty query in `--filter`**: prints all items in input order (smart: matches are scored 0 with no positions).
4. **`--with-nth` shadowing matching**: matching is on the line transformed by `--with-nth` UNLESS `--nth` overrides. Edge: `-d , -n 1 --with-nth 2` matches field 1 but displays field 2.
5. **`--print0` with `--filter`**: NUL between outputs, no trailing NUL.
6. **`--ansi` strips codes from match candidate but PRESERVES them in output** by default. `--no-ansi` does not exist in current fzf; use `--no-ansi=false` is invalid. Verify.
7. **CRLF input handling**: `\r` is stripped from matching but is part of the displayed line UNLESS the line ends with `\r\n` then `\r` is stripped on output too.
8. **UTF-8 width**: CJK chars are width 2; combining chars are width 0. Bonuses are byte-offset based; rendering uses display width. Test surface stays on byte offsets in `--filter`.

## Exit codes

| Code | Condition |
|------|-----------|
| 0    | At least one match (interactive: user pressed Enter) |
| 1    | No matches |
| 2    | Bad usage / arg error |
| 130  | Interrupted (Ctrl-C / SIGINT) |

Interactive-only: 0 means selected; 1 means no match; 130 if cancelled.

## Stderr behavior

- All errors prefixed by `fzf: error: ` then a message.
- Bad regex in `--filter` mode: `fzf: error: failed to compile regex: ...`.
- Unknown flag: `unknown option: --foo`.

## Testable feature combos likely to surprise

1. **`--filter "" --no-sort`** — emit input verbatim (matches all, original order).
2. **`--filter X` with no input** — exits 1 with no output (no matches by definition).
3. **`-d ' ' -n 2 --filter X`** — matches field 2 only; field 1 is irrelevant.
4. **`--read0 --print0`** with NUL-separated stream — must round-trip.
5. **`--tiebreak=length,begin`** — apply length first, then position-of-first-match.
6. **Smart-case turns off when query has any uppercase** — `Foo` in query is case-sensitive even with default settings.
7. **`--exact -e` and quoted query** — `'word` doesn't double up; `-e` is the same as auto-quoting all terms.
8. **Phony mode** — `--phony` (a.k.a. `--disabled`) means query has no matching effect; useful for header-only tests.
9. **Empty input** — `printf '' | fzf -f x` → exit 1.

## What the eval test names will probably look like

Expected (based on jq's pattern):
- `test_fuzzy_match_v2`, `test_exact_match`, `test_prefix_match`, `test_suffix_match`, `test_negation`, `test_and_or`
- `test_field_selectors`, `test_with_nth`, `test_delimiter`
- `test_tac`, `test_no_sort`, `test_tiebreak_length`, `test_tiebreak_index`
- `test_smart_case`, `test_case_sensitive`, `test_ignore_case`
- `test_read0`, `test_print0`, `test_ansi`
- `test_filter_mode`, `test_print_query`, `test_select_1`, `test_exit_0`
- `test_unicode`, `test_emoji`, `test_cjk`

Probability that the interactive event loop is tested at all: low (PB can't easily drive raw-mode IO). If it is, expect a tiny minority of tests; defer until eval confirms.
