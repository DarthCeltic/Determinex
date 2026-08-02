#!/usr/bin/env python3
"""
determinex_oracle.py -- The Universal Ground-Truth Oracle
======================================================
Determinex's entire moat is the Compiler Oracle: a deterministic source of ground
truth that the solve loop iterates against, with zero LLM judging. ProgramBench
proved this works for systems languages (Rust/Go/C/C++/Python) because PB SHIPS
the ground truth (a real test suite per task).

To make the IDE "natively know how to fix anything, any system, any language,"
two things must generalize:

  1. The oracle must be PLUGGABLE per language/domain. A tsc type error, a jest
     assertion, a JUnit/Gradle failure, an eslint diagnostic, a SQL planner
     error -- each is just another deterministic ground-truth surface. Register
     it, and the same closed loop (generate -> verify -> adjudicate -> iterate)
     runs unchanged. This is how we reach the JVM/JS-TS/mobile/web worlds that
     PB's language distribution never covers (and that Determinex's own products --
     Hook=Kotlin, SwingSwap/Aide=TypeScript -- actually live in).

  2. Where NO ground truth is shipped (greenfield work, or a domain PB has no
     task for), the system must SYNTHESIZE the oracle: derive an executable
     specification (characterization tests, property tests, type/contract checks,
     golden captures) BEFORE writing the fix, then run the same loop against it.
     "It should make tests for the ones it doesn't have" -- that is this module.

Design contract
---------------
An Oracle answers one question deterministically: does the work-tree satisfy
ground truth right now? It returns an `OracleResult` whose failures are already
normalized into `determinex_adjudicator.Failure` records, so the Adjudicator's
4-step gate runs identically regardless of language or domain.

    oracle = get_oracle("typescript")          # or "rust", "go", "kotlin", ...
    result = oracle.verify(workdir)             # deterministic; no LLM
    if not result.passed:
        for f in result.failures:
            adj = classify_failure(f, ...)      # ROUTE/MATCH/UNBLOCK/NEEDS_WORK/IMPOSSIBLE
            ...

This file ships REAL implementations for the surfaces Determinex already has
toolchains for, and explicit, typed STUBS (with the exact command they will run)
for the surfaces on the day-one roadmap. A stub raises OracleUnavailable with the
install hint rather than silently passing -- the oracle never lies.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

try:
    from determinex_adjudicator import Failure
except ImportError:  # allow `python scripts/determinex_oracle.py` from repo root
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from determinex_adjudicator import Failure


class OracleUnavailable(RuntimeError):
    """Raised when an oracle's toolchain is not installed. Carries the fix hint."""


@dataclass
class OracleResult:
    passed: bool
    failures: list[Failure] = field(default_factory=list)
    raw: str = ""
    oracle: str = ""
    total: int = 0
    n_passed: int = 0


@dataclass
class Oracle:
    """A deterministic ground-truth surface for one language/domain."""
    name: str
    languages: tuple[str, ...]
    probe: tuple[str, ...]              # ANY of these on PATH proves the toolchain
    install_hint: str                  # how to get the toolchain
    verify_fn: Callable[[Path], OracleResult]

    def available(self) -> bool:
        # Available if ANY probed tool is present. The JVM oracle, e.g., can
        # drive gradle OR maven OR plain javac — having any one is enough.
        return any(shutil.which(p) is not None for p in self.probe)

    def verify(self, workdir: Path) -> OracleResult:
        if not self.available():
            raise OracleUnavailable(
                f"oracle '{self.name}' needs one of {self.probe}. {self.install_hint}")
        return self.verify_fn(workdir)


# ---------------------------------------------------------------------------
# Helpers shared by concrete oracles
# ---------------------------------------------------------------------------
def _run(cmd: list[str], cwd: Path, timeout: int = 600) -> subprocess.CompletedProcess:
    # Route through the hardened runner: cwd is workspace-bounded and the child
    # env is secret-scrubbed. allow_network=True because oracle BUILDS legitimately
    # fetch dependencies (cargo/go/npm/gradle) — the operator's own toolchain is
    # trusted-by-design; what we harden here is path-bounding + secret hygiene.
    # Returns a CompletedProcess so every verify_fn caller stays unchanged.
    from intake.hardened_runner import run as _hrun
    res = _hrun(cmd, workspace=cwd, cwd=cwd, timeout=timeout,
                allow_network=True, output_limit=None)
    return subprocess.CompletedProcess(
        args=cmd, returncode=res.exit_code, stdout=res.stdout, stderr=res.stderr)


def _junit_failures(xml_path: Path) -> list[Failure]:
    """Parse a JUnit XML into normalized Failure records (jest/pytest/gradle/go all
    emit JUnit). Kept dependency-free with ElementTree."""
    import xml.etree.ElementTree as ET
    out: list[Failure] = []
    try:
        root = ET.parse(str(xml_path)).getroot()
    except Exception:
        return out
    for tc in root.iter("testcase"):
        cls = tc.get("classname", "")
        name = tc.get("name", "")
        tid = f"{cls}.{name}" if cls else name
        fail = tc.find("failure") if tc.find("failure") is not None else tc.find("error")
        skip = tc.find("skipped")
        if fail is not None:
            out.append(Failure(test_id=tid, name=name,
                               text=(fail.get("message", "") + "\n" + (fail.text or "")),
                               status="failure"))
        elif skip is not None:
            out.append(Failure(test_id=tid, name=name,
                               text=skip.get("message", "") or (skip.text or ""),
                               status="skipped"))
    return out


def _junit_counts(xml_path: Path) -> tuple[int, int]:
    """Parse a JUnit XML into (total, n_passed) testcase counts.

    Every OracleResult below previously left `total`/`n_passed` at the
    dataclass default of 0 -- pass/fail itself was always correct (verified
    live 2026-07-02), but the counters were silently dead across every
    JUnit-backed oracle (python/jvm/swift/dotnet/ruby/php/typescript), which
    matters because determinex_oracle_env's OpenEnv observation contract
    exposes these exact fields to external RL consumers. A skipped testcase
    counts toward total but not n_passed (it neither passed nor failed)."""
    import xml.etree.ElementTree as ET
    try:
        root = ET.parse(str(xml_path)).getroot()
    except Exception:
        return (0, 0)
    total = 0
    n_passed = 0
    for tc in root.iter("testcase"):
        total += 1
        fail = tc.find("failure") if tc.find("failure") is not None else tc.find("error")
        skip = tc.find("skipped")
        if fail is None and skip is None:
            n_passed += 1
    return (total, n_passed)


def _uses_vitest(workdir: Path) -> bool:
    """vitest vs jest -- checked, not assumed. A vitest.config.* file is the
    clearest signal; falls back to checking package.json's own dependency
    lists (covers a vitest project configured inline in package.json's
    "test" script with no separate config file)."""
    for cfg in ("vitest.config.ts", "vitest.config.js", "vitest.config.mjs",
               "vitest.config.cjs", "vite.config.ts", "vite.config.js"):
        if (workdir / cfg).exists():
            # vite.config.* only counts if it actually configures a `test`
            # block -- a plain Vite app with no vitest set up shouldn't
            # falsely route here.
            if cfg.startswith("vitest.config"):
                return True
            try:
                if "test" in (workdir / cfg).read_text(encoding="utf-8", errors="replace"):
                    return True
            except OSError:
                pass
    pkg = workdir / "package.json"
    if pkg.exists():
        try:
            data = json.loads(pkg.read_text(encoding="utf-8", errors="replace"))
            deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
            if "vitest" in deps:
                return True
        except (OSError, json.JSONDecodeError):
            pass
    return False


