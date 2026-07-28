# Determinex — Full Benchmark Expansion Plan

> **Written**: May 2026. **Status as of 2026-06-10**: Planning doc; several items are now live.
> ProgramBench: 53 confirmed full-suite locks / 26.5% (vs "4 tools" when this doc was written).
> SWE-bench Lite: B-Uncloaked 14.0% audited May snapshot, lower-bound Cloak-on configs.
> SWE-bench Verified / Full / Pro, Terminal-Bench, LiveCodeBench: still planned / not started.
> The Cloak extension for Go/TypeScript described in Tier 2 is not yet built.
> Based on: complete codebase audit, smoke7 post-mortem, SWE-bench Lite ablation in progress,
> full architecture review (all 5 generations).
> **Purpose**: Map every major AI coding benchmark to Determinex's existing architecture,
> identify the true capability gaps, and specify what needs to be built — with no hand-waving.

---

## What We Actually Know Right Now

**Two validated scores:**

1. **~11.7% on SWE-bench Lite** (D-NuclearHybrid-Cloaked, broken baseline, 12 known bugs).
   Hardened post-fix number: TBD (eval running).
2. **4 tools at TRUE 100% on ProgramBench** (zoxide, yj, ripsecrets, htmlq) — the 200-task
   benchmark where every frontier model currently scores 0% fully resolved. First documented
   full-resolutions of any ProgramBench tasks by any system. Strategy + 8 cross-tool transferable
   lessons in [`docs/PROGRAMBENCH.md`](PROGRAMBENCH.md).

Everything below is extrapolation or new capability. Be honest about that.

**What SWE-bench Lite actually tests:**
- Python repos only
- Bug fixes (patch, not new code)
- Single-file or small multi-file changes
- Issue text → identify file → generate unified diff → pass pytest

**What Determinex's architecture actually is:**
- **Gen 3 (Tauri/Rust)**: Consumer IDE — MPSC actor loop, Vanguard vault, fastembed RAG, sqlite-vec
- **Gen 4 (Hive Mind Python)**: Research pipeline — DAG orchestrator, Compiler Oracle, Rosetta Stone, ForgeDaemon
- **Gen 5 (Project Cloak)**: Privacy layer — AST obfuscation for cloud AI on SWE-bench

These are complementary, not competing. The expansion plan touches all three.

---

## The Full Benchmark Map

### Tier 0 — ProgramBench (Active, 5 tools at display-100)

- **What it is**: 200 real-world CLI tools, each reimplemented from scratch and verified
  against pytest test suites + byte-exact golden output files (224 to 14,637 tests per task).
  Released by Facebook Research, May 2026.
- **SOTA**: **0% fully resolved** across every frontier model (Opus 4.7, GPT-5.4, Gemini 3.1 Pro).
  Partial scores cap at ~95% for any given tool. The full-resolution threshold is what makes
  this the hardest coding benchmark on earth.
- **Determinex's confirmed score**: 4 tools at TRUE 100% (zoxide, yj, ripsecrets, htmlq).
- **Why it matters**: Determinex's compiler-gated retry loop is structurally aligned with what
  ProgramBench rewards. The benchmark is the cleanest demonstration of "the loop converts
  *nearly correct* into *resolved*" because frontier single-pass models cap at 95% and never
  improve without human intervention.
- **Strategy**: Five-anchor compounding plan (jq → fzf → lz4 → fd → curlie) targeting 35-40
  cluster-sibling locks, plus a parallel mass-run v1 for the 157 residual tools. Combined
  target: 40+ tools at 100%. See [`docs/PROGRAMBENCH.md`](PROGRAMBENCH.md).
- **What's needed**: Anchor 1 (jq) build session; mass-run v1 first pass.
- **Run command**:
  ```bash
  cd T:/Dev/ProgramBench && PYTHONUTF8=1 uv run programbench eval \
    "T:/determinex-programbench/<pilot_dir>" --filter "<author>" --force
  ```

---

### Tier 1 — Drop-In (Zero New Code, Run Tomorrow)

#### SWE-bench Verified (500 instances)
- **What it is**: Human-verified subset of SWE-bench Full. Each instance has been confirmed
  solvable and has a clear, non-ambiguous problem statement. Better quality signal than Lite.
- **SOTA**: ~94% (Claude Mythos Preview). We'd expect: ~15-20% hardened.
- **Why it matters**: More instances = better statistical confidence in our score.
  The "Verified" quality bar makes our number more credible.
