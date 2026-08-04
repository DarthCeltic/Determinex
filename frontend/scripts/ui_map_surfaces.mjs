/**
 * ui_map_surfaces.mjs — build the map. Every group, every member, every after-state.
 *
 * Ryan, 2026-08-03: "do it step by step surface by surface, and id/tag it all and verify on
 * the list ... the initial shot, all the after behaviors, and the onclicks or onnavigates on
 * everything, how overlays look in that spot ... then because its all tagged it will make
 * your videos easier, because you wont have to trace blindly."
 *
 * WHY THE PREVIOUS SWEEP LIED. It clicked `rail-group-<g>` and then measured
 * `document.body.innerText`. The rail is always mounted and contains every group's name, and
 * the body is ~2,300 characters before anything opens — so every surface scored ~2,340 chars,
 * "contained its own name", and passed. Nine for nine, having established nothing. Clicking a
 * group only opens the DRAWER; the panel is two clicks further on.
 *
 * The real chain is: rail-group-<g>  ->  surface-member-<id>  ->  surface-open-<id>-panel.
 * So this asserts on `workbench-primary-surface` and, decisively, requires that its text
 * CHANGED from what was there before the click. A surface that renders nothing new cannot
 * pass by inheriting the last one's content.
 *
 *   node scripts/ui_map_surfaces.mjs [width]
 */
import { chromium } from "playwright";
import fs from "node:fs";
import { sync, renderBoardHtml, verdict } from "./ui_automap.mjs";

const CDP = process.env.DTX_CDP || "http://localhost:9223";
const SYNC = process.argv.includes("--sync");
const WIDTH = Number(process.argv.find((a) => /^\d+$/.test(a)) || 0);
const OUT = `${process.env.DTX_OUT || "C:/tmp/uimap"}/${WIDTH || "native"}`;
fs.mkdirSync(OUT, { recursive: true });

const browser = await chromium.connectOverCDP(CDP);
const page = browser.contexts()[0].pages().find((p) => p.url().includes("localhost:3000"));

// Resize the REAL window rather than setting a device-metrics override. The override
// outlived the run: a later "native" sweep inherited 960 without saying so, and its
// screenshots were not what a user sees at any size. Moving the window makes the state
// visible in the window itself.
{
  const cdp = await page.context().newCDPSession(page);
  await cdp.send("Emulation.clearDeviceMetricsOverride").catch(() => {});
  const { windowId } = await cdp.send("Browser.getWindowForTarget");
  await cdp.send("Browser.setWindowBounds", {
    windowId,
    bounds: { windowState: "normal", width: WIDTH || 1600, height: 1000 },
  });
  await page.waitForTimeout(1000);
}

const PRIMARY = '[data-testid="workbench-primary-surface"]';
const ERR = /failed to fetch|unhandled|cannot read|undefined is not|is not a function|error:/i;

// Measure the WHOLE visible page, not one container. A surface may open as a panel inside
// workbench-primary-surface OR as a maximised add-on overlay on top of it -- Agent Chat Room
// rendered a full, correct screen and scored DID-NOT-RENDER(0) because it took the overlay
// path. Comparing whole-page text before/after works for both: the rail and status bar are
// constant, so they cancel, and what remains is what the click actually produced.
const primaryText = () => page.evaluate(() => document.body.innerText || "");

/** Lines present after the click that were not there before. This is the real evidence. */
const newLines = (before, after) => {
  const split = (t) => t.split(/\r?\n/).map((x) => x.trim()).filter(Boolean);
  const b = new Set(split(before));
  return split(after).filter((x) => !b.has(x));
};

/**
 * Where the surface actually rendered. Not every surface renders into
 * `workbench-primary-surface`: `settings` opens `settings-modal` and Agent Chat Room opens
 * as a maximised add-on. Scanning only the primary container reported a complete, correct
 * screen as DID-NOT-RENDER(0) — so find the container that is really on top, and scan that.
 */
