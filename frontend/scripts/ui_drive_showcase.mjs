/**
 * THE UNIFIED SHOWCASE — one continuous, real run through the whole product.
 *
 * Ryan: *"I want a unified video, one that does the whole showcase"*, *"we need a full real
 * actual rerun that is actually legit and runs correctly and tapes correctly"*, and *"I want
 * it to see all of the different AIs working in tandem on something."*
 *
 * So: one script, one pass, no stitching of segments recorded at different times. Everything
 * shown is the live app answering for itself — the setup report is a real probe of this
 * machine, the oracle preview is real synthesis, the chat room hosts the real installed CLIs.
 * Nothing here types into a mock.
 *
 * Run it alongside `ui_record_frames.mjs`, which screenshots the PAGE over CDP rather than
 * grabbing a screen region — a window-title grab once recorded 120 seconds of somebody else's
 * chat window while reporting success at every step.
 *
 * THINGS LEARNED THE HARD WAY, ALL LOAD-BEARING HERE:
 *   - never `page.reload()` a Tauri window: it breaks the webview's IPC and every backend call
 *     then resolves to null, which looks exactly like a broken product
 *   - every rail / accordion / panel is a TOGGLE, so open conditionally or you close things
 *   - surface labels open an ACCORDION, not the panel; use the data-testids
 *   - an attached tool opens MAXIMISED over the cockpit; dismiss it before moving on
 *   - the bottom status bar must stay in frame — Ryan has had it cut off more than once
 */
import fs from "node:fs";
import { chromium } from "playwright";

const CDP = process.env.DETERMINEX_CDP ?? "http://localhost:9223";
const DONE = process.env.DX_DONE ?? "C:/tmp/frames_done.flag";
const IDEA =
  process.env.DX_IDEA ??
  "a command line tool that takes a CSV file and prints the average of a chosen column";

const browser = await chromium.connectOverCDP(CDP);
const page = browser
  .contexts()
  .flatMap((c) => c.pages())
  .find((p) => !p.url().startsWith("devtools://"));
