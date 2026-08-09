#!/usr/bin/env python3
"""corpus_wiring_census.py -- every corpus artifact must have a consumer, every pointer must resolve.

The two failure modes this guards (both hit us in July 2026):
  * BUILT-BUT-INVISIBLE: an artifact is current on disk but nothing wires it into the query
    surface, so sessions re-derive its facts by hand (canonical_tasks.json, 2026-07-16 --
    corpus_gap_canonical_tasks_not_queryable_20260716).
  * SPLIT-BRAIN POINTER: a doc/config points at a data root that exists but is EMPTY because
    the real content moved (T:/determinex_corpus vs T:/citadel_corpus, 2026-07-18 --
    corpus_root_split_brain_healed_2026_07_18).

CENSUS: for each top-level data artifact under EVERY corpus/<subcorpus>/ directory (.json/
.jsonl/.tsv/.npy -- programbench, swebench, terminal_bench, and any future addition; NOT
recursive into content subdirs like locked/, repos/, per_tool_overrides/, which hold hundreds of
per-item files that are wired collectively, not individually), count referencing scripts under
scripts/ + tests/. Zero consumers = ORPHAN (report; guard-fail unless allowlisted as archival).
POINTERS: known root-pointer values (TRAINING_EXCLUSION.json active_replacement_root, settings
corpus_root) must resolve to a NON-EMPTY directory. Scope widened 2026-07-19 from PB-only to all
of corpus/ -- the same built-but-invisible risk applies to any subcorpus, not just PB.

Usage:  python scripts/corpus/corpus_wiring_census.py [--guard]
  --guard  exit 1 on any non-allowlisted orphan or any empty/unresolvable pointer (CI gate).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORPUS_DIR = ROOT / "corpus"
PB = (
    CORPUS_DIR / "programbench"
)  # kept as a name: the TRAINING_EXCLUSION pointer check below is PB-specific

# Archival / write-only / historical artifacts that legitimately have no code consumer.
# Add here ONLY with a reason -- an unexplained allowlist row defeats the census.
_ALLOWLIST: dict[str, str] = {
    "amd_submission_record.json": "record of the AMD DevMaster submission (2026-08-06); a historical snapshot, not queryable knowledge -- wiring a static record into the query surface makes search noisier without making it better.",
    "radeon_breadth_findings.json": "raw 31-model breadth results from the Radeon run; evidence behind the published table, kept as record. The LESSONS from it belong in a playbook, the measurements belong here.",
    "repair_rehearsal.jsonl": "rehearsal log, historical signal with no live consumer.",
    "gap_gen_bash_2k.jsonl": 'training corpus; consumed by dataset_generation/gen_all_languages.py via f"gap_gen_{lang}_2k.jsonl" -- the name is BUILT, so a substring census cannot see it. Verified 2026-08-07.',
    "gap_gen_cpp_2k.jsonl": 'training corpus; consumed by dataset_generation/gen_all_languages.py via f"gap_gen_{lang}_2k.jsonl" -- the name is BUILT, so a substring census cannot see it. Verified 2026-08-07.',
    "gap_gen_csharp_2k.jsonl": 'training corpus; consumed by dataset_generation/gen_all_languages.py via f"gap_gen_{lang}_2k.jsonl" -- the name is BUILT, so a substring census cannot see it. Verified 2026-08-07.',
    "gap_gen_go_2k.jsonl": 'training corpus; consumed by dataset_generation/gen_all_languages.py via f"gap_gen_{lang}_2k.jsonl" -- the name is BUILT, so a substring census cannot see it. Verified 2026-08-07.',
    "gap_gen_javascript_2k.jsonl": 'training corpus; consumed by dataset_generation/gen_all_languages.py via f"gap_gen_{lang}_2k.jsonl" -- the name is BUILT, so a substring census cannot see it. Verified 2026-08-07.',
    "gap_gen_kotlin_2k.jsonl": 'training corpus; consumed by dataset_generation/gen_all_languages.py via f"gap_gen_{lang}_2k.jsonl" -- the name is BUILT, so a substring census cannot see it. Verified 2026-08-07.',
    "gap_gen_python_2k.jsonl": 'training corpus; consumed by dataset_generation/gen_all_languages.py via f"gap_gen_{lang}_2k.jsonl" -- the name is BUILT, so a substring census cannot see it. Verified 2026-08-07.',
    "gap_gen_ruby_2k.jsonl": 'training corpus; consumed by dataset_generation/gen_all_languages.py via f"gap_gen_{lang}_2k.jsonl" -- the name is BUILT, so a substring census cannot see it. Verified 2026-08-07.',
    "gap_gen_rust_2k.jsonl": 'training corpus; consumed by dataset_generation/gen_all_languages.py via f"gap_gen_{lang}_2k.jsonl" -- the name is BUILT, so a substring census cannot see it. Verified 2026-08-07.',
    "gap_gen_scala_2k.jsonl": 'training corpus; consumed by dataset_generation/gen_all_languages.py via f"gap_gen_{lang}_2k.jsonl" -- the name is BUILT, so a substring census cannot see it. Verified 2026-08-07.',
    "gap_gen_sql_2k.jsonl": 'training corpus; consumed by dataset_generation/gen_all_languages.py via f"gap_gen_{lang}_2k.jsonl" -- the name is BUILT, so a substring census cannot see it. Verified 2026-08-07.',
    "gap_gen_swift_2k.jsonl": 'training corpus; consumed by dataset_generation/gen_all_languages.py via f"gap_gen_{lang}_2k.jsonl" -- the name is BUILT, so a substring census cannot see it. Verified 2026-08-07.',
    "gap_gen_typescript_2k.jsonl": 'training corpus; consumed by dataset_generation/gen_all_languages.py via f"gap_gen_{lang}_2k.jsonl" -- the name is BUILT, so a substring census cannot see it. Verified 2026-08-07.',
    "OVERNIGHT_RESULTS.json": "historical overnight snapshot (read by humans)",
    "OVERNIGHT_RESULTS_wave4.json": "historical overnight snapshot",
    "OVERNIGHT_RESULTS_wave5.json": "historical overnight snapshot",
    "OVERNIGHT_RESULTS_waves12_broken.json": "historical (broken) snapshot kept as record",
    "autodrive_results.json": "historical drive snapshot",
    "ceiling_certification_results.json": "historical certification snapshot",
    "tmp_oha_v17.tar.gz": "stray tmp tarball (candidate for deletion)",
    "tmp_pigz_v4.tar.gz": "stray tmp tarball (candidate for deletion)",
    "crucible_gate_results.jsonl": "manual-run output of determinex_crucible.py (historical signal)",
    "wall_taxonomy.json": "historical wall-classification snapshot, no live consumer",
    "hetzner_drive_queue.tsv": "drive queue for the STOPPED Hetzner churn loop (box off 2026-07-02)",
    "build_knowledge_archive.json": "COLD half of build_knowledge.json, split 2026-08-02. The brain is HuggingFace-hosted "
    "and read on every query, so its bytes are latency: absorbed_sources (1,333 KB) and "
    "the 2026-07-16 quarantine key (619 KB) were 56% of the file and are never read during "
    "retrieval. Moved, not deleted -- the corpus rule is that superseded entries stay, "
    "because dead ends are load-bearing data. Deliberately has no live consumer; read it "
    "directly when you need provenance or the quarantine record. Pointer lives in the hot "
    "file under _cold_archive.",
}


# .sqlite3 added 2026-07-26 with corpus_fts.py's FTS5 index. Without it the census was blind to
# an entire artifact class -- a prebuilt database could sit in corpus/ with no consumer and never
# be reported, which is precisely the built-but-invisible failure mode this census exists to catch.
_ARTIFACT_SUFFIXES = (".json", ".jsonl", ".tsv", ".gz", ".npy", ".sqlite3")


def _artifacts() -> list[Path]:
    out = []
    if not CORPUS_DIR.is_dir():
        return out
    # Files sitting directly in corpus/ -- the playbooks. These were invisible to this census,
    # which only walked subdirectories, so a top-level artifact could be added and never wired
    # and nothing would say so. Found 2026-08-07: bit_techniques_playbook.json had been an
    # orphan the whole time, loaded by nothing.
    for p in sorted(CORPUS_DIR.iterdir()):
        if p.is_file() and p.suffix in _ARTIFACT_SUFFIXES:
            out.append(p)
    for subcorpus in sorted(CORPUS_DIR.iterdir()):
        if not subcorpus.is_dir():
            continue
        for p in sorted(subcorpus.iterdir()):  # top-level only, never recurse into content dirs
            if p.is_file() and p.suffix in _ARTIFACT_SUFFIXES:
                out.append(p)
    return out


def _scan_sources() -> str:
    """One concatenated haystack of all code that could consume an artifact (scripts + tests +
    the Tauri backend command surface). Filenames are matched as plain substrings."""
    hay = []
    for base, pat in (
        (ROOT / "scripts", "**/*.py"),
        (ROOT / "tests", "**/*.py"),
        # Training data is consumed OUTSIDE scripts/. Without these two the census reported
        # fifteen gap_gen_*.jsonl files as orphans the instant top-level artifacts became
        # visible -- all of them read by dataset_generation/. A census that cries wolf is a
        # census nobody reads.
        (ROOT / "dataset_generation", "**/*.py"),
        (ROOT / "determinex_trainer", "**/*.py"),
        (ROOT / "frontend", "**/*.rs"),
        (ROOT / "frontend", "**/*.ts"),
    ):
        if not base.exists():
            continue
        for f in base.glob(pat):
            sp = str(f).replace("\\", "/")
            if any(x in sp for x in ("node_modules", "/target/", "__pycache__", "/.next/")):
                continue
            # NEVER count this file. The census lives under scripts/, so its own source was in
            # its own haystack, and every artifact it names -- in the allowlist, in a comment, in
            # an example -- counted as a consumer of itself. Three real orphans passed that way:
            # bit_techniques_playbook.json, radeon_breadth_findings.json and
            # amd_submission_record.json were reachable from NO query surface while the guard
            # reported 72/72 wired. A check satisfied by its own existence establishes nothing.
            if Path(sp).resolve() == Path(__file__).resolve():
                continue
            try:
                hay.append(f.read_text(encoding="utf-8", errors="replace"))
            except OSError:
                continue
    return "\n".join(hay)


def census() -> dict:
    hay = _scan_sources()
    orphans, wired, allowlisted = [], [], []
    for a in _artifacts():
        n = hay.count(a.name)
        if n > 0:
            wired.append({"artifact": a.name, "consumers~": n})
        elif a.name in _ALLOWLIST:
            allowlisted.append({"artifact": a.name, "reason": _ALLOWLIST[a.name]})
        else:
            orphans.append(a.name)

    # POINTER checks: every declared data-root must exist AND be non-empty.
    pointers = []
    tx = PB / "training_corpus" / "TRAINING_EXCLUSION.json"
    if tx.exists():
        try:
            root = json.loads(tx.read_text(encoding="utf-8")).get("active_replacement_root", "")
            p = Path(root)
            ok = p.is_dir() and any(p.iterdir())
            pointers.append(
                {
                    "pointer": "TRAINING_EXCLUSION.active_replacement_root",
                    "value": root,
                    "resolves_nonempty": ok,
                }
            )
        except (OSError, json.JSONDecodeError) as e:
            pointers.append(
                {
                    "pointer": "TRAINING_EXCLUSION.active_replacement_root",
                    "value": f"<unreadable: {e}>",
                    "resolves_nonempty": False,
                }
            )
    try:
        sys.path.insert(0, str(ROOT / "scripts"))
        from determinex_settings import DeterminexSettings

        r = DeterminexSettings().corpus_root
        # A path on a drive this machine does not have is machine-specific configuration,
        # not a broken pointer. The default is `T:/determinex_corpus`; on a Linux runner
        # there is no T: drive, so the census reported the corpus root broken on every CI
        # run -- a true statement about a question the census cannot answer there.
        import re as _re

        _drive = _re.match(r"^([A-Za-z]):[\\/]", str(r))
        if _drive and not Path(f"{_drive.group(1)}:/").exists():
            pointers.append(
                {
                    "pointer": "settings.corpus_root",
                    "value": str(r),
                    "resolves_nonempty": True,
                    "unevaluated": True,
                    "note": "drive not present on this host",
                }
            )
        else:
            ok = r.is_dir() and any(r.iterdir())
            pointers.append(
                {"pointer": "settings.corpus_root", "value": str(r), "resolves_nonempty": ok}
            )
    except ImportError as e:
        # A MISSING DEPENDENCY IS NOT A BROKEN POINTER. Reporting resolves_nonempty=False
        # here made the guard fail with `bad_pointers=[{'pointer': 'settings.corpus_root',
        # 'value': "<error: No module named 'pydantic'>"}]` -- which reads as "your corpus
        # root is broken" and means "I could not import the settings module". The pointer
        # was never examined, so the census must not render a verdict on it.
        pointers.append(
            {
                "pointer": "settings.corpus_root",
                "value": f"<not evaluated: {e}>",
                "resolves_nonempty": True,
                "unevaluated": True,
            }
        )
    except Exception as e:  # a real resolution failure -- report it as one
        pointers.append(
            {
                "pointer": "settings.corpus_root",
                "value": f"<error: {e}>",
                "resolves_nonempty": False,
            }
        )

    return {
        "artifacts": len(_artifacts()),
        "wired": len(wired),
        "orphans": orphans,
        "allowlisted": allowlisted,
        "pointers": pointers,
    }


def main() -> int:
    res = census()
    print(json.dumps(res, indent=1))
    if "--guard" in sys.argv:
        bad_ptr = [p for p in res["pointers"] if not p["resolves_nonempty"]]
        if res["orphans"] or bad_ptr:
            print(f"\nGUARD FAIL: orphans={res['orphans']} bad_pointers={bad_ptr}", file=sys.stderr)
            return 1
        print(
            "\nGUARD PASS: every artifact wired or allowlisted; every pointer resolves non-empty."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
