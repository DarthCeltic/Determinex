import { describe, expect, it } from "vitest";
import { readFileSync, readdirSync, statSync } from "node:fs";
import { join, resolve } from "node:path";

/**
 * Return-shape contract: a Rust response struct and the TypeScript interface that
 * consumes it must declare the same fields.
 *
 * This is the third and last piece of what `tauri-specta` would generate for us.
 * `commandContract` pins command NAMES, `argContract` pins ARGUMENT names, and
 * nothing pinned RETURN shapes -- so a field renamed on one side only was a
 * silent break, exactly like the seven argument bugs `argContract` found.
 *
 * Why this test instead of specta: `tauri-specta` is at 2.0.0-rc.25. Adopting it
 * means an RC dependency plus replacing `generate_handler!` wholesale across 153
 * commands and deriving `specta::Type` on ~94 structs -- and 36 of those commands
 * return an untyped `serde_json::Value`, which specta emits as `unknown`, so a
 * quarter of the surface would gain no shape safety anyway. Typing the returns is
 * the prerequisite either way; this test makes each one pay off immediately,
 * without an RC crate in a build about to ship.
 *
 * It only covers commands whose Rust side is a real struct. That set is small on
 * purpose and is meant to grow: every `Value` return converted should add a row
 * here.
 */

const TAURI_SRC = resolve(__dirname, "../../../src-tauri/src");

function rustSources(dir: string, out: string[] = []): string[] {
  for (const entry of readdirSync(dir)) {
    const p = join(dir, entry);
    if (statSync(p).isDirectory()) {
      if (entry === "target" || entry === "gen") continue;
      rustSources(p, out);
    } else if (entry.endsWith(".rs")) {
      out.push(p);
    }
  }
  return out;
}

/** Field names of a `pub struct Name { ... }` from the Rust sources. */
function rustStructFields(structName: string): string[] {
  for (const file of rustSources(TAURI_SRC)) {
    const src = readFileSync(file, "utf8");
    const re = new RegExp(`struct\\s+${structName}\\s*\\{([\\s\\S]*?)\\n\\}`, "m");
    const m = re.exec(src);
    if (!m) continue;
    // A `rename_all` would change the wire names without changing these, which
    // is precisely the drift this test exists to catch -- so refuse to compare.
    const decl = src.slice(Math.max(0, m.index - 220), m.index);
    if (/rename_all/.test(decl)) {
      throw new Error(
        `${structName} carries a serde rename_all; the wire names no longer match ` +
          `its field names, so this comparison would be meaningless. Pin the ` +
          `renamed names explicitly instead.`
      );
    }
    return [...m[1].matchAll(/^\s*pub\s+([a-z_0-9]+)\s*:/gm)].map((f) => f[1]);
  }
  throw new Error(`Rust struct ${structName} not found under ${TAURI_SRC}`);
}

/** Field names of an `export interface Name { ... }` in a TS source file. */
function tsInterfaceFields(relPath: string, interfaceName: string): string[] {
  const src = readFileSync(resolve(__dirname, "../..", relPath), "utf8");
  const re = new RegExp(`interface\\s+${interfaceName}\\s*\\{([\\s\\S]*?)\\n\\}`, "m");
  const m = re.exec(src);
  if (!m) throw new Error(`TS interface ${interfaceName} not found in ${relPath}`);
  return [...m[1].matchAll(/^\s*([a-zA-Z_0-9]+)\??\s*:/gm)].map((f) => f[1]);
}

const PAIRS: Array<{
  command: string;
  rustStruct: string;
  tsFile: string;
  tsInterface: string;
}> = [
  {
    command: "probe_hardware",
    rustStruct: "HardwareProbeResponse",
    tsFile: "lib/api.ts",
    tsInterface: "HardwareProbe",
  },
  {
    command: "check_docker_status",
    rustStruct: "DockerStatusResponse",
    tsFile: "lib/api.ts",
    tsInterface: "DockerStatus",
  },
];

describe("Rust response structs match the TypeScript interfaces that read them", () => {
  it.each(PAIRS)(
    "$command: $rustStruct <-> $tsInterface",
    ({ rustStruct, tsFile, tsInterface }) => {
      const rust = rustStructFields(rustStruct).sort();
      const ts = tsInterfaceFields(tsFile, tsInterface).sort();

      expect(rust.length, `${rustStruct} parsed as having no fields`).toBeGreaterThan(0);
      expect(ts.length, `${tsInterface} parsed as having no fields`).toBeGreaterThan(0);

      const onlyRust = rust.filter((f) => !ts.includes(f));
      const onlyTs = ts.filter((f) => !rust.includes(f));
      expect(
        { onlyInRust: onlyRust, onlyInTypeScript: onlyTs },
        `${rustStruct} and ${tsInterface} have drifted`
      ).toEqual({ onlyInRust: [], onlyInTypeScript: [] });
    }
  );

  it("catches a field that exists on only one side", () => {
    // Guard for the guard: the comparison above must actually be capable of
    // failing. A matcher that passes on any input is worse than no test, which
    // this repo has already learned once from argContract.
    const rust = ["running", "version", "message"];
    const ts = ["running", "version"];
    const onlyRust = rust.filter((f) => !ts.includes(f));
    expect(onlyRust).toEqual(["message"]);
  });

  it("knows how many commands still return an untyped Value", () => {
    // Not a threshold to defend -- a visible number, so converting one is
    // recorded and regressing one is noticed. 36 at the start of this pass.
    let untyped = 0;
    for (const file of rustSources(TAURI_SRC)) {
      const src = readFileSync(file, "utf8");
      for (const m of src.matchAll(
        /#\[tauri::command\][^\n]*\n(?:\s*#[^\n]*\n)*\s*(?:pub\s+)?(?:async\s+)?fn\s+\w+\s*\(/g
      )) {
        // Walk the parameter list, then read to the body brace.
        let i = m.index + m[0].length - 1;
        let depth = 0;
        for (; i < src.length; i++) {
          if (src[i] === "(") depth++;
          else if (src[i] === ")" && --depth === 0) break;
        }
        const brace = src.indexOf("{", i + 1);
        if (brace === -1) continue;
        if (/\b(serde_json::)?Value\b/.test(src.slice(i + 1, brace))) untyped++;
      }
    }
    // Fails if it grows, so a new command cannot quietly add to the backlog.
    expect(untyped).toBeLessThanOrEqual(34);
  });
});
