import { ADDONS } from "@/lib/addons";

export const ADDON_STORAGE_KEY = "determinex.addons.installed";
export const LEGACY_ADDON_STORAGE_KEY = "determinex-ext-installed";
export const ADDONS_UPDATED_EVENT = "addons-updated";

export function defaultInstalledAddonIds(): Set<string> {
  return new Set(
    ADDONS.filter((a) => a.status === "installed" || a.status === "builtin").map((a) => a.id)
  );
}

function parseAddonIds(raw: string | null): string[] {
  if (!raw) return [];
  const parsed = JSON.parse(raw);
  return Array.isArray(parsed) ? parsed.filter((id): id is string => typeof id === "string") : [];
}

export function readInstalledAddonIds(storage: Storage): Set<string> {
  const defaults = defaultInstalledAddonIds();
  const current = parseAddonIds(storage.getItem(ADDON_STORAGE_KEY));
  const legacy = parseAddonIds(storage.getItem(LEGACY_ADDON_STORAGE_KEY));
  const merged = new Set([...defaults, ...legacy, ...current]);

  if (legacy.length > 0 && current.length === 0) {
    writeInstalledAddonIds(storage, merged);
  }

  return merged;
}

export function writeInstalledAddonIds(storage: Storage, installed: Set<string>): string[] {
  const userInstalled = [...installed].filter((id) => {
    const addon = ADDONS.find((a) => a.id === id);
    return addon && addon.status !== "builtin";
  });
  storage.setItem(ADDON_STORAGE_KEY, JSON.stringify(userInstalled));
  return userInstalled;
}