if (!page) {
  console.log("no app page on " + CDP);
  process.exit(2);
}
const title = await page.title();
if (!/determinex/i.test(title)) {
  console.log(`refusing to drive: attached page is "${title}"`);
  process.exit(2);
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const beat = (ms = 2200) => sleep(ms); // a pause long enough to READ, this is a video
const step = (n, what) => console.log(`\n[${n}] ${what}`);

async function unobstructed() {
  await page
    .waitForFunction(
      () => !document.querySelector('div.absolute.inset-0[class*="z-[110]"]'),
      null,
      { timeout: 180000, polling: 400 }
    )
    .catch(() => {});
}

async function openTo(target, opener) {
  if (await target.isVisible().catch(() => false)) return true;
  await opener.click({ timeout: 15000 }).catch(() => {});
  await sleep(1000);
  return target.isVisible().catch(() => false);
}

async function openSurface(rail, id) {
  await unobstructed();
  await page.getByRole("button", { name: /^Dismiss$/ }).first().click({ timeout: 3000 }).catch(() => {});
  const member = page.locator(`[data-testid="surface-member-${id}"]`).first();
  await openTo(member, page.getByRole("button", { name: new RegExp(`^${rail}$`, "i") }).first());
  await unobstructed();
  const panelBtn = page.locator(`[data-testid="surface-open-${id}-panel"]`).first();
  await openTo(panelBtn, member);
  await panelBtn.click({ timeout: 12000 }).catch(() => {});
  await sleep(2500);
}

/** Dismiss a maximised attached tool so the next surface is actually reachable. */
async function dropAddon() {
  await page.getByTitle("Close add-on").first().click({ timeout: 4000 }).catch(() => {});
  await sleep(800);
}

// ── The bottom of the frame is part of the frame ────────────────────────────────────────
// The status bar carries "Oracle Ready", the workspace and the router state -- it is evidence,
// not chrome, and it is the first thing lost when a capture is sized wrong.
const geom = await page.evaluate(() => ({
  inner: [window.innerWidth, window.innerHeight],
  statusBarBottom: (() => {
    const el = [...document.querySelectorAll("*")].find((e) =>
      /Oracle Ready/i.test(e.textContent || "") && e.children.length < 8
    );
    return el ? Math.round(el.getBoundingClientRect().bottom) : null;
  })(),
}));
console.log(`viewport ${geom.inner.join("x")}  status bar bottom: ${geom.statusBarBottom}`);
if (geom.statusBarBottom !== null && geom.statusBarBottom > geom.inner[1]) {
  console.log("  WARNING: the status bar sits below the viewport -- the bottom would be cut");
}

try {
  // ── 1. What already works on this machine ──────────────────────────────────────────────
  step(1, "the answer to 'which button do I press' — a real probe of this machine");
  const report = await page.evaluate(async () => {
    const env = await window.__TAURI_INTERNALS__.invoke("provider_setup_report");
    return env?.data ?? env;
  });
  console.log(`    "${report?.headline}"`);
  for (const o of (report?.options ?? []).filter((o) => o.group === "start_here")) {
    console.log(`      ${o.title.padEnd(24)} ${o.readiness.padEnd(24)} ${o.action_label}`);
  }
  await beat(2500);

  // ── 1b. The projects it is pointed at ──────────────────────────────────────────────────
  // Worth showing for its own sake, and because it is where the cross-drive fix is visible:
  // one codebase on C: and one on T:. Until today a project on any drive but the system one
  // was refused outright ("outside workspace boundary 'C:\'") and the explorer came up empty.
  step("1b", "the projects it is pointed at — including one on another drive");
  await dropAddon();
  await openSurface("WORK", "hub");
  const codebases = await page.evaluate(() =>
    [...document.querySelectorAll("*")]
      .filter((e) => e.children.length === 0 && /^[A-Z]:[\\/]/.test((e.textContent || "").trim()))
      .map((e) => e.textContent.trim())
      .filter((v, i, a) => a.indexOf(v) === i)
  );
  for (const c of codebases) console.log(`      ${c}`);
  await beat(4000);

  // Bind the workspace to the real repository, so everything after this shows LIVE git rather
  // than the honest-but-empty "could not read this repository" of a non-repo scratch folder.
  //
  // By the card's own data-testid. Two earlier attempts clicked a path-shaped text node INSIDE
  // the card -- an inert div, six levels below the button that carries the handler -- so the
  // click landed on nothing, and the script then reported a binding it had never established.
  // SELECTING the card is what binds (`handleProjectSelect` -> `setExplorerRoot`); the card's
  // own Work button only navigates, so selecting is the step that matters.
  await page
    .locator('[data-testid="project-hub-card-determinex"]')
    .first()
    .click({ timeout: 8000 })
    .catch(() => {});
  await sleep(3500);
  const boundRoot = await page.evaluate(() => window.localStorage.getItem("explorerRoot"));
  console.log(`      workspace bound to: ${boundRoot}`);
  if (!/Dev[\\/]Determinex$/i.test(String(boundRoot))) {
    console.log("      WARNING: the card click did not bind — git would read empty on camera");
  }
  await beat(3000);

  // ── 2. The Work cockpit: an idea, in plain language ────────────────────────────────────
  step(2, "describe what to build, in a sentence");
  // Whatever a previous run left MAXIMISED sits over the cockpit, and the idea box then stays
  // mounted but unreachable -- the failure reads as "the box is missing" when it is covered.
  await dropAddon();
  await openSurface("WORK", "hive");

  // Report what was OBSERVED, and read it from the COCKPIT, which is the thing whose workspace
  // actually matters. An earlier version printed "bound to the repo" after matching a branch
  // name that was already on the Project Hub card before the click, then after matching the
  // first path-shaped string on a page where the Hub itself was still open -- twice asserting a
  // state change it had never established, which is the exact defect this session has spent the
  // night removing from the product.
  const activeWorkspace = await page.evaluate(() => {
    // The cockpit's own WORKSPACE tile, found by its label and read from the tile itself --
    // not "the first path-shaped string on the page", which matched the Project Hub card.
    const label = [...document.querySelectorAll("*")].find(
      (e) => e.children.length === 0 && /^WORKSPACE$/i.test((e.textContent || "").trim())
    );
    const tile = label?.closest("div")?.parentElement;
    return (tile?.innerText || "(unreadable)").replace(/\s+/g, " ").trim();
  });
  console.log(`      cockpit workspace: ${activeWorkspace.replace(/\s+/g, " ").slice(0, 70)}`);

  const box = page.getByPlaceholder(/describe what you want to build/i).first();
  await box.waitFor({ state: "visible", timeout: 60000 });
  await box.click();
  await box.fill("");
  // Typed, not pasted -- the video should look like a person using it.
  for (const ch of IDEA) {
    await page.keyboard.type(ch);
    await sleep(18);
  }
  await beat(2000);

  // ── 3. The oracle is synthesized BEFORE any code is written ────────────────────────────
  step(3, "the oracle first — checks the answer must pass, derived from the idea");
  const oracle = await page.evaluate(async (idea) => {
    try {
      // `ideaText`, not a payload object -- the command takes `idea_text: String`, and Tauri
      // camel-cases it. The backend said so plainly rather than returning an empty oracle,
      // which is the difference between a bug you fix in a minute and one you ship.
      const env = await window.__TAURI_INTERNALS__.invoke("preview_idea_oracle", {
        ideaText: idea,
      });
      return env?.data ?? env;
    } catch (e) {
      return { error: String(e).slice(0, 200) };
    }
  }, IDEA);
  // The response is `{status, payload:{n_checks, oracle_sound, oracle_tests, note}}`.
  const o = oracle?.payload ?? oracle ?? {};
  console.log(`    ${o.n_checks ?? 0} ground-truth checks; sound=${o.oracle_sound}`);
  if (o.note) console.log(`    "${o.note}"`);
  // AND SAY WHEN IT IS NOT ENOUGH. A one-line idea yields a VACUOUS oracle -- one that only
  // checks the symbol exists -- and the synthesizer marks it as such rather than quietly
  // presenting a trivial oracle as ground truth. That refusal IS the thesis ("an oracle never
  // silently passes"), and it is what the Concept Lab's interview exists to resolve, so the
  // showcase states it instead of cropping it out.
  if (String(o.oracle_tests ?? "").includes("DETERMINEX_VACUOUS_ORACLE")) {
    console.log(
      "    the synthesizer marked this oracle VACUOUS — one sentence is not enough to pin down"
    );
    console.log(
      "    behaviour, and it says so rather than pretending. That is what the interview fixes."
    );
  }
  if (oracle?.error) console.log(`      (oracle preview said: ${oracle.error})`);
  await beat(3500);

  // ── 3b. The refusal, then the verified solve ───────────────────────────────────────────
  // This is the entire thesis in two calls, and the ORDER is the point. First the system is
  // asked to build from the one-line idea: it comes back solved=false with "that cannot verify
  // behaviour. Add one concrete input/output example and re-run" -- it will not claim a result
  // it cannot check. Then the same idea WITH examples produces a sound oracle and a program
  // that passes it, generated locally by the 1.5B model with no network.
  step("3b", "it refuses to claim a result it cannot verify");
  const vague = await page.evaluate(async (idea) => {
    try {
      const env = await window.__TAURI_INTERNALS__.invoke("build_idea", {
        ideaText: idea,
        optIn: true,
        modelId: "determinex-engineer-v11-dsl",
      });
      return env?.payload ?? env;
    } catch (e) {
      return { error: String(e).slice(0, 200) };
    }
  }, IDEA);
  console.log(`    solved=${vague?.solved}  checks=${vague?.n_checks}`);
  console.log(`    "${String(vague?.proof ?? vague?.error ?? "").slice(0, 220)}"`);
  await beat(4000);

  step("3c", "the same idea with one concrete example — now it can be checked");
  const EXAMPLES =
    "solution(numbers) returns the average of a list of numbers. For example " +
    "solution([1, 2, 3]) returns 2.0, solution([10]) returns 10.0, and solution([]) returns 0.0.";
  const built = await page.evaluate(async (idea) => {
    try {
      const env = await window.__TAURI_INTERNALS__.invoke("build_idea", {
        ideaText: idea,
        optIn: true,
        modelId: "determinex-engineer-v11-dsl",
      });
      return env?.payload ?? env;
    } catch (e) {
      return { error: String(e).slice(0, 200) };
    }
  }, EXAMPLES);
  console.log(`    solved=${built?.solved}  checks=${built?.n_checks}  samples=${built?.samples}`);
  console.log(`    "${String(built?.proof ?? built?.error ?? "").slice(0, 220)}"`);
  for (const line of String(built?.program ?? "").split("\n").slice(0, 8)) {
    console.log(`      ${line}`);
  }
  await beat(5000);

  // ── 4. Several AIs in one room, on the same task ───────────────────────────────────────
  step(4, "the AIs working in tandem — one room, one plan, oracle-checked between turns");
  await dropAddon();
  await openSurface("AGENTS", "agent-chat");

  const roster = await page.evaluate(async () => {
    const r = await window.__TAURI_INTERNALS__.invoke("list_coding_agents");
    return (Array.isArray(r) ? r : []).map((a) => ({
      name: a.name,
      installed: a.installed,
      models: (a.models ?? []).map((m) => `${m.tier}:${m.model}`),
    }));
  });
  for (const a of roster) {
    console.log(
      `      ${String(a.name).padEnd(14)} installed=${String(a.installed).padEnd(5)} ${a.models.join("  ") || "(free text)"}`
    );
  }
  await beat(2500);

  // START THE ROOM. Ryan: "I want to see all of the different AIs working in tandem on
  // something" -- a roster on screen is not that. A real session with several participants is,
  // and it is what makes the Mission Plan and the turn-taking visible at all.
  const composerCount = () => page.getByPlaceholder(/message the room/i).count();
  if ((await composerCount()) === 0) {
    const backToForm = page.getByRole("button", { name: /^\+?\s*new$/i }).first();
    if (await backToForm.isVisible().catch(() => false)) {
      await backToForm.click({ timeout: 6000 }).catch(() => {});
      await sleep(1200);
    }
    await page
      .locator("text=/probe: (claude|codex|gemini|ollama)/i")
      .first()
      .waitFor({ state: "visible", timeout: 45000 })
      .catch(() => {});
    // Three of them, so "in tandem" is literally what is on screen.
    for (const who of ["probe: claude", "probe: codex", "probe: ollama"]) {
      await page.locator(`text=/${who}/i`).first().click({ timeout: 6000 }).catch(() => {});
      await sleep(700);
    }
    await beat(2000);
    await page
      .getByRole("button", { name: /start session/i })
      .first()
      .click({ timeout: 10000 })
      .catch(() => {});
    await sleep(6000);
  }
  console.log(`      composer present: ${(await composerCount()) > 0}`);
  await beat(2500);

  // Show the model choice being made in the shared vocabulary, on camera.
  const picker = page.locator("select").first();
  if (await picker.isVisible().catch(() => false)) {
    const opts = await picker.locator("option").allInnerTexts().catch(() => []);
    console.log(`      model choices on screen: ${opts.join(" | ")}`);
    await picker.selectOption({ index: Math.min(2, Math.max(0, opts.length - 2)) }).catch(() => {});
    await beat(1800);
  }

  // ── 5. The Mission Plan every participant reads ────────────────────────────────────────
  step(5, "one Mission Plan, read by every participant, synced from the repo's own docs");
  const resync = page.getByRole("button", { name: /^resync$/i }).first();
  if (await resync.isVisible().catch(() => false)) {
    console.log("      resync available (pulls CLAUDE.md / PROJECT.md into the plan)");
    await beat(1800);
  } else {
    console.log("      (no live session yet — the plan appears once a session is running)");
  }

  // ── 6. Proof: the compiler/test verdict, not the model's opinion ───────────────────────
  step(6, "proof — the compiler and test run decide, never the model");
  await dropAddon();
  await openSurface("PROVE", "proof");
  await beat(3500);

  // ── 7. It is a real IDE around all of it ───────────────────────────────────────────────
  step(7, "a real workbench around it: terminal, files, health");
  await dropAddon();
  await openSurface("WORK", "hive");
  for (const card of ["TERMINAL", "HEALTH"]) {
    await unobstructed();
    await page
      .getByRole("button", { name: new RegExp(`^${card}`, "i") })
      .first()
      .click({ timeout: 10000 })
      .catch(() => {});
    await beat(3000);
    await dropAddon();
    await openSurface("WORK", "hive");
  }

  step(8, "back to where a new user starts");
  await beat(2500);
} finally {
  fs.writeFileSync(DONE, "done");
  console.log("\nsignalled the recorder to stop");
  await browser.close();
}
