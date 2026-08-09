#!/usr/bin/env python3
"""ingest_external_refs.py — fetch an external reading list and score it against our claims.

Doing this by hand costs a context window per link. This does it mechanically: fetch, extract
text, and score each source against the specific things Determinex asserts - so the output is
"this touches our prefix-cache claim" rather than "this is about caching".

The scoring is deliberately dumb and auditable. Every hit is a phrase that appears in the
source, listed with the claim it bears on, so a human can check the judgement rather than
trust it. Nothing is summarised from a title: a source that cannot be fetched is recorded as
UNREACHABLE, never guessed at.

    python scripts/dev/ingest_external_refs.py
    python scripts/dev/ingest_external_refs.py --only prefix,spec
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DOC = ROOT / "docs" / "EXTERNAL_REFERENCES.md"
OUT_CORPUS = ROOT / "corpus" / "external_references.json"
SITE = "https://gdymind.com"

# The claims Determinex actually makes. A source is "direct" only if it bears on one of these,
# not merely because it shares a topic.
CLAIMS = {
    "prefix_cache": (
        "We measure 93.5% prefix-cache hits on a shared-prefix arm vs ~1% when one distinct "
        "token is prepended, and treat that as a GPU optimisation of the access pattern.",
        r"prefix cach|block hash|cache hit|hash of the current block|reuse.{0,20}KV",
    ),
    "kv_ceiling": (
        "K is bounded by kv_cache_tokens / max_model_len, measured rather than read from "
        "vLLM's boot-time declaration.",
        r"kv cache|num_gpu_blocks|block size|paged ?attention|memory pressure|evict",
    ),
    "verification_word": (
        "Determinex's verifier is a compiler or test suite. Speculative decoding uses the same "
        "word for a model checking a model.",
        r"speculative decod|drafter|draft model|verif(y|ication).{0,40}(model|target)|acceptance rate",
    ),
    "batch_throughput": (
        "K verified candidates cost 5.58x aggregate throughput for 1.07x wall clock, because "
        "the GPU batches them.",
        r"continuous batching|batch(ing)? throughput|tokens?/s|concurren\w+ request|scheduler",
    ),
    "quantisation_bonus": (
        "We serve an AWQ 4-bit 32B and ship LoRA-distilled local models.",
        r"quantiz|awq|gptq|distillation|LoRA|4-?bit",
    ),
}

# Known-live paths on the site. lnkd.in shortlinks from the original list mostly 404 now - the
# blog reorganised - so these come from the site index, and anything not found is recorded as
# unreachable rather than invented.
SEEDS = [
    "/2025/04/11/vLLM-03-prefix-caching/",
    "/2026/06/29/DSpark/",
    "/2026/04/04/vLLM-Omni-deep-dive/",
    "/2026/03/02/sliding-window-attention/",
    "/2026/07/06/Ragged-Paged-Attention-on-TPU/",
    "/2026/04/27/DeepSeek-V4-attention-deep-dive-say-yes-to-longer-context/",
]

TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")


def fetch(url: str, raw: bool = False) -> tuple[str | None, str]:
    try:
        rq = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 determinex-ingest"})
        with urllib.request.urlopen(rq, timeout=45) as r:
            page = r.read().decode("utf-8", "replace")
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as e:
        return None, f"{type(e).__name__}: {e}"
    # Discovery needs the RAW markup: hrefs live inside tags, so stripping tags first deletes
    # exactly what a link regex is looking for. Scoring wants the opposite - text without
    # markup. One function, two callers, one flag.
    if raw:
        return page, ""
    body = re.sub(r"(?is)<(script|style|nav|footer|header)[^>]*>.*?</\1>", " ", page)
    return WS.sub(" ", TAG.sub(" ", body)).strip(), ""


def discover(max_pages: int = 12) -> list[str]:
    """Walk the site's own index AND its pagination.

    The first version read page 1 only and found six posts, which silently under-reported the
    site. A crawler that stops at the first page and says "six sources" is making a completeness
    claim it never checked - the same failure this project keeps finding elsewhere.
    """
    found: set[str] = set()
    seen_pages = 0
    for page in range(1, max_pages + 1):
        url = SITE if page == 1 else f"{SITE}/page/{page}/"
        html, _ = fetch(url, raw=True)
        if not html:
            break
        hits = set(re.findall(r"/20\d{2}/\d{2}/\d{2}/[A-Za-z0-9\-_.%]+/", html))
        new_hits = hits - found
        seen_pages += 1
        found |= hits
        if not new_hits and page > 1:  # only stop once a real page adds nothing
            break
    # Also try common archive surfaces, since some generators keep a full list there.
    for extra in ("/archives/", "/sitemap.xml", "/atom.xml", "/index.xml"):
        html, _ = fetch(SITE + extra, raw=True)
        if html:
            found |= set(re.findall(r"/20\d{2}/\d{2}/\d{2}/[A-Za-z0-9\-_.%]+/", html))
    print(f"  discovery: {seen_pages} index page(s), {len(found)} post path(s)")
    return sorted(found)


def score(text: str) -> dict:
    hits = {}
    low = text.lower()
    for key, (_claim, pat) in CLAIMS.items():
        found = sorted({m.group(0).lower() for m in re.finditer(pat, low)})[:6]
        if found:
            hits[key] = found
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="comma-separated substrings to filter paths")
    a = ap.parse_args()

    paths = sorted(set(SEEDS) | set(discover()))
    if a.only:
        want = [s.strip().lower() for s in a.only.split(",")]
        paths = [p for p in paths if any(w in p.lower() for w in want)]
    print(f"  {len(paths)} source(s) to fetch\n")

    entries, unreachable = [], []
    for path in paths:
        url = SITE + path
        text, err = fetch(url)
        if not text or len(text) < 400:
            unreachable.append({"url": url, "reason": err or "empty/too short after extraction"})
            print(f"  UNREACHABLE  {path}  ({err or 'empty'})")
            continue
        hits = score(text)
        rel = "direct" if hits else "not relevant"
        entries.append(
            {
                "url": url,
                "chars": len(text),
                "relevance": rel,
                "claims_touched": {
                    k: {"claim": CLAIMS[k][0], "phrases_found": v} for k, v in hits.items()
                },
                "fetched": datetime.now(UTC).isoformat(timespec="seconds"),
            }
        )
        print(f"  {rel:<12} {path}  -> {', '.join(hits) or 'no claim overlap'}")

    OUT_CORPUS.parent.mkdir(parents=True, exist_ok=True)
    OUT_CORPUS.write_text(
        json.dumps(
            {
                "fetched_at": datetime.now(UTC).isoformat(timespec="seconds"),
                "entries": entries,
                "unreachable": unreachable,
            },
            indent=1,
        ),
        encoding="utf-8",
    )
    print(
        f"\n  {len(entries)} ingested, {len(unreachable)} unreachable "
        f"-> {OUT_CORPUS.relative_to(ROOT)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