const activeRoot = () =>
  page.evaluate((s) => {
    const big = (e) => {
      const r = e?.getBoundingClientRect?.();
      return r && r.width > 200 && r.height > 200;
    };
    const modal = document.querySelector('[data-testid="settings-modal"]');
    if (big(modal)) return '[data-testid="settings-modal"]';
    // Most surfaces open as a hosted add-on window (`zone1-hosted-addon`), NOT into
    // `workbench-primary-surface` — that container only exists in some layouts, and was
    // absent for 22 of 33 surfaces. Scanning for it and falling back to `body` compared
    // every leaf on the page against every other, so the guide tour's own body text and
    // its "Prev" button were reported as a collision on 20 unrelated surfaces.
    const zone = [...document.querySelectorAll("[data-testid$='-hosted-addon']")].find(big);
    if (zone) return `[data-testid="${zone.getAttribute("data-testid")}"]`;
    if (big(document.querySelector(s))) return s;
    // No known container. Say so; do NOT scan `body` and call the noise a finding.
    return "unknown";
  }, PRIMARY);

/** Overlapping text inside the panel — the cockpit defect ("Ready" over "NO VERDICT"). */
const overlapsIn = (sel) =>
  page.evaluate((s) => {
    const root = s === "body" ? document.body : document.querySelector(s);
    if (!root) return [];

    /**
     * Is this element actually PAINTED where its rect says it is?
     *
     * `getBoundingClientRect()` reports layout position, not visibility. An item scrolled out
     * of a `overflow-y-auto` list still reports its full offset — measured live, a mission
     * button clipped to y 349-652 reported itself at y 712-730 and duly "collided" with the
     * card below it. Five of the five overlaps on Mission Control were that, and any surface
     * with a scrollable list would have produced them. So intersect against every clipping
     * ancestor before believing a rect.
     */
    const paintedRect = (e) => {
      let r = e.getBoundingClientRect();
      let top = r.top, left = r.left, right = r.right, bottom = r.bottom;
      for (let p = e.parentElement; p && p !== document.body; p = p.parentElement) {
        const st = getComputedStyle(p);
        if (st.overflow === "visible" && st.overflowX === "visible" && st.overflowY === "visible") {
          continue;
        }
        const c = p.getBoundingClientRect();
        top = Math.max(top, c.top);
        left = Math.max(left, c.left);
        right = Math.min(right, c.right);
        bottom = Math.min(bottom, c.bottom);
      }
      top = Math.max(top, 0);
      left = Math.max(left, 0);
      right = Math.min(right, window.innerWidth);
      bottom = Math.min(bottom, window.innerHeight);
      return { top, left, right, bottom, width: right - left, height: bottom - top };
    };

    const els = [...root.querySelectorAll("*")]
      .filter((e) => {
        if ([...e.children].some((c) => (c.textContent || "").trim())) return false;
        const t = (e.textContent || "").trim();
        if (!t) return false;
        const r = paintedRect(e);
        return r.width > 14 && r.height > 8;
      })
      .map((e) => {
        e.__pr = paintedRect(e);
        return e;
      });
    const hits = [];
    for (let i = 0; i < els.length && hits.length < 5; i++) {
      const a = els[i].__pr;
      for (let j = i + 1; j < els.length; j++) {
        const b = els[j].__pr;
        const ox = Math.min(a.right, b.right) - Math.max(a.left, b.left);
        const oy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
        if (ox > 10 && oy > 10) {
          hits.push(
            `${els[i].textContent.trim().slice(0, 22)} || ${els[j].textContent.trim().slice(0, 22)}`
          );
          break;
        }
      }
    }
    return hits;
  }, sel);

/** Everything clickable inside the panel — this is the onclick inventory for the map. */
const actionsIn = (sel) =>
  page.evaluate((s) => {
    const root = s === "body" ? document.body : document.querySelector(s);
    if (!root) return [];
    return [...root.querySelectorAll("button,a,[role=button],[data-testid]")]
      .map((e) => ({
        tid: e.getAttribute("data-testid") || "",
        label: (e.textContent || "").trim().slice(0, 34),
        tag: e.tagName.toLowerCase(),
        disabled: e.hasAttribute("disabled") || e.getAttribute("aria-disabled") === "true",
      }))
      .filter((x) => x.tid || x.label)
      .slice(0, 40);
  }, sel);

