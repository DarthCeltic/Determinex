/**
 * Runs inside a real VS Code extension host.
 *
 * `extension_compat` requires five fields. Four are statements about files -- the contract exists,
 * the VSIX imports, the Open VSX metadata parses, the extension declares no `capabilities` and
 * spawns a fixed argv. `activation_event_smoke_passed` is different in kind: it is a claim about
 * VS Code's runtime behaviour, and until now it was the field I could not establish, so the gate
 * stayed deferred.
 *
 * The specific thing worth verifying: `package.json` declares `"activationEvents": []`. That is
 * only correct because VS Code >= 1.74 synthesises implicit `onCommand:` activation events from
 * `contributes.commands`. If that assumption were wrong -- or if a future manifest edit broke the
 * link between a contributed command and its handler -- every command would silently do nothing,
 * and no file-reading check would notice.
 */
import * as assert from "assert";

import * as vscode from "vscode";

const EXTENSION_ID = "darthceltic.determinex";

/** Every command in contributes.commands. Kept explicit so a manifest edit that drops one fails. */
const CONTRIBUTED_COMMANDS = [
  "determinex.buildFromIdea",
  "determinex.previewIdeaOracle",
  "determinex.repairDiagnose",
  "determinex.governanceStatus",
];

suite("Determinex extension in a real extension host", () => {
  test("the extension is loaded under its published identity", () => {
    const ext = vscode.extensions.getExtension(EXTENSION_ID);
    assert.ok(
      ext,
      `no extension with id ${EXTENSION_ID}. A publisher/name change in package.json breaks ` +
        "every marketplace update path, and this ran green once while the VSIX still identified " +
        "itself as lunarian-data-systems.citadel."
    );
  });

  test("the manifest still relies on implicit activation, which is what makes the next test load-bearing", () => {
    const ext = vscode.extensions.getExtension(EXTENSION_ID);
    assert.ok(ext);
    const declared = (ext.packageJSON.activationEvents ?? []) as string[];
    assert.deepStrictEqual(
      declared,
      [],
      "activationEvents is no longer empty; if an explicit event was added, the implicit " +
        "onCommand path below is no longer the mechanism in play and this suite should say so"
    );
  });

  // THIS TEST MUST COME FIRST of the two below.
  //
  // The activation transition can only be observed once per host, and observing it is the whole
  // point -- so nothing that might activate the extension may run before it. Ordering discovered
  // the honest way: the registry assertion was originally first and failed with all four commands
  // absent, which is CORRECT VS Code behaviour. Contributed commands are not in the command
  // registry until the extension activates and calls registerCommand; the command palette routes
  // them from the manifest, and `executeCommand` on one triggers the implicit activation. That
  // failure was the mechanism proving itself.
  test("invoking a contributed command activates the extension", async () => {
    const ext = vscode.extensions.getExtension(EXTENSION_ID);
    assert.ok(ext);

    const wasActiveBefore = ext.isActive;
    const registeredBefore = await vscode.commands.getCommands(true);
    const presentBefore = CONTRIBUTED_COMMANDS.filter((c) => registeredBefore.includes(c));

    try {
      await vscode.commands.executeCommand("determinex.governanceStatus");
    } catch (err) {
      // The command body shells out to the Python backend, which is not provisioned in this host.
      // Its failure is expected and irrelevant: activation happens before the handler runs, and
      // activation is the claim under test. The backend itself is verified directly against
      // scripts/ide/determinex_backend_cli.py, not through the editor.
      console.log(`  (command body failed as expected without a backend: ${String(err)})`);
    }

    assert.strictEqual(
      ext.isActive,
      true,
      "executing a contributed command did not activate the extension — with " +
        "activationEvents: [] that means the implicit onCommand activation is not firing, and " +
        "every command would silently do nothing"
    );
    // Recorded rather than asserted: if something else had already activated the extension the
    // transition would not be observable, and claiming to have observed it would be exactly the
    // overclaim this exercise exists to avoid.
    console.log(
      `  activation observed as a transition: ${!wasActiveBefore}` +
        ` (active before invocation: ${wasActiveBefore};` +
        ` contributed commands in registry before: ${presentBefore.length}/${CONTRIBUTED_COMMANDS.length})`
    );
  });

  test("all four contributed commands are registered once the extension is active", async () => {
    const ext = vscode.extensions.getExtension(EXTENSION_ID);
    assert.ok(ext);
    // Explicit activate() so this does not silently depend on the test above having run.
    await ext.activate();

    const registered = await vscode.commands.getCommands(true);
    const missing = CONTRIBUTED_COMMANDS.filter((c) => !registered.includes(c));
    assert.deepStrictEqual(
      missing,
      [],
      `contributed commands absent from the registry after activation: ${missing.join(", ")}. ` +
        "A manifest entry whose handler is never registered is a command that appears in the " +
        "palette and does nothing."
    );
  });

  test("the extension contributes no capabilities, so the sandbox claim is checkable here too", () => {
    const ext = vscode.extensions.getExtension(EXTENSION_ID);
    assert.ok(ext);
    assert.strictEqual(
      ext.packageJSON.capabilities,
      undefined,
      "the extension now declares capabilities; sandbox_permissions_enforced in the " +
        "extension_compat packet asserts it declares none"
    );
  });
});
