#!/usr/bin/env python3
"""determinex_pb_absorb -- SEED the flywheel from everything the system already knows in PROSE.

The flywheel (determinex_pb_amplified_fix.learn_class) learns (symptom -> fix) classes from FUTURE
verified solves. But years of hand-won knowledge already sit in prose: the campaign milestones in
CLAUDE.md, the corpus pattern docs (FAILURE_GROUPS / cross_tool_patterns / the playbooks), the
program docs. This absorbs that prose into build_knowledge.learned_classes so the grounded fixer
applies the accumulated knowledge FIRST-shot -- not just what it re-learns.

SOUND: absorbed classes are flagged source=prose, verified=False. They are HINTS; the next use is
still oracle-gated (a wrong hint fails verification, no harm). Gaming patterns are excluded at
extraction. One-time seed; the flywheel continues from verified solves.

Usage:  python3 determinex_pb_absorb.py [--max-chunks N] [--dry-run]
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KN = ROOT / "corpus" / "programbench" / "build_knowledge.json"

EXTRACT_PROMPT = """From the notes below (about fixing CLI tools' BUILDS and TESTS for a benchmark),
extract REUSABLE fix classes. Output ONLY a JSON list (no prose). Each item:
  {{"detect": "<generalized symptom: an error/failure signature, with tool names, absolute paths and
     version numbers replaced by <tool> / <path> / <n>>",
    "fix": "<the concrete, generalizable fix: a build flag, toolchain pin, locale/timezone/clock,
     dep install, build-target, or output-format normalization>",
    "source_tool": "<the tool name if the note names one, else \\"\\">"}}
RULES: only CONCRETE, GENERALIZABLE fixes. EXCLUDE gaming (branching on PYTEST_CURRENT_TEST,
embedding golden/expected bytes, capping/ignoring test collection, shipping a prebuilt binary).
If the text contains no such fix, output exactly [].
NOTES:
{chunk}
JSON:"""

_GAMING = re.compile(
    r"pytest_current_test|current.test.routing|embed.*golden|golden.*bytes|del items\[|"
    r"collect_ignore|prebuilt binary|answer.key|hardcode.*expected", re.I)

# A real (symptom->fix) class: the DETECT looks like a FAILURE and the FIX is an ACTION -- this
# rejects strategy/meta prose the model sometimes returns ("X is the bottleneck -> move toward 100").
_SYMPTOM = re.compile(
    r"error|fail|not found|missing|cannot|can't|undefined|mismatch|exit|\brc\b|compil|build|panic|"
    r"exception|timeout|no such|expected|assert|unresolved|--|/workspace|stderr|stdout|segfault|"
    r"crash|wrong|incorrect|differ|unexpected|invalid|broke|broken|\bhang|stuck|version|skip|"
    r"not_run|rc=127|linker|header|cargo|go\.mod|configure", re.I)
_ACTION = re.compile(
    r"\b(install|build|export|set|add|convert|run|use|replace|remove|pin|enable|disable|apt|cargo|"
    r"make|cmake|sed|chmod|dos2unix|vendor|fetch|download|patch|inject|rename|link|copy|symlink|"
    r"create|generate|normalize|strip|wrap|redirect|mount|provision|ensure|check|verify|point|"
    r"target|expect|require|provide|specify|configure|update|delete|drop|prefer|switch|apply|"
    r"rebuild|recompile|adjust|correct|match|map|extract|validate|pass|disable)\b|--|=| -[a-zA-Z]", re.I)
# A raw CODE statement (not a failure description) -- the absorber sometimes pulls a code diff out of
# a source file ("if a in (...) -> if arg in (...)"); reject those as classes (refactors, not fixes).
_CODE = re.compile(
    r"^\s*(if |for |while |def |return |import |from |let |fn |func |var |const |pub |public |private |"
    r"class |struct |elif |else|try|except|match |switch |case |#include|//|/\*|\}|\{)", re.I)


def _chunks(text: str, size: int = 3000):
    """Split on markdown structure so a chunk is a coherent note (a milestone / a pattern entry)."""
    parts = re.split(r"\n(?=#{1,6}\s|\* |\d+\.\s|\- |\|)", text)
    buf = ""
    for p in parts:
        if len(buf) + len(p) > size and buf.strip():
            yield buf
            buf = p
        else:
            buf = buf + "\n" + p if buf else p
    if buf.strip():
        yield buf


def _parse_json_list(out: str) -> list:
    """Robustly pull the JSON list out of a model reply (it may wrap it in prose/fences)."""
    if not out:
        return []
    m = re.search(r"\[.*\]", out, re.DOTALL)
    if not m:
        return []
    try:
        data = json.loads(m.group(0))
        return data if isinstance(data, list) else []
    except Exception:
        return []


def _sources() -> list[Path]:
    """ALL the LOCAL prose knowledge to absorb -- the whole corpus, every doc, the specs, the memory
    learnings, the campaign milestones, and archived knowledge on T:. The web ingester (determinex_web
    or a saved-pages dir) drops fetched pages into corpus/programbench/ingest/ which this also picks
    up, so online material flows through the same distiller."""
    srcs: list[Path] = []
    for base, pat in (
        (ROOT / "corpus" / "programbench", "*.md"),            # top corpus docs (NOT source READMEs)
        (ROOT / "corpus" / "programbench" / "_strategy", "*.md"),
        (ROOT / "docs", "**/*.md"),                            # the docs tree (no source trees in it)
        (ROOT / "specs", "*.md"),
        (ROOT / "corpus" / "programbench" / "ingest", "**/*.txt"),  # web-fetched pages land here
        (Path.home() / ".claude" / "projects" / "c--Dev-Determinex" / "memory", "*.md"),
    ):
        try:
            if base.exists():
                srcs += sorted(base.glob(pat))
        except Exception:
            continue
    for extra in (ROOT / "CLAUDE.md", ROOT.parent / "CLAUDE.md"):
        if extra.exists():
            srcs.append(extra)
    # NOTE: T:/determinex-archive + the T: tool-source trees are HUGE recursive globs -- too slow for
    # this per-batch hot path. They are a bounded one-time follow-on (--scan-drive writes a cached
    # file list to corpus/programbench/ingest/_drive_sources.txt that this then reads), not here.
    cache_list = ROOT / "corpus" / "programbench" / "ingest" / "_drive_sources.txt"
    if cache_list.exists():
        try:
            for line in cache_list.read_text(encoding="utf-8").splitlines():
                p = Path(line.strip())
                if line.strip() and p.exists():
                    srcs.append(p)
        except Exception:
            pass
    # CODEBASES: build configs (how tools/projects build -- the fix-relevant code) across the tool
    # overrides + T: tool source. The model extracts build patterns; the quality gate filters noise.
    cfg = ("compile.sh", "Cargo.toml", "go.mod", "Makefile", "CMakeLists.txt", "package.json",
           "pyproject.toml", "setup.py", "build.sh", "configure.ac")
    cbase = ROOT / "corpus" / "programbench" / "per_tool_overrides"   # top-level config per tool only
    for name in cfg:
        try:
            if cbase.exists():
                srcs += sorted(cbase.glob("*/" + name))[:250]   # */name (top), not **/ (source tree)
        except Exception:
            continue
    # NOTE: the T: tool-source tree (determinex-programbench) is a HUGE recursive glob -- too slow for
    # this per-batch hot path. It's a bounded one-time follow-on (cached file list), not here.
    # de-dup; existing only; cap size at 400KB; SKIP dependency/build junk dirs (node_modules etc.)
    _SKIP = ("node_modules", "/.git/", "/target/", "/dist/", "/build/", "/vendor/",
             "site-packages", "/.venv", "/_superseded/")
    seen: set = set()
    out: list[Path] = []
    for s in srcs:
        try:
            sp = str(s).replace("\\", "/")
            if any(x in sp for x in _SKIP):
                continue
            rp = s.resolve()
            if s.exists() and rp not in seen and s.stat().st_size < 400_000:
                seen.add(rp)
                out.append(s)
        except (OSError, ValueError):
            continue
    return out


_CAP = 1500  # max learned classes kept (verified/flywheel preferred; the playbook ranks top-20)


def _bound_and_write(kn: dict, lc: dict, dry_run: bool) -> None:
    if len(lc) > _CAP:                    # keep verified (flywheel) over prose-absorbed, then recent
        drop = sorted(lc, key=lambda x: (bool(lc[x].get("verified")), str(lc[x].get("learned", ""))))
        for k in drop[:len(lc) - _CAP]:
            lc.pop(k, None)
    if not dry_run:
        KN.write_text(json.dumps(kn, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def absorb(generate, max_chunks: int = 400, dry_run: bool = False) -> dict:
    """Model-extract (symptom->fix) classes from the prose into learned_classes. RESUMABLE (skips
    sources already in absorbed_sources) + INCREMENTAL (writes after each source) so a long FREE
    local-model run progresses + survives interruption; re-run to continue."""
    kn = json.loads(KN.read_text(encoding="utf-8"))
    lc = kn.setdefault("learned_classes", {})
    if not isinstance(lc, dict):
        lc, kn["learned_classes"] = {}, {}
    done = set(kn.setdefault("absorbed_sources", []) if isinstance(kn.get("absorbed_sources"), list) else [])
    added = scanned = skipped_gaming = srcs_done = 0
    for src in _sources():
        sid = str(src.resolve())
        if sid in done:                   # RESUME: already absorbed this file
            continue
        if scanned >= max_chunks:
            break
        try:
            text = src.read_text(encoding="utf-8", errors="replace")
        except Exception:
            done.add(sid)
            continue
        for ch in _chunks(text):
            if scanned >= max_chunks:
                break
            scanned += 1
            try:
                items = _parse_json_list(generate(EXTRACT_PROMPT.format(chunk=ch[:3500]), 0.1))
            except Exception:
                continue
            for it in items if isinstance(items, list) else []:
                if not isinstance(it, dict):
                    continue
                det = str(it.get("detect") or "").strip()[:200]
                fix = str(it.get("fix") or "").strip()[:600]
                if not det or not fix or len(det) < 12 or len(fix) < 10:
                    continue
                if len(re.findall(r"[A-Za-z]{3,}", det)) < 4:   # too terse to MATCH a real failure
                    continue                                     # (e.g. "build-fail / CRLF") -> skip
                if not _SYMPTOM.search(det) or not _ACTION.search(fix):  # meta/strategy, not a fix
                    continue
                if _GAMING.search(fix) or _GAMING.search(det):
                    skipped_gaming += 1
                    continue
                key = "absorbed_" + hashlib.sha256((det + "||" + fix).encode("utf-8")).hexdigest()[:10]
                if key in lc:
                    continue
                lc[key] = {"detect": det, "symptom": det, "fix": fix,
                           "source_tool": (str(it.get("source_tool") or "") or src.stem)[:40],
                           "source": "prose:" + src.name, "verified": False,
                           "learned": time.strftime("%Y-%m-%d"), "uses": 0}
                added += 1
        done.add(sid)
        srcs_done += 1
        kn["absorbed_sources"] = sorted(done)
        _bound_and_write(kn, lc, dry_run)   # incremental checkpoint after each source
    return {"added": added, "scanned": scanned, "skipped_gaming": skipped_gaming, "srcs_done": srcs_done,
            "total_learned": len(lc), "remaining_sources": len(_sources()) - len(done)}


def scan_drive(max_files: int = 6000) -> dict:
    """One-time BOUNDED scan of the wider drive -- T: archive + every C:/Dev project CODEBASE -- for
    knowledge + source files, written to the cached list _sources() reads. os.walk with junk-dir
    pruning (node_modules/.git/target/...) + a hard file cap, so it's bounded (the recursive globs
    were unbounded -> too slow). Includes code (.rs/.go/.c/.py) so the CODEBASES get ingested too."""
    import os
    roots = [Path("T:/determinex-archive"), ROOT.parent]   # T: archive + C:/Dev (all 8 projects)
    SKIP = {"node_modules", ".git", "target", "dist", "build", "vendor", "site-packages", ".venv",
            "__pycache__", ".next", ".cargo", "determinex-models", "_superseded", ".pytest_cache",
            "backups", "dist-windows"}
    # prose + BUILD CONFIGS only. Raw .rs/.go/.c/.py source produces code-DIFF noise for a
    # symptom->fix distiller (gets purged); raw source belongs in a future code-RAG for the BUILDER.
    exts = {".md", ".txt", ".toml", ".mod", ".sh", ".cfg", ".ini", ".cmake"}
    found: list[str] = []
    for root in roots:
        if not root.exists():
            continue
        for dirpath, dirs, files in os.walk(root):
            dirs[:] = [d for d in dirs if d not in SKIP and not d.startswith(".")]
            for f in files:
                if Path(f).suffix.lower() in exts:
                    fp = Path(dirpath) / f
                    try:
                        if fp.stat().st_size < 400_000:
                            found.append(str(fp))
                    except Exception:
                        continue
            if len(found) >= max_files:
                break
        if len(found) >= max_files:
            break
    out = ROOT / "corpus" / "programbench" / "ingest" / "_drive_sources.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(found), encoding="utf-8")
    return {"scanned_files": len(found), "cache": str(out)}


DOC_URLS = [
    # Rust / cargo
    "https://doc.rust-lang.org/cargo/reference/build-scripts.html",
    "https://doc.rust-lang.org/cargo/reference/config.html",
    "https://doc.rust-lang.org/cargo/commands/cargo-build.html",
    "https://doc.rust-lang.org/rustc/command-line-arguments.html",
    # Go
    "https://go.dev/doc/toolchain",
    "https://go.dev/ref/mod",
    "https://pkg.go.dev/cmd/cgo",
    # C / C++ / build
    "https://cmake.org/cmake/help/latest/manual/cmake.1.html",
    "https://cmake.org/cmake/help/latest/command/find_package.html",
    "https://www.gnu.org/software/make/manual/make.html",
    "https://people.freedesktop.org/~dbn/pkg-config-guide.html",
    # Python / pytest
    "https://docs.pytest.org/en/stable/how-to/failures.html",
    "https://packaging.python.org/en/latest/tutorials/packaging-projects/",
]


def _fetch_clean(u: str) -> str:
    """URL -> clean ingest text. Prefers Crawl4AI (github.com/unclecode/crawl4ai) when it is
    installed -- it renders JS and returns clean markdown, the right tool for the dynamic pages urllib
    cannot read (Stack Overflow, GitHub Issues). Falls back to urllib + tag-strip for static docs.
    Credit: Crawl4AI (unclecode/crawl4ai)."""
    try:
        from crawl4ai import WebCrawler  # type: ignore  # optional dep; clean JS-rendered markdown
        c = WebCrawler(); c.warmup()
        md = (getattr(c.run(url=u), "markdown", "") or "").strip()
        if md:
            return md
    except Exception:
        pass                                     # not installed / API drift -> urllib fallback
    import urllib.request
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (determinex-ingest)"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.DOTALL | re.I)
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"&[a-z#0-9]+;", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", text).strip()


def fetch_urls(urls=None) -> dict:
    """Bulk-fetch curated DOC URLs (free, autonomous) -> stripped text in ingest/ -> the running
    distiller turns them into classes. Uses _fetch_clean (Crawl4AI when installed, else urllib), so
    JS-heavy pages (SO / GitHub Issues) work too once Crawl4AI is present."""
    urls = urls or DOC_URLS
    outdir = ROOT / "corpus" / "programbench" / "ingest"
    outdir.mkdir(parents=True, exist_ok=True)
    n = 0
    for u in urls:
        try:
            text = _fetch_clean(u)
            if len(text) > 300:
                fn = "web_" + re.sub(r"[^a-z0-9]+", "_", u.lower().split("//", 1)[-1])[:70] + ".txt"
                (outdir / fn).write_text(text[:200000], encoding="utf-8")
                n += 1
                print(f"  fetched {u} ({len(text)} chars)")
        except Exception as e:
            print(f"  fetch FAILED {u}: {e}")
    return {"fetched": n, "of": len(urls)}


def purge() -> dict:
    """One-pass cleanup: re-filter the ABSORBED (verified=False) learned_classes against the current
    quality gate (word-count + symptom + action + not-gaming + not-code) and drop the failures.
    Flywheel-VERIFIED classes are kept untouched. Run with the absorber paused (avoids a write race)."""
    kn = json.loads(KN.read_text(encoding="utf-8"))
    lc = kn.get("learned_classes", {})
    if not isinstance(lc, dict):
        return {"dropped": 0, "kept": 0}
    drop = []
    for k, v in list(lc.items()):
        if not isinstance(v, dict):
            drop.append(k)
            continue
        if v.get("verified"):                     # flywheel-proven -> keep
            continue
        det, fix = str(v.get("detect", "")), str(v.get("fix", ""))
        if (len(re.findall(r"[A-Za-z]{3,}", det)) < 4 or len(fix) < 10
                or not _SYMPTOM.search(det) or not _ACTION.search(fix)
                or _GAMING.search(det) or _GAMING.search(fix) or _CODE.search(det)):
            drop.append(k)
    for k in drop:
        lc.pop(k, None)
    KN.write_text(json.dumps(kn, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"dropped": len(drop), "kept": len(lc)}


def main() -> int:
    if "--purge" in sys.argv:
        print(f"purge: {purge()}")
        return 0
    if "--fetch-urls" in sys.argv:
        print(f"fetch-urls: {fetch_urls()}")
        return 0
    if "--scan-drive" in sys.argv:
        print("scanning drive (bounded os.walk; T: archive + C:/Dev codebases)...")
        print(f"drive scan: {scan_drive()}")
        return 0
    max_chunks = 400
    dry = "--dry-run" in sys.argv
    for i, a in enumerate(sys.argv):
        if a == "--max-chunks" and i + 1 < len(sys.argv):
            max_chunks = int(sys.argv[i + 1])
    allow_paid = "--allow-paid" in sys.argv
    sys.path.insert(0, str(ROOT / "scripts"))
    import determinex_providers as PV
    # FREE/LOCAL ONLY by default (operator: do not spend on paid APIs for bulk ingest). Only the
    # local model (Ollama) is used unless --allow-paid is passed.
    PAID = {"deepseek", "claude", "gemini", "codex", "groq", "openai", "openrouter", "anthropic"}
    avail = [n for n, ok in PV.available().items() if ok and (allow_paid or n not in PAID)]
    if not avail:
        print("absorb: no FREE/local provider available (pass --allow-paid to permit paid APIs)")
        return 1
    print(f"absorb: providers={avail} (free/local only) sources={len(_sources())} max_chunks={max_chunks}")
    gen = PV.get_rotating_generator(avail)
    res = absorb(gen, max_chunks=max_chunks, dry_run=dry)
    print(f"absorb done: {res}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
