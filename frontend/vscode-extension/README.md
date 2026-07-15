# Determinex VS Code Extension

The brain in the editor you already use. Four commands, each delegating to the
ONE governed backend (`scripts/ide/determinex_backend_cli.py` -> Tauri bridge ->
command surface -> canonical engine). VS Code is the editor; Determinex is the
brain; the oracle judges everything any AI produces.

- **Determinex: Build From Idea** - describe it, get an oracle-verified program.
- **Determinex: Preview the Sound Oracle** - see the tests your idea will be verified against.
- **Determinex: Diagnose This Repo** - blame (CODE/ENVIRONMENT/TEST) + proven-slop.
- **Determinex: Governance Status** - the no-overclaim invariant.

## Build

```
cd frontend/vscode-extension
npm install
npm run compile     # tsc -> out/extension.js
npm run package     # vsce package -> .vsix   (needs @vscode/vsce)
```

Use `determinex.pythonPath`, `determinex.repoRoot`, and `determinex.model` if the
defaults do not resolve. The old `determinex.*` keys remain compatibility aliases.

Status: scaffold complete and wired to the verified backend CLI. Packaging needs
Node + `@vscode/vsce` + VS Code.
