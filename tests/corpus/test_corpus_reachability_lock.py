"""Guards on corpus REACHABILITY -- can the corpus actually answer from everything it holds?

WHY THIS IS SEPARATE FROM THE WIRING CENSUS.

The census reported **72 artifacts, 72 wired, 0 orphans** while four files holding 47 entries were
reachable from no query path at all: `bit_techniques_playbook.json` (twelve verifiable oracle
contracts), `external_references.json` (thirty sources), `radeon_breadth_findings.json` and
`amd_submission_record.json`. It was green because its own source lives under `scripts/` and was
therefore inside its own haystack -- every filename it mentioned, including in its allowlist,
counted as a consumer of itself. Excluding that one file moved it from 72 wired to 48 wired plus
24 allowlisted.

So the census answers "is this filename mentioned anywhere?". The question anyone actually has is
"if I ask the corpus, can it answer from this?" -- and those differ exactly when it matters. This
file guards the second question, and it guards it by EXERCISING each path rather than grepping
for evidence that it exists.

The stake is not tidiness: the publish path reads the query surface, so an artifact the query
surface cannot see is silently missing from anything ever published.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "scripts"))

import determinex_corpus_api as api  # noqa: E402
import determinex_corpus_share as sh  # noqa: E402

from corpus import corpus_reachability_audit as ra  # noqa: E402

CORPUS_DIR = _ROOT / "corpus"


# ── the registry is the single source of truth ───────────────────────────────


def test_every_top_level_corpus_file_has_a_registry_row():
    """The failure this whole file exists to prevent: a file added to corpus/ that no loader,
    no search and no export knows about. Adding a row is the one step, and forgetting it is what
    left four artifacts invisible for weeks."""
    registered = {a["file"] for a in api.registered_artifacts()}
    on_disk = {p.name for p in CORPUS_DIR.glob("*.json")}
    missing = on_disk - registered
    assert not missing, (
        f"corpus/{sorted(missing)} exist with no _ARTIFACT_REGISTRY row -- they are invisible to "
        "search and absent from every export. Add a row."
    )


def test_every_registry_row_points_at_a_real_file():
    """A row for a deleted file makes the registry lie in the other direction."""
    for a in api.registered_artifacts():
        assert (CORPUS_DIR / a["file"]).exists(), f"{a['file']} is registered but missing"


def test_every_registry_row_declares_its_export_label():
    """`kind` and `export_as` are different questions. Four artifacts share kind "playbook" while
    meaning two different things to a consumer, and deriving the label from the kind collapsed 16
    engineering lessons into design_knowledge the moment the export became registry-driven."""
    for a in api.registered_artifacts():
        if a.get("exportable"):
            assert a.get("export_as"), f"{a['file']} is exportable with no export_as label"


# ── each access path, exercised ──────────────────────────────────────────────


def test_every_searchable_artifact_can_be_found_by_its_own_words():
    """If an entry's own identifier cannot surface it, nothing a user types will."""
    for a in api.registered_artifacts(searchable_only=True):
        entries = api.artifact_entries(a["file"])
        if not entries:
            continue
        ident = next(iter(entries))
        import re

        probe = " ".join(w for w in re.split(r"[^A-Za-z0-9]+", ident) if len(w) > 2)
        hits = api.search(probe, limit=10)
        assert any(h.key == ident for h in hits), (
            f"{a['file']}: entry {ident!r} is not findable by its own words"
        )


def test_snake_case_ids_are_findable_by_their_words():
    """`_tokens` keeps underscores, so `population_count` is ONE token and a search for the two
    words a person would actually type could never match it."""
    hits = api.search("population count", limit=10)
    assert any(h.key == "population_count" for h in hits)


def test_the_loader_handles_every_shape_these_files_use():
    """A second parser was written for the audit and immediately diverged -- it looked for `id`
    while external_references.json keys on `url`, and reported 30 reachable entries as invisible.
    One loader, exercised against every real file."""
    for a in api.registered_artifacts():
        entries = api.artifact_entries(a["file"])
        assert isinstance(entries, dict)
        for k, v in entries.items():
            assert k and isinstance(v, dict), f"{a['file']} yielded a malformed entry"


def test_the_reachability_audit_finds_nothing_invisible():
    """The live assertion. Anything here is content the corpus holds and cannot answer from."""
    result = ra.audit()
    invisible = [r["artifact"] for r in result["invisible"]]
    assert not invisible, f"unreachable corpus artifacts: {invisible}"


# ── the publish path carries what the registry says it should ────────────────


def test_the_export_carries_every_exportable_artifact():
    """The export read a hardcoded list of three playbooks while seven artifacts existed, so
    bit_techniques_playbook -- twelve verifiable oracle contracts, exactly what the dataset is
    for -- was absent from every payload with nothing in the output saying so."""
    exportable = [a for a in api.registered_artifacts() if a.get("exportable")]
    published = {r["id"] for r in sh._rows()}
    for a in exportable:
        ids = set(api.artifact_entries(a["file"]))
        missing = ids - published
        assert not missing, f"{a['file']}: {len(missing)} entries never reach the payload"


def test_non_exportable_artifacts_stay_home():
    """`exportable=False` is a decision, not an oversight. Breadth findings and the submission
    record are OUR measurements of OUR hardware and OUR entry -- local corpus, not public
    dataset of transferable lessons."""
    published = {r["id"] for r in sh._rows()}
    for a in api.registered_artifacts():
        if a.get("exportable"):
            continue
        leaked = set(api.artifact_entries(a["file"])) & published
        assert not leaked, f"{a['file']} leaked into the published payload: {sorted(leaked)[:3]}"


def test_export_labels_survive_the_registry():
    """16 engineering lessons must not be published as design knowledge."""
    by_source: dict[str, int] = {}
    for r in sh._rows():
        by_source[r["source"]] = by_source.get(r["source"], 0) + 1
    assert by_source.get("engineering_lesson", 0) >= 10
    assert by_source.get("design_knowledge", 0) >= 10


# ── incremental publish ──────────────────────────────────────────────────────


def test_remote_digest_is_none_for_absent_files_and_repos():
    """Any failure must mean "assume changed". An unnecessary upload is harmless; skipping an
    upload of genuinely new content is not."""
    assert sh._remote_digest("nobody/does-not-exist-xyz-determinex", "README.md") is None


def test_publish_compares_content_not_timestamps():
    """Regenerating the payload rewrites every staged file with a fresh `generated_at`, so mtime
    always differs and an mtime comparison would upload everything, every time -- defeating the
    only reason the delta exists."""
    src = (_ROOT / "scripts" / "determinex_corpus_share.py").read_text(encoding="utf-8")
    block = src[src.index("# ONLY WHAT CHANGED.") :]
    head = block[: block.index("if not changed:")]
    assert "hashlib.sha256" in head, "the delta no longer compares content"
    assert "st_mtime" not in head and "getmtime" not in head


def test_the_payload_is_json_serialisable_and_row_shaped():
    payload = sh.build_payload()
    json.dumps(payload)
    assert payload["n_rows"] == len(payload["rows"])
    assert payload["n_rows"] > 300
