---
name: jq-behavioral-spec
description: Empirical build brief for jq, derived from 1,938 CATCHES docstrings + 619 byte-exact golden output files + 96 stderr golden files across 12 ProgramBench test branches. Injected into the builder prompt to drive a one-shot 100% lock.
type: behavioral-spec
---

# jq — Behavioral Build Spec

> **Read order.** Section 1 (binary contract) and Section 5 (pre-flight self-tests) are mandatory. Section 4 is the surface — read in full before writing any code. The golden files are **byte-exact** comparisons; deviations of a single character fail tests. Number-formatting and error-message-format rules are the dominant 90→100% gap.

---

## Section 1 — Binary Contract

The system under test is a single executable at `/workspace/executable`.

| Property | Value |
|---|---|
| Path | `./executable` (relative to the build dir, becomes `/workspace/executable` at test time) |
| Permissions | must be executable (`chmod +x`) |
| Invocation | `executable [FLAGS...] [FILTER] [FILE...]` |
| Stdin | optional — used when no FILE args, or with `--slurp`/`-R`/`-n` |
| Stdout | filter output, format determined by output flags |
| Stderr | error messages only, exact format (see §4.6) |
| Environment vars consumed | `JQ_COLORS`, `JQ_LIBRARY_PATH` |
| Working dir | `/workspace/` at test time |

The test fixture invokes the binary as:

```python
subprocess.run([executable, *args, filter_expr], input=stdin_text, capture_output=True, text=True)
```

`text=True` means stdin/stdout/stderr are decoded as UTF-8. Tests pass JSON data via `input=...` and compare `result.stdout` and `result.stderr` byte-for-byte against golden files.

---

## Section 2 — Test Invocation API

The test fixture (`run_jq` in conftest.py) supports:

| Parameter | Meaning |
|---|---|
| `filter_expr` | The jq program (positional last) |
| `args` | List of additional CLI flags before the filter |
| `input_data` | Python value auto-serialized to JSON for stdin, OR a string |
| `stdin_text` | Raw stdin bytes (overrides `input_data`) |
| `capture_stderr` | If True, returns `(stdout, stderr, returncode)` tuple |
| `check` | If True, raises on non-zero exit |

A second fixture (`run_binary`) calls with arbitrary args list — used when filter position is non-standard or for `-h`/`-V`/`-f` cases.

`env` is sometimes overridden — primarily `JQ_COLORS` for color tests. Tests run with `text=True`, so tests passing `b'...'` bytes use a separate raw-bytes path.

---

## Section 3 — Implementation Constraints

### Language: Python 3.10

