#!/usr/bin/env python3
"""determinex_eda_report.py -- render a config-search run as something a chip engineer will read.

WHO THIS IS FOR. Someone who has closed timing, has hand-tuned the config being challenged, and
will decide in about thirty seconds whether this is real. That shapes every choice here:

  * THE BASELINE IS ALWAYS SHOWN, and it is shown first. A report that displays only the winning
    candidate is asking to be trusted. Showing what the run was measured against -- their config,
    their numbers -- lets a reader check the claim instead.
  * FAILURES ARE NOT HIDDEN. The attempts that congested or missed timing stay in the table with
    their verdicts. A search that reports only its successes has concealed its hit rate, and hit
    rate is the honest measure of whether the loop works.
  * "NO IMPROVEMENT" IS A FIRST-CLASS RESULT with its own banner. The shipped config was tuned by
    someone who knew what they were doing; failing to beat it is the expected outcome and saying
    so plainly is worth more than a report that never prints that sentence.
  * A DRY RUN SAYS SO, LOUDLY, at the top. A modelled result that could be mistaken for silicon
    is the single most damaging thing this file could produce.

Self-contained HTML: no CDN, no fonts fetched, no JavaScript. It has to survive being emailed,
opened offline, and read on a phone.

    python scripts/determinex_eda_report.py run.json --out report.html
    python scripts/determinex_eda_drive.py --config X --dry-run --json run.json
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path
from typing import Any

_VERDICT_TONE = {
    "clean": ("#3ddc97", "passed"),
    "timing": ("#ffb454", "timing not closed"),
    "congestion": ("#ff7a7a", "route congested"),
    "drc": ("#ff7a7a", "DRC violations"),
    "gave_up": ("#c77dff", "stopped trying"),
    "incomplete": ("#8b93a7", "no result"),
    "crashed": ("#8b93a7", "run crashed"),
}


def _esc(v: Any) -> str:
    return html.escape(str(v), quote=True)


def _fmt(v: Any, nd: int = 4) -> str:
    if v is None or v == "":
        return "&mdash;"
    try:
        return f"{float(v):.{nd}f}"
    except (TypeError, ValueError):
        return _esc(v)


def _pill(verdict: str) -> str:
    colour, label = _VERDICT_TONE.get(verdict, ("#8b93a7", verdict))
    return f'<span class="pill" style="--pc:{colour}">{_esc(verdict)}<em>{_esc(label)}</em></span>'


def render_html(run: dict[str, Any], dry: bool = True) -> str:
    design = run.get("design", "unknown")
    attempts = run.get("attempts") or []
    baseline = run.get("baseline") or {}
    base_score = run.get("baseline_score")
    best_i = run.get("best_index")
    best = attempts[best_i] if best_i is not None and best_i < len(attempts) else None

    spread: dict[str, int] = {}
    for a in attempts:
        spread[a.get("verdict", "?")] = spread.get(a.get("verdict", "?"), 0) + 1
    n = len(attempts) or 1
    p = sum(1 for a in attempts if a.get("passed")) / n
    at_least_one = 1 - (1 - p) ** n

    # ── the headline ─────────────────────────────────────────────────────────
    if best is None:
        headline = (
            '<div class="banner neutral"><strong>No candidate beat the hand-tuned baseline.</strong>'
            " That is a result, not a failure of the run: the shipped configuration was tuned by "
            "someone who knew what they were doing, and this search did not improve on it.</div>"
        )
    elif base_score is None:
        # The baseline produced no score, so there is nothing to have beaten. Claiming otherwise
        # would be the report's worst possible failure -- and a baseline that fails is itself
        # worth flagging, because that configuration taped out. It usually means the run
        # conditions differ from the ones it was tuned under, not that the config is bad.
        headline = (
            f'<div class="banner warn"><strong>The baseline configuration did not pass under '
            f"these run conditions, so there is no baseline score to compare against.</strong> "
            f"Attempt {best['index']} did pass. That is a weaker claim than beating the shipped "
            "config, and it is the accurate one. A shipped configuration failing here usually "
            "means the run conditions differ from the ones it was tuned under &mdash; worth "
            "resolving before drawing any conclusion from this page.</div>"
        )
    else:
        delta = ""
        if best.get("score") is not None:
            d = base_score - best["score"]
            pct = (d / abs(base_score) * 100) if base_score else 0.0
            delta = f" &mdash; {pct:+.1f}% on the objective"
        headline = (
            f'<div class="banner good"><strong>Attempt {best["index"]} beat the hand-tuned '
            f"baseline{delta}.</strong> Every changed setting is listed below; nothing else in the "
            "config was touched.</div>"
        )

    dry_banner = (
        '<div class="banner warn"><strong>DRY RUN.</strong> The flow was <em>modelled</em>, not '
        "executed. No number on this page is a measurement of real silicon. This mode exists to "
        "exercise the search loop without an hour of place-and-route per candidate.</div>"
        if dry
        else ""
    )

    # ── baseline ─────────────────────────────────────────────────────────────
    base_rows = (
        "".join(
            f"<tr><td class='k'>{_esc(k)}</td><td class='v'>{_esc(v)}</td></tr>"
            for k, v in sorted(baseline.items())
        )
        or "<tr><td colspan='2' class='muted'>no baseline recorded</td></tr>"
    )

    # ── attempts ─────────────────────────────────────────────────────────────
    rows = []
    for a in attempts:
        m = a.get("metrics") or {}
        changed = ", ".join(f"{k}={v}" for k, v in sorted((a.get("values") or {}).items()))
        star = " best" if a.get("index") == best_i else ""
        rows.append(
            f"<tr class='att{star}'>"
            f"<td class='n'>{_esc(a.get('index'))}</td>"
            f"<td>{_pill(a.get('verdict', '?'))}</td>"
            f"<td class='num'>{_fmt(m.get('worst_slack'))}</td>"
            f"<td class='num'>{_fmt(m.get('drc_violations'), 0)}</td>"
            f"<td class='num'>{_fmt(a.get('score'))}</td>"
            f"<td class='chg'>{_esc(changed)}</td>"
            f"</tr>"
        )
    attempt_rows = "".join(rows) or "<tr><td colspan='6' class='muted'>no attempts</td></tr>"

    # ── the diff that matters ────────────────────────────────────────────────
    diff_html = ""
    if best:
        diffs = []
        for k, v in sorted((best.get("values") or {}).items()):
            was = baseline.get(k, "&mdash;")
            if str(was) != str(v):
                diffs.append(
                    f"<tr><td class='k'>{_esc(k)}</td>"
                    f"<td class='was'>{_esc(was)}</td>"
                    f"<td class='arrow'>&rarr;</td>"
                    f"<td class='now'>{_esc(v)}</td></tr>"
                )
        if diffs:
            diff_html = (
                "<section><h2>What changed</h2>"
                "<p class='lede'>Only these settings differ from the shipped configuration. "
                "Comments, ordering and every other value are byte-identical, so this is a diff "
                "you can review line by line.</p>"
                f"<table class='diff'>{''.join(diffs)}</table></section>"
            )

    spread_html = "".join(
        f"<li>{_pill(v)}<span class='count'>{c}</span></li>" for v, c in sorted(spread.items())
    )

    return f"""<style>
  :root {{
    --bg:#0b0d12; --panel:rgba(255,255,255,.045); --line:rgba(255,255,255,.10);
    --ink:#e8ecf4; --dim:#98a1b5; --accent:#6ea8fe;
  }}
  @media (prefers-color-scheme: light) {{
    :root {{ --bg:#f6f7fb; --panel:rgba(10,14,25,.035); --line:rgba(10,14,25,.12);
             --ink:#161b26; --dim:#5a6376; --accent:#2f6fdb; }}
  }}
  :root[data-theme="dark"] {{ --bg:#0b0d12; --panel:rgba(255,255,255,.045);
    --line:rgba(255,255,255,.10); --ink:#e8ecf4; --dim:#98a1b5; --accent:#6ea8fe; }}
  :root[data-theme="light"] {{ --bg:#f6f7fb; --panel:rgba(10,14,25,.035);
    --line:rgba(10,14,25,.12); --ink:#161b26; --dim:#5a6376; --accent:#2f6fdb; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--ink);
    font:15px/1.6 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; }}
  .wrap {{ max-width:1000px; margin:0 auto; padding:40px 22px 72px; }}
  .eyebrow {{ font-size:11px; letter-spacing:.16em; text-transform:uppercase;
    color:var(--dim); font-weight:700; }}
  h1 {{ font-size:clamp(26px,4vw,40px); line-height:1.12; margin:.25em 0 .1em;
    letter-spacing:-.02em; text-wrap:balance; }}
  h1 code {{ font-family:ui-monospace,"JetBrains Mono",SFMono-Regular,Menlo,monospace;
    font-size:.82em; color:var(--accent); }}
  h2 {{ font-size:18px; margin:34px 0 10px; letter-spacing:-.01em; }}
  .lede {{ color:var(--dim); margin:.2em 0 1em; max-width:68ch; }}
  section {{ margin-top:26px; }}
  .banner {{ border:1px solid var(--line); border-left-width:3px; border-radius:10px;
    padding:13px 16px; margin:14px 0; background:var(--panel); }}
  .banner.good {{ border-left-color:#3ddc97; }}
  .banner.warn {{ border-left-color:#ffb454; }}
  .banner.neutral {{ border-left-color:var(--dim); }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:12px; }}
  .card {{ background:var(--panel); border:1px solid var(--line); border-radius:12px; padding:14px 16px; }}
  .card .big {{ font-size:26px; font-weight:750; letter-spacing:-.02em;
    font-variant-numeric:tabular-nums; }}
  .card .lbl {{ font-size:11px; text-transform:uppercase; letter-spacing:.1em; color:var(--dim); }}
  .scroll {{ overflow-x:auto; border:1px solid var(--line); border-radius:12px; background:var(--panel); }}
  table {{ width:100%; border-collapse:collapse; font-size:13.5px; }}
  th {{ text-align:left; font-size:11px; text-transform:uppercase; letter-spacing:.09em;
    color:var(--dim); padding:11px 13px; border-bottom:1px solid var(--line); white-space:nowrap; }}
  td {{ padding:10px 13px; border-bottom:1px solid var(--line); vertical-align:top; }}
  tr:last-child td {{ border-bottom:0; }}
  .num, .n {{ font-variant-numeric:tabular-nums; text-align:right; white-space:nowrap;
    font-family:ui-monospace,"JetBrains Mono",monospace; }}
  .k, .v, .was, .now, .chg {{ font-family:ui-monospace,"JetBrains Mono",monospace; font-size:12.5px; }}
  .chg {{ color:var(--dim); }}
  .att.best {{ background:linear-gradient(90deg,rgba(61,220,151,.10),transparent 65%); }}
  .att.best .n::after {{ content:"  \\2190 best"; color:#3ddc97; font-size:11px; }}
  .pill {{ display:inline-flex; align-items:baseline; gap:7px; padding:3px 9px; border-radius:999px;
    border:1px solid color-mix(in srgb, var(--pc) 45%, transparent);
    background:color-mix(in srgb, var(--pc) 12%, transparent); color:var(--pc);
    font-size:11.5px; font-weight:700; white-space:nowrap; }}
  .pill em {{ font-style:normal; font-weight:500; opacity:.72; font-size:10.5px; }}
  .diff td {{ padding:8px 13px; }}
  .diff .was {{ color:var(--dim); text-decoration:line-through; }}
  .diff .now {{ color:#3ddc97; font-weight:700; }}
  .diff .arrow {{ color:var(--dim); width:1.4em; text-align:center; }}
  ul.spread {{ list-style:none; padding:0; margin:0; display:flex; flex-wrap:wrap; gap:9px; }}
  ul.spread li {{ display:flex; align-items:center; gap:7px; }}
  ul.spread .count {{ font-variant-numeric:tabular-nums; color:var(--dim); font-size:12px; }}
  .muted {{ color:var(--dim); }}
  footer {{ margin-top:40px; padding-top:16px; border-top:1px solid var(--line);
    color:var(--dim); font-size:12.5px; }}
</style>

<div class="wrap">
  <div class="eyebrow">Determinex &middot; verified configuration search</div>
  <h1>Physical-design run: <code>{_esc(design)}</code></h1>
  <p class="lede">Each candidate configuration was run through the flow and judged by the flow's
  own metrics. A candidate is only accepted when it completes, routes without congestion, closes
  timing and reports no DRC violations &mdash; and is rejected outright if the configuration told
  the flow to stop repairing timing early.</p>

  {dry_banner}
  {headline}

  <section>
    <div class="grid">
      <div class="card"><div class="lbl">Candidates</div><div class="big">{len(attempts)}</div></div>
      <div class="card"><div class="lbl">Accepted</div><div class="big">{p:.0%}</div></div>
      <div class="card"><div class="lbl">P(&ge;1 pass)</div><div class="big">{at_least_one:.3f}</div></div>
      <div class="card"><div class="lbl">Baseline score</div><div class="big">{_fmt(base_score)}</div></div>
    </div>
  </section>

  <section>
    <h2>Verdict spread</h2>
    <p class="lede">Failures are kept. A search that reports only its successes has hidden its
    hit rate, and the hit rate is what says whether the loop is working.</p>
    <ul class="spread">{spread_html}</ul>
  </section>

  <section>
    <h2>Baseline &mdash; the shipped, hand-tuned configuration</h2>
    <p class="lede">Everything below was measured against this. It is shown first so the claim can
    be checked rather than taken on trust.</p>
    <div class="scroll"><table>{base_rows}</table></div>
  </section>

  <section>
    <h2>Every candidate</h2>
    <div class="scroll"><table>
      <tr><th>#</th><th>Verdict</th><th>Worst slack</th><th>DRC</th><th>Score</th>
          <th>Settings changed</th></tr>
      {attempt_rows}
    </table></div>
    <p class="lede" style="margin-top:10px">Lower score is better. A failing candidate has no
    score at all rather than a bad one &mdash; a run that crashed and a run that merely
    underperformed are different things, and giving the crash a number lets it compete.</p>
  </section>

  {diff_html}

  <footer>
    Generated by Determinex. The oracle is the flow's own metrics, so a candidate is accepted by
    the same evidence a human reviewer would use. Clock period and TNS end percent are pinned
    rather than tuned: relaxing either improves the reported numbers by weakening the
    requirement, which is not an optimisation.
  </footer>
</div>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("run_json", help="output of determinex_eda_drive.py --json")
    ap.add_argument("--out", required=True, help="where to write the HTML")
    ap.add_argument("--real", action="store_true", help="this was a real flow run, not modelled")
    args = ap.parse_args()

    reconf = getattr(sys.stdout, "reconfigure", None)
    if reconf is not None:
        reconf(encoding="utf-8")

    run = json.loads(Path(args.run_json).read_text(encoding="utf-8"))
    out = Path(args.out)
    out.write_text(render_html(run, dry=not args.real), encoding="utf-8", newline="\n")
    print(f"  wrote {out}  ({len(out.read_text(encoding='utf-8')):,} chars)")
    if not args.real:
        print("  NOTE: marked as a DRY RUN. Pass --real only for an actual flow execution.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
