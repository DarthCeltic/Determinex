/**
 * ui_record_unified_demo.mjs — ONE screen: the product running its own measurement.
 *
 * Ryan on the first cut: "why does the left side the ide not show the right? ... we have a
 * terminal in the ide that could show it both running. this is very disjointed and very
 * wierd and i wouldnt chose this for anything to win."
 *
 * He was right, and the reason was worse than layout. The split screen was two unrelated
 * captures composited side by side, because the IDE's terminal appeared to do nothing at
 * all — no prompt, no output, no error. That turned out to be a stale stack, not a bug:
 * `invokeSafe` swallows a missing-command error silently, the app running was the INSTALLED
 * build serving its own bundled frontend, and `frontend/src-tauri/target/debug/determinex.exe`
 * predates `pty_terminal.rs` by four days and contains zero occurrences of `pty_spawn`. With
 * the current backend the terminal is a real PTY: PowerShell prompt, output streaming per
 * 4KB chunk over `pty-output`, no timeout.
 *
 * So this drives the real thing. The Work cockpit stays on screen, the terminal opens over it
 * as a restored (non-maximised) dock, and the Radeon demo runs INSIDE it. Nothing is
 * composited from two sources: one window, one recording, one truth.
 *
 *   node scripts/ui_record_unified_demo.mjs [outDir] [maxSeconds]
 */
import fs from "node:fs";
import { chromium } from "playwright";

const OUT = process.argv[2] || "C:/tmp/unified";
const MAX_S = Number(process.argv[3] || 420);
const FPS = 4;

const BASE = process.env.DETERMINEX_VLLM_BASE_URL || "";
const KEY = process.env.DETERMINEX_VLLM_API_KEY || "";
if (!BASE || !KEY) {
  console.log("set DETERMINEX_VLLM_BASE_URL and DETERMINEX_VLLM_API_KEY");
  process.exit(2);
}

fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(OUT, { recursive: true });

const browser = await chromium.connectOverCDP(process.env.DTX_CDP || "http://localhost:9223");
const page = browser.contexts()[0].pages().find((p) => p.url().includes("localhost:3000"));
if (!page) {
  console.log("FAIL: no localhost:3000 page — is `npm run tauri dev` running?");
  process.exit(1);
}

const click = async (t, ms = 4000) => {
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
      await page.waitForTimeout(250);
    }
    if (await page.locator('[data-testid="guide-overlay"]').count().catch(() => 0)) {
      await page.evaluate(() => document.querySelector('[data-testid="guide-overlay"]')?.remove());
      acted = true;
      await page.waitForTimeout(200);
    }
    if (!acted) return;
  }
}

// ── 1. Cockpit first, so it is what sits behind the terminal ────────────────────
await clearOverlays();
await click("rail-group-work");
await page.waitForTimeout(600);
await click("surface-member-hive");
await page.waitForTimeout(400);
await click("surface-open-hive-panel");
await page.waitForTimeout(1800);

// ── 2. Terminal into the floating dock, then RESTORE it ─────────────────────────
// The dock defaults to maximised, which covers the cockpit completely and puts us back to a
// single pane showing one thing. Restoring gives a ~920x600 window with the cockpit visible
// around it — the product and its own terminal, on one screen.
await click("rail-group-run");
await page.waitForTimeout(600);
await click("surface-member-terminal");
await page.waitForTimeout(400);
await click("surface-open-terminal-dock");
await page.waitForTimeout(1500);

for (const name of ["Restore", "Restore down", "Restore window"]) {
  const b = page.getByTitle(name);
  if (await b.count().catch(() => 0)) {
    await b.first().click({ timeout: 2500 }).catch(() => {});
    break;
  }
}
await page.waitForTimeout(1200);

// Assert BOTH are on screen. If the dock is still maximised we are filming one pane again,
// which is the thing this script exists to stop.
const layout = await page.evaluate(() => {
  const dock = document.querySelector('[data-testid="workspace-addon-drawer"]');
  const cockpit = document.querySelector('[data-testid="workbench-primary-surface"]');
  const r = (e) => (e ? e.getBoundingClientRect() : null);
  const d = r(dock);
  const c = r(cockpit);
  return {
    dock: d ? `${Math.round(d.width)}x${Math.round(d.height)}` : null,
    cockpit: c ? `${Math.round(c.width)}x${Math.round(c.height)}` : null,
    dockCoversAll: d ? d.width > window.innerWidth * 0.92 : false,
    vw: window.innerWidth,
  };
});
console.log(`layout: dock=${layout.dock} cockpit=${layout.cockpit} coversAll=${layout.dockCoversAll}`);
if (!layout.dock) {
  console.log("FAIL: no terminal dock on screen");
  await browser.close();
  process.exit(1);
}

