import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./playwright-tests",
  timeout: 60_000,
  expect: { timeout: 10_000 },
  fullyParallel: false,
  retries: 0,
  reporter: [["list"], ["json", { outputFile: "playwright-report/results.json" }]],
  use: {
    // Matches tauri.conf.json's devUrl exactly -- the real app only ever
    // connects via localhost, not 127.0.0.1 (see next.config.ts's
    // allowedDevOrigins comment for why that distinction silently breaks
    // hydration).
    baseURL: "http://localhost:3000",
    headless: true,
    screenshot: "only-on-failure",
    video: "off",
  },
  projects: [
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
    },
  ],
  // Playwright owns the server so CI does not need a separate one, and a local
  // run reuses the dev server you already have open instead of fighting it for
  // port 3000.
  //
  // `next dev`, deliberately, not a production build: it is the exact mode
  // `tauri dev` runs under (see the baseURL note above), and `next.config.ts`
  // sets `distDir: "out"` for the export build, which would need a separate
  // static file server here for no added coverage.
  webServer: {
    command: "npm run dev",
    url: "http://localhost:3000",
    reuseExistingServer: !process.env.CI,
    timeout: 180_000,
    stdout: "ignore",
    stderr: "pipe",
  },
});