- Container has Python 3.10.12 + pip + gcc + cmake + libonig5 (system Oniguruma library, version 6.9.7.1).
- `pip install` works (network is enabled during compile).
- Required deps:
  - `onigurumacffi` — Python binding to libonig. **MUST USE THIS** for regex (not Python's `re`). Python's `re` is not Oniguruma-compatible and will fail ~495 regex tests.

### File layout (multi-file mandatory)

A monolithic `main.py` will hit Claude's output token limit. Split:

```
compile.sh          ← installs deps, makes ./executable
main.py             ← entry point (argparse, dispatch, I/O)
jvalue.py           ← JSON value model + path machinery
json_io.py          ← strict JSON parser + jq-exact emitter
lexer.py            ← jq filter language tokenizer
parser.py           ← recursive-descent → AST
evaluator.py        ← tree-walking generator interpreter
builtins.py         ← every builtin function (largest file)
regex_onig.py       ← onigurumacffi wrapper for test/match/capture/sub/gsub
errors.py           ← error message construction (exact format)
```

`main.py` should `from <module> import ...` the others. Each module should be self-contained and importable.

### compile.sh skeleton

```bash
#!/bin/bash
set -e
pip3 install -q onigurumacffi
chmod +x main.py
ln -sf main.py executable
# Pre-flight smoke test (Section 5) — must pass or compile fails:
echo '{"a":1}' | ./executable . | grep -q '"a": 1' || { echo "smoke failed"; exit 1; }
echo '1' | ./executable -r '"x"' | grep -q '^x$' || { echo "raw smoke failed"; exit 1; }
```

### main.py skeleton

```python
#!/usr/bin/env python3
import sys
sys.dont_write_bytecode = True   # avoid __pycache__ pollution in /workspace
from main_impl import run
sys.exit(run(sys.argv[1:]))
```

Or inline `run` in main.py — but the import shim keeps the script entry small for `chmod +x`.

### Forbidden shortcuts

- ❌ Do not use Python's stdlib `re` for any test/match/capture/sub/gsub builtin. Use `onigurumacffi`.
- ❌ Do not use `json.dumps()` for output — its formatting differs from jq (separators, float format). Hand-write the emitter.
- ❌ Do not use `json.loads()` for input — it accepts `NaN`/`Infinity` (jq does not) and may use float promotion that breaks integer roundtripping. Hand-write the parser.
- ❌ Do not delegate to `/usr/bin/jq` (different version, fails byte-exact golden tests).
- ❌ Do not noop — the test will run against the reference at `/workspace/executable` only if you don't write a new one. We must produce a real implementation for corpus value.

---

## Section 4 — Behavioral Surface

### 4.1 — CLI flags (every flag is testable)

| Flag | Long | Effect |
|---|---|---|
| `-h` | `--help` | print usage to stdout, exit 0, no stderr |
| `-V` | `--version` | print version like `jq-1.7` to stdout, exit 0 |
| `-c` | `--compact-output` | one value per line, no internal whitespace |
| `-r` | `--raw-output` | strings emit without quotes; non-strings still emit JSON |
| `-R` | `--raw-input` | each line of stdin becomes a JSON string value |
| `-s` | `--slurp` | collect all input values into a single array, then run filter |
| `-n` | `--null-input` | use `null` as input (don't read stdin), filter still runs |
| `-j` | `--join-output` | no newlines between outputs (raw concatenation); implies `-r` for strings |
| `-a` | `--ascii-output` | non-ASCII chars escape as `\uXXXX` (surrogate pair for >U+FFFF) |
| `-S` | `--sort-keys` | sort object keys lexicographically at every nesting depth |
| `-C` | `--color-output` | force color even when stdout is not a TTY |
| `-M` | `--monochrome-output` | force no color |
| `-e` | `--exit-status` | exit 1 if last output was null/false/empty, else 0 |
| `--tab` | | indent with tabs instead of spaces |
| `--indent N` | | indent with N spaces (default 2; 0..7 valid) |
| `--unbuffered` | | flush stdout after each output value |
| `--arg NAME VAL` | | bind `$NAME` to the **string** `VAL` (always string, never coerced) |
| `--argjson NAME JSON` | | bind `$NAME` to parsed JSON value |
| `--args` | | remaining positionals → `$ARGS.positional[]` (strings) |
| `--jsonargs` | | remaining positionals → `$ARGS.positional[]` (parsed JSON) |
| `--slurpfile NAME path` | | read whole file as JSON-stream → array → bind to `$NAME` |
| `--rawfile NAME path` | | read whole file as one string → bind to `$NAME` |
| `-f FILE` / `--from-file` | | read filter expression from FILE instead of arg |
| `--seq` | | RFC 7464 — prepend `\x1e` (RS) before each output value |
| `--stream` | | emit `[path, value]` events instead of values |
| `--raw-output0` | | like `-r` but null-separated instead of newline |

**Flag-combination behaviors that ARE tested:**

- `-r -e`: raw output, exit code reflects falsy-last-value.
- `-s -n`: slurp wins; with `--null-input`, `--slurp` slurps an empty array `[]` from stdin and feeds that as input.
- `-c -j`: compact + no-newline → one big concatenated line, no separator.
- `--tab --indent 4`: last wins on the indent setting (`--indent 4` overrides `--tab`).
- `-r` on non-string value: still emits JSON-formatted (only strings drop quotes).
- `-a` on emoji `😀`: outputs `😀` (UTF-16 surrogate pair, lowercase hex).
- `-S` is recursive — sorts keys at every depth, in arrays of objects too.

### 4.2 — JSON parser rules

Hand-write a **strict RFC 8259** parser. Behaviors that ARE tested:

- **Reject** trailing commas in objects and arrays. `[1,2,]` → exit 5, stderr `jq: parse error: Expected another array element at line 1, column 7`.
- **Reject** unquoted keys. `{key: 1}` → parse error.
- **Reject** comments (`//`, `/* */`).
- **Reject** `NaN`, `Infinity`, `-Infinity`, hex literals, octal literals.
- **Reject** unterminated strings, unterminated objects, unterminated arrays.
  - `{` → `Unfinished JSON term at EOF at line 1, column 1`
  - `{"key": }` → `Unmatched '}' at line 1, column 9`
- **Reject** invalid UTF-8 sequences. Stderr must contain `parse error` and `Invalid numeric literal` (jq's specific phrasing for trailing garbage; verify against golden).
- **Accept** escape sequences in strings: `\"`, `\\`, `\/`, `\b`, `\f`, `\n`, `\r`, `\t`, `\uXXXX` (with surrogate pair handling for `😀` → emoji).
- **Accept** integers up to and including beyond 2^53 — jq preserves integers exactly when possible. Test: `9999999999999999` round-trips identically.
- **Accept** numbers with sign, decimal, exponent: `-1.5e+10`, `0.001`, `1E10`, `-0`.
- **Multiple top-level values**: `1 2 3` (whitespace-separated) is valid input — three top-level values.
- **No surrogate-pair fragments**: a lone `\uD800` without paired low surrogate is rejected (jq emits `parse error` mentioning invalid escape).

Position reporting: line and column are 1-based for both. **Column is 1-based and points at the offending character or position.**

Exit code on JSON parse error: **5**. Stderr is exactly `jq: parse error: <message>` followed by a single newline.

### 4.3 — JSON printer rules (byte-exact)

#### Pretty (default)
- Indent: **2 spaces** per level (no tabs unless `--tab`).
- `{` on its own line **only when** the object has at least one key. Empty `{}` and `[]` stay on one line.
- After `{`: newline + indent.
- Each key: `"key": value` with **one space** after `:`.
- Members separated by `,` followed by newline + indent.
- Closing `}`: newline + outdent + `}`.
- Same rules for arrays.
- One value per top-level output, **followed by a single trailing newline `\n`**.

Example (`echo '{"a":1,"b":2}' | jq .`):
```
{
  "a": 1,
  "b": 2
}
```
Exact bytes: `{\n  "a": 1,\n  "b": 2\n}\n`.

#### Compact (`-c`)
- No whitespace except: one space after `:` is **NOT** present (in jq compact mode, no space after `:`); separator after `,` is no whitespace.
- One value per line (newline after each top-level output).

Example: `{"a":1,"b":2}\n`.

#### Raw (`-r`)
- For string values: emit the string content directly with all escapes interpreted (no surrounding quotes), followed by `\n`.
- For non-string values: emit JSON-formatted (same as default), followed by `\n`.
- `\n` and `\t` inside strings are literal newlines/tabs in output.

Example (`echo '"hello\nworld"' | jq -r .`):
```
hello
world
```
Bytes: `hello\nworld\n`.

#### Join (`-j`)
- Suppresses **all** trailing newlines between and after outputs.
- Strings emit raw content (like `-r`), non-strings emit JSON.
- No `-j` separator at all — pure concatenation.

Example (`echo '"test"' | jq -j .`): bytes are exactly `test` (4 bytes, no newline).

#### ASCII (`-a`)
- Non-ASCII characters in strings escape as `\uXXXX` (lowercase hex digits).
- Code points above U+FFFF emit as **UTF-16 surrogate pairs**: `😀` (U+1F600) → `😀`.
- Output STILL has surrounding JSON quotes for strings (it's still JSON, just ASCII-safe).

Example (`echo '"Café ☕"' | jq -a .`):
```
"Café ☕"
```

#### Sort keys (`-S`)
- Sort object keys lexicographically (Unicode codepoint order).
- Recursive: nested objects also have keys sorted.
- Arrays of objects: each object's keys sorted, but array order preserved.

#### Tab indent (`--tab`)
- Replace 2-space indent with single-tab indent at each depth level.

#### Indent N (`--indent N`)
- N must be 0..7. `--indent 0` produces no indentation but still has newlines.
- `--indent 0` ≠ `-c` (compact has no newlines either).

### 4.4 — Number formatting (the 90→100% trap)

This is where most implementations leak tests. Behaviors that ARE tested:

- **Integers stay integers**: `1` → `1`, `1.0` → `1` (whole-number float coerces in output), `100000000000000` (within safe int range) → `100000000000000`.
- **Floats show fractional part**: `1.5` → `1.5`, `0.1` → `0.1` (NOT `0.10000000000000001`).
- **Scientific notation**: very large or very small floats use `e+`/`e-` (with sign even for positive exponent). Example: `1e100` → `1e+100`, NOT `1e100`.
- **Negative zero**: `-0` → `-0`. The sign is preserved.
- **NaN / Infinity**: jq emits `null` for these (NaN is **not** valid JSON). `1e1000` (overflow) → `null`.
- **Integer division by zero**: `1/0` → runtime error, exit 5. NOT `Infinity`.
- **Modulo by zero**: `5 % 0` → runtime error, exit 5.
- **Modulo coerces to integer**: `5.7 % 2` → integer remainder (truncate, not modulo on floats).
- **Float precision**: jq uses jvp_dtoa (Steele-White / Grisu) for float printing. **Use Python's `repr(float)`** as a starting point — it's correct for most cases, but verify by sampling against the reference. For exact match, prefer manual formatting that matches jq's output.

Concrete rule for emitting a Python `int | float`:

```python
def emit_num(x):
    if isinstance(x, bool):       # bool is int subclass — guard first
        return "true" if x else "false"
    if isinstance(x, int):
        return str(x)
    if math.isnan(x) or math.isinf(x):
        return "null"
    if x.is_integer() and -1e16 < x < 1e16:
        return str(int(x))        # 1.0 → "1"
    # Use Python's repr — matches jq for most floats
    s = repr(x)
    # Normalize scientific notation: ensure '+' for positive exponent
    if 'e' in s and 'e+' not in s and 'e-' not in s:
        s = s.replace('e', 'e+')
    return s
```

### 4.5 — Filter language (lexer/parser)

#### Tokens
- Identifiers: `[A-Za-z_][A-Za-z0-9_]*` followed by optional `::` for namespacing.
- Numbers: same as JSON numbers (with sign, decimal, exponent).
- Strings: `"..."` with same escapes as JSON. **Plus** string interpolation `\(expr)` inside strings.
- Punctuation: `. , ; : | ( ) [ ] { } ? // ?// = == != < <= > >= |= += -= *= /= %= //= - + * / % @`
- Keywords: `def`, `if`, `then`, `elif`, `else`, `end`, `as`, `and`, `or`, `not`, `try`, `catch`, `reduce`, `foreach`, `import`, `include`, `module`, `null`, `true`, `false`, `__loc__`, `label`.
- Format strings: `@text @json @csv @tsv @html @uri @sh @base64 @base64d`.
- Variables: `$name`.
- Recursive descent: `..`.
- Field access: `.foo`, `.["foo"]`.

#### Grammar (recursive-descent)
Operator precedence, low to high (matches `jq` reference):
1. `|` (pipe — sequencing)
2. `,` (comma — concat streams)
3. `=`, `|=`, `+=`, `-=`, `*=`, `/=`, `%=`, `//=` (assignments — RIGHT associative)
4. `or`
5. `and`
6. `==`, `!=`, `<`, `<=`, `>`, `>=`
7. `//` (alternative — short-circuits on null/false)
8. `+`, `-` (arithmetic)
9. `*`, `/`, `%` (arithmetic)
10. unary `-`
11. `try`/`catch`, `?` (postfix error suppression)
12. function application (calls)
13. `as $x` binding
14. `.` field access, `.[]` iterate, `.[k]` index, `.[a:b]` slice

#### Common syntax
- `def f: BODY;` — no-arg function
- `def f(g): BODY;` — call-by-name (g is re-evaluated each use, NOT pre-evaluated)
- `def f(a; b): BODY;` — semicolon-separated args (NOT comma)
- Arity overload: `f`, `f/1`, `f/2` are distinct functions.
- `. as $x | BODY` — variable binding
- `. as [$a, $b] | BODY` — array destructuring
- `. as {a, b} | BODY` — object destructuring (shorthand: `{a: $a, b: $b}`)
- `. as {a: $x, b: $y} | BODY` — object destructuring (full form)
- `if cond then A elif cond2 then B else C end` — note `end`
- `try EXPR catch HANDLER` — handler receives error message string
- `EXPR?` — equivalent to `try EXPR catch empty`
- `reduce GEN as $x (INIT; UPDATE)` — left fold over generator
- `foreach GEN as $x (INIT; UPDATE; EXTRACT)` — like reduce but emits intermediate values
- `label $out | BODY` + `, break $out` — non-local exit
- `import "module" as NAME ;` — module imports (rarely tested but exists)

#### String interpolation
```
"hello \(.name) you are \(.age) years old"
```
Inside a `"..."` literal, `\(EXPR)` evaluates EXPR with the current input as input, formats result as a string (numbers via num-to-string, strings as-is, others via tojson).

#### Filter syntax errors
- Format: `jq: error: syntax error, <expected> at <top-level>, line N, column M:\n    <source-line>\n        ^\njq: 1 compile error\n`
- Note the leading 4 spaces on the source line and on the caret line.
- Caret position (column) is 1-based, points at the offending token.
- Exit code: **3**.

### 4.6 — Filter evaluation semantics (the engine)

Every filter is a function `JqValue → Iterator[JqValue]`. The engine yields zero or more values. **Backtracking is implicit via Python generators.**

#### Core combinators

```python
def eval_pipe(a, b, ctx, val):
    for av in eval_filter(a, ctx, val):
        yield from eval_filter(b, ctx, av)

def eval_comma(a, b, ctx, val):
    yield from eval_filter(a, ctx, val)
    yield from eval_filter(b, ctx, val)

def eval_array_construct(elem, ctx, val):
    yield list(eval_filter(elem, ctx, val))

def eval_object_construct(pairs, ctx, val):
    # cross-product of all key/value emit streams
    for combo in cartesian(pairs, ctx, val):
        yield dict(combo)
```

#### Identity, field, index
- `.` → emit input
- `.foo` → if input is object: emit `input["foo"]` if present, else `null`. If input is `null`: emit `null` (no error). Else: type error.
- `.foo?` → suppress type errors (still emit `null` for missing on object/null).
- `.[0]` → array index, supports negative. Out-of-range → `null` (NOT error).
- `.["foo"]` → equivalent to `.foo`.
- `.[1:3]` → slice. Supports negative indices, defaults: `.[:-1]`, `.[2:]`.
- `.[]` → iterate. Object → values, array → elements, null/scalar → error (suppress with `?`).
- `..` → recurse: emit input, then all sub-values recursively (depth-first, pre-order).
- `.foo.bar` → chain: if `.foo` is null, `null.bar` → null.

#### Path expressions
For assignment operators, the LHS must be a "path expression": only `.foo`, `.[index]`, `.[]`, sub-paths thereof. `path(EXPR)` returns the path as an array `["foo", 0, "bar"]`.

#### Truthiness
- Falsy: `null`, `false`. Everything else (including `0`, `""`, `[]`, `{}`) is truthy.

#### Equality
- `==`, `!=`: structural equality. Numbers compare numerically (`1 == 1.0` → true).

#### Order
- `<`, `<=`, `>`, `>=`: jq's total order is `null < false < true < numbers < strings < arrays < objects`.
- Within numbers: numerical order.
- Within strings: byte-wise (NOT locale).
- Within arrays: lexicographic.
- Within objects: keys sorted then compared.

#### Arithmetic + - * / %
- `+`: number+number=add, string+string=concat, array+array=concat (preserving order), object+object=merge (right wins on key collision), `null + X` = X (null is identity for non-string side).
- `-`: number-number=sub, array-array=set difference (keep elements from left not in right).
- `*`: number*number=multiply, string*number=repeat (`"ab"*3` → `"ababab"`), object*object=**recursive merge** (deep), null*X = null.
- `/`: number/number=divide, string/string=split (`"a,b,c"/","` → `["a","b","c"]`).
- `%`: integer remainder, both args coerce to int.
- Type mismatch → runtime error: `jq: error (at <stdin>:LINE): <typeA> (<value>) and <typeB> (<value>) cannot be added`.

#### Logical
- `and`: short-circuits.
- `or`: short-circuits.
- `not` is a **filter** (postfix-applied via pipe): `false | not` → `true`. NOT a unary operator.

#### Alternative `//`
- `A // B`: emit each value of A that is **not null and not false**; if A emits no such value, emit each of B.
- Common idiom: `.foo // "default"`.

### 4.7 — Builtin functions (compact reference table)

> Every builtin is testable. Where an arity-overloaded name (e.g. `range`, `range/2`) exists, **all arities** are tested.

#### Inspection
| Name | Behavior |
|---|---|
| `length` | array→count, string→character count (NOT byte count), object→key count, null→0, number→absolute value |
| `utf8bytelength` | string byte count (UTF-8 encoded) |
| `type` | one of `"null" "boolean" "number" "string" "array" "object"` |
| `keys` | object → sorted array of keys (alphabetical); array → 0..N-1 |
| `keys_unsorted` | object → keys in insertion order |
| `values` | object → array of values; array → input unchanged |
| `has(key)` | object: key in keys?; array: index in range? |
| `in(container)` | inverse of `has`: input is a key of container |
| `contains(x)` | recursive containment: numbers equal, strings substring, arrays subset (order-irrelevant), objects sub-keys+sub-values |
| `inside(x)` | inverse: input is contained in x |
| `to_entries` | object → `[{key:..., value:...}]` |
| `from_entries` | array of `{key,value}` (or `{name,value}`, or `{k,v}`) → object |
| `with_entries(f)` | `to_entries | map(f) | from_entries` |
| `paths` | all paths to non-null values |
| `paths(f)` | all paths where the value at the path satisfies `f` |
| `leaf_paths` | paths to scalars only |
| `getpath(p)` | navigate path array `p`; missing → null |
| `setpath(p; v)` | return input with path `p` set to `v` |
| `delpaths(ps)` | input with each path in `ps` deleted |
| `del(f)` | input with everything matched by `f` deleted |

#### Generation
| Name | Behavior |
|---|---|
| `range(N)` | 0,1,...,N-1 (one value per yield, multi-output) |
| `range(from; to)` | from,from+1,...,to-1 |
| `range(from; to; step)` | step-incrementing; supports negative step |
| `empty` | yield nothing |
| `null`, `true`, `false` | constants |
| `repeat(f)` | infinite stream — used with `limit` |
| `recurse(f)` | apply f repeatedly until error (or null in 1-arg form) |
| `recurse` | shorthand for `recurse(.[]?)` — emits self + all descendants |
| `recurse(f; cond)` | apply while `cond` holds |
| `walk(f)` | post-order traversal applying f at each node |

#### Iteration / mapping / filtering
| Name | Behavior |
|---|---|
| `map(f)` | array → `[.[] | f]` |
| `map_values(f)` | object → object with values transformed |
| `select(cond)` | yield input only if cond is truthy |
| `add` | array → reduce with `+`; null on empty array |
| `any`, `all` | array → boolean; arity-2 forms `any(f)`, `all(f)`, `any(g; cond)`, `all(g; cond)` |
| `min`, `max` | array → null on empty, else extreme element |
| `min_by(f)`, `max_by(f)` | extreme by f-applied projection |
| `unique` | sort + dedup |
| `unique_by(f)` | unique by f-projection |
| `sort` | stable sort by jq total order |
| `sort_by(f)` | stable sort by f-projection |
| `group_by(f)` | sort by f then group consecutive equals |
| `reverse` | array reversed; string reversed |
| `flatten` | unlimited depth |
| `flatten(d)` | up to depth d |
| `first`, `last` | array → first/last element; or generator → first/last yielded |
| `first(f)`, `last(f)` | first/last yielded by f |
| `nth(n)`, `nth(n; f)` | n-th value (0-indexed) |
| `limit(n; f)` | first n values from f |
| `until(cond; update)` | iterate update while cond is false |
| `combinations` | list of lists → all cross-product combinations |
| `combinations(n)` | n-length combinations of input array |
| `transpose` | array of arrays → swap rows/cols |

#### Strings
| Name | Behavior |
|---|---|
| `tostring` | `null|true|false|number|string|array|object → "..."` (object/array → JSON encoded) |
| `tonumber` | string → parsed number; non-numeric string → error |
| `ascii_downcase`, `ascii_upcase` | only ASCII A-Z ↔ a-z |
| `explode` | string → array of codepoints (integers) |
| `implode` | array of codepoints → string |
| `split(s)` | by literal string |
| `split(re; flags)` | by regex (Oniguruma) |
| `splits(re)`, `splits(re; flags)` | generator version |
| `join(s)` | array of strings joined by separator |
| `ascii(N)` | integer → 1-char string |
| `ltrimstr(s)`, `rtrimstr(s)` | strip prefix/suffix once if present, else input unchanged |
| `startswith(s)`, `endswith(s)` | boolean |
| `tojson`, `fromjson` | string ↔ value (JSON encode/decode) |
| `@text @json @csv @tsv @html @uri @sh @base64 @base64d` | format strings |
| `ascii` (no arg) | NOT a builtin; arity-error |
| `ltrimstr`, `rtrimstr` on non-string input | identity (return input) |

Format-string semantics:
- `@text`: same as `tostring` for strings, JSON for non-strings.
- `@json`: JSON-encode the input.
- `@csv`: array → comma-separated, fields quoted with `"..."`, internal `"` doubled. Strings only — non-strings: error or coerce per jq.
- `@tsv`: array → tab-separated; tabs/newlines/backslashes inside fields escaped (`\t`, `\n`, `\\`).
- `@html`: HTML-escape `&<>'"` → entities.
- `@uri`: percent-encode reserved chars.
- `@sh`: array → space-separated POSIX-shell-quoted, single-quoted with `'\''` escaping.
- `@base64`: encode (UTF-8 bytes → base64).
- `@base64d`: decode.

Format-string-with-interpolation: `@uri "\(.q)"` — interpolation values pass through the format encoder.

#### Regex (Oniguruma — use onigurumacffi)

| Name | Behavior |
|---|---|
| `test(re)` | boolean |
| `test(re; flags)` | flags string `"gimsxn"` etc. |
| `match(re)` | object `{offset, length, string, captures: [...]}` |
| `match(re; flags)` | with flags |
| `capture(re)` | named captures → object |
| `capture(re; flags)` | |
| `scan(re)` | generator of all matches (string or array of capture group strings if there are groups) |
| `splits(re)` | inverse of `scan` (the unmatched between-pieces) |
| `sub(re; replacement)` | first match replacement; replacement supports `\(g)` for group |
| `sub(re; r; flags)` | with flags |
| `gsub(re; replacement)`, `gsub(re; r; flags)` | global |

Replacement strings inside `sub`/`gsub` have **jq-specific semantics**: `\(.captures.NAME)` to reference named groups, plus jq filter syntax inside parens. Keep this exact.

Regex flags:
- `g` — global (only meaningful on `sub`/`gsub`/`scan`)
- `i` — case-insensitive
- `m` — multiline (`^`/`$` match line boundaries)
- `s` — dotall (`.` matches newlines)
- `x` — ignore whitespace + comments in pattern
- `n` — never-utf8 (rare)
- `p` — `s` and `x` combined

Use onigurumacffi:
```python
import onigurumacffi
def compile_re(pattern, flags=""):
    opts = onigurumacffi.OnigOption.NONE
    if "i" in flags: opts |= onigurumacffi.OnigOption.IGNORECASE
    if "m" in flags: opts |= onigurumacffi.OnigOption.MULTILINE
    if "s" in flags: opts |= onigurumacffi.OnigOption.SINGLELINE
    if "x" in flags: opts |= onigurumacffi.OnigOption.EXTEND
    return onigurumacffi.compile(pattern, opts)
```

#### Math
| Name | Behavior |
|---|---|
| `floor`, `ceil`, `round` | rounding |
| `sqrt`, `cbrt` | roots |
| `pow(x; y)` | `x^y` |
| `log`, `log2`, `log10`, `logb` | logarithms |
| `exp`, `exp2`, `exp10` | exponentials |
| `sin cos tan asin acos atan atan2 sinh cosh tanh asinh acosh atanh` | trig |
| `fabs` | absolute value |
| `nan`, `infinite` | constants |
| `isnan`, `isinfinite`, `isnormal` | predicates |
| `frexp`, `ldexp`, `scalb`, `scalbln` | bit-level |
| `trunc`, `significand`, `j0` `j1` `y0` `y1` `gamma` `tgamma` `lgamma` `lgamma_r` | uncommon but tested |

#### Date / time
| Name | Behavior |
|---|---|
| `now` | current Unix timestamp (float seconds) |
| `strftime(fmt)` | input is `[Y,M,D,H,M,S,WDAY,YDAY]` (broken-down UTC) → formatted string |
| `strptime(fmt)` | string → broken-down UTC |
| `mktime` | broken-down → Unix seconds |
| `gmtime` | seconds → broken-down |
| `localtime` | seconds → broken-down (local TZ) |
| `date`, `dateadd(n)`, `datesub(n)` | ISO 8601 helpers |
| `fromdate`, `fromdateiso8601` | ISO string → seconds |
| `todate`, `todateiso8601` | seconds → ISO string |

#### Control / flow
| Name | Behavior |
|---|---|
| `error(msg)` | raise error with msg |
| `error` (no arg) | raise with input as msg |
| `halt` | exit 0 immediately |
| `halt_error` | print input to stderr, exit nonzero |
| `halt_error(N)` | exit code N |
| `__loc__` | object `{file, line}` for current source location |
| `input` | read next JSON value from stdin (in `-n` mode useful) |
| `inputs` | generator: yields every remaining stdin value |
| `debug` | print input to stderr as `["DEBUG:", VALUE]`, then yield input |
| `debug(msg)` | with custom message |
| `stderr` | print input to stderr (no formatting), yield input |
| `splits(re)`, `getpath(p)`, etc. | already covered |

#### Path-aware
| Name | Behavior |
|---|---|
| `path(f)` | apply f, return the path traversed (only valid for path expressions) |
| `paths`, `paths(f)`, `leaf_paths` | already covered |
| `getpath(path)` | already covered |
| `setpath(path; value)` | already covered |
| `delpaths(paths)` | already covered |
| `del(f)` | already covered |

#### Module / introspection
| Name | Behavior |
|---|---|
| `env` | environment as object |
| `$ENV` | same |
| `builtins` | array of builtin names |
| `input_filename` | name of current input file |
| `input_line_number` | line number for `-R` |
| `getpath` etc. | already covered |

### 4.8 — Error message format (byte-exact)

There are **three error categories**, each with a strict format:

#### Filter syntax errors (compile errors) — exit 3
```
jq: error: syntax error, <description> at <top-level>, line N, column M:
    <source line>
        ^
jq: 1 compile error
```
- Both lines indented with 4 spaces.
- The caret `^` aligns to column M (4 spaces + (M-1) spaces + `^`).
- `<description>` is jq-specific phrasing like `unexpected end of file, expecting FORMAT or QQSTRING_START or '['`.
- Always trailing newline after `compile error`.

#### JSON parse errors — exit 5
```
jq: parse error: <reason> at line N, column M
```
- Single line, terminated with `\n`.
- Reasons (verbatim):
  - `Unfinished JSON term at EOF`
  - `Expected another array element`
  - `Expected another object key-value pair`
  - `Unmatched '<char>'` (e.g. `'}'`)
  - `Invalid numeric literal`
  - `Invalid string`
  - `Unexpected character: '<c>'`

#### Runtime errors — exit 5
```
jq: error (at <FILE>:LINE): <message>
```
- `<FILE>` is `<stdin>` when reading from stdin, else the file path.
- `LINE` is the line number of the input value (zero-indexed for stdin: first value at `<stdin>:0`, but golden samples show `<stdin>:0` even when there's just one input — verify exact behavior).
- Common runtime messages:
  - `<TYPE> (<repr>) and <TYPE> (<repr>) cannot be added`
  - `<TYPE> (<repr>) and <TYPE> (<repr>) cannot be divided because the divisor is zero`
  - `<TYPE> (<repr>) and <TYPE> (<repr>) cannot be divided (remainder) because the divisor is zero`
  - `Cannot iterate over <TYPE> (<repr>)`
  - `Cannot index <TYPE> with <TYPE>`
  - `<TYPE> (<repr>) has no keys`
  - `Cannot index array with string "..."`
  - `Cannot index object with number`
- `<TYPE>` is lowercase: `null`, `boolean`, `number`, `string`, `array`, `object`.
- `<repr>` is the JSON-stringified value, parenthesized.

#### Common arity / undefined errors — exit 3
```
jq: error: <name>/<arity> is not defined at <top-level>, line N, column M:
    <source>
       ^
jq: 1 compile error
```

### 4.9 — Exit code matrix

| Code | Meaning |
|---|---|
| 0 | success (default) |
| 1 | with `-e`: last output was null/false (or there were no outputs) |
| 2 | usage error (invalid CLI flag, missing required arg) |
| 3 | filter compile error (syntax error in jq filter) |
| 4 | (rare — sometimes used for `-e` empty-output, sometimes 1) |
| 5 | JSON parse error in input, OR runtime error during evaluation |

When in doubt, prefer exit 5 for runtime errors, exit 3 for compile errors, exit 1 for `-e` falsy.

### 4.10 — Variables / args

- `--arg NAME VALUE`: bind `$NAME = "VALUE"` (string literal, NEVER number).
- `--argjson NAME JSON`: bind `$NAME` to the parsed JSON value.
- `--args FOO BAR ...`: positionals after `--args` become `$ARGS.positional[0]`, `$ARGS.positional[1]`, ... (strings).
- `--jsonargs ...`: same but each positional is parsed JSON.
- `$ARGS.named` is an object of named bindings.
- `$ENV` is the environment as an object.
- `env` is the same builtin form.
- `$__loc__` returns `{file: "<top-level>", line: N}` at the current source location.

### 4.11 — Module loading (`import`/`include`)

Less commonly tested but exists:
- `import "name" as $alias` — import a module's filter as `$alias::FUNC`.
- `include "name"` — splice all definitions into current scope.
- Module search path: `$JQ_LIBRARY_PATH:$XDG_CONFIG_HOME/jq:$HOME/.jq`.
- Module file: `name.jq` or `name/name.jq`.
- Module metadata: `module {name: "...", description: "..."};` at top of file.

### 4.12 — Streaming mode (`--stream`)

Tested in stream-related branches. Emits `[path, value]` pairs:
- `{"a": [1,2]}` with `--stream` produces:
  ```
  [["a",0],1]
  [["a",1],2]
  [["a",1]]      // close array marker
  [["a"]]        // close object marker
  ```
- Open markers are `[path, value]`; close markers are `[path]` (no value).
- The reverse: `fromstream` rebuilds a value from a stream.
- `truncate_stream(d)` drops outermost d levels from paths.

### 4.13 — File I/O (`-R`, `--rawfile`, `--slurpfile`, `-f`)

- `-R` (raw input): each line of stdin → string value (line-by-line generator). With `-s -R`, all of stdin → single string.
- `--rawfile NAME PATH`: read entire file as string → bind to `$NAME`.
- `--slurpfile NAME PATH`: read file as JSON-stream of values → array → bind to `$NAME`.
- `-f FILE`: read filter expression from FILE (instead of as positional).
- `--`: end of options marker (everything after is positional).

### 4.14 — Color output (`-C`, `JQ_COLORS`)

- `-C` forces ANSI colors even when stdout is not a TTY.
- `JQ_COLORS` env var is a colon-separated list of color codes for: `null:false:true:numbers:strings:arrays:objects:object_keys`.
- Default: `1;30:0;39:0;39:0;39:0;32:1;39:1;39:34;1`.
- Empty `JQ_COLORS` falls back to default (does NOT disable color).
- Colors wrap output via `\x1b[Nm...\x1b[0m`.
- `-M` overrides `-C`.

### 4.15 — Standard library (recursive functions defined in jq itself)

Reference jq has a builtin.jq file with definitions for: `add`, `any`, `all`, `select`, `recurse`, `walk`, `range`, `to_entries`, `from_entries`, `with_entries`, `paths`, `leaf_paths`, `flatten`, `unique`, `unique_by`, `group_by`, `min_by`, `max_by`, `index`, `indices`, `rindex`, `splits`, `tojson`, `fromjson`, `truncate_stream`, `fromstream`, `tostream`, `gsub`, `sub`, `ascii`, `tonumber`, `tostring`, etc.

For our Python impl: implement these as Python functions in `builtins.py`; do NOT need to parse a builtin.jq file. Simpler and faster.

---

## Section 5 — Pre-flight Self-Tests (compile.sh smoke tests)

The compile.sh **must** end with smoke tests that exit non-zero if the binary doesn't behave correctly. This catches "compiles but doesn't work" before paying for a full pytest probe.

**Critical: every smoke failure MUST surface the actual stdout/stderr** so the next-attempt prior_error has diagnostic value. Do NOT use `> /dev/null 2>&1`.

```bash
#!/bin/bash
set -e

# 1. install deps
pip3 install -q onigurumacffi 2>&1 | tail -3

# 2. produce ./executable
chmod +x main.py
ln -sf main.py executable
chmod +x executable

# Diagnostic helper — used by every smoke test
EXEC=./executable
fail_smoke() {
    local name="$1"; shift
    echo "================================"
    echo "SMOKE FAIL: $name"
    echo "INPUT: $LAST_INPUT"
    echo "ARGS: $LAST_ARGS"
    echo "EXIT: $LAST_RC"
    echo "STDOUT:"
    cat /tmp/t.out 2>/dev/null | head -40
    echo "STDERR:"
    cat /tmp/t.err 2>/dev/null | head -40
    echo "EXPECTED:"
    echo "$1"
    echo "================================"
    exit 1
}
run_smoke() {
    LAST_INPUT="$1"; LAST_ARGS="$2"
    if [ -z "$LAST_INPUT" ]; then
        $EXEC $LAST_ARGS > /tmp/t.out 2> /tmp/t.err
    else
        printf '%s' "$LAST_INPUT" | $EXEC $LAST_ARGS > /tmp/t.out 2> /tmp/t.err
    fi
    LAST_RC=$?
}

# 3. smoke tests

# Help (must exit 0)
run_smoke "" "-h"
[ "$LAST_RC" = "0" ] || fail_smoke "-h returned $LAST_RC" "exit 0"

# Identity, default pretty
run_smoke '{"a":1,"b":2}' '.'
EXPECTED=$(printf '{\n  "a": 1,\n  "b": 2\n}\n')
[ "$(cat /tmp/t.out)" = "$EXPECTED" ] || fail_smoke "pretty default" "$EXPECTED"

# Compact
run_smoke '{"a":1}' '-c .'
EXPECTED=$(printf '{"a":1}')   # trailing newline added by jq
[ "$(cat /tmp/t.out)" = "$EXPECTED" ] || fail_smoke "compact -c" "$EXPECTED"

# Raw output
run_smoke '"hello"' '-r .'
[ "$(cat /tmp/t.out)" = "hello" ] || fail_smoke "raw -r" "hello"

# Sort keys
run_smoke '{"z":3,"a":1,"m":2}' '-S .'
EXPECTED=$(printf '{\n  "a": 1,\n  "m": 2,\n  "z": 3\n}\n')
[ "$(cat /tmp/t.out)" = "$EXPECTED" ] || fail_smoke "sort keys -S" "$EXPECTED"

# Pipe + iterate
run_smoke '[1,2,3]' '.[]'
EXPECTED=$(printf '1\n2\n3\n')
[ "$(cat /tmp/t.out)" = "$EXPECTED" ] || fail_smoke "iterate .[]" "$EXPECTED"

# Number formatting (1.0 → 1)
run_smoke '1.0' '.'
[ "$(cat /tmp/t.out)" = "1" ] || fail_smoke "1.0 → 1 number formatting" "1"

# JSON parse error → exit 5
run_smoke '{' '.'
[ "$LAST_RC" = "5" ] || fail_smoke "JSON parse error exit code (got $LAST_RC, want 5)" "exit 5"
grep -q "parse error" /tmp/t.err || fail_smoke "JSON parse error stderr (no 'parse error' phrase)" "stderr contains 'parse error'"

# Runtime error → exit 5 (iterate over null)
run_smoke 'null' '.[]'
[ "$LAST_RC" = "5" ] || fail_smoke "Runtime error exit code (got $LAST_RC, want 5)" "exit 5"

# Filter syntax error → exit 3
run_smoke '1' '.foo.'
[ "$LAST_RC" = "3" ] || fail_smoke "Compile error exit code (got $LAST_RC, want 3)" "exit 3"
grep -q "compile error" /tmp/t.err || fail_smoke "Compile error stderr ('compile error' phrase missing)" "stderr contains 'compile error'"

# Regex via onigurumacffi
run_smoke '"hello"' 'test("ell")'
[ "$(cat /tmp/t.out)" = "true" ] || fail_smoke "regex test() — proves onigurumacffi loaded" "true"

# String concat
run_smoke '"a"' '. + "b"'
[ "$(cat /tmp/t.out)" = '"ab"' ] || fail_smoke "string concat with +" '"ab"'

# Reduce
run_smoke '' '-n reduce range(5) as $x (0; . + $x)'
[ "$(cat /tmp/t.out)" = "10" ] || fail_smoke "reduce 0..4 → 10" "10"

# Builtin: keys (sorted)
run_smoke '{"b":2,"a":1}' 'keys'
EXPECTED=$(printf '[\n  "a",\n  "b"\n]\n')
[ "$(cat /tmp/t.out)" = "$EXPECTED" ] || fail_smoke "keys returns sorted array" "$EXPECTED"

echo "All smoke tests passed."
exit 0
```

**The smoke set covers**: help flag, I/O modes (default, compact, raw), sort, iterate, number formatting, all three error categories, regex (proves onigurumacffi loaded + jq filter `test()` wired), arithmetic on strings, reduce, builtins. If all 14 smoke tests pass, the implementation has the major patterns right and the pytest probe is worth running.

**If a smoke test fails**, the `fail_smoke` helper prints input, args, exit code, full stdout, full stderr, and expected output. This is what the next attempt's prior_error sees — make sure your implementation surfaces the actual exception traceback to stderr (don't swallow ImportErrors silently). If the binary fails on `-h` with no diagnostic, it's almost always a missing import or a syntax error in a sibling module.

---

## Section 6 — Common Failure Modes

These are negated CATCHES — wrong-implementation patterns that recur across categories:

1. **Number formatting**: emitting `1.0` instead of `1`; emitting `1e100` instead of `1e+100`; using Python's `json.dumps` (loses `1.0` → `1` distinction); not preserving negative zero `-0`.
2. **Sort stability**: `sort_by` not being stable when projection ties; `group_by` not preserving array order within groups.
3. **Error message format**: wrong line/column (1-based vs 0-based), missing `at <stdin>:0`, wrong type name (`integer` instead of `number`), missing parens around values.
4. **Path semantics**: `getpath` returning error instead of null on missing; `setpath` replacing entire object instead of just the leaf; `del` not shifting array elements after deletion.
5. **`null` arithmetic**: `null + X` should be `X` for non-string X; `null + "s"` is error.
6. **String coercion**: `--arg name 1` should bind to **string** `"1"`, not number `1`.
7. **Builtin arity overload**: `range`, `min_by`, `paths` all have multi-arity forms — implementing only one fails the others.
8. **Filter language semantics**: `f, g` is comma not pipe; `def f(g): g | g; 5 | f(.+1)` evaluates `.+1` twice (call-by-name); `if A then B end` (no `else`) returns input on false.
9. **Pipe + comma precedence**: `f | g, h` parses as `f | (g, h)`, not `(f | g), h`.
10. **`@csv`/`@tsv` quoting**: not doubling internal `"` for CSV; not escaping `\t` `\n` for TSV.
11. **Number-to-string in output**: `tostring` on object → `"{\"a\":1}"` (compact JSON), NOT `"[object Object]"`.
12. **Slice out-of-range**: jq returns `null` for `.[10]` on a 3-element array, NOT error. With `?` also valid.
13. **`.foo` on null**: returns `null` (not error). With `?` also returns `null`.
14. **`-r` only affects strings**: non-string values still emit JSON.
15. **`-S` is recursive**: must sort keys at every depth, not just top level.
16. **Regex Oniguruma compatibility**: Python `re` does not match jq's regex semantics (named groups syntax differs `(?<name>...)` vs `(?P<name>...)`, character classes differ, lookbehind support differs). MUST use libonig.
17. **Empty input edge**: `[] | min` → `null`, NOT error.
18. **Boolean-int conflation**: `true == 1` is **false** in jq (different types); `true + 1` is error.
19. **`length` on string**: character count (NOT byte count). For UTF-8, `length` of `"日本語"` is 3 (chars), but `utf8bytelength` is 9.
20. **Recursion depth**: `def f: ., (.[] | f);` can recurse arbitrarily — Python's default 1000-level limit will trip on moderately deep input. Set `sys.setrecursionlimit(50000)` early in main.py.
21. **`limit(0; f)`** → no output. `limit(N; f)` where N >= count → all values.
22. **Stream / `--stream` order**: open-first, close-last; sibling order matches insertion.
23. **`paths(f)` filter semantics**: only emit paths where the value at the path matches f, recursively.
24. **`del` with overlapping paths**: delete deepest first to avoid invalidation; jq does this internally.
25. **Trailing newlines**: pretty/compact emit one newline per output value; `-j` emits NONE; `-r` on string emits newline after raw content.

---

## Source provenance

- 1,938 CATCHES docstrings extracted from 124 unique test files across 12 branches of `jqlang__jq.b33a763`.
- 619 `.golden` files + 96 `.stderr` files inspected from branch `ff26b33afe1a` (largest, 2,976 tests).
- conftest.py fixture API extracted directly from the test tarballs.
- This spec is dated 2026-05-09 and is canonical for the next jq build attempt.
