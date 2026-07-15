/**
 * Determinex VS Code extension - the brain in the editor you already use.
 *
 * Every command shells out to the ONE governed backend entry point
 * (scripts/ide/determinex_backend_cli.py), which delegates to the Tauri bridge ->
 * command surface -> canonical engine. The extension implements no logic of its
 * own; it is the editor-side adapter. VS Code is the editor, Determinex is the
 * brain, and the oracle still judges everything any AI produces.
 */
import * as cp from "child_process";
import * as path from "path";
import * as vscode from "vscode";

function setting<T>(key: string, fallback: T, legacyKey?: string): T {
  const [section, ...rest] = key.split(".");
  const value = vscode.workspace.getConfiguration(section).get<T>(rest.join("."));
  if (value !== undefined && value !== "") return value;

  if (legacyKey) {
    const [legacySection, ...legacyRest] = legacyKey.split(".");
    const legacyValue = vscode.workspace.getConfiguration(legacySection).get<T>(legacyRest.join("."));
    if (legacyValue !== undefined && legacyValue !== "") return legacyValue;
  }

  return fallback;
}

function repoRoot(): string {
  const cfg = setting<string>("determinex.repoRoot", "", "determinex.repoRoot");
  if (cfg && cfg.length > 0) return cfg;
  const folders = vscode.workspace.workspaceFolders;
  return folders && folders.length > 0 ? folders[0].uri.fsPath : process.cwd();
}

function callBackend(command: string, args: Record<string, unknown>): Promise<any> {
  const py = setting<string>("determinex.pythonPath", "python", "determinex.pythonPath");
  const root = repoRoot();
  const cli = path.join(root, "scripts", "ide", "determinex_backend_cli.py");
  return new Promise((resolve, reject) => {
    const child = cp.spawn(py, [cli, command, "--json", JSON.stringify(args)], { cwd: root });
    let out = "";
    let err = "";
    child.stdout.on("data", (d) => (out += d.toString()));
    child.stderr.on("data", (d) => (err += d.toString()));
    child.on("close", () => {
      const line = out.trim().split("\n").filter((l) => l.trim().startsWith("{")).pop();
      if (!line) return reject(new Error(err || "no JSON from backend"));
      try {
        resolve(JSON.parse(line));
      } catch (e) {
        reject(e);
      }
    });
  });
}

async function buildFromIdea() {
  const idea = await vscode.window.showInputBox({
    prompt: "Describe what to build (include examples like f(2,3)==5 for a sound oracle).",
  });
  if (!idea) return;
  await vscode.window.withProgress(
    { location: vscode.ProgressLocation.Notification, title: "Determinex: synthesizing oracle + building..." },
    async () => {
      const model = setting<string>("determinex.model", "determinex-engineer-v11-dsl", "determinex.model");
      const r = await callBackend("build_idea", { idea_text: idea, opt_in: true, model_id: model });
      const p = r.payload || {};
      if (p.solved) {
        const doc = await vscode.workspace.openTextDocument({ language: "python", content: p.program || "" });
        await vscode.window.showTextDocument(doc);
        vscode.window.showInformationMessage(`Determinex: verified program (${p.proof || "oracle passed"}).`);
      } else {
        vscode.window.showWarningMessage(`Determinex: not solved. ${p.proof || ""} Moves: ${(p.next_moves || []).join(", ")}`);
      }
    }
  );
}

async function previewIdeaOracle() {
  const idea = await vscode.window.showInputBox({ prompt: "Idea to preview the sound oracle for:" });
  if (!idea) return;
  const r = await callBackend("preview_idea_oracle", { idea_text: idea });
  const p = r.payload || {};
  const doc = await vscode.workspace.openTextDocument({
    language: "python",
    content: `# Sound oracle preview (${p.n_checks} checks, sound=${p.oracle_sound})\n\n${p.oracle_tests || ""}`,
  });
  await vscode.window.showTextDocument(doc);
}

async function repairDiagnose() {
  const r = await callBackend("repair_diagnose", { workspace: repoRoot() });
  const p = r.payload || {};
  if (p.healthy) {
    vscode.window.showInformationMessage("Determinex: oracle passes - nothing to repair.");
  } else {
    vscode.window.showInformationMessage(
      `Determinex diagnosis - lang ${p.language}, ${p.n_failures} failures. Blame: ${JSON.stringify(p.blame)}, proven slop: ${p.proven_slop}.`
    );
  }
}

async function governanceStatus() {
  const r = await callBackend("get_governance_status", {});
  const p = r.payload || {};
  vscode.window.showInformationMessage(
    `Determinex governance: no-overclaim invariant ${p.all_closed ? "HOLDS" : "VIOLATED"} (${(p.violations || []).length} violations across ${Object.keys(p.authority_anchors || {}).length} anchors).`
  );
}

export function activate(context: vscode.ExtensionContext) {
  context.subscriptions.push(
    vscode.commands.registerCommand("determinex.buildFromIdea", buildFromIdea),
    vscode.commands.registerCommand("determinex.previewIdeaOracle", previewIdeaOracle),
    vscode.commands.registerCommand("determinex.repairDiagnose", repairDiagnose),
    vscode.commands.registerCommand("determinex.governanceStatus", governanceStatus)
  );
}

export function deactivate() {}
