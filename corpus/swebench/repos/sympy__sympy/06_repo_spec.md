---
name: swebench-sympy__sympy
description: SWE-bench repo behavioral spec for sympy/sympy. Aggregated from 538 bug-fix instances across 3 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# sympy/sympy — SWE-bench Repo Spec

> **538 bug-fix instances** across 3 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-test | 386 |
| swe-bench-lite-test | 77 |
| swe-bench-verified-test | 75 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `sympy/printing/latex.py` | 43 |
| `sympy/core/numbers.py` | 30 |
| `sympy/printing/pretty/pretty.py` | 27 |
| `sympy/printing/str.py` | 24 |
| `sympy/printing/pycode.py` | 19 |
| `sympy/core/function.py` | 17 |
| `sympy/sets/sets.py` | 16 |
| `sympy/matrices/expressions/matexpr.py` | 14 |
| `sympy/core/power.py` | 14 |
| `sympy/sets/fancysets.py` | 14 |
| `sympy/core/mul.py` | 12 |
| `sympy/polys/polytools.py` | 11 |
| `sympy/core/mod.py` | 10 |
| `sympy/utilities/lambdify.py` | 10 |
| `sympy/geometry/point.py` | 10 |
| `sympy/core/exprtools.py` | 10 |
| `sympy/printing/mathematica.py` | 9 |
| `sympy/combinatorics/permutations.py` | 9 |
| `sympy/core/expr.py` | 9 |
| `sympy/core/basic.py` | 9 |
| `sympy/matrices/matrices.py` | 8 |
| `sympy/functions/elementary/hyperbolic.py` | 8 |
| `sympy/core/add.py` | 8 |
| `sympy/simplify/simplify.py` | 8 |
| `sympy/printing/codeprinter.py` | 8 |
| `sympy/printing/mathml.py` | 7 |
| `sympy/solvers/diophantine.py` | 7 |
| `sympy/utilities/iterables.py` | 7 |
| `sympy/functions/elementary/complexes.py` | 7 |
| `sympy/simplify/cse_main.py` | 7 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: test_ccode_Relational, test_ccode_sinc, test_sinc, test_latex_Piecewise, test_Derivative**

Sample FAIL_TO_PASS test names (first 10):
```
  test_ccode_Relational
  test_ccode_sinc
  test_sinc
  test_latex_Piecewise
  test_Derivative
  test_div
  test_Identity
  test_is_upper
  test_hessenberg
  test_args
```

## Section 4 — Problem-theme distribution

Top themes across 538 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 180 | 33.5% |
| import_module | 113 | 21.0% |
| crash_or_traceback | 84 | 15.6% |
| wrong_output | 82 | 15.2% |
| edge_case | 31 | 5.8% |
| documentation | 19 | 3.5% |
| config_environment | 9 | 1.7% |
| regression | 7 | 1.3% |
| encoding_unicode | 6 | 1.1% |
| performance | 4 | 0.7% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `sympy__sympy-11400`

**Files likely affected**: `sympy/printing/ccode.py`
**FAIL_TO_PASS** (2 tests, first 3): `['test_ccode_Relational', 'test_ccode_sinc']`

**Problem statement (excerpt):**
> ccode(sinc(x)) doesn't work ''' In [30]: ccode(sinc(x)) Out[30]: '// Not supported in C:\n// sinc\nsinc(x)' '''  I don't think 'math.h' has 'sinc', but it could print  ''' In [38]: ccode(Piecewise((sin(theta)/theta, Ne(theta, 0)), (1, True))) Out[38]: '((Ne(theta, 0)) ? (\n   sin(theta)/theta\n)\n: (\n   1\n))' '''  

### Sample 2 — `sympy__sympy-11870`

**Files likely affected**: `sympy/functions/elementary/trigonometric.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test_sinc']`

**Problem statement (excerpt):**
> simplifying exponential -> trig identities '''
 f = 1 / 2 * (-I*exp(I*k) + I*exp(-I*k))
 trigsimp(f)
 '''
 
 Ideally, this would yield 'sin(k)'. Is there a way to do this?
 
 As a corollary, it would be awesome if 
 
 '''
 f = 1 / 2 / k* (-I*exp(I*k) + I*exp(-I*k))
 trigsimp(f)
 '''
 
 could yield 'sinc(k)'. Thank you for your consideration! 

### Sample 3 — `sympy__sympy-11897`

**Files likely affected**: `sympy/printing/latex.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test_latex_Piecewise']`

**Problem statement (excerpt):**
> LaTeX printer inconsistent with pretty printer The LaTeX printer should always give the same output as the pretty printer, unless better output is possible from LaTeX. In some cases it is inconsistent. For instance:  ''' py In [9]: var('x', positive=True) Out[9]: x  In [10]: latex(exp(-x)*log(x)) Out[10]: '\\frac{1}{e^{x}} \\log{\\left (x \\right )}'  In [11]: pprint(exp(-x)*log(x))  -x ℯ  ⋅log(x)

### Sample 4 — `sympy__sympy-12171`

**Files likely affected**: `sympy/printing/mathematica.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test_Derivative']`

**Problem statement (excerpt):**
> matematica code printer does not handle floats and derivatives correctly In its current state the mathematica code printer does not handle Derivative(func(vars), deriver) 
 e.g. Derivative(f(t), t) yields Derivative(f(t), t) instead of D[f[t],t]
 
 Also floats with exponents are not handled correctly e.g. 1.0e-4 is not converted to 1.0*^-4
 
 This has an easy fix by adding the following lines to M

