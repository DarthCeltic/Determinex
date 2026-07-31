"""Publish this checkout's source/docs onto the curated release mirror.

WHY THIS EXISTS
---------------
`DarthCeltic/Determinex` is a deliberately curated ~46 MB mirror. This dev
checkout is ~10 GB of `.git`, 2,486 commits, and **completely unrelated history**
-- the mirror's `main` commit does not exist in this repository's object store at
all. So `git push origin <branch>` does not do what it looks like it does: it tries
to graft the entire dev history onto the mirror, and GitHub answers `HTTP 500`
(confirmed 2026-07-28, twice, including with `http.postBuffer=500MB`;
`--dry-run` succeeds, so it is the pack, not auth).

There was no tool for this. The mirror had been assembled by hand, which is why
"just push it" kept looking like the obvious move and kept failing.

WHAT IT DOES
------------
Copies the allowlisted paths from this checkout onto the mirror's own history as
one ordinary commit, keeping it small, then pushes that.

THE ALLOWLIST IS DERIVED, NOT MAINTAINED
----------------------------------------
It comes from `git ls-tree origin/main` -- the mirror's own published top level.
A hand-kept list would drift from what is actually published, and the drift would
be silent in the direction that matters: a new directory of corpus data or
evidence quietly appearing in a repo that exists to not contain it. Deriving it
means the mirror can only ever receive paths it already publishes; adding a NEW
top-level entry is a deliberate act requiring `--allow-new-path`.

Default is a dry run. Nothing is pushed without `--push`.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Never copied, whatever the mirror's tree says. Belt to the allowlist's braces:
# if one of these ever appears in the mirror it is a leak to fix, not a path to
# faithfully re-sync.
#: Paths inside an otherwise-published top-level entry that must not travel.
#:
#: `corpus` came OFF the NEVER list on 2026-07-31: the corpus is the point of Determinex — the
#: Native Reimplementation Loop feeds real source and a real oracle to a model — so publishing a
#: repo without it ships a hollow product. What cannot travel is the ~150,000 files of VENDORED
#: UPSTREAM SOURCE inside it, for two independent reasons:
#:
#:   SIZE  the pack is 9.73 GiB. GitHub soft-limits at 1 GB and rejects any file over 100 MB.
#:   LAW   those trees are other people's software. Redistribution obliges us to carry each
#:         project's copyright notice and license, and 59 of them still have no license text.
#:
#: So the KNOWLEDGE layer ships — the oracles, our `compile.sh` recipes, eval reports, learned
#: build knowledge, and `canonical_tasks.json`, which pins repository+commit for all 200 tasks —
#: and `determinex corpus fetch` reconstructs any upstream tree from its own maintainers at
#: exactly that commit. Same inputs to the model, nothing re-hosted.
CORPUS_VENDORED_MARKERS = (
    "/source/",                      # locked/<tool>/source, pending_unlock/<tier>/<tool>/source
)

#: Inside `per_tool_overrides/<tool>/` only these are ours; the rest of that directory is a
#: complete upstream checkout the recipe happens to sit inside.
CORPUS_OVERRIDE_KEEP = ("compile.sh", "conftest.py", "eval_report.json", "tests.json")

#: Bulk EVIDENCE that belongs in the dataset, not in a git repo. Dropping the vendored source got
#: corpus/ from 158,788 files to 2,351 — but still 908 MB, because 519 `eval_report.json` files are
#: 554 MB of raw per-test output on their own, plus 146 MB of `.bak` archives and 72 MB of training
#: corpus. A git repo is the wrong home for that: every revision keeps a copy forever.
#:
#: Verifiability is not lost. `eval_index.json` records `eval_report_sha256` for each row, so the
#: repo carries a checksum of every report and the dataset carries the report — you can prove the
#: artifact you downloaded is the one the board's number came from.
CORPUS_BULK_EVIDENCE = (
    ".bak",              # pre-bidir backups; never publish a backup
    ".tar.gz",           # submission archives, reproducible from compile.sh
    "/training_corpus/", # the flywheel's training data
)

#: Basename PREFIXES for bulk evidence. A prefix, not an exact name: matching only
#: `eval_report.json` left `eval_report_tui_v1.json`, `eval_report_v3.json` and friends behind,
#: which is 20 MB of the same raw per-test output under a different filename.
CORPUS_BULK_PREFIXES = ("eval_report",)

#: Individually large reference data that belongs in the dataset. Named explicitly rather than
#: caught by a size threshold, because a size rule would silently start dropping things as files
#: grow, and "the repo quietly stopped shipping X" is the failure mode this repo keeps finding.
CORPUS_BULK_FILES = (
    "corpus/swebench/swebench_inventory.json",   # 36 MB SWE-bench task inventory
    "corpus/programbench/xray_index.json",       # 8.8 MB per-test index
)

NEVER = {
    ".env",
    ".env.local",
    ".git",
    "assurance",
    "logs",
    "sessions",
    ".determinex",
    "node_modules",
    "target",
    ".venv",
    "uv.lock",
}


def run(args: list[str], cwd: Path | None = None, check: bool = True) -> str:
    """Run a git/subprocess command. No shell=True (pre-commit forbids it)."""
    proc = subprocess.run(
        args,
        cwd=str(cwd or REPO),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if check and proc.returncode != 0:
        raise SystemExit(
            f"command failed ({proc.returncode}): {' '.join(args)}\n"
            f"stdout: {proc.stdout}\nstderr: {proc.stderr}"
        )
    return proc.stdout


def mirror_allowlist(remote: str, branch: str) -> list[str]:
    """The mirror's own published top-level entries."""
    run(["git", "fetch", remote, branch])
    out = run(["git", "ls-tree", "--name-only", "FETCH_HEAD"])
    entries = [line.strip() for line in out.splitlines() if line.strip()]
    if not entries:
        raise SystemExit(f"{remote}/{branch} has an empty tree -- refusing to guess an allowlist")
    return entries