def _has_test_framework(workdir: Path) -> bool:
    """Does this subproject actually have a JS/TS test framework configured
    at all? A package.json with no jest/vitest dependency and no "test"
    script (e.g. a thin CLI-wrapper extension whose only scripts are
    compile/package) has nothing for _verify_typescript's test-run step to
    invoke -- that's "nothing to verify", not "0 tests ran"."""
    if _uses_vitest(workdir):
        return True
    pkg = workdir / "package.json"
    if not pkg.exists():
        return False
    try:
        data = json.loads(pkg.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError):
        return False
    deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
    if "jest" in deps:
        return True
    test_script = data.get("scripts", {}).get("test", "")
    # npm's own default placeholder for `npm init` scaffolds -- explicitly
    # NOT a real test command.
    return bool(test_script) and "Error: no test specified" not in test_script


# ---------------------------------------------------------------------------
# Concrete oracle: TypeScript / JavaScript (tsc + jest/vitest)
# This is the surface Determinex's OWN products live in -- highest day-one priority.
# ---------------------------------------------------------------------------
def _verify_typescript(workdir: Path) -> OracleResult:
    # Found live 2026-07-22: this whole function computed `passed = len(failures)
    # == 0` -- if tsc/jest failed to even LAUNCH (missing binary, bad --
    # no-install resolution, config error) with a nonzero exit that didn't
    # happen to contain a parseable "error TSxxxx"/JUnit failure line,
    # `failures` stayed empty and the oracle silently reported PASSED without
    # ever actually verifying anything. Ryan: "it should be fixed to where it
    # all compiles and reports one way or the other" -- a tool that couldn't
    # run is not the same claim as "nothing's wrong", and must never be
    # reported identically.
    raw = []
    failures: list[Failure] = []
    ran_typecheck = False
    # 1) type check -- tsc is itself a compiler oracle (no tests required)
    if (workdir / "tsconfig.json").exists():
        ran_typecheck = True
        cp = _run(["npx", "--no-install", "tsc", "--noEmit", "--pretty", "false"], workdir)
        out = cp.stdout + cp.stderr
        raw.append(out)
        ts_failures = [
            Failure(test_id=line.split("(")[0].strip(), name=line.split("(")[0].strip(),
                   text=line, status="failure")
            for line in out.splitlines() if "): error TS" in line
        ]
        failures.extend(ts_failures)
        if cp.returncode != 0 and not ts_failures:
            # tsc itself failed to produce a real type-check verdict (missing
            # binary, npx resolution failure, OOM, etc.) -- not "0 errors".
            tail = out.strip()[-1500:]
            failures.append(Failure(
                test_id="tsc", name="typecheck",
                text=f"tsc exited {cp.returncode} with no parsed TS error lines "
                     f"(likely failed to run at all, not '0 errors'):\n{tail}",
                status="failure"))
    # 2) run the test suite if one exists, emitting JUnit. vitest OR jest --
    # found live 2026-07-22: this always ran jest unconditionally, so any
    # vitest-based project (this repo's OWN frontend among them -- "test":
    # "vitest run" in package.json, no jest anywhere) got an npx prompt to
    # auto-install jest, which _run's --no-install correctly refuses, and
    # that refusal read as a real test failure. Detect which one this
    # project actually uses instead of assuming.
    junit = workdir / "junit.xml"
    total, n_passed = 0, 0
    ran_tests = False
    # Found live 2026-07-22: a package.json with NO test framework configured
    # at all (this repo's own vscode-extension: no jest/vitest dependency,
    # no "test" script -- it's a thin CLI wrapper with its own compile-only
    # scripts) still unconditionally tried to run jest, which npx correctly
    # refused to auto-install, and that refusal read as a real test failure.
    # No test framework configured is "nothing to verify" (vacuous pass,
    # same principle as pytest's "no tests collected"), not "broken".
    if (workdir / "package.json").exists() and _has_test_framework(workdir):
        ran_tests = True
        if _uses_vitest(workdir):
            cp = _run(["npx", "--no-install", "vitest", "run",
                       "--reporter=junit", f"--outputFile={junit}"], workdir)
            runner_name = "vitest"
        else:
            cp = _run(["npx", "--no-install", "jest", "--ci",
                       "--reporters=jest-junit"], workdir)
            runner_name = "jest"
        out = cp.stdout + cp.stderr
        raw.append(out)
        if junit.exists():
            junit_failures = _junit_failures(junit)
            failures.extend(junit_failures)
            total, n_passed = _junit_counts(junit)
        elif cp.returncode != 0 and "No tests found" not in out:
            # No JUnit report AND a real nonzero exit that isn't the test
            # runner's own well-known "there simply are no tests here"
            # message -- it failed to run at all (missing binary, config
            # error, crash), not "0 test failures".
            tail = out.strip()[-1500:]
            failures.append(Failure(
                test_id=runner_name, name="test-run",
                text=f"{runner_name} exited {cp.returncode} with no JUnit report and no "
                     f"'No tests found' message (likely failed to run at all):\n{tail}",
                status="failure"))
    # Nothing to verify is NOT a pass. This branch used to set passed=len(failures)==0, which is
    # True when neither the type check nor the tests ran -- so an empty workspace, or a workspace
    # holding `const a: number = "not a number";` with no tsconfig, returned passed=True with
    # total=0. The explanation went into `raw`, which no caller reads.
    #
    # This is the Python `compileall`-over-zero-files bug relocated into the universal registry,
    # and every other oracle in this file already refuses an empty tree (jvm, swift, dotnet,
    # ruby, php, ...). It matters more here than it looks: verified_search turns a generation
    # exception into the candidate string "__generation_error__: ..." and verifies it like any
    # other, so against a lenient oracle that string is reported solved with a proof line.
    if not (ran_typecheck or ran_tests):
        failures.append(Failure(
            test_id="typescript", name="verify",
            text="no tsconfig.json and no package.json test script -- nothing was verified, so "
                 "this cannot be reported as a pass",
            status="failure"))
    passed = len(failures) == 0
    return OracleResult(passed=passed, failures=failures, raw="\n".join(raw),
                        oracle="typescript", total=total, n_passed=n_passed)


# ---------------------------------------------------------------------------
# Concrete oracle: Python (pytest -> JUnit) -- already PB's main surface
# ---------------------------------------------------------------------------
def _repo_python(workdir: Path) -> str:
    """The interpreter that can actually import this project.

    Bare "python" is whatever is on PATH -- for us, Determinex's own venv, which does not
    have the target project's dependencies. Measured 2026-08-01 against a real seaborn
    checkout: pytest exited 4 with "ImportError while loading conftest ... No module named
    'matplotlib'", and because that is not a parsed test failure it was reported as a single
    failure with test_id="pytest", name="collection/run".

    The Adjudicator then classified that as CODE. It is ENVIRONMENT -- the most consequential
    misclassification this oracle can make, because it sends a repair loop off to rewrite
    working source. Prefer the project's own venv when it ships one.
    """
    for c in (workdir / ".venv/Scripts/python.exe", workdir / ".venv/bin/python",
              workdir / "venv/Scripts/python.exe", workdir / "venv/bin/python"):
        if c.exists():
            return str(c)
    return "python"


