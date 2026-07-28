import { test, expect } from "@playwright/test";

test.describe("Network policy", () => {
  test("loads the persisted user network policy into the IDE snapshot", async ({ page }) => {
    await page.addInitScript(() => {
      window.localStorage.setItem("determinex.networkPolicy", "offline");
      window.localStorage.setItem("determinex.setupCompleted", "true");
      // Separate from setupCompleted -- WorkspaceOnboarding gates on its own
      // per-workspace-path key (src/app/page.tsx), else it stacks on top of
      // the Setup Wizard and blocks every click in the suite.
      // Pin the workspace root AND its dismissal key together. Setting only
      // ":default" relied on the show-check falling back to "default" when no
      // root was persisted -- one of two disagreeing key derivations, since
      // unified in lib/workspaceOnboarding.ts. Pinning the root makes this
      // independent of whatever the in-app default path happens to be.
      window.localStorage.setItem("explorerRoot", "C:/tmp/determinex-e2e-ws");
      window.localStorage.setItem("workspaceOnboardingDismissed:C:/tmp/determinex-e2e-ws", "1");
    });

    await page.goto("http://127.0.0.1:3000", {
      waitUntil: "domcontentloaded",
      timeout: 30_000,
    });

    await page.waitForFunction(
      () => typeof (window as any).__DETERMINEX_UI_SNAPSHOT__ === "function"
    );
    await page.waitForFunction(
      () => (window as any).__DETERMINEX_UI_SNAPSHOT__?.().networkPolicy === "offline"
    );

    const snapshot = await page.evaluate(() => (window as any).__DETERMINEX_UI_SNAPSHOT__?.());
    expect(snapshot?.app).toBe("Determinex");
    expect(snapshot?.networkPolicy).toBe("offline");
  });

  test("rail Cloak control toggles local-only into cloaked mode", async ({ page }) => {
    await page.addInitScript(() => {
      window.localStorage.setItem("determinex.networkPolicy", "offline");
      window.localStorage.setItem("determinex.setupCompleted", "true");
      // Separate from setupCompleted -- WorkspaceOnboarding gates on its own
      // per-workspace-path key (src/app/page.tsx), else it stacks on top of
      // the Setup Wizard and blocks every click in the suite.
      // Pin the workspace root AND its dismissal key together. Setting only
      // ":default" relied on the show-check falling back to "default" when no
      // root was persisted -- one of two disagreeing key derivations, since
      // unified in lib/workspaceOnboarding.ts. Pinning the root makes this
      // independent of whatever the in-app default path happens to be.
      window.localStorage.setItem("explorerRoot", "C:/tmp/determinex-e2e-ws");
      window.localStorage.setItem("workspaceOnboardingDismissed:C:/tmp/determinex-e2e-ws", "1");
    });

    await page.goto("http://127.0.0.1:3000", {
      waitUntil: "domcontentloaded",
      timeout: 30_000,
    });

    const toggle = page.getByTestId("rail-cloak-policy-toggle");
    await expect(toggle).toBeVisible();
    await expect(toggle).toContainText("Local");

    await toggle.click();

    await page.waitForFunction(
      () => window.localStorage.getItem("determinex.networkPolicy") === "cloaked"
    );
    await page.waitForFunction(
      () => (window as any).__DETERMINEX_UI_SNAPSHOT__?.().activeAddon === "cloak"
    );

    const snapshot = await page.evaluate(() => (window as any).__DETERMINEX_UI_SNAPSHOT__?.());
    expect(snapshot?.networkPolicy).toBe("cloaked");
    expect(snapshot?.activeAddon).toBe("cloak");
    await expect(toggle).toContainText("Cloak");
  });

  test("interactive guide states the Cloak boundary without absolute leakage claims", async ({
    page,
  }) => {
    await page.addInitScript(() => {
      window.localStorage.setItem("determinex.setupCompleted", "true");
      // Pin the workspace root AND its dismissal key together. Setting only
      // ":default" relied on the show-check falling back to "default" when no
      // root was persisted -- one of two disagreeing key derivations, since
      // unified in lib/workspaceOnboarding.ts. Pinning the root makes this
      // independent of whatever the in-app default path happens to be.
      window.localStorage.setItem("explorerRoot", "C:/tmp/determinex-e2e-ws");
      window.localStorage.setItem("workspaceOnboardingDismissed:C:/tmp/determinex-e2e-ws", "1");
    });

    await page.goto("http://127.0.0.1:3000", {
      waitUntil: "domcontentloaded",
      timeout: 30_000,
    });

    // domcontentloaded fires before React hydration completes -- wait for the same
    // hydration marker the other two tests in this file already gate on, rather than
    // relying on a bare click racing the boot overlay/hydration (the exact silent-dead-UI
    // bug fixed in cf5c6f054e).
    await page.waitForFunction(
      () => typeof (window as any).__DETERMINEX_UI_SNAPSHOT__ === "function"
    );

    await page.getByTitle("Open Guide").first().click();
    const guide = page.getByTestId("guide-window");
    await expect(guide).toBeVisible();

    // The guide is a multi-page tour (16 steps) that doesn't default to the
    // Local/Cloak step -- jump to it explicitly, same pattern as
    // TeacherOverlay.test.tsx's own navigation.
    await guide.getByText("Local vs Cloak").click();

    const text = await guide.innerText();
    // Copy has since been revised (was "Local models keep code on your
    // machine..."); check the current wording's same semantic claim.
    expect(text).toContain("Local keeps prompts, source, and model execution on your machine");
    expect(text).not.toMatch(
      /Zero leakage|source code never leaves|cloud AI blind|fully obfuscated/
    );
  });
});

