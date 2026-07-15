# Red Team Plan

Determinex red-team tests focus on untrusted content becoming instructions.

## Surfaces

- browser pages
- PDFs and screenshots
- repository README/issues/tests
- tool output and compiler errors
- package manifests
- corpus source

## Required Test Families

- prompt injection in browser content
- prompt injection in repository documentation
- malicious build hooks
- poisoned corpus rows
- fake verifier output
- cloud egress with secrets
- unsafe action requests hidden inside task text

Passing red-team tests are evidence, not decoration. Failed red-team cases must
be converted into signed refusal or repair corpus rows.
