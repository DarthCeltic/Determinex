#!/usr/bin/env python3
"""Determinex I/O-example extractor.

Turns a tool's shipped pytest suite into concrete black-box examples:
    {test, argv, stdin, env, expect_rc, expect_stdout (exact), expect_in[...]}
by AST-parsing each test function for its run-helper invocation and assertions,
and resolving golden-file references (`(RESOURCES / "x.golden").read_text()`)
against the actual golden files on disk. These examples are ground truth -- the
local oracle (determinex_local_oracle) runs the reimpl against them with zero
network and no Docker, so a fix is validated in milliseconds before any eval.

It is deliberately CONSERVATIVE: an example is emitted only when argv is
recoverable AND at least one expectation (rc / exact stdout / contains) is
known. Anything ambiguous is skipped and counted -- never a guessed expectation,
so the oracle never reports false confidence.

PB-compliant: read-only over the shipped tests. It never edits a test, a golden,
collection, or the eval.
"""
from __future__ import annotations

import argparse
import ast
import json
from dataclasses import dataclass, field, asdict
from pathlib import Path

RUN_NAMES = {"run", "run_exe", "run_hx", "run_cmd", "_run", "run_executable",
             "run_minimap", "run_nomino", "run_tool", "invoke", "execute"}
STDIN_KW = {"stdin", "input", "input_bytes", "input_text", "input_data", "input_str"}
ARGS_KW = {"args", "argv", "arguments"}
RESULT_ATTRS = {"returncode", "code", "rc"}


@dataclass
class Example:
    test: str
    argv: list = field(default_factory=list)
    stdin: str | None = None          # decoded text; None = no stdin
    env: dict = field(default_factory=dict)
    expect_rc: int | None = None
    expect_stdout: str | None = None  # exact match (from golden or literal)
    expect_stderr: str | None = None  # exact match (reference-enriched: the real stderr)
    expect_in: list = field(default_factory=list)   # substrings asserted present
    files: dict = field(default_factory=dict)       # filename -> content for file-arg tests
    ci: bool = False                  # contains check is case-insensitive
                                      # (test compared against .lower()/.casefold())
    source: str = ""                  # test file:line


@dataclass
class Coverage:
    examples: list
    n_tests: int
    n_examples: int
    skipped: list                     # test names we couldn't pin down


# --- small constant / path evaluators -------------------------------------

def _const(node):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, (ast.List, ast.Tuple)):
        out = []
        for e in node.elts:
            v = _const(e)
            if v is _UNK:
                return _UNK
            out.append(v)
        return out
    if isinstance(node, ast.Call):
        # str(x) / bytes(...) wrappers around constants
        fn = node.func
        if isinstance(fn, ast.Name) and fn.id == "str" and node.args:
            v = _const(node.args[0])
            return _UNK if v is _UNK else str(v)
    if isinstance(node, ast.JoinedStr):     # f-strings -> only if all literal
        parts = []
        for v in node.values:
            if isinstance(v, ast.Constant):
                parts.append(str(v.value))
            else:
                return _UNK
        return "".join(parts)
    return _UNK


_UNK = object()


def _argv_strs(value):
    """Coerce an extracted list into a list[str] argv, or None if not usable."""
    if value is _UNK or value is None:
        return None
    if not isinstance(value, list):
        return None
    out = []
    for v in value:
        if isinstance(v, bool):
            return None
        if isinstance(v, (str, int, float)):
            out.append(str(v))
        else:
            return None
    return out


