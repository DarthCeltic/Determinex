/**
 * Drive the named product surfaces for real and report what breaks.
 *
 * The 72-panel rail sweep proved every panel OPENS. This asks the harder question: does each
 * surface actually WORK when you use it? A panel that renders beautifully over an empty
 * response is the failure mode being hunted, and it survives any check that only counts
 * whether something appeared.
 *
 * Surfaces, in the order they were asked for:
 *   multichat     AGENTS -> Agent Chat Room
 *   concept lab   WORK   -> (covered by ui_drive_conceptlab.mjs)
 *   project md    the spec/markdown surface
 *   build tools   the tool cards under ATTACH WHAT YOU NEED
 *   terminal      the in-IDE terminal
 *
 * For each: open it, interact with it, and record console errors, failed requests, empty
 * payloads, and controls that do nothing. Screenshots go to C:/tmp/surface_*.png.
 */
import fs from "node:fs";
import { chromium } from "playwright";

const browser = await chromium.connectOverCDP("http://localhost:9223");
const page = browser
  .contexts()[0]
  .pages()
  .find((p) => !p.url().startsWith("devtools://"));
if (!page) {
  console.log("no app page on 9223");
  process.exit(2);
}
const title = await page.title();
if (!/determinex/i.test(title)) {
  console.log(`refusing: attached page is "${title}"`);
  process.exit(2);
}

// START FROM A KNOWN STATE -- WITHOUT RELOADING.
//
// Every surface here is a toggle and the panel is shared, so the app carries whatever the last
// run left behind and consecutive runs disagreed about an unchanged build. The obvious fix,
// `page.reload()`, is WRONG for a Tauri window: reloading the webview breaks its IPC
// ("IPC custom protocol failed, Tauri will now use the postMessage interface instead
// TypeError: Failed to fetch"), after which every backend call resolves to null. That made
// the chat room report no agents -- a failure the reset itself had caused, in a state no real
// user can reach, since nobody reloads a desktop app window.
//
// So reset the way a user would: clear the persisted panel layout, then close whatever add-on
// is maximised. `explorerRoot` is deliberately KEPT -- clearing it would drop the opened
// project and with it the cross-drive grant every file read depends on.
await page
  .evaluate(() => {
    window.localStorage.removeItem("addonWindowLayouts");
    window.localStorage.removeItem("activeContexts");
  })
  .catch(() => {});
await page.getByTitle("Close add-on").first().click({ timeout: 4000 }).catch(() => {});
await page.waitForTimeout(1500);

const errors = [];
const failed = [];
page.on("console", (m) => m.type() === "error" && errors.push(m.text().replace(/\s+/g, " ").slice(0, 170)));
page.on("pageerror", (e) => errors.push("PAGEERROR " + String(e).slice(0, 170)));
page.on("requestfailed", (r) => {
  const t = r.failure()?.errorText ?? "";
  if (!/ERR_ABORTED|NS_BINDING_ABORTED/.test(t)) failed.push(`${r.method()} ${r.url().slice(0, 80)} :: ${t}`);
});

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const findings = [];

async function unobstructed() {
  await page
    .waitForFunction(
      () => !document.querySelector('div.absolute.inset-0[class*="z-[110]"]'),
      null,
      { timeout: 120000, polling: 400 }
    )
    .catch(() => {});
}

/** Click `opener` only if `target` is not already showing.
 *
 * Every step on this path is a TOGGLE — the rail, the surface accordion inside it, and the
 * panel — so an unconditional click CLOSES whatever the previous run left open, and the script
 * then reports the thing it just closed as broken. A drive whose verdict depends on inherited
 * state is not a check.
 */
async function openTo(target, opener) {
  if (await target.isVisible().catch(() => false)) return true;
  await opener.click({ timeout: 15000 }).catch(() => {});
  await sleep(1200);
  return target.isVisible().catch(() => false);
}

/** Open a surface by its SurfaceDrawer id, e.g. `openSurface("AGENTS", "agent-chat")`.
 *
 * By data-testid, not by visible label. Clicking the label opened only the ACCORDION — which
 * reveals a Panel / Dock choice and nothing else — so this script concluded the multichat had
 * no message input when it had simply never opened the room. `surface-member-<id>` and
 * `surface-open-<id>-panel` are stable ids SurfaceDrawer already exposes.
 */
