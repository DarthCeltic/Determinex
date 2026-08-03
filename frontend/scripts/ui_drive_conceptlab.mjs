/**
 * Drive the Concept Lab end to end over CDP, so the interview can be filmed doing real work.
 *
 * The story this tells is today's fix: the interview used to stop after 4 questions from a
 * static bank (and after only 2 replies in free-form), whatever the answers contained. It now
 * runs until a SOUND ORACLE can be synthesized from what the user has said.
 *
 * Run with --dry to rehearse without recording. Every step prints what it saw, so a failed
 * take is diagnosable instead of mysterious.
 */
import fs from "node:fs";
import { chromium } from "playwright";

const IDEA =
  "A command line tool that merges overlapping calendar bookings so I can see my real free time";

// Deliberately helpful-but-vague answers, exactly like a real user: none of them contains a
// concrete input/output example until the last one. The old build would have written the spec
// after four of these.
const ANSWERS = [
  "It should read a list of bookings and collapse the ones that overlap",
  "Python",
  "A CLI command I run in the terminal",
  "Standard library only, no dependencies",
  "If two bookings just touch end-to-start they should still merge",
  "merge([(9,10),(10,11)]) == [(9,11)] and merge([(9,10),(14,15)]) == [(9,10),(14,15)]",
];

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

/**
 * Wait until nothing is covering the page.
 *
 * `BootOverlay` is a full-screen opaque div at z-[110]. It is NOT a screensaver -- it is the
 * boot splash -- and in dev it comes BACK whenever Next Fast Refresh remounts the app, which
 * happens every time a frontend file is touched. Three takes died because the check was done
 * once at the start: the overlay was absent then, appeared during a 20-45s oracle wait, and
 * the next click timed out looking exactly like a dead button.
 *
 * So it is checked immediately before every interaction, not once at the top.
 */
async function waitUnobstructed(page, label = "") {
  const t0 = Date.now();
  await page.waitForFunction(
    () => !document.querySelector('div.absolute.inset-0[class*="z-[110]"]'),
    null,
    { timeout: 180000, polling: 400 }
  );
  const waited = (Date.now() - t0) / 1000;
  if (waited > 1) console.log(`   waited ${waited.toFixed(1)}s for the boot overlay${label ? ` (${label})` : ""}`);
}

const browser = await chromium.connectOverCDP("http://localhost:9223");
const page = browser
  .contexts()[0]
  .pages()
  .find((p) => !p.url().startsWith("devtools://"));
if (!page) {
  console.log("no app page on 9223");
  process.exit(2);
}

const errors = [];
page.on("console", (m) => m.type() === "error" && errors.push(m.text().slice(0, 160)));
page.on("pageerror", (e) => errors.push("PAGEERROR " + String(e).slice(0, 160)));

async function shot(name) {
  await page.screenshot({ path: `C:/tmp/drive_${name}.png` }).catch(() => {});
}

async function visibleText() {
  return page.evaluate(() => document.body.innerText);
}

console.log("== 0. reset to a clean start ==");
// A previous take can leave the app mid-flow (or on an error screen), and the drive would
// then fail looking for an input that is no longer on screen -- which reads as a broken app
// rather than a dirty starting state. Reload, then wait for the real entry point.
// Reload only if we are not already at the entry point, and NEVER fail on its promise: the
// Next dev server holds the connection open, so `reload()` can hang for 30s+ after the
// navigation has actually completed. Waiting for the UI is the real signal.
const atStart = await page
  .getByPlaceholder(/describe what you want to build/i)
  .first()
  .isVisible()
  .catch(() => false);
if (!atStart) {
  await page.reload({ waitUntil: "domcontentloaded", timeout: 15000 }).catch(() => {
    console.log("   (reload promise did not settle; continuing on the UI signal)");
  });
}
await page.locator("nav, [role='navigation']").first().waitFor({ timeout: 60000 });
// Wait for the CONTROL to be clickable rather than for the boot overlay to disappear.
// The app shows a full-screen splash (z-110) after a reload, and chasing that specific
// element meant guessing whether it unmounts or merely hides -- two wrong guesses and two
// timeouts. Playwright's actionability check already waits for the element to be visible,
// stable and unobstructed, which is the real precondition and covers any overlay.
const t0 = Date.now();
await page
  .getByPlaceholder(/describe what you want to build/i)
  .first()
  .waitFor({ state: "visible", timeout: 120000 });

// VISIBLE IS NOT THE SAME AS CLICKABLE.
//
// The app shows a full-screen boot overlay (`div.absolute.inset-0.z-[110].bg-black`) that
// the idea box is visible *behind*. Three takes died here: the text typed fine, and then
// CONSULT ORACLE timed out after 30s looking like a dead button, when the truth was that
// the overlay owned every pointer event. The precise condition is not "the overlay is gone"
// -- guessing whether it unmounts or merely hides cost two more attempts -- it is "the
// button is the element at its own centre".
await page.waitForFunction(
  () => {
    const btn = [...document.querySelectorAll("button")].find((b) =>
      /consult oracle/i.test(b.innerText || "")
    );
    if (!btn) return false;
    const r = btn.getBoundingClientRect();
    const top = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
    return !!top && (top === btn || btn.contains(top));
  },
  null, // <- `arg`. Passing the options object here instead is why this timed out at the
  // 30s default while claiming to allow 180s: waitForFunction is (fn, arg, options).
  { timeout: 180000, polling: 500 }
);
console.log(`   entry point clickable after ${((Date.now() - t0) / 1000).toFixed(1)}s`);
await sleep(1200);