def _verify_python(workdir: Path) -> OracleResult:
    junit = workdir / "_determinex_junit.xml"
    # SCOPE (DETERMINEX_PYTEST_SCOPE, space-separated pytest node ids). Running a whole
    # suite is the wrong question for repair: a real project carries breakage unrelated to
    # the bug in hand. Measured on a 2022 seaborn checkout under modern pytest -- the full
    # run reports a collection error in tests/test_core.py (a positional @pytest.fixture arg
    # newer pytest rejects), which has nothing to do with the failure being repaired and
    # would make any fix look unsuccessful. A developer says "this test fails", not "my repo
    # is broken"; unset, behaviour is unchanged.
    scope = [s for s in os.environ.get("DETERMINEX_PYTEST_SCOPE", "").split() if s]
    cp = _run([_repo_python(workdir), "-m", "pytest", "-q", f"--junitxml={junit}",
               "-p", "no:cacheprovider", *scope], workdir)
    failures = _junit_failures(junit) if junit.exists() else []
    total, n_passed = _junit_counts(junit) if junit.exists() else (0, 0)
    # Found live 2026-07-22: `passed=(len(failures)==0 and returncode==0)` reported
    # a bare, unexplained "not passed" (0 failures, no notes -- nothing to look
    # at) for ANY nonzero pytest exit that wasn't a parsed test failure. The
    # most common real case: exit code 5 = "no tests were collected" for a
    # small package with no local tests (its coverage lives in the root
    # tests/ tree) -- that is NOT the same claim as "this package is broken",
    # and reporting it identically was exactly the un-actionable "fails with
    # no reason" this project's whole philosophy forbids. Ryan: "it should be
    # fixed to where it all compiles and reports one way or the other."
    if cp.returncode == 5 and not failures:
        return OracleResult(passed=True, failures=[], raw=cp.stdout + cp.stderr,
                            oracle="python", total=0, n_passed=0)
    if cp.returncode != 0 and not failures:
        # Some other non-test-failure exit (import/collection error, crash,
        # etc.) -- a REAL problem, but the JUnit file never got a chance to
        # record it as a normal test failure. Surface it explicitly instead
        # of silently reporting "0 failures" alongside passed=False.
        tail = (cp.stdout + cp.stderr).strip()
        tail = tail[-2000:] if len(tail) > 2000 else tail
        failures = [Failure(test_id="pytest", name="collection/run",
                            text=f"pytest exited {cp.returncode} with no parsed test "
                                 f"failures (collection or environment error):\n{tail}",
                            status="failure")]
    return OracleResult(passed=(len(failures) == 0 and cp.returncode == 0),
                        failures=failures, raw=cp.stdout + cp.stderr, oracle="python",
                        total=total, n_passed=n_passed)


# ---------------------------------------------------------------------------
# Concrete oracle: Go (go build ./... -> compile errors are ground truth)
# ---------------------------------------------------------------------------
def _verify_go(workdir: Path) -> OracleResult:
    cp = _run(["go", "build", "./..."], workdir)
    out = cp.stdout + cp.stderr
    failures: list[Failure] = []
    for line in out.splitlines():
        # go errors: path:line:col: message
        m = re.match(r"(\S+\.go):(\d+):\d*:?\s*(.+)", line)
        if m:
            failures.append(Failure(test_id=f"{m.group(1)}:{m.group(2)}",
                                    name=m.group(1), text=line, status="failure"))
    passed = cp.returncode == 0
    return OracleResult(passed=passed,
                        failures=failures or ([] if passed else
                                              [Failure("go", "build", out[:600], status="failure")]),
                        raw=out, oracle="go")


# ---------------------------------------------------------------------------
# Concrete oracle: Rust (cargo build --message-format short)
# ---------------------------------------------------------------------------
def _verify_rust(workdir: Path) -> OracleResult:
    cp = _run(["cargo", "build", "--message-format", "short"], workdir)
    out = cp.stdout + cp.stderr
    failures: list[Failure] = []
    for line in out.splitlines():
        # rustc short: path:line:col: error[Exxxx]: message
        m = re.match(r"(\S+\.rs):(\d+):\d*:?\s*(error.*)", line)
        if m:
            failures.append(Failure(test_id=f"{m.group(1)}:{m.group(2)}",
                                    name=m.group(1), text=line, status="failure"))
    passed = cp.returncode == 0
    return OracleResult(passed=passed,
                        failures=failures or ([] if passed else
                                              [Failure("rust", "build", out[:600], status="failure")]),
                        raw=out, oracle="rust")


# ---------------------------------------------------------------------------
# Concrete oracle: JVM (Gradle / Maven / plain javac) -> JUnit XML
# ---------------------------------------------------------------------------
def _verify_jvm(workdir: Path) -> OracleResult:
    if (workdir / "build.gradle").exists() or (workdir / "build.gradle.kts").exists():
        gradle = "./gradlew" if (workdir / "gradlew").exists() else "gradle"
        cp = _run([gradle, "test", "--console=plain", "--no-daemon"], workdir, timeout=1800)
        results = list(workdir.glob("**/build/test-results/**/*.xml"))
    elif (workdir / "pom.xml").exists():
        mvn = "./mvnw" if (workdir / "mvnw").exists() else "mvn"
        cp = _run([mvn, "-q", "test"], workdir, timeout=1800)
        results = list(workdir.glob("**/target/surefire-reports/*.xml"))
    else:
        # plain javac compile = ground truth (no build system shipped)
        srcs = [str(p) for p in workdir.glob("**/*.java")]
        if not srcs:
            return OracleResult(passed=False, oracle="jvm",
                                failures=[Failure("jvm", "build", "no gradle/maven/.java found",
                                                  status="failure")])
        cp = _run(["javac", "-d", "_determinex_out", *srcs], workdir, timeout=900)
        results = []
    failures: list[Failure] = []
    total, n_passed = 0, 0
    for x in results:
        failures.extend(_junit_failures(x))
        t, p = _junit_counts(x)
        total += t
        n_passed += p
    hard = [f for f in failures if f.status == "failure"]
    passed = cp.returncode == 0 and not hard
    if not passed and not failures:
        failures = [Failure("jvm", "build", (cp.stdout + cp.stderr)[:600], status="failure")]
    return OracleResult(passed=passed, failures=failures, raw=cp.stdout + cp.stderr, oracle="jvm",
                        total=total, n_passed=n_passed)


# ---------------------------------------------------------------------------
# Concrete oracle: Swift (swift test --xunit-output -> JUnit-shaped XML)
# ---------------------------------------------------------------------------
def _verify_swift(workdir: Path) -> OracleResult:
    xml = workdir / "_determinex_swift.xml"
    cp = _run(["swift", "test", "--xunit-output", str(xml)], workdir, timeout=1800)
    failures = _junit_failures(xml) if xml.exists() else []
    total, n_passed = _junit_counts(xml) if xml.exists() else (0, 0)
    hard = [f for f in failures if f.status == "failure"]
    passed = cp.returncode == 0 and not hard
    if not passed and not failures:
        failures = [Failure("swift", "test", (cp.stdout + cp.stderr)[:600], status="failure")]
    return OracleResult(passed=passed, failures=failures, raw=cp.stdout + cp.stderr, oracle="swift",
                        total=total, n_passed=n_passed)


