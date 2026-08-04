/**
 * ui_probe_state.mjs — what is actually on screen right now, and what can dismiss it.
 * Read-only. No clicks. Used to separate "measured nothing" from "nothing happened".
 */
import { chromium } from "playwright";

const browser = await chromium.connectOverCDP(process.env.DTX_CDP || "http://localhost:9223");
const page = browser.contexts()[0].pages().find((p) => p.url().includes("localhost:3000"));

const info = await page.evaluate(() => {
  const vp = { w: window.innerWidth, h: window.innerHeight, dpr: devicePixelRatio };
  const tids = [...document.querySelectorAll("[data-testid]")].map((e) =>
    e.getAttribute("data-testid")
  );
  // Anything that paints over the workbench: fixed/absolute, big, high z.
  const overlays = [...document.querySelectorAll("body *")]
    .filter((e) => {
      const s = getComputedStyle(e);
      if (s.position !== "fixed" && s.position !== "absolute") return false;
      const r = e.getBoundingClientRect();
      return r.width > window.innerWidth * 0.5 && r.height > window.innerHeight * 0.5;
    })
    .slice(0, 12)
    .map((e) => ({
      tag: e.tagName.toLowerCase(),
      tid: e.getAttribute("data-testid") || "",
      cls: (e.className || "").toString().slice(0, 70),
      z: getComputedStyle(e).zIndex,
      text: (e.textContent || "").trim().slice(0, 50),
    }));
  const closers = [...document.querySelectorAll("button,[role=button]")]
    .map((e) => (e.textContent || "").trim())
    .filter((t) => /close|cancel|dismiss|back|done/i.test(t) && t.length < 30);
  return {
    vp,
    bodyChars: (document.body.innerText || "").length,
    railGroups: tids.filter((t) => t.startsWith("rail-group-")),
    members: tids.filter((t) => t.startsWith("surface-member-")),
    overlays,
    closers: [...new Set(closers)],
    head: (document.body.innerText || "").slice(0, 200).replace(/\n/g, " / "),
  };
});
console.log(JSON.stringify(info, null, 2));
await browser.close();
