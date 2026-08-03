/**
 * The same first-run drive, through the DESKTOP app's Tauri IPC.
 *
 * This exists as a separate run because passing in the browser proves almost nothing about
 * the shipped product: `invokeSafe` prefers Tauri IPC and only falls back to the HTTP bridge,
 * so a feature can be complete on the Python side, green in every test, reachable over the
 * bridge -- and dead in the app. That is exactly what happened to `assess_idea_context`
 * earlier today, and the failure looked like a feature that simply did not do anything.
 *
 * Needs the app running with CDP:
 *   $env:WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS="--remote-debugging-port=9223"; npm run tauri dev
 */
import { chromium } from "playwright";

const CDP = process.env.DETERMINEX_CDP ?? "http://localhost:9223";
const fail = [];
const note = (ok, what, detail = "") => {
  console.log(`${ok ? "  PASS" : "  FAIL"}  ${what}${detail ? ` — ${detail}` : ""}`);
  if (!ok) fail.push(what);
};

const browser = await chromium.connectOverCDP(CDP);
const page = browser
  .contexts()
  .flatMap((c) => c.pages())
  .find((p) => !p.url().startsWith("devtools://"));
if (!page) {
  console.log("no app page on " + CDP);
  process.exit(1);
}

console.log("[0] the four onboarding commands are reachable over Tauri IPC");
// Reaching a command needs a #[tauri::command], its generate_handler! registration AND a
// capability ACL entry. Missing any one of the three fails identically from the UI, so each
// is called for real rather than inferred from the source.
const probes = await page.evaluate(async () => {
  const inv = window.__TAURI_INTERNALS__?.invoke;
  if (!inv) return { noTauri: true };
  const call = async (cmd, args) => {
    try {
      const r = await inv(cmd, args);
      return { ok: true, shape: Object.keys(r ?? {}).join(",") };
    } catch (e) {
      return { ok: false, error: String(e).slice(0, 200) };
    }
  };
  return {
    provider_setup_report: await call("provider_setup_report"),
    user_profile_get: await call("user_profile_get"),
    provider_setup_verify: await call("provider_setup_verify", { payload: { id: "claude-code" } }),
    user_profile_set: await call("user_profile_set", { payload: { level: "mixed" } }),
  };
});

note(!probes.noTauri, "running inside the desktop app, not a browser tab");
for (const [cmd, res] of Object.entries(probes).filter(([k]) => k !== "noTauri")) {
  note(res.ok, `${cmd} reachable`, res.ok ? res.shape : res.error);
}

console.log("\n[1] the report the desktop app actually receives");
const report = await page.evaluate(async () => {
  const env = await window.__TAURI_INTERNALS__.invoke("provider_setup_report");
  return env?.data ?? env;
});
note(Array.isArray(report?.options), "report carries an options list");
if (Array.isArray(report?.options)) {
  console.log(`    "${report.headline}"`);
  for (const o of report.options) {
    console.log(
      `      ${o.group.padEnd(11)} ${o.id.padEnd(12)} ${o.readiness.padEnd(22)} ${o.action_label}`
    );
  }
  const google = report.options.filter((o) => o.id === "google");
  note(google.length === 1, "Google is exactly one row", `${google.length} found`);
  note(google[0]?.signin === true, "Google is offered as a sign-in, not a bare key field");
  note(
    report.options.filter((o) => o.group === "start_here").length >= 3,
    "at least three no-key options are offered up front"
  );
  // A saved credential is not a working provider. Nothing may claim ready without a live call.
  const liars = report.options.filter((o) => o.ready && o.readiness !== "verified");
  note(liars.length === 0, "nothing claims ready without a verified live call", liars.map((o) => o.id).join(","));
}

console.log(`\n${fail.length === 0 ? "ALL PASS" : `${fail.length} FAILED: ${fail.join(", ")}`}`);
await browser.close();
process.exit(fail.length === 0 ? 0 : 1);