# ---------------------------------------------------------------------------
# Concrete oracle: C# / .NET (dotnet test, JUnit logger -> XML)
# ---------------------------------------------------------------------------
def _verify_dotnet(workdir: Path) -> OracleResult:
    xml = workdir / "_determinex_dotnet.xml"
    cp = _run(["dotnet", "test", "--logger", f"junit;LogFilePath={xml}"], workdir, timeout=1800)
    failures = _junit_failures(xml) if xml.exists() else []
    total, n_passed = _junit_counts(xml) if xml.exists() else (0, 0)
    hard = [f for f in failures if f.status == "failure"]
    # If the JUnit logger package isn't present, fall back to return code (never silent-pass).
    passed = cp.returncode == 0 and not hard
    if not passed and not failures:
        failures = [Failure("dotnet", "test", (cp.stdout + cp.stderr)[:600], status="failure")]
    return OracleResult(passed=passed, failures=failures, raw=cp.stdout + cp.stderr, oracle="dotnet",
                        total=total, n_passed=n_passed)


# ---------------------------------------------------------------------------
# Concrete oracle: Ruby (rspec JUnit if a suite ships, else `ruby -c` per file)
# ---------------------------------------------------------------------------
def _verify_ruby(workdir: Path) -> OracleResult:
    if (workdir / "spec").is_dir() or (workdir / ".rspec").exists():
        xml = workdir / "_determinex_rspec.xml"
        cp = _run(["rspec", "--format", "RspecJunitFormatter", "--out", str(xml)],
                  workdir, timeout=1800)
        failures = _junit_failures(xml) if xml.exists() else []
        total, n_passed = _junit_counts(xml) if xml.exists() else (0, 0)
        hard = [f for f in failures if f.status == "failure"]
        passed = cp.returncode == 0 and not hard
        if not passed and not failures:
            failures = [Failure("ruby", "test", (cp.stdout + cp.stderr)[:600], status="failure")]
        return OracleResult(passed=passed, failures=failures, raw=cp.stdout + cp.stderr, oracle="ruby",
                            total=total, n_passed=n_passed)
    # No suite shipped: syntax compile of every .rb is the ground truth.
    srcs = list(workdir.glob("**/*.rb"))
    if not srcs:
        return OracleResult(passed=False, oracle="ruby",
                            failures=[Failure("ruby", "build", "no .rb found", status="failure")])
    fails: list[Failure] = []
    raw = ""
    for s in srcs:
        cp = _run(["ruby", "-c", str(s)], workdir, timeout=120)
        raw += cp.stdout + cp.stderr
        if cp.returncode != 0:
            fails.append(Failure("ruby", s.name, (cp.stdout + cp.stderr)[:400], status="failure"))
    return OracleResult(passed=not fails, failures=fails, raw=raw[:4000], oracle="ruby",
                        total=len(srcs), n_passed=len(srcs) - len(fails))


# ---------------------------------------------------------------------------
# Concrete oracle: PHP (phpunit JUnit if configured, else `php -l` per file)
# ---------------------------------------------------------------------------
def _verify_php(workdir: Path) -> OracleResult:
    if (workdir / "phpunit.xml").exists() or (workdir / "phpunit.xml.dist").exists():
        xml = workdir / "_determinex_phpunit.xml"
        cp = _run(["phpunit", "--log-junit", str(xml)], workdir, timeout=1800)
        failures = _junit_failures(xml) if xml.exists() else []
        total, n_passed = _junit_counts(xml) if xml.exists() else (0, 0)
        hard = [f for f in failures if f.status == "failure"]
        passed = cp.returncode == 0 and not hard
        if not passed and not failures:
            failures = [Failure("php", "test", (cp.stdout + cp.stderr)[:600], status="failure")]
        return OracleResult(passed=passed, failures=failures, raw=cp.stdout + cp.stderr, oracle="php",
                            total=total, n_passed=n_passed)
    # No suite shipped: `php -l` lint of every .php is the ground truth.
    srcs = list(workdir.glob("**/*.php"))
    if not srcs:
        return OracleResult(passed=False, oracle="php",
                            failures=[Failure("php", "build", "no .php found", status="failure")])
    fails: list[Failure] = []
    raw = ""
    for s in srcs:
        cp = _run(["php", "-l", str(s)], workdir, timeout=120)
        raw += cp.stdout + cp.stderr
        if cp.returncode != 0:
            fails.append(Failure("php", s.name, (cp.stdout + cp.stderr)[:400], status="failure"))
    return OracleResult(passed=not fails, failures=fails, raw=raw[:4000], oracle="php",
                        total=len(srcs), n_passed=len(srcs) - len(fails))


# ---------------------------------------------------------------------------
# Concrete oracle: C / C++ (cmake / make / autotools build, else compiler
# syntax-check per file -- same "compile is ground truth" shape as go/rust).
# ---------------------------------------------------------------------------
_C_FAMILY_ERROR_RE = re.compile(r"(\S+\.(?:c|cc|cpp|cxx|h|hpp)):(\d+):\d*:?\s*(error.*)")


def _verify_c_family(workdir: Path, cc: str, lang: str, ext: str) -> OracleResult:
    if (workdir / "CMakeLists.txt").exists():
        build_dir = workdir / "_determinex_cbuild"
        build_dir.mkdir(exist_ok=True)
        cfg = _run(["cmake", "-S", str(workdir), "-B", str(build_dir)], workdir, timeout=300)
        cp = cfg if cfg.returncode != 0 else _run(
            ["cmake", "--build", str(build_dir)], workdir, timeout=900)
    elif (workdir / "Makefile").exists() or (workdir / "makefile").exists():
        cp = _run(["make"], workdir, timeout=900)
    elif (workdir / "configure").exists():
        cfg = _run(["./configure"], workdir, timeout=300)
        cp = cfg if cfg.returncode != 0 else _run(["make"], workdir, timeout=900)
    else:
        # No build system shipped: per-file syntax-only compile is ground
        # truth, same posture as _verify_ruby/_verify_php's lint fallback.
        srcs = [str(p) for p in workdir.glob(f"**/{ext}")]
        if not srcs:
            return OracleResult(passed=False, oracle=lang,
                                failures=[Failure(lang, "build", f"no {ext} found",
                                                  status="failure")])
        cp = _run([cc, "-fsyntax-only", *srcs], workdir, timeout=300)

    out = cp.stdout + cp.stderr
    failures: list[Failure] = []
    for line in out.splitlines():
        m = _C_FAMILY_ERROR_RE.match(line)
        if m:
            failures.append(Failure(test_id=f"{m.group(1)}:{m.group(2)}",
                                    name=m.group(1), text=line, status="failure"))
    passed = cp.returncode == 0
    if not passed and not failures:
        # Compiler/build-system failed to even launch (missing toolchain
        # component, configure error, ...) with no parseable error line --
        # must surface as an explained failure, never a silent 0/0 pass.
        failures = [Failure(lang, "build", out[:600], status="failure")]
    return OracleResult(passed=passed, failures=failures, raw=out, oracle=lang)


