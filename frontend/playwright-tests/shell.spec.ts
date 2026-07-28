import { test, expect, type Page } from "@playwright/test";

/**
 * Shell smoke specs.
 *
 * There were already two suites here (network_policy, lane_c_rendered_qa), but
 * nothing covering the shell itself -- so every check of boot, the rail and
 * panel navigation was manual and screenshot-driven. Two of the defects found by
 * hand this week were exactly the kind a three-line spec catches for free and
 * forever:
 *
 *   * the rail silently clipped its last three entries (`overflow-y-auto` plus
 *     `no-scrollbar`, so there was no scrollbar to reveal that Review and Merge
 *     were unreachable);
 *   * the boot splash could hang forever behind a fake progress bar.
 *
 * These run against `next dev` in browser mode, so the Tauri IPC layer is
 * absent. That is a real limit and worth stating plainly: these specs cover
 * mount, layout, navigation and clipping -- NOT backend behaviour. The IPC
 * contracts are covered by commandContract/argContract and the vitest suites.
 */

const RAIL_GROUPS = [
  "work",
  "code",
  "source",
  "run",
  "prove",
  "agents",
  "trust",
  "learn",
  "system",
] as const;

/**
 * Get past the two blocking first-run modals.
 *
 * Both are correct behaviour on a fresh profile (setup wizard, then the
 * workspace onboarding sheet), and both are `fixed inset-0 z-50`, so nothing
 * behind them is clickable until they are dealt with.
 */
async function bootToShell(page: Page) {
  await page.addInitScript(() => {
    localStorage.setItem("determinex.setupCompleted", "true");
    localStorage.setItem("determinex.networkPolicy", "local-only");
    // Pin the workspace root and its onboarding-dismissal key together, so the
    // first-run sheet does not appear at all and this does not depend on the
    // in-app default path. The dismissal branch below stays as a fallback.
    localStorage.setItem("explorerRoot", "C:/tmp/determinex-e2e-ws");
    localStorage.setItem("workspaceOnboardingDismissed:C:/tmp/determinex-e2e-ws", "1");
  });
  await page.goto("/", { waitUntil: "domcontentloaded" });

  // The rail is the first thing that proves the shell mounted at all.
  await expect(page.getByTestId("rail-group-work")).toBeVisible({ timeout: 30_000 });

  // The workspace-onboarding sheet mounts with `loading: true`, rendering a
  // full-bleed spinner BEFORE it renders its Dismiss button, and it can mount a
  // beat after the rail does. Two earlier attempts at this helper failed on
  // that: one checked "is Dismiss visible?" once and raced the spinner, the
  // other waited for "no fixed z>=40 element" and never settled, because the
  // addon dock is legitimately a fixed z-40 surface. So target the sheet
  // itself and wait for the specific thing.
  const sheet = page.getByTestId("workspace-onboarding");
  await sheet.waitFor({ state: "visible", timeout: 10_000 }).catch(() => {
    // Already dismissed for this profile, or the workspace scan never proposed
    // anything -- either way there is nothing to clear.
  });
  if (await sheet.isVisible().catch(() => false)) {
    const dismiss = page.getByRole("button", { name: "Dismiss", exact: true }).first();
    await dismiss.waitFor({ state: "visible", timeout: 20_000 });
    await dismiss.click();
    await sheet.waitFor({ state: "detached", timeout: 10_000 });
  }
}

