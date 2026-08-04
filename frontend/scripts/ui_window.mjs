/**
 * ui_window.mjs — resize the REAL Tauri window, not an emulation override.
 *
 * The map runs at two widths, and the narrow one is where the collisions live. Doing that
 * with `page.setViewportSize` sets a device-metrics override that outlives the run: the next
 * "native" sweep silently inherits 960 and its screenshots are not what a user sees. It also
 * cannot be undone reliably from a CDP-attached page — clearing the override left innerWidth
 * unchanged because the window itself had been left at 958.
 *
 * Resizing the window through `Browser.setWindowBounds` moves the actual window, so what the
 * screenshot shows is what the app looks like at that size, and the state is visible in the
 * window rather than hidden in an override.
 *
 *   node scripts/ui_window.mjs 1600 1000
 *   node scripts/ui_window.mjs 960 1000
 */
import { chromium } from "playwright";

const W = Number(process.argv[2] || 1600);
const H = Number(process.argv[3] || 1000);

const browser = await chromium.connectOverCDP(process.env.DTX_CDP || "http://localhost:9223");
const page = browser.contexts()[0].pages().find((p) => p.url().includes("localhost:3000"));
const cdp = await page.context().newCDPSession(page);

// A pinned emulation override would win over the real window size, so drop it first.
await cdp.send("Emulation.clearDeviceMetricsOverride").catch(() => {});

const { windowId } = await cdp.send("Browser.getWindowForTarget");
await cdp.send("Browser.setWindowBounds", {
  windowId,
  bounds: { windowState: "normal", width: W, height: H },
});
await page.waitForTimeout(900);

const got = await page.evaluate(() => `${innerWidth}x${innerHeight}`);
console.log(`window -> ${W}x${H}   viewport now ${got}`);
await browser.close();