def _verify_c(workdir: Path) -> OracleResult:
    return _verify_c_family(workdir, cc="gcc", lang="c", ext="*.c")


def _verify_cpp(workdir: Path) -> OracleResult:
    return _verify_c_family(workdir, cc="g++", lang="cpp", ext="*.cpp")


# ---------------------------------------------------------------------------
# Concrete oracle: COBOL (legacy) -- GnuCOBOL `cobc -c` compile-only per file.
# ---------------------------------------------------------------------------
def _verify_cobol(workdir: Path) -> OracleResult:
    srcs = [p for p in list(workdir.glob("**/*.cob")) + list(workdir.glob("**/*.cbl"))]
    if not srcs:
        return OracleResult(passed=False, oracle="cobol",
                            failures=[Failure("cobol", "build", "no .cob/.cbl found",
                                              status="failure")])
    fails: list[Failure] = []
    raw = ""
    for s in srcs:
        cp = _run(["cobc", "-c", str(s)], workdir, timeout=120)
        raw += cp.stdout + cp.stderr
        if cp.returncode != 0:
            fails.append(Failure("cobol", s.name, (cp.stdout + cp.stderr)[:400], status="failure"))
    return OracleResult(passed=not fails, failures=fails, raw=raw[:4000], oracle="cobol",
                        total=len(srcs), n_passed=len(srcs) - len(fails))


# ---------------------------------------------------------------------------
# Concrete oracle: BASIC (legacy) -- FreeBASIC `fbc -c` compile-only per file.
# ---------------------------------------------------------------------------
def _verify_basic(workdir: Path) -> OracleResult:
    srcs = list(workdir.glob("**/*.bas"))
    if not srcs:
        return OracleResult(passed=False, oracle="basic",
                            failures=[Failure("basic", "build", "no .bas found",
                                              status="failure")])
    fails: list[Failure] = []
    raw = ""
    for s in srcs:
        cp = _run(["fbc", "-c", str(s)], workdir, timeout=120)
        raw += cp.stdout + cp.stderr
        if cp.returncode != 0:
            fails.append(Failure("basic", s.name, (cp.stdout + cp.stderr)[:400], status="failure"))
    return OracleResult(passed=not fails, failures=fails, raw=raw[:4000], oracle="basic",
                        total=len(srcs), n_passed=len(srcs) - len(fails))


# ---------------------------------------------------------------------------
# Concrete oracle: Tauri (composite) -- the Rust backend (src-tauri/) AND the
# TS/JS frontend verified together as ONE unit. A Tauri app is only actually
# correct when both halves compile; a passing `cargo check` next to a broken
# frontend build (or vice versa) is not a real pass. Reuses the existing
# _verify_rust / _verify_typescript oracles rather than reimplementing either
# half -- this is composition, not a third compiler frontend.
# ---------------------------------------------------------------------------
def _verify_tauri(workdir: Path) -> OracleResult:
    src_tauri = workdir / "src-tauri"
    if not src_tauri.exists():
        if (workdir / "Cargo.toml").exists() and (workdir / "tauri.conf.json").exists():
            # workdir passed in as the src-tauri dir itself
            src_tauri = workdir
            workdir = workdir.parent
        else:
            return OracleResult(passed=False, oracle="tauri",
                                failures=[Failure("tauri", "layout",
                                          "no src-tauri/ (or Cargo.toml+tauri.conf.json) found -- "
                                          "not a Tauri project layout", status="failure")])

    backend = _verify_rust(src_tauri)
    failures = list(backend.failures)
    raw = f"--- backend (cargo, {src_tauri}) ---\n{backend.raw}\n"
    total = backend.total
    n_passed = backend.n_passed
    passed = backend.passed

    if (workdir / "package.json").exists():
        frontend = _verify_typescript(workdir)
        failures.extend(frontend.failures)
        raw += f"--- frontend (tsc/tests, {workdir}) ---\n{frontend.raw}\n"
        total += frontend.total
        n_passed += frontend.n_passed
        passed = passed and frontend.passed

    if not passed and not failures:
        failures = [Failure("tauri", "build", raw[:600], status="failure")]
    return OracleResult(passed=passed, failures=failures, raw=raw[:6000], oracle="tauri",
                        total=total, n_passed=n_passed)


# ---------------------------------------------------------------------------
# Concrete oracle: RISC-V / ET-SoC1 silicon kernels (Docker toolchain + sys-emu)
# Built 2026-07-10 during the AIFoundry CORE-ET hackathon. workdir must be a
# checkout of aifoundry-org/hf-hackathon (or a git worktree of it) with the
# candidate kernel already written into ported_models/yolo/src/. Requires
# Docker Desktop + a one-time toolchain/SDK build under DETERMINEX_ET_WORK
# (default <repo-parent>/et-soc1-work) -- see docs/architecture (or ask this session)
# for the exact bootstrap; probe below only checks Docker itself is present,
# matching the "available() = a toolchain COULD run" contract other oracles use.
#
# Two-tier verification, same shape as every other domain oracle here:
#   tier 1 (this function, seconds): compiles the candidate with the REAL
#     riscv64-unknown-elf-gcc via the shared toolchain container -- catches
#     syntax/type/link errors exactly like tsc/cargo/go build do elsewhere in
#     this file. This is the fast, always-run gate.
#   tier 2 (opt-in, 30-90+ min per test image on this hardware -- NOT run by
#     default, pass env DETERMINEX_ET_SYSEMU_VERIFY=1 to enable): runs one
#     sys-emu image through the actual launcher and checks it produces a
#     non-empty dump without crashing. This is a REAL accuracy signal but too
#     slow to gate every candidate; use it selectively on tier-1 survivors.
# ---------------------------------------------------------------------------
def _et_soc1_work_root() -> Path:
    import os
    return Path(os.environ.get("DETERMINEX_ET_WORK",
                               str(Path(__file__).resolve().parent.parent.parent / "et-soc1-work")))


def _docker(cmd: list[str], timeout: int = 300) -> subprocess.CompletedProcess:
    import os
    env = dict(os.environ)
    env["MSYS_NO_PATHCONV"] = "1"
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, env=env)
    except subprocess.TimeoutExpired as e:
        # Found live 2026-07-23: _wait_for_container_ready's readiness-probe
        # loop calls this with a short per-attempt timeout (10s) specifically
        # so a hung probe doesn't block the whole poll -- but subprocess.run
        # RAISES on timeout rather than returning a nonzero-exit
        # CompletedProcess, so an unhandled TimeoutExpired crashed the entire
        # oracle call instead of just failing that one poll attempt (every
        # _docker() caller's existing `cp.returncode != 0` handling expects a
        # CompletedProcess, never an exception). 124 matches the conventional
        # `timeout` shell command's exit code for "the command timed out".
        stdout = (e.stdout or b"").decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        stderr = (e.stderr or b"").decode("utf-8", "replace") if isinstance(e.stderr, bytes) else (e.stderr or "")
        return subprocess.CompletedProcess(
            args=cmd, returncode=124,
            stdout=stdout, stderr=stderr + f"\n[determinex] docker command timed out after {timeout}s: {cmd}")


