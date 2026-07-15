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


# ---------------------------------------------------------------------------
# Concrete oracle: TypeScript / JavaScript (tsc + jest/vitest)
# This is the surface Determinex's OWN products live in -- highest day-one priority.
# ---------------------------------------------------------------------------
def _verify_typescript(workdir: Path) -> OracleResult:
    raw = []
    failures: list[Failure] = []
    # 1) type check -- tsc is itself a compiler oracle (no tests required)
    if (workdir / "tsconfig.json").exists():
        cp = _run(["npx", "--no-install", "tsc", "--noEmit", "--pretty", "false"], workdir)
        raw.append(cp.stdout + cp.stderr)
        for line in (cp.stdout + cp.stderr).splitlines():
            # tsc format: path(line,col): error TSxxxx: message
            if "): error TS" in line:
                tid = line.split("(")[0].strip()
                failures.append(Failure(test_id=tid, name=tid, text=line, status="failure"))
    # 2) run the test suite if one exists, emitting JUnit
    junit = workdir / "junit.xml"
    total, n_passed = 0, 0
    if (workdir / "package.json").exists():
        cp = _run(["npx", "--no-install", "jest", "--ci",
                   "--reporters=jest-junit"], workdir)
        raw.append(cp.stdout + cp.stderr)
        if junit.exists():
            failures.extend(_junit_failures(junit))
            total, n_passed = _junit_counts(junit)
    passed = len(failures) == 0
    return OracleResult(passed=passed, failures=failures, raw="\n".join(raw),
                        oracle="typescript", total=total, n_passed=n_passed)


# ---------------------------------------------------------------------------
# Concrete oracle: Python (pytest -> JUnit) -- already PB's main surface
# ---------------------------------------------------------------------------
def _verify_python(workdir: Path) -> OracleResult:
    junit = workdir / "_determinex_junit.xml"
    cp = _run(["python", "-m", "pytest", "-q", f"--junitxml={junit}",
               "-p", "no:cacheprovider"], workdir)
    failures = _junit_failures(junit) if junit.exists() else []
    total, n_passed = _junit_counts(junit) if junit.exists() else (0, 0)
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
# Concrete oracle: RISC-V / ET-SoC1 silicon kernels (Docker toolchain + sys-emu)
# Built 2026-07-10 during the AIFoundry CORE-ET hackathon. workdir must be a
# checkout of aifoundry-org/hf-hackathon (or a git worktree of it) with the
# candidate kernel already written into ported_models/yolo/src/. Requires
# Docker Desktop + a one-time toolchain/SDK build under DETERMINEX_ET_WORK
# (default C:/Dev/et-soc1-work) -- see docs/architecture (or ask this session)
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
    return Path(os.environ.get("DETERMINEX_ET_WORK", "C:/Dev/et-soc1-work"))


def _docker(cmd: list[str], timeout: int = 300) -> subprocess.CompletedProcess:
    import os
    env = dict(os.environ)
    env["MSYS_NO_PATHCONV"] = "1"
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, env=env)


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
register(Oracle("riscv-et-soc1", ("riscv-et-soc1", "et-soc1", "erbium"), ("docker",),
                "Docker Desktop + one-time toolchain/SDK build under "
                "DETERMINEX_ET_WORK (default C:/Dev/et-soc1-work); see "
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
