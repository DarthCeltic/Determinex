/**
 * ui_record_live_build.mjs — record the IDE doing REAL work, not posing for a photo.
 *
 * Ryan on the rejected showcase: "the showcase shows NOTHING just screens", "nothing in
 * flight". Six settled screenshots of idle panels are still six screenshots; run/build with
 * "No diagnostics reported" is an honest frame of nothing happening. This drives an actual
 * oracle-verified build through the cockpit and grabs frames while it runs, so what is on
 * screen is the product working.
 *
 * Frames come from `page.screenshot()`, never a screen grab: a window-region grab once
 * recorded two minutes of somebody else's chat window while reporting success at every step.
 * A page screenshot renders the page itself and cannot capture a different window.
 *
 *   node scripts/ui_record_live_build.mjs [outDir] [seconds]
 */
import fs from "node:fs";
import { chromium } from "playwright";

const OUT = process.argv[2] || "C:/tmp/liveframes";
const MAX_S = Number(process.argv[3] || 240);
const FPS = 4;

fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(OUT, { recursive: true });

const browser = await chromium.connectOverCDP(process.env.DTX_CDP || "http://localhost:9223");
const page = browser.contexts()[0].pages().find((p) => p.url().includes("localhost:3000"));

const click = async (t) => {
  const l = page.locator(`[data-testid="${t}"]`);
  if (!(await l.count())) return false;
  await l.first().click({ timeout: 4000 }).catch(() => {});
  return true;
};

// Uncover, then open the cockpit. Never reload: it kills the Tauri IPC and every backend
// call then resolves null, which would look exactly like a build that silently did nothing.
for (let i = 0; i < 4; i++) {
  const x = page.getByTitle("Close add-on");
  if (!(await x.count().catch(() => 0))) break;
  await x.first().click({ timeout: 2000 }).catch(() => {});
  await page.waitForTimeout(250);
}
if (await page.locator('[data-testid="guide-overlay"]').count().catch(() => 0)) {
  await page.evaluate(() => document.querySelector('[data-testid="guide-overlay"]')?.remove());
}
await click("rail-group-work");
await page.waitForTimeout(600);
await click("surface-member-hive");
await page.waitForTimeout(400);
await click("surface-open-hive-panel");
await page.waitForTimeout(1500);

// An idea with concrete examples, so the oracle can synthesize real checks rather than
// refuse. The refusal path is its own story; this take is about a build that lands.
const IDEA =
  "solution(numbers) returns the average of a list of numbers. For example " +
  "solution([1, 2, 3]) returns 2.0, solution([10]) returns 10.0, and solution([]) returns 0.0.";

const box = page.getByPlaceholder(/describe what you want to build/i).first();
await box.waitFor({ state: "visible", timeout: 30000 });
await box.click();
await box.fill("");

let n = 0;
const shoot = async () => {
  await page
    .screenshot({ path: `${OUT}/f${String(n).padStart(5, "0")}.png` })
    .catch(() => {});
  n++;
};

// Type it visibly — the typing IS part of the footage.
const grabber = setInterval(shoot, Math.round(1000 / FPS));
await box.type(IDEA, { delay: 18 });
await page.waitForTimeout(800);

// TWO steps, not one. Quick Verify runs preview_idea_oracle and shows the oracle it
// would use; "Build Verified Program" only appears afterwards and runs build_idea to
// generate a program and verify it against that oracle. Earlier footage clicked the
// first button only, so the video claimed "a program verified against it" over a screen
// that showed nothing of the sort -- and it is also why the footage was so short.
const verify = page.getByRole("button", { name: /quick verify/i }).first();
const enabled = (await verify.count()) && (await verify.isEnabled().catch(() => false));
console.log(`quick-verify button: count=${await verify.count()} enabled=${enabled}`);
if (!enabled) {
  clearInterval(grabber);
  console.log("FAIL: the build control never enabled — nothing to record.");
  await browser.close();
  process.exit(1);
}
const t0 = Date.now();
await verify.click({ timeout: 8000 });

const buildBtn = page.getByRole("button", { name: /build verified program/i }).first();
await buildBtn.waitFor({ state: "visible", timeout: 180000 }).catch(() => {});
if (await buildBtn.count().catch(() => 0)) {
  await page.waitForTimeout(2500); // let the oracle sit on screen and be readable
  await buildBtn.click({ timeout: 8000 }).catch(() => {});
  console.log("build started");
}

// Watch for a real verdict rather than filming a fixed duration.
const TERMINAL = /oracle-verified|verified|passes all|solved|failed|refus|not sound|no example/i;
let verdict = "";
for (let i = 0; i < (MAX_S * 1000) / 500; i++) {
  await page.waitForTimeout(500);
  const t = await page.evaluate(() => document.body.innerText || "");
  const m = t.match(TERMINAL);
  if (m && Date.now() - t0 > 6000) {
    verdict = m[0];
    break;
  }
}
await page.waitForTimeout(2500);

// Then walk to Proof and film it carrying the verdict. Before the ledger fix this shot
// was an empty state, which is why the video used to close on "No evidence yet".
const clickTid = async (t) => {
  const l = page.locator(`[data-testid="${t}"]`);
  if (!(await l.count())) return false;
  await l.first().click({ timeout: 4000 }).catch(() => {});
  return true;
};
const x2 = page.getByTitle("Close add-on");
if (await x2.count().catch(() => 0)) await x2.first().click({ timeout: 2000 }).catch(() => {});
await clickTid("rail-group-prove");
await page.waitForTimeout(700);
await clickTid("surface-member-proof");
await page.waitForTimeout(450);
await clickTid("surface-open-proof-panel");
await page.waitForTimeout(6000);

clearInterval(grabber);
await shoot();

const secs = (Date.now() - t0) / 1000;
console.log(`frames: ${n}  build wall clock: ${secs.toFixed(1)}s  verdict matched: ${verdict || "(none)"}`);
fs.writeFileSync(
  `${OUT}/run.json`,
  JSON.stringify({ frames: n, fps: FPS, seconds: secs, verdict, idea: IDEA }, null, 2)
);
console.log(`-> ${OUT}`);
await browser.close();
if (!verdict) process.exitCode = 1;