/**
 * Has the surface actually finished rendering, or is it still a spinner?
 *
 * `source/merge` scored "ok · +3 new lines" while showing an empty black panel with a
 * loading ring in the middle — the title bar alone clears a 3-line bar. "Rendered something"
 * and "rendered its content" are different claims, and only the screenshot told them apart.
 * So the poll now waits for the spinner to go and for there to be real text, and says so when
 * it never arrives.
 */
const settledIn = (sel) =>
  page.evaluate((s) => {
    // Not every surface renders into a tagged container: at 960 the Source Control panel
    // has no data-testid ancestor over 250x250, so the detector found nothing and reported
    // a fully rendered panel -- branch, 8 changed files, commit box, all visible in the
    // screenshot -- as "no container". Rather than invent a pass, fall back to the page and
    // SAY that settle was not asserted for this surface, so a green row is not read as more
    // evidence than it is.
    if (s === "unknown") {
      const spin = document.querySelector('.animate-spin,[role="progressbar"],[aria-busy="true"]');
      const chars = (document.body.innerText || "").trim().length;
      if (spin && chars < 400) return { settled: false, why: "spinner, page nearly empty", chars };
      return { settled: true, why: "no tagged container — settle not asserted", chars };
    }
    const root = s === "body" ? document.body : document.querySelector(s);
    if (!root) return { settled: false, why: "no container", chars: 0 };
    const spinner = root.querySelector(
      '.animate-spin,[role="progressbar"],[aria-busy="true"],[data-loading="true"]'
    );
    const text = (root.innerText || "").trim();
    // A spinner over a POPULATED panel is a refresh indicator, not a loading state.
    // Source Control polls git and spins a small icon in its header while it does; the
    // panel underneath is fully rendered — branch, 8 changed files, commit box — and
    // calling that "still loading" reported a working surface as broken. The case this
    // must still catch is source/merge: a loading ring centred on a black panel with
    // nothing but the title bar, which lands well under this threshold.
    if (spinner && text.length < 150) {
      return { settled: false, why: `spinner over ${text.length} chars`, chars: text.length };
    }
    // A text-based loading state is as real as a spinner and has no class to find. The
    // editor's Explorer sits on "Scanning..." for ~8s, so the screenshot caught an empty
    // tree under "No files open" and the board would have shipped that as the CODE surface.
    // Matched only as a whole standalone line, so prose containing the word is not a hit.
    const waiting = text
      .split(/\r?\n/)
      .map((l) => l.trim())
      .find((l) => /^(scanning|loading|fetching|initializing|please wait)[.…\s]*$/i.test(l));
    if (waiting) return { settled: false, why: `"${waiting}" still showing`, chars: text.length };
    if (text.length < 40) return { settled: false, why: `only ${text.length} chars`, chars: text.length };
    return { settled: true, why: "", chars: text.length };
  }, sel);

const clickTid = async (tid, ms = 4000) => {
  const l = page.locator(`[data-testid="${tid}"]`);
  if (!(await l.count())) return false;
  await l.first().click({ timeout: ms }).catch(() => {});
  return true;
};

/**
 * Uncover the workbench. TWO things can paint over it and they fail differently.
 *
 * The maximised add-on leaves the cards underneath mounted and sized, so Playwright still
 * calls them visible while every click lands on the tool.
 *
 * `settings-modal` is worse, and it is what made `system/settings` and `system/flywheel`
 * unreadable. It is a SIBLING of the workbench at z-50 across inset-0. Once `skin` opens
 * it, it stays open: every later member click is swallowed by the backdrop, and because its
 * text is already in the page it contributes no new lines — so the product looked like it
 * rendered nothing when in fact it had rendered the Config Vault correctly and the sweep
 * never closed it. It also survived to the END of the run, which is how the app was found
 * sitting in Skin Pack with an empty drawer.
 */
