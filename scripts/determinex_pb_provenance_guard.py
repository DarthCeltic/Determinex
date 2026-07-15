#!/usr/bin/env python3
"""
determinex_pb_provenance_guard.py -- anti-test-gaming guard (the credibility gate)
===============================================================================
The #1 "laughed at" risk: a locked binary that PASSES by DETECTING THE TEST (reads the test
name, embeds golden outputs, switches behavior on test identity) instead of IMPLEMENTING the
tool. One such tool found by a skeptic's grep discredits the entire board. This is distinct
from determinex_copyright_guard (which checks attribution vs registered references); this checks
that the binary EARNS its passes.

It scans each locked tool's SOURCE for gaming signatures and demands every hit be either
JUSTIFIED (recorded in provenance_justifications.json -- e.g. svd2rust-style per-context
routing where the contexts are genuinely distinct and the output is independently correct)
or treated as a RED violation. Surface + require justification = a skeptic's grep finds
nothing we haven't already audited.

Gaming signatures (RED unless justified):
  * reads test identity        PYTEST_CURRENT_TEST, sys.argv scan for test paths, stack-walk to test
  * embeds golden output        include_bytes!/include_str!/embed of golden|expected|snapshot|fixture
  * branches on test name       match/switch/if on a test-name string to choose output
Usage:
  python scripts/determinex_pb_provenance_guard.py            # report
  python scripts/determinex_pb_provenance_guard.py --guard    # exit 1 if any UNJUSTIFIED hit on a lock
"""
from __future__ import annotations

import json
import re
import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCKED = ROOT / "corpus" / "programbench" / "locked"
REG = ROOT / "corpus" / "programbench" / "verified_locks.json"
JUST = ROOT / "corpus" / "programbench" / "provenance_justifications.json"
# from-source PROOFS: a lock that ships a prebuilt binary is only cleared if its source
# build was independently verified (answer-key removed -> still builds + passes). Written by
# pb_provenance_verify. A shipped binary WITHOUT a proof here is an unverified credibility
# risk (the atlas failure mode) and fails the guard.
PROOFS = ROOT / "corpus" / "programbench" / "provenance_proofs.json"


def load_proofs() -> dict:
    if not PROOFS.exists():
        return {}
    try:
        return json.loads(PROOFS.read_text(encoding="utf-8")).get("from_source", {})
    except Exception:
        return {}


def record_proof(slug: str, info: dict) -> None:
    """Record a verified from-source build (clears the ships-prebuilt-binary flag)."""
    data = {"from_source": {}}
    if PROOFS.exists():
        try:
            data = json.loads(PROOFS.read_text(encoding="utf-8"))
            data.setdefault("from_source", {})
        except Exception:
            data = {"from_source": {}}
    data["from_source"][slug] = info
    PROOFS.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

GAMING = [
    ("reads-test-identity", re.compile(
        r"PYTEST_CURRENT_TEST|PYTEST_XDIST|getenv\([\"']PYTEST|"
        r"argv.*test_|inspect\.stack\(\).*test|__name__.*test_", re.I)),
    ("embeds-golden", re.compile(
        r"include_bytes!\s*\(\s*[\"'][^\"']*(golden|expected|snapshot|fixture|\.out)|"
        r"include_str!\s*\(\s*[\"'][^\"']*(golden|expected|snapshot|fixture)|"
        r"embed_file.*(golden|expected|snapshot)", re.I)),
    ("branch-on-test-name", re.compile(
        r"(match|switch|if|case)[^\n]{0,40}(test_[a-z0-9_]+)[^\n]{0,20}(=>|:|then|\{)|"
        r"==\s*[\"']test_[a-z0-9_]+[\"']", re.I)),
]
_SRC_EXT = (".rs", ".go", ".c", ".cpp", ".h", ".hpp", ".py", ".js", ".ts")


def load_just() -> dict:
    return json.loads(JUST.read_text(encoding="utf-8")) if JUST.exists() else {"justified": {}}


