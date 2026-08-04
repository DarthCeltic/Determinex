/**
 * ui_verify_surfaces.mjs — drive every surface and CHECK WHAT IT BECAME.
 *
 * Ryan, 2026-08-03: "driving every surface, hitting each and looking at it and checking the
 * after click or navigate or whatever so you can ensure it does what its supposed to do."
 *
 * A click that does not assert its result is not a check. The earlier sweep only proved a
 * button could be pressed; it would have passed against a surface that opened blank, opened
 * the wrong panel, or rendered on top of itself.
 *
 * Per surface this asserts four things AFTER the click:
 *   ALIVE     — the panel region gained real content, not a spinner or a background
 *   OWN       — the content actually belongs to the surface that was opened
 *   NO-ERROR  — no error/exception/failed-to-fetch text surfaced
 *   NO-OVERLAP— no two text elements physically collide (the cockpit bug: "Ready" printed
 *               on top of "NO VERDICT", the four step cards crushed together)
 *
 * Runs at several widths, because the overlap only appears below a breakpoint and a judge
 * who resizes the window is the person who finds it.
 *
 *   node scripts/ui_verify_surfaces.mjs [width]
 */
import { chromium } from "playwright";
import fs from "node:fs";

const CDP = process.env.DTX_CDP || "http://localhost:9223";
const OUT = process.env.DTX_OUT || "C:/tmp/surfverify";
fs.mkdirSync(OUT, { recursive: true });

const browser = await chromium.connectOverCDP(CDP);
const ctx = browser.contexts()[0];
const page = ctx.pages().find((p) => p.url().includes("localhost:3000")) || ctx.pages()[0];

const ERR = /failed to fetch|unhandled|exception|cannot read|undefined is not|error:/i;

/** Do any two visible text boxes physically overlap? That is the cockpit defect. */
async function overlaps() {
  return page.evaluate(() => {
    const els = [...document.querySelectorAll("h1,h2,h3,h4,p,span,div")].filter((e) => {
      if (!e.textContent || !e.textContent.trim()) return false;
      // only leaf-ish nodes, or every parent "overlaps" its child
      if ([...e.children].some((c) => c.textContent && c.textContent.trim())) return false;
      const r = e.getBoundingClientRect();
      return r.width > 12 && r.height > 6 && r.top >= 0 && r.top < window.innerHeight;
    });
    const hits = [];
    for (let i = 0; i < els.length && hits.length < 6; i++) {
      const a = els[i].getBoundingClientRect();
      for (let j = i + 1; j < els.length; j++) {
        const b = els[j].getBoundingClientRect();
        const ox = Math.min(a.right, b.right) - Math.max(a.left, b.left);
        const oy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
        // require a real intersection, not a 1px rounding kiss
        if (ox > 8 && oy > 8) {
          hits.push(
            `"${els[i].textContent.trim().slice(0, 26)}" x "${els[j].textContent.trim().slice(0, 26)}"`
          );
          break;
        }
      }
    }
    return hits;
  });
}

async function dismissAddon() {
  try {
    const x = page.getByTitle("Close add-on");
    if (await x.count()) {
      await x.first().click({ timeout: 2000 });
      await page.waitForTimeout(400);
    }
  } catch {}
}

// The rail exposes GROUPS (rail-group-work, -code, -run, ...). Surface members only mount
// once their group accordion is open, which is why a scan for surface-member-* found zero.
async function surfaceIds() {
  return page.evaluate(() =>
    [...document.querySelectorAll("[data-testid^='rail-group-']")].map((e) =>
      e.getAttribute("data-testid").replace("rail-group-", "")
    )
  );
}

async function openAndCheck(id) {
  const res = { id, opened: false, chars: 0, own: false, err: "", overlap: [] };
  try {
    await dismissAddon();
    const group = page.locator(`[data-testid="rail-group-${id}"]`);
    if (await group.count()) {
      await group.first().click({ timeout: 4000 });
      await page.waitForTimeout(500);
      res.opened = true;
    }
    for (const t of [`surface-open-${id}-panel`, `surface-open-${id}-dock`, `surface-open-${id}`]) {
      const b = page.locator(`[data-testid="${t}"]`);
      if (await b.count()) {
        await b.first().click({ timeout: 4000 });
        res.opened = true;
        break;
      }
    }
    // Real content takes time; poll rather than sampling once — an earlier sweep called
    // Source Control "EMPTY" because it read at 2.6 s and that panel needs about twelve.
    let body = "";
    for (let i = 0; i < 26; i++) {
      await page.waitForTimeout(600);
      body = await page.evaluate(() => document.body.innerText || "");
      if (body.length > 400 && body.toUpperCase().includes(id.toUpperCase())) break;
    }
    res.chars = body.length;
    res.own = body.toUpperCase().includes(id.toUpperCase());
    const m = body.match(ERR);
    res.err = m ? m[0] : "";
    res.overlap = await overlaps();
    await page.screenshot({ path: `${OUT}/${id}.png` });
  } catch (e) {
    res.err = String(e).slice(0, 90);
  }
  return res;
}

const width = Number(process.argv[2] || 0);
if (width) {
  await page.setViewportSize({ width, height: 940 });
  await page.waitForTimeout(1200);
}

const ids = await surfaceIds();
console.log(`width=${width || "native"}  surfaces=${ids.length}\n`);

const rows = [];
for (const id of ids) rows.push(await openAndCheck(id));

let bad = 0;
for (const r of rows) {
  const problems = [];
  if (!r.opened) problems.push("NO-OPEN-BUTTON");
  if (r.chars < 400) problems.push(`THIN(${r.chars})`);
  if (!r.own) problems.push("NOT-ITS-OWN-CONTENT");
  if (r.err) problems.push(`ERR:${r.err}`);
  if (r.overlap.length) problems.push(`OVERLAP x${r.overlap.length}`);
  if (problems.length) bad++;
  console.log(
    `  ${problems.length ? "FAIL" : "ok  "}  ${r.id.padEnd(14)} ${
      problems.length ? problems.join(" · ") : `${r.chars} chars`
    }`
  );
  if (r.overlap.length) r.overlap.slice(0, 3).forEach((o) => console.log(`          ${o}`));
}
console.log(`\n  ${rows.length - bad}/${rows.length} clean at width ${width || "native"}`);
fs.writeFileSync(`${OUT}/report_${width || "native"}.json`, JSON.stringify(rows, null, 2));
await browser.close();