def _verify_riscv_et_soc1(workdir: Path) -> OracleResult:
    et_work = _et_soc1_work_root()
    if not (et_work / "et" / "bin" / "riscv64-unknown-elf-gcc").exists() and \
       not (et_work / "build").exists():
        raise OracleUnavailable(
            "riscv-et-soc1 oracle needs a one-time toolchain+SDK build under "
            f"{et_work} (Docker-based, ~30-60 min, fully self-serve, no board "
            "credentials needed -- see docs/security/OPENENV_SUBMISSION.md-adjacent "
            "notes or corpus/programbench/build_knowledge.json "
            "'local_verification_boundary' for the exact bootstrap steps).")

    container = "determinex-et-oracle"
    # Reuse a running container ONLY if it's already mounted at THIS exact
    # workdir -- a container reused across a DIFFERENT workdir silently tests
    # stale code from whichever worktree originally created it (found
    # 2026-07-10: a leaked container from an earlier apt-get timeout stayed
    # mounted to one worktree for 25+ minutes while later verify_fn calls for
    # OTHER worktrees reused it under started_here=False, none of them ever
    # cleaning it up). Mount identity, not "does a container exist", is the
    # correctness condition for reuse.
    mount_check = _docker(["docker", "inspect", container,
                           "--format", "{{range .Mounts}}{{.Source}}|{{end}}"])
    workdir_str = str(workdir)
    mount_matches = (mount_check.returncode == 0 and workdir_str in mount_check.stdout)
    started_here = False
    if not mount_matches:
        _docker(["docker", "rm", "-f", container])
        run = _docker(["docker", "run", "-d", "--name", container,
                       "-v", f"{workdir}:/repo", "-v", f"{et_work}:/etwork",
                       "-w", "/repo", "ubuntu:24.04", "sleep", "1800"], timeout=60)
        if run.returncode != 0:
            return OracleResult(passed=False, oracle="riscv-et-soc1",
                                failures=[Failure("riscv-et-soc1", "docker-start",
                                          run.stderr[:2000], status="failure")])
        started_here = True

    try:
        if started_here:
            # Inside try/finally now: an apt-get timeout no longer leaks an
            # un-cleaned, stale-mounted container for subsequent calls to
            # silently inherit.
            _docker(["docker", "exec", container, "bash", "-c",
                    "apt-get update -qq && apt-get install -y -qq python3 libmpc-dev "
                    "libmpfr-dev libgmp-dev 2>&1 | tail -5"], timeout=180)
        env_args = ["-e", "WORK_ROOT=/etwork", "-e", "ET_INSTALL=/etwork/et",
                   "-e", "BUILD_ROOT=/etwork/build",
                   "-e", "BENCHMARK_ARTIFACT_ROOT=/repo/local-artifacts/model-port-benchmarks"]
        cp = _docker(["docker", "exec", *env_args, container, "bash", "-c",
                     "bash .github/ci/scripts/prepare_benchmark_inputs.sh yolo 2>&1 && "
                     "bash .github/ci/scripts/build_leaderboard_elf.sh yolo 2>&1"],
                     timeout=300)
        raw = cp.stdout + cp.stderr
        elf_check = _docker(["docker", "exec", container, "bash", "-c",
                            "test -s /repo/local-artifacts/model-port-benchmarks/"
                            "yolo-bench/yolo_m30.elf && echo ELF_OK"], timeout=30)
        passed = cp.returncode == 0 and "ELF_OK" in elf_check.stdout
        failures: list[Failure] = []
        if not passed:
            failures.append(Failure("riscv-et-soc1", "compile",
                                    raw[-4000:], status="failure"))
        return OracleResult(passed=passed, failures=failures, raw=raw[-4000:],
                            oracle="riscv-et-soc1", total=1, n_passed=1 if passed else 0)
    finally:
        if started_here:
            _docker(["docker", "rm", "-f", container])


# ---------------------------------------------------------------------------
# Concrete oracle: DuckDB (embedded -- no server, no Docker). Runs every
# *.sql file in workdir through the real duckdb CLI against an in-memory
# database. Installed live 2026-07-22 via `winget install --id DuckDB.cli
# --location T:/determinex-tools/duckdb` (kept off C: per Ryan: "put what
# you need on T to save for now on space").
# ---------------------------------------------------------------------------
_SQL_ERROR_RE = re.compile(r"^Error:.*", re.IGNORECASE)


def _verify_duckdb(workdir: Path) -> OracleResult:
    srcs = list(workdir.glob("**/*.sql"))
    if not srcs:
        return OracleResult(passed=False, oracle="duckdb",
                            failures=[Failure("duckdb", "build", "no .sql found",
                                              status="failure")])
    fails: list[Failure] = []
    raw = ""
    for s in srcs:
        # ".bail on" is load-bearing: without it the CLI (sqlite3-style)
        # keeps going after a failed statement and exits 0 even though a
        # query inside the script errored -- would be a silent pass.
        # DuckDB's dot-command tokenizer treats backslash as an escape char
        # (sqlite3-style), so a raw Windows path in ".read C:\Users\..."
        # silently eats the backslashes -- found live 2026-07-22. Forward
        # slashes are accepted by Windows paths and aren't special to the
        # tokenizer.
        cp = _run(["duckdb", ":memory:", "-c", ".bail on", "-c", f".read {s.as_posix()}"],
                  workdir, timeout=120)
        out = cp.stdout + cp.stderr
        raw += out
        errors = [line for line in out.splitlines() if _SQL_ERROR_RE.match(line)]
        if cp.returncode != 0 or errors:
            text = "\n".join(errors) or out[:400]
            fails.append(Failure("duckdb", s.name, text[:400], status="failure"))
    return OracleResult(passed=not fails, failures=fails, raw=raw[:4000], oracle="duckdb",
                        total=len(srcs), n_passed=len(srcs) - len(fails))


# ---------------------------------------------------------------------------
# Concrete oracle: MariaDB (Docker-backed, ephemeral). A native Windows
# MSI service install was tried live 2026-07-22 (`winget install --id
# MariaDB.Server`) and failed with a generic 1603, rolling back cleanly with
# no files left on disk -- exactly the fragile, elevation-hungry, host-
# service-registering path an EPHEMERAL verification sandbox shouldn't
# depend on. Every *.sql file in workdir is run against a real, disposable
# mariadb server instead -- same "spin up -> verify -> tear down" Docker
# shape already proven by the riscv-et-soc1 oracle above.
# ---------------------------------------------------------------------------
def _wait_for_container_ready(container: str, probe_cmd: list[str], timeout: int = 150) -> bool:
    # 90s was measured live 2026-07-23 to be uncomfortably close to the real
    # boundary -- mariadb:11's first-time container init (mariadb-install-db
    # + the temp-server bootstrap/restart cycle) consistently took 94-99s on
    # this box, one run exceeded 90s outright. 150s gives real margin without
    # meaningfully slowing down the common case (the loop returns as soon as
    # the probe succeeds, it doesn't wait out the full budget).
    import time
    deadline = time.time() + timeout
    while time.time() < deadline:
        cp = _docker(["docker", "exec", container, *probe_cmd], timeout=10)
        if cp.returncode == 0:
            return True
        time.sleep(2)
    return False


