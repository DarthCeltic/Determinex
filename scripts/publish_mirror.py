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
NEVER = {
    ".env",
    ".env.local",
    ".git",
    "corpus",
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
        files.extend(found)
    if not allow_new:
        return files, skipped
    return files, skipped


def secret_scan(root: Path) -> None:
    """Run the repo's own scanner over the staged mirror before anything is
    committed. The mirror is the public artifact; this is the last gate."""
    scanner = REPO / "scripts" / "security" / "secret_scan.py"
    if not scanner.exists():
        print("  [warn] secret_scan.py not found -- skipping (verify by hand)")
        return
    proc = subprocess.run(
        [sys.executable, str(scanner)],
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
             "-c", f"user.email={os.environ.get('GIT_AUTHOR_EMAIL', 'noreply@lunariandata.com')}",
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
