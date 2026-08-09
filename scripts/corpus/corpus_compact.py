"""scripts/corpus/corpus_compact.py — distil learned entries into small memory packets.

WHY THIS EXISTS. The corpus grows monotonically: 233 build-knowledge entries, 272 learned
classes, 89 class patterns, and more every time something fails. That is the right behaviour for
a record and the wrong shape for a PROMPT. A builder prompt has a budget of a few hundred tokens
for accumulated knowledge, so a corpus that only grows becomes a corpus that can never be
consulted at the moment it would help.

Compaction is the other half of the flywheel. Ingest and learn produce specific entries; this
turns a family of specific entries into ONE general packet small enough to carry, while keeping
a pointer back to the sources so the detail is never lost -- only deferred.

    specific:  "go.mod pins 1.21 but a dep needs 1.22, and `auto` silently wins"      (x7 tools)
    packet:    "a stale toolchain pin loses to auto-resolution; pin forward, not back"

THE RULE THAT KEEPS IT HONEST. A packet must name the entries it replaced (`sources`) and must
never be the only copy. Compaction is a VIEW over the corpus, written to its own file, and the
originals stay exactly where they were. A lossy summary that overwrites its inputs is not
compaction, it is data loss with a nicer name.

WHAT IS NOT DONE HERE. No model is called. Grouping is by declared category and shared tokens,
which is deterministic and reviewable; a packet's wording comes from the highest-signal member
rather than from generated prose. An LLM-written summary would be a claim nobody verified, and
the whole point of this corpus is that claims carry evidence.

    python scripts/corpus/corpus_compact.py                # report what would compact
    python scripts/corpus/corpus_compact.py --write        # write corpus/memory_packets.json
    python scripts/corpus/corpus_compact.py --budget 1200  # packets that fit N characters
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

PACKETS_PATH = REPO_ROOT / "corpus" / "memory_packets.json"

#: A family smaller than this is not worth a packet -- one entry compacted is just the entry.
MIN_FAMILY = 3
#: Shared vocabulary required to call two entries the same lesson. Two tokens produced families
#: of 102 whose carrier text was about one specific tool -- a packet that claims to cover a
#: hundred entries while describing one of them is a false summary, which is worse than none.
MIN_OVERLAP = 5
#: Jaccard, not raw count. Two 80-token narratives sharing 5 tokens are 3% alike; two 12-token
#: symptom/fix pairs sharing 5 are 40% alike -- and a raw threshold cannot tell them apart. That
#: is what grouped "a capture reports success for a stalled subject" with "git stash roundtrip
#: as a measurement tool": generic vocabulary, nothing in common.
MIN_SIMILARITY = 0.34
#: Above this a "family" is not a family, it is the grouper failing open. Real lesson families
#: in this corpus are single digits; a group of 76 means the threshold let noise in.
MAX_FAMILY = 12
#: A carrier must actually SAY the shared thing. Below this fraction of the family's shared
#: vocabulary, the text is about its own specific case and cannot speak for the others.
MIN_CARRIER_COVERAGE = 0.6
#: Packets are for carrying, so each one is capped. Over this and it is a document, not a packet.
MAX_PACKET_CHARS = 240
#: Words too common to group on.
_STOP = frozenset(
    """the a an and or but if then than that this these those is are was were be been being
    to of in on at by for with from as it its it's not no do does did done can could should
    would will when where which who whom what how why all any some each every more most other
    into over under again further once here there both few own same so only very just also""".split()
)


def _tokens(text: str) -> set[str]:
    out = set()
    for raw in str(text).lower().replace("_", " ").replace("-", " ").split():
        w = "".join(ch for ch in raw if ch.isalnum())
        if len(w) > 3 and w not in _STOP:
            out.add(w)
    return out


def _sources() -> list[dict[str, Any]]:
    """Every learned item, flattened to a common shape: id, text, category, origin."""
    import determinex_corpus_api as api

    rows: list[dict[str, Any]] = []

    kn = api.load_corpus()
    for key, val in (kn.get("class_patterns") or {}).items():
        if not isinstance(val, dict):
            continue
        text = " ".join(
            str(val.get(f, "")) for f in ("symptom", "fix", "detect", "rule", "generalized_in")
        ).strip()
        if text:
            rows.append(
                {"id": key, "text": text, "category": "build_failure", "origin": "class_patterns"}
            )

    for key, val in (kn.get("learned_classes") or {}).items():
        if not isinstance(val, dict):
            continue
        text = " ".join(str(val.get(f, "")) for f in ("lesson", "symptom", "fix", "summary"))
        if text.strip():
            rows.append(
                {
                    "id": key,
                    "text": text.strip(),
                    "category": str(val.get("category") or "learned"),
                    "origin": "learned_classes",
                }
            )

    for loader, origin in (
        (api.general_engineering_playbook, "general_engineering_playbook"),
        (getattr(api, "model_architecture_playbook", dict), "model_architecture_playbook"),
        (getattr(api, "gemm_blocking_playbook", dict), "gemm_blocking_playbook"),
    ):
        for key, val in (loader() or {}).items():
            if not isinstance(val, dict):
                continue
            text = " ".join(
                str(val.get(f, ""))
                for f in ("lesson", "why_it_generalizes", "generalised", "used_when")
            ).strip()
            if text:
                rows.append(
                    {
                        "id": key,
                        "text": text,
                        "category": str(val.get("category") or "engineering"),
                        "origin": origin,
                    }
                )
    return rows


def _families(rows: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    """Group by declared category, then split on shared vocabulary.

    Deterministic on purpose. A clustering that changes between runs would make the packet set
    unreviewable, and an unreviewable summary of the corpus is worse than no summary.
    """
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_cat[r["category"]].append(r)

    families: list[list[dict]] = []
    for _cat, members in by_cat.items():
        if len(members) < MIN_FAMILY:
            continue
        # Seed on the most token-rich member and attach anything sharing >= 2 tokens with it.
        pool = sorted(members, key=lambda m: -len(_tokens(m["text"])))
        used: set[str] = set()
        for seed in pool:
            if seed["id"] in used:
                continue
            stoks = _tokens(seed["text"])
            fam = [seed]
            used.add(seed["id"])
            for other in pool:
                if other["id"] in used:
                    continue
                if len(fam) >= MAX_FAMILY:
                    break
                otoks = _tokens(other["text"])
                inter = len(stoks & otoks)
                union = len(stoks | otoks) or 1
                if inter >= MIN_OVERLAP and inter / union >= MIN_SIMILARITY:
                    fam.append(other)
                    used.add(other["id"])
            if len(fam) >= MIN_FAMILY:
                families.append(fam)
            else:
                # Release the members: a seed that gathered nobody must not consume entries
                # that could group with a later seed.
                for m in fam:
                    used.discard(m["id"])
                used.add(seed["id"])
    return families


def _packet(family: list[dict[str, Any]]) -> dict[str, Any]:
    """One packet from one family. Wording is TAKEN, never generated.

    The shortest member that still carries the family's shared vocabulary is the best carrier:
    it is the one that said the general thing without the tool-specific framing.
    """
    shared: set[str] = set.intersection(*(_tokens(m["text"]) for m in family)) or set()
    scored = sorted(
        family,
        key=lambda m: (-(len(_tokens(m["text"]) & shared)), len(m["text"])),
    )
    carrier = scored[0]
    text = carrier["text"]
    if len(text) > MAX_PACKET_CHARS:
        text = text[: MAX_PACKET_CHARS - 1].rsplit(" ", 1)[0] + "…"
    return {
        "id": f"packet_{carrier['id']}",
        "category": carrier["category"],
        "packet": text,
        "covers": len(family),
        # Provenance is not optional. A packet whose sources are unknown cannot be checked, and
        # an unverifiable summary of verified knowledge throws away the only property that made
        # the corpus worth having.
        "sources": sorted(m["id"] for m in family),
        "origins": sorted({m["origin"] for m in family}),
        "shared_terms": sorted(shared)[:8],
    }


#: Memo keyed on the source files' (mtime, size). compact() costs ~750 ms and is called on every
#: builder prompt; without this a 50-step DAG spends minutes re-deriving an identical answer.
#: NOT a TTL cache -- a TTL serves stale packets for its whole window after the flywheel learns
#: something, which is precisely when the new lesson is most worth carrying.
_CACHE: tuple[tuple, list[dict[str, Any]]] | None = None


#: The source files whose contents decide the packets. Named explicitly rather than discovered,
#: so adding a source without adding it here is a visible omission rather than a silent one.
_FINGERPRINT_ATTRS: tuple[str, ...] = (
    "DEFAULT_PATH",  # build_knowledge.json -- class_patterns + learned_classes
    "GENERAL_PLAYBOOK_PATH",
    "MODEL_ARCH_PLAYBOOK_PATH",
    "GEMM_PLAYBOOK_PATH",
)


def _fingerprint() -> tuple | None:
    """Cheap identity of everything compaction reads. Any write to any source changes it.

    Returns None -- meaning DO NOT CACHE -- if a named source cannot be resolved. That case is
    not hypothetical: the first version of this used a constant name that does not exist
    (`CORPUS_PATH`), `getattr(..., None)` swallowed it, and the main corpus dropped out of the
    key entirely. The cache still looked correct and would have served stale packets forever
    after a flywheel write. Failing closed makes a missing source cost speed, never freshness.
    """
    import determinex_corpus_api as api

    out = []
    for name in _FINGERPRINT_ATTRS:
        pth = getattr(api, name, None)
        if pth is None:
            return None
        try:
            st = Path(pth).stat()
            out.append((str(pth), st.st_mtime_ns, st.st_size))
        except OSError:
            # A source that is absent is a real state, not an error -- an optional playbook may
            # simply not exist. Recorded as its own value so its later ARRIVAL invalidates.
            out.append((str(pth), 0, 0))
    return tuple(out)


def compact() -> list[dict[str, Any]]:
    global _CACHE
    fp = _fingerprint()
    if fp is not None and _CACHE is not None and _CACHE[0] == fp:
        return _CACHE[1]

    rows = _sources()
    packets = []
    for fam in _families(rows):
        pk = _packet(fam)
        # Reject a packet whose carrier does not carry. Publishing it would assert that N
        # entries share a lesson while quoting text that only describes one of them.
        shared = set(pk["shared_terms"])
        if shared and len(_tokens(pk["packet"]) & shared) / len(shared) < MIN_CARRIER_COVERAGE:
            continue
        packets.append(pk)
    result = sorted(packets, key=lambda p: -p["covers"])
    if fp is not None:
        _CACHE = (fp, result)
    return result


def for_prompt(budget_chars: int = 1200, category: str | None = None) -> list[str]:
    """The packets that fit a prompt budget, densest coverage first.

    This is the function the builder calls. It returns lines, not a blob, so the caller decides
    the framing -- and it returns FEWER lines rather than truncating one, because half a lesson
    is worse than none.
    """
    out: list[str] = []
    used = 0
    for p in compact():
        if category and p["category"] != category:
            continue
        line = f"- {p['packet']}"
        if used + len(line) > budget_chars:
            continue
        out.append(line)
        used += len(line)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--write", action="store_true", help="write corpus/memory_packets.json")
    ap.add_argument("--budget", type=int, help="show what fits N characters of prompt")
    args = ap.parse_args()

    reconf = getattr(sys.stdout, "reconfigure", None)
    if reconf is not None:
        reconf(encoding="utf-8")

    rows = _sources()
    packets = compact()
    covered = sum(p["covers"] for p in packets)
    print(f"  {len(rows)} learned items -> {len(packets)} packets covering {covered} of them")

    if args.budget:
        lines = for_prompt(args.budget)
        print(f"\n  fits {args.budget} chars: {len(lines)} packet(s)")
        for ln in lines:
            print("   " + ln[:110])
        return 0

    for p in packets[:12]:
        print(f"\n  [{p['covers']:>2} entries] {p['id']}")
        print(f"     {p['packet'][:150]}")
        print(f"     from: {', '.join(p['sources'][:4])}{' …' if len(p['sources']) > 4 else ''}")

    if args.write:
        PACKETS_PATH.write_text(
            json.dumps(
                {
                    "_doc": "Compacted memory packets, generated by scripts/corpus/"
                    "corpus_compact.py. A VIEW over the corpus: every packet names the "
                    "entries it summarises and none of them were modified. Regenerate "
                    "rather than hand-edit.",
                    "schema_version": 1,
                    "source_items": len(rows),
                    "entries": packets,
                },
                indent=1,
            ),
            encoding="utf-8",
            newline="\n",
        )
        print(f"\n  wrote {PACKETS_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
