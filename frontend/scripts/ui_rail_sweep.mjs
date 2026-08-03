/**
 * Visit every rail group AND every panel under it, and report what each one actually renders.
 *
 * The backend sweep found 24 of 31 governed commands unreachable through the CLI, and the
 * Concept Lab fix turned out to be unreachable in the desktop app entirely. Both were
 * invisible to a green test suite and obvious the moment something drove the real product.
 *
 * The first version of this file clicked the nine rails and reported nine clean panels --
 * having opened none of them. A rail opens a SUBMENU (PROVE -> Proof Center / Trace /
 * Health); the panels are one level down. "Nine green rails" was a true statement about
 * menus and a false impression about the product.
 *
 * For each panel it records:
 *   - console errors and failed requests attributable to that panel
 *   - whether it says anything concrete about THIS workspace, or only static copy
 * A panel that renders beautifully over an empty response is the failure mode being hunted,
 * so "did it render" is not the question -- "did it say anything" is.
 */
import fs from "node:fs";
import { chromium } from "playwright";

const RAILS = ["WORK", "CODE", "SOURCE", "RUN", "PROVE", "AGENTS", "TRUST", "LEARN", "SYSTEM"];
const SETTLE_MS = 3500;

const browser = await chromium.connectOverCDP("http://localhost:9223");
const page = browser
  .contexts()[0]
  .pages()
  .find((p) => !p.url().startsWith("devtools://"));
if (!page) {
  console.log("no app page on 9223");
  process.exit(2);
}
const title = await page.title();
if (!/determinex/i.test(title)) {
  console.log(`refusing to sweep: attached page is "${title}"`);
  process.exit(2);
}

const errors = [];
const failed = [];
page.on("console", (m) => m.type() === "error" && errors.push(m.text().replace(/\s+/g, " ").slice(0, 170)));
page.on("pageerror", (e) => errors.push("PAGEERROR " + String(e).slice(0, 170)));
page.on("requestfailed", (r) => {
  const t = r.failure()?.errorText ?? "";
  if (!/ERR_ABORTED|NS_BINDING_ABORTED/.test(t)) failed.push(`${r.method()} ${r.url().slice(0, 80)} :: ${t}`);
});

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function unobstructed() {
  await page
    .waitForFunction(
      () => !document.querySelector('div.absolute.inset-0[class*="z-[110]"]'),
      null,
      { timeout: 180000, polling: 400 }
    )
    .catch(() => {});
}

async function snapshot() {
  return page.evaluate(() => {
    const t = document.body.innerText;
    return {
      chars: t.length,
      signs: [
        /\d[\d,]*\s+uncommitted/i.test(t) && "uncommitted",
        /C:\\[\w\\-]+/.test(t) && "path",
        /origin\/[\w.-]+/.test(t) && "remote",
        /\b\d{2,}\b/.test(t) && "numbers",
        /PASS|VERIFIED|Ready|BLOCKED|AWAITING/i.test(t) && "status",
      ].filter(Boolean),
    };
  });
}

const rows = [];
console.log(`  ${"rail".padEnd(8)}${"panel".padEnd(30)}${"chars".padEnd(7)}${"signals".padEnd(28)}err`);
for (const rail of RAILS) {
  await unobstructed();
  const railBtn = page.getByRole("button", { name: new RegExp(`^${rail}$`, "i") }).first();
  if (!(await railBtn.click({ timeout: 20000 }).then(() => true).catch(() => false))) {
    console.log(`  ${rail.padEnd(8)}[rail click failed]`);
    continue;
  }
  await sleep(1500);

  // The submenu entries are the clickable rows in the flyout that just opened. They are
  // Title Case labels, distinct from the ALL-CAPS rail buttons themselves.
  const items = await page.evaluate(() => {
    const btns = [...document.querySelectorAll("button, [role='button']")];
    return [...new Set(
      btns
        .map((b) => (b.innerText || "").trim().split("\n")[0])
        .filter(
          (t) =>
            t &&
            t.length > 3 &&
            t.length < 32 &&
            /[a-z]/.test(t) &&
            !/^(Describe|Select|Paste|Start|Choose|Open|Request|Your answer|Skip)/i.test(t)
        )
    )].slice(0, 8);
  });

  if (items.length === 0) {
    const s = await snapshot();
    rows.push({ rail, panel: "(no submenu)", ...s, errors: [], failed: [] });
    console.log(`  ${rail.padEnd(8)}${"(no submenu)".padEnd(30)}${String(s.chars).padEnd(7)}${s.signs.join(",").padEnd(28).slice(0, 28)}0`);
    continue;
  }

  for (const item of items) {
    const before = errors.length;
    const beforeReq = failed.length;
    await unobstructed();
    const ok = await page
      .getByRole("button", { name: item, exact: false })
      .first()
      .click({ timeout: 12000 })
      .then(() => true)
      .catch(() => false);
    await sleep(SETTLE_MS);
    const s = await snapshot();
    const e = errors.slice(before);
    const f = failed.slice(beforeReq);
    rows.push({ rail, panel: item, clicked: ok, ...s, errors: e, failed: f });
    console.log(
      `  ${rail.padEnd(8)}${item.slice(0, 29).padEnd(30)}${String(s.chars).padEnd(7)}${s.signs
        .join(",")
        .padEnd(28)
        .slice(0, 28)}${e.length}${f.length ? `+${f.length}r` : ""}${ok ? "" : " [no click]"}`
    );
    await page
      .screenshot({ path: `C:/tmp/panel_${rail}_${item.replace(/[^A-Za-z0-9]+/g, "_").slice(0, 24)}.png` })
      .catch(() => {});
  }
}

console.log("\n  === panels that errored ===");
const bad = rows.filter((r) => (r.errors || []).length || (r.failed || []).length);
if (!bad.length) console.log("    (none)");
for (const r of bad) {
  for (const e of r.errors.slice(0, 2)) console.log(`    ${r.rail}/${r.panel}: ${e}`);
  for (const f of r.failed.slice(0, 2)) console.log(`    ${r.rail}/${r.panel}: REQ ${f}`);
}

console.log("\n  === panels with nothing concrete to say ===");
const mute = rows.filter((r) => (r.signs || []).length <= 1);
console.log(mute.length ? mute.map((r) => `    ${r.rail}/${r.panel}`).join("\n") : "    (none)");

fs.writeFileSync("C:/tmp/panel_sweep.json", JSON.stringify(rows, null, 2));
console.log(`\n  visited ${rows.length} panels -> C:/tmp/panel_sweep.json`);
await browser.close();