# Found live 2026-07-23: the official mariadb image's entrypoint runs a
# TEMPORARY bootstrap mysqld first (binds the port, answers "ready for
# connections" and responds to a ping/ident probe) purely to apply
# MARIADB_ROOT_PASSWORD, then stops it and starts the REAL server ~10-15s
# later -- confirmed via `docker logs`: two separate "ready for
# connections" lines with a "Temporary server stopped" in between. A probe
# landing in that temporary-server window reports ready, but the actual
# root password grant isn't durably in place yet, so the first real exec
# right after can get a genuine `ERROR 1045 Access denied` with the
# CORRECT password -- not a bad credential, a startup race. Retrying the
# exact same exec a few times (not a separate readiness probe, which
# raced identically) is what actually closes the window.
_TRANSIENT_AUTH_SIGNATURES = ("Access denied for user", "Can't connect to")


def _run_with_transient_retry(cmd: list[str], timeout: int, attempts: int = 5,
                              delay: float = 3.0) -> subprocess.CompletedProcess:
    import time
    cp = _docker(cmd, timeout=timeout)
    for _ in range(attempts - 1):
        out = cp.stdout + cp.stderr
        if cp.returncode == 0 or not any(sig in out for sig in _TRANSIENT_AUTH_SIGNATURES):
            break
        time.sleep(delay)
        cp = _docker(cmd, timeout=timeout)
    return cp


def _verify_mariadb(workdir: Path) -> OracleResult:
    srcs = list(workdir.glob("**/*.sql"))
    if not srcs:
        return OracleResult(passed=False, oracle="mariadb",
                            failures=[Failure("mariadb", "build", "no .sql found",
                                              status="failure")])
    container = "determinex-mariadb-oracle"
    _docker(["docker", "rm", "-f", container])
    run = _docker(["docker", "run", "-d", "--name", container,
                   "-e", "MARIADB_ROOT_PASSWORD=determinex",
                   "-v", f"{workdir}:/sql:ro", "mariadb:11"], timeout=120)
    if run.returncode != 0:
        return OracleResult(passed=False, oracle="mariadb",
                            failures=[Failure("mariadb", "docker-start",
                                      run.stderr[:2000], status="failure")])
    try:
        if not _wait_for_container_ready(
                container, ["mariadb-admin", "ping", "-uroot", "-pdeterminex"]):
            return OracleResult(passed=False, oracle="mariadb",
                                failures=[Failure("mariadb", "startup",
                                          "mariadb server never became ready within 90s",
                                          status="failure")])
        fails: list[Failure] = []
        raw = ""
        for s in srcs:
            rel = f"/sql/{s.relative_to(workdir).as_posix()}"
            cp = _run_with_transient_retry(
                ["docker", "exec", container, "sh", "-c", f"mariadb -uroot -pdeterminex < {rel}"],
                timeout=60)
            out = cp.stdout + cp.stderr
            raw += out
            if cp.returncode != 0:
                fails.append(Failure("mariadb", s.name, out[:400], status="failure"))
        return OracleResult(passed=not fails, failures=fails, raw=raw[:4000], oracle="mariadb",
                            total=len(srcs), n_passed=len(srcs) - len(fails))
    finally:
        _docker(["docker", "rm", "-f", container])


# ---------------------------------------------------------------------------
# Concrete oracle: MongoDB (Docker-backed, ephemeral) -- same shape as
# MariaDB above. Every *.js file in workdir is run as a mongosh script
# against a real, disposable mongod instance.
# ---------------------------------------------------------------------------
def _verify_mongodb(workdir: Path) -> OracleResult:
    srcs = list(workdir.glob("**/*.js"))
    if not srcs:
        return OracleResult(passed=False, oracle="mongodb",
                            failures=[Failure("mongodb", "build", "no .js found",
                                              status="failure")])
    container = "determinex-mongodb-oracle"
    _docker(["docker", "rm", "-f", container])
    run = _docker(["docker", "run", "-d", "--name", container,
                   "-v", f"{workdir}:/scripts:ro", "mongo:7"], timeout=120)
    if run.returncode != 0:
        return OracleResult(passed=False, oracle="mongodb",
                            failures=[Failure("mongodb", "docker-start",
                                      run.stderr[:2000], status="failure")])
    try:
        if not _wait_for_container_ready(
                container, ["mongosh", "--quiet", "--eval", "db.runCommand({ping:1})"]):
            return OracleResult(passed=False, oracle="mongodb",
                                failures=[Failure("mongodb", "startup",
                                          "mongod never became ready within 90s",
                                          status="failure")])
        fails: list[Failure] = []
        raw = ""
        for s in srcs:
            rel = f"/scripts/{s.relative_to(workdir).as_posix()}"
            cp = _docker(["docker", "exec", container, "mongosh", "--quiet", rel], timeout=60)
            out = cp.stdout + cp.stderr
            raw += out
            if cp.returncode != 0:
                fails.append(Failure("mongodb", s.name, out[:400], status="failure"))
        return OracleResult(passed=not fails, failures=fails, raw=raw[:4000], oracle="mongodb",
                            total=len(srcs), n_passed=len(srcs) - len(fails))
    finally:
        _docker(["docker", "rm", "-f", container])


# ---------------------------------------------------------------------------
# Stubs for surfaces still on the roadmap. Each declares the EXACT command it
# will run; raising OracleUnavailable (never silently passing) until wired.
# ---------------------------------------------------------------------------
def _stub(name: str, cmd: str) -> Callable[[Path], OracleResult]:
    def _fn(workdir: Path) -> OracleResult:
        raise OracleUnavailable(f"oracle '{name}' not yet wired; planned command: {cmd}")
    return _fn


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
_ORACLES: dict[str, Oracle] = {}


def register(o: Oracle) -> None:
    for lang in o.languages:
        _ORACLES[lang.lower()] = o


def get_oracle(language: str) -> Oracle:
    key = language.lower()
    if key not in _ORACLES:
        raise KeyError(f"no oracle registered for language '{language}'. "
                       f"Known: {sorted(_ORACLES)}")
    return _ORACLES[key]


def available_oracles() -> dict[str, bool]:
    return {lang: o.available() for lang, o in sorted(_ORACLES.items())}


register(Oracle("typescript", ("typescript", "ts", "javascript", "js", "tsx", "node"),
                ("npx",), "npm i -D typescript jest jest-junit", _verify_typescript))
register(Oracle("python", ("python", "py"), ("python",),
                "python 3.11+ with pytest", _verify_python))
register(Oracle("jvm", ("kotlin", "kt", "java", "jvm"), ("gradle", "mvn", "javac"),
                "install Gradle/Maven (JVM); gradle/maven emit JUnit XML, or plain javac "
                "compile is used as ground truth when no build file ships",
                _verify_jvm))
register(Oracle("rust", ("rust", "rs"), ("cargo",),
                "rustup toolchain", _verify_rust))
register(Oracle("go", ("go", "golang"), ("go",),
                "go toolchain", _verify_go))
register(Oracle("swift", ("swift",), ("swift",),
                "Swift toolchain (swift test --xunit-output)", _verify_swift))
register(Oracle("csharp", ("csharp", "cs", "dotnet"), ("dotnet",),
                ".NET SDK + JUnitXml.TestLogger (dotnet add package JunitXml.TestLogger)",
                _verify_dotnet))
