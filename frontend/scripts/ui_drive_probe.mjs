/**
 * ui_drive_probe.mjs -- drive the RUNNING desktop app and record what it actually does.
 *
 * WHY THIS EXISTS AS A BUILD STEP RATHER THAN A ONE-OFF
 * The unit tests and the Playwright specs both run against a page. Neither one ever attaches
 * to the SHIPPED application with its real Tauri backend behind it, so a whole class of
 * defect -- a command that resolves to backendMissing(), a panel that renders beautifully
 * over an empty response, a console error nobody sees because nobody has devtools open --
 * survives a fully green suite. This repository has been bitten by exactly that shape
 * repeatedly: a guard that matched nothing and passed, a module that could not be imported,
 * a hook whose pattern required more escaping than the source had.
 *
 * So: attach over CDP to the live window, exercise it, and report what breaks.
 *
 * WHAT IT CHECKS
 *   structure   the rail groups and named controls that are actually present
 *   liveness    whether the app is reading real workspace state or rendering an empty shell
 *   errors      every console error and failed request produced while it is driven
 *   cloak       Cloak's own claim about what a cloud participant can and cannot see,
 *               read from the backend rather than from the marketing copy
 *
 * USAGE
 *   npm run tauri dev            # in one terminal; devtools listens on 9222 in dev
 *   node scripts/ui_drive_probe.mjs [--json out.json]
 *
 * Exit code is non-zero when the app produced errors, so this can gate a release.
 */
import fs from "node:fs";
import { chromium } from "playwright";

// 9223, NOT 9222. 9222 is Chrome's default remote-debugging port, and on a developer's box
// Chrome usually already owns it -- the first run of this probe attached to a JupyterLab tab
// in the operator's browser and cheerfully reported that "the app" had no rail groups and no
// Tauri IPC. A probe that attaches to the wrong process and then describes it is worse than
// no probe, so the port is app-specific and the target is verified below by title.
const CDP = process.env.DETERMINEX_CDP ?? "http://localhost:9223";
const EXPECT_TITLE = /determinex/i;
const jsonIdx = process.argv.indexOf("--json");
const jsonOut = jsonIdx > -1 ? process.argv[jsonIdx + 1] : null;

const report = {
  attached: false,
  title: null,
  url: null,
  rails: [],
  namedControls: [],
  liveState: [],
  consoleErrors: [],
  failedRequests: [],
  cloak: {},
  verdict: null,
};

function log(s = "") {
  console.log(s);
}

let browser;
try {
  browser = await chromium.connectOverCDP(CDP);
} catch (e) {
  log(`  could not attach to ${CDP}`);
  log(`  is the app running?  npm run tauri dev`);
  log(`  (${String(e).slice(0, 120)})`);
  process.exit(2);
}

const ctx = browser.contexts()[0];
const candidates = ctx.pages().filter((p) => !p.url().startsWith("devtools://"));

// Verify we attached to OUR app. Silently probing whatever happens to be listening produces
// a confident report about someone else's browser tab -- which is exactly what happened on
// the first run.
let page = null;
for (const p of candidates) {
  const t = await p.title().catch(() => "");
  if (EXPECT_TITLE.test(t) || p.url().includes("localhost:3000")) {
    page = p;
    break;
  }
}
if (!page) {
  const seen = [];
  for (const p of candidates) seen.push(`${await p.title().catch(() => "?")} :: ${p.url().slice(0, 70)}`);
  log(`  attached to ${CDP}, but no Determinex page is there. Saw:`);
  seen.forEach((s) => log("    " + s));
  log(`\n  Start the app with WebView2 debugging enabled:`);
  log(`    $env:WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS="--remote-debugging-port=9223"`);
  log(`    npm run tauri dev`);
  await browser.close();
  process.exit(2);
}

report.attached = true;
report.title = await page.title();
report.url = page.url();
log(`  attached: ${report.title}`);
log(`  url     : ${report.url}\n`);

