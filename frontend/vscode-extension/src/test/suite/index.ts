/**
 * Mocha entry point, executed INSIDE the extension host by @vscode/test-electron.
 *
 * Discovers test files with fs rather than glob: glob v11 is ESM-only and this bundle is
 * commonjs, so requiring it here would fail at runtime for no benefit -- there is exactly one
 * directory to scan.
 */
import * as fs from "fs";
import * as path from "path";

// This bundle is emitted as CommonJS and loaded by the VS Code extension host, which is a
// CJS runtime. `import Mocha from "mocha"` compiles to an interop wrapper that resolves to a
// namespace object here, so `new Mocha(...)` below throws "is not a constructor" at run
// time. The import-equals form is the documented TypeScript spelling for exactly this case.
// The directive has to sit on the line IMMEDIATELY above the statement -- with the
// explanation in between, it applied to the next comment line and the error stood.
// eslint-disable-next-line @typescript-eslint/no-require-imports
import Mocha = require("mocha");

export function run(): Promise<void> {
  const mocha = new Mocha({ ui: "tdd", color: true, timeout: 60_000 });
  const testsRoot = __dirname;

  for (const entry of fs.readdirSync(testsRoot)) {
    if (entry.endsWith(".test.js")) {
      mocha.addFile(path.resolve(testsRoot, entry));
    }
  }

  return new Promise((resolve, reject) => {
    try {
      mocha.run((failures) => {
        if (failures > 0) {
          reject(new Error(`${failures} test(s) failed in the extension host`));
        } else {
          resolve();
        }
      });
    } catch (err) {
      reject(err);
    }
  });
}
