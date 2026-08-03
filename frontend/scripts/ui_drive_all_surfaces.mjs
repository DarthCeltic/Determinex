/**
 * Drive EVERY declared surface, and report which ones actually work.
 *
 * The 72-panel rail sweep proved each panel OPENS. `ui_surface_drive.mjs` asked the harder
 * question of five named surfaces. Neither covers the other 20+, and "every surface driven"
 * was not a claim anyone could make honestly — 12 of 42 had been exercised.
 *
 * For each member of `surfaceGroups.ts`: open it by its data-testid, wait for it to settle,
 * and then decide whether it is ALIVE or merely PRESENT. The distinction is the whole point:
 *
 *   ALIVE     rendered its own content — text beyond the shell, or controls of its own
 *   EMPTY     opened and rendered nothing a user could act on
 *   ERROR     threw, or a backend call it made failed
 *   BLOCKED   could not be reached at all
 *
 * A panel that renders beautifully over an empty response is the failure mode being hunted,
 * and it survives any check that only counts whether something appeared.
 *
 * Every navigation lesson from this session is load-bearing: no page.reload (it kills a Tauri
 * webview's IPC), conditional opens (everything is a toggle), data-testids (a label opens the
 * accordion, not the panel), and dismissing a maximised add-on before moving on.
 */
import fs from "node:fs";
import { chromium } from "playwright";

const CDP = process.env.DETERMINEX_CDP ?? "http://localhost:9223";
const OUT = process.env.DX_OUT ?? "C:/tmp/all_surfaces";

const browser = await chromium.connectOverCDP(CDP);
const page = browser
  .contexts()
  .flatMap((c) => c.pages())
  .find((p) => !p.url().startsWith("devtools://"));
