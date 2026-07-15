# register_models.ps1 — Windows helper to register Determinex DSL models in Ollama
# Usage: .\register_models.ps1
# Requires: Ollama running, DETERMINEX_MODELS_DIR set in .env or as env var

param(
    [string]$ModelsDir = $env:DETERMINEX_MODELS_DIR
)

if (-not $ModelsDir) {
    # Try loading from .env
    $envFile = Join-Path $PSScriptRoot ".env"
    if (Test-Path $envFile) {
        Get-Content $envFile | ForEach-Object {
            if ($_ -match "^DETERMINEX_MODELS_DIR=(.+)$") {
                $ModelsDir = $Matches[1].Trim()
            }
        }
    }
}

if (-not $ModelsDir) {
    Write-Error "DETERMINEX_MODELS_DIR is not set. Set it in .env or pass -ModelsDir 'T:/determinex-models'"
    exit 1
}

Write-Host "[DETERMINEX] Using DETERMINEX_MODELS_DIR = $ModelsDir" -ForegroundColor Cyan

$models = @(
    @{
        Tag      = "determinex-engineer-v11-dsl"
        GgufPath = "$ModelsDir/versions/engineer/v11-dsl/determinex-engineer-v11-dsl.gguf"
        NumCtx   = 4096
        Role     = "Builder (Qwen2.5-Coder-1.5B, DSL v11)"
    },
    @{
        Tag      = "determinex-observer-v6-dsl"
        GgufPath = "$ModelsDir/versions/observer/v6-dsl/determinex-observer-v6-dsl.gguf"
        NumCtx   = 4096
        Role     = "Monitor (Qwen2.5-3B, DSL v6) — oracle/architect use sentinel"
    },
    @{
        Tag      = "determinex-sentinel-v5-dsl"
        GgufPath = "$ModelsDir/versions/sentinel/v5-dsl/determinex-sentinel-v5-dsl.gguf"
        NumCtx   = 4096
        Role     = "Architect / Oracle (Mistral-7B, DSL v5)"
    }
)

foreach ($m in $models) {
    Write-Host "`n[DETERMINEX] Checking: $($m.Tag) — $($m.Role)" -ForegroundColor Yellow

    # Check if already registered
    $list = ollama list 2>&1
    if ($list -match [regex]::Escape($m.Tag)) {
        Write-Host "  Already registered — skipping." -ForegroundColor Green
        continue
    }

    # Check GGUF exists
    if (-not (Test-Path $m.GgufPath)) {
        Write-Warning "  GGUF not found at: $($m.GgufPath)"
        Write-Warning "  Run the RunPod training pipeline first, then re-run this script."
        continue
    }

    # Write temp Modelfile
    $tmpFile = [System.IO.Path]::GetTempFileName() + ".txt"
    $content = "FROM $($m.GgufPath)`nPARAMETER num_ctx $($m.NumCtx)`nPARAMETER temperature 0`n"
    Set-Content -Path $tmpFile -Value $content -Encoding UTF8

    Write-Host "  Registering from $($m.GgufPath) ..." -ForegroundColor White
    $result = ollama create $m.Tag -f $tmpFile 2>&1
    Remove-Item $tmpFile -Force -ErrorAction SilentlyContinue

    if ($LASTEXITCODE -eq 0) {
        Write-Host "  Registered: $($m.Tag)" -ForegroundColor Green
    } else {
        Write-Warning "  Registration failed: $result"
    }
}

Write-Host "`n[DETERMINEX] Model registration complete." -ForegroundColor Cyan
Write-Host "Verify with: ollama list" -ForegroundColor Cyan
