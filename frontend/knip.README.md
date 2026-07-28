# knip configuration notes

`npm run knip` reports unused files, exports and dependencies. Two entries in
`knip.json`'s `ignore` list are deliberate and must not be "cleaned up":

- **`src/lib/ide-panel-bindings.ts`** — unreferenced from TypeScript, but pinned by
  `scripts/ide/systematic_ide_user_audit.py:277`, which reads this file to check
  that each repair panel calls the command it claims to. Deleting it breaks that
  audit, not just a lint rule.
- **`src/lib/ide-invoke-client.ts`** — same lane. It carries
  `FRONTEND_COMMAND_INVOKE_CLIENT_LOCK_001` and has archived evidence under
  `assurance/evidence/frontend_command_invoke_client/`.

Everything else knip reports is a genuine backlog, tracked in
`docs/audits/` rather than silenced here. Adding an ignore to make the
report green is the same mistake as a collection cap that makes a test suite look
complete.