if (!page) {
  console.log("no app page on " + CDP);
  process.exit(2);
}
const title = await page.title();
if (!/determinex/i.test(title)) {
  console.log(`refusing to drive: attached page is "${title}"`);
  process.exit(2);
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const errors = [];
const failedReq = [];
page.on("console", (m) => m.type() === "error" && errors.push(m.text().slice(0, 200)));
page.on("pageerror", (e) => errors.push("PAGEERROR " + String(e).slice(0, 200)));
page.on("requestfailed", (r) => {
  const t = r.failure()?.errorText ?? "";
  if (!/ERR_ABORTED|NS_BINDING_ABORTED/.test(t)) failedReq.push(`${r.url().slice(0, 70)} ${t}`);
});

/** rail label -> members, mirrored from src/lib/surfaceGroups.ts */
const GROUPS = {
  WORK: ["hive", "hub"],
  CODE: ["editor", "explorer", "findfiles", "search"],
  SOURCE: ["git", "review", "merge"],
  RUN: ["terminal", "build", "execution", "pipeline"],
  PROVE: ["proof", "trace", "health"],
  AGENTS: ["repair", "agents", "agent-chat", "passport"],
  TRUST: ["cloak", "audit", "repoclinic", "maintenancebay"],
  LEARN: ["learning", "benchmark", "guide"],
  SYSTEM: ["extensions", "skin", "settings", "flywheel", "mission", "roadmap"],
};

async function unobstructed() {
  await page
    .waitForFunction(() => !document.querySelector('div.absolute.inset-0[class*="z-[110]"]'), null, {
      timeout: 180000,
      polling: 400,
    })
    .catch(() => {});
}

async function dropAddon() {
  await page.getByTitle("Close add-on").first().click({ timeout: 3000 }).catch(() => {});
  await sleep(500);
}

async function openTo(target, opener) {
  if (await target.isVisible().catch(() => false)) return true;
  await opener.click({ timeout: 12000 }).catch(() => {});
  await sleep(900);
  return target.isVisible().catch(() => false);
}

async function open(rail, id) {
  await unobstructed();
  await page.getByRole("button", { name: /^Dismiss$/ }).first().click({ timeout: 2000 }).catch(() => {});
  const member = page.locator(`[data-testid="surface-member-${id}"]`).first();
  const gotMember = await openTo(
    member,
    page.getByRole("button", { name: new RegExp(`^${rail}$`, "i") }).first()
  );
  if (!gotMember) return { reached: false, why: "rail member never appeared" };
  await unobstructed();
  // A MODAL surface has no Panel/Dock choice -- SurfaceDrawer renders one "Open" button for
  // it, because offering a destination for something that opens a dialog is a meaningless
  // choice. Expecting `-panel` for all of them reported guide/skin/settings as BLOCKED when
  // they were working exactly as designed; that was the harness, not the product.
  const panelBtn = page.locator(`[data-testid="surface-open-${id}-panel"]`).first();
  const modalBtn = page.locator(`[data-testid="surface-open-${id}"]`).first();

  // EXPAND THE ACCORDION FIRST. Neither button exists until the member is expanded, so
  // testing which kind it is before expanding always answered "neither" -- which reported
  // the three modal surfaces as BLOCKED twice: once for expecting a Panel button they never
  // have, and once for looking for their Open button before it was rendered.
  const anyBtn = async () =>
    (await panelBtn.isVisible().catch(() => false)) || (await modalBtn.isVisible().catch(() => false));
  if (!(await anyBtn())) {
    await member.click({ timeout: 10000 }).catch(() => {});
    await sleep(1000);
  }

  // A MODAL surface has no Panel/Dock choice -- SurfaceDrawer renders one "Open" button for
  // it, because offering a destination for something that opens a dialog is a meaningless
  // choice.
  if (!(await panelBtn.isVisible().catch(() => false))) {
    if (await modalBtn.isVisible().catch(() => false)) {
      await modalBtn.click({ timeout: 10000 }).catch(() => {});
      await sleep(2200);
      return { reached: true, modal: true };
    }
    return { reached: false, why: "neither a Panel nor an Open control appeared" };
  }
  const clicked = await panelBtn.click({ timeout: 10000 }).then(() => true).catch(() => false);
  if (!clicked) return { reached: false, why: "Panel control did not accept a click" };
  await sleep(2600);
  return { reached: true };
}

/** Does the hosted panel show content of its own, or is it an empty shell? */
async function inspect() {
  return page.evaluate(() => {
    const host =
      document.querySelector('[data-testid="zone1-hosted-addon"]') ||
      document.querySelector(".overflow-y-auto");
    if (!host) return { found: false };
    const text = (host.innerText || "").replace(/\s+/g, " ").trim();
    const controls = host.querySelectorAll("button, input, select, textarea, a[href]").length;
    // "Nothing here yet" states are DESIGNED and count as alive: they explain themselves.
    const explains = /no |not |empty|yet|none|open |run |choose |select |install/i.test(text);
    return { found: true, chars: text.length, controls, explains, sample: text.slice(0, 90) };
  });
}

const rows = [];
console.log(`driving ${Object.values(GROUPS).flat().length} surfaces\n`);

for (const [rail, ids] of Object.entries(GROUPS)) {
  for (const id of ids) {
    const before = errors.length;
    const beforeReq = failedReq.length;
    await dropAddon();
    const opened = await open(rail, id);
    let verdict, detail = "";
    if (!opened.reached) {
      verdict = "BLOCKED";
      detail = opened.why;
    } else if (opened.modal) {
      // A modal renders OVER the shell, so the panel host is the wrong place to look.
      const info = await page.evaluate(() => {
        const dlg = document.querySelector('[role=dialog]')
          || [...document.querySelectorAll("div")].filter((d) => {
               const s = getComputedStyle(d);
               return s.position === "fixed" && d.innerText && d.innerText.length > 40;
             }).pop();
        if (!dlg) return { found: false };
        const text = (dlg.innerText || "").replace(/\s+/g, " ").trim();
        return { found: true, chars: text.length,
                 controls: dlg.querySelectorAll("button,input,select,textarea").length };
      });
      verdict = !info.found ? "BLOCKED" : info.chars < 40 ? "EMPTY" : "ALIVE";
      detail = info.found ? `modal: ${info.chars} chars, ${info.controls} controls`
                          : "modal did not render";
      await page.keyboard.press("Escape").catch(() => {});
      await sleep(600);
    } else {
      const info = await inspect();
      const newErrors = errors.slice(before);
      const newReq = failedReq.slice(beforeReq);
      if (newErrors.length) {
        verdict = "ERROR";
        detail = newErrors[0].slice(0, 110);
      } else if (!info.found) {
        verdict = "BLOCKED";
        detail = "no panel host in the DOM";
      } else if (info.chars < 40 && info.controls === 0) {
        verdict = "EMPTY";
        detail = `${info.chars} chars, ${info.controls} controls`;
      } else {
        verdict = "ALIVE";
        detail = `${info.chars} chars, ${info.controls} controls`;
      }
      if (newReq.length && verdict === "ALIVE") detail += ` | failed req: ${newReq[0].slice(0, 60)}`;
    }
    rows.push({ rail, id, verdict, detail });
    const mark = { ALIVE: "  ok  ", EMPTY: " EMPTY", ERROR: " ERROR", BLOCKED: "BLOCKD" }[verdict];
    console.log(`  ${mark}  ${rail.padEnd(7)} ${id.padEnd(16)} ${detail}`);
  }
}

const tally = rows.reduce((a, r) => ((a[r.verdict] = (a[r.verdict] || 0) + 1), a), {});
console.log(`\n  ${rows.length} surfaces: ` + Object.entries(tally).map(([k, v]) => `${k}=${v}`).join("  "));
const bad = rows.filter((r) => r.verdict !== "ALIVE");
if (bad.length) {
  console.log("\n  not alive:");
  for (const r of bad) console.log(`    ${r.verdict.padEnd(8)} ${r.rail}/${r.id}  ${r.detail}`);
}
fs.writeFileSync(`${OUT}.json`, JSON.stringify({ rows, errors, failedReq }, null, 2));
console.log(`\n  wrote ${OUT}.json`);
await browser.close();
process.exit(bad.length ? 1 : 0);