def scan_tool(tool: str) -> list[dict]:
    hits = []
    # SOURCE-SNAPSHOT scan: the submission.tar.gz is often gitignored (regenerable), so the
    # tracked evidence is locked/<tool>/source/. An answer-key ELF committed THERE is the same
    # credibility risk as one in the tarball -- scan it too (closes the prior blind spot where
    # the guard only opened the tarball and missed binaries committed in source/).
    src_dir = LOCKED / tool / "source"
    if src_dir.is_dir():
        for p in src_dir.rglob("*"):
            try:
                if p.is_file() and p.stat().st_size > 2_000_000:
                    with open(p, "rb") as fh:
                        if fh.read(4) == b"\x7fELF":
                            hits.append({"file": f"source/{p.relative_to(src_dir).as_posix()}",
                                         "kind": "ships-prebuilt-binary",
                                         "snippet": f"{p.stat().st_size // 1024 // 1024}MB ELF in tracked source/"})
            except Exception:
                continue
    tarp = LOCKED / tool / "submission.tar.gz"
    if not tarp.exists():
        return hits
    try:
        with tarfile.open(tarp, "r:gz") as t:
            for m in t.getmembers():
                n = m.name
                low = n.lower()
                # BUILD-PROVENANCE: a submission that SHIPS a prebuilt binary can pass by
                # falling back to that answer-key ELF instead of building from source (the
                # atlas failure mode: a 'lock' that was the official binary, not the build).
                # Any shipped large ELF is a credibility risk -> demand a from-source proof.
                if m.isfile() and m.size > 2_000_000:
                    magic = b""
                    try:
                        ef = t.extractfile(m)
                        if ef is not None:
                            magic = ef.read(4)
                    except Exception:
                        magic = b""
                    if magic == b"\x7fELF":
                        hits.append({"file": n, "kind": "ships-prebuilt-binary",
                                     "snippet": f"{m.size // 1024 // 1024}MB ELF shipped in submission"})
                        continue
                # SOURCE only (skip the shipped test files themselves)
                if not n.endswith(_SRC_EXT) or "/test" in low or low.startswith("test") or "conftest" in low:
                    continue
                try:
                    txt = t.extractfile(n).read().decode("utf-8", "replace")
                except Exception:
                    continue
                for kind, rx in GAMING:
                    mm = rx.search(txt)
                    if mm:
                        hits.append({"file": n, "kind": kind, "snippet": mm.group(0)[:80]})
    except Exception:
        pass
    return hits


def audit() -> dict:
    reg = list(json.loads(REG.read_text(encoding="utf-8"))["locks"]) if REG.exists() else []
    just = load_just().get("justified", {})
    proofs = load_proofs()
    flagged = {}
    for tool in sorted(reg):
        hits = scan_tool(tool)
        if not hits:
            continue
        # a hit clears if (a) recorded justified, OR (b) for ships-prebuilt-binary, a
        # from-source proof exists (the source build was verified without the answer key).
        def _cleared(h):
            if h["kind"] in just.get(tool, []):
                return True
            if h["kind"] == "ships-prebuilt-binary" and tool in proofs:
                return True
            return False
        unjust = [h for h in hits if not _cleared(h)]
        flagged[tool] = {"hits": hits, "unjustified": unjust,
                         "status": "JUSTIFIED" if not unjust else "NEEDS-REVIEW"}
    return {"scanned": len(reg), "flagged": flagged}


def main() -> int:
    r = audit()
    guard = "--guard" in sys.argv
    print(f"provenance/anti-gaming scan: {r['scanned']} locks")
    needs = {t: v for t, v in r["flagged"].items() if v["status"] == "NEEDS-REVIEW"}
    just = {t: v for t, v in r["flagged"].items() if v["status"] == "JUSTIFIED"}
    print(f"  JUSTIFIED (audited, recorded): {len(just)} {sorted(just)}")
    print(f"  NEEDS-REVIEW (potential gaming): {len(needs)}")
    for t, v in needs.items():
        for h in v["unjustified"][:3]:
            print(f"    {t}: {h['kind']} in {h['file']} -> {h['snippet']!r}")
    if guard and needs:
        print("\nPROVENANCE GUARD FAILED: unjustified test-gaming signatures on locked tools. "
              "Audit each: justify (genuinely-distinct context, independently-correct output) "
              "or fix the tool to implement the behavior. Record in provenance_justifications.json.")
        return 1
    if guard:
        print("\nPROVENANCE GUARD PASSED: no unjustified test-gaming on any lock.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
