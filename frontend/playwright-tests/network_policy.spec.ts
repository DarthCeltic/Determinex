import { test, expect } from "@playwright/test";

test.describe("Network policy", () => {
  test("loads the persisted user network policy into the IDE snapshot", async ({ page }) => {
    await page.addInitScript(() => {
      window.localStorage.setItem("determinex.networkPolicy", "offline");
      window.localStorage.setItem("determinex.setupCompleted", "true");
    });

    await page.goto("http://127.0.0.1:3000", {
      waitUntil: "networkidle",
      timeout: 30_000,
    });

    await page.waitForFunction(() => typeof (window as any).__DETERMINEX_UI_SNAPSHOT__ === "function");
    await page.waitForFunction(() => (window as any).__DETERMINEX_UI_SNAPSHOT__?.().networkPolicy === "offline");

    const snapshot = await page.evaluate(() => (window as any).__DETERMINEX_UI_SNAPSHOT__?.());
    expect(snapshot?.app).toBe("Determinex");
    expect(snapshot?.networkPolicy).toBe("offline");
  });

  test("rail Cloak control toggles local-only into cloaked mode", async ({ page }) => {
    await page.addInitScript(() => {
      window.localStorage.setItem("determinex.networkPolicy", "offline");
      window.localStorage.setItem("determinex.setupCompleted", "true");
    });

    await page.goto("http://127.0.0.1:3000", {
      waitUntil: "networkidle",
      timeout: 30_000,
    });

    const toggle = page.getByTestId("rail-cloak-policy-toggle");
    await expect(toggle).toBeVisible();
    await expect(toggle).toContainText("Local");

    await toggle.click();

    await page.waitForFunction(() => window.localStorage.getItem("determinex.networkPolicy") === "cloaked");
    await page.waitForFunction(() => (window as any).__DETERMINEX_UI_SNAPSHOT__?.().activeAddon === "cloak");

    const snapshot = await page.evaluate(() => (window as any).__DETERMINEX_UI_SNAPSHOT__?.());
    expect(snapshot?.networkPolicy).toBe("cloaked");
    expect(snapshot?.activeAddon).toBe("cloak");
    await expect(toggle).toContainText("Cloak");
  });

  test("interactive guide states the Cloak boundary without absolute leakage claims", async ({ page }) => {
    await page.addInitScript(() => {
      window.localStorage.setItem("determinex.setupCompleted", "true");
    });

    await page.goto("http://127.0.0.1:3000", {
      waitUntil: "networkidle",
      timeout: 30_000,
    });

    await page.getByTitle("Open Guide").first().click();
    const guide = page.getByTestId("guide-window");
    await expect(guide).toBeVisible();

    const text = await guide.innerText();
    expect(text).toContain("Local models keep code on your machine");
    expect(text).not.toMatch(/Zero leakage|source code never leaves|cloud AI blind|fully obfuscated/);
  });
});
