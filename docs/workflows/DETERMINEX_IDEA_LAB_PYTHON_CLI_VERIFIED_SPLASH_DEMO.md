# Determinex Idea Lab Python CLI Verified Splash Demo

Lock: `DETERMINEX_IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_LOCK_001`

This lock executes the first narrow Idea Lab splash path: a beginner-style idea becomes a Python CLI/file-data fixture demo, then Determinex records build/test and smoke evidence before allowing the scoped verified-local-app status.

## Scope

The demo workspace is:

`assurance/demo_workspaces/idea_lab_python_cli_verified_splash_demo/run_20260529`

It is a fixture/demo-local root only. It is not an existing user source repository, and it does not grant source mutation authority.

## Verifier Gates

- Build verifier: `python -m compileall -q src`
- Acceptance verifier: `python -m pytest tests -q`
- Smoke verifier: `python -m splash_tool --input tests/fixtures/sample_input.csv --output .tmp/smoke_output.csv`

The demo may only report `VERIFIED_WORKING_LOCAL_APP` for this Python CLI/file-data fixture when build, acceptance, and smoke evidence pass.

## Blocked Paths

- A working-app claim before smoke evidence remains blocked.
- The broad claim "all apps in any language" remains blocked.
- Output writes outside the demo project root are blocked by the CLI.

## Boundary

This does not prove all apps, any language, all codebases, production-ready arbitrary app creation, mobile support, enterprise readiness, or training eligibility.

