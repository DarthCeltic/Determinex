#!/usr/bin/env python3
"""
determinex_corpus_share.py -- opt-in corpus signal sharing to HuggingFace
========================================================================
The flywheel learns from every oracle-verified solve: a symptom -> fix class that the
grounded fixer applies first on the next occurrence. Those classes are the product's real
compounding asset, and they get better the more machines contribute.

They are also derived from THE OPERATOR'S SOURCE CODE, which is the one thing this project
exists to keep local. So sharing is:

  * **OFF by default.** Not "on with a setting to disable" -- absent consent, nothing leaves.
  * **Explicit.** `DETERMINEX_CORPUS_SHARE=1` plus a recorded consent record. A flag alone is
    not consent; a flag can be set by a script the operator never read.
  * **Redacted before it leaves.** A class is a generalized rule, but it is distilled FROM a
    specific repository, and the distillation can carry identifiers, paths and fragments.
    Everything is scrubbed and then RE-SCANNED, because a redactor that is never checked is
    a redactor nobody knows the coverage of.
  * **Previewable.** `--dry-run` prints the exact payload. Nobody should have to trust a
    description of what is about to be uploaded when they can read the bytes.

    python scripts/determinex_corpus_share.py --dry-run     # see exactly what would go
    python scripts/determinex_corpus_share.py --consent     # record consent, once
    python scripts/determinex_corpus_share.py --push        # upload (needs both)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import sys
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus" / "programbench" / "build_knowledge.json"
CONSENT = ROOT / ".determinex" / "corpus_share_consent.json"
DEFAULT_REPO = "darthceltic85/determinex-corpus"

# What must never leave, whatever else changes. Ordered most-specific first so a broad
# pattern cannot swallow a narrow one before it is seen.
_REDACTIONS: list[tuple[str, re.Pattern]] = [
    ("<key>", re.compile(r"\b(?:sk-ant-api[0-9]{2}-|sk-proj-|sk-)[A-Za-z0-9_\-]{16,}")),
    ("<key>", re.compile(r"\bAIzaSy[A-Za-z0-9_\-]{30,}")),
    ("<key>", re.compile(r"\bghp_[A-Za-z0-9]{30,}|\bhf_[A-Za-z0-9]{30,}")),
    ("<key>", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    (
        "<pem>",
        re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----"),
    ),
    ("<email>", re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]{2,}\b")),
    ("<host>", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")),
    ("<path>", re.compile(r"[A-Za-z]:\\Users\\[^\\\"'\s]+")),
    ("<path>", re.compile(r"/home/[^/\"'\s]+")),
    ("<path>", re.compile(r"/Users/[^/\"'\s]+")),
    # Server-side absolute paths. Added after a sweep of the real payload found /root/Citadel,
    # /opt/determinex_clock and /opt/determinex_hermetic surviving every check above -- the
    # deployment layout of the operator's private box, published under a consent record whose
    # own stated scope promises "no paths". The residue re-scan could not catch them because it
    # re-scans with these same patterns: it can only confirm the list is satisfied, never that
    # the list is complete. Completeness is a separate property and needs a separate sweep.
    ("<path>", re.compile(r"/(?:root|opt|srv|var|mnt)/[\w.\-]+(?:/[\w.\-]+)*")),
    # The operator's infrastructure. A lesson reads identically as "the eval box"; naming the
    # provider tells a reader where the machine is and nothing about the engineering.
    ("<host>", re.compile(r"\bHetzner\b", re.I)),
    ("<drive>", re.compile(r"\b[T-Z]:[/\\][^\"'\s]*")),
]


def redact(text: str) -> str:
    for repl, pat in _REDACTIONS:
        text = pat.sub(repl, text)
    return text


def _residue(text: str) -> list[str]:
    """Re-scan AFTER redaction. A redactor whose output is never checked has unknown
    coverage, and unknown coverage on an upload path is the whole risk."""
    return [repl for repl, pat in _REDACTIONS if pat.search(text)]


#: A SECOND check, with patterns the redactor deliberately does not share.
#:
#: _residue re-scans using the very patterns that performed the redaction, so it can only ever
#: confirm that list is satisfied -- never that the list is complete. That is the same limitation
#: already documented for Cloak's leak count, and it is not theoretical here: a sweep of the real
#: payload found /root/Citadel, /opt/determinex_clock and the operator's hosting provider passing
#: every check, under a consent record promising "no paths". Completeness is a separate property
#: and gets a separate instrument.
#:
#: These describe things a READER would recognise as ours, rather than things we know to strip.
_COMPLETENESS_SWEEP: tuple[tuple[str, re.Pattern], ...] = (
    ("operator username", re.compile(r"\bryang\b", re.I)),
    ("server path", re.compile(r"(?<![\w<])/(?:home|root|opt|srv|mnt|var)/[\w./-]+")),
    ("hosting provider", re.compile(r"\bhetzner\b|\brunpod\b|\broot@", re.I)),
    ("windows user path", re.compile(r"[A-Za-z]:\\Users\\", re.I)),
    ("ssh key reference", re.compile(r"id_[a-z]+\b|\.ssh/", re.I)),
    # No generic "long high-entropy string" rule. It was tried and it flagged
    # DETERMINEX_TYPESCRIPT_NODE_CLI_ADAPTER_LOCK_001, half the class names, and the payload's
    # own content sha256 -- none of them secrets. On a corpus whose substance IS long
    # identifiers, an entropy heuristic fires constantly, and a check that cries wolf is a check
    # someone disables the week after it lands. Real credentials are prefix-anchored (sk-, ghp_,
    # hf_, AKIA, AIzaSy) and _REDACTIONS catches those precisely. This sweep is for identifiable
    # OWNERSHIP -- whose machine, whose account, whose filesystem -- not for entropy.
)


def completeness_sweep(text: str) -> dict[str, list[str]]:
    """What a reader could still identify as ours. Empty dict means nothing found.

    Repo-relative paths (`scripts/...`, `corpus/...`) are intentionally NOT swept: the repository
    is public, and knowing which module a lesson came from is provenance a consumer benefits
    from. The line is the operator's private infrastructure, not our own published layout.
    """
    found: dict[str, list[str]] = {}
    for label, pat in _COMPLETENESS_SWEEP:
        hits = sorted({m if isinstance(m, str) else m[0] for m in pat.findall(text)})
        if hits:
            found[label] = hits[:5]
    return found


def _remote_digest(repo: str, filename: str) -> str | None:
    """sha256 of a file already published, or None if it is absent or unreadable.

    Fetched over plain HTTPS rather than through the hub client so this stays cheap and cannot
    fail the push on a client-version difference. Any error means "assume changed" -- an
    unnecessary upload is harmless, a skipped upload of genuinely new content is not.
    """
    import urllib.error
    import urllib.request

    url = f"https://huggingface.co/datasets/{repo}/resolve/main/{filename}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "determinex-corpus-share"})
        with urllib.request.urlopen(req, timeout=20) as fh:
            return hashlib.sha256(fh.read()).hexdigest()
    except (urllib.error.HTTPError, urllib.error.URLError, OSError):
        return None


def consent_record() -> dict | None:
    try:
        return json.loads(CONSENT.read_text(encoding="utf-8"))
    except Exception:
        return None


def record_consent() -> int:
    CONSENT.parent.mkdir(parents=True, exist_ok=True)
    CONSENT.write_text(
        json.dumps(
            {
                "consented_at": datetime.now(UTC).isoformat(),
                "host": platform.node(),
                "scope": "oracle-verified symptom->fix classes, redacted; no source, no paths, "
                "no credentials, no repository names",
                "revoke": "delete this file; sharing stops immediately",
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"consent recorded -> {CONSENT}")
    print("  revoke at any time by deleting that file.")
    return 0


#: What each source contributes and how far it can be trusted. `confidence` travels with every
#: published row because these sources are NOT equal: class_patterns were proven against a real
#: compiler, while 267 of 272 learned_classes are absorbed prose that no oracle has confirmed.
#: Publishing both under one word would be the same overclaim this project keeps auditing out of
#: its own documents. A consumer can filter on it; a consumer who is not told cannot.
_SHARE_SOURCES: tuple[tuple[str, str, str, tuple[str, ...]], ...] = (
    (
        "class_pattern",
        "oracle_verified",
        "Failure classes proven against a real compiler or test suite during the ProgramBench "
        "campaign; each was applied and confirmed to fix the failure it describes.",
        (
            "detect",
            "symptom",
            "fix",
            "rule",
            "measured",
            "scope",
            "trap",
            "applies_to",
            # `proven` is free text, not a flag -- "eva branch 1bf494 (19 tests): BEFORE...".
            # It IS the evidence, so it is published rather than reduced to a boolean. A reader
            # who can see "go-critic 1.2%->94.5%" can judge the claim; a reader given only
            # `verified: true` has to take our word for it.
            "proven",
        ),
    ),
    (
        "learned_class",
        "mixed",
        "Symptom->fix pairs from the flywheel. Only those tagged verified=true were confirmed by "
        "an oracle; the rest were absorbed from prose and are hints, not facts. The row's own "
        "`verified` field is authoritative -- read it rather than the source name.",
        ("detect", "symptom", "fix", "learned", "uses"),
    ),
    (
        "engineering_lesson",
        "generalized",
        "General engineering lessons distilled FROM the verified failure classes, stripped of "
        "tool-specific framing so they transfer to any project.",
        ("lesson", "why_it_generalizes", "category", "source_pattern", "used_when"),
    ),
    (
        "design_knowledge",
        "reference",
        "Domain knowledge for DESIGN decisions -- shapes, invariants, and the requirements a "
        "prompt leaves implicit. Each entry carries its own `source` and `verified_by`.",
        ("lesson", "why_it_generalizes", "category", "used_when", "reference", "verified_by"),
    ),
)


def _registry_books() -> dict[str, dict]:
    """Exportable top-level artifacts, taken from the corpus API's registry.

    Was a hardcoded list of three playbooks. Four other artifacts holding 47 entries existed and
    were silently absent from every payload -- including bit_techniques_playbook, twelve verifiable
    oracle contracts that are exactly the sort of thing this dataset is for. A published corpus
    assembled from a hand-written list is a published corpus that is quietly incomplete, and
    nothing about the output says so.
    """
    import determinex_corpus_api as api

    out: dict[str, dict] = {}
    for a in api.registered_artifacts():
        if not a.get("exportable"):
            continue
        # Keyed by the PUBLISHED label, not the internal kind. Four artifacts share kind
        # "playbook" while carrying two different meanings to a consumer, and keying on `kind`
        # silently merged 16 engineering lessons into design_knowledge.
        out.setdefault(a["export_as"], {}).update(api.artifact_entries(a["file"]))
    return out


def _rows() -> list[dict]:
    """Every shareable row, flat, each carrying its provenance and confidence.

    Flat rows rather than one nested blob because a HuggingFace dataset is loaded row-wise --
    `load_dataset(...)` over a single deeply-nested object gives a consumer one row containing
    everything, which is technically a dataset and practically unusable.

    Deliberately still NOT the whole corpus. `per_tool` holds tool-specific build recipes and
    `absorbed_sources` holds ingest provenance -- both are ours, neither generalizes, and both
    raise the chance of leaking something specific to a machine. The dated write-up entries are
    excluded for the same reason: they are this project's operational history, full of host
    names, drive letters and campaign specifics, and no amount of redaction makes a session log
    into transferable knowledge.
    """

    kn = json.loads(CORPUS.read_text(encoding="utf-8"))
    # The two big registries live inside build_knowledge.json; everything else comes from the
    # artifact registry, so an exportable file added to corpus/ is carried without editing this.
    # The previous hardcoded version named three playbooks out of seven artifacts and omitted
    # bit_techniques_playbook -- twelve verifiable oracle contracts, exactly what this dataset is
    # for -- with nothing in the output indicating anything was missing.
    books: dict[str, dict] = {
        "class_pattern": kn.get("class_patterns", {}),
        "learned_class": kn.get("learned_classes", {}),
    }
    for label, entries in _registry_books().items():
        books.setdefault(label, {}).update(entries)

    rows: list[dict] = []
    for source, confidence, _desc, fields in _SHARE_SOURCES:
        for name, body in (books.get(source) or {}).items():
            if not isinstance(body, dict):
                continue
            kept = {k: redact(str(body[k])) for k in fields if body.get(k) not in (None, "")}
            if not kept:
                continue
            # The row's own verification beats the source's blanket confidence. A learned_class
            # tagged verified=true really was oracle-confirmed and should not be published under
            # the same caveat as the 267 that were not.
            #
            # `proven` is checked for CONTENT, not for `is True`. It holds an evidence string,
            # so an identity check against True marked all 84 class patterns unverified and the
            # card would have advertised 5 verified rows out of 381 when 50 carry real evidence
            # -- understating the dataset's one distinguishing property. 39 class patterns carry
            # no evidence string and are honestly not counted, whatever the layer is called.
            verified = body.get("verified") is True or bool(str(body.get("proven") or "").strip())
            rows.append(
                {
                    "id": str(name),
                    "source": source,
                    "confidence": "oracle_verified" if verified else confidence,
                    "verified": verified,
                    **kept,
                }
            )
    return rows


def build_payload() -> dict:
    """The shareable slice: generalized knowledge only, redacted, with provenance attached."""
    rows = _rows()
    blob = json.dumps(rows, sort_keys=True)
    by_source: dict[str, int] = {}
    for row in rows:
        by_source[row["source"]] = by_source.get(row["source"], 0) + 1
    return {
        "schema": "determinex-corpus-share-v2",
        "generated_at": datetime.now(UTC).isoformat(),
        "n_rows": len(rows),
        "n_verified": sum(1 for r in rows if r["verified"]),
        "by_source": by_source,
        "sha256": hashlib.sha256(blob.encode("utf-8")).hexdigest(),
        "rows": rows,
    }


def dataset_card(payload: dict) -> str:
    """The README HuggingFace renders as the dataset's front page.

    Written from the payload rather than hand-maintained, because a card that states counts a
    human typed once will disagree with the data the first time the corpus grows, and a dataset
    whose own description is wrong is worse than one with no description -- a reader has no way
    to tell which half to believe.

    States the confidence split up front. 267 of these rows are unconfirmed hints, and a card
    that said "learned from real builds" without that number would be technically true and
    materially misleading.
    """
    by = payload["by_source"]
    unverified = payload["n_rows"] - payload["n_verified"]
    rows = "\n".join(
        f"| `{name}` | {by.get(name, 0)} | {conf} | {desc} |"
        for name, conf, desc, _ in _SHARE_SOURCES
        if by.get(name)
    )
    return f"""---
