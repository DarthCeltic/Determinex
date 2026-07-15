# Determinex Windows Evaluation Playbook

**Purpose**: Benchmark AI models for Windows-native correctness. Quantify Linux-ism injection rate, Windows API literacy, and functional portability. Feed results back into Determinex's training pipeline to stop models from hallucinating Unix conventions on Windows tasks.

---

## Why This Exists

Every major AI model — GPT-4o, Claude, DeepSeek, Gemini — confidently writes `apt install`, `/tmp/`, `chmod 755`, and `~/` when asked to solve Windows problems. This isn't a minor UX annoyance; it breaks production deployments, confuses Windows users, and reflects a fundamental training data imbalance (GitHub is ~90% Unix-oriented).

Determinex's Windows Literacy suite measures this failure mode precisely and generates labeled training data to fix it.

---

## Suite Components

| Script | What It Tests | Output |
|--------|--------------|--------|
| `win_bench_runner.py` | PowerShell Windows literacy (22 rubric tasks) | `logs/windows_bench/TIMESTAMP_MODEL.json` |
| `ps_aishell_eval.ps1` | PowerShell with live Windows Sandbox execution | `logs/windows_bench/TIMESTAMP_ps_MODEL.json` |
| `deepeval_humaneval.py` | HumanEval portability (164 Python problems) | `logs/windows_bench/TIMESTAMP_humaneval_MODEL.json` |
| `swebench_live_windows.py` | SWE-bench patches for Windows-illiteracy | `logs/windows_bench/TIMESTAMP_swebench_*/` |

---

## Quick Start

### Phase 1 — Establish Baselines

Run against all models to collect data:

```bash
# PowerShell rubric benchmark
python scripts/benchmarks/windows/win_bench_runner.py --model all

# HumanEval portability (no sandbox needed — pure static analysis)
python scripts/benchmarks/windows/deepeval_humaneval.py --model all --skip-functional

# HumanEval full (with functional test execution)
python scripts/benchmarks/windows/deepeval_humaneval.py --model all --limit 164
```

From PowerShell (requires `DEEPSEEK_API_KEY`, `ANTHROPIC_API_KEY`, or `OPENAI_API_KEY`):

```powershell
# Static rubric only (fast, no sandbox)
.\scripts\benchmarks\windows\ps_aishell_eval.ps1 -Model deepseek -SkipExecution

# With Windows Sandbox execution (requires Sandbox feature enabled)
.\scripts\benchmarks\windows\ps_aishell_eval.ps1 -Model claude
```

### Phase 2 — Extract Golden Test Set

After collecting ≥2 model runs, derive the minimal tests that reliably catch Windows-illiteracy:

```bash
python scripts/benchmarks/windows/win_bench_runner.py --extract-golden
```

Output: `logs/windows_bench/golden_test_set.json` — tasks where ≥50% of models failed or ≥30% produced Linux-isms.

---

## Enabling Windows Sandbox

Windows Sandbox is an optional feature required for live PowerShell execution in `ps_aishell_eval.ps1`.

```powershell
# Enable (requires reboot)
Enable-WindowsOptionalFeature -FeatureName "Containers-DisposableClientVM" -Online

# Verify
Get-WindowsOptionalFeature -Online -FeatureName "Containers-DisposableClientVM"
```

Without Sandbox, use `-SkipExecution` for static rubric analysis only. The static rubric is ~85% predictive of execution failures for well-designed tasks.

---

## Scoring System

### PowerShell Rubric (`win_bench_runner.py`)

Each task has a rubric: a list of `(regex, required, description)` checks.

- `required=True`: pattern MUST match (e.g., `Join-Path` must appear)
- `required=False`: pattern MUST NOT match (e.g., `/tmp/` must not appear)

**Task score** = `passed_checks / total_checks` (0.0–1.0)

**Weighted system score** = `sum(score × weight) / sum(weight)`

Weights: 3 = critical (path handling, env vars, registry), 2 = important, 1 = nice-to-have

### Linux-ism Count (primary failure metric)

Count of Unix-specific constructs appearing in model output. Zero is the target.

Current 21-pattern detection list covers:
`/usr/`, `/home/`, `~/`, `/etc/`, `/tmp/`, `apt install`, `yum install`, `brew install`, `dnf install`, `chmod`, `chown`, `ln -s`, `pkill/killall`, `export VAR=`, `systemctl`, `service start/stop`, `iptables/ufw`, `sed -i`, `grep -r`, `inotifywait/fswatch`, `#!/bin/bash`

### HumanEval Scoring (`deepeval_humaneval.py`)

Two dimensions per problem:
1. **Functional** — does the generated code pass HumanEval's test suite?
2. **Portability** — zero Linux-isms, no hardcoded Unix paths (pattern checks)

**Portability score** = `1.0 − (linux_ism_count × 0.1)` applied to base rubric score

### PowerShell + Sandbox (`ps_aishell_eval.ps1`)

**Final score** = rubric score × 0.7 + exec_passed × 0.3

Status thresholds: PASS ≥ 0.9, WARN ≥ 0.6, FAIL < 0.6

---

## Task Categories

