/**
 * ui_record_scroll.mjs — film a surface being READ, not stared at.
 *
 * Ryan: "nothing is really changed on this window." Some sections of the demo have only a
 * few seconds of terminal footage against half a minute of narration, so they cut to a still
 * and freeze. A still is a still however relevant it is.
 *
 * Scrolling a panel is real motion AND real content: the viewer gets to see the rest of the
 * surface instead of the top 40% of it held for thirty seconds. This drives one surface,
 * scrolls it slowly to the bottom, and captures while it moves.
 *
 *   node scripts/ui_record_scroll.mjs <group> <member> <outDir> [seconds]
 */
import fs from "node:fs";
import { chromium } from "playwright";

const [group, member] = [process.argv[2], process.argv[3]];
const OUT = process.argv[4] || `C:/tmp/scroll_${member}`;
const SECONDS = Number(process.argv[5] || 22);
const FPS = 4;

if (!group || !member) {
  console.log("usage: node scripts/ui_record_scroll.mjs <group> <member> <outDir> [seconds]");
  process.exit(2);
}
fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(OUT, { recursive: true });

const browser = await chromium.connectOverCDP(process.env.DTX_CDP || "http://localhost:9223");
const page = browser.contexts()[0].pages().find((p) => p.url().includes("localhost:3000"));

const click = async (t) => {
  const l = page.locator(`[data-testid="${t}"]`);
  if (!(await l.count())) return false;
  await l.first().click({ timeout: 5000 }).catch(() => {});
  return true;
};

for (let i = 0; i < 4; i++) {
  const x = page.getByTitle("Close add-on");
  if (!(await x.count().catch(() => 0))) break;
  await x.first().click({ timeout: 2000 }).catch(() => {});
  await page.waitForTimeout(220);
}
if (await page.locator('[data-testid="guide-overlay"]').count().catch(() => 0)) {
  await page.evaluate(() => document.querySelector('[data-testid="guide-overlay"]')?.remove());
}

await click(`rail-group-${group}`);
await page.waitForTimeout(700);
await click(`surface-member-${member}`);
await page.waitForTimeout(450);
await click(`surface-open-${member}-panel`);
await click(`surface-open-${member}-dock`);
await click(`tools-launch-${member}`);

// Let it finish before filming, or the first frames are a loading state.
for (let i = 0; i < 80; i++) {
  await page.waitForTimeout(500);
  const ok = await page.evaluate(() => {
    const r =
      document.querySelector("[data-testid$='-hosted-addon']") ||
      document.querySelector('[data-testid="workbench-primary-surface"]');
    if (!r) return false;
    const t = (r.innerText || "").trim();
    if (r.querySelector(".animate-spin") && t.length < 150) return false;
    return t.length >= 40;
  });
  if (ok) break;
}
await page.waitForTimeout(800);

const shots = Math.max(4, SECONDS * FPS);
for (let i = 0; i < shots; i++) {
  await page.screenshot({ path: `${OUT}/f${String(i).padStart(4, "0")}.png` }).catch(() => {});
  // Ease into the scroll and ease out, so it reads as deliberate rather than a jerk.
  const frac = i / (shots - 1);
  await page.evaluate((f) => {
    const root =
      document.querySelector("[data-testid$='-hosted-addon']") ||
      document.querySelector('[data-testid="workbench-primary-surface"]');
    if (!root) return;
    const scrollers = [...root.querySelectorAll("*")].filter(
      (e) => e.scrollHeight > e.clientHeight + 40 && e.clientHeight > 180
    );
    const target = scrollers.sort((a, b) => b.clientHeight - a.clientHeight)[0];
    if (!target) return;
    const max = target.scrollHeight - target.clientHeight;
    // hold at the top for the first 15%, then travel, then rest at the bottom
    const eased = f < 0.15 ? 0 : Math.min((f - 0.15) / 0.7, 1);
    target.scrollTop = max * eased;
  }, frac);
  await page.waitForTimeout(Math.round(1000 / FPS));
}

fs.writeFileSync(
  `${OUT}/run.json`,
  JSON.stringify({ group, member, frames: shots, fps: FPS, seconds: SECONDS }, null, 2) + "\n"
);
console.log(`${group}/${member}: ${shots} frames over ~${SECONDS}s -> ${OUT}`);
await browser.close();