async function dismissOverlays() {
  for (let i = 0; i < 5; i++) {
    let acted = false;

    const x = page.getByTitle("Close add-on");
    if (await x.count().catch(() => 0)) {
      await x.first().click({ timeout: 2000 }).catch(() => {});
      acted = true;
      await page.waitForTimeout(250);
    }

    // The 16-step guide tour is a THIRD overlay, and the most misleading one: it is a small
    // floating card, so it never looks like it is in the way, but it survives every surface
    // change and it sits inside whatever container gets scanned. It put the same phantom
    // collision ("Local models keep code … || Prev") on 20 surfaces at once.
    const guide = page.locator('[data-testid="guide-overlay"]');
    if (await guide.count().catch(() => 0)) {
      const close = page.locator('[data-testid="guide-window"] button').last();
      if (await close.count().catch(() => 0)) {
        await close.click({ timeout: 1500 }).catch(() => {});
      }
      await page.keyboard.press("Escape").catch(() => {});
      await page.waitForTimeout(300);
      if (await guide.count().catch(() => 0)) {
        // Last resort so one stuck tour cannot poison the whole sweep.
        await page.evaluate(() =>
          document.querySelector('[data-testid="guide-overlay"]')?.remove()
        );
      }
      acted = true;
    }

    const open = await page
      .evaluate(() => {
        const m = document.querySelector('[data-testid="settings-modal"]');
        return !!(m && m.getBoundingClientRect().width > 100);
      })
      .catch(() => false);
    if (open) {
      const close = page.getByRole("button", { name: /close config/i });
      if (await close.count().catch(() => 0)) {
        await close.first().click({ timeout: 2000 }).catch(() => {});
      } else {
        await page.keyboard.press("Escape").catch(() => {});
      }
      acted = true;
      await page.waitForTimeout(350);
    }

    if (!acted) return true;
  }
  return false;
}

/**
 * Open a surface from scratch: uncover, re-open its group (opening a panel closes the
 * drawer), click the member, then take whichever open-affordance it offers.
 */
async function openSurface(g, m) {
  await dismissOverlays();
  if (!(await page.locator(`[data-testid="surface-member-${m}"]`).count())) {
    await clickTid(`rail-group-${g}`);
    await page.waitForTimeout(650);
  }
  await clickTid(`surface-member-${m}`);
  await page.waitForTimeout(450);
  const modes = [];
  for (const mode of ["panel", "dock"]) {
    if (await page.locator(`[data-testid="surface-open-${m}-${mode}"]`).count()) modes.push(mode);
  }
  await clickTid(`surface-open-${m}-panel`);
  await clickTid(`surface-open-${m}-dock`);
  await clickTid(`surface-open-${m}`);
  await clickTid(`${m}-modal`);
  await clickTid(`tools-launch-${m}`);
  return modes;
}

/**
 * `before` must be some OTHER surface's content, or the comparison is vacuous. The reset
 * parks the app on work/hive, so mapping work/hive first diffed hive against hive and
 * reported the cockpit as rendering nothing — a fresh instance of the same false failure
 * this script was rewritten to stop producing. Pivoting through a fixed surface first makes
 * every member's `before` a known, different screen.
 */
const PIVOT = { group: "work", member: "hub" };
const PIVOT_ALT = { group: "code", member: "editor" };
async function pivotAwayFrom(m) {
  const p = m === PIVOT.member ? PIVOT_ALT : PIVOT;
  await openSurface(p.group, p.member);
  await page.waitForTimeout(900);
  return p.member;
}

/**
 * --selftest: prove the two assertions go RED against the defects they exist to catch,
 * before any green result from them is believed.
 *
 * This script has now reported four different verdicts about builds that were fine, every
 * time because the check could not fail. A guard that has never been shown failing is not
 * evidence; it is decoration.
 */
