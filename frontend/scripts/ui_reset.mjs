import { chromium } from "playwright";
const b = await chromium.connectOverCDP("http://localhost:9223");
const p = b.contexts()[0].pages().find(x => !x.url().startsWith("devtools://"));
await p.goto("http://localhost:3000/", { waitUntil: "domcontentloaded", timeout: 20000 }).catch(() => {});
const box = p.getByPlaceholder(/describe what you want to build/i).first();
await box.waitFor({ state: "visible", timeout: 120000 });
console.log("AT_START: idea box visible");
await p.screenshot({ path: "C:/tmp/ui_reset.png" });
await b.close();
