#!/usr/bin/env pwsh
# Determinex ProgramBench VS Code Extension Installer
# Only installs extensions NOT already present — safe to re-run.

# Capture current installed extensions
code --list-extensions > installed.txt
$installed = Get-Content installed.txt

function Install-Extension {
    param([string]$id, [string]$label)
    if ($installed -contains $id) {
        Write-Host "  SKIP (already installed): $id" -ForegroundColor DarkGray
    } else {
        Write-Host "  INSTALLING: $id" -ForegroundColor Cyan
        code --install-extension $id --force
    }
}

# ── CRITICAL: Rust (100 tools, 50% of surface) ─────────────────────────────
Write-Host "`nCRITICAL — Rust Support (100 tools)" -ForegroundColor Yellow
Install-Extension "rust-lang.rust-analyzer" "Rust Analyzer"
Install-Extension "tamasfe.even-better-toml" "Even Better TOML (Cargo.toml)"

# ── CRITICAL: Go (44 tools, 22% of surface) ────────────────────────────────
Write-Host "`nCRITICAL — Go Support (44 tools)" -ForegroundColor Yellow
Install-Extension "golang.go" "Go Language Server (gopls)"

# ── CRITICAL: Shell / compile.sh (196 compile.sh files) ───────────────────
Write-Host "`nCRITICAL — Shell Script Support (all compile.sh files)" -ForegroundColor Yellow
Install-Extension "timonwong.shellcheck" "ShellCheck Linter"
Install-Extension "foxundermoon.shell-format" "Shell Format"

# ── HIGH: C/C++ Build (37 tools, cmake for jq/doxygen/cmatrix) ────────────
Write-Host "`nHIGH — C/C++ & CMake Support (37 tools)" -ForegroundColor Green
Install-Extension "ms-vscode.cmake-tools" "CMake Tools"
# ms-vscode.cpptools already installed — skip

# ── HIGH: Error Lens (inline diagnostics for ShellCheck + rust-analyzer) ───
Write-Host "`nHIGH — Inline Diagnostics" -ForegroundColor Green
Install-Extension "usernamehw.errorlens" "Error Lens"

# ── HIGH: Python Test Adapter (pytest eval reports) ────────────────────────
Write-Host "`nHIGH — Python Test Explorer" -ForegroundColor Green
Install-Extension "LittleFoxTeam.vscode-python-test-adapter" "Python Test Adapter"

# ── MEDIUM: Hex Editor (tarball CRLF diagnosis) ────────────────────────────
Write-Host "`nMEDIUM — Binary / Hex" -ForegroundColor Cyan
Install-Extension "ms-vscode.hexeditor" "Hex Editor"

# ── MEDIUM: Git Graph (campaign history visualization) ─────────────────────
Write-Host "`nMEDIUM — Git" -ForegroundColor Cyan
Install-Extension "mhutchie.git-graph" "Git Graph"

# ── Final count ────────────────────────────────────────────────────────────
Write-Host "`n── Final Extension Count ──" -ForegroundColor White
code --list-extensions | Measure-Object -Line
Write-Host "Done. Restart VS Code to activate all extensions." -ForegroundColor Green