license: agpl-3.0
task_categories:
- text-generation
tags:
- code
- software-engineering
- failure-analysis
- compiler-verified
size_categories:
- n<1K
configs:
- config_name: default
  data_files: corpus.jsonl
---

# Determinex Corpus — verified failure classes and engineering lessons

{payload["n_rows"]} rows distilled from real build failures and their fixes.
**{payload["n_verified"]} were confirmed by a compiler or test suite. {unverified} were not** —
read the `verified` field on every row before trusting it.

Determinex is a local-first coding system whose only judge is a compiler. When a build fails, the
error and the fix that resolved it are recorded; when a fix is confirmed by the oracle, it is
generalised into a class that the system applies first on the next occurrence. This dataset is
that accumulated layer, redacted and published.

## What is in here

| source | rows | confidence | what it is |
|---|---|---|---|
{rows}

## Row schema

| field | meaning |
|---|---|
| `id` | stable identifier for the class |
| `source` | which layer it came from (table above) |
| `confidence` | `oracle_verified` / `mixed` / `generalized` / `reference` |
| `verified` | **authoritative.** `true` only if an oracle confirmed this specific row |
| `detect` | how to recognise the situation, where recorded |
| `symptom` | what the failure looks like |
| `fix` | what resolved it |
| `lesson` | the generalised form, for the non-failure sources |

