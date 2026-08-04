/**
 * ui_reset_safe.mjs — reset the app WITHOUT navigating.
 *
 * `ui_reset.mjs` does `page.goto("http://localhost:3000/")`, which is a reload in all but
 * name, and trap 1 of the Tauri drive rules is: never reload a Tauri window — it breaks the
 * webview IPC (`IPC custom protocol failed … Failed to fetch`) and every backend call then
 * resolves to null, which reads as a broken product in a state no real user can reach.
 *
 * So this resets the way the rules say to: dismiss whatever is painting over the workbench,
 * clear the two layout keys, keep `explorerRoot` (or the opened project is dropped), drop
 * any viewport override a narrow run left behind, and put the workbench back on Work/hive.
 *
 * Two things it deliberately does NOT do:
 *   - probe `window.__TAURI__`. `withGlobalTauri` is unset in tauri.conf.json, so that global
 *     is absent by design and the app imports `invoke` from the bundled npm module. A probe
 *     for it reports NO_TAURI_GLOBAL on a perfectly healthy bridge — a check that cannot
 *     pass is not a check.
 *   - assume a click landed. `settings-modal` sits at z-50 across `inset-0`, so a rail click
 *     underneath it is swallowed; the drawer then has zero members and the next run reports
 *     the group empty. Dismissal is verified, not fired and forgotten.
 *
 *   node scripts/ui_reset_safe.mjs
 */
import { chromium } from "playwright";

const CDP = process.env.DTX_CDP || "http://localhost:9223";
const browser = await chromium.connectOverCDP(CDP);
const page = browser.contexts()[0].pages().find((p) => p.url().includes("localhost:3000"));
if (!page) {
  console.log("FAIL: no localhost:3000 page on the CDP endpoint");
  process.exit(1);
}

/** Anything painting over the workbench: the maximised add-on, or a modal at inset-0. */
export async function clearOverlays(p) {
  for (let i = 0; i < 5; i++) {
    let acted = false;

    const x = p.getByTitle("Close add-on");
    if (await x.count().catch(() => 0)) {
      await x.first().click({ timeout: 2000 }).catch(() => {});
      acted = true;
      await p.waitForTimeout(250);
    }

    // The modal is a sibling of the workbench, not a child, so it never shows up as new
    // content in a container diff and it swallows every click aimed at the rail.
    const open = await p
      .evaluate(() => {
        const m = document.querySelector('[data-testid="settings-modal"]');
        return !!(m && m.getBoundingClientRect().width > 100);
      })
      .catch(() => false);
    if (open) {
      const close = p.getByRole("button", { name: /close config/i });
      if (await close.count().catch(() => 0)) {
        await close.first().click({ timeout: 2000 }).catch(() => {});
      } else {
        await p.keyboard.press("Escape").catch(() => {});
      }
      acted = true;
      await p.waitForTimeout(350);
    }

    if (!acted) return true;
  }
  return false;
}

// 1. Drop any device-metrics override a narrow run (960) left pinned on the window.
const cdp = await page.context().newCDPSession(page);
await cdp.send("Emulation.clearDeviceMetricsOverride").catch(() => {});
await page.waitForTimeout(300);

// 2. Uncover the workbench.
const clean = await clearOverlays(page);

// 3. Clear only the layout state. explorerRoot survives.
const cleared = await page.evaluate(() => {
  const drop = Object.keys(localStorage).filter((k) =>
    /addonWindowLayouts|activeContexts/i.test(k)
  );
  drop.forEach((k) => localStorage.removeItem(k));
  return { dropped: drop, keptRoot: localStorage.getItem("explorerRoot") ? "yes" : "none" };
});

// 4. Put the workbench back on Work/hive — closing the panel drops the body to ~198 chars
//    of background, so "no panel" is not a neutral starting state.
const rail = page.locator('[data-testid="rail-group-work"]');
if (await rail.count()) {
  await rail.first().click({ timeout: 3000 }).catch(() => {});
  await page.waitForTimeout(600);
  const m = page.locator('[data-testid="surface-member-hive"]');
  if (await m.count()) {
    await m.first().click({ timeout: 3000 }).catch(() => {});
    await page.waitForTimeout(400);
    const pnl = page.locator('[data-testid="surface-open-hive-panel"]');
    if (await pnl.count()) await pnl.first().click({ timeout: 3000 }).catch(() => {});
  }
}
await page.waitForTimeout(1500);

const out = await page.evaluate(() => ({
  vp: `${window.innerWidth}x${window.innerHeight}`,
  chars: (document.body.innerText || "").length,
  modal: !!document.querySelector('[data-testid="settings-modal"]'),
  members: document.querySelectorAll("[data-testid^='surface-member-']").length,
  head: (document.body.innerText || "").slice(0, 90).replace(/\n/g, " / "),
}));
await page.screenshot({ path: "C:/tmp/ui_reset_safe.png" });
console.log(`overlays cleared: ${clean}`);
console.log(`localStorage:     ${JSON.stringify(cleared)}`);
console.log(`viewport:         ${out.vp}`);
console.log(`modal present:    ${out.modal}`);
console.log(`body:             ${out.chars} chars  (a closed panel is ~198)`);
console.log(`head:             ${out.head}`);
console.log(`shot:             C:/tmp/ui_reset_safe.png`);
await browser.close();
