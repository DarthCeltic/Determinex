/**
 * Open every surface and photograph it, so a human can see what a user would see.
 *
 * `ui_drive_all_surfaces.mjs` answers "does it work". This answers "does it look right", which
 * no character count can: a panel can report 900 characters and 12 controls while the text
 * overflows its box, the bottom is cut, or a spinner sits where content should be.
 *
 * Writes C:/tmp/shots/<rail>_<id>.png plus a manifest with the cheap layout facts worth
 * flagging automatically -- horizontal overflow, content taller than its frame, empty regions,
 * and any element whose text is clipped.
 */
import fs from "node:fs";
import { chromium } from "playwright";

const CDP = process.env.DETERMINEX_CDP ?? "http://localhost:9223";
const OUT = process.env.DX_SHOTS ?? "C:/tmp/shots";

fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(OUT, { recursive: true });

const browser = await chromium.connectOverCDP(CDP);
const page = browser
  .contexts()
  .flatMap((c) => c.pages())
  .find((p) => !p.url().startsWith("devtools://"));
if (!page) {
  console.log("no app page on " + CDP);
  process.exit(2);
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
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

async function open(rail, id) {
  await unobstructed();
  await page.getByTitle("Close add-on").first().click({ timeout: 2500 }).catch(() => {});
  await page.getByRole("button", { name: /^Dismiss$/ }).first().click({ timeout: 2000 }).catch(() => {});
  const member = page.locator(`[data-testid="surface-member-${id}"]`).first();
  if (!(await member.isVisible().catch(() => false))) {
    await page.getByRole("button", { name: new RegExp(`^${rail}$`, "i") }).first().click({ timeout: 12000 }).catch(() => {});
    await sleep(900);
  }
  const panelBtn = page.locator(`[data-testid="surface-open-${id}-panel"]`).first();
  const modalBtn = page.locator(`[data-testid="surface-open-${id}"]`).first();
  const any = async () =>
    (await panelBtn.isVisible().catch(() => false)) || (await modalBtn.isVisible().catch(() => false));
  if (!(await any())) {
    await member.click({ timeout: 10000 }).catch(() => {});
    await sleep(900);
  }
  if (await panelBtn.isVisible().catch(() => false)) {
    await panelBtn.click({ timeout: 10000 }).catch(() => {});
    await sleep(6500);
    return "panel";
  }
  if (await modalBtn.isVisible().catch(() => false)) {
    await modalBtn.click({ timeout: 10000 }).catch(() => {});
    await sleep(4000);
    return "modal";
  }
  return null;
}

/** Cheap layout facts a screenshot alone will not tell you. */
async function layout() {
  return page.evaluate(() => {
    const body = document.documentElement;
    const clipped = [];
    for (const el of document.querySelectorAll("div,p,span,h1,h2,h3,button,td,li")) {
      const r = el.getBoundingClientRect();
      if (r.width < 4 || r.height < 4) continue;
      // Text that does not fit the box it was given and is not scrollable.
      if (el.scrollWidth > el.clientWidth + 2 && getComputedStyle(el).overflowX === "hidden") {
        const t = (el.textContent || "").trim().slice(0, 50);
        if (t) clipped.push({ overflow: "x", by: el.scrollWidth - el.clientWidth, text: t });
      }
      if (r.bottom > window.innerHeight + 2 && r.top < window.innerHeight) {
        const t = (el.textContent || "").trim().slice(0, 40);
        if (t && el.childElementCount === 0)
          clipped.push({ overflow: "below-fold", by: Math.round(r.bottom - window.innerHeight), text: t });
      }
    }
    return {
      pageScrollsSideways: body.scrollWidth > body.clientWidth + 2,
      viewport: [window.innerWidth, window.innerHeight],
      clipped: clipped.slice(0, 6),
    };
  });
}

const manifest = [];
for (const [rail, ids] of Object.entries(GROUPS)) {
  for (const id of ids) {
    const how = await open(rail, id);
    const file = `${OUT}/${rail}_${id}.png`;
    await page.screenshot({ path: file }).catch(() => {});
    const lay = how ? await layout() : { note: "not opened" };
    if (how === "modal") await page.keyboard.press("Escape").catch(() => {});
    manifest.push({ rail, id, how, ...lay });
    const flags = [
      lay.pageScrollsSideways ? "SIDEWAYS-SCROLL" : "",
      (lay.clipped?.length ?? 0) > 0 ? `CLIPPED x${lay.clipped.length}` : "",
      how ? "" : "NOT-OPENED",
    ].filter(Boolean);
    console.log(`  ${rail.padEnd(7)} ${id.padEnd(16)} ${(how ?? "-").padEnd(6)} ${flags.join("  ")}`);
  }
}
fs.writeFileSync(`${OUT}/manifest.json`, JSON.stringify(manifest, null, 2));
const flagged = manifest.filter((m) => m.pageScrollsSideways || (m.clipped?.length ?? 0) > 0 || !m.how);
console.log(`\n  ${manifest.length} shots -> ${OUT}`);
console.log(`  ${flagged.length} flagged for a look:`);
for (const f of flagged) {
  const why = f.pageScrollsSideways ? "sideways scroll" : !f.how ? "did not open" : `${f.clipped.length} clipped`;
  console.log(`    ${f.rail}/${f.id}  ${why}`);
  for (const c of f.clipped ?? []) console.log(`        ${c.overflow} by ${c.by}px: ${c.text}`);
}
await browser.close();