console.log("== 1. the cockpit ==");
console.log("   title:", await page.title());
await sleep(1200);
await shot("01_cockpit");

console.log("== 2. describe the idea ==");
const box = page.getByPlaceholder(/describe what you want to build/i).first();
await box.waitFor({ timeout: 30000 });
// focus() + keyboard, not click() + type(). Under screen capture the click was intercepted
// intermittently -- a take died here after the encoder was already running, which costs a
// whole recording to discover. focus() does not depend on the element being unobstructed at
// the moment of the click, and keyboard.type still produces the character-by-character
// typing that makes the video look like a person rather than a paste.
for (let attempt = 1; attempt <= 3; attempt++) {
  try {
    await box.focus({ timeout: 10000 });
    break;
  } catch (e) {
    console.log(`   focus attempt ${attempt} failed: ${String(e).slice(0, 80)}`);
    if (attempt === 3) throw e;
    await sleep(1500);
  }
}
await page.keyboard.type(IDEA, { delay: 28 });

// VERIFY the text actually landed. focus() can succeed while the keystrokes go somewhere
// else, and the only visible symptom is the CONSULT button staying disabled 30 seconds
// later -- which reads as a dead button rather than an empty field. Assert, then repair.
let landed = await box.inputValue().catch(() => "");
if (!landed.trim()) {
  console.log("   keystrokes did not land; falling back to fill()");
  await box.fill(IDEA);
  landed = await box.inputValue().catch(() => "");
}
console.log(`   idea in the box: ${landed.length} chars`);
if (!landed.trim()) {
  throw new Error("could not enter the idea text -- aborting before the take is wasted");
}
await sleep(600);
await shot("02_idea");

console.log("== 3. consult the oracle ==");
await waitUnobstructed(page, "before consult");
const consult = page.getByRole("button", { name: /consult oracle/i }).first();
await consult.click({ timeout: 60000 });
console.log("   waiting for the oracle to answer...");

// The oracle call goes to a real model; wait for the discovery view rather than a fixed delay.
let asked = 0;
let sawQuestion = false;
for (let i = 0; i < 90; i++) {
  await sleep(2000);
  const t = await visibleText();
  if (/Q\s*\d+\s*\/\s*\d+/.test(t) || /I've identified this as/i.test(t)) {
    sawQuestion = true;
    break;
  }
}
console.log("   discovery reached:", sawQuestion);
await shot("03_discovery");
if (!sawQuestion) {
  console.log("   NOTE: never reached the guided interview; text was:");
  console.log((await visibleText()).split("\n").slice(0, 25).map((l) => "     " + l).join("\n"));
  await browser.close();
  process.exit(1);
}

console.log("== 4. answer until it stops asking ==");
for (const answer of ANSWERS) {
  const input = page
    .locator("textarea, input[type=text]")
    .filter({ hasNot: page.locator("[disabled]") })
    .last();
  // focus(), not click() -- same reason as the idea box above: under screen capture a
  // transient overlay intercepted the click and killed a take that was already recording.
  await waitUnobstructed(page, "before answer");
  await input.focus({ timeout: 15000 }).catch(async () => {
    await input.click({ force: true, timeout: 10000 }).catch(() => {});
  });
  await page.keyboard.type(answer, { delay: 18 });
  await sleep(400);
  await page.keyboard.press("Enter");
  asked += 1;

  // Wait for the Oracle to respond before typing the next answer.
  await sleep(3500);
  const t = await visibleText();
  const m = t.match(/Q\s*(\d+)\s*\/\s*(\d+)/);
  const missing = t.match(/Still needed for a verifiable build:\s*([^\n]+)/);
  console.log(
    `   answered ${asked}: ${m ? `now at ${m[0]}` : "(no counter)"}` +
      (missing ? ` | still needs: ${missing[1].slice(0, 60)}` : "")
  );
  await shot(`04_q${asked}`);

  if (/Generating your specification|I have enough now/i.test(t)) {
    console.log(`   >>> the interview ended after ${asked} answers`);
    break;
  }
}

console.log("== 5. the spec ==");
for (let i = 0; i < 60; i++) {
  await sleep(2000);
  const t = await visibleText();
  if (/##\s|Goal|Constraints|Files/i.test(t) && /spec/i.test(t)) break;
}
await shot("05_spec");

console.log("\n== console errors:", errors.length, "==");
errors.slice(0, 8).forEach((e) => console.log("   ! " + e));
console.log("answers given before the spec was written:", asked, "(old hard cap: 4)");
// Tell the frame grabber to stop. A signal file rather than a port or a pid: both processes
// already share a filesystem, and neither needs to know anything else about the other.
fs.writeFileSync("C:/tmp/frames_done.flag", String(Date.now()));
await browser.close();