class _PathResolver:
    """Resolves module-level path vars like
    RESOURCES = Path(__file__).parent.parent / "test_resources" / "test_function"
    so golden references can be read from disk."""

    def __init__(self, test_file: Path):
        self.test_file = test_file
        self.vars: dict[str, Path] = {}

    def learn(self, tree: ast.Module):
        for node in tree.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1:
                tgt = node.targets[0]
                if isinstance(tgt, ast.Name):
                    p = self.eval_path(node.value)
                    if p is not None:
                        self.vars[tgt.id] = p

    def eval_path(self, node) -> Path | None:
        # Path(__file__) ...
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id == "Path" and node.args:
            a = node.args[0]
            if isinstance(a, ast.Name) and a.id == "__file__":
                return self.test_file
            c = _const(a)
            if isinstance(c, str):
                return Path(c)
            return None
        if isinstance(node, ast.Attribute):  # .parent
            base = self.eval_path(node.value)
            if base is None:
                return None
            if node.attr == "parent":
                return base.parent
            return None
        if isinstance(node, ast.Name):
            return self.vars.get(node.id)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            base = self.eval_path(node.left)
            rhs = _const(node.right)
            if base is not None and isinstance(rhs, str):
                return base / rhs
            return None
        return None

    def resolve_read(self, node) -> str | None:
        """If node is `(<path>).read_text()` / `.read_bytes()`, return file text."""
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
            return None
        if node.func.attr not in ("read_text", "read_bytes"):
            return None
        p = self.eval_path(node.func.value)
        if p is None or not p.exists():
            return None
        try:
            data = p.read_bytes()
            return data.decode("utf-8", "replace")
        except Exception:
            return None


# --- per-test extraction ----------------------------------------------------

# pipe/consumer commands whose arg-lists must NOT be mistaken for the reimpl's
# argv (e.g. subprocess to `head -n 5` in a broken-pipe test).
_CONSUMER_CMDS = {"head", "tail", "grep", "cat", "sort", "wc", "sed", "awk",
                  "tr", "less", "more", "tee", "xxd", "od", "cut", "uniq"}


def _track_files(func: ast.FunctionDef, vmap: dict | None = None) -> dict:
    """Map file-arg variables to (basename, content), following the common pattern
    `p = tmp_path / "in.tex"; p.write_text(content)` then `run(..., str(p))`.
    Resolves a content VARIABLE via vmap (content="..."; p.write_text(content)).
    Without this the reference observation runs against a MISSING file (wrong oracle)."""
    vmap = vmap or {}
    names: dict[str, str] = {}
    files: dict[str, tuple] = {}
    for node in ast.walk(func):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            v = node.targets[0].id
            val = node.value
            if isinstance(val, ast.BinOp) and isinstance(val.op, ast.Div):
                c = _const(val.right)
                if isinstance(c, str):
                    names[v] = c.rsplit("/", 1)[-1]
            elif isinstance(val, ast.Call) and isinstance(val.func, ast.Attribute) \
                    and val.func.attr in ("create", "write_file", "make_file", "add_file", "make", "add") \
                    and len(val.args) >= 2:
                # `tf = temp_files.create("test.tex", content)` fixture helper -> file+content
                nm = _const(val.args[0])
                ct = _resolve(val.args[1], vmap)
                content = ct.decode("utf-8", "replace") if isinstance(ct, bytes) \
                    else (ct if isinstance(ct, str) else None)
                if isinstance(nm, str) and content is not None:
                    files[v] = (nm.rsplit("/", 1)[-1], content)
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr in ("write_bytes", "write_text") \
                and isinstance(node.func.value, ast.Name) and node.args:
            v = node.func.value.id
            c = _resolve(node.args[0], vmap)
            content = c.decode("utf-8", "replace") if isinstance(c, bytes) \
                else (c if isinstance(c, str) else None)
            if content is not None and v in names:
                files[v] = (names[v], content)
    return files


def _file_arg(a, files_map: dict):
    """If arg node `a` is `str(v)` or `v` for a tracked file var, return (basename, content)."""
    target = None
    if isinstance(a, ast.Call) and isinstance(a.func, ast.Name) and a.func.id == "str" \
            and len(a.args) == 1 and isinstance(a.args[0], ast.Name):
        target = a.args[0].id
    elif isinstance(a, ast.Name):
        target = a.id
    return files_map.get(target) if target else None


def _track_vars(func: ast.FunctionDef) -> dict:
    """Map local variables assigned a constant (str/bytes/int) so `stdin=input_tex`
    where `input_tex = "..."` resolves -- a VERY common pattern that otherwise leaves
    stdin uncaptured (the reference then runs with no input -> wrong oracle target)."""
    vmap: dict = {}
    for node in ast.walk(func):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            c = _const(node.value)
            if isinstance(c, (str, bytes, int, float, list)) and not isinstance(c, bool):
                vmap[node.targets[0].id] = c
    return vmap