test.describe("Mission Control layout", () => {
  test("the active-mission card gets its real fr-ratio share of width, not a min-content sliver", async ({
    page,
  }) => {
    // Real bug found live 2026-07-27 driving the actual app, root-caused by measuring
    // getBoundingClientRect() down the ancestor chain: `xl:grid-cols-[1.05fr_0.95fr]` has no
    // minmax(0, ...), so an `Nfr` track floors at its content's max-content width, not 0. The
    // sibling "Next useful action" card's `whitespace-nowrap` command strings (meant to
    // ellipsis-truncate) never got constrained enough to truncate, so their ~1076px intrinsic
    // width became that track's floor -- squeezing THIS card down to ~130px at an ordinary
    // 1600px window regardless of the 1.05fr/0.95fr split. A first attempted fix (@container +
    // @md: on the inner Objective/User-outcome grid) improved the inner wrapping but did NOT
    // fix this -- confirmed by measuring the card was still 130px wide after that change alone.
    // The real fix is min-w-0 on both grid children, restoring proper fr-ratio sizing. This
    // test pins the width ratio directly rather than checking for visual overlap/wrapping,
    // which a later copy change could accidentally make pass even with the bug still present.
    await page.setViewportSize({ width: 1600, height: 1000 });
    await page.addInitScript(() => {
      window.localStorage.setItem("determinex.setupCompleted", "true");
      // Pin the workspace root AND its dismissal key together. Setting only
      // ":default" relied on the show-check falling back to "default" when no
      // root was persisted -- one of two disagreeing key derivations, since
      // unified in lib/workspaceOnboarding.ts. Pinning the root makes this
      // independent of whatever the in-app default path happens to be.
      window.localStorage.setItem("explorerRoot", "C:/tmp/determinex-e2e-ws");
      window.localStorage.setItem("workspaceOnboardingDismissed:C:/tmp/determinex-e2e-ws", "1");
    });

    await page.goto("http://127.0.0.1:3000", {
      waitUntil: "domcontentloaded",
      timeout: 30_000,
    });
    await page.waitForFunction(
      () => typeof (window as any).__DETERMINEX_UI_SNAPSHOT__ === "function"
    );

    // "Mission" also appears in the DETERMINEX/rail area and in a hidden-by-default addon
    // switcher dropdown with the same testid pattern -- the reliable, always-visible trigger
    // is the "ATTACH WHAT YOU NEED" tile in the Work cockpit, matched by its visible label text.
    await page.getByText("Mission", { exact: false }).first().click();
    const activeCard = page.getByTestId("mission-active-card");
    const nextActionCard = page.getByTestId("mission-next-action-card");
    await expect(activeCard).toBeVisible();
    await expect(nextActionCard).toBeVisible();

    const activeBox = await activeCard.boundingBox();
    const nextBox = await nextActionCard.boundingBox();
    expect(activeBox).not.toBeNull();
    expect(nextBox).not.toBeNull();

    // The bug measured 130px vs 1118px (a ~9:1 real split against an intended ~1:0.9 ratio).
    // Assert the active-mission card gets at least 40% of the combined width -- comfortably
    // inside the intended ~52% (1.05fr of 2.0fr) but far above what the min-content-floor bug
    // produces, so this fails loudly if the min-w-0 fix ever regresses.
    const combined = activeBox!.width + nextBox!.width;
    const activeShare = activeBox!.width / combined;
    expect(activeShare).toBeGreaterThan(0.4);

    // And the Objective/User outcome labels must actually be legible -- each label's own text
    // box should be wide enough to hold its word without single-word-per-line wrapping.
    const objectiveLabel = activeCard.getByText("Objective", { exact: true });
    const outcomeLabel = activeCard.getByText("User outcome", { exact: true });
    await expect(objectiveLabel).toBeVisible();
    await expect(outcomeLabel).toBeVisible();
  });
});