| Category | Tasks | Critical Weight | What Fails |
|----------|-------|----------------|------------|
| `path` | 4 | 3 | Unix home, `/tmp/`, no `Join-Path` |
| `envvar` | 3 | 3 | `export` instead of `$env:`, `:` path separator |
| `process` | 3 | 2 | `ps aux`, `kill -9`, Python `subprocess` |
| `registry` | 2 | 3 | `/etc/os-release` instead of `HKLM:` |
| `tools` | 3 | 2-3 | `apt install`, `systemctl`, `iptables` |
| `syntax` | 3 | 2-3 | bash `for` loop, `sed -i`, `grep -r` |
| `filesystem` | 3 | 1-3 | `chmod`, `ln -s`, `inotifywait` |

---

## Interpreting Results

### Windows Literacy Score

| Score | Meaning |
|-------|---------|
| ≥ 95% | Windows-native: ready for Windows deployment |
| 80–95% | Mostly correct: minor Unix habits, catchable by review |
| 60–80% | Significant issues: likely to break Windows deployments |
| < 60% | Windows-illiterate: untrusted for Windows tasks |

### Linux-ism Rate (per task)

| Rate | Meaning |
|------|---------|
| 0.0 | Perfect Windows hygiene |
| 0.1–0.3 | Occasional Unix slips |
| 0.5+ | Model not Windows-aware |
| 1.0+ | Model actively writing Linux code |

---

## Feedback Loop Integration

### Into SWE-bench Agent

When `determinex_swebench_agent.py` generates a patch, the Windows ism detector runs automatically:

```python
from scripts.benchmarks.windows.swebench_live_windows import detect_linux_isms

patch = generate_patch(instance, model)
isms = detect_linux_isms(patch)
if isms and is_windows_repo(instance):
    # Inject warning into next attempt prompt
    retry_prompt = f"WARN: patch contains {len(isms)} Linux-isms: {isms}. Fix for Windows."
```

### Into Training Flywheel

Failed tasks (score < 0.6) become SFT training pairs:

```
input:  <task prompt>
output: <correct Windows-native PowerShell>
```

The golden test set (`--extract-golden`) provides the curated discrimination set for:
1. Fine-tuning C1/C3/C7 on Windows tasks
2. Regression testing after each retrain (score must not drop)
3. Determinex's onboard sandbox sidecar (eval without Docker)

---

## Onboard Sandbox Sidecar (Phase 2)

Once baseline golden tests are extracted, the sidecar replaces Docker for ongoing quality checks:

1. **Trusted execution**: golden scripts are known-good; sidecar just re-runs to verify model outputs
2. **No Docker overhead**: Windows Sandbox spins up in ~5s vs Docker's 30-60s
3. **Local-first**: no external dependencies, works air-gapped
4. **Integration**: `determinex_hive.py` calls sidecar check before accepting any PowerShell output

Architecture:

```
Model output (PS code)
    → Linux-ism scan (instant, regex)
    → Golden rubric check (instant, regex)
    → Windows Sandbox execution (5-10s, for high-risk admin code)
    → PASS: include in response
    → FAIL: inject error + retry (same compile-gate loop as C code)
```

---

## Environment Variables

```
DEEPSEEK_API_KEY    — for --model deepseek
ANTHROPIC_API_KEY   — for --model claude
OPENAI_API_KEY      — for --model gpt
```

Local model (`--model local`) requires Ollama running at `http://localhost:11434`.

---

## Adding New Tasks

Edit `windows_literacy_tasks.py`. Follow the schema:

```python
{
    "id": "unique_id",          # snake_case, category_verb_NN
    "category": "path",         # path|envvar|process|registry|tools|syntax|filesystem
    "weight": 3,                # 1=nice, 2=important, 3=critical
    "prompt": "...",            # user-facing ask, present tense, specific
    "rubric": [
        (r"pattern", True,  "MUST: description"),   # required=True
        (r"pattern", False, "MUST NOT: description"), # required=False
    ],
}
```

**Good rubric patterns**:
- Required: specific Windows API (`Join-Path`, `Get-Process`, `HKLM:`)
- Forbidden: equivalent Unix construct (`ln -s`, `ps aux`, `/etc/`)
- Be specific enough that a correct answer can't accidentally fail

**Adding to `ps_aishell_eval.ps1`**: add a hashtable to `$Tasks` with `Id`, `Category`, `Weight`, `Prompt`, `ValidateScript`, `MustContain`, `MustNotContain`.

---

## Result File Schema

### `win_bench_runner.py` output

```json
{
  "model": "deepseek",
  "timestamp": "20260511_143022",
  "tasks_run": 22,
  "weighted_score_pct": 71.3,
  "total_linux_isms": 8,
  "linux_ism_rate": 0.36,
  "pass_count": 14,
  "fail_count": 3,
  "results": [
    {
      "task_id": "path_join_01",
      "category": "path",
      "weight": 3,
      "score": 1.0,
      "weighted_score": 3.0,
      "linux_ism_count": 0,
      "latency_s": 1.4,
      "checks": [...]
    }
  ]
}
```

### `golden_test_set.json` (Phase 2)

```json
{
  "generated": "2026-05-11T14:30:22Z",
  "golden_count": 8,
  "tasks": [
    {
      "task_id": "tools_install_01",
      "category": "tools",
      "weight": 3,
      "fail_rate": 0.75,
      "linux_ism_rate": 0.50,
      "models_tested": 4,
      "prompt": "Write a command to install the 'git' package on Windows."
    }
  ]
}
```

---

*Determinex Windows Eval Playbook · Ryan Gurganious · Lunarian Data Systems · May 2026*
