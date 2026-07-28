import { describe, expect, it } from "vitest";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { SURFACE_GROUPS, GROUP_BY_SURFACE, allSurfaceIds } from "../surfaceGroups";

/**
 * The taxonomy is only worth anything if it stays exhaustive. The mess it
 * replaced grew because panels were added to a type union and then wired into
 * whichever of four overlapping menus the author happened to remember -- so
 * Review and Merge ended up reachable from none of them.
 *
 * These tests read the REAL type unions out of page.tsx instead of a
 * hand-copied list, so adding a panel without giving it a home fails here
 * rather than silently producing another orphan.
 */
const PAGE = readFileSync(resolve(__dirname, "../../app/page.tsx"), "utf8");

function unionMembers(typeName: string): string[] {
  // e.g.  type WorkspaceAddon =\n  | "terminal"\n  | "editor" ... ;
  const re = new RegExp(`type\\s+${typeName}\\s*=([\\s\\S]*?);`, "m");
  const block = PAGE.match(re);
  if (!block) throw new Error(`could not find type ${typeName} in page.tsx`);
  return [...block[1].matchAll(/"([a-z0-9-]+)"/g)].map((m) => m[1]);
}

describe("surface taxonomy", () => {
  it("has exactly nine groups", () => {
    // Ryan asked for nine rail icons; more than that is the clutter we removed.
    expect(SURFACE_GROUPS).toHaveLength(9);
  });

  it("gives every surface exactly one home", () => {
    const ids = allSurfaceIds();
    const dupes = ids.filter((id, i) => ids.indexOf(id) !== i);
    expect(dupes, `surfaces listed in more than one group: ${dupes.join(", ")}`).toEqual([]);
  });

  it("covers every addon panel declared in page.tsx", () => {
    const declared = unionMembers("WorkspaceAddon");
    expect(declared.length).toBeGreaterThan(20); // sanity: the regex found a real union
    const missing = declared.filter((id) => !GROUP_BY_SURFACE[id]);
    expect(
      missing,
      `addon panels with no group -- add them to surfaceGroups.ts: ${missing.join(", ")}`
    ).toEqual([]);
  });

  it("never offers a surface that cannot open", () => {
    // The REVERSE of the two checks above, and the one that was missing.
    // `skin` sat in the taxonomy pointing at an addon id that was never in
    // `addonItems`, so the drawer advertised a panel, the user clicked it, and
    // nothing could render -- exactly the "list of things that do nothing" this
    // taxonomy replaced. The old checks only ran page.tsx -> taxonomy, so a
    // taxonomy entry with no panel behind it was invisible.
    const addons = new Set(unionMembers("WorkspaceAddon"));
    const sidebars = new Set(unionMembers("PrimaryWorkspace"));
    const orphans = SURFACE_GROUPS.flatMap((g) =>
      g.members
        .filter((m) => {
          // A modal surface has no panel by design; what it must have is a
          // declared target, or the shell's handler falls through silently.
          if (m.kind === "modal") return !m.modal;
          return m.kind === "addon" ? !addons.has(m.id) : !sidebars.has(m.id);
        })
        .map((m) => `${m.id} (${m.kind})`)
    );
    expect(orphans, `taxonomy members with no panel behind them: ${orphans.join(", ")}`).toEqual(
      []
    );
  });

  it("covers every primary sidebar declared in page.tsx", () => {
    // "none" is a state, not a surface; "extensions" is covered as Tools.
    const declared = unionMembers("PrimaryWorkspace").filter((id) => id !== "none");
    const missing = declared.filter((id) => !GROUP_BY_SURFACE[id]);
    expect(
      missing,
      `sidebars with no group -- add them to surfaceGroups.ts: ${missing.join(", ")}`
    ).toEqual([]);
  });

  it("explains every member, because the drawer promises to", () => {
    for (const g of SURFACE_GROUPS) {
      for (const m of g.members) {
        expect(m.what.trim().length, `${m.id} missing "what"`).toBeGreaterThan(10);
        expect(m.does.trim().length, `${m.id} missing "does"`).toBeGreaterThan(10);
        expect(m.label.trim()).not.toBe("");
      }
    }
  });

  it("keeps groups small enough to scan", () => {
    for (const g of SURFACE_GROUPS) {
      expect(g.members.length, `${g.id} is empty`).toBeGreaterThan(0);
      // A group that grows past ~6 is a sign it needs splitting, which is how
      // the original rail got to 18 icons.
      expect(g.members.length, `${g.id} has too many members`).toBeLessThanOrEqual(6);
    }
  });

  it("marks Determinex's own release tooling internal-only", () => {
    // These are about shipping Determinex, not the user's project, and must not
    // appear in an end-user build.
    expect(GROUP_BY_SURFACE["mission"]).toBeDefined();
    const mission = SURFACE_GROUPS.flatMap((g) => g.members).find((m) => m.id === "mission");
    const roadmap = SURFACE_GROUPS.flatMap((g) => g.members).find((m) => m.id === "roadmap");
    expect(mission?.internalOnly).toBe(true);
    expect(roadmap?.internalOnly).toBe(true);
  });
});