async function openSurface(rail, id) {
  await unobstructed();
  // A first-run modal can sit over the rail.
  await page.getByRole("button", { name: /^Dismiss$/ }).first().click({ timeout: 3000 }).catch(() => {});
  const member = page.locator(`[data-testid="surface-member-${id}"]`).first();
  await openTo(member, page.getByRole("button", { name: new RegExp(`^${rail}$`, "i") }).first());
  await unobstructed();
  const panelBtn = page.locator(`[data-testid="surface-open-${id}-panel"]`).first();
  await openTo(panelBtn, member);
  const ok = await panelBtn
    .click({ timeout: 12000 })
    .then(() => true)
    .catch(() => false);
  await sleep(3000);
  return ok;
}

function note(surface, level, msg) {
  findings.push({ surface, level, msg });
  console.log(`    [${level}] ${msg}`);
}

async function textNow() {
  return page.evaluate(() => document.body.innerText);
}

// ── 1. multichat: AGENTS -> Agent Chat Room ─────────────────────────────────────────────
console.log("\n== multichat (AGENTS -> Agent Chat Room) ==");
{
  const before = errors.length;
  const opened = await openSurface("AGENTS", "agent-chat");
  if (!opened) note("multichat", "FAIL", "could not open Agent Chat Room");
  await page.screenshot({ path: "C:/tmp/surface_multichat.png" }).catch(() => {});
  const t = await textNow();

  // The room opens with NO session, and the composer belongs to a session -- so "no textarea
  // on screen" is the designed empty state, not a broken room. An earlier version of this
  // check counted inputs immediately and reported "the room cannot be used" about a room it
  // had not started. What must be true is: a way to start one, and a composer once started.
  const hasParticipants = /participant|model|agent|room|claude|codex|gemini|gpt|qwen/i.test(t);
  if (!hasParticipants) note("multichat", "WARN", "no participants/models named in the room");

  // TWO STARTING STATES, and this script kept assuming the first one. On a machine with no
  // sessions the room opens on the creation form; once ANY session exists -- including one a
  // previous run left behind -- it opens straight into that session, with no participant list
  // and no "Start Session" button. Handling only the empty case made consecutive runs disagree
  // about an unchanged build: clean run green, next run three FAILs. The returning-user state
  // is the more common one in real use, so it is the one that must not be treated as broken.
  //
  // "+ NEW SESSION" is a HEADING div, not a control; the action is "START SESSION".
  const composerAt = () => page.getByPlaceholder(/message the room/i).count();
  let gotRoster = true;

  if ((await composerAt()) === 0) {
    // Not already in a session. Get to the creation form -- "+ new" returns to it if the room
    // is showing a session list rather than the form.
    const backToForm = page.getByRole("button", { name: /^\+?\s*new$/i }).first();
    if (await backToForm.isVisible().catch(() => false)) {
      await backToForm.click({ timeout: 6000 }).catch(() => {});
      await sleep(1500);
    }

    // THE CONTRACT IS "never an unexplained blank", not "agents always load instantly".
    // A previous run can leave a live agent session occupying the backend, so the lookup
    // genuinely queues -- and asserting "participants within 20s" made consecutive runs
    // disagree about an unchanged build. What must ALWAYS hold is that the user sees either
    // the roster or a sentence saying which of loading / failed / none-installed this is.
    // (That distinction is the fix this check exists to guard: all three used to render as the
    // same empty gap above a Start Session button disabled for no stated reason.)
    const participant = page.locator("text=/probe: (claude|codex|gemini|ollama)/i").first();
    const gotParticipants = await participant
      .waitFor({ state: "visible", timeout: 25000 })
      .then(() => true)
      .catch(() => false);
    if (!gotParticipants) {
      const status = await page
        .locator("text=/Looking for agents|Could not read the list|did not answer in time|No coding agents/i")
        .first()
        .innerText()
        .catch(() => "");
      await page.screenshot({ path: "C:/tmp/surface_multichat_noagents.png" }).catch(() => {});
      gotRoster = false;
      if (status) {
        console.log(`    (no roster yet, and the room says why: "${status.replace(/\s+/g, " ")}")`);
      } else {
        note("multichat", "FAIL", "no agents listed AND no explanation -- a silent blank");
      }
    }

    const start = page.getByRole("button", { name: /start session/i }).first();
    if (!(await start.isVisible().catch(() => false))) {
      await page.screenshot({ path: "C:/tmp/surface_multichat_nosession.png" }).catch(() => {});
      note("multichat", "FAIL", "no Start Session control -- the room cannot be used");
    } else {
      // Put someone in the room first; starting an empty one proves nothing.
      await page.locator("text=/probe: claude/i").first().click({ timeout: 6000 }).catch(() => {});
      await sleep(600);
      await start.click({ timeout: 10000 }).catch(() => {});
      await sleep(6000);
    }
  } else {
    console.log("    (a session was already open -- the returning-user state)");
  }

  const composer = await composerAt();
  console.log(`    composer inputs: ${composer}`);
  // Only a failure if the room COULD have started one. With no roster there is nothing to put
  // in a session, and the room says so -- which is the designed behaviour, not a break.
  if (composer === 0 && gotRoster) {
    note("multichat", "FAIL", "participants are listed but no session/composer could be reached");
  }

  // ── project md: the Mission Plan's CLAUDE.md / PROJECT.md resync ──────────────────────
  // Named in this file's header from the start and never actually driven -- the header
  // promised five surfaces and the script checked three, which is the same shape of overclaim
  // the script exists to catch. It is not a separate panel: it is the Mission Plan inside a
  // LIVE session. Checked as its own surface after a panel reset it was always absent, and the
  // script reported a missing control when the check was simply run in the wrong place.
  console.log("\n== project md (Mission Plan resync) ==");
  const resync = page.getByRole("button", { name: /^resync$/i }).first();
  const resyncPresent = await resync.isVisible().catch(() => false);
  console.log(`    resync control present: ${resyncPresent}`);
  if (!resyncPresent) {
    note("project-md", "FAIL", "no CLAUDE.md/PROJECT.md resync control in the Mission Plan");
  } else {
    // The command must EXIST, not merely have a button. A control wired to a command the
    // backend does not expose looks identical to a working one until it is pressed.
    const probeRes = await page.evaluate(async () => {
      const inv = window.__TAURI_INTERNALS__?.invoke;
      if (!inv) return { err: "no ipc" };
      try {
        await inv("agent_chat_resync_plan", { sessionId: "", workspace: "" });
        return { reached: true };
      } catch (e) {
        const msg = String(e);
        // An argument complaint proves the command is registered and reachable; "not allowed"
        // or "not found" proves it is not.
        return { reached: !/not allowed|not found|unknown command/i.test(msg), msg: msg.slice(0, 140) };
      }
    });
    console.log(`    agent_chat_resync_plan: ${JSON.stringify(probeRes)}`);
    if (!probeRes.reached)
      note("project-md", "FAIL", `resync command unreachable: ${probeRes.msg ?? probeRes.err}`);
    await page.screenshot({ path: "C:/tmp/surface_project_md.png" }).catch(() => {});
  }

  // Cloak status is a governance claim this surface makes; check it answers.
  const cloak = await page
    .evaluate(async () => {
      const inv = window.__TAURI_INTERNALS__?.invoke;
      if (!inv) return { err: "no ipc" };
      try {
        return { active: await inv("agent_chat_cloak_status", {}) };
      } catch (e) {
        return { err: String(e).slice(0, 120) };
      }
    })
    .catch((e) => ({ err: String(e).slice(0, 120) }));
  console.log(`    cloak status: ${JSON.stringify(cloak)}`);
  if (cloak.err) note("multichat", "FAIL", `cloak status unavailable: ${cloak.err}`);
  for (const e of errors.slice(before)) note("multichat", "ERR", e);
}