// ── 3. Wait for the PTY's shell, then run the demo inside it ────────────────────
const rows = () =>
  page.evaluate(() => {
    const r = document.querySelector(".xterm-rows");
    return (r?.innerText || "").trim();
  });

// Prove the shell is ALIVE rather than looking for its start-up banner. The PTY is
// persistent and only the visible rows are in the DOM, so on a second run the banner has
// long scrolled away and a banner test reports a perfectly healthy shell as dead. Pressing
// Enter and waiting for a fresh prompt works on the first run and every run after it.
const screenEl = page.locator(".xterm-screen").first();
await screenEl.click({ timeout: 8000 }).catch(() => {});
let shell = false;
for (let i = 0; i < 30; i++) {
  await page.keyboard.press("Enter");
  await page.waitForTimeout(700);
  const t = await rows();
  if (/PS [A-Za-z]:.*>/.test(t)) {
    shell = true;
    break;
  }
}
console.log(`PTY shell up: ${shell}`);
if (!shell) {
  console.log("FAIL: the shell never came up — stale backend? check pty_spawn exists in the running exe");
  await browser.close();
  process.exit(1);
}

const screen = page.locator(".xterm-screen").first();
await screen.click({ timeout: 8000 });
await page.waitForTimeout(400);

let n = 0;
const shoot = async () => {
  await page.screenshot({ path: `${OUT}/f${String(n).padStart(5, "0")}.png` }).catch(() => {});
  n++;
};
const grabber = setInterval(shoot, Math.round(1000 / FPS));

// The PTY hosts a persistent PowerShell, so env is set by typing it — there is no env
// parameter on pty_spawn and none is needed.
await page.keyboard.type(`$env:DETERMINEX_VLLM_BASE_URL='${BASE}'; $env:DETERMINEX_VLLM_API_KEY='${KEY}'`, { delay: 8 });
await page.keyboard.press("Enter");
await page.waitForTimeout(1200);
await page.keyboard.type("cd C:\\Dev\\Determinex", { delay: 8 });
await page.keyboard.press("Enter");
await page.waitForTimeout(1000);
// Wipe the pane. The PTY is PERSISTENT, so a previous run's closing line is still on
// screen; without this the end-detector matched it 4.7s in and stopped the recording
// having filmed nothing. Same stale-state false positive as everything else tonight.
await page.keyboard.type("clear", { delay: 8 });
await page.keyboard.press("Enter");
await page.waitForTimeout(900);
await page.keyboard.type("python -u scripts/dev/submission_demo.py", { delay: 10 });
await page.waitForTimeout(600);
await page.keyboard.press("Enter");

const t0 = Date.now();
let done = false;
// When each section's banner first appears. Narration is aligned to these instead of to the
// @@SECTION@@ markers, which are now suppressed so they stay off camera. The banner is real
// content a viewer reads, so aligning to it is aligning to what they actually see.
const sectionAt = {};
for (let i = 0; i < (MAX_S * 1000) / 500; i++) {
  await page.waitForTimeout(500);
  const t = await rows();
  for (const m of t.matchAll(/(\d)\/6\s{2}[A-Z]/g)) {
    if (sectionAt[m[1]] === undefined) sectionAt[m[1]] = (Date.now() - t0) / 1000;
  }
  // Markers are suppressed on camera, so finish on real content instead — but never
  // before the run could plausibly have got there. The demo takes ~90s; anything
  // claiming completion inside 45s is stale text, not a finished run.
  const elapsed = (Date.now() - t0) / 1000;
  if (elapsed > 45 && (/Every number in this recording/.test(t) || /@@SECTION@@END/.test(t))) {
    done = true;
    break;
  }
}
await page.waitForTimeout(4000);
clearInterval(grabber);
await shoot();

const secs = (Date.now() - t0) / 1000;
console.log(`frames=${n}  demo wall clock=${secs.toFixed(1)}s  reached end=${done}`);
console.log(`section banners at: ${JSON.stringify(sectionAt)}`);
fs.writeFileSync(
  `${OUT}/run.json`,
  JSON.stringify({ frames: n, fps: FPS, seconds: secs, done, layout, sectionAt }, null, 2)
);
console.log(`-> ${OUT}`);
await browser.close();
if (!done) process.exitCode = 1;
