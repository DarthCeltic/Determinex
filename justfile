# Determinex — task runner
# Install: https://just.systems (cargo install just, brew install just, scoop install just)
# Usage:   just <recipe>

# Default — show available recipes
default:
    @just --list

# ── Environment check ──────────────────────────────────────────────────────────

# Run the full environment health check
doctor:
    python scripts/determinex_doctor.py

# Show resolved configuration and safety flags
config:
    determinex config show

# ── Testing ────────────────────────────────────────────────────────────────────

# Run the full test suite (fast — excludes integration and slow markers)
test:
    python -m pytest tests/ -q --tb=short -m "not integration and not slow"

# Run tests with coverage report (requires pytest-cov)
test-cov:
    python -m pytest tests/ -q --tb=short -m "not integration and not slow" \
        --cov=scripts --cov-report=term-missing --cov-fail-under=30

# Run only the settings + CLI tests (quick sanity check)
test-quick:
    python -m pytest tests/test_settings.py tests/test_determinex_cli.py tests/test_doctor.py -q

# Run the Compiler Oracle limits test (6 Rust levels)
limits:
    python scripts/determinex_limits_test.py

# ── Evidence ───────────────────────────────────────────────────────────────────

# Validate the evidence index (read-only, no mutations)
evidence:
    determinex evidence validate

# Render the EVIDENCE_INDEX.md from lock manifests
evidence-render:
    determinex evidence render

# ── Linting ────────────────────────────────────────────────────────────────────

# Run ruff linter and formatter check
lint:
    ruff check scripts/ *.py
    ruff format --check scripts/ *.py

# Run ruff with auto-fix
lint-fix:
    ruff check --fix scripts/ *.py
    ruff format scripts/ *.py

# Run pre-commit hooks on all files
precommit:
    pre-commit run --all-files

# ── Security ───────────────────────────────────────────────────────────────────

# Run pip-audit to check for known vulnerabilities in dependencies
audit:
    pip-audit --desc

# Run pip-audit via uv (works without local pip-audit install)
audit-uv:
    uv run pip-audit --desc

# Verify cloak audit log (requires DETERMINEX_CLOAK_AUDIT=1 run first)
cloak-verify:
    python scripts/verify_cloak.py

# ── Status ─────────────────────────────────────────────────────────────────────

# Show last pipeline session events
status:
    python scripts/determinex_status.py --last-run

# Live tail the event log
tail:
    python scripts/determinex_status.py --tail

# ── Doc integrity guards ───────────────────────────────────────────────────────

# Scan docs for mojibake (fail on any found) + verify PB lock count consistency
doc-guard:
    python scripts/fix_mojibake.py --scan
    python scripts/pb_doc_count_check.py

# ── All-in-one quality gate ────────────────────────────────────────────────────

# Full pre-push quality gate: lint + test + evidence + config check + doc guard
all: lint test evidence config doc-guard
    @echo "Quality gate PASSED"