if (process.argv.includes("--selftest")) {
  let bad = 0;
  await openSurface("trust", "cloak");
  // Wait for it to actually finish, rather than a fixed guess. On the real backend this
  // surface reads a live Cloak audit off disk (~5,000 chars) instead of the stale binary's
  // "No Cloak audit loaded", so a 1.5s baseline caught it mid-load and the selftest failed
  // its own clean control -- the harness reporting a defect in itself.
  const root = await activeRoot();
  for (let i = 0; i < 30; i++) {
    await page.waitForTimeout(500);
    if ((await settledIn(root)).settled) break;
  }
  console.log(`selftest: scanning ${root}`);

  // 1. Overlap detector must find a collision that is definitely there.
  const clean = await overlapsIn(root);
  await page.evaluate((s) => {
    const r = document.querySelector(s);
    const mk = (t, left) => {
      const d = document.createElement("div");
      d.className = "__selftest";
      d.textContent = t;
      d.style.cssText = `position:absolute;top:120px;left:${left}px;width:200px;height:40px;font-size:16px`;
      return d;
    };
    r.style.position = r.style.position || "relative";
    r.appendChild(mk("SELFTEST LEFT BLOCK", 20));
    r.appendChild(mk("SELFTEST RIGHT BLOCK", 90)); // deliberately overlapping
  }, root);
  await page.waitForTimeout(400);
  const dirty = await overlapsIn(root);
  const caught = dirty.some((o) => o.includes("SELFTEST"));
  console.log(`  overlap detector: clean=${clean.length} injected=${dirty.length} caught=${caught}`);
  if (!caught) { console.log("  FAIL overlap detector did not see a real collision"); bad++; }
  await page.evaluate(() => document.querySelectorAll(".__selftest").forEach((e) => e.remove()));

  // 1b. …and must NOT report a collision between elements that are scrolled out of their
  //     own clipping container. Without this the detector reported five phantom overlaps on
  //     Mission Control alone, and would fire on every scrollable list in the product.
  await page.evaluate((s) => {
    const r = document.querySelector(s);
    const box = document.createElement("div");
    box.className = "__selftest";
    box.style.cssText = "position:absolute;top:60px;left:20px;width:240px;height:60px;overflow-y:auto";
    const tall = document.createElement("div");
    tall.style.cssText = "height:600px;position:relative";
    const far = document.createElement("div");
    far.textContent = "SELFTEST SCROLLED AWAY";
    far.style.cssText = "position:absolute;top:400px;left:0;width:220px;height:40px;font-size:16px";
    tall.appendChild(far);
    box.appendChild(tall);
    r.appendChild(box);
  }, root);
  await page.waitForTimeout(400);
  const clipped = await overlapsIn(root);
  const phantom = clipped.some((o) => o.includes("SCROLLED AWAY"));
  console.log(`  clipped-element filter: phantom reported=${phantom}`);
  if (phantom) { console.log("  FAIL a scrolled-out element was reported as colliding"); bad++; }
  await page.evaluate(() => document.querySelectorAll(".__selftest").forEach((e) => e.remove()));

  // 1c. The settle assertion must go red on a spinner and on a bare "Scanning..." line, and
  //     green on neither. This is what stopped source/merge shipping as clean while it showed
  //     an empty panel with a loading ring.
  const settledClean = await settledIn(root);
  // Inject the spinner into an EMPTIED clone-scope so the control matches the real case:
  // a loading ring on a panel with nothing else on it. A spinner dropped into an already
  // populated panel is the Source Control refresh case, which must NOT be reported.
  await page.evaluate((s) => {
    const r = document.querySelector(s);
    r.dataset.selftestHtml = r.innerHTML;
    r.innerHTML = '<div class="__selftest animate-spin" style="width:24px;height:24px"></div>';
  }, root);
  await page.waitForTimeout(300);
  const settledSpin = await settledIn(root);
  await page.evaluate((s) => {
    const r = document.querySelector(s);
    if (r.dataset.selftestHtml !== undefined) {
      r.innerHTML = r.dataset.selftestHtml;
      delete r.dataset.selftestHtml;
    }
  }, root);
  await page.evaluate(() => document.querySelectorAll(".__selftest").forEach((e) => e.remove()));
  await page.evaluate((s) => {
    const d = document.createElement("div");
    d.className = "__selftest";
    d.textContent = "Scanning...";
    document.querySelector(s).appendChild(d);
  }, root);
  await page.waitForTimeout(300);
  const settledScan = await settledIn(root);
  await page.evaluate(() => document.querySelectorAll(".__selftest").forEach((e) => e.remove()));
  console.log(
    `  settle assertion: clean=${settledClean.settled} spinner=${settledSpin.settled} scanning=${settledScan.settled}`
  );
  if (!settledClean.settled || settledSpin.settled || settledScan.settled) {
    console.log("  FAIL settle assertion does not separate rendered from still-loading");
    bad++;
  }

  // 2. New-content assertion must go red when a surface renders nothing new — which is what
  //    "opening the surface that is already open" is.
  await openSurface("trust", "cloak");
  await page.waitForTimeout(1200);
  const a = await primaryText();
  await openSurface("trust", "cloak");
  await page.waitForTimeout(1200);
  const again = newLines(a, await primaryText()).length;
  console.log(`  no-new-content assertion: reopening the same surface -> ${again} new lines`);
  if (again >= 3) { console.log("  FAIL re-opening one surface looked like fresh content"); bad++; }

  console.log(bad ? `\nSELFTEST FAILED (${bad})` : "\nSELFTEST PASSED — both assertions can fail");
  await browser.close();
  process.exit(bad ? 1 : 0);
}

