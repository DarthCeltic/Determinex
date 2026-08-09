#!/usr/bin/env python3
"""determinex_eda_config.py -- read, mutate and write chip-flow configurations.

TWO FORMATS, AND THE DIFFERENCE MATTERS. OpenROAD-flow-scripts uses a Makefile (`config.mk`,
`NAME = value`). OpenLane uses Tcl (`config.tcl`, `set ::env(NAME) "value"`). They are not
interchangeable, and a tool that only speaks one silently does nothing useful on the other -- the
Makefile parser finds zero assignments in a Tcl file and reports an empty config rather than an
error, which is the worst possible failure because it looks like a valid empty result.

MUTATION PRESERVES THE FILE. A config is hand-written, commented, and often carries per-block
reasoning a person put there deliberately. Rewriting it from a parsed dict throws all of that
away and hands a reviewer a diff they cannot read. So `write_value` performs a surgical
line-level edit: the assignment changes, everything else -- comments, ordering, unrelated
settings, the Tcl preamble that computes `script_dir` -- survives byte for byte. A diff of a
mutated config shows exactly one changed line, which is what makes the result reviewable by the
engineer who wrote the original.

VALUES ARE NOT ALL NUMBERS. `CTS_CLK_BUFFER_LIST` is a space-separated cell list and
`PL_RESIZER_MAX_SLEW_MARGIN` is brace-quoted. Quoting style is preserved on write for the same
reason: an unnecessary reformat is noise in a diff someone has to review.

    python scripts/determinex_eda_config.py corpus/eda/riscduino_baseline/wb_interconnect.config.tcl
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

#: `set ::env(NAME) value` -- OpenLane. Also matches `set ::env(NAME) "a b c"` and `{...}`.
_TCL_SET = re.compile(
    r"^(?P<indent>\s*)set\s+::env\((?P<name>[A-Za-z_][A-Za-z0-9_]*)\)\s+(?P<value>.+?)\s*$"
)
#: `NAME = value`, `NAME := value`, `NAME ?= value`, optional `export` -- ORFS / Make.
_MK_SET = re.compile(
    r"^(?P<indent>\s*)(?:export\s+)?(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*(?P<op>[:?+]?=)\s*"
    r"(?P<value>.*?)\s*$"
)


@dataclass
class ConfigEntry:
    name: str
    value: str
    line_no: int  # 1-indexed
    raw: str
    quote: str  # '"', '{', or '' -- preserved so a rewrite does not reformat


class FlowConfig:
    """A parsed flow config that remembers its own text, so edits are surgical."""

    def __init__(self, text: str, fmt: str):
        self.text = text
        self.fmt = fmt  # "tcl" | "mk"
        self.entries: dict[str, ConfigEntry] = {}
        self._parse()

    # ── reading ──────────────────────────────────────────────────────────────

    def _parse(self) -> None:
        pat = _TCL_SET if self.fmt == "tcl" else _MK_SET
        for i, line in enumerate(self.text.splitlines(), 1):
            if line.lstrip().startswith("#"):
                continue
            m = pat.match(line)
            if not m:
                continue
            raw_value = m.group("value")
            # A trailing comment is not part of the value. Only stripped for Make: in Tcl a `#`
            # inside a quoted cell list would be a legitimate character.
            if self.fmt == "mk" and "#" in raw_value:
                raw_value = raw_value.split("#", 1)[0].rstrip()
            value, quote = _unquote(raw_value)
            self.entries[m.group("name")] = ConfigEntry(
                name=m.group("name"), value=value, line_no=i, raw=line, quote=quote
            )

    def get(self, name: str, default: str | None = None) -> str | None:
        e = self.entries.get(name)
        return e.value if e else default

    def as_dict(self) -> dict[str, str]:
        return {k: v.value for k, v in self.entries.items()}

    # ── writing ──────────────────────────────────────────────────────────────

    def with_value(self, name: str, value: str) -> FlowConfig:
        """A copy with one setting changed. Everything else is byte-identical.

        Appends the setting if it is absent, rather than failing: a parameter a block never set
        is exactly the parameter most worth trying, and refusing to add it would confine the
        search to whatever the original author had already thought of.
        """
        lines = self.text.splitlines(keepends=True)
        entry = self.entries.get(name)
        if entry is not None:
            lines[entry.line_no - 1] = _render(self.fmt, name, value, entry.quote) + _eol(
                lines[entry.line_no - 1]
            )
        else:
            if lines and not lines[-1].endswith("\n"):
                lines[-1] = lines[-1] + "\n"
            lines.append(_render(self.fmt, name, value, '"') + "\n")
        return FlowConfig("".join(lines), self.fmt)

    def with_values(self, updates: dict[str, str]) -> FlowConfig:
        cfg = self
        for k, v in updates.items():
            cfg = cfg.with_value(k, str(v))
        return cfg

    def diff_against(self, other: FlowConfig) -> dict[str, tuple[str | None, str | None]]:
        """{name: (theirs, ours)} for every setting that differs. The reviewable summary."""
        out: dict[str, tuple[str | None, str | None]] = {}
        for key in sorted(set(self.entries) | set(other.entries)):
            a, b = other.get(key), self.get(key)
            if a != b:
                out[key] = (a, b)
        return out


def _eol(line: str) -> str:
    return "\n" if line.endswith("\n") else ""


def _unquote(v: str) -> tuple[str, str]:
    v = v.strip()
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        return v[1:-1], '"'
    if len(v) >= 2 and v[0] == "{" and v[-1] == "}":
        return v[1:-1], "{"
    return v, ""


def _render(fmt: str, name: str, value: str, quote: str) -> str:
    if quote == '"':
        v = f'"{value}"'
    elif quote == "{":
        v = f"{{{value}}}"
    else:
        v = value
    return f"set ::env({name}) {v}" if fmt == "tcl" else f"{name} = {v}"


#: MULTILINE variants, used ONLY for format detection. The parsing patterns are anchored with ^
#: and applied line by line, so they do not need the flag -- but `search()` over a whole file
#: does, and without it `^` tests only the first line. RISCduino's config.tcl opens with
#: `set script_dir [file dirname ...]`, which is not an `::env` assignment, so detection fell
#: through to the filename -- and `loads(text)` has no filename. The result was a Tcl file parsed
#: as a Makefile: zero assignments found, an empty config returned, and every downstream default
#: silently substituted. Exactly the failure this module's docstring warns about, in this module.
_TCL_ANY = re.compile(_TCL_SET.pattern, re.MULTILINE)
_MK_ANY = re.compile(_MK_SET.pattern, re.MULTILINE)


def detect_format(path: str | Path | None, text: str) -> str:
    """Tcl or Make. Decided by CONTENT first, because the extension can lie.

    A file called config.tcl that happens to contain Make assignments should still be read
    correctly, and more importantly the reverse: guessing from the name and finding no
    assignments returns a valid-looking empty config rather than an error.
    """
    if _TCL_ANY.search(text or ""):
        return "tcl"
    if _MK_ANY.search(text or ""):
        return "mk"
    name = str(path or "").lower()
    return "tcl" if name.endswith(".tcl") else "mk"


def load(path: str | Path) -> FlowConfig:
    text = Path(path).read_text(encoding="utf-8")
    return FlowConfig(text, detect_format(path, text))


def loads(text: str, fmt: str | None = None) -> FlowConfig:
    return FlowConfig(text, fmt or detect_format(None, text))


#: The knobs worth searching, with sane bounds and the format each flow names them in.
#:
#: Bounds are deliberately conservative. A search that proposes PL_TARGET_DENSITY 0.99 wastes an
#: hour of place-and-route discovering what the corpus already records -- density that high
#: congests rather than producing a worse-but-valid result. Encoding known-bad regions as bounds
#: is cheaper than rediscovering them, once per run, forever.
TUNABLE: dict[str, dict] = {
    "PL_TARGET_DENSITY": {
        "lo": 0.20,
        "hi": 0.82,
        "kind": "float",
        "flow": "openlane",
        "note": "above ~0.85 congests rather than degrading gracefully",
    },
    "FP_CORE_UTIL": {
        "lo": 20,
        "hi": 70,
        "kind": "int",
        "flow": "openlane",
        "note": "core area occupation percent",
    },
    # PINNED, and this was a real bug caught in a dry run. Clock period is the design's
    # SPECIFICATION, not a tuning knob: a search allowed to touch it discovers that relaxing the
    # clock improves slack, converges on a slower chip, and reports an improvement. That is
    # exactly TNS_END_PERCENT's trap wearing different clothes -- the metric got better because
    # the requirement got weaker. Anyone who has closed timing spots it instantly.
    # Widen deliberately, per design, only when exploring what a block COULD run at.
    "CLOCK_PERIOD": {
        "lo": 0,
        "hi": 0,
        "kind": "float",
        "flow": "both",
        "note": "PINNED: the spec, not a knob. Relaxing it buys slack by making "
        "the chip slower and calls that an optimisation.",
    },
    "SYNTH_MAX_FANOUT": {"lo": 4, "hi": 16, "kind": "int", "flow": "openlane"},
    "CTS_SINK_CLUSTERING_SIZE": {"lo": 8, "hi": 40, "kind": "int", "flow": "openlane"},
    "CTS_CLK_MAX_WIRE_LENGTH": {"lo": 0, "hi": 800, "kind": "int", "flow": "openlane"},
    "GLB_RT_ADJUSTMENT": {
        "lo": 0.0,
        "hi": 0.6,
        "kind": "float",
        "flow": "openlane",
        "note": "routing layer capacity derate; higher relieves congestion",
    },
    "CORE_UTILIZATION": {"lo": 20, "hi": 70, "kind": "int", "flow": "orfs"},
    "PLACE_DENSITY": {"lo": 0.20, "hi": 0.82, "kind": "float", "flow": "orfs"},
    "TNS_END_PERCENT": {
        "lo": 100,
        "hi": 100,
        "kind": "int",
        "flow": "orfs",
        "note": "PINNED at 100. Lowering it buys runtime by abandoning timing "
        "repair, so a search allowed to touch it will converge on a "
        "config that gave up and looks fast -- see the eda oracle's "
        "gave_up verdict. Not a knob; a trap.",
    },
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("config")
    ap.add_argument("--set", nargs=2, metavar=("NAME", "VALUE"), action="append")
    args = ap.parse_args()

    reconf = getattr(sys.stdout, "reconfigure", None)
    if reconf is not None:
        reconf(encoding="utf-8")

    cfg = load(args.config)
    print(f"  format: {cfg.fmt}   settings: {len(cfg.entries)}")
    tunable = {k: v for k, v in cfg.as_dict().items() if k in TUNABLE}
    print(f"  tunable settings present ({len(tunable)}):")
    for k, v in sorted(tunable.items()):
        print(f"    {k:<28} {v}")

    if args.set:
        new = cfg.with_values({k: v for k, v in args.set})
        print("\n  diff:")
        for k, (was, now) in new.diff_against(cfg).items():
            print(f"    {k}: {was} -> {now}")
        changed = sum(
            1 for a, b in zip(cfg.text.splitlines(), new.text.splitlines(), strict=False) if a != b
        )
        print(f"  lines changed: {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