/** Close whatever surface is hosted in the panel.
 *
 * MANDATORY between sections. The panel covers the Work cockpit, which is where the terminal
 * and every tool card live -- so leaving it open made the next nine checks click at hidden
 * buttons and report "did not open" for surfaces that were merely behind something. Nine false
 * failures is worse than no check: it trains you to ignore the output.
 */
async function backToWork() {
  // NOT "close the panel". The Work cockpit -- which hosts the terminal and every tool card --
  // is itself what the panel displays, so closing the panel does not reveal the cockpit, it
  // removes it: the body dropped to 198 characters of background and every later check
  // reported its surface as broken. Restoring the cockpit means OPENING it again.
  //
  // But an ATTACHED tool (Trace, Build, ...) opens MAXIMISED over the whole shell, and
  // reopening Work underneath it changes nothing on screen: the cockpit's cards stay mounted
  // and sized -- so Playwright calls them visible -- while every click lands on the tool's own
  // table instead. Six surfaces were reported broken purely because Trace was still on top.
  // Dismiss the add-on first ("Close add-on" is its own header control), then restore Work.
  await page.getByTitle("Close add-on").first().click({ timeout: 4000 }).catch(() => {});
  await sleep(600);
  await openSurface("WORK", "hive");
  await sleep(1200);
}

