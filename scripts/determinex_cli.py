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

Built on click's Group/Command structure (real subcommand dispatch, not a
hand-rolled if/elif chain) but main()'s public contract -- an int return
value, "Unknown command"/"Unknown config subcommand"/"Unknown evidence
subcommand" text on stdout, exit code 1 -- is preserved exactly rather than
adopting click's own error format (exit code 2, "No such command" on
stderr): this is a shipped, installed console script, and anything already
scripting against `determinex <bad-cmd>; echo $?` shouldn't silently start
seeing a different exit code because of an internal refactor.
"""
from __future__ import annotations

import sys
from pathlib import Path

import click

# Ensure scripts/ is importable however the CLI was invoked
_SCRIPTS = Path(__file__).resolve().parent
_ROOT = _SCRIPTS.parent
for _p in (_ROOT, _SCRIPTS):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

__version__ = "1.0.0"

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


# ---------------------------------------------------------------------------
# Command implementations (unchanged from the pre-click dispatcher)
# ---------------------------------------------------------------------------

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
# Click command tree — real subcommand dispatch, help text, option parsing
# infrastructure. doctor/status forward all extra args to the wrapped
# legacy script's own argparse main() unparsed (click.UNPROCESSED).
# ---------------------------------------------------------------------------

@click.group(
    invoke_without_command=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.version_option(__version__, "--version", "-V", prog_name="determinex")
@click.pass_context
def _cli(ctx: click.Context) -> None:
    if ctx.invoked_subcommand is None:
        click.echo(_USAGE)


_PASSTHROUGH = {"ignore_unknown_options": True, "help_option_names": []}


@_cli.command(context_settings=_PASSTHROUGH, add_help_option=False)
@click.argument("extra", nargs=-1, type=click.UNPROCESSED)
@click.pass_context
def doctor(ctx: click.Context, extra: tuple[str, ...]) -> None:
    """Check local environment setup."""
    ctx.exit(_cmd_doctor(list(extra)))


@_cli.command(context_settings=_PASSTHROUGH, add_help_option=False)
@click.argument("extra", nargs=-1, type=click.UNPROCESSED)
@click.pass_context
def status(ctx: click.Context, extra: tuple[str, ...]) -> None:
    """View pipeline event log."""
    ctx.exit(_cmd_status(list(extra)))


@_cli.group()
def config() -> None:
    """Config subcommands."""


@config.command("show")
@click.pass_context
def config_show(ctx: click.Context) -> None:
    """Print all resolved config settings."""
    ctx.exit(_cmd_config_show([]))


@config.command("doctor")
@click.pass_context
def config_doctor(ctx: click.Context) -> None:
    """Check config/safety defaults."""
    ctx.exit(_cmd_config_doctor([]))


@_cli.group()
def evidence() -> None:
    """Evidence subcommands."""


@evidence.command("validate")
@click.pass_context
def evidence_validate(ctx: click.Context) -> None:
    """Validate evidence index integrity."""
    ctx.exit(_cmd_evidence_validate([]))


@evidence.command("render")
@click.pass_context
def evidence_render(ctx: click.Context) -> None:
    """Re-render docs/EVIDENCE_INDEX.md."""
    ctx.exit(_cmd_evidence_render([]))


# ---------------------------------------------------------------------------
# main() — preserves the pre-click int-return / exit-code / message contract
# ---------------------------------------------------------------------------

def main() -> int:
    args = sys.argv[1:]

    # -h/--help and bare invocation keep the original hand-written _USAGE
    # text exactly (tests assert its exact substrings) rather than click's
    # auto-generated help.
    if not args or args[0] in ("-h", "--help"):
        print(_USAGE)
        return 0

    if args[0] in ("--version", "-V"):
        print(f"determinex {__version__}")
        return 0

    cmd = args[0]
    rest = args[1:]

    if cmd == "config":
        sub = rest[0] if rest else ""
        if sub not in ("show", "doctor"):
            print(f"Unknown config subcommand: {sub!r}")
            print("Available: determinex config show | determinex config doctor")
            return 1
    elif cmd == "evidence":
        sub = rest[0] if rest else ""
        if sub not in ("validate", "render"):
            print(f"Unknown evidence subcommand: {sub!r}")
            print("Available: determinex evidence validate | determinex evidence render")
            return 1
    elif cmd not in ("doctor", "status"):
        print(f"Unknown command: {cmd!r}\n")
        print(_USAGE)
        return 1

    try:
        return _cli.main(args=args, prog_name="determinex", standalone_mode=False)
    except click.exceptions.Exit as e:
        return e.exit_code
    except click.ClickException as e:
        e.show()
        return e.exit_code


if __name__ == "__main__":
    sys.exit(main())
