#!/usr/bin/env python3
"""
determinex_ingest.py -- The Universal Task Ingester (Adjudicator component A)
==========================================================================
"...take any bench and first run, take it in, understand it, realize it will
need these edits to work or to create this according to what is being asked."

This is the comprehension front of the loop. Pointed at an arbitrary repo or
benchmark task it has never seen, it derives -- deterministically, no LLM -- the
four things the rest of the pipeline needs:

    language     : which language(s) the task is in (extension census)
    build_system : how to build it (cargo / go / cmake / make / npm / gradle / pip)
    harness      : how it is verified (pytest / jest / junit / cargo test / go test)
    oracle       : the ground-truth surface (from determinex_oracle registry); if the
                   task ships NO tests, flag for synthesize_oracle()
    spec         : an inferred behavioral specification -- the asserted behaviors,
                   CLI surface, and invariants reverse-engineered from the tests,
                   so planning is PROACTIVE ("it will need these edits") rather than
                   purely try-fail-inject.

The spec inference is intentionally evidence-based: it extracts the concrete
assertions, invoked argv, and test docstrings already present, rather than
guessing intent. That keeps it honest -- it reports what the tests demand, which
is exactly the ground truth the solve loop must satisfy.

    from determinex_ingest import ingest
    u = ingest(Path("some_repo/"))
    print(u.language, u.harness, u.oracle, len(u.spec.behaviors))

CLI
---
    python scripts/determinex_ingest.py <repo_or_task_dir> [--json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path

_HERE = str(Path(__file__).resolve().parent)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
try:
    from determinex_oracle import _ORACLES  # registry: language -> Oracle
except Exception:
    _ORACLES = {}
try:
    from determinex_hw_profiler import detect_dialect_sources
    from determinex_hw_profiler import profile_repo as hw_profile_repo
except Exception:
    detect_dialect_sources = None
    hw_profile_repo = None


_LANG_BY_EXT = {
    ".rs": "rust", ".go": "go", ".py": "python", ".c": "c", ".h": "c",
    ".cc": "cpp", ".cpp": "cpp", ".cxx": "cpp", ".hpp": "cpp",
    ".ts": "typescript", ".tsx": "typescript", ".js": "javascript", ".jsx": "javascript",
    ".kt": "kotlin", ".java": "java", ".swift": "swift", ".cs": "csharp",
    ".rb": "ruby", ".php": "php",
}

_BUILD_MARKERS = {
    "Cargo.toml": "cargo", "go.mod": "go", "CMakeLists.txt": "cmake",
    "Makefile": "make", "configure": "autotools", "package.json": "npm",
    "build.gradle": "gradle", "build.gradle.kts": "gradle", "pom.xml": "maven",
    "setup.py": "pip", "pyproject.toml": "pip", "Package.swift": "swiftpm",
}

_HARNESS_SIGNATURES = [
    ("pytest", re.compile(r"\bimport pytest\b|def test_|@pytest\.")),
    ("jest", re.compile(r"\b(describe|it|test)\s*\(|expect\(.*\)\.to")),
    ("cargo-test", re.compile(r"#\[test\]|#\[cfg\(test\)\]")),
    ("go-test", re.compile(r"func Test\w+\(t \*testing\.T\)")),
    ("junit", re.compile(r"@Test\b|org\.junit")),
]


@dataclass
class Spec:
    summary: str = ""
    cli_surface: list[str] = field(default_factory=list)   # observed argv/flags
    behaviors: list[str] = field(default_factory=list)     # asserted behaviors
    invariants: list[str] = field(default_factory=list)    # derived properties
    terms: dict = field(default_factory=dict)              # canonical verbiage
                                                           # (extracted, never guessed)


@dataclass
class TaskUnderstanding:
    root: str
    language: str
    language_census: dict[str, int]
    build_system: str
    harness: str
    has_tests: bool
    oracle: str                 # registered language oracle name, or "SYNTHESIZE"
    oracle_available: bool
    spec: Spec
    notes: list[str] = field(default_factory=list)
    hardware_profile: dict | None = None   # Pre-Flight Static Graph Profiler result, if a
                                            # known hardware-kernel dialect was auto-detected


def _census_languages(root: Path) -> dict[str, int]:
    c: Counter = Counter()
    for p in root.rglob("*"):
        if p.is_file() and not any(seg in p.parts for seg in (".git", "node_modules", "target", "vendor")):
            lang = _LANG_BY_EXT.get(p.suffix.lower())
            if lang:
                c[lang] += 1
    return dict(c.most_common())


def _detect_build(root: Path) -> str:
    for marker, system in _BUILD_MARKERS.items():
        if (root / marker).exists() or list(root.rglob(marker))[:1]:
            return system
    return "unknown"


def _detect_harness(root: Path) -> tuple[str, bool, list[Path]]:
    test_files: list[Path] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        n = p.name.lower()
        in_test_path = any("test" in part.lower() or "spec" in part.lower()
                           for part in p.parts[:-1])
        looks_like_test = (n.startswith("test_") or n.endswith("_test.py")
                           or n.endswith(".test.ts") or n.endswith(".test.js")
                           or n.endswith("_test.go") or n.endswith("_test.rs")
                           or n in ("tests.rs",) or "test" in n or "spec" in n)
        if (looks_like_test or in_test_path) and p.suffix.lower() in _LANG_BY_EXT:
            test_files.append(p)
    sample = ""
    for p in test_files[:25]:
        try:
            sample += p.read_text(encoding="utf-8", errors="replace")[:4000]
        except Exception:
            pass
    for name, pat in _HARNESS_SIGNATURES:
        if pat.search(sample):
            return name, bool(test_files), test_files
    return ("none", bool(test_files), test_files)


def _infer_spec(test_files: list[Path], language: str) -> Spec:
    behaviors: list[str] = []
    cli: set[str] = set()
    invariants: set[str] = set()
    for p in test_files[:80]:
        try:
            src = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        # observed argv / flags from run("--flag", ...) and subprocess calls
        for m in re.finditer(r"""run\(\s*["']([^"']+)["']""", src):
            cli.add(m.group(1))
        for m in re.finditer(r"""["'](--?[a-zA-Z][\w-]*)["']""", src):
            cli.add(m.group(1))
        # asserted behaviors: test docstrings + assertion lines
        for m in re.finditer(r'def (test_\w+)\([^)]*\):\s*(?:"""(.*?)"""|\'\'\'(.*?)\'\'\')?',
                             src, re.DOTALL):
            name = m.group(1)
            doc = (m.group(2) or m.group(3) or "").strip().splitlines()
            desc = doc[0].strip() if doc else name.replace("test_", "").replace("_", " ")
            behaviors.append(f"{name}: {desc}")
        # invariants from common property patterns
        if re.search(r"round.?trip|encode.*decode|decode.*encode", src, re.I):
            invariants.add("round-trip: encode then decode == identity")
        if re.search(r"idempoten", src, re.I):
            invariants.add("idempotence: f(f(x)) == f(x)")
        if re.search(r"returncode\s*==\s*0", src):
            invariants.add("valid invocations exit 0")
    # Canonical verbiage: mine the proper terms straight from test sources so
    # the reimpl never guesses flag long-names, metavars, possible-values, or
    # error templates. Shared engine with the eval-JSON term extractor.
    terms: dict = {}
    try:
        from determinex_term_extractor import mine_texts
        blobs = []
        for p in test_files[:80]:
            try:
                blobs.append(p.read_text(encoding="utf-8", errors="replace"))
            except Exception:
                pass
        terms = mine_texts(blobs)
    except Exception:
        terms = {}

    summary = (f"{language} tool; {len(behaviors)} asserted behaviors across "
               f"{len(test_files)} test files; {len(cli)} CLI tokens observed.")
    return Spec(summary=summary, cli_surface=sorted(cli)[:60],
                behaviors=behaviors[:200], invariants=sorted(invariants),
                terms=terms)


def ingest(root: Path) -> TaskUnderstanding:
    census = _census_languages(root)
    language = next(iter(census), "unknown")
    build = _detect_build(root)
    harness, has_tests, test_files = _detect_harness(root)
    spec = _infer_spec(test_files, language)

    notes: list[str] = []
    oracle_name = "SYNTHESIZE"
    oracle_avail = False
    if language in _ORACLES:
        oracle = _ORACLES[language]
        oracle_name = oracle.name
        oracle_avail = oracle.available()
        if not oracle_avail:
            notes.append(f"oracle '{oracle.name}' toolchain missing: {oracle.install_hint}")
    else:
        notes.append(f"no registered oracle for '{language}' -- register one or synthesize.")
    if not has_tests:
        oracle_name = "SYNTHESIZE"
        notes.append("no tests shipped -> synthesize_oracle() must manufacture ground "
                     "truth (characterization / property / golden / contract) first.")

    hardware_profile = None
    if detect_dialect_sources is not None and hw_profile_repo is not None and language in ("c", "cpp"):
        try:
            found = detect_dialect_sources(root)
            if found:
                dialect, sources = found
                hp = hw_profile_repo(dialect, sources)
                hardware_profile = asdict(hp)
                if hp.critical_findings:
                    notes.append(
                        f"PRE-FLIGHT PROFILER: {hp.n_critical} CRITICAL hardware-boundary risk(s) "
                        f"detected across {hp.n_tensor_eligible}/{hp.n_call_sites} hardware-unit-"
                        f"eligible call sites for dialect '{dialect}' -- see hardware_profile."
                        f"critical_findings before starting any optimization work on this kernel.")
                for w in hp.warnings:
                    notes.append(f"PRE-FLIGHT PROFILER warning: {w}")
        except Exception as e:
            notes.append(f"hardware profiler attempted but failed: {e}")

    return TaskUnderstanding(
        root=str(root), language=language, language_census=census,
        build_system=build, harness=harness, has_tests=has_tests,
        oracle=oracle_name, oracle_available=oracle_avail, spec=spec, notes=notes,
        hardware_profile=hardware_profile)


def main() -> int:
    ap = argparse.ArgumentParser(description="Determinex Universal Task Ingester")
    ap.add_argument("root", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    u = ingest(args.root)
    if args.json:
        print(json.dumps(asdict(u), indent=2))
        return 0
    print(f"=== INGEST: {u.root} ===")
    print(f"  language     : {u.language}   census={u.language_census}")
    print(f"  build_system : {u.build_system}")
    print(f"  harness      : {u.harness}   has_tests={u.has_tests}")
    print(f"  oracle       : {u.oracle}   available={u.oracle_available}")
    print(f"\n  SPEC: {u.spec.summary}")
    if u.spec.cli_surface:
        print(f"  CLI surface  : {' '.join(u.spec.cli_surface[:20])}")
    if u.spec.invariants:
        print("  invariants   :")
        for inv in u.spec.invariants:
            print(f"    - {inv}")
    if u.spec.behaviors:
        print(f"  behaviors    : ({len(u.spec.behaviors)} total, first 8)")
        for b in u.spec.behaviors[:8]:
            print(f"    - {b[:90]}")
    if u.notes:
        print("  notes:")
        for n in u.notes:
            print(f"    ! {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
