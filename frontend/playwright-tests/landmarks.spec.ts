import { expect, test } from "@playwright/test";

/**
 * The shell must have document structure, not just accessible controls.
 *
 * WHY THIS EXISTS
 * shell.spec.ts already asserts that every interactive control has an accessible name and a
 * 24px target, and it passes -- accessibility was plainly cared about here. But nothing
 * asserted the PAGE had structure, and on 2026-08-02 driving the running desktop app over
 * CDP found it rendered ZERO landmarks: no <nav>, no <main>, no <h1>. A screen-reader user
 * had no way to reach the navigation, skip to content, or learn what the document was.
 *
 * A control-level check cannot catch a document-level absence. This is the document-level
 * check.
 *
 * Only nav / main / h1 are required. header and aside are optional for a workbench with no
 * page banner, and demanding them would make this fail on something correct -- a test that
 * cries wolf gets skipped, which is how the real gap survived.
 */
test.describe("document structure", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/", { waitUntil: "domcontentloaded" });
    // In a BROWSER the Tauri backend is absent, so the app renders its Setup Wizard first
    // and the shell mounts behind it. Waiting for the rail rather than a fixed delay is the
    // difference between testing the shell and testing whatever happened to be on screen at
    // 1500ms -- which is how the first version of this file failed against a correct app.
    await page.locator("nav, [role='navigation']").first().waitFor({ timeout: 20000 });
  });

  test("the primary navigation is inside a landmark", async ({ page }) => {
    const nav = page.locator("nav, [role='navigation']");
    await expect(nav).toHaveCount(1);
    // and it is the rail, not some other list of links
    await expect(nav.first()).toContainText(/WORK/i);
  });

  test("the content region is a main landmark", async ({ page }) => {
    await expect(page.locator("main, [role='main']")).toHaveCount(1);
  });

  test("the shell contributes a heading naming the document", async ({ page }) => {
    // Deliberately NOT "exactly one h1". The Setup Wizard is a separate view with its own
    // legitimate heading, and it renders in browser mode where no Tauri backend answers.
    // Asserting a global count would fail on correct behaviour; what matters is that the
    // shell itself names the document.
    await expect(page.locator("h1.sr-only")).toHaveCount(1);
    await expect(page.locator("h1.sr-only")).toHaveText(/determinex/i);
  });

  test("the main landmark does not disturb the layout", async ({ page }) => {
    /**
     * The wrapper uses `display: contents` precisely so the flex row lays its children out
     * exactly as before. If someone later replaces it with a normal block, the rail and the
     * content stop being siblings in the flex context and the whole shell reflows -- so
     * assert the computed style rather than trusting the class name to survive.
     */
    const display = await page
      .locator("main")
      .first()
      .evaluate((el) => getComputedStyle(el).display);
    expect(display).toBe("contents");
  });

  test("the shell heading is available to screen readers but not visible", async ({ page }) => {
    const h1 = page.locator("h1.sr-only");
    await expect(h1).toHaveText(/determinex/i); // present in the accessibility tree
    const box = await h1.boundingBox();
    // sr-only collapses the box to ~1px; a visible h1 here would push the whole shell down.
    expect(box === null || box.height <= 2).toBeTruthy();
  });
});