test.describe("shell", () => {
  test("boots to an interactive shell rather than hanging on the splash", async ({ page }) => {
    const errors: string[] = [];
    page.on("pageerror", (e) => errors.push(e.message));

    await bootToShell(page);

    // The splash used to be able to hang forever behind a fake progress bar, so
    // "no splash still on screen" is the actual assertion.
    await expect(page.getByText(/Initializing|Booting|Starting up/i).first()).toBeHidden();
    expect(errors, `uncaught page errors: ${errors.join(" | ")}`).toEqual([]);
  });

  test("all nine rail groups are present and none is clipped out of view", async ({ page }) => {
    await bootToShell(page);

    const viewport = page.viewportSize()!;
    for (const id of RAIL_GROUPS) {
      const el = page.getByTestId(`rail-group-${id}`);
      await expect(el, `rail group "${id}" must be visible`).toBeVisible();
      const box = (await el.boundingBox())!;
      // The regression this pins: the rail scrolled internally with the
      // scrollbar hidden, so entries below the fold existed in the DOM and were
      // visible to a query while being unreachable to a user.
      expect(
        box.y + box.height,
        `rail group "${id}" is below the viewport fold (y=${box.y})`
      ).toBeLessThanOrEqual(viewport.height);
      expect(box.y, `rail group "${id}" is above the viewport`).toBeGreaterThanOrEqual(0);
    }
  });

  test("every rail group opens a drawer that names its surfaces", async ({ page }) => {
    await bootToShell(page);

    for (const id of RAIL_GROUPS) {
      const rail = page.getByTestId(`rail-group-${id}`);
      await rail.click();
      const drawer = page.getByTestId("surface-drawer");
      await expect(drawer, `group "${id}" must open the drawer`).toBeVisible();
      await expect(rail).toHaveAttribute("aria-expanded", "true");

      // A group with no reachable members would be a dead rail entry -- which is
      // the whole class of "a list of things that do nothing" this rail replaced.
      const members = drawer.getByTestId(/^surface-member-/);
      expect(await members.count(), `group "${id}" has no members`).toBeGreaterThan(0);

      await rail.click(); // toggle closed
      await expect(drawer).toBeHidden();
    }
  });

  test("a surface opened into the panel is not clipped by its container", async ({ page }) => {
    await bootToShell(page);

    await page.getByTestId("rail-group-agents").click();
    const member = page.getByTestId("surface-member-agent-chat");
    await expect(member).toBeVisible();
    await member.click(); // expand to reveal the destination buttons

    const toPanel = page.getByTestId("surface-open-agent-chat-panel");
    await expect(toPanel).toBeVisible();
    await toPanel.click();

    // The reported symptom: "the multiagent popout drawer is still super wierd"
    // -- Agent Chat Room's own text cut off mid-sentence because a wide panel was
    // placed in a narrow container that hid the overflow instead of adapting.
    // Any element wider than its own scrollport, with the overflow hidden, is
    // content the user simply cannot read.
    const clipped = await page.evaluate(() => {
      const out: { cls: string; clientW: number; scrollW: number; text: string }[] = [];
      for (const el of document.querySelectorAll("*")) {
        const s = getComputedStyle(el);
        if (s.overflowX !== "hidden" && s.overflowX !== "clip") continue;
        if (el.scrollWidth <= el.clientWidth + 4) continue;
        if (el.clientWidth < 120) continue;
        out.push({
          cls: (el.className || "").toString().slice(0, 60),
          clientW: el.clientWidth,
          scrollW: el.scrollWidth,
          text: (el.textContent || "").trim().slice(0, 60),
        });
      }
      return out;
    });
    expect(
      clipped,
      `content is clipped with no way to reach it:\n${JSON.stringify(clipped, null, 2)}`
    ).toEqual([]);
  });

  test("the page never scrolls horizontally at any supported width", async ({ page }) => {
    await bootToShell(page);
    for (const width of [1280, 1440, 1920]) {
      await page.setViewportSize({ width, height: 900 });
      await page.waitForTimeout(400);
      const overflow = await page.evaluate(
        () => document.documentElement.scrollWidth - document.documentElement.clientWidth
      );
      expect(
        overflow,
        `body scrolls horizontally by ${overflow}px at ${width}px wide`
      ).toBeLessThanOrEqual(0);
    }
  });
});