- **What's needed**: Nothing. Exact same harness, different `--dataset_name`.
- **Run command**:
  ```bash
  python scripts/determinex_swebench_run.py --config d --cloak --workers 4 --instances 500 \
    --dataset princeton-nlp/SWE-bench_Verified
  ```
- **Known issue**: OpenAI found training data contamination across all frontier models on
  Verified. Our models aren't trained on SWE-bench data, so contamination is less of a concern,
  but be clear about this in the white paper.

#### SWE-bench Full (2,294 instances)
- **What it is**: All 2,294 original instances, unfiltered. Includes hard, ambiguous, and
  genuinely unsolvable cases.
- **SOTA**: ~58%. We'd expect: 8-12%.
- **Why it matters**: The 300-instance Lite subsample was chosen for "approachability" — Full
  is the real thing. Scale reveals failure modes that don't appear at 300.
- **What's needed**: Nothing new. Same harness.
- **Caution**: 2,294 instances × ~2min/instance = ~77 hours at 1 worker. Need 4+ workers
  and a full weekend run. Docker state management becomes critical at this scale.

#### SWE-bench Verified Hard (~45 instances)
- **What it is**: The subset of Verified that takes >1 hour human time to solve.
  These are the genuinely hard bugs — multi-file, subtle logic errors, architectural issues.
- **SOTA**: ~30-35% (much lower than overall Verified).
- **Why it matters**: These are the instances where the Architect's reasoning quality determines
  everything. The Builder can't "pattern-match" a solution — it has to actually understand
  the bug.
- **What's needed**: Filter the Verified dataset to the Hard subset. The SWE-bench paper
  defines this as instances with `difficulty: "hard"` or similar field.
- **Our expectation**: ~5-8%. This is where the Architect plan quality bottleneck shows up most.

---

### Tier 2 — SWE-bench Pro (The New Gold Standard — Requires Cloak Extension)

#### SWE-bench Pro (1,865 instances, Python/Go/TypeScript/JavaScript)
- **What it is**: The benchmark that replaced Verified as the credible standard in 2026.
  Created specifically to address training contamination (uses recent commits from active repos).
  Every task requires ≥10 lines of change. Multi-language.
- **SOTA**: ~78% (Claude Mythos). We'd expect: ~8-12% Python instances, 0% Go/TS without Cloak extension.
- **Why it matters**: This is the headline benchmark for 2026. The white paper needs a Pro score.
  Also — Go and TypeScript are the two languages where Determinex's compiler oracle is weakest
  (go build is strong; tsc is good but JS is still weak). Building for Pro forces us to close
  that gap.
- **The Cloak problem**: Our Python AST obfuscation doesn't work on Go or TypeScript.
  The Python `IdentifierClassifier` component lives in `scripts/determinex_cloak/classifier.py` and historically used `ast.parse()` — Python-only.
  Building Cloak for Go and TypeScript is the core engineering task for Tier 2.

##### Go Cloak Extension

Go has a critical advantage: exported identifiers start with uppercase, unexported with lowercase.
This is a language-level privacy boundary. We only need to obfuscate lowercase (package-private)
identifiers. No full AST parser required — regex + heuristics + stdlib manifest suffices.

**Go stdlib manifest**: The Go standard library has ~300 packages. Rather than a static file,
we can generate it: `go list std` outputs all stdlib package names. Key safe names include all
stdlib package identifiers (fmt, os, io, sync, http, etc.) plus exported names from imported
packages.

**Go identifier extraction**:
```python
import re

GO_BUILTIN_SAFE = frozenset([
    # language builtins
    'true', 'false', 'nil', 'iota',
    'bool', 'byte', 'complex64', 'complex128', 'error',
    'float32', 'float64', 'int', 'int8', 'int16', 'int32', 'int64',
    'uint', 'uint8', 'uint16', 'uint32', 'uint64', 'uintptr',
    'rune', 'string',
    # builtin functions
    'append', 'cap', 'close', 'complex', 'copy', 'delete', 'imag',
    'len', 'make', 'new', 'panic', 'print', 'println', 'real',
    'recover',
    # special
    'init', 'main', 'Error', 'String',
])

def extract_go_private_identifiers(source: str) -> frozenset[str]:
    """Extract unexported (lowercase) Go identifiers for obfuscation.
    Exported identifiers (uppercase) are public API — never obfuscate.
    """
    # Find all identifiers: word-boundary \b, starts with lowercase
    candidates = set(re.findall(r'\b[a-z][a-zA-Z0-9_]*\b', source))
    # Remove builtins, keywords, and short names
    GO_KEYWORDS = frozenset([
        'break', 'case', 'chan', 'const', 'continue', 'default',
        'defer', 'else', 'fallthrough', 'for', 'func', 'go', 'goto',
        'if', 'import', 'interface', 'map', 'package', 'range',
        'return', 'select', 'struct', 'switch', 'type', 'var',
        'err', 't', 'ok', 'n', 'i', 'j', 'k', 'v', 'w', 'r',
    ])
    private = candidates - GO_BUILTIN_SAFE - GO_KEYWORDS
    # Filter single-char and very common short names
    private = {name for name in private if len(name) > 2}
    return frozenset(private)
```

