---
name: jq-impl-sequence
description: jq build order. Numbered steps from "passes 30% of tests on day 1" to "the 90→100% gap". Each step has an explicit gate; do not advance until the gate is green.
type: implementation-sequence
---

# jq — Implementation Sequence

> **Run eval after every step.** Don't batch. The probe is the oracle.

## Phase A — Foundation (target: 30-40% pass)

1. **JSON I/O round-trip.**
   Hand-write parser + emitter. Gate: parse + emit a known fixture matches reference jq's output byte-for-byte for objects, arrays, strings (with escapes), numbers (whole / float / scientific), booleans, null. **Do not skip the byte-for-byte gate** — every later test depends on this.

2. **Identity filter `.`** + `-c`, `-r`, `--tab`, `--indent N`, `--sort-keys`, `-j`, `-n`. Gate: `echo '{"b":2,"a":1}' | jq '.'` → identical to reference; `--sort-keys` sorts; `-c` compacts; `-r` on a string drops quotes.

3. **Field access** `.foo`, `.foo.bar`, `.["foo"]`, `.[0]`, `.[-1]`, `.[1:3]`. Gate: array slice including negative indexes.

4. **Pipe `|` and comma `,`**. Gate: `[1,2,3] | .[] | .+1` and `., .` produce duplicated stream.

5. **Recursive descent `..`** and `.[]` on objects/arrays. Gate: `.. | numbers` walks an entire document.

## Phase B — Construction + builtins (target: 65-75%)

6. **Object/array literals** `{a: .b}`, `[.foo]`. Gate: shorthand `{a, b}` works.
7. **Arithmetic** including string concat, array concat, object merge `+`, recursive merge `*`. Gate: `null + 1` → `1`, `null + "x"` → error.
8. **Builtins — Tier 1**: `length`, `keys`, `keys_unsorted`, `values`, `type`, `has`, `in`, `to_entries`, `from_entries`, `with_entries`, `empty`, `not`, `add`, `any`, `all`, `range`. Gate: `range(3)` yields 0,1,2 as separate outputs.
9. **Iteration / map**: `map(f)`, `map_values(f)`, `select(cond)`. Gate: `[1,2,3] | map(.*2)` → `[2,4,6]`.
10. **Sort/group**: `sort`, `sort_by(f)`, `group_by(f)`, `unique`, `unique_by(f)`, `min`, `max`, `min_by`, `max_by`, `reverse`, `flatten`, `flatten(d)`. Gate: `group_by` sorts its result keys.

## Phase C — Strings, regex, paths (target: 80-88%)

11. **String builtins**: `tostring`, `tonumber`, `ascii_downcase`, `ascii_upcase`, `explode`, `implode`, `split`, `join`, `startswith`, `endswith`, `ltrimstr`, `rtrimstr`, `tojson`, `fromjson`. Gate: `explode`/`implode` round-trips on `"héllo"`.
12. **Format strings**: `@text`, `@json`, `@csv`, `@tsv`, `@html`, `@uri`, `@sh`, `@base64`, `@base64d`. Gate: `@csv` on `[1,"a,b",null]` → `1,"a,b",`.
13. **Regex builtins**: `test`, `match`, `capture`, `scan`, `splits`, `sub`, `gsub` — all with optional flags arg. Gate: `match("(a)(b)")` returns `{offset, length, string, captures: [...]}` shape.
14. **Path machinery**: `path(.a.b)`, `paths`, `leaf_paths`, `getpath`, `setpath`, `delpaths`, `del(.a)`. Gate: `path(.a[0])` → `["a", 0]`.
15. **Assignment operators**: `=`, `|=`, `+=`, `-=`, `*=`, `/=`, `//=`. Gate: `(.a, .b) += 1` updates both paths.

## Phase D — Control flow + variables (target: 92-96%)