const map = [];
const groups = await page.evaluate(() =>
  [...document.querySelectorAll("[data-testid^='rail-group-']")].map((e) =>
    e.getAttribute("data-testid").replace("rail-group-", "")
  )
);

console.log(`width=${WIDTH || "native"}   groups=${groups.length}\n`);

for (const g of groups) {
  await dismissOverlays();
  await clickTid(`rail-group-${g}`);
  await page.waitForTimeout(700);

  const members = await page.evaluate(() =>
    [...document.querySelectorAll("[data-testid^='surface-member-']")].map((e) =>
      e.getAttribute("data-testid").replace("surface-member-", "")
    )
  );
  console.log(`  ${g}  (${members.length} members: ${members.join(", ") || "none"})`);

  for (const m of members) {
    const rec = { group: g, member: m, opened: false, changed: false, chars: 0, err: "",
                  overlap: [], actions: [], modes: [], renderedIn: "", pivot: "" };

    // Park on a known DIFFERENT surface first, so `before` is that screen and not this one.
    rec.pivot = await pivotAwayFrom(m);
    const before = await primaryText();

    // Not every surface offers a Panel/Dock choice. settings opens settings-modal,
    // mission and roadmap are tools-launch-*, and extensions opens straight away -- these
    // open on the MEMBER click itself. Reporting them NO-OPEN was this script looking for
    // a button that correctly does not exist.
    rec.modes = await openSurface(g, m);
    rec.opened = true; // the member click fired; the new-content assertion below is the real test

    // Poll: some panels genuinely need ~12s (Source Control), and an earlier sweep called
    // one EMPTY by sampling at 2.6s.
    // Poll: some panels genuinely need a long time. Brain & Model Slots populates its four
    // Role Slots somewhere between 12s and 16s, so a 12s ceiling reported it NOT-SETTLED —
    // a defect in this script's patience, not in the panel. The time itself is worth keeping
    // though: fourteen seconds of "loading..." is a real thing a user (and a camera) sees.
    let after = "";
    let settle = { settled: false, why: "never polled", chars: 0 };
    // EVER settled, not "settled at the instant I happened to look". Brain & Model Slots
    // re-polls telemetry every 8s and shows a spinner while it refetches, so a panel that
    // rendered perfectly can be caught mid-refresh forever -- which is how run/build and
    // learn/benchmark were reported NOT-SETTLED while both were clean when opened alone.
    // The question worth asking is whether the surface ever finished, not whether it is
    // momentarily busy afterwards.
    let everSettled = false;
    const t0 = Date.now();
    let firstSettleMs = null;
    // Budget covers the slowest HONEST operation in the product, not the fastest. run/build
    // says on screen "Running cargo check... first run can take up to 90s" and means it; a
    // 25s ceiling reported real work as a hang. Every surface breaks out the moment it
    // settles, so only the genuinely slow ones pay this.
    for (let i = 0; i < 200; i++) {
      await page.waitForTimeout(550);
      after = await primaryText();
      settle = await settledIn(await activeRoot());
      if (settle.settled && !everSettled) {
        everSettled = true;
        firstSettleMs = Date.now() - t0;
      }
      // Both conditions, not either: content must be new AND the surface must have rendered.
      if (newLines(before, after).length >= 3 && everSettled) break;
    }
    rec.settled = everSettled;
    // Keep the note even on a pass when it records a limitation rather than a result.
    rec.settleNote = everSettled
      ? settle.why.includes("not asserted")
        ? settle.why
        : ""
      : settle.why;
    rec.settleMs = firstSettleMs ?? Date.now() - t0;
    const fresh = newLines(before, after);
    rec.chars = after.length;
    rec.fresh = fresh.length;
    rec.freshSample = fresh.slice(0, 3);
    // A surface must put something NEW on screen. Inheriting the previous panel is a fail.
    rec.changed = fresh.length >= 3;
    // Don't read a TERMINAL's scrollback for error text. The detector exists to catch the
    // UI failing, and `run/terminal` faithfully displays whatever was last run in it -- so a
    // command that printed "ERROR:" makes the terminal look broken for doing its job. It
    // flagged exactly that on leftover output from this session's own probes.
    const scanText = await page.evaluate(() => {
      const body = document.body.cloneNode(true);
      body.querySelectorAll(".xterm").forEach((e) => e.remove());
      return body.innerText || "";
    });
    const e = scanText.match(ERR);
    rec.err = e ? e[0] : "";
    rec.renderedIn = await activeRoot();
    if (rec.renderedIn === "unknown") {
      rec.overlap = [];
      rec.actions = [];
    } else {
      rec.overlap = await overlapsIn(rec.renderedIn);
      rec.actions = await actionsIn(rec.renderedIn);
    }
    rec.head = after.slice(0, 60).replace(/\n/g, " / ");

    await page.screenshot({ path: `${OUT}/${g}__${m}.png` });

    const bad = verdict(rec).bad;
    const where = rec.renderedIn.includes("settings-modal")
      ? " [modal]"
      : rec.renderedIn === "addon"
        ? " [addon]"
        : "";
    console.log(
      `      ${bad.length ? "FAIL" : "ok  "} ${m.padEnd(16)} ${
        bad.length ? bad.join(" · ") : `+${rec.fresh} lines · ${rec.actions.length} actions`
      }${where}`
    );
    if (rec.overlap.length) console.log(`             ${rec.overlap[0]}`);
    map.push(rec);
  }
}