Fields are sparse: a row carries only what its source recorded. Do not assume `fix` is present.

## Intended use

Grounding a code-generation prompt. Determinex itself injects a compacted subset into its builder
prompt so a model applies an accumulated fix rather than rediscovering it. A row is a *prior*, not
a guarantee — the whole design assumes an oracle checks the result afterwards.

## What is deliberately NOT here

Tool-specific build recipes, ingest provenance, and this project's dated operational write-ups.
They do not generalise, and they carry host names, paths and campaign specifics. Every published
string is passed through a redactor and then **re-scanned**, and the upload refuses outright if
anything matching a credential, email, host, or user path survives — a redactor whose output is
never checked has unknown coverage.

## Provenance

Generated `{payload["generated_at"]}` by `scripts/determinex_corpus_share.py`.
Content sha256 `{payload["sha256"]}`. Sharing is opt-in and off by default; this snapshot exists
because an operator explicitly consented to publish it.
"""


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--consent", action="store_true", help="record consent (one time)")
    ap.add_argument("--revoke", action="store_true", help="delete the consent record")
    ap.add_argument(
        "--dry-run", action="store_true", help="print the exact payload, upload nothing"
    )
    ap.add_argument("--push", action="store_true", help="upload to HuggingFace")
    ap.add_argument("--repo", default=os.environ.get("DETERMINEX_CORPUS_REPO", DEFAULT_REPO))
    args = ap.parse_args()

    if args.revoke:
        CONSENT.unlink(missing_ok=True)
        print("consent revoked; nothing will be shared.")
        return 0
    if args.consent:
        return record_consent()

    payload = build_payload()
    body = json.dumps(payload, indent=2, ensure_ascii=False)

    left = _residue(body)
    if left:
        print(f"REFUSING: redaction left {left} in the payload. Nothing uploaded.", file=sys.stderr)
        return 1

    # The second, independent check. Runs even for --dry-run: someone reading the dry-run output
    # to decide whether to publish should be told what the first check cannot see.
    missed = completeness_sweep(body)
    if missed:
        print(
            "REFUSING: the completeness sweep found identifiers the redactor has no pattern "
            "for. Nothing uploaded.",
            file=sys.stderr,
        )
        for label, hits in missed.items():
            print(f"  {label}: {', '.join(hits)}", file=sys.stderr)
        print("  Add a pattern to _REDACTIONS, then re-run.", file=sys.stderr)
        return 1

    if args.dry_run or not args.push:
        print(
            body
            if args.dry_run
            else f"{payload['n_rows']} rows ({payload['n_verified']} oracle-verified) "
            f"{payload['by_source']}, sha256 {payload['sha256'][:16]}...  "
            f"(--dry-run to see the bytes, --push to upload)"
        )
        return 0

    # --- upload requires BOTH the flag and the recorded consent -------------------------
    if os.environ.get("DETERMINEX_CORPUS_SHARE") != "1":
        print(
            "REFUSING: DETERMINEX_CORPUS_SHARE=1 is not set. Sharing is off by default.",
            file=sys.stderr,
        )
        return 1
    rec = consent_record()
    if not rec:
        print(
            "REFUSING: no consent record. Run --consent first.\n"
            "  A flag alone is not consent: a flag can be set by a script nobody read.",
            file=sys.stderr,
        )
        return 1

    from huggingface_hub import HfApi

    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")
    if not token:
        print("REFUSING: no HF_TOKEN in the environment.", file=sys.stderr)
        return 1

    api = HfApi(token=token)
    api.create_repo(repo_id=args.repo, repo_type="dataset", exist_ok=True)

    staging = ROOT / ".determinex" / "corpus_share"
    staging.mkdir(parents=True, exist_ok=True)

    # JSONL is what `load_dataset` actually consumes row-wise. The nested JSON is kept beside it
    # because it carries the manifest -- counts, sha256, generation time -- that a consumer needs
    # to tell one snapshot from another, and a bare JSONL has nowhere to put that.
    (staging / "corpus.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in payload["rows"]),
        encoding="utf-8",
        newline="\n",
    )
    (staging / "manifest.json").write_text(
        json.dumps({k: v for k, v in payload.items() if k != "rows"}, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    (staging / "README.md").write_text(dataset_card(payload), encoding="utf-8", newline="\n")

    # ONLY WHAT CHANGED.
    #
    # The corpus is small and moves constantly; the model weights are gigabytes and almost never
    # move. Publishing them as one thing would make every corpus refresh pay for the models, so
    # the dataset is a separate repo -- and within it, a file whose bytes are unchanged is not
    # re-uploaded at all. The common case, re-running after a session that learned nothing new,
    # becomes a few HTTP HEADs instead of a full push.
    #
    # Compared by CONTENT hash, not mtime: regenerating the payload rewrites every staged file
    # with a fresh `generated_at`, so mtime always differs and would defeat the whole point.
    changed, unchanged = [], []
    for fname in ("corpus.jsonl", "manifest.json", "README.md"):
        local = (staging / fname).read_bytes()
        if _remote_digest(args.repo, fname) == hashlib.sha256(local).hexdigest():
            unchanged.append(fname)
            continue
        changed.append(fname)

    if not changed:
        print(
            f"nothing to publish -- {args.repo} already holds this exact corpus "
            f"(sha256 {payload['sha256'][:16]}...). {len(unchanged)} file(s) unchanged."
        )
        return 0

    for fname in changed:
        api.upload_file(
            path_or_fileobj=str(staging / fname),
            path_in_repo=fname,
            repo_id=args.repo,
            repo_type="dataset",
            commit_message=f"corpus refresh: {payload['n_rows']} rows, "
            f"sha256 {payload['sha256'][:12]}",
        )
    print(
        f"uploaded {len(changed)} changed file(s) to {args.repo}: {', '.join(changed)}"
        + (f"  ({len(unchanged)} unchanged, skipped)" if unchanged else "")
    )
    print(
        f"  {payload['n_rows']} rows, {payload['n_verified']} oracle-verified, "
        f"sha256 {payload['sha256'][:16]}..."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