def tracked_files_under(path: str) -> list[str]:
    """Files git tracks under a path in THIS checkout, so ignored build output and
    untracked scratch never reach the mirror."""
    out = run(["git", "ls-files", "-z", "--", path])
    return [p for p in out.split("\0") if p]


def filter_corpus(paths: list[str]) -> tuple[list[str], int]:
    """Keep the knowledge layer, drop the vendored upstream source.

    Two shapes of vendored tree exist and both must go:

      `.../<tool>/source/**`            a whole upstream checkout under an explicit `source/` dir
      `per_tool_overrides/<tool>/**`    a whole upstream checkout with OUR recipe sitting inside it

    The second is the subtle one: `per_tool_overrides` reads like a directory of our own files, and
    it is 142,750 files of which only ~420 are ours. Everything there is dropped except the four
    recipe filenames, so a new upstream file cannot arrive in the public repo by default.
    """
    kept: list[str] = []
    dropped = 0
    for path in paths:
        posix = path.replace("\\", "/")
        if any(marker in posix for marker in CORPUS_VENDORED_MARKERS):
            dropped += 1
            continue
        if any(marker in posix or posix.endswith(marker) for marker in CORPUS_BULK_EVIDENCE):
            dropped += 1
            continue
        if posix in CORPUS_BULK_FILES:
            dropped += 1
            continue
        if Path(posix).name.startswith(CORPUS_BULK_PREFIXES):
            dropped += 1
            continue
        if "/per_tool_overrides/" in posix:
            # Allowlist by basename, not blocklist by pattern: an unknown file inside a vendored
            # checkout is upstream's until proven otherwise.
            if Path(posix).name not in CORPUS_OVERRIDE_KEEP:
                dropped += 1
                continue
        kept.append(path)
    return kept, dropped


def collect(allowlist: list[str], allow_new: bool) -> tuple[list[str], list[str]]:
    """Resolve the allowlist to a concrete tracked-file list."""
    files: list[str] = []
    skipped: list[str] = []
    for entry in allowlist:
        top = entry.split("/", 1)[0]
        if top in NEVER:
            skipped.append(f"{entry} (on the never-copy list)")
            continue
        if not (REPO / entry).exists():
            # The mirror publishes something this checkout no longer has. Report
            # it rather than silently deleting it from the mirror.
            skipped.append(f"{entry} (published by the mirror, absent here)")
            continue
        found = tracked_files_under(entry)
        if not found:
            skipped.append(f"{entry} (nothing tracked under it)")
            continue
        if top == "corpus":
            kept, dropped = filter_corpus(found)
            if dropped:
                skipped.append(f"{entry} ({dropped} vendored upstream file(s) withheld)")
            found = kept
        files.extend(found)
    if not allow_new:
        return files, skipped
    return files, skipped


