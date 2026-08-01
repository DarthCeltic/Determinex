---
name: jq-fuzzing-surface
description: Specific testable behaviors the ProgramBench harness will probe in jq. CLI flags, output format edge cases, filter-language semantics, and exit-code matrix.
type: fuzzing-surface
---

# jq — Fuzzing Attack Surface

The PB pytest suite for jq has 6,796 tests across 12 branches. The branch with 2,976 tests likely exercises the filter language; the 2,219-test branch likely exercises CLI flags + builtins. Below is the surface they will hit.

## CLI flag matrix (every combination matters)

- **Input modes**: stdin (default) | positional file(s) | `-n` (null input) | `--arg X V` | `--argjson X V` | `--args` (positionals as $ARGS.positional) | `--jsonargs` | `--rawfile X path` | `-R`/`--raw-input` (each line/whole stream as string) | `--slurp` (`-s`) (concat into array)
- **Output formats**: default (pretty) | `-c` (compact, single-line per top-level value) | `-j` (no trailing newlines) | `-r` (raw strings, no quotes) | `-a`/`--ascii-output` (`\uXXXX` escape non-ASCII) | `--tab` | `--indent N` | `--sort-keys` (`-S`) | `--rawfile-output` (rare)
- **Behavioral**: `-e` (exit non-zero if last result null/false/empty) | `-C` always color | `-M` no color | `--unbuffered`
- **Combos that test author traps**: `-r -e` (raw + exit code), `-s -n` (slurp with null input — should slurp into a single array), `-c -j` (compact + no newline, should be one line no terminator), `--tab --indent 4` (last wins or error?), `--arg name 1` then `$name` should be the *string* `"1"` not the number `1`.

## Filter-language surface

### Identity / access
- `.`, `.foo`, `.["foo"]`, `.["foo bar"]`, `.foo.bar`, `.foo.bar?`, `.[0]`, `.[-1]`, `.[1:3]`, `.[2:]`, `.[:-1]`
- `.foo // "default"` (alternative — fires on null/false too, NOT on missing-and-error)
- `.foo?` suppresses type errors but propagates value errors
- `..` (recurse) returns *all* values in document including the document itself
- `.[]` — iterate; on object → values, on array → elements, on null/scalar → error (without `?`)

### Construction
- `[1,2,3]` array literal
- `{a: 1, "b c": 2}` object literal — keys are strings always
- `{a, b}` shorthand for `{a: .a, b: .b}` (key with no value)
- `{(.k): .v}` computed key (parens required)
- `{a: 1} + {b: 2}` merges (right wins on conflict)

### Pipes / comma / parens
- `f | g` pipe
- `f, g` comma (concatenated streams)
- `(f | g), h` parenthesized — change associativity
- `f | (g, h)` ≠ `f | g, h` (precedence: `|` binds tightest at top level)

### Arithmetic
- `+`, `-`, `*`, `/`, `%` work on **numbers AND non-numbers** with type-specific semantics:
  - `1 + 2` → 3
  - `"a" + "b"` → `"ab"`
  - `[1] + [2]` → `[1,2]`
  - `{a:1} + {b:2}` → `{a:1,b:2}` (right wins on collision)
  - `{a:1} * {a:{b:2}}` → recursive merge
  - `null + 1` → 1 (null is additive identity for non-string types only)
  - `1 / 0` → error "jq: error (at <stdin>:N): /0"
  - `5 % 2` → 1 (always integer; floats coerced)
- Unary `-` works on numbers only; `-null` errors

### Builtins (every one of these is testable)
**Inspection**: `length`, `utf8bytelength`, `type`, `not`, `keys`, `keys_unsorted`, `values`, `has(k)`, `in(o)`, `contains(x)`, `inside(x)`, `paths`, `leaf_paths`, `paths(filter)`, `to_entries`, `from_entries`, `with_entries(f)`

**Generation**: `range(N)`, `range(from; to)`, `range(from; to; step)`, `empty`, `null`, `true`, `false`

**Iteration / mapping**: `map(f)`, `map_values(f)`, `select(cond)`, `add`, `any`, `all`, `any(f)`, `all(f)`, `any(g; cond)`, `all(g; cond)`, `min`, `max`, `min_by(f)`, `max_by(f)`, `unique`, `unique_by(f)`, `sort`, `sort_by(f)`, `group_by(f)`, `reverse`, `flatten`, `flatten(d)`

**String**: `tostring`, `tonumber`, `ascii_downcase`, `ascii_upcase`, `explode`, `implode`, `split(s)`, `split(re; flags)`, `join(s)`, `ltrimstr(s)`, `rtrimstr(s)`, `startswith(s)`, `endswith(s)`, `tojson`, `fromjson`, `ascii(n)`

**Path**: `path(f)`, `paths`, `getpath(p)`, `setpath(p; v)`, `delpaths(ps)`, `del(f)`

**Reduce / foreach**: `reduce X as $x (init; update)`, `foreach X as $x (init; update; extract)`