**What NOT to obfuscate in Go**:
- Any identifier starting with uppercase (exported, public API)
- Package names (navigation)
- File paths
- Test function names starting with `Test`, `Benchmark`, `Example`
- Method names on exported types (they're part of the public interface)
- `err`, `t`, `ok` — near-universal short names

**Go RestorationEngine**: Same regex-based approach as Python — replace `x_NNNN` tokens
in the raw diff text. Go's identifier syntax is identical to Python's for this purpose.

##### TypeScript/JavaScript Cloak Extension

TypeScript is harder than Go because it has no language-level public/private indicator.
TypeScript's `private` keyword exists but isn't consistently used. The approach:

**Strategy**: Use tree-sitter for TypeScript AST parsing. The `tree-sitter` Python package
supports TypeScript/JavaScript grammars.

```python
# Install: pip install tree-sitter tree-sitter-typescript
from tree_sitter import Language, Parser
import tree_sitter_typescript as tstypescript

TS_LANG = Language(tstypescript.language_typescript())
JS_LANG = Language(tstypescript.language_javascript())

def extract_ts_private_identifiers(source: str, lang='typescript') -> frozenset[str]:
    """Extract TypeScript identifiers that are internal to the module."""
    parser = Parser(TS_LANG if lang == 'typescript' else JS_LANG)
    tree = parser.parse(source.encode())
    
    safe = set()  # exported names, decorators, etc.
    private = set()
    
    def walk(node):
        if node.type == 'export_statement':
            # Mark all identifiers in export statements as safe
            for child in node.children:
                if child.type == 'identifier':
                    safe.add(child.text.decode())
        elif node.type == 'identifier':
            name = node.text.decode()
            if len(name) > 2 and not name[0].isupper():
                private.add(name)
        for child in node.children:
            walk(child)
    
    walk(tree.root_node)
    
    TS_BUILTIN_SAFE = frozenset([
        'undefined', 'null', 'true', 'false', 'this', 'super',
        'console', 'process', 'require', 'module', 'exports',
        'Promise', 'Array', 'Object', 'String', 'Number', 'Boolean',
        'Error', 'Map', 'Set', 'Symbol', 'BigInt', 'RegExp',
        'JSON', 'Math', 'Date', 'fetch', 'window', 'document',
        'setTimeout', 'clearTimeout', 'setInterval', 'clearInterval',
        # TS built-ins
        'readonly', 'abstract', 'declare', 'namespace',
        'type', 'interface', 'enum', 'implements', 'extends',
    ])
    return frozenset(private - safe - TS_BUILTIN_SAFE)
```

**TypeScript Compiler Oracle**:
The validator registry already lists `tsc` as planned. `tsc --noEmit --strict` on the patched
file validates TypeScript syntax and type correctness. Need to add `typescript_validator.py`:

```python
# scripts/validators/typescript_validator.py
import subprocess, tempfile, os

def validate_typescript(code: str, tsconfig: dict | None = None) -> tuple[bool, str]:
    with tempfile.NamedTemporaryFile(suffix='.ts', mode='w', delete=False) as f:
        f.write(code)
        path = f.name
    try:
        result = subprocess.run(
            ['tsc', '--noEmit', '--strict', '--target', 'ES2020', path],
            capture_output=True, text=True, timeout=30
        )
        return result.returncode == 0, result.stdout + result.stderr
    except FileNotFoundError:
        # tsc not installed — fall back to syntax check via node
        result = subprocess.run(
            ['node', '--input-type=module', '-e', f'import("{path}")'],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0, result.stderr
    finally:
        os.unlink(path)
```

**Language detection in determinex_swebench_agent.py**:
```python
def _detect_repo_language(repo_path: str) -> str:
    """Detect primary language of repo for routing cloak + validator."""
    exts = Counter()
    for root, _, files in os.walk(repo_path):
        for fname in files:
            _, ext = os.path.splitext(fname)
            exts[ext.lower()] += 1
    # Priority order: most distinctive extensions first
    if exts.get('.go', 0) > 5:
        return 'go'
    if exts.get('.ts', 0) > 5 or exts.get('.tsx', 0) > 5:
        return 'typescript'
    if exts.get('.js', 0) > 5:
        return 'javascript'
    return 'python'  # default

def _get_cloak_for_language(lang: str) -> type:
    if lang == 'go':
        return GoCloakContext
    if lang in ('typescript', 'javascript'):
        return TypeScriptCloakContext
    return PythonCloakContext  # existing
```

**The Architect plan re-obfuscation fix** (open item from ARCHITECTURE.md):
This is critical for Go/TS where the Architect may use more descriptive identifiers.
The fix: after Architect generates its plan, run `IssueTextTransformer` on the plan text
before passing it to the Builder. This is language-agnostic and should be applied to
Python too (it's listed as a known hole in all configs).

---

### Tier 3 — LiveCodeBench (Algorithm Invention, Not Bug Fixing)

#### What It Tests
LiveCodeBench problems are LeetCode-style: given a problem description, write a function
that passes all test cases. No existing codebase. No patches. Pure algorithm invention.

This is a fundamentally different capability from SWE-bench:
- SWE-bench: "here is broken code, here is the error, fix it"
- LiveCodeBench: "here is a problem description, write the solution from scratch"

**Our current system's fit**: The Hive Mind's `new-session` mode is designed EXACTLY for
write-from-scratch tasks. This is the Gen 4 pipeline: spec → Architect generates DAG →
Builder implements each step → Compiler Oracle validates. The SWE-bench harness is the
*exception* — it wraps the Hive in a patch-generation interface. For LiveCodeBench, we
use the Hive directly.

**The critical difference**: LiveCodeBench has a hidden test oracle. We don't know if
`py_compile` passing means the solution is correct. We need execution-based validation:
run the solution against the provided example test cases, and against our own stress tests.

#### Execution Oracle for LiveCodeBench

The existing Python validator only does `ast.parse()` + `exec()`. For LiveCodeBench,
we need:

```python
# scripts/validators/execution_oracle.py

import subprocess, tempfile, json, os, sys
from typing import Any

def run_solution_against_tests(
    solution_code: str,
    test_cases: list[dict],  # [{'input': ..., 'expected_output': ...}]
    language: str = 'python',
    timeout_seconds: float = 10.0,
) -> tuple[bool, str]:
    """
    Execute solution_code against each test case.
    Returns (all_passed, error_message).
    """
    if language == 'python':
        return _run_python_solution(solution_code, test_cases, timeout_seconds)
    elif language == 'cpp':
        return _run_cpp_solution(solution_code, test_cases, timeout_seconds)
    return False, f"Unsupported language: {language}"

def _run_python_solution(code: str, tests: list[dict], timeout: float) -> tuple[bool, str]:
    with tempfile.NamedTemporaryFile(suffix='.py', mode='w', delete=False) as f:
        # Inject test harness
        test_runner = '''
import json, sys

# User solution
{code}

# Test runner
results = []
for tc in {tests}:
    try:
        actual = solution(**tc['input']) if isinstance(tc['input'], dict) else solution(tc['input'])
        passed = actual == tc['expected_output']
        results.append({{'passed': passed, 'actual': actual, 'expected': tc['expected_output']}})
    except Exception as e:
        results.append({{'passed': False, 'error': str(e)}})

print(json.dumps(results))
'''.format(code=code, tests=json.dumps(tests))
        f.write(test_runner)
        path = f.name
    
    try:
        result = subprocess.run(
            [sys.executable, path],
            capture_output=True, text=True, timeout=timeout
        )
        if result.returncode != 0:
            return False, result.stderr
        outputs = json.loads(result.stdout)
        failures = [o for o in outputs if not o.get('passed')]
        if failures:
            return False, f"{len(failures)}/{len(outputs)} tests failed. First failure: {failures[0]}"
        return True, f"All {len(outputs)} tests passed"
    except subprocess.TimeoutExpired:
        return False, f"Time limit exceeded ({timeout}s)"
    except json.JSONDecodeError as e:
        return False, f"Malformed output: {e}"
    finally:
        os.unlink(path)
```

#### LiveCodeBench Harness

```python
# scripts/determinex_livecode_agent.py (new file)

"""
LiveCodeBench solver — uses the Hive Mind new-session pipeline.
Input: problem description + function signature + example test cases
Output: solution code that passes all test cases
"""

from scripts.determinex_hive import HiveSession
from scripts.validators.execution_oracle import run_solution_against_tests

class LiveCodeAgent:
    def __init__(self, config: str = 'd'):
        self.config = config
    
    def solve(self, problem: dict) -> dict:
        """
        problem format (from LiveCodeBench):
        {
            'question_id': str,
            'title': str,
            'description': str,
            'starter_code': str,  # function signature to fill in
            'test_cases': [{'input': ..., 'expected_output': ...}],
            'difficulty': 'easy' | 'medium' | 'hard',
        }
        """
        # Convert LCB problem to Determinex spec format
        spec = self._problem_to_spec(problem)
        
        # Use Hive write-from-scratch mode
        session = HiveSession.new_session(spec=spec, lang='python')
        session.generate_dag()
        result = session.run_session()
        
        # Extract generated solution from workspace
        solution_code = self._extract_solution(result, problem['starter_code'])
        
        # Validate against test cases
        passed, msg = run_solution_against_tests(
            solution_code,
            problem['test_cases'],
            language='python',
        )
        
        return {
            'question_id': problem['question_id'],
            'solution': solution_code,
            'passed': passed,
            'message': msg,
        }
    
    def _problem_to_spec(self, problem: dict) -> str:
        return f"""# {problem['title']}

## Goal
{problem['description']}

## Starting Point
```python
{problem['starter_code']}
```

## Constraints
- Implement the function to pass all test cases
- Time complexity should be optimal for the problem constraints
- Language: Python

## Files
- solution.py — the complete solution
"""
```

#### Key Insight: LiveCodeBench Exposes Our Architect's Write-From-Scratch Quality

SWE-bench only measures patch quality — the Architect identifies a file, the Builder modifies
a few lines. LiveCodeBench forces the Architect to decompose an algorithm problem into
implementation steps from scratch. This will expose gaps in the Architect's planning quality
that SWE-bench masks.

Expected performance gap: likely much worse than SWE-bench Lite. The 1.5B Builder was
trained primarily on fix patterns. Algorithm invention requires a different kind of reasoning.
This is where the Rosetta Stone + Leviathan escalation path becomes critical — the 1.5B model
hits its ceiling fast on hard algorithm problems; Leviathan (DeepSeek-Coder-V2) as escalation
is the backstop.

---

### Tier 4 — BigCodeBench (Library Ecosystem Knowledge)

#### What It Tests
1,000+ tasks that require writing functions using specific Python library APIs.
Example: "write a function that reads a CSV, groups by column X, and returns the top 3 groups by count."
The test harness executes the code with all libraries available.

**Key difference from SWE-bench**: The challenge is library API knowledge, not bug diagnosis.
The code environment has numpy, pandas, sklearn, requests, PIL, etc. all available.

**Key difference from LiveCodeBench**: These are not algorithm problems — they're practical
code-generation tasks. The Hive's existing Python validator is weak here because it only
checks syntax. We need Docker execution with the full library environment.

#### BigCodeBench Execution Environment

BigCodeBench provides a Docker image (`bigcode/bigcode-bench`) with all dependencies.
The SWE-bench Docker infrastructure we already have can be reused:

```python
# scripts/determinex_bigcode_agent.py (new file)

import subprocess, json

BIGCODE_DOCKER_IMAGE = "bigcode/bigcode-bench:latest"

def run_bigcode_solution(task_id: str, solution_code: str, test_code: str) -> tuple[bool, str]:
    """Execute solution in BigCodeBench Docker image."""
    container_name = f"determinex.bigcode.{task_id}"
    
    # Mount solution + test harness into container
    full_code = solution_code + "\n\n" + test_code
    
    result = subprocess.run([
        'wsl', '-d', 'Ubuntu', 'docker', 'run', '--rm',
        '--name', container_name,
        '--memory', '2g',
        '--cpus', '2',
        BIGCODE_DOCKER_IMAGE,
        'python', '-c', full_code
    ], capture_output=True, text=True, timeout=60)
    
    return result.returncode == 0, result.stdout + result.stderr
```

**Cloak considerations for BigCodeBench**: Not applicable. BigCodeBench tasks are isolated
functions — there's no existing codebase to obfuscate. Cloak's privacy guarantee is about
hiding proprietary identifiers from existing repos. BigCodeBench is pure generation.

---

### Tier 5 — SWE-lancer (Freelance Work Simulation)

#### What It Tests
1,400+ tasks from Upwork with real dollar values. Mix of:
- **IC tasks** (764): Implement a specific feature or fix a specific bug. Evaluated by whether
  the implementation passes the client's test suite.
- **Management tasks** (724): Given multiple candidate implementations, pick the best one.
  Evaluated by whether the chosen implementation would succeed in production.

**IC bug fix tasks** → Map directly to our existing SWE-bench harness. These are bug fixes.

**IC feature tasks** → Map to Hive new-session mode. Write new code from scratch to spec.

**Management tasks** → Completely new capability. Requires evaluating multiple code implementations
and picking the best one. This is the Monitor's job, not the Builder's.

#### SWE-lancer Management Tasks: The Monitor as Evaluator

This is where the Hive architecture's Monitor role becomes genuinely useful outside training.
Management tasks send multiple implementations to the Monitor and ask it to rank them.

The Observer (determinex-observer-v6-dsl) was trained to detect hallucinations and correctness issues.
For management tasks, we'd use it as a code reviewer:

```python
def solve_management_task(implementations: list[str], spec: str, test_suite: str) -> int:
    """Return index of best implementation using Monitor + Compiler Oracle."""
    scores = []
    for impl in implementations:
        # 1. Compiler Oracle: does it even compile?
        compile_ok, _ = python_validator.validate_python(impl)
        if not compile_ok:
            scores.append(0.0)
            continue
        
        # 2. Run test suite
        test_ok, _ = run_tests(impl, test_suite)
        
        # 3. Monitor quality score
        monitor_verdict = observer_api.score(impl, spec)
        
        # 4. Composite score
        score = (0.5 * int(test_ok)) + (0.3 * monitor_verdict['confidence']) + (0.2 * int(compile_ok))
        scores.append(score)
    
    return scores.index(max(scores))
```

#### Dollar Value Metric

SWE-lancer reports scores in dollars earned (out of $1M total). This is a different reporting
format from pass/fail. The mapping: if you solve a $500 task correctly, you earn $500. Claude
3.5 Sonnet earned $208K / $500K. The headline metric is meaningful to non-technical stakeholders.

---

### Tier 6 — OSWorld / WebArena (Computer Use — New Architecture Required)

This is the honest assessment: **Determinex cannot do these benchmarks today.** They require:

1. **Screenshot input** — Our system takes text (code + issue description). OSWorld sends screenshots.
2. **GUI action output** — Our system generates diffs. OSWorld requires click/type/scroll/drag.
3. **Multi-app context** — OSWorld tasks span desktop apps, browsers, terminal, file system.
4. **Long-horizon planning** — OSWorld tasks have 15-50 action steps. Our DAG is designed for
   code generation steps, not OS interaction steps.

**What we'd need to build:**

```
New Layer: Computer Use Agent
├── ScreenReader — parse screenshot → structured state
├── ActionPlanner — given state + goal → next action (click/type/scroll)
├── ActionExecutor — pyautogui or win32api for actual execution
└── VerificationLoop — take new screenshot, check if goal state reached
```

The Tauri frontend (Gen 3) runs on the local machine and has OS access. The Action Executor
would be a Tauri IPC command that calls OS APIs. The ScreenReader would use the Anthropic
computer-use API (already available in Claude 3.5 Sonnet and higher).

**This is a Phase 4 capability** — after Phase 3 (async build loop, KV cache broadcast)
is shipped and validated. Don't build this until the existing pipeline is mature.

**What it would unlock**: OSWorld at 82%+ SOTA means being on the frontier of computer use.
This directly enables the "AI runs your entire development workflow" vision — not just coding,
but running terminals, browsers, git, deployment pipelines.

---

## What the Smoke7 Failures Taught Us (Cross-Benchmark Lessons)

The smoke7 run exposed patterns that will recur across ALL benchmarks. These are now in
`scripts/coding_laws.md` as LAW-220 and LAW-221, but the principle generalizes:

### The Two-Bug Pattern (django-15202)
**Lesson**: Real bugs often have a primary manifestation (the ValueError at line 130) and
a secondary manifestation that appears only at a different code path (the TypeError at line 142).
The Architect identifies the first one. The second one only appears in test cases that hit a
different execution path. This will recur constantly.

**Fix for the pipeline**: The Monitor needs to run test cases after patch application and
inject test failure context into the retry loop — not just compiler errors. For Python, this
means running `pytest -x` after patch application (we already do this in the Hive), not just
`py_compile`. The test runner result IS the correct oracle for Python.

**For all benchmarks**: Any benchmark using execution-based validation (LiveCodeBench,
BigCodeBench, SWE-lancer) must route test failure messages back into the Architect's retry
context. The "Rust/Go only error injection" restriction in executor.py is too conservative —
Python test failures are also surgical enough to guide retries when they include file+line info.

### The Regex Blindness Pattern (sphinx-8506)
**Lesson**: Single-character changes in regex patterns (`[^\s=[]+` → `[^\s=]+`) are nearly
impossible for the Architect to reason about from issue text alone. The Architect can identify
the file but returns 0 steps because it can't see the connection.

**Fix for the pipeline**: The coding_laws.md injection approach is the right pattern. As we
encounter these cases, we codify the exact fix. Over time, the laws library becomes a learned
pattern database that bootstraps the Architect's weak spots.

**Cross-benchmark implication**: LiveCodeBench hard problems will have similar "single insight
changes" — problems where the key realization is small but non-obvious. The laws library
approach scales: after seeing enough failures, we codify the recurring patterns.

### The Empty Plan Failure Mode
**Lesson**: The Architect (Claude Sonnet 4.6 in Config D) returns 0 steps when:
1. The fix is a subtle pattern it can't connect to the issue text
2. The issue is described ambiguously
3. The relevant file is identified but the exact change isn't obvious from the structure

**For SWE-bench Pro Go/TS**: This failure mode will be more frequent. Go and TypeScript issues
often describe type-system failures that require understanding Go/TS semantics deeply. The
Architect's training on Python patterns doesn't transfer cleanly to Go's interface satisfaction
or TypeScript's type narrowing.

**Mitigation**: Shadow compilation (already implemented in agent.py) — run the test before
patching to capture the actual error, inject into Architect. For Go type errors, the compiler
error is VERY surgical (`./file.go:42: cannot use x (type int) as type string in assignment`).
This makes Go harder than Python in the "locate the bug" phase but easier in the "implement
the fix" phase once located.

---

## The Cloak Discovery Backlog (For Every New Language)

From `docs/PROJECT_CLOAK.md` and the smoke7 session, these are the hard-won Cloak lessons
that MUST be re-validated when extending to Go and TypeScript:

1. **Context Paradox**: File discovery always runs on REAL text. Only API calls get cloaked.
   For Go/TS, `locate_relevant_files()` uses regex search — this is already language-agnostic.
   No change needed here.

2. **Region Threshold = 0**: Always use region mode. Builder should never receive a full file.
   This is already `_REGION_THRESHOLD = 0`. Language-agnostic.

3. **Line-Number Stripping**: Builder echoes back the `"  67 | code"` prefix. The strip
   logic must be outside any language-specific branch. Already fixed. Language-agnostic.

4. **Architect Plan Re-Obfuscation**: Currently the Architect generates plans with REAL names
   visible to the Builder's context. Fix: run `IssueTextTransformer` on the plan text before
   passing to Builder. This is the #1 open item for Python and applies to all languages.

5. **Star Import Holes**: Python-specific (`from x import *`). Go has explicit imports — no
   star imports possible. Go has zero star-import holes. TypeScript has `import *` but it's
   less common in module-oriented code. For Go: this class of hole doesn't exist.

6. **Semantic Key**: The functional glossary (`x_1234: session cache (private attr)`) is
   generated from identifier name word-splitting. This works for any naming convention
   (snake_case Python, camelCase Go/TS). Language-agnostic.

---

## Implementation Sequence

### Now (eval running — do after smoke7 completes)
1. Run full hardened SWE-bench Lite (300 instances) with corrected patches (django-15202, sphinx-8506 fixed)
2. Get final smoke7 score, update CLAUDE.md and white paper

### Next (1-2 days)
3. Fix Architect plan re-obfuscation — `IssueTextTransformer` on plan text before Builder
4. Run SWE-bench Verified (500 instances) — zero new code, immediate credibility improvement
5. Fix Python test failure injection in executor.py (extend error injection to Python when pytest output available)

### Week 1-2
6. **Go Cloak extension** — `GoLanguageCloak` class, stdlib manifest, regex-based identifier extraction
7. **TypeScript validator** — `tsc --noEmit` wrapper in `scripts/validators/typescript_validator.py`
8. Run SWE-bench Pro subset (100 instances, Python only) — validate harness
9. Run SWE-bench Pro subset (100 instances, Go only) — validate Go Cloak

### Week 2-3
10. **LiveCodeBench harness** — `determinex_livecode_agent.py`, execution oracle, Hive integration
11. Run LiveCodeBench Easy + Medium (150 instances) — get write-from-scratch baseline
12. Analyze LiveCodeBench Hard failures — calibrate Leviathan escalation threshold

### Week 3-4
13. **BigCodeBench harness** — Docker execution, BigCodeBench dataset integration
14. Run BigCodeBench Complete subset (500 tasks) — library ecosystem score
15. SWE-bench Pro full run (1,865 instances, all languages) — the headline number

### Ongoing
16. Coding laws library expansion — each new benchmark reveals new recurring patterns
17. White paper numbers update with each new benchmark result

---

## Capability Inventory (Honest Assessment)

| Benchmark | Determinex Capability | Gap | Blocker |
|-----------|-------------------|-----|---------|
| SWE-bench Lite | ✅ Running | Score vs SOTA | Architecture quality |
| SWE-bench Verified | ✅ Drop-in | Score | None |
| SWE-bench Full | ✅ Drop-in | Scale/time | None |
| SWE-bench Verified Hard | ✅ Drop-in | Score (hard) | Architect quality |
| SWE-bench Pro Python | ✅ Drop-in | Score | None |
| SWE-bench Pro Go | 🔶 Needs Go Cloak | Cloak extension | 1-2 days |
| SWE-bench Pro TypeScript | 🔶 Needs TS Cloak | Cloak + tsc validator | 2-3 days |
| LiveCodeBench Easy | 🔶 Needs harness | Write-from-scratch | 1 day |
| LiveCodeBench Hard | 🔶 Needs harness + Leviathan | Algorithm quality | 2-3 days |
| BigCodeBench | 🔶 Needs Docker harness | Library knowledge | 2-3 days |
| SWE-lancer IC bugs | ✅ Near drop-in | Score | Minor harness |
| SWE-lancer IC features | 🔶 Needs Hive integration | Feature scope | 3-5 days |
| SWE-lancer Management | 🔶 Needs Monitor-as-evaluator | New mode | 2-3 days |
| OSWorld | ❌ Architecture gap | Computer use layer | Weeks |
| WebArena | ❌ Architecture gap | Browser automation | Weeks |
| USACO Hard | ❌ Algorithm ceiling | Model capability | Months |
| FrontierMath | ❌ Wrong domain | Math reasoning | N/A |

---

## The White Paper Score Hierarchy (What We're Building Toward)

The paper's headline is the privacy sovereignty claim. The score hierarchy supports it:

```
B-Uncloaked:  X%  ← DeepSeek alone, no privacy (SWE-bench Lite baseline)
B-Cloaked:    Y%  ← X + privacy sovereignty (the cost of Cloak)
D-Cloaked:    Z%  ← Z > Y (the value of Claude as Architect, still private)

Same hierarchy on SWE-bench Pro:
B-Uncloaked-Pro:  A%  ← multi-language baseline
D-Cloaked-Pro:    B%  ← privacy-sovereign multi-language

LiveCodeBench:
D-NuclearHybrid-LCB: C%  ← Hive write-from-scratch under Cloak
```

Each benchmark tier adds a new dimension to the claim:
- Lite: privacy-sovereign bug fixing (Python)
- Pro: privacy-sovereign multi-language bug fixing
- LiveCodeBench: privacy-sovereign algorithm generation
- BigCodeBench: privacy-sovereign library-ecosystem coding

Together these paint a complete picture: **Determinex resolves software tasks across all major
benchmark paradigms while the cloud AI remains blind to every proprietary identifier.**

---

*Document: BENCHMARK_EXPANSION.md*
*Author: Ryan Gurganious / Lunarian Data Systems*
*Status: Living document — update as scores come in*

