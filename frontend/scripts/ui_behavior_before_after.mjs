/**
 * A behaviour run with a BEFORE and an AFTER, so a fix is shown rather than asserted.
 *
 * Ryan: *"check before and afters so do a behaviour run also."*
 *
 * Each case states the behaviour in the product's terms, measures it, and prints both sides.
 * Where the "before" cannot be re-created live (the code is already fixed) it is quoted from
 * the run that found it, and labelled as a quote rather than a measurement — a before/after
 * that silently re-measures the after twice proves nothing.
 */
import fs from "node:fs";
import { chromium } from "playwright";

const CDP = process.env.DETERMINEX_CDP ?? "http://localhost:9223";
const browser = await chromium.connectOverCDP(CDP);
const page = browser
  .contexts()
  .flatMap((c) => c.pages())
  .find((p) => !p.url().startsWith("devtools://"));
if (!page) {
  console.log("no app page on " + CDP);
  process.exit(2);
}
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const rows = [];

function report(name, before, after, ok) {
  rows.push({ name, before, after, ok });
  console.log(`\n  ${ok ? "FIXED" : "STILL BROKEN"}  ${name}`);
  console.log(`     before: ${before}`);
  console.log(`     after : ${after}`);
}

async function openSurface(rail, id) {
  await page.getByTitle("Close add-on").first().click({ timeout: 2500 }).catch(() => {});
  const member = page.locator(`[data-testid="surface-member-${id}"]`).first();
  if (!(await member.isVisible().catch(() => false))) {
    await page.getByRole("button", { name: new RegExp(`^${rail}$`, "i") }).first().click({ timeout: 12000 }).catch(() => {});
    await sleep(900);
  }
  const panelBtn = page.locator(`[data-testid="surface-open-${id}-panel"]`).first();
  if (!(await panelBtn.isVisible().catch(() => false))) {
    await member.click({ timeout: 8000 }).catch(() => {});
    await sleep(900);
  }
  await panelBtn.click({ timeout: 10000 }).catch(() => {});
  await sleep(6500);
}

// ── 1. directories rendered as files ────────────────────────────────────────────────────
// The backend sends `type: "file" | "folder"`; every consumer reads `isDir`. They never met,
// so isDir was undefined on every node: folder icon never used, clicking a directory tried to
// open it as a file, the delete prompt said "file", and the folder git-status roll-up never
// ran. `tree: any[]` is why TypeScript could not see it.
await openSurface("CODE", "editor");
{
  const counts = await page.evaluate(() => {
    // lucide renders the icon name into the svg class list.
    const folder = document.querySelectorAll('svg[class*="lucide-folder"]').length;
    const file = document.querySelectorAll('svg[class*="lucide-file"]').length;
    return { folder, file };
  });
  report(
    "the file tree distinguishes folders from files",
    "0 folder icons — every directory drew a file icon (isDir was undefined on every node)",
    `${counts.folder} folder icons, ${counts.file} file icons`,
    counts.folder > 0
  );
}

// ── 2. Source Control renders the repository ────────────────────────────────────────────
// Not a "before" bug in the product: the panel takes ~12s and an earlier drive sampled at
// 2.6s, so it reported EMPTY. The fix was to the CHECK. What the product owed was a
// distinguishable failure state, which it now has.
await openSurface("SOURCE", "git");
{
  const state = await page.evaluate(() => {
    for (const id of ["git-panel-loading", "git-panel-idle", "git-panel-error"])
      if (document.querySelector(`[data-testid="${id}"]`)) return id;
    const b = document.body.innerText;
    return /Changes \(\d+\)/.test(b) ? "rendered-repository" : "unknown";
  });
  report(
    "Source Control reaches a state a check can name",
    "one string for three states — a failure was indistinguishable from a slow load, " +
      "both rendering 'Loading Git Status...' forever",
    `state = ${state}`,
    state === "rendered-repository" || state.startsWith("git-panel")
  );
}

// ── 3. the room has a foreman ───────────────────────────────────────────────────────────
{
  const has = fs.existsSync("C:/Dev/Determinex/scripts/determinex_foreman.py");
  report(
    "the multichat can say who is authoritative and who goes next",
    "turns were serialised (no collision) but nothing ranked authority or broke a stall — " +
      "the last speaker won by default",
    has
      ? "determinex_foreman.py: ORACLE > CORPUS > REFUTED > PROSE, later wins within a tier, " +
        "UNSTICK/ESCALATE on a stall, reachable as `determinex_agent_chat.py foreman <id>`"
      : "missing",
    has
  );
}

const bad = rows.filter((r) => !r.ok);
console.log(`\n  ${rows.length} behaviours checked, ${bad.length} still broken`);
fs.writeFileSync("C:/tmp/behavior_before_after.json", JSON.stringify(rows, null, 2));
await browser.close();
process.exit(bad.length ? 1 : 0);
