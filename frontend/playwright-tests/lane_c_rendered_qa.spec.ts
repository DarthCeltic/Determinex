/**
 * Lane C Rendered QA — Playwright screenshot test
 *
 * Proves the Determinex IDE UI renders correctly in browser mode.
 * Expected: panel is visible with "Native Runtime Required" overlay or Lane C panel.
 * Screenshot saved to assurance/evidence/first_gui_hive_ipc/playwright_screenshot.png.
 */

import * as path from "path";
import * as fs from "fs";
import * as crypto from "crypto";
import { test, expect } from "@playwright/test";

const EVIDENCE_DIR = path.resolve(__dirname, "../../assurance/evidence/first_gui_hive_ipc");
const SCREENSHOT_PATH = path.join(EVIDENCE_DIR, "playwright_screenshot.png");

test.describe("Lane C — Rendered UI QA", () => {
  test("dev server responds at port 3000", async ({ page }) => {
    const response = await page.goto("http://127.0.0.1:3000", {
      waitUntil: "domcontentloaded",
      timeout: 30_000,
    });
    expect(response?.status()).toBe(200);
  });

  test("Lane C panel or native-runtime overlay is visible", async ({ page }) => {
    await page.goto("http://127.0.0.1:3000", { waitUntil: "domcontentloaded", timeout: 30_000 });
    // domcontentloaded fires before React hydration completes, and this dev server's HMR
    // websocket means "networkidle" never resolves (Playwright's own docs discourage it for
    // exactly this reason) -- wait for the real post-hydration marker instead (same one
    // playwright-tests/network_policy.spec.ts gates on).
    await page.waitForFunction(
      () => typeof (window as any).__DETERMINEX_UI_SNAPSHOT__ === "function"
    );

    // Either the panel itself or the native-runtime required overlay must be present.
    // `.isVisible()` is a single immediate check with no retry -- it fires the instant it's
    // called, before React has necessarily painted this specific element, and returns false
    // rather than waiting. Measured: the overlay text is reliably present by ~1s post-hydration,
    // but a bare .isVisible() called right after the hydration marker resolves can still lose
    // that race. expect(...).toBeVisible() polls up to its own timeout instead of sampling once.
    const panelLocator = page.locator('[data-testid="first-gui-hive-ipc-panel"]');
    const overlayLocator = page.getByText(/native runtime required/i);

    const panelVisible = await expect(panelLocator)
      .toBeVisible({ timeout: 8_000 })
      .then(() => true)
      .catch(() => false);

    const overlayVisible = panelVisible
      ? false
      : await expect(overlayLocator)
          .toBeVisible({ timeout: 8_000 })
          .then(() => true)
          .catch(() => false);

    // At least one must be true — UI is rendered
    expect(panelVisible || overlayVisible, "Neither panel nor native-runtime overlay found").toBe(
      true
    );
  });

  test("screenshot captured and written to evidence dir", async ({ page }) => {
    await page.goto("http://127.0.0.1:3000", { waitUntil: "domcontentloaded", timeout: 30_000 });
    await page.waitForFunction(
      () => typeof (window as any).__DETERMINEX_UI_SNAPSHOT__ === "function"
    );

    // Scroll to show Lane C panel if it exists
    const panel = page.locator('[data-testid="first-gui-hive-ipc-panel"]');
    const panelCount = await panel.count();
    if (panelCount > 0) {
      await panel.scrollIntoViewIfNeeded().catch(() => {});
    }

    fs.mkdirSync(EVIDENCE_DIR, { recursive: true });
    const screenshotBytes = await page.screenshot({ fullPage: true });
    fs.writeFileSync(SCREENSHOT_PATH, screenshotBytes);

    const sha256 = crypto.createHash("sha256").update(screenshotBytes).digest("hex");
    const hashPath = path.join(EVIDENCE_DIR, "playwright_screenshot_sha256.txt");
    fs.writeFileSync(hashPath, sha256 + "\n");

    // Verify file was written
    expect(fs.existsSync(SCREENSHOT_PATH)).toBe(true);
    expect(screenshotBytes.length).toBeGreaterThan(1000);

    console.log(
      `Screenshot: ${SCREENSHOT_PATH} (${screenshotBytes.length} bytes, sha256=${sha256})`
    );
  });
});
