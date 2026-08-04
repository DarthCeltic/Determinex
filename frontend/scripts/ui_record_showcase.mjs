/**
 * ui_record_showcase.mjs — the product tour, DRIVEN, not screenshotted.
 *
 * Ryan on the old showcase: "product showcase is all static... these are not worthy of
 * anything". It was six stills of idle panels, several of them showing a broken state
 * (aider not signed in, cursor-agent not installed) that later work had already fixed.
 *
 * This walks the app the way a person would and films it doing so: open a group, open a
 * surface, let it finish rendering, move on. Every frame is the live product on the current
 * backend — which matters, because the backend the last tour was shot against could not
 * answer half of what it displayed. On the current one Cloak reports 1,714,560 cloaked
 * identifiers and 0 leaks, the Flywheel shows its real corpus, and Brain's Role Slots
 * actually bind to models instead of sitting on "loading..." forever.
 *
 *   node scripts/ui_record_showcase.mjs [outDir]
 */
import fs from "node:fs";
import { chromium } from "playwright";

const OUT = process.argv[2] || "C:/tmp/showcase";
const FPS = 4;

fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(OUT, { recursive: true });

const browser = await chromium.connectOverCDP(process.env.DTX_CDP || "http://localhost:9223");
const page = browser.contexts()[0].pages().find((p) => p.url().includes("localhost:3000"));
if (!page) {
  console.log("FAIL: no localhost:3000 page — is `npm run tauri dev` running?");
  process.exit(1);
}

const click = async (t, ms = 5000) => {
  const l = page.locator(`[data-testid="${t}"]`);
  if (!(await l.count())) return false;
  await l.first().click({ timeout: ms }).catch(() => {});
  return true;
};

async function clearOverlays() {
  for (let i = 0; i < 5; i++) {
    let acted = false;
    const x = page.getByTitle("Close add-on");
    if (await x.count().catch(() => 0)) {
      await x.first().click({ timeout: 2000 }).catch(() => {});
      acted = true;
      await page.waitForTimeout(220);
    }
    if (await page.locator('[data-testid="guide-overlay"]').count().catch(() => 0)) {
      await page.evaluate(() => document.querySelector('[data-testid="guide-overlay"]')?.remove());
      acted = true;
      await page.waitForTimeout(200);
    }
    const modal = await page
      .evaluate(() => {
        const m = document.querySelector('[data-testid="settings-modal"]');
        return !!(m && m.getBoundingClientRect().width > 100);
      })
      .catch(() => false);
    if (modal) {
      const c = page.getByRole("button", { name: /close config/i });
      if (await c.count().catch(() => 0)) await c.first().click({ timeout: 2000 }).catch(() => {});
      else await page.keyboard.press("Escape").catch(() => {});
      acted = true;
      await page.waitForTimeout(300);
    }
    if (!acted) return;
  }
}

const activeRoot = () =>
  page.evaluate(() => {
    const big = (e) => {
      const r = e?.getBoundingClientRect?.();
      return r && r.width > 200 && r.height > 200;
    };
    const m = document.querySelector('[data-testid="settings-modal"]');
    if (big(m)) return '[data-testid="settings-modal"]';
    const z = [...document.querySelectorAll("[data-testid$='-hosted-addon']")].find(big);
    if (z) return `[data-testid="${z.getAttribute("data-testid")}"]`;
    const p = document.querySelector('[data-testid="workbench-primary-surface"]');
    return big(p) ? '[data-testid="workbench-primary-surface"]' : "unknown";
  });

async function settled() {
  const root = await activeRoot();
  if (root === "unknown") return true;
  return page.evaluate((s) => {
    const el = document.querySelector(s);
    if (!el) return false;
    const text = (el.innerText || "").trim();
    if (el.querySelector('.animate-spin,[role="progressbar"]') && text.length < 150) return false;
    if (
      text
        .split(/\r?\n/)
        .some((l) => /^(scanning|loading|fetching|initializing|please wait)[.…\s]*$/i.test(l.trim()))
    )
      return false;
    return text.length >= 40;
  }, root);
}

