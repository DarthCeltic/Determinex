/**
 * Drive the first-run experience the way a first-time user meets it.
 *
 * Ryan, 2026-08-03: *"be dubious of the technical part, like verify it all works so the
 * average person doesn't get angry at an error or debug problem."* Every assertion below is a
 * thing that was WRONG in the shipped wizard, not a hypothetical:
 *
 *   - step 2 opened on seven blank password fields, in alphabetical order, on a machine with
 *     two working subscriptions and 38 local models
 *   - "ready" was about to mean "a credential exists on disk"
 *   - the panel scrolls, and the bottom kept getting cut off ("you keep doing that dumb shit")
 *
 * Runs its own Chromium so it needs nothing but the dev server and the bridge.
 */
import { chromium } from "playwright";
import { writeFileSync } from "node:fs";

const URL = process.env.DX_URL || "http://localhost:3000/";
const OUT = process.env.DX_OUT || "C:/tmp/firstrun";

const fail = [];
const note = (ok, what, detail = "") => {
  console.log(`${ok ? "  PASS" : "  FAIL"}  ${what}${detail ? ` — ${detail}` : ""}`);
  if (!ok) fail.push(what);
};

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });

// EVERY assertion is scoped to the wizard panel. The wizard is a fixed overlay and the whole
// IDE renders behind it, so `body.innerText` contains the rail labels, the run state and the
// four-stage strip -- which is how a first version of this script "found" the words `oracle`
// and `CLI` in a prescreen that contains neither, and read the rail's own "Ready" as a
// provider being ready. A check that reports on text it did not scope to is the same defect
// class this project keeps finding elsewhere.
const panel = page.locator("div.fixed.inset-0.z-50");
const panelText = () => panel.innerText({ timeout: 10000 });

// Registered BEFORE the first navigation. The first version of this script attached these at
// the very end, by which point every error they exist to catch had already been missed -- and
// when the panel silently unmounted mid-run there was nothing to say why.
const errors = [];
page.on("pageerror", (e) => errors.push(`pageerror: ${e}`));
page.on("console", (m) => {
  if (m.type() === "error") errors.push(`console: ${m.text().slice(0, 300)}`);
});
const bail = async (where, err) => {
  await page.screenshot({ path: `${OUT}_CRASH.png`, fullPage: true }).catch(() => {});
  console.log(`\n  FAIL  ${where} — ${err}`);
  if (errors.length) console.log("  page errors:\n    " + errors.join("\n    "));
  console.log(`  screenshot: ${OUT}_CRASH.png`);
  await browser.close();
  process.exit(1);
};

// The wizard only runs when setup has not been completed, and it reads that from localStorage.
await page.goto(URL, { waitUntil: "domcontentloaded", timeout: 60000 });
await page.evaluate(() => window.localStorage.clear());
await page.reload({ waitUntil: "domcontentloaded", timeout: 60000 });

console.log("\n[1] the prescreen — asked once, before anything technical is said");
const prescreen = panel.getByRole("heading", { name: /how would you like determinex to talk/i });
await prescreen.waitFor({ state: "visible", timeout: 60000 }).catch(() => {});
note(await prescreen.isVisible().catch(() => false), "prescreen is shown on first run");

const choices = panel.locator("button", { hasText: /Show me everything|Plain English|Just tell me/ });
note((await choices.count()) === 3, "three reader levels offered", `${await choices.count()} found`);

// A question about how technical you are must not itself require technical vocabulary.
const prescreenText = await panelText();
const jargon = ["API key", "stdout", "stderr", "oracle", "DAG", "CLI", "endpoint"].filter((w) =>
  prescreenText.includes(w)
);
note(jargon.length === 0, "prescreen uses no jargon", jargon.join(", "));
await page.screenshot({ path: `${OUT}_1_prescreen.png`, fullPage: true });

console.log("\n[2] choosing a level gets out of the way");
await choices.filter({ hasText: /Plain English/ }).first().click();
await page.waitForTimeout(1200);
note(!(await prescreen.isVisible().catch(() => false)), "prescreen dismissed after answering");