16. **Variables**: `. as $x | f`, destructuring `[ . as [$a,$b] | $a+$b ]`, `{a, b} as {a:$a,b:$b}`. Gate: shadowing — inner `as` wins.
17. **Function definitions**: `def f: .;`, `def f(g): g|g;`, recursion, arity overloading. Gate: `def f(g): g + g; 5 | f(.+1)` → `12`.
18. **Conditional `if/then/elif/else/end`**. Gate: nested if-elif chain.
19. **`try`/`catch`** and `?` operator. Gate: `try (1/0) catch "no"` → `"no"`.
20. **`reduce`/`foreach`**. Gate: `reduce range(5) as $x (0; . + $x)` → `10`.
21. **Alternative `//`**. Gate: `null // "x"` → `"x"`; `1 // "x"` → `1`; `false // "x"` → `"x"`.

## Phase E — CLI args + edge case sweep (target: 96-99%)

22. **Args plumbing**: `--arg`, `--argjson`, `--args`, `--jsonargs`, `--rawfile`, `-R`, `-s`, `-n`, `-e`, `-a`. Gate: each flag produces its documented effect; combinations don't break.
23. **Multiple inputs / file args**: `jq '.' a.json b.json` reads both; stdin piping with multiple top-level values; `--slurp` collects all.
24. **Exit codes**: 0/2/3/4/5 per spec. Gate: matrix below.

| Scenario | Expected exit |
|----------|---------------|
| Normal success | 0 |
| Filter syntax error | 3 (or 2 in some configs — verify against reference) |
| Input JSON parse error | 2 |
| `-e` and last output was null/false | 1 |
| `-e` and no outputs (`empty`) | 1 |
| `error("msg")` triggered | 5 |

## Phase F — The 90→100% gap

This is where the long tail lives. **Each of these has produced a 1-2% test failure cluster historically:**

1. **Number formatting precision.** `0.1 + 0.2` must emit jq's exact representation, not Python's `0.30000000000000004`. Use a custom formatter that matches reference jq character-for-character.
2. **Whole-number-float emission.** `1.0` → `1`, but `[1.0]` may emit `[1]` or `[1.0]` depending on context. Verify against reference.
3. **Negative zero.** `-0` must round-trip as `-0`, not `0`.
4. **Surrogate handling.** `"😀"` round-trips byte-for-byte.
5. **Recursive merge `*` corner.** `{a: {b: 1}} * {a: 2}` — does the right-side scalar replace the left-side object, or error? (Replaces, in current jq.)
6. **`del` on overlapping paths.** `del(.a, .a.b)` order semantics.
7. **`getpath` on missing.** Returns null, not error.
8. **Stream of zero values.** `empty | f` — `f` is never called; output is empty stream, not null.
9. **`limit(n; f)` arity.** Often missed; `limit(3; range(10))` → 0,1,2.
10. **Sort stability.** jq's sort is stable by spec; verify on `sort_by(.k)` with duplicate keys.
11. **`keys_unsorted` insertion order.** Must match parse order, not sorted.
12. **Error message format.** `jq: error (at <stdin>:N) (file:line): MSG` — exact prefix matters.
13. **`@csv`/`@tsv` quoting rules.** Newlines, double-quotes inside cells.
14. **`@sh` quoting.** Single-quoted with `'\''` escape inside.
15. **`-a` ASCII output.** `é` for `é`, but emoji surrogate pair `😀`.

## Failure-category triage (when stuck at >95%)

When a probe shows N failures clustered, **classify before fixing**:

```
Group A — JSON output formatting differences (whitespace, number precision, escape rules)
Group B — Filter-language semantic deviation (wrong stream content, missing yield)
Group C — Builtin behavior gap (wrong return type, edge case)
Group D — CLI flag plumbing (wrong combination, default mismatch)
Group E — Exit code / stderr format
```

**Fix one group per attempt.** Mixing groups burns Claude-attempts. The agent's `format_failure_report` already groups failures by test name prefix; use that grouping as your trigger.