test.describe("keyboard", () => {
  test("Ctrl+1..9 opens each rail group and Escape closes the drawer", async ({ page }) => {
    await bootToShell(page);
    const drawer = page.getByTestId("surface-drawer");

    // Every group must be reachable from the keyboard. Before this, only 1/2/3
    // were bound, and they went to three left-hand workspaces rather than to the
    // rail -- a leftover from before the nine-group rail existed.
    for (let i = 0; i < RAIL_GROUPS.length; i++) {
      await page.keyboard.press(`Control+${i + 1}`);
      await expect(drawer, `Ctrl+${i + 1} must open a drawer`).toBeVisible();
      await expect(page.getByTestId(`rail-group-${RAIL_GROUPS[i]}`)).toHaveAttribute(
        "aria-expanded",
        "true"
      );
      await page.keyboard.press("Escape");
      await expect(drawer, "Escape must close the drawer").toBeHidden();
    }
  });

  test("the command palette shortcut is visible, not just bound", async ({ page }) => {
    await bootToShell(page);
    // The palette existed with its shortcut recorded only in a code comment, so
    // the fastest path through the app was undiscoverable.
    const hint = page.getByRole("button", { name: "Open the command palette" });
    await expect(hint).toBeVisible();
    await expect(hint).toContainText("Ctrl+K");
  });

  test("every interactive control has an accessible name and a 24px target", async ({ page }) => {
    await bootToShell(page);
    const bad = await page.evaluate(() => {
      const noName: string[] = [];
      const small: string[] = [];
      for (const el of document.querySelectorAll("button,[role=button]")) {
        const r = el.getBoundingClientRect();
        if (!r.width || !r.height) continue;
        const name = (el.getAttribute("aria-label") || el.textContent || "").trim();
        const id = el.getAttribute("data-testid") || el.getAttribute("title") || "(unlabelled)";
        // A `title` is a tooltip, not an accessible name.
        if (!name) noName.push(id);
        if (r.height < 24 || r.width < 24)
          small.push(`${id} ${Math.round(r.width)}x${Math.round(r.height)}`);
      }
      return { noName, small };
    });
    expect(bad.noName, "buttons with no accessible name").toEqual([]);
    expect(bad.small, "targets under WCAG 2.2 AA's 24px floor").toEqual([]);
  });
});

test.describe("panel arrangement", () => {
  test("the cockpit split is draggable and the ratio persists", async ({ page }) => {
    await bootToShell(page);

    const handle = page.getByTestId("cockpit-split-resize");
    await expect(handle, "the cockpit split needs a real handle").toBeVisible();

    const before = await page.evaluate(
      () =>
        getComputedStyle(
          document.querySelector('[data-testid="cockpit-split-resize"]')!.parentElement!
        ).gridTemplateColumns
    );

    const box = (await handle.boundingBox())!;
    const vp = page.viewportSize()!;
    // Grab a point on the handle that is actually ON SCREEN. The handle spans the
    // full column height (~892px), so `box.y + box.height / 2` lands below a
    // 720px viewport and the drag silently never happens -- which is exactly how
    // this spec first "failed" against a feature that worked.
    const grabX = box.x + box.width / 2;
    const grabY = Math.min(box.y + 80, vp.height - 60);
    await page.mouse.move(grabX, grabY);
    await page.mouse.down();
    await page.mouse.move(grabX - 140, grabY, { steps: 10 });
    await page.mouse.up();

    const after = await page.evaluate(
      () =>
        getComputedStyle(
          document.querySelector('[data-testid="cockpit-split-resize"]')!.parentElement!
        ).gridTemplateColumns
    );
    expect(after, "dragging must change the split").not.toEqual(before);

    // Persisted, so it is still there next launch -- the point of the feature.
    const stored = await page.evaluate(() =>
      localStorage.getItem("determinex.splitRatio.workCockpit")
    );
    expect(Number(stored)).toBeGreaterThan(0);
    expect(Number(stored)).toBeLessThan(1);
  });

  test("a named layout round-trips through the UI", async ({ page }) => {
    await bootToShell(page);

    await page.getByTestId("layout-menu-toggle").click();
    await expect(page.getByTestId("layout-menu")).toBeVisible();
    await page.getByTestId("layout-save-current").click();
    await page.getByLabel("Layout name").fill("e2e-arrangement");
    await page.getByRole("button", { name: "Save", exact: true }).click();

    await expect(page.getByTestId("layout-restore-e2e-arrangement")).toBeVisible();
    const saved = await page.evaluate(() =>
      JSON.parse(localStorage.getItem("determinex.panelLayouts") || "[]")
    );
    expect(saved.map((l: { name: string }) => l.name)).toContain("e2e-arrangement");

    // Restoring must actually apply, not just close the menu.
    await page.getByTestId("layout-restore-e2e-arrangement").click();
    await expect(page.getByText(/Restored "e2e-arrangement"/)).toBeVisible();
  });
});
