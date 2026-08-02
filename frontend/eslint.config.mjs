import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";
import determinex from "./eslint-rules/index.mjs";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    ".next/**",
    "out/**",
    "build/**",
    "src-tauri/target/**",
    "next-env.d.ts",
    // "out/**" only matches a top-level out/ dir; vscode-extension/ has its
    // own compiled-JS out/ (tsc build output, not source) that was getting
    // linted as if it were hand-written TypeScript -- 3 require()-import
    // errors that were never real bugs, just compiled CommonJS output.
    "vscode-extension/out/**",
    // A DOWNLOADED VS Code build (@vscode/test-electron fetches an entire archive here to
    // run extension tests). Linting it walks thousands of bundled files and ends in
    // "FATAL ERROR: Ineffective mark-compacts near heap limit - JavaScript heap out of
    // memory", so `npx eslint .` could not complete locally at all -- only in CI, where the
    // directory does not exist. Not our code, and not lintable.
    "vscode-extension/.vscode-test/**",
  ]),
  {
    rules: {
      "@typescript-eslint/no-explicit-any": "off",
      "react-hooks/purity": "off",
      "react-hooks/set-state-in-effect": "off",
    },
  },
  // Determinex-local rules. See eslint-rules/voidCommands.mjs for why this one
  // exists -- it is the mechanical half of a defect class that hand-auditing
  // demonstrably failed to close.
  {
    files: ["src/**/*.{ts,tsx}"],
    plugins: { determinex },
    rules: {
      "determinex/no-invokesafe-on-void-command": "error",
    },
  },
]);

export default eslintConfig;
