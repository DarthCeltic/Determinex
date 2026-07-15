import { describe, expect, it, beforeEach } from "vitest";

import {
  ADDON_STORAGE_KEY,
  LEGACY_ADDON_STORAGE_KEY,
  readInstalledAddonIds,
  writeInstalledAddonIds,
} from "../addonStorage";

describe("add-on storage", () => {
  beforeEach(() => {
    window.localStorage.clear();
  });

  it("migrates legacy Determinex installed add-ons to the Determinex key", () => {
    window.localStorage.setItem(LEGACY_ADDON_STORAGE_KEY, JSON.stringify(["gemini", "mistral"]));

    const installed = readInstalledAddonIds(window.localStorage);

    expect(installed.has("gemini")).toBe(true);
    expect(installed.has("mistral")).toBe(true);
    expect(window.localStorage.getItem(ADDON_STORAGE_KEY)).toContain("gemini");
    expect(window.localStorage.getItem(ADDON_STORAGE_KEY)).toContain("mistral");
  });

  it("stores only user-installed add-ons under the Determinex key", () => {
    writeInstalledAddonIds(window.localStorage, new Set(["python-pytest", "gemini"]));

    expect(JSON.parse(window.localStorage.getItem(ADDON_STORAGE_KEY) || "[]")).toEqual(["gemini"]);
  });
});