page.on("console", (m) => {
  if (m.type() === "error") report.consoleErrors.push(m.text().replace(/\s+/g, " ").slice(0, 240));
});
page.on("pageerror", (e) => report.consoleErrors.push("PAGEERROR " + String(e).slice(0, 240)));
page.on("requestfailed", (r) => {
  const t = r.failure()?.errorText ?? "";
  // A cancelled navigation is not a defect; a failed command is.
  if (!/ERR_ABORTED|NS_BINDING_ABORTED/.test(t)) {
    report.failedRequests.push(`${r.method()} ${r.url().slice(0, 120)} :: ${t}`);
  }
});

// ── landmarks: can assistive technology find anything at all ───────────────────────────
// This is the check that earned its keep. `nav button` returned nothing, which looked like a
// bad selector and was not: the app renders ZERO landmarks -- no <nav>, no <main>, no <h1>.
// The existing Playwright spec asserts every control has an accessible name and a 24px
// target, so accessibility was clearly cared about; nothing asserted that the page has
// structure, so a screen reader has no way to reach the navigation or skip to content.
report.landmarks = await page.evaluate(() => {
  const q = (s) => document.querySelectorAll(s).length;
  return {
    nav: q("nav") + q("[role='navigation']"),
    main: q("main") + q("[role='main']"),
    h1: q("h1"),
    header: q("header") + q("[role='banner']"),
    aside: q("aside") + q("[role='complementary']"),
  };
});
// nav / main / h1 are what a screen reader needs to orient: reach the navigation, skip to
// content, know what the document is. header and aside are genuinely optional for a
// workbench with no page banner and no sidebar-of-asides, so requiring them would be the
// probe inventing a standard -- and a check that fails on something correct gets ignored,
// which is how the real gap survived in the first place.
const REQUIRED = ["nav", "main", "h1"];
const missing = REQUIRED.filter((k) => !report.landmarks[k]);
const optionalAbsent = ["header", "aside"].filter((k) => !report.landmarks[k]);
log(`  landmarks: ${JSON.stringify(report.landmarks)}`);
if (missing.length) {
  log(`    MISSING (required): ${missing.join(", ")} -- assistive tech cannot navigate this`);
} else {
  log(`    required landmarks present${optionalAbsent.length ? ` (optional absent: ${optionalAbsent.join(", ")})` : ""}`);
}
if (report.landmarks.h1 > 1) {
  log(`    note: ${report.landmarks.h1} h1 elements -- one per document is the convention`);
}

const railNames = [];
for (const el of await page.locator("button").all()) {
  const t = (await el.innerText().catch(() => "")).replace(/\s+/g, " ").trim();
  if (/^(WORK|CODE|SOURCE|RUN|PROVE|AGENTS|TRUST|LEARN|SYSTEM)$/i.test(t)) railNames.push(t.toUpperCase());
}
report.rails = [...new Set(railNames)];
log(`  rail groups (${report.rails.length}): ${report.rails.join(", ")}`);

const names = [];
for (const b of (await page.getByRole("button").all()).slice(0, 80)) {
  const n = ((await b.getAttribute("aria-label").catch(() => null)) ||
    (await b.innerText().catch(() => "")) || "").replace(/\s+/g, " ").trim();
  if (n && n.length < 60) names.push(n);
}
report.namedControls = [...new Set(names)];
log(`  named controls: ${report.namedControls.length}`);

// ── liveness: is it reading the real workspace, or rendering an empty shell ─────────────
// Read the rendered TEXT, not a locator match. The first version used a text= locator and
// reported "shell may be empty" about an app that was displaying "1849 uncommitted changes"
// at the time -- a probe wrong about the thing it exists to check.
const ws = await page.evaluate(() => {
  const t = document.body.innerText;
  return {
    uncommitted: (t.match(/(\d[\d,]*)\s+uncommitted changes/i) || [])[1] ?? null,
    branch: (t.match(/\b[\w.-]+\s+·\s+origin\/[\w.-]+/) || [])[0] ?? null,
    workspacePath: (t.match(/[A-Z]:\\[\w\\-]+/) || [])[0] ?? null,
    oracleReady: /Oracle Ready/i.test(t),
  };
});
report.liveState = ws;
log(`\n  live workspace read from the running app:`);
log(`    uncommitted changes : ${ws.uncommitted ?? "(none reported)"}`);
log(`    branch              : ${ws.branch ?? "(none)"}`);
log(`    workspace           : ${ws.workspacePath ?? "(none)"}`);
log(`    oracle              : ${ws.oracleReady ? "Ready" : "not reported"}`);
const readingRealRepo = Boolean(ws.uncommitted && ws.workspacePath);
log(`  reading a real workspace: ${readingRealRepo ? "YES" : "NO -- shell may be empty"}`);