// Leave the app usable. The previous sweep ended inside Config Vault with the drawer
// swallowed, which is the state the next run then had to diagnose.
await dismissOverlays();

// Use the SAME verdict the doc and the guard use. This line kept its own copy of the pass
// criteria, forgot the settle check the moment it was added, and printed "33/33 clean" on a
// run that had just reported a FAIL three lines above it.
const fails = map.filter((r) => !verdict(r).ok);
console.log(`\n  ${map.length - fails.length}/${map.length} surfaces clean at width ${WIDTH || "native"}`);
fs.writeFileSync(`${OUT}/map.json`, JSON.stringify(map, null, 2));
console.log(`  map -> ${OUT}/map.json`);

const meta = {
  width: WIDTH || "native",
  generatedAt: new Date().toISOString().replace(/\.\d+Z$/, "Z"),
  shots: `${OUT}/`,
};
// The board is the thing you LOOK at. Written every run, committed never.
fs.writeFileSync(`${OUT}/ui-map-board.html`, renderBoardHtml(map, meta));
console.log(`  board -> ${OUT}/ui-map-board.html`);

if (SYNC) {
  // Only the full-width crawl is authoritative for the committed map — syncing a narrow run
  // would overwrite it with a layout nobody's default window is at, and the overlap findings
  // would silently swap meaning between runs.
  if (WIDTH) {
    console.log(`\n  --sync ignored: the committed map tracks the native width only.`);
  } else {
    const d = sync(map, meta);
    console.log(`\n  synced -> frontend/ui-surface-map.json + docs/ide-frontend/UI_SURFACE_MAP.md`);
    if (!d.added.length && !d.removed.length && !d.changed.length) {
      console.log(`  no change since the last sync.`);
    }
    for (const k of d.added) console.log(`  ADDED    ${k}`);
    for (const k of d.removed) console.log(`  REMOVED  ${k}`);
    for (const c of d.changed) console.log(`  CHANGED  ${c.key}  —  ${c.notes.join(" · ")}`);
  }
}
await browser.close();
