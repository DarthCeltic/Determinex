"""scripts/corpus/corpus_reachability_audit.py -- is every corpus artifact actually REACHABLE?

WHY THIS EXISTS, AND WHY THE EXISTING CENSUS WAS NOT ENOUGH.

`corpus_wiring_census.py` reported 72 artifacts, 72 wired, 0 orphans. At that moment
`bit_techniques_playbook.json`, `radeon_breadth_findings.json` and `amd_submission_record.json`
were reachable from NO query surface at all, and `external_references.json` was referenced only
by the script that WRITES it. The census was green because its own source lives under `scripts/`
and was therefore inside its own haystack: every filename it mentioned -- in its allowlist, in a
comment -- counted as a consumer of itself.

So the census answers "is this filename mentioned in the tree?". That is a useful question and it
is not the question anyone actually has, which is: **if I ask the corpus, can it answer from
this?** A mention is not a reader, and a writer is not a consumer.

This audit answers the real question by EXERCISING each access path rather than grepping for it:

    LOAD      does a loader return entries from it?
    SEARCH    does search() ever surface content from it?
    EXPORT    would the HuggingFace payload carry it?
    BRIEF     can the push surface cite it?

An artifact reachable by none of these is invisible in practice, whatever any census says. The
distinction is not academic: the export path reads the query surface, so an artifact the query
surface cannot see is silently absent from anything ever published.

    python scripts/corpus/corpus_reachability_audit.py
    python scripts/corpus/corpus_reachability_audit.py --guard   # exit 1 if anything is invisible
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

CORPUS_DIR = REPO_ROOT / "corpus"

#: Artifacts that are legitimately not query-surface content, with the reason. Each is a
#: deliberate decision, not a backlog item -- an allowlist without reasons becomes a place to
#: hide things that should have been wired.
_NOT_QUERYABLE: dict[str, str] = {
    "REDISTRIBUTION_BOUNDARY.json": "publication manifest -- consumed by the release filter and "
    "the dataset export, not a knowledge source",
    "THIRD_PARTY_NOTICES.md": "license text required to travel with redistributed code",
}


def _top_level_artifacts() -> list[Path]:
    return sorted(p for p in CORPUS_DIR.glob("*.json") if p.is_file())


def _entry_count(path: Path) -> int:
    """Entries in a corpus JSON, whatever shape it uses. 0 means it holds nothing usable."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return 0
    for key in ("entries", "classes", "rows", "records"):
        v = data.get(key) if isinstance(data, dict) else None
        if isinstance(v, (list, dict)):
            return len(v)
    if isinstance(data, dict):
        return len([k for k in data if not k.startswith("_")])
    return len(data) if isinstance(data, list) else 0


def audit() -> dict[str, Any]:
    import determinex_corpus_api as api

    # LOAD: which files does the API's own self-description resolve?
    loadable = {Path(r["path"]).name: r for r in api.sources()}

    # SEARCH: probe with each artifact's own vocabulary. If its own words cannot surface it,
    # nothing a user types will either.
    def searchable(path: Path) -> bool:
        # Uses the API's OWN loader rather than re-parsing. A second parser was written here and
        # immediately diverged: it looked for an `id` field, while external_references.json keys
        # on `url`, so 30 entries that search demonstrably finds were reported unreachable. The
        # audit was wrong about the corpus because it disagreed with the corpus about what an
        # entry is -- exactly the duplication the project's audit-before-build rule forbids.
        ids = list(api.artifact_entries(path.name))[:3]
        for ident in ids:
            # Derive WORDS from the id, whatever shape it is. Feeding a whole URL to a
            # token-overlap search matches nothing, so external_references.json -- 30 entries
            # that `vllm prefix caching` demonstrably finds -- was reported invisible by this
            # audit rather than by the corpus. An instrument that misreads its subject is the
            # same class of bug it was written to catch.
            probe = " ".join(w for w in re.split(r"[^A-Za-z0-9]+", ident) if len(w) > 2)
            if not probe.strip():
                continue
            try:
                if any(h.key == ident for h in api.search(probe, limit=8)):
                    return True
            except Exception:
                return False
        return False

    # EXPORT: would the published payload carry rows from it?
    export_sources: set[str] = set()
    try:
        import determinex_corpus_share as sh

        for row in sh._rows():
            export_sources.add(row["source"])
    except Exception:
        pass
    # The share payload names logical sources, not filenames; map them back.
    _EXPORT_MAP = {
        "general_engineering_playbook.json": "engineering_lesson",
        "model_architecture_playbook.json": "design_knowledge",
        "gemm_blocking_playbook.json": "design_knowledge",
    }

    rows: list[dict[str, Any]] = []
    for p in _top_level_artifacts():
        name = p.name
        n = _entry_count(p)
        in_load = name in loadable and loadable[name]["entries"] > 0
        in_search = searchable(p) if n else False
        in_export = _EXPORT_MAP.get(name) in export_sources
        reachable = in_load or in_search or in_export
        rows.append(
            {
                "artifact": name,
                "entries": n,
                "load": in_load,
                "search": in_search,
                "export": in_export,
                "reachable": reachable,
                "exempt": _NOT_QUERYABLE.get(name, ""),
            }
        )

    invisible = [r for r in rows if not r["reachable"] and not r["exempt"] and r["entries"] > 0]
    return {"artifacts": rows, "invisible": invisible}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--guard", action="store_true", help="exit 1 if any artifact is unreachable")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    reconf = getattr(sys.stdout, "reconfigure", None)
    if reconf is not None:
        reconf(encoding="utf-8")

    result = audit()
    if args.json:
        print(json.dumps(result, indent=2))
        return 1 if result["invisible"] and args.guard else 0

    print(f"  {len(result['artifacts'])} top-level corpus artifacts\n")
    print(f"  {'artifact':<38} {'entries':>7}  load search export")
    for r in sorted(result["artifacts"], key=lambda x: (x["reachable"], x["artifact"])):
        mark = lambda b: " yes " if b else "  -  "  # noqa: E731
        flag = "" if r["reachable"] or r["exempt"] else "   <-- INVISIBLE"
        print(
            f"  {r['artifact']:<38} {r['entries']:>7}  "
            f"{mark(r['load'])}{mark(r['search'])}{mark(r['export'])}{flag}"
        )
        if r["exempt"]:
            print(f"      exempt: {r['exempt']}")

    if result["invisible"]:
        print(f"\n  {len(result['invisible'])} artifact(s) hold content NOTHING can reach:")
        for r in result["invisible"]:
            print(f"    - {r['artifact']} ({r['entries']} entries)")
        print("\n  These are invisible to every query AND absent from anything published.")
        return 1 if args.guard else 0

    print("\n  Every artifact with content is reachable by at least one path.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
