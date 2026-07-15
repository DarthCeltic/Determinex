"""scripts/determinex_cli.py — Unified ``determinex`` command entry point.

Installed as the ``determinex`` console script via pyproject.toml.
All existing scripts are untouched — this dispatches to them.

Usage::

    determinex --version
    determinex doctor [--json <path>] [--strict]
    determinex status [--last-run] [--tail] [--date YYYY-MM-DD] [--summary] [--json] [-n N] [--all]
    determinex config show
    determinex config doctor
    determinex evidence validate
    determinex evidence render

The subcommands are thin wrappers that call the existing script main()
functions, so all behaviour is identical to running the scripts directly.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Ensure scripts/ is importable however the CLI was invoked
_SCRIPTS = Path(__file__).resolve().parent
_ROOT = _SCRIPTS.parent
for _p in (_ROOT, _SCRIPTS):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

__version__ = "1.0.0"

# ---------------------------------------------------------------------------
# Sub-command dispatch
# ---------------------------------------------------------------------------

_USAGE = """\
determinex <command> [options]

Commands:
  doctor          Check local environment setup
  status          View pipeline event log
  config show     Print all resolved config settings
  config doctor   Check config/safety defaults
  evidence validate  Validate evidence index integrity
  evidence render    Re-render docs/EVIDENCE_INDEX.md

Options:
  --version       Print version and exit
  -h, --help      Show this help

Run `determinex <command> --help` for command-specific options.
"""


def _cmd_doctor(argv: list[str]) -> int:
    from determinex_doctor import main as doctor_main
    sys.argv = ["determinex doctor"] + argv
    return doctor_main()


def _cmd_status(argv: list[str]) -> int:
    from determinex_status import main as status_main
    sys.argv = ["determinex status"] + argv
    return status_main()


def _cmd_config_show(_argv: list[str]) -> int:
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    summary = s.resolved_summary()
    availability = s.check_path_availability()
    violations = s.assert_safety_defaults()

    print(f"Determinex config v{__version__}\n")
    width = max(len(k) for k in summary) + 2
    for key, val in summary.items():
        exists = availability.get(key)
        tag = ""
        if exists is True:
            tag = "  [exists]"
        elif exists is False:
            tag = "  [missing]"
        print(f"  {key:<{width}} {val}{tag}")

    if violations:
        print("\nSafety violations:")
        for v in violations:
            print(f"  !! {v}")
    else:
        print("\n  Safety defaults: all closed (OK)")

    return 1 if violations else 0


def _cmd_config_doctor(_argv: list[str]) -> int:
    from determinex_settings import DeterminexSettings
    s = DeterminexSettings()
    violations = s.assert_safety_defaults()
    if violations:
        print(f"Safety violations ({len(violations)}):")
        for v in violations:
            print(f"  !! {v}")
        return 1
    print("All safety defaults closed (OK)")
    return 0


def _cmd_evidence_validate(_argv: list[str]) -> int:
    evidence_index = _ROOT / "assurance" / "evidence" / "evidence_index.json"
    if not evidence_index.is_file():
        print(f"Evidence index not found: {evidence_index}")
        return 1
    import json
    data = json.loads(evidence_index.read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    print(f"Evidence index: {len(entries)} entries")
    missing = []
    for entry in entries:
        # entries use manifest_path as their file reference
        raw_path = entry.get("manifest_path", entry.get("path", ""))
        if not raw_path:
            continue
        path = _ROOT / raw_path
        if not path.is_file():
            missing.append(raw_path)
    if missing:
        print(f"  {len(missing)} missing file(s):")
        for m in missing[:20]:
            print(f"    ! {m}")
        return 1
    print("  All referenced files present")
    return 0


def _cmd_evidence_render(argv: list[str]) -> int:
    from docs_gen.render_evidence_index import render  # type: ignore[import]
    render()
    return 0


# ---------------------------------------------------------------------------
# Argument routing
# ---------------------------------------------------------------------------

def main() -> int:
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(_USAGE)
        return 0

    if args[0] in ("--version", "-V"):
        print(f"determinex {__version__}")
        return 0

    cmd = args[0]
    rest = args[1:]

    if cmd == "doctor":
        return _cmd_doctor(rest)

    if cmd == "status":
        return _cmd_status(rest)

    if cmd == "config":
        sub = rest[0] if rest else ""
        rest2 = rest[1:]
        if sub == "show":
            return _cmd_config_show(rest2)
        if sub == "doctor":
            return _cmd_config_doctor(rest2)
        print(f"Unknown config subcommand: {sub!r}")
        print("Available: determinex config show | determinex config doctor")
        return 1

    if cmd == "evidence":
        sub = rest[0] if rest else ""
        rest2 = rest[1:]
        if sub == "validate":
            return _cmd_evidence_validate(rest2)
        if sub == "render":
            return _cmd_evidence_render(rest2)
        print(f"Unknown evidence subcommand: {sub!r}")
        print("Available: determinex evidence validate | determinex evidence render")
        return 1

    print(f"Unknown command: {cmd!r}\n")
    print(_USAGE)
    return 1


if __name__ == "__main__":
    sys.exit(main())
