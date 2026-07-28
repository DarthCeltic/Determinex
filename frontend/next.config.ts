import type { NextConfig } from "next";

const isProductionBuild = process.env.NODE_ENV === "production";

const nextConfig: NextConfig = {
  output: "export",
  // Keep Tauri/static export in out, but keep next dev manifests in .next.
  // Sharing out for both lets build/export remove files a live dev server needs.
  distDir: isProductionBuild ? "out" : ".next",
  trailingSlash: true,
  images: {
    unoptimized: true,
  },
  reactStrictMode: false,
  // Next's dev-server HMR websocket rejects any Origin not on this list
  // (defaults to localhost only) -- 127.0.0.1 is the same machine but a
  // different origin string, and the mismatch silently breaks client-side
  // hydration entirely (chunks load, but the dev runtime never executes
  // them) with no error surfaced beyond a WebSocket ERR_INVALID_HTTP_RESPONSE.
  // The real Tauri app already uses localhost (tauri.conf.json devUrl) so
  // this didn't affect the shipped app, but it silently broke the whole
  // Playwright e2e suite, which used 127.0.0.1. Trust both explicitly.
  allowedDevOrigins: ["localhost", "127.0.0.1"],
};

export default nextConfig;