### Sample 5 — `sympy__sympy-12236`

**Files likely affected**: `sympy/polys/domains/polynomialring.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test_div']`

**Problem statement (excerpt):**
> Wrong result with apart '''
 Python 3.6.0 |Continuum Analytics, Inc.| (default, Dec 23 2016, 12:22:00) 
 Type "copyright", "credits" or "license" for more information.
 
 IPython 5.1.0 -- An enhanced Interactive Python.
 ?         -> Introduction and overview of IPython's features.
 %quickref -> Quick reference.
 help      -> Python's own help system.
 object?   -> Details about 'object', use 'obj

### Sample 6 — `sympy__sympy-12419`

**Files likely affected**: `sympy/matrices/expressions/matexpr.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test_Identity']`

**Problem statement (excerpt):**
> Sum of the elements of an identity matrix is zero I think this is a bug.
 
 I created a matrix by M.T * M under an assumption that M is orthogonal.  SymPy successfully recognized that the result is an identity matrix.  I tested its identity-ness by element-wise, queries, and sum of the diagonal elements and received expected results.
 
 However, when I attempt to evaluate the total sum of the elem

### Sample 7 — `sympy__sympy-12454`

**Files likely affected**: `sympy/matrices/matrices.py`
**FAIL_TO_PASS** (2 tests, first 3): `['test_is_upper', 'test_hessenberg']`

**Problem statement (excerpt):**
> is_upper() raises IndexError for tall matrices The function Matrix.is_upper raises an IndexError for a 4x2 matrix of zeros.
 '''
 >>> sympy.zeros(4,2).is_upper
 Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
   File "sympy/matrices/matrices.py", line 1112, in is_upper
     for i in range(1, self.rows)
   File "sympy/matrices/matrices.py", line 1113, in <genexpr>
     for

### Sample 8 — `sympy__sympy-12481`

**Files likely affected**: `sympy/combinatorics/permutations.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test_args']`

**Problem statement (excerpt):**
> 'Permutation' constructor fails with non-disjoint cycles Calling 'Permutation([[0,1],[0,1]])' raises a 'ValueError' instead of constructing the identity permutation.  If the cycles passed in are non-disjoint, they should be applied in left-to-right order and the resulting permutation should be returned.
 
 This should be easy to compute.  I don't see a reason why non-disjoint cycles should be forb

## Section 6 — Builder guidance

When building a fix for an instance in sympy/sympy:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. sympy/printing/latex.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 538 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "sympy/sympy"`).

First 20 instance_ids:

- `sympy__sympy-11400` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-11870` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-11897` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-12171` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-12236` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-12419` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-12454` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-12481` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-13031` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-13043` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-13146` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-13177` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-13437` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-13471` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-13480` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-13647` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-13773` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-13895` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-13915` (dataset: `swe-bench-lite-test`)
- `sympy__sympy-13971` (dataset: `swe-bench-lite-test`)
- ... (518 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*

---

## Section 8 — Anchor-grade hand-curated reference (top-2 by instance count, 538 instances)

### Repo overview
SymPy is the Python symbolic math library. Bug fixes cluster in printers (LaTeX/pretty/MathML),
core simplification, and numeric coercion. Heavy dependency on `Basic`, `Atom`, `Expr` class
hierarchy.

### High-leverage bug zones

| Subsystem | Touch count | Common bug pattern |
|-----------|------------|--------------------|
| `sympy/printing/latex.py` | 43 | Edge-case LaTeX formatting (Mul, Pow, Derivative, Integral) |
| `sympy/core/numbers.py` | 30 | Number coercion (Rational, Float, Integer); Infinity handling |
| `sympy/printing/pretty/pretty.py` | 27 | ASCII pretty-printing alignment |
| `sympy/core/expr.py` | ~20 | `_eval_*` methods; expression normalization |
| `sympy/polys/polytools.py` | ~18 | Polynomial domain coercion; gcd/lcm edges |
| `sympy/integrals/integrals.py` | ~15 | Symbolic integration; piecewise handling |

### Test framework
SymPy uses **pytest with a custom `sympy.testing.pytest`** wrapper. FAIL_TO_PASS names look like:
`sympy.printing.tests.test_latex.test_latex_basic`.

### Builder rules specific to SymPy

1. **Never use Python `==` between SymPy objects** unless you mean `Eq` semantics. Use `equals()` for structural equality.
2. **`Symbol('x')` is a singleton-by-name**. `Symbol('x') == Symbol('x')` is True.
3. **`evaluate=False`** in expression construction — when adding new code, decide if it should evaluate.
4. **Printer dispatch**: each new class needs its `_print_<ClassName>` method on each printer it supports (Latex, Pretty, MathML, etc.).
5. **Floating-point in symbolic context**: avoid `float()` coercion; use `nsimplify()` or `Float`.
6. **Cache invalidation**: many `Basic` subclasses have `__hash__` cached; don't mutate after hash.
7. **`assumptions`**: changes to assumption logic cascade across `is_real`, `is_positive`, etc.

### Where 90→100% lives

- `test_latex_*` → exact string match against goldens; whitespace + brace placement matters
- `test_pretty_*` → ASCII column alignment; Unicode subscripts/superscripts
- `test_simplify_*` → `_eval_simplify` correctness; pattern matching
- `test_solve*` → `solveset` vs `solve` API consistency
- `test_polynomial_*` → domain inference; ground-domain coercion

### Estimated lock cost per instance
~8-20 min on Sonnet; ~25-60 min on local Qwen 14b. SymPy bugs often need test-case mental simulation.