/**
 * Each stop is captured into its OWN directory, after it has settled.
 *
 * Three attempts were made to slice one continuous recording into per-stop spans, and all
 * three put the wrong screen under the narration: the nominal 4fps was really 2.93 because a
 * screenshot costs ~100ms; the stop's end boundary included the next stop's navigation; and
 * even with millisecond-stamped filenames the two clocks still disagreed by seconds. Every
 * fix was a patch on the same class of error -- inferring "what was on screen when" from
 * arithmetic instead of from the screen.
 *
 * Capturing per stop removes the arithmetic entirely. There is no cross-stop boundary to get
 * wrong, because frames for a stop are only ever taken while that stop is the thing open.
 */
let total = 0;
async function captureStop(member, seconds) {
  const dir = `${OUT}/${member}`;
  fs.mkdirSync(dir, { recursive: true });
  const shots = Math.max(2, Math.round(seconds * FPS));
  for (let i = 0; i < shots; i++) {
    await page
      .screenshot({ path: `${dir}/f${String(i).padStart(4, "0")}.png` })
      .catch(() => {});
    total++;
    // SCROLL while filming. Six seconds of footage under fifteen seconds of narration
    // means nine seconds of a frozen panel, which is the same "nothing really changes on
    // this window" the main demo was rejected for. Scrolling is motion and it also shows
    // the rest of the surface instead of its top third held until the sentence ends.
    // Eased: still at the top briefly, then travel, then rest at the bottom.
    const frac = i / Math.max(shots - 1, 1);
    await page
      .evaluate((f) => {
        const root =
          document.querySelector("[data-testid$='-hosted-addon']") ||
          document.querySelector('[data-testid="workbench-primary-surface"]');
        if (!root) return;
        const target = [...root.querySelectorAll("*")]
          .filter((e) => e.scrollHeight > e.clientHeight + 40 && e.clientHeight > 180)
          .sort((a, b) => b.clientHeight - a.clientHeight)[0];
        if (!target) return;
        const max = target.scrollHeight - target.clientHeight;
        const eased = f < 0.18 ? 0 : Math.min((f - 0.18) / 0.68, 1);
        target.scrollTop = max * eased;
      }, frac)
      .catch(() => {});
    await page.waitForTimeout(Math.round(1000 / FPS));
  }
  return shots;
}

// The tour. Chosen so a judge sees the ARGUMENT, not a menu: what it is, the proof it
// keeps, what it hides from the cloud, what it has learned, and what it admits it cannot do.
const TOUR = [
  ["work", "hive", "the cockpit — ask, plan, build, prove"],
  ["prove", "proof", "the proof ledger — oracle verdicts, not model opinions"],
  ["trust", "cloak", "Project Cloak — what the cloud never sees"],
  ["learn", "benchmark", "Brain & Model Slots — which model plays which role"],
  ["system", "flywheel", "the flywheel — every verified solve becomes training data"],
  ["system", "mission", "Mission Control — its own release gates, honestly counted"],
  ["system", "roadmap", "the roadmap — what is partial, and what is blocked"],
];

const marks = [];
const t0 = Date.now();
for (const [group, member, label] of TOUR) {
  await clearOverlays();
  if (!(await page.locator(`[data-testid="surface-member-${member}"]`).count())) {
    await click(`rail-group-${group}`);
    await page.waitForTimeout(700);
  }
  if (!(await click(`surface-member-${member}`))) {
    console.log(`  !! ${group}/${member} missing — skipped`);
    continue;
  }
  await page.waitForTimeout(450);
  await click(`surface-open-${member}-panel`);
  await click(`surface-open-${member}-dock`);
  await click(`surface-open-${member}`);
  await click(`tools-launch-${member}`);

  let ok = false;
  for (let i = 0; i < 200; i++) {
    await page.waitForTimeout(500);
    if (await settled()) {
      ok = true;
      break;
    }
  }
  // Only now, with this surface open and finished, does filming start.
  const shots = await captureStop(member, 19);
  marks.push({ group, member, label, settled: ok, shots });
  console.log(`  ${ok ? "shot" : "TIMED OUT"} ${group}/${member}  ${shots} frames`);
}

fs.writeFileSync(
  `${OUT}/run.json`,
  JSON.stringify({ frames: total, fps: FPS, seconds: (Date.now() - t0) / 1000, marks }, null, 2) +
    "\n"
);
console.log(`frames=${total}  ${((Date.now() - t0) / 1000).toFixed(1)}s -> ${OUT}`);
await browser.close();
if (marks.some((m) => !m.settled)) process.exitCode = 1;
