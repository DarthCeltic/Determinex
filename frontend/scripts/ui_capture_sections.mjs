/**
 * ui_capture_sections.mjs — capture one real IDE screenshot per demo section.
 *
 * The submission video shows the product on the left and the live GPU terminal on the right.
 * These are the left-hand frames, taken from the RUNNING app over CDP (never a screen grab —
 * a window-region grab once recorded two minutes of somebody else's chat window while
 * reporting success at every step).
 *
 * REWRITTEN 2026-08-04. The previous version called `openSurface("WORK")`, which looked for
 * `surface-member-WORK`. No such element exists: members are lowercase ids (`hive`, `build`,
 * `proof`, `trace`, `benchmark`) and the drawer has to be opened from `rail-group-<g>` first,
 * because opening a panel closes it again. Every miss was swallowed by a try/catch that
 * returned false, so the run "succeeded" while shooting six near-identical frames of whatever
 * happened to be on screen. That is precisely the "shows NOTHING, just screens" the last
 * showcase was rejected for — the capture, not the product.
 *
 * It also shot on a fixed timer. The surface map measured what that costs: Explorer sits on
 * "Scanning..." for ~8s, run/build settles at 6.7s and learn/benchmark at 20.3s. A 900ms wait
 * photographs a loading state and calls it the product. So each frame now waits for the
 * surface to actually finish rendering, and says how long it took.
 *
 *   node scripts/ui_capture_sections.mjs <outDir>
 */
import { chromium } from "playwright";
import fs from "node:fs";

const CDP = process.env.DTX_CDP || "http://localhost:9223";
const OUT = process.argv[2] || "C:/tmp/vidshots";
fs.mkdirSync(OUT, { recursive: true });

const browser = await chromium.connectOverCDP(CDP);
const ctx = browser.contexts()[0];
const page = ctx.pages().find((p) => p.url().includes("localhost:3000")) || ctx.pages()[0];
// Do NOT force a viewport. Forcing 1500x940 collapsed the cockpit grid into
// overlapping text -- "Ready" on top of "NO VERDICT", the four step cards crushed
// together. Capture the app at the size it actually runs at.
const vp = await page.evaluate(() => `${innerWidth}x${innerHeight}`);
console.log(`  native viewport: ${vp}`);

const click = async (tid, ms = 4000) => {
  const l = page.locator(`[data-testid="${tid}"]`);
  if (!(await l.count())) return false;
  await l.first().click({ timeout: ms }).catch(() => {});
  return true;
};

/** Uncover the workbench: maximised add-on, Config Vault modal, and the 16-step tour. */
async function clearOverlays() {
  for (let i = 0; i < 5; i++) {
    let acted = false;
    const x = page.getByTitle("Close add-on");
    if (await x.count().catch(() => 0)) {
      await x.first().click({ timeout: 2000 }).catch(() => {});
      acted = true;
      await page.waitForTimeout(250);
    }
    if (await page.locator('[data-testid="guide-overlay"]').count().catch(() => 0)) {
      await page.keyboard.press("Escape").catch(() => {});
      await page.evaluate(() =>
        document.querySelector('[data-testid="guide-overlay"]')?.remove()
      );
      acted = true;
      await page.waitForTimeout(250);
    }
    const modalOpen = await page
      .evaluate(() => {
        const m = document.querySelector('[data-testid="settings-modal"]');
        return !!(m && m.getBoundingClientRect().width > 100);
      })
      .catch(() => false);
    if (modalOpen) {
      const close = page.getByRole("button", { name: /close config/i });
      if (await close.count().catch(() => 0)) await close.first().click({ timeout: 2000 }).catch(() => {});
      else await page.keyboard.press("Escape").catch(() => {});
      acted = true;
      await page.waitForTimeout(300);
    }
    if (!acted) return;
  }
}

/** The container the surface really rendered into — usually a hosted add-on zone. */
const activeRoot = () =>
  page.evaluate(() => {
    const big = (e) => {
      const r = e?.getBoundingClientRect?.();
      return r && r.width > 200 && r.height > 200;
    };
    const zone = [...document.querySelectorAll("[data-testid$='-hosted-addon']")].find(big);
    if (zone) return `[data-testid="${zone.getAttribute("data-testid")}"]`;
    const prim = document.querySelector('[data-testid="workbench-primary-surface"]');
    return big(prim) ? '[data-testid="workbench-primary-surface"]' : "body";
  });

/** Rendered, or still loading? A spinner and a bare "Scanning..." both mean not yet. */
async function settled() {
  const root = await activeRoot();
  return page.evaluate((s) => {
    const el = s === "body" ? document.body : document.querySelector(s);
    if (!el) return false;
    if (el.querySelector('.animate-spin,[role="progressbar"],[aria-busy="true"]')) return false;
    const text = (el.innerText || "").trim();
    const waiting = text
      .split(/\r?\n/)
      .some((l) => /^(scanning|loading|fetching|initializing|please wait)[.…\s]*$/i.test(l.trim()));
    if (waiting) return false;
    return text.length >= 40;
  }, root);
}

/** Open group -> member -> panel. Opening a panel closes the drawer, so re-open each time. */
async function openSurface(group, member) {
  await clearOverlays();
  if (!(await page.locator(`[data-testid="surface-member-${member}"]`).count())) {
    await click(`rail-group-${group}`);
    await page.waitForTimeout(650);
  }
  if (!(await click(`surface-member-${member}`))) {
    console.log(`  !! ${group}/${member}: no such member — NOT captured`);
    return false;
  }
  await page.waitForTimeout(400);
  await click(`surface-open-${member}-panel`);
  await click(`surface-open-${member}-dock`);
  await click(`surface-open-${member}`);
  await click(`tools-launch-${member}`);
  return true;
}

/** Wait for the surface to finish, then shoot. Reports the wait so a slow one is visible. */
async function shot(name, group, member) {
  const ok = await openSurface(group, member);
  if (!ok) {
    process.exitCode = 1;
    return;
  }
  const t0 = Date.now();
  let done = false;
  for (let i = 0; i < 60; i++) {
    await page.waitForTimeout(500);
    if (await settled()) {
      done = true;
      break;
    }
  }
  const ms = Date.now() - t0;
  await page.waitForTimeout(400);
  await page.screenshot({ path: `${OUT}/${name}.png` });
  console.log(
    `  ${done ? "captured" : "TIMED OUT"} ${name}  (${group}/${member}, settled in ${(ms / 1000).toFixed(1)}s)`
  );
  if (!done) process.exitCode = 1;
}

// Section -> the surface that actually shows what the narration is talking about.
await clearOverlays();
await shot("s0", "work", "hive"); // the cockpit: what you see when you sit down
await shot("s1", "run", "build"); // throughput: the run/oracle surface (6.7s settle)
await shot("s2", "prove", "proof"); // the ceiling: oracle verdicts
await shot("s3", "prove", "trace"); // access pattern: per-step trace
await shot("s4", "learn", "benchmark"); // where it works and where it does not (20.3s settle)
await shot("s5", "work", "hive"); // refuse then earn: where an idea is entered

console.log(process.exitCode ? "DONE WITH FAILURES" : "done — all sections captured settled");
await browser.close();
