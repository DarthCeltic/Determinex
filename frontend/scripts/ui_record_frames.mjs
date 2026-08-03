/**
 * Record the IDE by screenshotting the PAGE over CDP, not by grabbing the screen.
 *
 * WHY NOT gdigrab. A window-title screen grab records the screen REGION the window occupies.
 * When the Determinex window was behind another app, the take contained that other app --
 * a 120-second recording of somebody else's chat window, produced by a pipeline that
 * reported success at every step. That is the same failure as a probe attaching to the wrong
 * debugger port and confidently describing someone else's tab.
 *
 * `page.screenshot()` renders the page itself. It cannot capture a different window, it does
 * not care whether the app is focused, occluded, or off-screen, and it needs no foreground
 * juggling. The frames are then assembled by ffmpeg at a fixed rate.
 *
 * The drive runs in parallel with the frame grabber, and both stop together.
 */
import fs from "node:fs";
import { chromium } from "playwright";

const OUT_DIR = process.argv[2] ?? "C:/tmp/frames";
const FPS = 4;
const MAX_SECONDS = 600;

fs.rmSync(OUT_DIR, { recursive: true, force: true });
fs.mkdirSync(OUT_DIR, { recursive: true });

const browser = await chromium.connectOverCDP("http://localhost:9223");
const page = browser
  .contexts()[0]
  .pages()
  .find((p) => !p.url().startsWith("devtools://"));
if (!page) {
  console.log("no app page on 9223");
  process.exit(2);
}

// Verify WHAT we are about to record before recording it.
const title = await page.title();
if (!/determinex/i.test(title)) {
  console.log(`refusing to record: attached page is "${title}"`);
  process.exit(2);
}
console.log(`recording page: ${title}`);

let stop = false;
let n = 0;
const grabber = (async () => {
  const started = Date.now();
  while (!stop && (Date.now() - started) / 1000 < MAX_SECONDS) {
    const t = Date.now();
    await page
      .screenshot({ path: `${OUT_DIR}/f_${String(n).padStart(5, "0")}.png` })
      .catch(() => {});
    n += 1;
    const spent = Date.now() - t;
    await new Promise((r) => setTimeout(r, Math.max(0, 1000 / FPS - spent)));
  }
})();

process.on("SIGINT", () => {
  stop = true;
});

// Signal file: the drive writes it when finished, so this process knows to stop.
const DONE = `${OUT_DIR}/../frames_done.flag`;
fs.rmSync(DONE, { force: true });
const watcher = setInterval(() => {
  if (fs.existsSync(DONE)) {
    stop = true;
    clearInterval(watcher);
  }
}, 500);

await grabber;
clearInterval(watcher);
console.log(`captured ${n} frames at ${FPS} fps -> ${OUT_DIR}`);
await browser.close();