def _fixture_return_const(node: ast.FunctionDef):
    """A @pytest.fixture body's returned/yielded constant (resolving its own locals)."""
    local = _track_vars(node)
    for n in reversed(list(ast.walk(node))):
        val = None
        if isinstance(n, ast.Return) and n.value is not None:
            val = n.value
        elif isinstance(n, ast.Expr) and isinstance(n.value, ast.Yield) and n.value.value is not None:
            val = n.value.value
        if val is not None:
            c = _const(val)
            if c is _UNK and isinstance(val, ast.Name) and val.id in local:
                c = local[val.id]
            if isinstance(c, (str, bytes, int, float, list)) and not isinstance(c, bool):
                return c
    return None


def _track_fixtures(tree: ast.Module) -> dict:
    """Map @pytest.fixture functions that return a constant -> value, so test args
    that are fixtures (sample_tex, etc.) resolve. Fixtures hold most test data."""
    fx: dict = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        is_fx = False
        for d in node.decorator_list:
            tgt = d.func if isinstance(d, ast.Call) else d
            if (isinstance(tgt, ast.Attribute) and tgt.attr == "fixture") \
                    or (isinstance(tgt, ast.Name) and tgt.id == "fixture"):
                is_fx = True
        if not is_fx:
            continue
        v = _fixture_return_const(node)
        if v is not None:
            fx[node.name] = v
    return fx


def _resolve(node, vmap: dict):
    """_const, but also resolve a bare Name via the local-var map."""
    c = _const(node)
    if c is _UNK and isinstance(node, ast.Name) and node.id in vmap:
        return vmap[node.id]
    return c


def _resolve_list(list_node, files_map: dict, vmap: dict, used_files: dict):
    """Resolve every element of an argv LIST literal: literals, vars, and
    str(file_var)/file_var (-> basename + stage file). Returns argv list or None
    if any element is unresolvable. Handles run(["--print", str(tex_file)])."""
    if not isinstance(list_node, ast.List):
        return None
    out = []
    for e in list_node.elts:
        fa = _file_arg(e, files_map)
        if fa is not None:
            out.append(fa[0]); used_files[fa[0]] = fa[1]; continue
        c = _resolve(e, vmap)
        if isinstance(c, (str, int, float)) and not isinstance(c, bool):
            out.append(str(c))
        else:
            return None
    return out


def _find_run_call(func: ast.FunctionDef, files_map: dict | None = None,
                   vars_map: dict | None = None):
    """Return (argv, stdin, env, files) for the run-helper call. Prefer calls whose
    func name is a known runner; never treat a pipe-consumer command's arg list
    (head/grep/...) as the reimpl argv."""
    files_map = files_map or {}
    vars_map = vars_map or {}
    # rank: named runner first, bare-list candidate last
    named = []
    other = []
    for node in ast.walk(func):
        if isinstance(node, ast.Call):
            fn = node.func
            nm = fn.id if isinstance(fn, ast.Name) else (
                fn.attr if isinstance(fn, ast.Attribute) else "")
            (named if nm in RUN_NAMES else other).append((nm, node))
    for name, node in named + other:
        looks_run = name in RUN_NAMES or any(
            isinstance(k, ast.keyword) and k.arg in (STDIN_KW | ARGS_KW)
            for k in node.keywords)
        if not looks_run:
            continue
        argv = None
        stdin = None
        env = {}
        used_files: dict = {}
        # positional argv: first positional that is a list, else collect strs
        pos_strs = []
        for a in node.args:
            if isinstance(a, ast.List):        # argv given as a list literal
                lst = _resolve_list(a, files_map, vars_map, used_files)
                if lst is not None:
                    argv = lst
                    break
                continue
            fa = _file_arg(a, files_map)
            if fa is not None:                 # file-arg: pass basename + stage content
                pos_strs.append(fa[0]); used_files[fa[0]] = fa[1]; continue
            c = _resolve(a, vars_map)
            if isinstance(c, list):
                argv = _argv_strs(c)
                break
            elif isinstance(c, (str, int, float)) and not isinstance(c, bool):
                pos_strs.append(str(c))
        if argv is None and pos_strs:
            argv = pos_strs            # run(*args) style
        for k in node.keywords:
            if k.arg in ARGS_KW:
                if isinstance(k.value, ast.List):
                    lst = _resolve_list(k.value, files_map, vars_map, used_files)
                    argv = lst if lst is not None else _argv_strs(_resolve(k.value, vars_map))
                else:
                    argv = _argv_strs(_resolve(k.value, vars_map))
            elif k.arg in STDIN_KW:
                v = _resolve(k.value, vars_map)
                if isinstance(v, bytes):
                    stdin = v.decode("utf-8", "replace")
                elif isinstance(v, str):
                    stdin = v
            elif k.arg == "env":
                v = _const(k.value)
                if isinstance(k.value, ast.Dict):
                    d = {}
                    for kk, vv in zip(k.value.keys, k.value.values):
                        ck, cv = _const(kk), _const(vv)
                        if isinstance(ck, str) and isinstance(cv, (str, int)):
                            d[ck] = str(cv)
                    env = d
        # never mistake a pipe-consumer command (head/grep/...) for the argv
        if argv and argv[0] in _CONSUMER_CMDS:
            continue
        if argv is not None:
            return argv, stdin, env, used_files
    return None, None, {}, {}