register(Oracle("ruby", ("ruby", "rb"), ("ruby",),
                "Ruby (rspec + rspec_junit_formatter for tests; else `ruby -c` syntax)",
                _verify_ruby))
register(Oracle("php", ("php",), ("php",),
                "PHP (phpunit --log-junit for tests; else `php -l` lint)",
                _verify_php))
register(Oracle("c", ("c",), ("gcc", "clang", "cc"),
                "a C compiler (gcc/clang); cmake/make/autotools build used if shipped, "
                "else `gcc -fsyntax-only` per file",
                _verify_c))
register(Oracle("cpp", ("cpp", "c++", "cxx"), ("g++", "clang++"),
                "a C++ compiler (g++/clang++); cmake/make/autotools build used if shipped, "
                "else `g++ -fsyntax-only` per file",
                _verify_cpp))
register(Oracle("cobol", ("cobol", "cob", "cbl"), ("cobc",),
                "GnuCOBOL (`cobc -c` compile-only per .cob/.cbl file)",
                _verify_cobol))
register(Oracle("basic", ("basic", "bas", "freebasic"), ("fbc",),
                "FreeBASIC (`fbc -c` compile-only per .bas file)",
                _verify_basic))
register(Oracle("tauri", ("tauri",), ("cargo", "npx"),
                "Rust toolchain (cargo) + Node/npm -- composite: verifies src-tauri/ "
                "(cargo) AND the TS/JS frontend (tsc/tests) together as one Tauri app",
                _verify_tauri))
register(Oracle("duckdb", ("duckdb",), ("duckdb",),
                "DuckDB CLI (embedded, no server) -- runs *.sql files with .bail on",
                _verify_duckdb))
register(Oracle("mariadb", ("mariadb", "mysql"), ("docker",),
                "Docker Desktop -- spins an ephemeral mariadb:11 container, "
                "runs *.sql files against it, tears down",
                _verify_mariadb))
register(Oracle("mongodb", ("mongodb", "mongo"), ("docker",),
                "Docker Desktop -- spins an ephemeral mongo:7 container, "
                "runs *.js (mongosh) scripts against it, tears down",
                _verify_mongodb))
register(Oracle("riscv-et-soc1", ("riscv-et-soc1", "et-soc1", "erbium"), ("docker",),
                "Docker Desktop + one-time toolchain/SDK build under "
                "DETERMINEX_ET_WORK (default <repo-parent>/et-soc1-work); see "
                "corpus/programbench/build_knowledge.json 'local_verification_boundary'",
                _verify_riscv_et_soc1))


# ===========================================================================
# Ground-Truth Synthesizer -- "make the tests for the ones it doesn't have"
# ===========================================================================
@dataclass
class SynthesizedOracle:
    """An executable specification derived for a task that shipped no tests.
    The synthesizer captures the CURRENT observable behavior (characterization)
    and/or derives invariants from a spec, so the solve loop has ground truth to
    iterate against even in greenfield / unbenchmarked domains."""
    kind: str                      # characterization | property | golden | contract
    language: str
    artifact_path: Path            # where the generated test/spec was written
    rationale: str


_SYNTH_TEMPLATES = {
    # characterization: pin the program's current output so refactors are safe
    "characterization": (
        "Run the target on a representative input corpus, capture stdout/stderr/rc "
        "as golden files, and emit a test that re-runs and diffs. Locks behavior "
        "before any change -- the classic 'tests for legacy code with no tests'."),
    # property: derive invariants from the spec (idempotence, round-trip, ordering)
    "property": (
        "From the spec, derive invariants (round-trip encode/decode == identity, "
        "sort is idempotent, output schema validates) and emit property tests that "
        "fuzz inputs against them. Ground truth without a reference binary."),
    # golden: when a reference implementation exists, diff against it
    "golden": (
        "Run a trusted reference implementation alongside the candidate over a "
        "shared input corpus; any divergence is a failure. The PB pattern, applied "
        "to a domain PB never benchmarked."),
    # contract: types/schemas/API contracts as the oracle
    "contract": (
        "Treat the type checker / schema validator / OpenAPI contract as the oracle. "
        "No example tests needed -- the contract IS ground truth (tsc, mypy, jsonschema)."),
}


def synthesize_oracle(workdir: Path, language: str, spec: str = "",
                      kind: str = "characterization") -> SynthesizedOracle:
    """Generate ground truth where none was shipped.

    This is the bridge from "PB has a test suite for this" to "the IDE can fix
    ANYTHING": for an unbenchmarked task the system first manufactures a
    deterministic oracle, then runs the identical closed loop against it.

    The returned SynthesizedOracle points at a generated artifact (a test file or
    golden corpus). Generation of the artifact body is delegated to the builder
    model under the relevant `get_oracle(language)` so the SAME compiler/test
    surface validates the synthesized tests themselves (tests must compile/run).
    """
    if kind not in _SYNTH_TEMPLATES:
        raise ValueError(f"unknown synthesis kind '{kind}'. "
                         f"Choose: {sorted(_SYNTH_TEMPLATES)}")
    out_dir = workdir / "_determinex_synth"
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = out_dir / f"oracle_{kind}.json"
    manifest.write_text(json.dumps({
        "kind": kind,
        "language": language,
        "strategy": _SYNTH_TEMPLATES[kind],
        "spec_excerpt": spec[:2000],
        "status": "manifest_only",
        "note": ("Builder model fills the test/golden body next, then the "
                 "language oracle runs it to confirm the synthesized oracle is "
                 "itself executable before it gates any fix."),
    }, indent=2), encoding="utf-8")
    return SynthesizedOracle(kind=kind, language=language, artifact_path=manifest,
                             rationale=_SYNTH_TEMPLATES[kind])


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Determinex Universal Ground-Truth Oracle")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="show registered oracles and toolchain availability")
    v = sub.add_parser("verify", help="run an oracle against a workdir")
    v.add_argument("language")
    v.add_argument("workdir", type=Path)
    s = sub.add_parser("synthesize", help="manufacture ground truth where none exists")
    s.add_argument("language")
    s.add_argument("workdir", type=Path)
    s.add_argument("--kind", default="characterization", choices=sorted(_SYNTH_TEMPLATES))
    args = ap.parse_args()

    if args.cmd == "status":
        print("Registered oracles (language -> toolchain present?):")
        for lang, ok in available_oracles().items():
            o = _ORACLES[lang]
            mark = "OK " if ok else "-- "
            print(f"  {mark} {lang:12} via {o.probe[0]:8} | {'' if ok else o.install_hint}")
        return 0
    if args.cmd == "verify":
        o = get_oracle(args.language)
        res = o.verify(args.workdir)
        print(f"oracle={res.oracle} passed={res.passed} failures={len(res.failures)}")
        for f in res.failures[:20]:
            print(f"  [{f.status}] {f.name}: {f.text[:80]}")
        return 0 if res.passed else 1
    if args.cmd == "synthesize":
        so = synthesize_oracle(args.workdir, args.language, kind=args.kind)
        print(f"synthesized {so.kind} oracle -> {so.artifact_path}")
        print(f"  rationale: {so.rationale}")
        return 0
    return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