**Regex**: `test(re)`, `test(re; flags)`, `match(re)`, `match(re; flags)`, `capture(re)`, `capture(re; flags)`, `scan(re)`, `splits(re)`, `sub(re; str)`, `gsub(re; str)`, `sub(re; str; flags)`, `gsub(re; str; flags)`

**Math**: `floor`, `ceil`, `round`, `sqrt`, `fabs`, `pow(a;b)`, `log`, `log2`, `log10`, `exp`, `exp2`, `exp10`, `sin`/`cos`/`tan` and inverses, `nan`, `isnan`, `isinfinite`, `infinite`

**Format**: `@text`, `@json`, `@csv`, `@tsv`, `@html`, `@uri`, `@sh`, `@base64`, `@base64d`

**Date/time**: `now`, `mktime`, `strftime(fmt)`, `strptime(fmt)`, `fromdateiso8601`, `todateiso8601` — implement; cheap with `datetime.strptime`

**Error/control**: `error`, `error(msg)`, `halt`, `halt_error`, `halt_error(exit_code)`, `try X catch Y`, `X?`

**Environment**: `env`, `$ENV`, `$__loc__`

### Assignment operators (path-based)
- `=`, `|=`, `+=`, `-=`, `*=`, `/=`, `//=`
- LHS must be a path expression (validated by `path()`)
- `(.a, .b) += 1` — assigns to both paths

### Variable bindings
- `. as $x | f` — capture, then continue
- `[1,2] as [$a,$b] | $a + $b` — destructuring (array)
- `{a, b} as {a: $a, b: $b} | $a + $b` — destructuring (object)

### Functions
- `def f: .;` — no args
- `def f(a): a + a;` — call-by-name (NOT call-by-value): `f(.+1)` re-evaluates `.+1` for each use
- `def f(a; b): a + b;` — semicolons (NOT commas)
- Arity overloading: `f`, `f/1`, `f/2` are different functions
- Recursion: `def r(n): if n <= 0 then n else r(n-1) end;` — works
- Closures capture lexical scope

## Output format edge cases (where 90→100% lives)

1. **Number formatting**: `1.0` → `1`, `1.5` → `1.5`, `1e100` → `1e+100`, `0.1` → `0.1` (not `0.10000000000000001`), `-0` → `-0` (preserve sign)
2. **Integer overflow**: `9999999999999999` (16+ digits) — jq promotes to float silently. Test: `.+1` past safe integer.
3. **Surrogate pairs**: `"😀"` — must encode/decode as UTF-8, not as paired surrogates.
4. **Control chars in strings**: `\b \f \n \r \t \" \\ \/` — and `` for everything else < 0x20.
5. **`/` escaping**: jq escapes `/` as `\/` only when `--ascii-output`; default does not. Verify in current ref.
6. **Pretty-print indent**: default 2 spaces. Newlines after `{`, before `}`, after `,` between members. Empty objects `{}`, empty arrays `[]` stay on one line.
7. **Compact `-c`**: one value per line, no internal whitespace.
8. **Raw `-r`**: strings emit without quotes; non-strings still emit JSON. Raw + compact mixes per value.
9. **`-j`**: no trailing newlines between outputs (concatenated); strings still emit JSON unless `-r` is also set.
10. **`--sort-keys`**: alphabetical at every object level. Stable for equal keys (impossible in JSON, but defensive).

## Exit codes

- 0: success
- 2: usage / syntax error in filter or args
- 3: with `-e`: last output was null/false (still success in normal mode)
- 4: with `-e`: no outputs at all (e.g. `empty`)
- 5: parse error in input JSON

`error` builtin → exit 5 (or whatever `halt_error` was given).

## Stderr behavior

- Errors are `jq: error (at <stdin>:N): MSG` — the `(at <file>:N)` part is testable.
- `--seq` mode is unlikely to be hit but if so, prepends `\x1e` per value.

## Testable feature combos likely to surprise

1. `--arg foo 42` — `$foo` is the **string `"42"`**, not the number 42. `--argjson foo 42` makes it a number.
2. `--slurp` with `-r` (raw input) reads whole stream as **single string**, no array.
3. `null | empty` → no output (correct), exit 0.
4. `0 | not` → `true` (in jq, `0` is truthy, `null` and `false` are falsy — Python-different!).
5. `[1,2,3] | .[10]?` → no output (suppresses out-of-range error). `.[10]` without `?` is **null**, NOT an error. (Out-of-range index returns null.)
6. `.foo` on a non-object → error. `.foo?` on a non-object → no output.
7. `.["foo"]` on null → null (NOT error). `.foo` on null → null also. But `.[0]` on null → null.
8. `1 as $x | 2 as $x | $x` → 2 (inner shadows outer).

## What the eval test names tell us

From the SHA `9130f7b96d` branch (16 tests): names like `test_basic_operations`, `test_arithmetic_logic`, `test_advanced_features`, `test_builtin_functions`, `test_corrections` confirm category structure. The 2,976-test branch (`ff26b33afe`) is almost certainly the full filter-language matrix; treat it as the dominant signal.