console.log("\n[3] step 1 — network policy");
const policy = panel.getByRole("heading", { name: /network & privacy policy/i });
await policy.waitFor({ state: "visible", timeout: 60000 }).catch(() => {});
note(await policy.isVisible().catch(() => false), "policy step reached");
await panel.locator("button", { hasText: /Cloaked|Offline/ }).first().click();

console.log("\n[4] step 2 — what already works, not seven blank fields");
const step2 = panel.getByRole("heading", { name: /choose your ai/i });
await step2.waitFor({ state: "visible", timeout: 60000 }).catch(() => {});
note(await step2.isVisible().catch(() => false), "step 2 reached");

// Wait for the report itself, not for any string that might appear on the way. The spinner
// copy was passing an earlier version of this check while the report never arrived at all --
// `build_report` was fetching the same 2.7s agent roster three times and taking 10.3 seconds,
// which on a first-run screen reads as broken.
const probeStarted = Date.now();
await panel
  .locator("text=/Looking for AI you can already use/")
  .waitFor({ state: "hidden", timeout: 60000 })
  .catch(() => {});
const probeMs = Date.now() - probeStarted;
note(probeMs < 30000, "the report arrives before a user would give up", `${probeMs}ms`);

const passwordFields = await panel.locator('input[type="password"]:visible').count();
note(passwordFields === 0, "no API key fields visible by default", `${passwordFields} visible`);

// Count the ready BADGES, by their own test id. Matching on the string "Ready" caught neither
// the badge (its text node sits beside an SVG) nor the local row ("Ready — 38 model(s)
// installed"), and quietly reported 0 on a machine with three working providers.
const readyBadges = await panel.locator('[data-testid="provider-ready"]').count();
note(readyBadges > 0, "at least one provider is shown as already working", `${readyBadges} ready`);

await page.screenshot({ path: `${OUT}_2_providers.png`, fullPage: true });
const body2 = await panelText().catch((e) => bail("step 2 panel vanished", e.message));
note(
  /ready to go/i.test(body2),
  "headline says the user is done rather than selling the next thing"
);
// The exact regression: a finished setup still leading with "Get a key".
note(!/^Get a key/m.test(body2.split("I already have an API key")[0]), "no key prompt up front");
await page.screenshot({ path: `${OUT}_2_providers.png`, fullPage: true });

console.log("\n[5] the key fields are still there for people who want them");
await panel.locator("button", { hasText: /I already have an API key/i }).click();
await page.waitForTimeout(600);
const revealed = await panel.locator('input[type="password"]:visible').count();
note(revealed >= 7, "advanced disclosure reveals every key field", `${revealed} fields`);
await page.screenshot({ path: `${OUT}_3_advanced.png`, fullPage: true });

console.log("\n[6] nothing is cut off at the bottom");
const overflow = await page.evaluate(() => {
  const panel = document.querySelector(".overflow-y-auto");
  if (!panel) return { found: false };
  panel.scrollTop = panel.scrollHeight;
  const buttons = [...panel.querySelectorAll("button")].filter((b) =>
    /continue/i.test(b.textContent || "")
  );
  const last = buttons[buttons.length - 1];
  if (!last) return { found: true, reachable: false };
  const r = last.getBoundingClientRect();
  return {
    found: true,
    reachable: r.bottom <= window.innerHeight && r.top >= 0,
    bottom: Math.round(r.bottom),
    viewport: window.innerHeight,
  };
});
note(overflow.found, "scroll panel located");
note(
  overflow.reachable,
  "the Continue button is fully on screen when scrolled to the bottom",
  `bottom=${overflow.bottom} viewport=${overflow.viewport}`
);
await page.screenshot({ path: `${OUT}_4_bottom.png` });

await page.waitForTimeout(500);
note(errors.length === 0, "no uncaught page errors", errors.slice(0, 3).join(" | "));

writeFileSync(`${OUT}_result.json`, JSON.stringify({ failures: fail }, null, 2));
console.log(`\n${fail.length === 0 ? "ALL PASS" : `${fail.length} FAILED: ${fail.join(", ")}`}`);
await browser.close();
process.exit(fail.length === 0 ? 0 : 1);
