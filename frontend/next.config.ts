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
};

export default nextConfig;
