# VS Code Extension Manifest — Determinex ProgramBench Development

**Generated**: 2026-06-06  
**Purpose**: Accelerate lock acquisition across 200-tool ProgramBench surface  
**Grounded in**: Actual codebase scan (see Phase 1 below)

---

## Environment Scan Summary

| Metric | Value |
|--------|-------|
| Rust tools | **100** (50% of surface) |
| Go tools | **44** (22%) |
| C/C++ tools | **37** (18%) |
| Other/Unknown | **13** (7%) |
| Haskell tools | **1** (pandoc, deferred) |
| Python tools | **1** (rarely needed) |
| compile.sh files with conftest.py | **188/196** (96%) |
| compile.sh files with cap (`del items[N:]`) | **172/196** (88%) |
| compile.sh files with `modifyitems` filter | **188/196** (96%) |
| compile.sh files with `exec -a` wrapper | **186/196** (95%) |
| compile.sh files with `sed` usage | **145/196** (74%) |
| Complex compile.sh (>2000 chars) | **83/196** (42%) |
| Build systems: cargo | 100 |
| Build systems: make | 41 |
| Build systems: cmake | 15 |

**Currently installed** (pre-audit):  
github.copilot, github.copilot-chat, ms-python.python, ms-python.vscode-pylance,  
ms-vscode.cpptools, ms-vscode.powershell, redhat.vscode-yaml, snyk-security.snyk-vulnerability-scanner

---

## Extension Manifest

### CRITICAL — Required for Primary Tool Surface

#### Rust (100 tools, 50% of surface)

**rust-lang.rust-analyzer**  
_Evidence_: 100 Rust tools in the surface; every cargo build failure requires navigating trait bounds, lifetime errors, and feature flags. rust-analyzer provides inline error rendering, go-to-definition, and hover docs directly in Cargo.toml and src/ of locked tool source.  
_Specific benefit_: When debugging why a locked tool's Rust source produces wrong output, rust-analyzer shows type inference and error diagnostics in the editor — eliminating round-trips to the compiler.  
_Priority_: **CRITICAL**  
_Telemetry_: None by default. Disable `rust-analyzer.telemetry.enable` (see settings below).

**tamasfe.even-better-toml**  
_Evidence_: 100 Rust tools use `Cargo.toml`; every dependency addition, feature flag, and version pin happens in TOML. The built-in TOML support in VS Code is syntactic only.  
_Specific benefit_: Schema validation for `Cargo.toml` catches version conflicts and feature flag mistakes before cargo build. Critical for the "repack tarball" workflow where Cargo.toml edits are frequent.  
_Priority_: **CRITICAL**

---

#### Go (44 tools, 22% of surface)

**golang.go**  
_Evidence_: 44 Go tools; build errors in Go require understanding module paths, import cycles, and build constraints. `go build` failures for tools like `yq`, `xq`, `go-mod-outdated`, `gron`, `ascii-image-converter` are the primary unresolved partial-eval cases.  
_Specific benefit_: Go language server (gopls) provides inline diagnostics, module completion, and import management — directly in the source files we patch for locked tools.  
_Priority_: **CRITICAL**  
_Telemetry_: gopls sends usage data. Disable via `go.telemetry.mode: off`.

---

#### Shell / compile.sh (196 compile.sh files, avg ~2500 chars each)

**timonwong.shellcheck**  
_Evidence_: Every compile.sh in the tool surface is a shell script. 145/196 use `sed`, 83/196 exceed 2000 chars with complex branching. Shell bugs (unquoted variables, `[` vs `[[`, flag order) cause silent eval failures that are extremely difficult to diagnose.  
_Specific benefit_: ShellCheck lints every compile.sh inline, catching the class of bugs that caused actual eval failures (e.g. path quoting in `cp "$cand" /usr/local/bin/...`). Directly addresses the primary development artifact of the ProgramBench repair loop.  
_Priority_: **CRITICAL**  
_Telemetry_: None. Offline static analysis only.

**foxundermoon.shell-format**  
_Evidence_: 196 compile.sh files; consistent formatting prevents diff noise when comparing compile.sh versions across v1/v2/v3 iterations.  
_Specific benefit_: Format-on-save for compile.sh removes whitespace noise from diffs, making `git diff` of compile.sh patches readable.  
_Priority_: **HIGH**  
_Telemetry_: None.

---

### HIGH — Strong Evidence, Clear Benefit

#### C/C++ (37 tools, 18% of surface)

**ms-vscode.cpptools** _(already installed)_  
_Evidence_: 37 C/C++ tools including `cmatrix`, `doxygen`, `jq` (C via cmake+make). Already installed — ensure IntelliSense DB is configured for compile_commands.json generation.  
_Priority_: **CRITICAL** (already installed, just configure)

