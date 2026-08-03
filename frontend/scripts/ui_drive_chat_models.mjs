/**
 * The multichat model picker, driven in the desktop app.
 *
 * Ryan, 2026-08-03: *"the multichat and the services need to have an easy way to figure out
 * usage and changing between their different models -- claude has three, google like 4, open
 * ai a few, we need to make sure it all is easy to understand and easy to use."*
 *
 * What this must NOT find is what was there before: a free-text box whose placeholder read
 * "e.g. gemini-2.5-pro", so switching model required already knowing the exact string.
 */
import { chromium } from "playwright";

const CDP = process.env.DETERMINEX_CDP ?? "http://localhost:9223";
const OUT = process.env.DX_OUT || "C:/tmp/chatmodels";
const fail = [];
const note = (ok, what, detail = "") => {
  console.log(`${ok ? "  PASS" : "  FAIL"}  ${what}${detail ? ` — ${detail}` : ""}`);
  if (!ok) fail.push(what);
};

const browser = await chromium.connectOverCDP(CDP);
const page = browser
  .contexts()
  .flatMap((c) => c.pages())
  .find((p) => !p.url().startsWith("devtools://"));
if (!page) {
  console.log("no app page on " + CDP);
  process.exit(1);
}

console.log("[1] the registry is the one place that knows which models an agent takes");
const agents = await page.evaluate(async () => {
  const inv = window.__TAURI_INTERNALS__?.invoke;
  if (!inv) return null;
  try {
    return await inv("list_coding_agents");
  } catch (e) {
    return { error: String(e) };
  }
});
note(Array.isArray(agents), "list_coding_agents reachable", agents?.error ?? "");
if (Array.isArray(agents)) {
  for (const a of agents) {
    const tiers = (a.models ?? []).map((m) => m.tier).join("/");
    console.log(
      `      ${String(a.name).padEnd(14)} supportsModel=${String(a.supportsModel ?? a.supports_model).padEnd(5)} ${tiers || "(free text)"}`
    );
  }
  const withShortlist = agents.filter((a) => (a.models ?? []).length > 0);
  note(withShortlist.length >= 3, "the cloud CLIs all carry a shortlist", `${withShortlist.length}`);

  // The same three words for every provider, so the vocabulary is learned once.
  for (const a of withShortlist) {
    const tiers = a.models.map((m) => m.tier);
    note(
      JSON.stringify(tiers) === JSON.stringify(["fast", "balanced", "deep"]),
      `${a.name} uses the shared vocabulary`,
      tiers.join(",")
    );
    // A label that is just the model string is the memory test wearing a dropdown.
    const raw = a.models.filter((m) => m.label === m.model);
    note(raw.length === 0, `${a.name} labels are human, not raw ids`, raw.map((m) => m.model).join(","));
  }

  // `gemini --model gemini/gemini-3-pro-preview` fails: those prefixes are for LiteLLM
  // routing, not for the CLI's own flag. Conflating the two would break the picker for the
  // one vendor whose setup story is already the hardest.
  const prefixed = agents.flatMap((a) => (a.models ?? []).filter((m) => m.model.includes("/")));
  note(prefixed.length === 0, "no LiteLLM routing prefix leaked into a CLI model string",
    prefixed.map((m) => m.model).join(","));
}

console.log("\n[2] the picker as the user meets it");
// Agents rail -> Agent Chat Room. Found by listing the app's own clickables rather than
// guessing a "CHAT" dock button, which is what an earlier version of this script did -- and it
// then reported the picker missing when it had simply never opened the panel.
// A first-run modal ("Workspace Detected") sits over the rail; dismiss it if present.
await page.locator("button", { hasText: /^Dismiss$/ }).first().click({ timeout: 4000 }).catch(() => {});
await page.waitForTimeout(500);

/** Click `opener` only if `target` is not already showing.
 *
 * EVERY step on this path is a TOGGLE, at three nested levels: the Agents rail, the "Agent
 * Chat Room" accordion inside it, and the panel itself. An unconditional click therefore
 * CLOSES whatever a previous run left open, and the script then reports the thing it just
 * closed as missing -- which happened at each level in turn while writing this. A drive script
 * whose result depends on the state it inherited is not a check.
 */
const openTo = async (target, opener, label) => {
  if (await target.isVisible().catch(() => false)) return;
  await opener.click({ timeout: 15000 });
  await page.waitForTimeout(1200);
  await target.waitFor({ state: "visible", timeout: 15000 }).catch(() => {
    throw new Error(`${label} did not appear after opening`);
  });
};

// By data-testid, not by visible text. SurfaceDrawer already exposes stable ids
// (`surface-member-<id>`, `surface-open-<id>-panel`); matching on the rendered label instead
// meant fighting uppercase-by-CSS and icon-plus-text nodes, and every miss looked like a
// missing feature rather than a missing selector.
const chatEntry = page.locator('[data-testid="surface-member-agent-chat"]').first();
await openTo(chatEntry, page.locator("button", { hasText: /^Agents$/ }).first(), "Agents rail");

// "Agent Chat Room" is an ACCORDION, not the panel. Expanding it reveals Panel / Dock, and
// only those open the room -- an earlier version of this script stopped at the accordion and
// concluded the multichat had no inputs at all, when it had simply never been opened.
const panelBtn = page.locator('[data-testid="surface-open-agent-chat-panel"]').first();
await openTo(panelBtn, chatEntry, "Panel / Dock choice");
await panelBtn.click({ timeout: 15000 });
await page.waitForTimeout(3500);

// The picker only renders for a SELECTED agent -- an unselected one is not in the room, so
// choosing its model would mean nothing. Select the cloud CLIs before looking for it.
for (const name of ["claude-code", "codex", "gemini-cli"]) {
  await page
    .locator("button", { hasText: new RegExp(name, "i") })
    .first()
    .click({ timeout: 8000 })
    .catch(() => {});
  await page.waitForTimeout(400);
}
await page.waitForTimeout(1200);

const selects = page.locator("select");
const selectCount = await selects.count();
const optionTexts = [];
for (let i = 0; i < selectCount; i++) {
  optionTexts.push((await selects.nth(i).innerText()).replace(/\s+/g, " ").trim());
}
const tiered = optionTexts.filter((t) => /Haiku|Sonnet|Opus|Mini|Standard|Pro|Flash/i.test(t));
note(
  tiered.length > 0,
  "a tiered model dropdown is rendered",
  `${selectCount} selects, ${tiered.length} tiered`
);
for (const t of tiered) console.log("      " + t.slice(0, 150));

// The wall this replaced: a text box whose placeholder was the answer you had to already know.
const memoryTest = await page
  .locator('input[placeholder*="e.g."]')
  .count()
  .catch(() => 0);
note(memoryTest === 0, "no free-text box with a model name as its placeholder", `${memoryTest}`);

// The escape hatch must survive: a closed list cannot name a model that does not exist yet.
note(
  optionTexts.some((t) => /type a model name/i.test(t)),
  "the free-text escape is still offered"
);

await page.screenshot({ path: `${OUT}.png` });
console.log(`\n${fail.length === 0 ? "ALL PASS" : `${fail.length} FAILED: ${fail.join(", ")}`}`);
await browser.close();
process.exit(fail.length === 0 ? 0 : 1);