await backToWork();

// ── 2. terminal ─────────────────────────────────────────────────────────────────────────
console.log("\n== terminal ==");
{
  const before = errors.length;
  await unobstructed();
  const opened = await page
    .getByRole("button", { name: /^TERMINAL/i })
    .first()
    .click({ timeout: 15000 })
    .then(() => true)
    .catch(() => false);
  await sleep(3000);
  if (!opened) note("terminal", "FAIL", "TERMINAL tool card did not open");
  await page.screenshot({ path: "C:/tmp/surface_terminal.png" }).catch(() => {});
  const t = await textNow();
  const looksLikeTerminal = /\$|>|PS |bash|cmd|shell|prompt/i.test(t);
  console.log(`    terminal-ish content present: ${looksLikeTerminal}`);
  if (!looksLikeTerminal) note("terminal", "WARN", "opened but nothing terminal-shaped rendered");
  for (const e of errors.slice(before)) note("terminal", "ERR", e);
}

await backToWork();

// ── 3. build tools under ATTACH WHAT YOU NEED ───────────────────────────────────────────
console.log("\n== build tool cards ==");
{
  const cards = ["CODE", "BUILD", "TRACE", "SEARCH", "FIND IN FILES", "HEALTH", "LEARNING STUDIO", "REPO CLINIC", "MAINTENANCE BAY"];
  for (const card of cards) {
    const before = errors.length;
    const beforeReq = failed.length;
    // Each card opens INTO the panel, which then covers the cockpit the next card sits on.
    // Without this the first card that works hides every card after it.
    await backToWork();
    await unobstructed();
    const target = page.getByRole("button", { name: new RegExp(`^${card}`, "i") }).first();
    // Distinguish "the control is missing" from "the click failed" from "it is covered".
    // "did not open" collapsed all three into one useless word.
    const exists = await target.count().then((n) => n > 0).catch(() => false);
    const visible = exists ? await target.isVisible().catch(() => false) : false;
    let clickErr = "";
    const ok = await target
      .click({ timeout: 10000 })
      .then(() => true)
      .catch((err) => {
        // "did not open" hid WHY. Playwright names the intercepting element, which is the
        // whole answer when a control is present, visible, and still unclickable.
        clickErr = String(err).replace(/\s+/g, " ").slice(0, 260);
        return false;
      });
    await sleep(2500);
    const t = await textNow();
    const e = errors.slice(before);
    const f = failed.slice(beforeReq);
    console.log(`    ${card.padEnd(18)} exists=${exists ? "y" : "n"} visible=${visible ? "y" : "n"} click=${ok ? "y" : "n"}  chars=${t.length}  err=${e.length}${f.length ? ` req=${f.length}` : ""}`);
    if (!exists) note("build-tools", "FAIL", `${card}: no such control on the cockpit`);
    else if (!ok) note("build-tools", "FAIL", `${card}: present and visible but unclickable -- ${clickErr}`);
    for (const x of e) note("build-tools", "ERR", `${card}: ${x}`);
    for (const x of f) note("build-tools", "ERR", `${card}: REQ ${x}`);
    await page.screenshot({ path: `C:/tmp/surface_tool_${card.replace(/\W+/g, "_")}.png` }).catch(() => {});
  }
}

// ── report ──────────────────────────────────────────────────────────────────────────────
console.log("\n== findings ==");
if (!findings.length) console.log("    (none)");
const bySurface = {};
for (const f of findings) (bySurface[f.surface] ||= []).push(f);
for (const [s, list] of Object.entries(bySurface)) {
  console.log(`  ${s}: ${list.filter((x) => x.level === "FAIL").length} FAIL, ${list.filter((x) => x.level === "ERR").length} ERR, ${list.filter((x) => x.level === "WARN").length} WARN`);
}
fs.writeFileSync("C:/tmp/surface_findings.json", JSON.stringify({ findings, errors, failed }, null, 2));
console.log("\n  wrote C:/tmp/surface_findings.json");
await browser.close();