// ── cloak: ask the BACKEND what a cloud participant can see, not the copy ───────────────
const cloak = await page
  .evaluate(async () => {
    const inv = window.__TAURI_INTERNALS__?.invoke;
    if (!inv) return { available: false, why: "no Tauri IPC on this page" };
    const out = { available: true };
    try {
      out.active = await inv("agent_chat_cloak_status", {});
    } catch (e) {
      out.statusError = String(e).slice(0, 160);
    }
    try {
      const s = await inv("get_cloak_audit_summary", {});
      out.auditPresent = !!s;
      out.identifierCount = s?.identifiers?.length ?? 0;
      // Never surface the REAL identifiers from an audit -- the point of the feature is that
      // they do not travel. Report only the shape and one token as evidence of mapping.
      out.sampleToken = s?.identifiers?.[0]?.token ?? null;
    } catch (e) {
      out.auditError = String(e).slice(0, 160);
    }
    return out;
  })
  .catch((e) => ({ available: false, why: String(e).slice(0, 160) }));
report.cloak = cloak;

log(`\n  cloak (asked of the backend, not the UI copy):`);
if (!cloak.available) {
  log(`    IPC unavailable: ${cloak.why}`);
} else {
  log(`    room active for cloud participants : ${cloak.active}`);
  log(`    audit evidence on this machine     : ${cloak.auditPresent ? "yes" : "no"}`);
  if (cloak.auditPresent) {
    log(`    identifiers mapped                 : ${cloak.identifierCount}`);
    log(`    sample opaque token                : ${cloak.sampleToken}`);
  }
  if (cloak.statusError) log(`    status error: ${cloak.statusError}`);
  if (cloak.auditError) log(`    audit error : ${cloak.auditError}`);
}

// ── drive it a little, then report what broke ──────────────────────────────────────────
for (const k of ["Control+1", "Escape", "Control+5", "Escape", "Control+7", "Escape"]) {
  await page.keyboard.press(k).catch(() => {});
  await page.waitForTimeout(600);
}
await page.waitForTimeout(2500);

const errs = [...new Set(report.consoleErrors)];
const reqs = [...new Set(report.failedRequests)];
log(`\n  === console errors: ${errs.length} ===`);
errs.slice(0, 12).forEach((e) => log("    ! " + e));
log(`  === failed requests: ${reqs.length} ===`);
reqs.slice(0, 10).forEach((r) => log("    ! " + r));

report.consoleErrors = errs;
report.failedRequests = reqs;
// Landmarks count toward the verdict. Reporting CLEAN while printing "assistive tech cannot
// navigate this" would be a probe contradicting itself in its own output -- the same shape as
// a guard that prints a finding and then exits 0.
const a11yOk = missing.length === 0;
report.verdict =
  errs.length || reqs.length
    ? "ERRORS"
    : !readingRealRepo
      ? "SHELL_ONLY"
      : !a11yOk
        ? "A11Y_GAPS"
        : "CLEAN";
log(`\n  verdict: ${report.verdict}`);
if (!a11yOk) log(`    (no console errors, but the page has no landmarks: ${missing.join(", ")})`);

if (jsonOut) {
  fs.writeFileSync(jsonOut, JSON.stringify(report, null, 2), "utf8");
  log(`  wrote ${jsonOut}`);
}

await browser.close();
process.exit(report.verdict === "CLEAN" ? 0 : 1);