def _find_expectations(func: ast.FunctionDef, resolver: _PathResolver):
    rc = None
    exact = None
    contains = []
    ci = False
    for node in ast.walk(func):
        if not isinstance(node, ast.Assert):
            continue
        t = node.test
        if isinstance(t, ast.Compare) and len(t.ops) == 1:
            op = t.ops[0]
            left, right = t.left, t.comparators[0]
            if isinstance(op, ast.Eq):
                # rc?  result.returncode == N  /  result.code == N
                if _is_result_rc(left):
                    c = _const(right)
                    if isinstance(c, int):
                        rc = c
                elif _is_result_rc(right):
                    c = _const(left)
                    if isinstance(c, int):
                        rc = c
                else:
                    # exact stdout: result.stdout(.decode()) == golden/const
                    if _is_result_out(left):
                        exact = _golden_or_const(right, resolver)
                    elif _is_result_out(right):
                        exact = _golden_or_const(left, resolver)
            elif isinstance(op, ast.In):
                snip = _const(left)
                # detect case-insensitive haystack: `snippet in result.stderr.lower()`
                if _is_lower_call(right):
                    ci = True
                if isinstance(snip, bytes):
                    contains.append(snip.decode("utf-8", "replace"))
                elif isinstance(snip, str):
                    contains.append(snip)
    return rc, exact, contains, ci


def _is_lower_call(node):
    """True if node is X.lower() / X.casefold() — marks a case-insensitive check."""
    return (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
            and node.func.attr in ("lower", "casefold"))


def _is_result_rc(node):
    return isinstance(node, ast.Attribute) and node.attr in RESULT_ATTRS


def _is_result_out(node):
    # result.stdout / result.out / result.stdout.decode()
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
            and node.func.attr == "decode":
        node = node.func.value
    return isinstance(node, ast.Attribute) and node.attr in ("stdout", "out")


def _golden_or_const(node, resolver: _PathResolver):
    g = resolver.resolve_read(node)
    if g is not None:
        return g
    c = _const(node)
    if isinstance(c, bytes):
        return c.decode("utf-8", "replace")
    if isinstance(c, str):
        return c
    return None


def extract_file(path: Path) -> Coverage:
    src = path.read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return Coverage([], 0, 0, [])
    resolver = _PathResolver(path)
    resolver.learn(tree)
    # Fixtures (this file + sibling conftest.py) hold most test data; resolve them so
    # `run(stdin=sample_tex)` / `create("x.tex", sample_tex)` capture the real input.
    fixtures = _track_fixtures(tree)
    conf = path.parent / "conftest.py"
    if conf.exists():
        try:
            fixtures.update(_track_fixtures(ast.parse(conf.read_text(encoding="utf-8", errors="replace"))))
        except SyntaxError:
            pass
    examples: list[Example] = []
    skipped: list[str] = []
    n_tests = 0
    for node in ast.walk(tree):
        if not (isinstance(node, ast.FunctionDef) and node.name.startswith("test_")):
            continue
        n_tests += 1
        vars_map = {**fixtures, **_track_vars(node)}   # local vars shadow fixtures
        files_map = _track_files(node, vars_map)
        argv, stdin, env, files = _find_run_call(node, files_map, vars_map)
        if argv is None:
            skipped.append(node.name)
            continue
        rc, exact, contains, ci = _find_expectations(node, resolver)
        if rc is None and exact is None and not contains:
            skipped.append(node.name)
            continue
        examples.append(Example(
            test=node.name, argv=argv, stdin=stdin, env=env,
            expect_rc=rc, expect_stdout=exact, expect_in=contains, ci=ci,
            files=files, source=f"{path.name}:{node.lineno}"))
    return Coverage(examples, n_tests, len(examples), skipped)


