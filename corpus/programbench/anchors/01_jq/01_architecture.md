---
name: jq-architecture
description: Architecture blueprint for the jq reimplementation. Picks Python as the build language; designs the lexer/parser/compiler/VM/JSON-IO split; specifies the value model, the bytecode-or-tree-walk decision, and the build script.
type: architecture
---

# jq — Architecture Blueprint

## Language choice

**Python.** Justification:
1. PB containers ship `python3` (3.10) and pip works. No build step.
2. jq's two hard parts — *generators* and *recursive filters* — map cleanly to Python generators + `yield`.
3. JSON I/O is stdlib; jq's exact output formatting just needs careful overrides.
4. The reference jq is C, but C in the container means stdlib-only writing of a JSON parser + filter compiler. That's possible, but slower to lock; Python is the fastest path to 100%.

Fallback: Go, if a Python attempt collides on runtime perf for the largest test branches (>2k tests/branch). Use only after Python attempt at 1 hangs >95%.

## Core data structures

### `JqValue` (the jv equivalent)
A tagged Python type:
```
None | bool | int | float | str | list[JqValue] | dict[str, JqValue]
```
Use Python's native types directly. The only place this leaks: `dict` insertion order **must** be preserved (Python 3.7+ does this natively — verify in tests). Number formatting needs a wrapper:

```python
def emit_num(x):
    if isinstance(x, int): return str(x)
    if x.is_integer(): return f"{int(x)}"   # 1.0 → "1" (jq behavior)
    return repr(x)                           # but watch trailing precision
```

### `Path` — list of keys for assignments
Used by `=`, `|=`, `+=`, etc. A path is `tuple[str|int, ...]` from root.

### `AST` nodes (the filter program)
A tagged dataclass tree:
```
Identity | Field(name) | Index(expr) | Slice(lo, hi)
Pipe(a,b) | Comma(a,b) | Neg(a) | Not(a)
Literal(v) | Variable(name) | RecurseDescent
Object(pairs) | Array(elem)
Funcall(name, args) | Funcdef(name, params, body, rest)
Assign(path, value, op)   # op in {=, |=, +=, -=, *=, /=, //=}
TryCatch(try_, catch_)    | Reduce(src, var, init, update)
Foreach(src, var, init, update, extract) | If(cond, then_, else_)
Format(name)              | Bind(var, expr, body)   # . as $x | ...
```

### Backtracking: the **stream/generator** is the core abstraction
Every filter is a function `JqValue → Iterator[JqValue]`. **No bytecode VM is required for a 100%-passing implementation** — a tree-walk interpreter that yields is enough. (jq's reference uses a bytecode VM for speed, but PB tests correctness, not speed.)

```python
def eval_filter(node, ctx, val) -> Iterator[JqValue]: ...
```

`Pipe(a, b)` is implemented as:
```python
for av in eval_filter(a, ctx, val):
    yield from eval_filter(b, ctx, av)
```
`Comma(a, b)` is:
```python
yield from eval_filter(a, ctx, val)
yield from eval_filter(b, ctx, val)
```

This single pattern reproduces jq's "every comma is a fork point" semantics without explicit backtracking machinery.

## Module breakdown

```
main.py              entrypoint, argparse, --slurp, file/stdin handling
json_io.py           parse_json, emit_json (exact formatting + key ordering modes)
lexer.py             token stream from filter source
parser.py            recursive-descent → AST
compiler.py          desugar (range as a function, // as alternative, etc.)
evaluator.py         tree-walking generator interpreter; ctx = funcs+vars
builtins.py          all builtin functions: length/keys/values/type/map/select/...
paths.py             path expressions for assignments (=, |=, +=, etc.)
regex.py             test/match/capture/sub/gsub — wraps Python re module
errors.py            JqError + halt/halt_error/error/$__loc__
```

## Build script

`compile.sh`:
```bash
#!/bin/bash
set -e
# Stdlib only — no pip installs needed, jq is pure parsing
chmod +x main.py
ln -sf main.py executable
```

`main.py` shebang: `#!/usr/bin/env python3`. PB's container ships Python 3.10; `dataclasses`, `enum`, `re`, `json`, `argparse` are all stdlib.

## Critical implementation decisions

### Decision 1: Use Python's `json` parser? **No.**
Python's stdlib `json` accepts more than jq accepts (it accepts `NaN`, `Infinity` by default; integers can lose precision through float promotion). Hand-write a strict RFC 8259 parser that matches jq's `--exit-on-error` semantics exactly. ~150 LOC.

### Decision 2: Path tracking via "shadow eval"
Assignments like `.a.b += 1` need to know where the result came from. Implement `eval_paths(node, val) → Iterator[Path]` as a parallel function — only used in the LHS of an assignment. Avoids polluting the value-emitting evaluator.

### Decision 3: Generators over recursion limit
Python's default recursion limit is 1000. jq programs can recurse arbitrarily (`def f: ., (.[] | f);`). Two options:
- (a) `sys.setrecursionlimit(50000)` at top of main.py — quick fix.
- (b) Trampoline-based eval — correct but invasive.
Pick (a). PB tests don't go past a few hundred levels.

### Decision 4: Number formatting
The trickiest single point. jq prints `1.0` as `1`, `1.5` as `1.5`, `1e100` as `1e+100` (not `1e100`), and never prints `NaN`/`Inf`. Match exactly:
```python
def emit_num(x):
    if isinstance(x, bool): raise TypeError  # bool is int subclass!
    if isinstance(x, int):  return str(x)
    if math.isnan(x) or math.isinf(x): return "null"  # jq never emits NaN/Inf
    if x.is_integer() and abs(x) < 1e16: return str(int(x))
    return _format_jq_double(x)  # 1e+100 not 1e100, no trailing zeros
```

### Decision 5: Output flags
`-r`, `-c`, `-j`, `-s`, `-n`, `-e`, `--tab`, `--indent N`, `--sort-keys`, `-R`, `-a` (ascii output) — all argparse, all parameterize the `emit_json` call. Don't try to be clever; keep flag plumbing flat.

## What NOT to implement

These are documented but rarely tested at the 100% level — defer until eval shows they're hit:
- `@base64`, `@uri`, `@csv`, `@tsv`, `@html`, `@sh` — probably tested, *implement them*; they're cheap.
- `getpath`, `setpath`, `del` paths — implement; cheap.
- Module imports / `import "x" as $x` — almost certainly NOT tested; defer.
- SQL-style operations from the cookbook — defer.
- Streaming mode (`--stream`) — defer; check eval, only implement if hit.
- `jq -f`, `--args`, `--jsonargs` — implement, they're shallow.

## Reference jq quirks to NOT miss

1. `null | length` → `0`. `null | keys` → error. `null | type` → `"null"`.
2. `[] | min` → `null`. Empty array reductions are `null`, not error.
3. `1 / 0` → error (not Infinity).
4. String multiplication: `"-" * 3` → `"---"`. Number * string → repeat.
5. `"a" + null` → error; null is **not** the additive identity for strings.
6. `def f(g): g | g; 1 | f(.+1)` → 3 (closures capture lexical args, not values).
7. `--sort-keys` only sorts at object level, NOT recursively at the array level.
8. Default exit code 0; with `-e` set, exit 1 if last value was null/false/empty.

These get tested. Bake them into `evaluator.py` from day 1.
