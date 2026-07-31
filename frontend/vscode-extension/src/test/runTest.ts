/**
 * Launch a REAL VS Code extension host and run the suite inside it.
 *
 * This exists to establish `activation_event_smoke_passed`, the one field of the
 * `extension_compat` release gate that cannot be established by reading files. The other four are
 * statements about the manifest and the source; this one is a statement about VS Code's runtime
 * behaviour -- specifically that `activationEvents: []` still activates the extension when a
 * contributed command is invoked, via the implicit `onCommand:` events VS Code synthesises from
 * `contributes.commands`. Nothing short of an extension host can answer that.
 *
 * @vscode/test-electron downloads a real VS Code, so this is the product being exercised, not a
 * mock of it.
 */
import * as path from "path";

import { runTests } from "@vscode/test-electron";

/**
 * `ELECTRON_RUN_AS_NODE` makes any Electron binary -- including VS Code's own Code.exe -- behave
 * as plain Node. VS Code sets it for the processes it spawns, so it is present in the environment
 * of anything launched from a VS Code integrated terminal, task, or extension host, and child
 * processes inherit it.
 *
 * The failure it produces is genuinely confusing and cost real time to diagnose: the download
 * succeeds, Code.exe reports `ProductName: Visual Studio Code` and `FileVersion: 1.131.0`, and
 * then `Code.exe --version` prints `v24.18.0` -- Node's version -- and every launch flag comes
 * back as `Code.exe: bad option: --disable-extensions`, which is Node's error format, not VS
 * Code's. It reads like a corrupt download of the wrong binary.
 *
 * Cleared here rather than in a shell wrapper, because running extension tests from the VS Code
 * terminal is the normal thing to do and the harness should just work there.
 */
function clearElectronRunAsNode(): void {
  if (process.env.ELECTRON_RUN_AS_NODE !== undefined) {
    console.log("  (clearing inherited ELECTRON_RUN_AS_NODE so Code.exe runs as VS Code, not Node)");
    delete process.env.ELECTRON_RUN_AS_NODE;
  }
}

async function main(): Promise<void> {
  clearElectronRunAsNode();

  // __dirname is out/test at runtime, so two levels up is the extension root.
  const extensionDevelopmentPath = path.resolve(__dirname, "../../");
  const extensionTestsPath = path.resolve(__dirname, "./suite/index");

  try {
    await runTests({
      extensionDevelopmentPath,
      extensionTestsPath,
      // No folder is opened on purpose: the extension's repoRoot() falls back to process.cwd(),
      // and opening the checkout would let a configuration write land in the repo's .vscode/.
      // Activation is what is under test, not the Python backend -- which is verified separately
      // and directly through scripts/ide/determinex_backend_cli.py.
      launchArgs: [
        "--disable-extensions", // other extensions only; the one under development still loads
        "--disable-gpu",
        "--disable-workspace-trust",
      ],
    });
  } catch (err) {
    console.error("extension-host test run failed:", err);
    process.exit(1);
  }
}

void main();