def secret_scan(root: Path) -> None:
    """Run the repo's own scanner over the staged mirror before anything is
    committed. The mirror is the public artifact; this is the last gate."""
    scanner = REPO / "scripts" / "security" / "secret_scan.py"
    if not scanner.exists():
        # This is the last gate before a public push; a missing scanner is not a warning.
        raise SystemExit(
            f"secret_scan.py not found at {scanner} -- refusing to publish unscanned content"
        )
    # --root, not cwd. Passing cwd alone was inert and this gate never examined the mirror:
    # secret_scan derives REPO from its own __file__ and ran git with cwd=REPO, so for every
    # publish so far the verdict described the DEVELOPER CHECKOUT while the staged content about
    # to be committed and pushed was never scanned. Proven by running the scanner from an empty
    # non-git directory: it reported "clean -- no secrets in tracked files" and exited 0.
    proc = subprocess.run(
        [sys.executable, str(scanner), "--root", str(root)],
        cwd=str(root),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    print("  " + "\n  ".join(proc.stdout.strip().splitlines()[-4:]))
    if proc.returncode != 0:
        raise SystemExit("secret scan FAILED on the staged mirror -- nothing published")
    # The scanner now prints the root it examined. If that is not the mirror, the gate did not do
    # its job and silence would be indistinguishable from success.
    if str(root) not in proc.stdout:
        raise SystemExit(
            f"secret scan did not report scanning the staged mirror ({root}) -- nothing published"
        )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--remote", default="origin")
    ap.add_argument("--branch", default="main")
    ap.add_argument("-m", "--message", default=None, help="Commit message for the mirror commit")
    ap.add_argument("--push", action="store_true", help="Actually push. Without it, dry run.")
    ap.add_argument(
        "--allow-new-path",
        action="append",
        default=[],
        help="Publish a top-level path the mirror does not already have. Deliberate act.",
    )
    ap.add_argument("--keep", action="store_true", help="Keep the staging worktree for inspection")
    args = ap.parse_args()

    print(f"[1/5] Reading the mirror's own tree from {args.remote}/{args.branch} ...")
    allowlist = mirror_allowlist(args.remote, args.branch)
    for extra in args.allow_new_path:
        if extra not in allowlist:
            allowlist.append(extra)
            print(f"      + {extra} (NEW top-level path, explicitly allowed)")
    print(f"      {len(allowlist)} top-level entries published by the mirror")

    print("[2/5] Resolving to tracked files in this checkout ...")
    files, skipped = collect(allowlist, bool(args.allow_new_path))
    print(f"      {len(files)} tracked files to publish")
    for s in skipped:
        print(f"      - skipped {s}")

    total = sum((REPO / f).stat().st_size for f in files if (REPO / f).is_file())
    print(f"      {total / 1048576:.1f} MB")
    if total > 200 * 1048576:
        raise SystemExit(
            f"refusing to publish {total / 1048576:.0f} MB to a curated mirror -- "
            "something is wrong with the allowlist"
        )

    staging = Path(tempfile.mkdtemp(prefix="determinex-mirror-"))
    try:
        print(f"[3/5] Staging the mirror's history in {staging} ...")
        run(["git", "clone", "--branch", args.branch, "--single-branch",
             run(["git", "remote", "get-url", args.remote]).strip(), str(staging)])

        # Replace the tree wholesale: anything the mirror has and we no longer
        # publish should disappear, which a copy-over-the-top would silently keep.
        for child in staging.iterdir():
            if child.name == ".git":
                continue
            shutil.rmtree(child) if child.is_dir() else child.unlink()

        for rel in files:
            src, dst = REPO / rel, staging / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

        print("[4/5] Secret scan on the staged mirror ...")
        secret_scan(staging)

        run(["git", "add", "-A"], cwd=staging)
        status = run(["git", "status", "--porcelain"], cwd=staging)
        if not status.strip():
            print("      mirror already matches this checkout -- nothing to publish")
            return 0
        changed = len(status.strip().splitlines())
        print(f"      {changed} files differ from the published mirror")

        msg = args.message or "chore: sync source and docs from the development checkout"
        run(["git", "-c", "user.name=Determinex Publisher",
             "-c", f"user.email={os.environ.get('GIT_AUTHOR_EMAIL', 'noreply@github.com/DarthCeltic')}",
             "commit", "-q", "-m", msg], cwd=staging)

        if not args.push:
            print("[5/5] DRY RUN -- not pushed. Re-run with --push to publish.")
            print(f"      staged commit is in {staging}" if args.keep else "")
            return 0

        print(f"[5/5] Pushing to {args.remote}/{args.branch} ...")
        run(["git", "push", "origin", f"HEAD:{args.branch}"], cwd=staging)
        print("      published.")
        return 0
    finally:
        if not args.keep:
            shutil.rmtree(staging, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