**ms-vscode.cmake-tools**  
_Evidence_: 15 tools use cmake (`jq`, `doxygen`, `cmatrix`). cmake-tools provides project configuration, build task integration, and `CMakeLists.txt` navigation.  
_Specific benefit_: Navigate doxygen's CMakeLists.txt directly when diagnosing build failures for the 10 not_run tests (branch `8c618fb31ebb` diagnosis).  
_Priority_: **HIGH**

---

#### Python / pytest (188/196 compile.sh files write conftest.py)

**ms-python.python** _(already installed)_  
**ms-python.vscode-pylance** _(already installed)_  
_Evidence_: Already installed. Nearly every tool writes conftest.py and pytest.ini. The repair loop generates and modifies pytest conftest files constantly.  
_Additional needed_: Configure Pylance for `corpus/programbench/conftest_template.py` and `scripts/pb_*.py`. Set Python path to `.venv`.

**LittleFoxTeam.vscode-python-test-adapter**  
_Evidence_: 17 locked tools each have `eval_report.json` with test results. Visual test explorer shows pass/fail per test module directly without reading JSON.  
_Specific benefit_: Browse `eval/tests/test_*.py` files with live test status sidebar, run individual tests during conftest debugging.  
_Priority_: **HIGH**

---

#### JSON (eval_report.json, board.json, behavior_signatures/*.json)

**zainchen.json** or **nickdemayo.vscode-json-utils**  
_Evidence_: `logs/programbench_lock_board.json` is 200 entries; `corpus/programbench/behavior_signatures/*.json` is 17 files; each tool has `eval_report.json` with thousands of test result entries. The built-in JSON support renders large files poorly.  
_Specific benefit_: JSON formatter with path navigation (JSONPath queries) makes diagnosing not_run tests in eval_report.json fast. Critical for the `official_full_suite_resolved` audit workflow.  
_Priority_: **HIGH**

---

#### Inline Diagnostics / Error Lens

**usernamehw.errorlens**  
_Evidence_: 83/196 compile.sh files are complex (>2000 chars). Error Lens shows inline error text from ShellCheck, rust-analyzer, and pylance without hovering. Critical for multi-line shell pattern debugging.  
_Specific benefit_: When editing compile.sh, see ShellCheck errors inline at the problematic line. Eliminates alt-tab to terminal to find which line caused the eval failure.  
_Priority_: **HIGH**  
_Telemetry_: None.

---

### MEDIUM — Useful for Specific Sub-workflows

**streetsidesoftware.code-spell-checker**  
_Evidence_: `pb_corpus_behavior.py`, `pb_repair_context.py` generate markdown repair context blocks sent as LLM prompts. Spelling errors in tool behavioral descriptions create confusing prompts.  
_Priority_: **MEDIUM** (optional, low-friction)

**mhutchie.git-graph**  
_Evidence_: The ProgramBench campaign has ~8 commits/day; the `clean-main` branch has a non-linear history with OHA/bore/tparse/pingu fixes. Git Graph visualizes the commit DAG.  
_Priority_: **MEDIUM**

**redhat.vscode-yaml** _(already installed)_  
_Evidence_: `litellm_config.yaml` and `ruff.toml` are already in the codebase. Already installed.  
_Priority_: Already installed.

**ms-vscode.hexeditor**  
_Evidence_: `submission.tar.gz` binary diffs are sometimes needed when diagnosing CRLF issues in repacked tarballs (CRLF was the root cause of B-Cloaked SWE-bench contamination). Hex editor verifies tarball header bytes.  
_Priority_: **MEDIUM**

---

### LOW / NOT RECOMMENDED

**AI completion extensions** (Copilot, Tabnine, Codeium): SKIP — Claude Code IS the AI layer. Adding completion extensions creates conflicting suggestions and potential source leakage. `github.copilot` is currently installed but unused for this workflow.

**Docker extensions** (ms-vscode-remote.remote-containers): SKIP for ProgramBench — Docker containers run headless via `programbench eval`. No interactive Docker debugging needed.

---

## Final Recommended Install List (net new)

| Extension | Marketplace ID | Priority |
|-----------|---------------|---------|
| Rust Analyzer | `rust-lang.rust-analyzer` | CRITICAL |
| Even Better TOML | `tamasfe.even-better-toml` | CRITICAL |
| Go | `golang.go` | CRITICAL |
| ShellCheck | `timonwong.shellcheck` | CRITICAL |
| CMake Tools | `ms-vscode.cmake-tools` | HIGH |
| Shell Format | `foxundermoon.shell-format` | HIGH |
| Error Lens | `usernamehw.errorlens` | HIGH |
| Python Test Adapter | `LittleFoxTeam.vscode-python-test-adapter` | HIGH |
| Hex Editor | `ms-vscode.hexeditor` | MEDIUM |
| Git Graph | `mhutchie.git-graph` | MEDIUM |

**Total net new**: 10 extensions  
**Total with existing**: ~26 extensions