@dataclass
class InputProbe:
    """A recoverable test INPUT (no expectation) -- the reference fills the expectation."""
    test: str
    argv: list = field(default_factory=list)
    stdin: str | None = None
    env: dict = field(default_factory=dict)
    files: dict = field(default_factory=dict)
    source: str = ""


def extract_inputs_file(path: Path) -> list:
    """Every recoverable run-call INPUT in one test file (expectation NOT required)."""
    src = path.read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    resolver = _PathResolver(path)
    resolver.learn(tree)
    fixtures = _track_fixtures(tree)
    conf = path.parent / "conftest.py"
    if conf.exists():
        try:
            fixtures.update(_track_fixtures(ast.parse(conf.read_text(encoding="utf-8", errors="replace"))))
        except SyntaxError:
            pass
    out: list = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.FunctionDef) and node.name.startswith("test_")):
            continue
        vars_map = {**fixtures, **_track_vars(node)}
        files_map = _track_files(node, vars_map)
        argv, stdin, env, files = _find_run_call(node, files_map, vars_map)
        if argv is None:
            continue
        out.append(InputProbe(test=node.name, argv=argv, stdin=stdin, env=env or {},
                              files=files or {}, source=f"{path.name}:{node.lineno}"))
    return out


def extract_inputs(test_dir: Path) -> list:
    """All recoverable test INPUTS under test_dir (deduped by (argv, stdin, sorted files))."""
    seen: set = set()
    out: list = []
    for path in sorted(Path(test_dir).rglob("test_*.py")):
        for ip in extract_inputs_file(path):
            key = (tuple(ip.argv), ip.stdin, tuple(sorted((ip.files or {}).items())))
            if key in seen:
                continue
            seen.add(key)
            out.append(ip)
    return out


def extract_dir(test_dir: Path) -> Coverage:
    all_ex: list[Example] = []
    all_sk: list[str] = []
    n_tests = 0
    for p in sorted(test_dir.rglob("test_*.py")):
        cov = extract_file(p)
        all_ex.extend(cov.examples)
        all_sk.extend(cov.skipped)
        n_tests += cov.n_tests
    return Coverage(all_ex, n_tests, len(all_ex), all_sk)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Determinex I/O-example extractor")
    ap.add_argument("test_dir", help="dir containing test_*.py (+ resolvable goldens)")
    ap.add_argument("--out", help="write examples JSON here")
    ap.add_argument("--show", type=int, default=12)
    a = ap.parse_args(argv)
    cov = extract_dir(Path(a.test_dir))
    print(f"tests seen: {cov.n_tests}   examples extracted: {cov.n_examples}   "
          f"skipped: {len(cov.skipped)}   "
          f"({100*cov.n_examples/max(cov.n_tests,1):.0f}% coverage)")
    exact = sum(1 for e in cov.examples if e.expect_stdout is not None)
    print(f"  with exact-stdout golden: {exact}   with rc: "
          f"{sum(1 for e in cov.examples if e.expect_rc is not None)}   "
          f"with contains: {sum(1 for e in cov.examples if e.expect_in)}")
    for e in cov.examples[:a.show]:
        exp = f"rc={e.expect_rc}" if e.expect_rc is not None else ""
        ex = " EXACT" if e.expect_stdout is not None else ""
        ind = f" in={e.expect_in[:1]}" if e.expect_in else ""
        sd = f" stdin={e.stdin!r}" if e.stdin else ""
        print(f"  {e.test:46} argv={e.argv}{sd} {exp}{ex}{ind}")
    if a.out:
        Path(a.out).write_text(json.dumps([asdict(e) for e in cov.examples], indent=2),
                               encoding="utf-8")
        print(f"wrote {cov.n_examples} examples -> {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
