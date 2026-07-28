import { readFileSync, readdirSync, statSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

/**
 * Which Tauri commands return nothing.
 *
 * This exists because of one specific defect class that cost this project more
 * than any other. `invokeSafe` returns `null` when a command REJECTS. A Tauri
 * command declared `Result<(), String>` resolves to `null` when it SUCCEEDS. So
 * for a void command the two outcomes are the same value, and every caller that
 * used `invokeSafe` for a write could not tell a failed commit from a
 * successful one. The `try/catch` blocks wrapped around those calls were
 * unreachable code.
 *
 * Real consequences, all shipped: an editor save that cleared the dirty flag on
 * a write that never landed; a network-policy toggle that reported privacy was
 * enforced when the backend had refused; ten git writes where push/commit
 * failure was invisible; a Review-queue apply button that looked inert when it
 * had been refused, inviting re-clicks.
 *
 * The rule is derived from the Rust sources rather than a hand-kept list, for
 * the same reason `commandContract.test.ts` is: a maintained list drifts, and
 * the drift is silent. A command that later gains a return value stops being
 * flagged automatically; one that loses it starts being flagged automatically.
 */

const HERE = dirname(fileURLToPath(import.meta.url));
export const DEFAULT_TAURI_SRC = resolve(HERE, "..", "src-tauri", "src");

function rustFiles(dir, out = []) {
  let entries;
  try {
    entries = readdirSync(dir);
  } catch {
    return out; // missing src-tauri (e.g. a partial checkout) must not break linting
  }
  for (const entry of entries) {
    const p = join(dir, entry);
    let st;
    try {
      st = statSync(p);
    } catch {
      continue;
    }
    if (st.isDirectory()) {
      if (entry === "target" || entry === "gen") continue;
      rustFiles(p, out);
    } else if (entry.endsWith(".rs")) {
      out.push(p);
    }
  }
  return out;
}

/**
 * Return type of a `#[tauri::command]` fn, as written, or "" when there is none.
 *
 * Signatures wrap across lines and contain nested parens (closures, tuples), so
 * the parameter list is walked with a paren counter rather than matched with a
 * regex. The return type is then everything up to the `{` that opens the body.
 */
function signatureReturn(src, parenOpenIndex) {
  let depth = 0;
  let i = parenOpenIndex;
  for (; i < src.length; i++) {
    if (src[i] === "(") depth++;
    else if (src[i] === ")") {
      depth--;
      if (depth === 0) break;
    }
  }
  if (i >= src.length) return null; // unbalanced — not parseable, skip it
  const brace = src.indexOf("{", i + 1);
  if (brace === -1) return null;
  return src.slice(i + 1, brace).trim();
}

const COMMAND_FN =
  /#\[tauri::command\][^\n]*\n(?:\s*#[^\n]*\n)*\s*(?:pub\s+)?(?:async\s+)?fn\s+(\w+)\s*\(/g;

/** `Result<(), E>`, `Result<()>`, or a bare `()`. */
function isVoidReturn(ret) {
  if (!ret.startsWith("->")) return true; // no return type at all
  const t = ret.slice(2).trim();
  if (t === "()") return true;
  return /^Result\s*<\s*\(\s*\)\s*[,>]/.test(t);
}

let cache = null;

/**
 * Names of every `#[tauri::command]` whose success value is indistinguishable
 * from `invokeSafe`'s failure value.
 */
export function collectVoidCommands(tauriSrc = DEFAULT_TAURI_SRC) {
  if (cache && cache.dir === tauriSrc) return cache.names;
  const names = new Set();
  for (const file of rustFiles(tauriSrc)) {
    const src = readFileSync(file, "utf8");
    COMMAND_FN.lastIndex = 0;
    let m;
    while ((m = COMMAND_FN.exec(src)) !== null) {
      const ret = signatureReturn(src, m.index + m[0].length - 1);
      if (ret !== null && isVoidReturn(ret)) names.add(m[1]);
    }
  }
  cache = { dir: tauriSrc, names };
  return names;
}

/** Test-only: drop the parse cache so a fixture directory can be re-read. */
export function resetVoidCommandCache() {
  cache = null;
}
